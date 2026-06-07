---
from: launchagent
to: server
protocol: launchd
direction: OS → process
payload: process lifecycle
id: 266e69c2-43fc-4a45-8dae-68fb1734de40
index_schema_version: 1
---

## Kapcsolat

A macOS launchd rendszer a `com.bdos.dash-server.plist` LaunchAgent leíró
alapján indítja és felügyeli a `dash-server.mjs` Node.js folyamatot.
`KeepAlive: true` beállítással crash esetén automatikusan újraindul.

## plist struktúra (példa)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" ...>
<plist version="1.0">
<dict>
  <key>Label</key>
  <string>com.bdos.dash-server</string>
  <key>ProgramArguments</key>
  <array>
    <string>/usr/local/bin/node</string>
    <string>/Users/becze-mac/My Drive .../0. Ideas Vault/_dashboards/_tools/dash-server.mjs</string>
  </array>
  <key>KeepAlive</key>
  <true/>
  <key>RunAtLoad</key>
  <true/>
  <key>StandardOutPath</key>
  <string>/tmp/bdos-dash-server.log</string>
  <key>StandardErrorPath</key>
  <string>/tmp/bdos-dash-server.err</string>
</dict>
</plist>
```

## Karbantartási parancsok

```bash
# Betöltés (egyszeri, gép újraindítás után automatikus)
launchctl load ~/Library/LaunchAgents/com.bdos.dash-server.plist

# Kézi újraindítás
launchctl kickstart -k gui/$(id -u)/com.bdos.dash-server

# Leállítás
launchctl unload ~/Library/LaunchAgents/com.bdos.dash-server.plist

# Log figyelés
tail -f /tmp/bdos-dash-server.log
```
