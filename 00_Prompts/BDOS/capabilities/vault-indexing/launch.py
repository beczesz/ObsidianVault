#!/usr/bin/env python3
"""BDOS Vault Indexing — cross-platform launcher (macOS + Windows).

One launcher for both machines. Auto-detects:
  - the OS                 → per-machine cache/PID/log paths (via runtime.py)
  - whether `watchdog` is installed → event-based watcher, else polling fallback

Each machine manages ONLY its own processes (per-machine PID files), so the
other machine's running watcher/events-server is never touched. Each machine
indexes its own local vault.db, so the synced vault never gets conflict copies.

Usage:
  python launch.py start            # start watcher + indexing daemon (idempotent)
  python launch.py stop
  python launch.py restart
  python launch.py status

Options:
  --no-scheduler   don't run the cron scheduler inside events_server.
                   The scheduler must run on exactly ONE machine (it dispatches
                   jobs against the synced agent_observability.db). Secondary
                   machines should pass this. Default: scheduler enabled.

Exit codes: 0 ok, 1 failure.
"""

import argparse
import os
import signal
import subprocess
import sys
import time
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
import runtime
from runtime import (
    DB_PATH, CACHE_DIR, PID_WATCHER, PID_EVENTS, LOG_WATCH, LOG_EVENTS,
    pid_is_running, read_pid,
)

IS_WINDOWS = os.name == "nt"
PY = sys.executable


def _have_watchdog() -> bool:
    try:
        import watchdog.observers  # noqa: F401
        return True
    except Exception:
        return False


def _spawn(script: str, log_file: Path, extra_env: dict | None = None) -> int:
    """Spawn a detached background python process; return its PID."""
    env = os.environ.copy()
    # Force unbuffered stdout/stderr so the spawned process's print() output
    # reaches the log file live. Without this, Python block-buffers when stdout
    # is a file (not a TTY), leaving events.log empty even while the server runs
    # — which previously made a healthy server look like a crashed one.
    env["PYTHONUNBUFFERED"] = "1"
    if extra_env:
        env.update(extra_env)
    log_file.parent.mkdir(parents=True, exist_ok=True)
    logf = open(log_file, "a", buffering=1)
    kwargs: dict = dict(
        stdout=logf, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL,
        env=env, cwd=str(SCRIPT_DIR),
    )
    if IS_WINDOWS:
        # DETACHED_PROCESS: survive parent exit, no console window
        kwargs["creationflags"] = 0x00000008
    else:
        kwargs["start_new_session"] = True
    proc = subprocess.Popen([PY, str(SCRIPT_DIR / script)], **kwargs)
    return proc.pid


def _watcher_script() -> tuple[str, str]:
    if _have_watchdog():
        return "watch_event.py", "event-based (watchdog)"
    return "watch.py", "polling (stdlib fallback)"


def _ensure_db():
    if DB_PATH.exists():
        return
    print(f"  No local index at {DB_PATH} — building (one-time, ~a few seconds)...")
    r = subprocess.run([PY, str(SCRIPT_DIR / "build_index.py")],
                       cwd=str(SCRIPT_DIR))
    if r.returncode != 0:
        print("  ERROR: initial index build failed.")
        sys.exit(1)


def start(scheduler: bool = True):
    print(f"BDOS vault-indexing — start  (host cache: {CACHE_DIR})")

    # ---- watcher ----
    wpid = read_pid(PID_WATCHER)
    if pid_is_running(wpid):
        print(f"  watcher already running (PID {wpid})")
    else:
        if wpid:
            PID_WATCHER.unlink(missing_ok=True)
        _ensure_db()
        script, engine = _watcher_script()
        pid = _spawn(script, LOG_WATCH)
        PID_WATCHER.write_text(str(pid))
        time.sleep(1.0)
        if pid_is_running(pid):
            print(f"  watcher started — PID {pid} — {engine}")
        else:
            print(f"  ERROR: watcher failed to start. See {LOG_WATCH}")
            sys.exit(1)

    # ---- indexing daemon (headless: scheduler + sidecar refresh, no port) ----
    epid = read_pid(PID_EVENTS)
    if pid_is_running(epid):
        print(f"  indexing daemon already running (PID {epid})")
    else:
        if epid:
            PID_EVENTS.unlink(missing_ok=True)
        extra = {} if scheduler else {"BDOS_DISABLE_SCHEDULER": "1"}
        pid = _spawn("events_server.py", LOG_EVENTS, extra_env=extra)
        PID_EVENTS.write_text(str(pid))
        time.sleep(1.0)
        if pid_is_running(pid):
            sched = "scheduler ON" if scheduler else "scheduler OFF (sidecar refresh)"
            print(f"  indexing daemon started — PID {pid} — {sched}")
        else:
            print(f"  ERROR: indexing daemon failed to start. See {LOG_EVENTS}")
            sys.exit(1)

    print("  done — live updates + /health are served by dash-server.mjs (port 4321).")


def stop():
    print(f"BDOS vault-indexing — stop  (host cache: {CACHE_DIR})")
    for label, pid_file in (("watcher", PID_WATCHER), ("events server", PID_EVENTS)):
        pid = read_pid(pid_file)
        if pid_is_running(pid):
            try:
                os.kill(pid, signal.SIGTERM)
                print(f"  stopped {label} (PID {pid})")
            except OSError as e:
                print(f"  could not stop {label} (PID {pid}): {e}")
        else:
            print(f"  {label} not running")
        pid_file.unlink(missing_ok=True)


def status():
    script, engine = _watcher_script()
    print(f"BDOS vault-indexing — status")
    print(f"  OS               : {os.name} ({sys.platform})")
    print(f"  watcher engine   : {engine}")
    print(f"  host cache dir   : {CACHE_DIR}")
    print(f"  vault.db         : {'exists' if DB_PATH.exists() else 'MISSING'}"
          + (f"  ({DB_PATH.stat().st_size/1024:.0f} KB)" if DB_PATH.exists() else ""))
    wpid = read_pid(PID_WATCHER)
    epid = read_pid(PID_EVENTS)
    print(f"  watcher          : {'running PID ' + str(wpid) if pid_is_running(wpid) else 'stopped'}")
    print(f"  indexing daemon  : {'running PID ' + str(epid) if pid_is_running(epid) else 'stopped'}")


def main():
    ap = argparse.ArgumentParser(description="BDOS vault-indexing live stack launcher")
    ap.add_argument("action", choices=["start", "stop", "restart", "status"])
    ap.add_argument("--no-scheduler", action="store_true",
                    help="don't run the cron scheduler in events_server (secondary machines)")
    args = ap.parse_args()

    if args.action == "start":
        start(scheduler=not args.no_scheduler)
    elif args.action == "stop":
        stop()
    elif args.action == "restart":
        stop()
        time.sleep(1.0)
        start(scheduler=not args.no_scheduler)
    elif args.action == "status":
        status()


if __name__ == "__main__":
    main()
