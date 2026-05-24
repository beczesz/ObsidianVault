#!/usr/bin/env python3
"""BDOS Vault Indexing — event-based watcher (watchdog 6.x).

Sub-second latency. Uses inotify on Linux / FSEvents on macOS. Falls back to
polling internally if event-based observer fails. Indexes file changes the
moment they're flushed to disk.

Usage:
    python3 watch_event.py [--once]
"""

import os
import sys
import time
import signal
import sqlite3
import argparse
import threading
from pathlib import Path

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
from build_index import (
    walk_vault, index_file, VAULT_ROOT, DB_PATH, SCHEMA_PATH, EXCLUDE_DIRS
)

PID_FILE = SCRIPT_DIR / "cache" / "watch.pid"
LOG_FILE = SCRIPT_DIR / "cache" / "watch.log"
DEBOUNCE_SEC = 0.5  # collect changes for 500ms before applying (avoids burst-event spam)


def log(msg):
    """Write to log file only (not stdout, since nohup redirects stdout → log file)."""
    ts = time.strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{ts}] {msg}"
    try:
        with open(LOG_FILE, 'a') as f:
            f.write(line + '\n')
    except OSError:
        pass


def ensure_db_exists():
    if not DB_PATH.exists():
        log("No vault.db — running full rebuild first...")
        import subprocess
        result = subprocess.run([sys.executable, str(SCRIPT_DIR / "build_index.py")],
                                capture_output=True, text=True)
        if result.returncode != 0:
            log(f"Full rebuild failed: {result.stderr}")
            sys.exit(1)
        log("Full rebuild complete.")


def should_skip_path(p: Path) -> bool:
    """Return True if path is in an excluded dir or not a .md file."""
    if p.suffix != '.md':
        return True
    parts = p.parts
    for ex in EXCLUDE_DIRS:
        if ex in parts:
            return True
    if any(part.startswith('.smart-env') for part in parts):
        return True
    return False


class VaultEventHandler(FileSystemEventHandler):
    def __init__(self):
        super().__init__()
        self.pending = {}  # path → ('created' | 'modified' | 'deleted')
        self.lock = threading.Lock()
        self.last_event_ts = 0

    def _record(self, src_path: str, event_type: str):
        p = Path(src_path)
        if should_skip_path(p):
            return
        try:
            p.relative_to(VAULT_ROOT)
        except ValueError:
            return
        with self.lock:
            self.pending[str(p)] = event_type
            self.last_event_ts = time.time()

    def on_created(self, event):
        if not event.is_directory:
            self._record(event.src_path, 'created')

    def on_modified(self, event):
        if not event.is_directory:
            self._record(event.src_path, 'modified')

    def on_deleted(self, event):
        if not event.is_directory:
            self._record(event.src_path, 'deleted')

    def on_moved(self, event):
        if not event.is_directory:
            self._record(event.src_path, 'deleted')
            self._record(event.dest_path, 'created')

    def drain(self):
        """Pop and return all pending events, clearing the dict."""
        with self.lock:
            out = dict(self.pending)
            self.pending.clear()
        return out


def apply_events(events: dict, conn, now: float):
    """Apply a batch of events to the DB."""
    new_or_mod, deleted = [], []
    for path_str, etype in events.items():
        if etype == 'deleted':
            deleted.append(path_str)
        else:
            new_or_mod.append(path_str)

    deleted_rel, applied_rel = [], []

    for path_str in deleted:
        try:
            rel = Path(path_str).relative_to(VAULT_ROOT).as_posix()
        except ValueError:
            continue
        conn.execute("DELETE FROM notes WHERE path = ?", (rel,))
        conn.execute("DELETE FROM notes_fts WHERE path = ?", (rel,))
        conn.execute("DELETE FROM backlinks WHERE source_path = ?", (rel,))
        deleted_rel.append(rel)

    for path_str in new_or_mod:
        p = Path(path_str)
        if not p.exists():
            continue
        try:
            rel = p.relative_to(VAULT_ROOT).as_posix()
        except ValueError:
            continue
        try:
            index_file(p, VAULT_ROOT, conn, now)
            applied_rel.append(rel)
        except Exception as e:
            log(f"  ERR indexing {rel}: {e}")

    # Re-resolve backlinks if anything changed
    if deleted_rel or applied_rel:
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
    return len(applied_rel), len(deleted_rel)


def write_pid():
    PID_FILE.parent.mkdir(parents=True, exist_ok=True)
    PID_FILE.write_text(str(os.getpid()))


_observer = None


def cleanup(signum=None, frame=None):
    log(f"Stopping event-watcher (signal {signum}).")
    global _observer
    if _observer:
        _observer.stop()
        _observer.join(timeout=3)
    try:
        if PID_FILE.exists():
            PID_FILE.unlink()
    except OSError:
        pass
    sys.exit(0)


def main():
    global _observer
    ap = argparse.ArgumentParser()
    ap.add_argument('--once', action='store_true')
    args = ap.parse_args()

    ensure_db_exists()
    write_pid()
    signal.signal(signal.SIGTERM, cleanup)
    signal.signal(signal.SIGINT, cleanup)

    log(f"Event-watcher started. PID={os.getpid()} engine=watchdog")
    log(f"Vault: {VAULT_ROOT}")

    handler = VaultEventHandler()
    _observer = Observer()
    _observer.schedule(handler, str(VAULT_ROOT), recursive=True)
    _observer.start()

    log("Observer running. Listening for FS events.")

    try:
        last_apply = time.time()
        while True:
            time.sleep(0.2)
            # If there are pending events AND DEBOUNCE_SEC has passed since the last event → apply
            if handler.pending:
                if time.time() - handler.last_event_ts >= DEBOUNCE_SEC:
                    events = handler.drain()
                    if events:
                        conn = sqlite3.connect(DB_PATH)
                        now = time.time()
                        applied, deleted = apply_events(events, conn, now)
                        conn.close()
                        log(f"  applied {applied} new/mod, {deleted} del (event-batch, {len(events)} raw events)")
            if args.once and not handler.pending:
                break
    except KeyboardInterrupt:
        cleanup()


if __name__ == '__main__':
    main()
