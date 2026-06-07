#!/usr/bin/env bash
# Install a per-user LaunchAgent so the Ideas Vault dashboard server
# (dash-server.mjs, port 4321) starts at login and self-restarts on crash.
# macOS only. Reversible with uninstall-autostart.sh.
set -e

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
NODE="$(command -v node || echo /opt/homebrew/bin/node)"
PYBIN_DIR="$(dirname "$(command -v python3 || echo /usr/bin/python3)")"
LABEL="com.bdos.dash-server"
PLIST="$HOME/Library/LaunchAgents/${LABEL}.plist"
LOGDIR="$HOME/Library/Logs"
mkdir -p "$HOME/Library/LaunchAgents" "$LOGDIR"

echo "Installing LaunchAgent: $LABEL"
echo "  node:   $NODE"
echo "  server: $DIR/dash-server.mjs"

# Free port 4321: stop any dash-server we don't manage (manual start.sh, etc.)
EXISTING="$(pgrep -f 'dash-server.mjs' || true)"
if [ -n "$EXISTING" ]; then
  echo "  stopping existing dash-server P(s): $EXISTING"
  kill $EXISTING 2>/dev/null || true
  sleep 1
fi

cat > "$PLIST" <<PLISTEOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key><string>${LABEL}</string>
  <key>ProgramArguments</key>
  <array>
    <string>/bin/bash</string>
    <string>${DIR}/server-launch.sh</string>
  </array>
  <key>WorkingDirectory</key><string>${DIR}</string>
  <key>RunAtLoad</key><true/>
  <key>KeepAlive</key><true/>
  <key>LimitLoadToSessionType</key><string>Aqua</string>
  <key>ProcessType</key><string>Interactive</string>
  <key>StandardOutPath</key><string>${LOGDIR}/bdos-dash-server.out.log</string>
  <key>StandardErrorPath</key><string>${LOGDIR}/bdos-dash-server.err.log</string>
  <key>EnvironmentVariables</key>
  <dict>
    <key>PATH</key><string>$(dirname "$NODE"):${PYBIN_DIR}:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin</string>
  </dict>
</dict>
</plist>
PLISTEOF

echo "  wrote: $PLIST"

# Reload cleanly (bootout old if present, then bootstrap).
launchctl bootout "gui/$(id -u)/${LABEL}" 2>/dev/null || true
launchctl bootstrap "gui/$(id -u)" "$PLIST" 2>/dev/null || launchctl load -w "$PLIST"
launchctl enable "gui/$(id -u)/${LABEL}" 2>/dev/null || true

sleep 2
echo ""
echo "Status:"
launchctl print "gui/$(id -u)/${LABEL}" 2>/dev/null | grep -E "state|pid" | head -3 || true
echo ""
if curl -s --max-time 5 http://localhost:4321/health >/dev/null 2>&1; then
  echo "OK — dashboard server is up at http://localhost:4321/ and will auto-start at login."
else
  echo "Loaded, but /health not answering yet. Check: tail -f $LOGDIR/bdos-dash-server.err.log"
fi
echo "Note: do not run start.sh manually anymore; launchd owns the server now."
echo "To remove: bash $DIR/uninstall-autostart.sh"
