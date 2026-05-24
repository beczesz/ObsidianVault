#!/usr/bin/env python3
"""
BDOS Vault — SSE Events Server (port 4322)
===========================================
Watches vault.db mtime for changes (the vault-indexing watcher updates it
whenever it indexes markdown changes). Pushes a vault-update SSE event to
all connected clients when vault.db is touched.

Runs alongside dash-server.mjs (port 4321) — clean separation of concerns:
  dash-server.mjs  (4321) → serves static files + /__events for raw .md changes
  events_server.py (4322) → vault-update events from vault.db mtime + scheduler

Scheduler integration (Phase B, 2026-05-24):
  A scheduler_loop() daemon thread is started on main(). It scans
  scheduled_jobs every 60 s and dispatches due jobs as subprocesses.
  Job results are written to job_runs in agent_observability.db.

Usage:
  python3 events_server.py          # default port 4322
  PORT=4323 python3 events_server.py

Client JS:
  const es = new EventSource('http://localhost:4322/events');
  es.addEventListener('message', ev => {
    const d = JSON.parse(ev.data);
    if (d.type === 'vault-update') refetchAndRender();
  });

Requires only stdlib — no pip install.
"""

import http.server
import socketserver
import threading
import time
import os
import json
import sys
from pathlib import Path

# Make vault-indexing importable when run from any cwd
_SCRIPT_DIR = Path(__file__).resolve().parent
if str(_SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_DIR))

SCRIPT_DIR = _SCRIPT_DIR
VAULT_DB = SCRIPT_DIR / "cache" / "vault.db"
PORT = int(os.environ.get("PORT", 4322))
POLL_INTERVAL = 1.0      # seconds between mtime checks
HEARTBEAT_INTERVAL = 15  # seconds between SSE heartbeat comments

# Thread-safe set of active response objects
_clients_lock = threading.Lock()
_clients: set = set()
_last_mtime: float = 0.0


def get_db_mtime() -> float:
    try:
        return VAULT_DB.stat().st_mtime
    except OSError:
        return 0.0


def broadcast_vault_update():
    payload = json.dumps({"type": "vault-update", "ts": int(time.time())})
    msg = f"data: {payload}\n\n".encode()
    with _clients_lock:
        dead = set()
        for wfile in _clients:
            try:
                wfile.write(msg)
                wfile.flush()
            except OSError:
                dead.add(wfile)
        _clients -= dead


def watcher_loop():
    """Background thread: poll vault.db mtime, broadcast on change."""
    global _last_mtime
    _last_mtime = get_db_mtime()
    while True:
        time.sleep(POLL_INTERVAL)
        mt = get_db_mtime()
        if mt and mt != _last_mtime:
            _last_mtime = mt
            broadcast_vault_update()


def heartbeat_loop():
    """Background thread: send SSE heartbeat comment every 15s."""
    global _clients
    ping = b": heartbeat\n\n"
    while True:
        time.sleep(HEARTBEAT_INTERVAL)
        with _clients_lock:
            dead = set()
            for wfile in _clients:
                try:
                    wfile.write(ping)
                    wfile.flush()
                except OSError:
                    dead.add(wfile)
            _clients -= dead


class EventsHandler(http.server.BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):
        # Quiet: only log connections, not every heartbeat
        if "GET /events" in (args[0] if args else ""):
            print(f"[{time.strftime('%H:%M:%S')}] SSE client connected from {self.address_string()}")

    def do_OPTIONS(self):
        self.send_response(204)
        self._cors()
        self.end_headers()

    def do_GET(self):
        if self.path == "/events":
            self._handle_sse()
        elif self.path == "/health":
            self.send_response(200)
            self._cors()
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            body = json.dumps({
                "ok": True,
                "db_exists": VAULT_DB.exists(),
                "db_mtime": _last_mtime,
                "clients": len(_clients),
            }).encode()
            self.wfile.write(body)
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not found. Try /events or /health\n")

    def _cors(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "Cache-Control")

    def _handle_sse(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream")
        self.send_header("Cache-Control", "no-cache")
        self.send_header("Connection", "keep-alive")
        self._cors()
        self.end_headers()

        # Send retry directive
        try:
            self.wfile.write(b"retry: 3000\n\n")
            self.wfile.flush()
        except OSError:
            return

        with _clients_lock:
            _clients.add(self.wfile)

        # Hold the connection open — the background threads broadcast
        try:
            while True:
                time.sleep(1)
                # Check if connection is still alive by peeking
                if self.wfile.closed:
                    break
        except (OSError, BrokenPipeError):
            pass
        finally:
            with _clients_lock:
                _clients.discard(self.wfile)


class ThreadedHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True
    allow_reuse_address = True


def main():
    # Start background threads
    wt = threading.Thread(target=watcher_loop, daemon=True, name="db-watcher")
    wt.start()
    ht = threading.Thread(target=heartbeat_loop, daemon=True, name="heartbeat")
    ht.start()

    # Phase B: BDOS Job Scheduler — daemon thread attached to events_server
    try:
        from scheduler import scheduler_loop
        st = threading.Thread(target=scheduler_loop, daemon=True, name="scheduler")
        st.start()
        print(f"[events_server] Scheduler started (scan interval 60s)")
    except ImportError as _e:
        print(f"[events_server] WARNING: scheduler.py not found — scheduler disabled ({_e})")

    server = ThreadedHTTPServer(("", PORT), EventsHandler)
    print(f"[events_server] BDOS Vault SSE server — port {PORT}")
    print(f"[events_server] Watching: {VAULT_DB}")
    print(f"[events_server] Endpoint: http://localhost:{PORT}/events")
    print(f"[events_server] Health:   http://localhost:{PORT}/health")
    if not VAULT_DB.exists():
        print(f"[events_server] WARNING: vault.db not found at {VAULT_DB}")
        print(f"[events_server]          Start watch_event.py first (PID will be written to cache/watch.pid)")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n[events_server] Stopped.")


if __name__ == "__main__":
    main()
