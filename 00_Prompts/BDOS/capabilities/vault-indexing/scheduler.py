#!/usr/bin/env python3
"""
scheduler.py — BDOS Job Scheduler  (Phase B-redux, 2026-05-24)
==============================================================
Reads scheduled_jobs from agent_observability.db, acquires per-job locks
atomically (via job_runs rows), dispatches commands as subprocesses, and
records every run in job_runs.  Designed to be embedded as a daemon thread
in events_server.py but can also be tested standalone.

Architecture
------------
- Lock: each dispatch inserts a job_runs row with status='running' and
  claimed_by_device / claimed_at / lock_until set.  The atomic lock-acquire
  UPDATE queries job_runs for any running row whose lock_until < now, NOT
  scheduled_jobs.  Lock fields live on job_runs (a run is locked, not the
  job definition).
- Dispatch: subprocess.Popen (non-blocking), stdout/stderr captured to
  temp files, tail written to job_runs on finish.
- Logging: every meaningful event emitted via agent_log.log_event()
  → agent_logs table (tags=['scheduler']).
- Schedule evaluation:
    daily   — runs if UTC hour matches schedule_hour and last_run_at is
              not today (UTC).
    weekly  — runs if weekday (Mon=0) and hour match and last_run_at is
              not this week.
    interval — runs if (now - last_run_at) >= interval_seconds.
    manual  — never auto-runs (requires explicit trigger).

Column vocabulary (brief-aligned, schema v1.4):
  scheduled_jobs : job_id, job_name, agent_name, description,
                   schedule_type, schedule_hour, schedule_minute,
                   schedule_weekday, interval_seconds, command,
                   requires_approval, lock_duration_s, enabled,
                   last_run_at, next_run_at, created_at, updated_at

  job_runs       : id, job_id, run_id, job_name, agent_name,
                   schedule_type, scheduled_for, last_run_at, next_run_at,
                   status (9 states), claimed_by_device, claimed_at,
                   lock_until, completed_at, failed_at, duration_ms,
                   result_summary, error_message, metadata_json, created_at

Usage
-----
  # Standalone test (one scan then exit)
  python3 scheduler.py --once

  # Standalone loop (60-second interval)
  python3 scheduler.py --loop

  # From events_server.py (preferred):
  from scheduler import scheduler_loop
  t = threading.Thread(target=scheduler_loop, daemon=True, name='scheduler')
  t.start()
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import threading
import time
import uuid
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Optional

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
_HERE = Path(__file__).resolve().parent
_CACHE = _HERE / 'cache'
DB_PATH = _CACHE / 'agent_observability.db'
DEVICE_ID_FILE = Path.home() / '.bdos' / 'device_id'

SCAN_INTERVAL_S = 60            # How often the scheduler scans for due jobs
DEFAULT_LOCK_DURATION_S = 600   # 10 minutes (per-job override via lock_duration_s column)

# ---------------------------------------------------------------------------
# Import agent_log after path is known
# ---------------------------------------------------------------------------
sys.path.insert(0, str(_HERE))
import sqlite3  # noqa: E402 (stdlib)
from agent_log import log_event  # noqa: E402


# ---------------------------------------------------------------------------
# Device ID
# ---------------------------------------------------------------------------
def get_device_id() -> str:
    """Return stable device ID from ~/.bdos/device_id, creating if absent."""
    try:
        p = DEVICE_ID_FILE
        p.parent.mkdir(parents=True, exist_ok=True)
        if p.exists():
            did = p.read_text().strip()
            if did:
                return did
        did = str(uuid.uuid4())
        p.write_text(did)
        return did
    except Exception:
        return 'unknown-device'


_DEVICE_ID = get_device_id()


# ---------------------------------------------------------------------------
# DB helpers
# ---------------------------------------------------------------------------
def _db() -> sqlite3.Connection:
    con = sqlite3.connect(str(DB_PATH), timeout=15)
    con.row_factory = sqlite3.Row
    con.execute('PRAGMA journal_mode=WAL')
    con.execute('PRAGMA foreign_keys=ON')
    return con


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


def _iso_to_dt(s: Optional[str]) -> Optional[datetime]:
    if not s:
        return None
    try:
        return datetime.fromisoformat(s.replace('Z', '+00:00'))
    except ValueError:
        return None


# ---------------------------------------------------------------------------
# Scheduler logging helper
# ---------------------------------------------------------------------------
def _log(event_type: str, message: str, *, job_id: Optional[str] = None,
         level: str = 'info', status: Optional[str] = None,
         duration_ms: Optional[int] = None, metadata: Optional[dict] = None):
    """Emit a structured event to agent_logs with tags=['scheduler']."""
    try:
        log_event(
            agent_name='maestro',   # scheduler is an infra concern — log under maestro
            mode='scheduler',
            event_type=event_type,
            message=message,
            log_level=level,
            status=status,
            duration_ms=duration_ms,
            tags=['scheduler'] + ([f'job:{job_id}'] if job_id else []),
            metadata_json=metadata or ({} if job_id else None),
            refresh_sidecar=False,   # avoid N sidecar writes during a scan batch
        )
    except Exception as exc:
        print(f'[scheduler] log_event failed: {exc}', file=sys.stderr)


# ---------------------------------------------------------------------------
# Lock management — locks live on job_runs rows, not on scheduled_jobs
# ---------------------------------------------------------------------------
def _has_active_lock(con: sqlite3.Connection, job_id: str,
                     lock_duration_s: int) -> bool:
    """
    Return True if there is a running job_runs row for this job_id
    whose lock has NOT expired (claimed_at + lock_duration_s >= now).
    """
    now = _now_iso()
    row = con.execute("""
        SELECT run_id FROM job_runs
        WHERE job_id = ?
          AND status = 'running'
          AND claimed_at IS NOT NULL
          AND datetime(claimed_at, '+' || ? || ' seconds') >= datetime(?)
        LIMIT 1
    """, (job_id, lock_duration_s, now)).fetchone()
    return row is not None


def _expire_stale_run_locks(con: sqlite3.Connection) -> int:
    """
    Mark as 'failed' any running job_runs rows whose lock_until < now.
    Returns count of rows transitioned.
    """
    now = _now_iso()
    cur = con.execute("""
        UPDATE job_runs
        SET status = 'failed',
            failed_at = ?,
            error_message = COALESCE(error_message, '') || ' [lock expired — presumed dead]'
        WHERE status = 'running'
          AND lock_until IS NOT NULL
          AND datetime(lock_until) < datetime(?)
    """, (now, now))
    con.commit()
    return cur.rowcount


# ---------------------------------------------------------------------------
# Schedule evaluation
# ---------------------------------------------------------------------------
def _is_due(job: sqlite3.Row) -> bool:
    """Return True if a job is due to run now."""
    now_utc = datetime.now(timezone.utc)
    stype = job['schedule_type']
    last_run = _iso_to_dt(job['last_run_at'])

    if stype == 'manual':
        return False

    if not job['enabled']:
        return False

    if stype == 'interval':
        interval = job['interval_seconds']
        if not interval:
            return False
        if last_run is None:
            return True
        return (now_utc - last_run).total_seconds() >= interval

    if stype == 'daily':
        target_hour = job['schedule_hour']
        target_min  = job['schedule_minute'] or 0
        if target_hour is None:
            return False
        if now_utc.hour != target_hour or abs(now_utc.minute - target_min) > 1:
            return False
        # Already ran today?
        if last_run and last_run.date() >= now_utc.date():
            return False
        return True

    if stype == 'weekly':
        target_weekday = job['schedule_weekday']   # 0=Mon
        target_hour    = job['schedule_hour']
        target_min     = job['schedule_minute'] or 0
        if target_weekday is None or target_hour is None:
            return False
        if now_utc.weekday() != target_weekday:
            return False
        if now_utc.hour != target_hour or abs(now_utc.minute - target_min) > 1:
            return False
        # Already ran this week?
        if last_run:
            week_start = now_utc - timedelta(days=now_utc.weekday())
            week_start = week_start.replace(hour=0, minute=0, second=0, microsecond=0)
            if last_run >= week_start:
                return False
        return True

    return False


def _compute_next_run(job: sqlite3.Row) -> Optional[str]:
    """Compute approximate next_run_at ISO string (best-effort for display)."""
    now_utc = datetime.now(timezone.utc)
    stype = job['schedule_type']

    if stype == 'manual':
        return None

    if stype == 'interval':
        interval = job['interval_seconds'] or 3600
        last_run = _iso_to_dt(job['last_run_at'])
        base = last_run or now_utc
        nxt = base + timedelta(seconds=interval)
        return nxt.strftime('%Y-%m-%dT%H:%M:%SZ')

    if stype == 'daily':
        h = job['schedule_hour'] or 6
        m = job['schedule_minute'] or 0
        candidate = now_utc.replace(hour=h, minute=m, second=0, microsecond=0)
        if candidate <= now_utc:
            candidate += timedelta(days=1)
        return candidate.strftime('%Y-%m-%dT%H:%M:%SZ')

    if stype == 'weekly':
        target_wd  = job['schedule_weekday'] or 0
        h          = job['schedule_hour'] or 6
        m          = job['schedule_minute'] or 0
        days_ahead = (target_wd - now_utc.weekday()) % 7
        if days_ahead == 0:
            days_ahead = 7
        candidate = (now_utc + timedelta(days=days_ahead)).replace(
            hour=h, minute=m, second=0, microsecond=0)
        return candidate.strftime('%Y-%m-%dT%H:%M:%SZ')

    return None


# ---------------------------------------------------------------------------
# Subprocess dispatch
# ---------------------------------------------------------------------------
_active_runs: dict[str, subprocess.Popen] = {}
_active_runs_lock = threading.Lock()


def _dispatch(job: sqlite3.Row):
    """
    Dispatch a job as a subprocess. Non-blocking — reaper thread handles
    finish recording.
    """
    run_id = str(uuid.uuid4())
    now = _now_iso()
    command = job['job_id'] and job['command']
    job_id = job['job_id']
    job_name = job['job_name']
    agent_name = job['agent_name']
    schedule_type = job['schedule_type']
    lock_duration_s = job['lock_duration_s'] or DEFAULT_LOCK_DURATION_S

    # Compute lock_until
    lock_until_dt = datetime.now(timezone.utc) + timedelta(seconds=lock_duration_s)
    lock_until = lock_until_dt.strftime('%Y-%m-%dT%H:%M:%SZ')

    next_run = _compute_next_run(job)

    # Record run as 'running' with lock fields populated
    con = _db()
    try:
        con.execute("""
            INSERT INTO job_runs
              (job_id, run_id, job_name, agent_name, schedule_type,
               scheduled_for, last_run_at, next_run_at,
               status, claimed_by_device, claimed_at, lock_until,
               metadata_json)
            VALUES (?, ?, ?, ?, ?,
                    ?, ?, ?,
                    'running', ?, ?, ?,
                    ?)
        """, (
            job_id, run_id, job_name, agent_name, schedule_type,
            now, job['last_run_at'], next_run,
            _DEVICE_ID, now, lock_until,
            json.dumps({'command': job['command'][:200]}),
        ))

        con.execute("""
            UPDATE scheduled_jobs
            SET last_run_at = ?, next_run_at = ?, updated_at = ?
            WHERE job_id = ?
        """, (now, next_run, now, job_id))
        con.commit()
    finally:
        con.close()

    # The run start is recorded authoritatively in job_runs; we deliberately do
    # NOT write a task_started row to agent_logs (routine dispatch is not a
    # meaningful activity event — it was the bulk of the historical log noise).
    print(f'[scheduler] Dispatching job: {job_id} (run {run_id})', flush=True)

    # Launch subprocess
    try:
        out_fd, out_path = tempfile.mkstemp(prefix=f'bdos_{job_id}_', suffix='.out')
        err_fd, err_path = tempfile.mkstemp(prefix=f'bdos_{job_id}_', suffix='.err')
        proc = subprocess.Popen(
            ['/bin/bash', job['command']] if job['command'].endswith('.sh')
            else job['command'],
            shell=not job['command'].endswith('.sh'),
            stdout=out_fd,
            stderr=err_fd,
            close_fds=True,
        )
        os.close(out_fd)
        os.close(err_fd)

        with _active_runs_lock:
            _active_runs[run_id] = proc

        # Reaper thread
        def _reap():
            start_wall = time.perf_counter()
            proc.wait()
            duration_ms = int((time.perf_counter() - start_wall) * 1000)
            exit_code = proc.returncode
            success = exit_code == 0
            # Convention: exit 2 = benign skip (e.g. debounce no-op), NOT a failure.
            skipped = exit_code == 2
            ok = success or skipped

            def _tail(path: str, max_bytes: int = 2000) -> str:
                try:
                    data = Path(path).read_bytes()
                    return data[-max_bytes:].decode('utf-8', errors='replace')
                except Exception:
                    return ''

            out_tail = _tail(out_path)
            err_tail = _tail(err_path)

            # Cleanup temp files
            for p in (out_path, err_path):
                try:
                    os.unlink(p)
                except OSError:
                    pass

            finish_ts = _now_iso()
            con2 = _db()
            try:
                con2.execute("""
                    UPDATE job_runs
                    SET status       = ?,
                        completed_at = ?,
                        failed_at    = ?,
                        duration_ms  = ?,
                        result_summary = ?,
                        error_message  = ?,
                        metadata_json  = ?
                    WHERE run_id = ?
                """, (
                    'completed' if ok else 'failed',
                    finish_ts if ok else None,
                    None if ok else finish_ts,
                    duration_ms,
                    out_tail,
                    err_tail if not ok else None,
                    json.dumps({'exit_code': exit_code}),
                    run_id,
                ))
                con2.commit()
            finally:
                con2.close()

            with _active_runs_lock:
                _active_runs.pop(run_id, None)

            status_word = 'skipped' if skipped else ('completed' if success else 'failed')
            print(f'[scheduler] Job {job_id} {status_word} (exit {exit_code})', flush=True)
            # Only GENUINE failures reach agent_logs (real signal). Routine success
            # and benign skips (exit 2) are recorded in job_runs, not the activity log.
            if not ok:
                _log('task_completed',
                     f'[scheduler] Job {job_id} failed (exit {exit_code})',
                     job_id=job_id,
                     level='warning',
                     status='failure',
                     duration_ms=duration_ms,
                     metadata={'run_id': run_id, 'exit_code': exit_code})

        t = threading.Thread(target=_reap, daemon=True,
                             name=f'reaper-{job_id[:20]}')
        t.start()

    except Exception as exc:
        _log('error', f'[scheduler] Dispatch failed for {job_id}: {exc}',
             job_id=job_id, level='error', status='failure')
        finish_ts = _now_iso()
        con3 = _db()
        try:
            con3.execute("""
                UPDATE job_runs
                SET status='failed', failed_at=?, error_message=?
                WHERE run_id=?
            """, (finish_ts, str(exc), run_id))
            con3.commit()
        finally:
            con3.close()


# ---------------------------------------------------------------------------
# Skip (record that we skipped)
# ---------------------------------------------------------------------------
def _record_skip(job_id: str, reason: str, job: Optional[sqlite3.Row] = None):
    run_id = str(uuid.uuid4())
    now = _now_iso()
    con = _db()
    try:
        con.execute("""
            INSERT INTO job_runs
              (job_id, run_id, job_name, agent_name, schedule_type,
               status, metadata_json, created_at)
            VALUES (?, ?, ?, ?, ?, 'skipped', ?, ?)
        """, (
            job_id,
            run_id,
            job['job_name'] if job else None,
            job['agent_name'] if job else None,
            job['schedule_type'] if job else None,
            json.dumps({'skipped_reason': reason}),
            now,
        ))
        con.commit()
    finally:
        con.close()


# ---------------------------------------------------------------------------
# Main scan
# ---------------------------------------------------------------------------
def scan_and_dispatch():
    """
    One scan cycle:
    1. Expire stale run locks.
    2. Load all enabled jobs.
    3. For each due job: check for active lock → dispatch or skip.
    """
    scan_start = time.perf_counter()
    con = _db()
    try:
        expired = _expire_stale_run_locks(con)
        if expired:
            _log('index_update',
                 f'[scheduler] Expired {expired} stale run lock(s)', level='notice')

        rows = con.execute("""
            SELECT * FROM scheduled_jobs WHERE enabled = 1
        """).fetchall()
    finally:
        con.close()

    dispatched = 0
    skipped = 0

    for job in rows:
        job_id = job['job_id']
        if not _is_due(job):
            continue

        # Check if an active lock exists on job_runs
        con2 = _db()
        try:
            lock_held = _has_active_lock(
                con2, job_id, job['lock_duration_s'] or DEFAULT_LOCK_DURATION_S)
        finally:
            con2.close()

        if lock_held:
            _log('task_started',
                 f'[scheduler] Skipping {job_id} — lock held by another process',
                 job_id=job_id, level='debug')
            _record_skip(job_id, 'lock_held', job)
            skipped += 1
            continue

        _dispatch(job)
        dispatched += 1

    scan_ms = int((time.perf_counter() - scan_start) * 1000)
    if dispatched or skipped or expired:
        # Routine scan summary is operational chatter, not an activity event —
        # keep it on stdout (scheduler log), out of agent_logs.
        print(f'[scheduler] Scan done: {dispatched} dispatched, {skipped} skipped, '
              f'{expired} locks expired in {scan_ms}ms', flush=True)
    return scan_ms


# ---------------------------------------------------------------------------
# Daemon loop (called from events_server.py)
# ---------------------------------------------------------------------------
def scheduler_loop():
    """
    Daemon thread entry point for events_server.py.
    Runs one scan immediately on startup, then every SCAN_INTERVAL_S seconds.
    """
    _log('task_started', f'[scheduler] Scheduler loop started (device={_DEVICE_ID}, '
         f'interval={SCAN_INTERVAL_S}s)', level='info')
    try:
        scan_and_dispatch()
    except Exception as exc:
        _log('error', f'[scheduler] Initial scan error: {exc}', level='error')

    while True:
        time.sleep(SCAN_INTERVAL_S)
        try:
            scan_and_dispatch()
        except Exception as exc:
            _log('error', f'[scheduler] Scan error: {exc}', level='error')


# ---------------------------------------------------------------------------
# Seed helper — register Alfred cognition jobs (idempotent)
# Replaces the former seed_sage_jobs() after the Sage-Alfred merge (2026-05-28).
# ---------------------------------------------------------------------------
def seed_alfred_cognition_jobs():
    """
    Register alfred-daily-harvest and alfred-weekly-curate in scheduled_jobs.
    Idempotent: INSERT OR IGNORE.
    Budapest is UTC+2 in summer (UTC+1 in winter) — user accepts UTC-only
    + winter drift.  Daily 06:00 local summer = 04:00 UTC.
    Weekly Monday 06:05 local summer = 04:05 UTC (weekday=0, Mon=0).

    Registered DISABLED (enabled=0): the cron scripts run `claude -p "/alf-harvest"`
    headless, which fails with a 401 ("Invalid authentication credentials") because
    the claude CLI cannot authenticate in the unattended cron context. Until that
    auth is sorted, harvest/curate are interactive-only (run /alf-harvest manually).
    Re-enable by flipping `enabled` to 1 once headless auth works.

    The deprecated sage-daily-harvest / sage-weekly-curate jobs are deleted here
    (Sage was merged into Alfred 2026-05-28).
    """
    vault = str(Path(__file__).resolve().parent.parent.parent.parent.parent)
    daily_cmd  = f'{vault}/00_Prompts/BDOS/agents/alfred/cron/run_daily_harvest.sh'
    weekly_cmd = f'{vault}/00_Prompts/BDOS/agents/alfred/cron/run_weekly_curate.sh'

    con = _db()
    try:
        # Remove deprecated Sage jobs (merged into Alfred 2026-05-28).
        con.execute("""
            DELETE FROM scheduled_jobs
            WHERE job_id IN ('sage-daily-harvest', 'sage-weekly-curate')
        """)

        con.execute("""
            INSERT OR IGNORE INTO scheduled_jobs
              (job_id, job_name, agent_name, schedule_type,
               schedule_hour, schedule_minute, schedule_weekday,
               command, requires_approval, lock_duration_s, enabled)
            VALUES
              ('alfred-daily-harvest', 'Alfred Daily Harvest', 'alfred',
               'daily', 4, 0, NULL,
               ?, 0, 600, 0)
        """, (daily_cmd,))

        con.execute("""
            INSERT OR IGNORE INTO scheduled_jobs
              (job_id, job_name, agent_name, schedule_type,
               schedule_hour, schedule_minute, schedule_weekday,
               command, requires_approval, lock_duration_s, enabled)
            VALUES
              ('alfred-weekly-curate', 'Alfred Weekly Curate', 'alfred',
               'weekly', 4, 5, 0,
               ?, 0, 1800, 0)
        """, (weekly_cmd,))

        con.commit()
        cnt = con.execute('SELECT COUNT(*) FROM scheduled_jobs').fetchone()[0]
        print(f'[scheduler] seed_alfred_cognition_jobs: {cnt} total job(s) registered.')
    finally:
        con.close()


# ---------------------------------------------------------------------------
# Backward-compat alias — kept so any existing callsite using seed_sage_jobs()
# still works, but delegates to the new function.
# ---------------------------------------------------------------------------
def seed_sage_jobs():
    """Deprecated alias for seed_alfred_cognition_jobs() (Sage-Alfred merge 2026-05-28)."""
    print('[scheduler] WARNING: seed_sage_jobs() is deprecated; calling seed_alfred_cognition_jobs() instead.')
    seed_alfred_cognition_jobs()


# ---------------------------------------------------------------------------
# Seed helper — register the marketing board sidecar refresh job (idempotent)
# ---------------------------------------------------------------------------
def seed_marketing_jobs():
    """
    Register marketing-board-sidecar-refresh in scheduled_jobs.
    Idempotent: INSERT OR IGNORE.

    Role: safety net (primary trigger is the watchdog hook in watch_event.py).
    Schedule: interval every 300 seconds (5 minutes).
    Agent owner: presto (marketing board is Presto's domain).
    """
    vault = str(Path(__file__).resolve().parent.parent.parent.parent.parent)
    refresh_cmd = (
        f'python3 "{vault}/00_Prompts/BDOS/capabilities/vault-indexing/'
        f'marketing_board_refresh.py"'
    )

    con = _db()
    try:
        description = (
            "Safety-net 5-min interval regen of marketing_board.json sidecar. "
            "Primary trigger: watchdog hook in watch_event.py (event-driven). "
            "This scheduler job catches any events the watchdog may have missed."
        )
        con.execute("""
            INSERT OR IGNORE INTO scheduled_jobs
              (job_id, job_name, agent_name, description,
               schedule_type, interval_seconds,
               command, requires_approval, lock_duration_s, enabled)
            VALUES
              (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            'marketing-board-sidecar-refresh',
            'Marketing Board Sidecar Refresh',
            'presto',
            description,
            'interval', 300,
            refresh_cmd, 0, 120, 1,
        ))

        con.commit()
        cnt = con.execute('SELECT COUNT(*) FROM scheduled_jobs').fetchone()[0]
        print(f'[scheduler] seed_marketing_jobs: {cnt} total job(s) registered.')
    finally:
        con.close()


# ---------------------------------------------------------------------------
# Seed helper — register the Alfred hourly triage job (idempotent)
# ---------------------------------------------------------------------------
def seed_alfred_triage_job():
    """
    Register alfred-hourly-triage in scheduled_jobs (Alfred v0.4 Cognitive
    Triage Engine). Idempotent: INSERT OR IGNORE.

    Role: every hour (while the BDOS daemon is up), Alfred reads email
    (Gmail/Outlook/Yahoo MCP), filters threads needing a reply, and prepares
    multi-agent dossiers (Librarian + dynamic domain-routing) with a draft
    reply + actionable items. Read-only on the outside world: NEVER sends,
    never writes Gmail in --auto. requires_approval=0 because side effects are
    additive-only (internal dossiers under 02_Areas/Personal Growth/Alfred/tasks/).

    Registered DISABLED (enabled=0) at first: like harvest/curate, the headless
    `claude -p` LLM auth is solved via CLAUDE_CODE_OAUTH_TOKEN, but whether the
    interactively-authenticated email connectors (Gmail/Outlook) load in a
    headless `claude -p` is unverified. Run a smoke test (run_hourly_triage.sh
    or `claude -p "/alf-triage --auto"`) once; flip `enabled` to 1 when the
    sources are reachable headless. Degrade-safe regardless: an unreachable
    source is logged + skipped, the dossier-prep then waits for an interactive
    session.
    """
    vault = str(Path(__file__).resolve().parent.parent.parent.parent.parent)
    triage_cmd = f'{vault}/00_Prompts/BDOS/agents/alfred/cron/run_hourly_triage.sh'

    con = _db()
    try:
        description = (
            "Hourly email triage: read Gmail/Outlook/Yahoo, filter threads needing "
            "a reply, prepare multi-agent dossiers (Librarian + domain-routing) with "
            "draft + actionable items. Never sends. Additive-only (tasks/ dossiers). "
            "Heartbeat: state/triage_queue.md. enabled=0 until headless email-MCP "
            "reachability is verified."
        )
        con.execute("""
            INSERT OR IGNORE INTO scheduled_jobs
              (job_id, job_name, agent_name, description,
               schedule_type, interval_seconds,
               command, requires_approval, lock_duration_s, enabled)
            VALUES
              (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            'alfred-hourly-triage',
            'Alfred Hourly Triage',
            'alfred',
            description,
            'interval', 3600,
            triage_cmd, 0, 900, 0,
        ))

        con.commit()
        cnt = con.execute('SELECT COUNT(*) FROM scheduled_jobs').fetchone()[0]
        print(f'[scheduler] seed_alfred_triage_job: {cnt} total job(s) registered.')
    finally:
        con.close()


# ---------------------------------------------------------------------------
# Seed helper — register the vault-index reconciliation backstop (idempotent)
# ---------------------------------------------------------------------------
def seed_reach_jobs():
    """
    Register vault-index-reconcile in scheduled_jobs (Reach layer, 2026-06-07).
    Idempotent: INSERT OR IGNORE.

    Role: the GROWTH GUARANTEE. The live watcher gives low-latency updates but
    an incremental watcher can miss events (crash, sleep, Drive sync lag) and an
    event-based watcher never re-checks, so a missed file would stay invisible to
    the Librarian until the next full build. This interval job runs a full
    disk-vs-index reconciliation (reconcile.sh -> watch.py --once) every 30 min,
    independent of which watcher engine is live, and refreshes the honest reach
    sidecar (emit_stats.py) so the dashboard shows the real coverage number.

    Safe alongside the live watcher (both use WAL + busy_timeout). Owner: maestro
    (infra concern, same as the scheduler's own logs). Enabled by default: it is
    read-only when nothing changed, and additive (never deletes vault files).
    """
    vault = str(Path(__file__).resolve().parent.parent.parent.parent.parent)
    reconcile_cmd = (
        f'{vault}/00_Prompts/BDOS/capabilities/vault-indexing/reconcile.sh'
    )

    con = _db()
    try:
        description = (
            "Full disk-vs-index reconciliation backstop every 30 min: catches any "
            "file the live watcher missed (crash/sleep/Drive-lag), purges ghosts, "
            "and refreshes the honest reach sidecar. The growth guarantee, "
            "independent of the watcher engine. Safe alongside the watcher (WAL)."
        )
        con.execute("""
            INSERT OR IGNORE INTO scheduled_jobs
              (job_id, job_name, agent_name, description,
               schedule_type, interval_seconds,
               command, requires_approval, lock_duration_s, enabled)
            VALUES
              (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            'vault-index-reconcile',
            'Vault Index Reconcile',
            'maestro',
            description,
            'interval', 1800,
            reconcile_cmd, 0, 300, 1,
        ))

        con.commit()
        cnt = con.execute('SELECT COUNT(*) FROM scheduled_jobs').fetchone()[0]
        print(f'[scheduler] seed_reach_jobs: {cnt} total job(s) registered.')
    finally:
        con.close()


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='BDOS Job Scheduler')
    parser.add_argument('--once',            action='store_true', help='Run one scan then exit')
    parser.add_argument('--loop',            action='store_true', help='Run continuous loop')
    parser.add_argument('--seed',            action='store_true', help='Seed Alfred cognition jobs (harvest+curate) then exit')
    parser.add_argument('--seed-alfred',     action='store_true', help='Alias for --seed (Alfred cognition jobs)')
    parser.add_argument('--seed-triage',     action='store_true', help='Seed Alfred hourly triage job then exit')
    parser.add_argument('--seed-marketing',  action='store_true', help='Seed marketing board job then exit')
    parser.add_argument('--seed-reach',      action='store_true', help='Seed vault-index reconciliation backstop then exit')
    parser.add_argument('--status',          action='store_true', help='Print job status table')
    args = parser.parse_args()

    if args.seed or getattr(args, 'seed_alfred', False):
        seed_alfred_cognition_jobs()
        sys.exit(0)

    if getattr(args, 'seed_triage', False):
        seed_alfred_triage_job()
        sys.exit(0)

    if args.seed_marketing:
        seed_marketing_jobs()
        sys.exit(0)

    if getattr(args, 'seed_reach', False):
        seed_reach_jobs()
        sys.exit(0)

    if args.status:
        con = _db()
        rows = con.execute(
            'SELECT job_id, job_name, enabled, schedule_type, '
            'last_run_at, next_run_at FROM scheduled_jobs ORDER BY job_id'
        ).fetchall()
        con.close()
        print(f"{'JOB_ID':<30} {'TYPE':<10} {'ENABLED':<8} {'LAST_RUN':<22} {'NEXT_RUN'}")
        for r in rows:
            print(f"{r['job_id']:<30} {r['schedule_type']:<10} {r['enabled']:<8} "
                  f"{(r['last_run_at'] or 'never'):<22} {r['next_run_at'] or '—'}")
        sys.exit(0)

    if args.once:
        ms = scan_and_dispatch()
        print(f'[scheduler] Single scan completed in {ms}ms')
        sys.exit(0)

    if args.loop:
        scheduler_loop()
