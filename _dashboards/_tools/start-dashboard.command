#!/bin/bash
# === Ideas Vault dashboard launcher (double-click on macOS) ==================
# (1) Starts the zero-dependency Node SSE server (dash-server.mjs) from the vault
#     root if it isn't already running, (2) opens the launcher in the browser.
# Safe to run multiple times — won't double-start the server.
# Stop it again with stop-dashboard.command (same folder).
# =============================================================================

PORT="${PORT:-4321}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SERVER="$SCRIPT_DIR/dash-server.mjs"
URL="http://localhost:${PORT}/"

# Node present?
if ! command -v node >/dev/null 2>&1; then
  echo "ERROR: Node.js not found. Install it from https://nodejs.org then retry."
  sleep 4; exit 1
fi

# Server file present?
if [ ! -f "$SERVER" ]; then
  echo "ERROR: dash-server.mjs not found next to this script ($SERVER)."
  sleep 4; exit 1
fi

# Already running on this port?
if lsof -ti :"$PORT" >/dev/null 2>&1; then
  echo "✓ Server already running on port $PORT"
else
  echo "→ Starting Ideas Vault dashboard server on port $PORT..."
  # nohup + & detaches the server so it keeps running after this window closes.
  PORT="$PORT" nohup node "$SERVER" >/tmp/ideas-vault-dashboard.log 2>&1 &
  sleep 1.5
  if lsof -ti :"$PORT" >/dev/null 2>&1; then
    echo "✓ Server started (PID $(lsof -ti :$PORT)). Log: /tmp/ideas-vault-dashboard.log"
  else
    echo "ERROR: server failed to start — see /tmp/ideas-vault-dashboard.log"; sleep 4; exit 1
  fi
fi

echo "→ Opening $URL"
open "$URL"
sleep 1
