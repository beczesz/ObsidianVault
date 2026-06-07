#!/usr/bin/env python3
"""
BDOS Vault — Indexing Daemon (headless, no port)
================================================
Single-server consolidation (2026-05-29): this process used to be an SSE HTTP
server on port 4322. That HTTP role is gone. The browser-facing server is now
ONLY dash-server.mjs (port 4321): it serves files, pushes the `vault-update`
SSE event (by polling vault.db mtime itself) and answers /health. Dashboards
therefore only ever talk to localhost:4321.

What remains here is pure background work with NO socket to bind or conflict:
  - Scheduler (owner machine): scheduler_loop() scans scheduled_jobs every 60s
    and dispatches due jobs, recording results in agent_observability.db.
  - Sidecar self-refresh (secondary machine, BDOS_DISABLE_SCHEDULER=1):
    regenerates the agent_logs.json sidecar from the synced DB so the dashboard
    DB/Scheduler Health pills stay fresh despite Google Drive lag.

The filename, the events.pid / events.log names, and the launch.py "events
server" wiring are kept as-is to avoid PID/log migration churn; conceptually
this is the "indexing daemon". Single-owner rule unchanged: the scheduler runs
on exactly one machine (Mac), secondaries pass --no-scheduler.

Usage:
  python3 events_server.py                      # scheduler ON (owner)
  BDOS_DISABLE_SCHEDULER=1 python3 events_server.py   # secondary (sidecar refresh)

Requires only stdlib — no pip install.
"""

import threading
import time
import os
import sys
from pathlib import Path

# Make vault-indexing importable when run from any cwd
_SCRIPT_DIR = Path(__file__).resolve().parent
if str(_SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_DIR))

SCRIPT_DIR = _SCRIPT_DIR
from runtime import DB_PATH as VAULT_DB  # per-machine local index (this machine's watcher writes it)
# Sidecar self-refresh (added 2026-05-29): on the NON-scheduler machine the
# agent_logs.json sidecar is only ever produced on the owner (Mac) and reaches
# us via Google Drive with multi-minute lag, so the dashboard Health pills (DB,
# Scheduler) read it as stale even though the synced agent_observability.db is
# current. When BDOS_DISABLE_SCHEDULER=1 we therefore regenerate the sidecar
# locally from the synced DB on a short cadence. Only the secondary machine does
# this (the owner refreshes via scheduler/agent activity), so the synced JSON
# still has a single active writer per machine-role — no Drive write contention.
SIDECAR_REFRESH_INTERVAL = int(os.environ.get("BDOS_SIDECAR_REFRESH_S", 60))


def sidecar_refresh_loop():
    """Background thread (secondary machine only): regenerate agent_logs.json
    from the synced agent_observability.db every SIDECAR_REFRESH_INTERVAL seconds
    so the dashboard Health pills stay fresh without waiting for Drive sync.

    Imports agent_log lazily (same dir) and opens its own short-lived DB
    connection per cycle. Failures are logged but never kill the daemon."""
    import sqlite3
    try:
        import agent_log
    except Exception as exc:  # pragma: no cover
        print(f"[indexing-daemon] sidecar self-refresh disabled — agent_log import failed: {exc}")
        return
    print(f"[indexing-daemon] Sidecar self-refresh ON (every {SIDECAR_REFRESH_INTERVAL}s) — "
          f"keeps DB/Scheduler pills fresh on the non-scheduler machine")
    while True:
        try:
            con = sqlite3.connect(str(agent_log.DB_PATH), timeout=10)
            con.row_factory = sqlite3.Row
            try:
                agent_log._refresh_sidecar(con)
            finally:
                con.close()
        except Exception as exc:
            print(f"[indexing-daemon] sidecar refresh error: {exc}")
        time.sleep(SIDECAR_REFRESH_INTERVAL)


def main():
    print("[indexing-daemon] BDOS Vault indexing daemon — headless (no port)")
    print(f"[indexing-daemon] Local index: {VAULT_DB}")
    if not VAULT_DB.exists():
        print(f"[indexing-daemon] WARNING: vault.db not found at {VAULT_DB}")
        print(f"[indexing-daemon]          Start watch_event.py first (writes cache/watch.pid)")

    threads_started = 0

    # Sidecar self-refresh on BOTH roles. Keeps agent_logs.json freshness
    # (generated_at + the scheduled_jobs.last_run_at snapshot) current on a time
    # cadence, decoupled from agent_log inserts. Required on the owner since the
    # log-denoise (2026-05-29) removed the per-scan scheduler heartbeat that used
    # to refresh the sidecar implicitly; without this the dashboard DB/Sched pills
    # flap to "stale" during quiet periods even though the daemon is healthy.
    srt = threading.Thread(target=sidecar_refresh_loop, daemon=True, name="sidecar-refresh")
    srt.start()
    threads_started += 1

    if os.environ.get("BDOS_DISABLE_SCHEDULER") == "1":
        print("[indexing-daemon] Scheduler disabled (BDOS_DISABLE_SCHEDULER=1) — sidecar refresh only")
    else:
        # Phase B: BDOS Job Scheduler — single-owner. Runs on exactly ONE machine,
        # otherwise scheduled jobs double-fire against the synced agent_observability.db.
        try:
            from scheduler import scheduler_loop
            st = threading.Thread(target=scheduler_loop, daemon=True, name="scheduler")
            st.start()
            threads_started += 1
            print("[indexing-daemon] Scheduler started (scan interval 60s)")
        except ImportError as _e:
            print(f"[indexing-daemon] WARNING: scheduler.py not found — scheduler disabled ({_e})")

    if threads_started == 0:
        print("[indexing-daemon] No background work to do — exiting.")
        return

    # Block forever; daemon threads do the work. Ctrl-C / SIGTERM exits.
    stop = threading.Event()
    try:
        while not stop.wait(3600):
            pass
    except KeyboardInterrupt:
        print("\n[indexing-daemon] Stopped.")


if __name__ == "__main__":
    main()
