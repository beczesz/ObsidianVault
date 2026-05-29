#!/usr/bin/env python3
"""
marketing_board_refresh.py — Debounced marketing board sidecar regenerator
==========================================================================
Wraps scan_marketing_board.py with a file-based debounce lock so that rapid
successive calls (e.g. multiple FS events in a burst) collapse into a single
regen. Called from two sources:

  Primary:   watch_event.py — MarketingBoardHook fires after a seed or
             publication file changes (instant, event-driven).
  Safety net: BDOS scheduler — marketing-board-sidecar-refresh job fires
             every 5 minutes as a backstop if the watchdog misses an event.

Debounce:
  A lock file at cache/mktboard_refresh.lock stores the epoch of the last
  completed regen. If a call arrives within DEBOUNCE_SEC of the last-completed
  regen, it exits immediately (no-op). If a regen is already in progress
  (lock file mtime < DEBOUNCE_SEC ago), it also exits.

  This is a single-process filesystem lock — safe because both callers
  run in the same OS user context on the same machine.

Usage:
  python3 marketing_board_refresh.py [--force] [--dry-run]

Flags:
  --force    Bypass debounce (useful for manual one-shot regeneration).
  --dry-run  Pass --dry-run through to scan_marketing_board.py; no file written.

Exit codes:
  0  regen completed (or dry-run completed)
  2  skipped (debounce: already ran recently or regen in progress)
  1  regen failed
"""

from __future__ import annotations

import argparse
import hashlib
import os
import subprocess
import sys
import time
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
_HERE = Path(__file__).resolve().parent
LOCK_FILE    = _HERE / 'cache' / 'mktboard_refresh.lock'
SCAN_SCRIPT  = _HERE / 'scan_marketing_board.py'
LOG_FILE     = _HERE / 'cache' / 'mktboard_refresh.log'
# Output sidecar the scan rewrites; we hash it before/after to detect real change.
BOARD_JSON   = _HERE.parents[3] / '_dashboards' / '_design' / 'marketing_board.json'

DEBOUNCE_SEC = 5.0   # seconds: skip if last regen was within this window


def _board_hash() -> str:
    """Content hash of the board sidecar EXCLUDING volatile fields.

    The sidecar carries a `generated_at` timestamp that changes on every scan,
    so a raw byte hash would always differ and defeat change-detection. We hash
    the meaningful content (lanes/tasks/calendar) with `generated_at` removed.
    """
    try:
        import json
        data = json.loads(BOARD_JSON.read_text(encoding='utf-8'))
        if isinstance(data, dict):
            data.pop('generated_at', None)
        canonical = json.dumps(data, sort_keys=True, ensure_ascii=False)
        return hashlib.sha256(canonical.encode('utf-8')).hexdigest()
    except (OSError, ValueError):
        return ''

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------
def _log(msg: str) -> None:
    ts = time.strftime('%Y-%m-%d %H:%M:%S')
    line = f'[{ts}] {msg}'
    print(line, flush=True)
    try:
        with open(LOG_FILE, 'a', encoding='utf-8') as f:
            f.write(line + '\n')
    except OSError:
        pass


def _agent_log(event_type: str, message: str, status: str | None = None,
               duration_ms: int | None = None, tags: list[str] | None = None) -> None:
    """Emit a structured event to agent_observability.db (best-effort)."""
    try:
        sys.path.insert(0, str(_HERE))
        from agent_log import log_event
        log_event(
            agent_name='presto',
            mode='marketing-board-refresh',
            event_type=event_type,
            message=message,
            log_level='info',
            status=status,
            duration_ms=duration_ms,
            tags=(tags or []) + ['marketing-board'],
            refresh_sidecar=True,
        )
    except Exception as exc:
        _log(f'[agent_log] Could not write to observability DB: {exc}')


# ---------------------------------------------------------------------------
# Debounce helpers
# ---------------------------------------------------------------------------
def _last_completed_at() -> float:
    """Return epoch of the last completed regen (from lock file), or 0."""
    try:
        if LOCK_FILE.exists():
            return float(LOCK_FILE.read_text().strip())
    except Exception:
        pass
    return 0.0


def _mark_in_progress() -> None:
    """Write a sentinel value indicating regen is running."""
    LOCK_FILE.parent.mkdir(parents=True, exist_ok=True)
    # Use a negative epoch as "in-progress" sentinel; actual epoch on complete.
    LOCK_FILE.write_text('in-progress')


def _mark_complete(start_epoch: float) -> None:
    """Write the epoch when regen finished."""
    LOCK_FILE.write_text(str(start_epoch))


def _is_in_progress() -> bool:
    """True if a regen is currently running (based on lock file content)."""
    try:
        if LOCK_FILE.exists():
            content = LOCK_FILE.read_text().strip()
            if content == 'in-progress':
                # Treat as stale if lock file mtime > 120s ago
                age = time.time() - LOCK_FILE.stat().st_mtime
                return age < 120.0
    except Exception:
        pass
    return False


# ---------------------------------------------------------------------------
# Core regen
# ---------------------------------------------------------------------------
def run_regen(force: bool = False, dry_run: bool = False) -> int:
    """
    Attempt a marketing board regen.

    Returns:
      0  completed
      2  skipped (debounce)
      1  failed
    """
    now = time.time()

    if not force:
        if _is_in_progress():
            _log('[mktboard-refresh] Skipped — regen already in progress.')
            return 2
        last = _last_completed_at()
        if last > 0 and (now - last) < DEBOUNCE_SEC:
            _log(f'[mktboard-refresh] Skipped — last regen was {now - last:.1f}s ago '
                 f'(debounce={DEBOUNCE_SEC}s).')
            return 2

    _log('[mktboard-refresh] Starting sidecar regeneration...')
    # No agent_logs row for the start of a routine refresh — it is not a
    # meaningful activity event. We only log to agent_logs below IF the board
    # content actually changed (dashboard_update) or the scan failed (error).
    hash_before = _board_hash()

    _mark_in_progress()
    t0 = time.perf_counter()

    cmd = [sys.executable, str(SCAN_SCRIPT)]
    if dry_run:
        cmd.append('--dry-run')

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        duration_ms = int((time.perf_counter() - t0) * 1000)

        if result.returncode == 0:
            _mark_complete(time.time())
            stdout_tail = (result.stdout + result.stderr)[-500:]
            _log(f'[mktboard-refresh] Done in {duration_ms}ms. {stdout_tail.strip()}')
            # Only emit a meaningful event when the board content actually changed.
            # No-op refreshes (the common case on the 5-min safety-net) write nothing.
            if _board_hash() != hash_before:
                _agent_log('dashboard_update',
                           f'Marketing board sidecar updated in {duration_ms}ms',
                           status='success', duration_ms=duration_ms,
                           tags=['manual'] if force else [])
            return 0
        else:
            err = (result.stderr or result.stdout)[-500:]
            _log(f'[mktboard-refresh] scan_marketing_board.py failed '
                 f'(exit {result.returncode}): {err}')
            _agent_log('error',
                       f'Marketing board sidecar refresh failed: {err[:200]}',
                       status='failure', duration_ms=duration_ms,
                       tags=['scheduler'])
            # Clear the in-progress lock so next call can retry
            try:
                LOCK_FILE.unlink()
            except OSError:
                pass
            return 1

    except subprocess.TimeoutExpired:
        duration_ms = int((time.perf_counter() - t0) * 1000)
        _log('[mktboard-refresh] Timeout (60s) — regen killed.')
        _agent_log('error', 'Marketing board refresh timed out after 60s',
                   status='failure', duration_ms=duration_ms)
        try:
            LOCK_FILE.unlink()
        except OSError:
            pass
        return 1

    except Exception as exc:
        duration_ms = int((time.perf_counter() - t0) * 1000)
        _log(f'[mktboard-refresh] Unexpected error: {exc}')
        _agent_log('error', f'Marketing board refresh unexpected error: {exc}',
                   status='failure', duration_ms=duration_ms)
        try:
            LOCK_FILE.unlink()
        except OSError:
            pass
        return 1


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Debounced marketing board sidecar regenerator')
    parser.add_argument('--force', action='store_true',
                        help='Bypass debounce and run unconditionally')
    parser.add_argument('--dry-run', action='store_true',
                        help='Pass --dry-run to scan_marketing_board.py (no file written)')
    args = parser.parse_args()

    sys.exit(run_regen(force=args.force, dry_run=args.dry_run))
