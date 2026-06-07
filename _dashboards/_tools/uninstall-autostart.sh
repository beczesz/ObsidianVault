#!/usr/bin/env bash
# Remove the dashboard-server LaunchAgent installed by install-autostart.sh.
# After this, the server no longer auto-starts; use ./start.sh manually.
set -e
LABEL="com.bdos.dash-server"
PLIST="$HOME/Library/LaunchAgents/${LABEL}.plist"

launchctl bootout "gui/$(id -u)/${LABEL}" 2>/dev/null || launchctl unload "$PLIST" 2>/dev/null || true
if [ -f "$PLIST" ]; then rm -f "$PLIST"; echo "removed $PLIST"; else echo "no plist found at $PLIST"; fi
echo "Auto-start disabled. The running server (if any) was stopped; start manually with ./start.sh."
