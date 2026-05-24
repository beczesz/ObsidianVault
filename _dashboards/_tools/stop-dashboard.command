#!/bin/bash
# === Stop the Ideas Vault dashboard server ===================================
# Stops the Node SSE server started by start-dashboard.command (port 4321).
# Override the port with PORT=xxxx if you started it on a non-default port.
# =============================================================================

PORT="${PORT:-4321}"
PID=$(lsof -ti :"$PORT" 2>/dev/null)
if [ -z "$PID" ]; then
  echo "No server running on port $PORT."
else
  kill $PID
  echo "✓ Stopped server (PID $PID) on port $PORT."
fi
sleep 1
