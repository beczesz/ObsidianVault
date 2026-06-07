#!/usr/bin/env python3
"""BDOS Vault Indexing — incremental watcher (stdlib polling, no deps).

Polls the vault every POLL_INTERVAL seconds. Compares file mtimes to the
last-indexed mtime in SQLite. Updates the index for any changed/new/deleted
files. Lightweight — only does work when files actually change.

Usage:
    python3 watch.py [--interval 5] [--once]

Auto-managed via start.sh / stop.sh — manual invocation is rare.
"""

import os
import sys
import time
import signal
import sqlite3
import argparse
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
from build_index import (
    walk_vault, index_file, VAULT_ROOT, DB_PATH, SCHEMA_PATH, EXCLUDE_DIRS
)

from runtime import PID_WATCHER as PID_FILE, LOG_WATCH as LOG_FILE, connect
POLL_INTERVAL = 5  # seconds


def log(msg):
    ts = time.strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{ts}] {msg}"
    print(line, flush=True)
    try:
        with open(LOG_FILE, 'a') as f:
            f.write(line + '\n')
    except OSError:
        pass


def ensure_db_exists():
    """If no DB, run a full build first."""
    if not DB_PATH.exists():
        log("No vault.db found — running full rebuild first...")
        import subprocess
        result = subprocess.run([sys.executable, str(SCRIPT_DIR / "build_index.py")],
                                capture_output=True, text=True)
        if result.returncode != 0:
            log(f"Full rebuild failed: {result.stderr}")
            sys.exit(1)
        log("Full rebuild complete. Now watching for changes.")


def get_indexed_mtimes(conn):
    """Return dict of path → indexed_mtime from DB."""
    rows = conn.execute("SELECT path, mtime FROM notes").fetchall()
    return {p: m for p, m in rows}


def scan_vault_mtimes():
    """Walk vault, return dict of path → current mtime."""
    out = {}
    for p in walk_vault(VAULT_ROOT):
        try:
            rel = p.relative_to(VAULT_ROOT).as_posix()
            out[rel] = p.stat().st_mtime
        except (OSError, ValueError):
            pass
    return out


def detect_changes(indexed, current):
    """Return (new, modified, deleted) path lists."""
    indexed_set = set(indexed.keys())
    current_set = set(current.keys())
    new = current_set - indexed_set
    deleted = indexed_set - current_set
    modified = {p for p in (current_set & indexed_set)
                if current[p] > indexed[p] + 0.1}  # 100ms tolerance
    return new, modified, deleted


def apply_changes(conn, new, modified, deleted, now):
    """Update DB for the change set."""
    # Deletes
    for path in deleted:
        conn.execute("DELETE FROM notes WHERE path = ?", (path,))
        conn.execute("DELETE FROM notes_fts WHERE path = ?", (path,))
        conn.execute("DELETE FROM backlinks WHERE source_path = ?", (path,))

    # Inserts + updates
    for path in (new | modified):
        full = VAULT_ROOT / path
        if not full.exists():
            continue
        try:
            index_file(full, VAULT_ROOT, conn, now)
        except Exception as e:
            log(f"  ERR indexing {path}: {e}")

    # Re-resolve any backlinks touched (cheap update)
    if new or modified or deleted:
        conn.execute('''
            UPDATE backlinks SET resolved_path = (
                SELECT path FROM notes
                WHERE notes.path LIKE '%' || backlinks.target || '.md'
                ORDER BY length(notes.path) ASC LIMIT 1
            )
            WHERE resolved_path IS NULL
        ''')
        conn.execute('''
            UPDATE backlinks SET resolved_path = (
                SELECT path FROM notes
                WHERE notes.path LIKE '%/' || backlinks.target || '.md'
                   OR notes.path = backlinks.target || '.md'
                ORDER BY length(notes.path) ASC LIMIT 1
            )
            WHERE resolved_path IS NULL
              AND backlinks.target NOT LIKE '%/%'
        ''')

    conn.commit()


def write_pid():
    PID_FILE.parent.mkdir(parents=True, exist_ok=True)
    PID_FILE.write_text(str(os.getpid()))


def cleanup(signum=None, frame=None):
    log(f"Stopping watcher (signal {signum}).")
    try:
        if PID_FILE.exists():
            PID_FILE.unlink()
    except OSError:
        pass
    sys.exit(0)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--interval', type=float, default=POLL_INTERVAL)
    ap.add_argument('--once', action='store_true', help="One-shot mode: scan + apply once, exit")
    args = ap.parse_args()

    ensure_db_exists()

    if not args.once:
        write_pid()
        signal.signal(signal.SIGTERM, cleanup)
        signal.signal(signal.SIGINT, cleanup)
        log(f"Watcher started. PID={os.getpid()}, interval={args.interval}s")
        log(f"Vault: {VAULT_ROOT}")

    try:
        cycle = 0
        while True:
            cycle += 1
            conn = connect(DB_PATH)  # WAL + busy_timeout: safe alongside a scheduled reconcile
            indexed = get_indexed_mtimes(conn)
            current = scan_vault_mtimes()
            new, modified, deleted = detect_changes(indexed, current)

            if new or modified or deleted:
                now = time.time()
                apply_changes(conn, new, modified, deleted, now)
                log(f"  cycle {cycle}: +{len(new)} new / ~{len(modified)} mod / -{len(deleted)} del → applied")
            elif cycle % 12 == 1:  # heartbeat every ~1 min at default interval
                log(f"  cycle {cycle}: no changes (idle)")

            conn.close()

            if args.once:
                break
            time.sleep(args.interval)
    except KeyboardInterrupt:
        cleanup()


if __name__ == '__main__':
    main()
