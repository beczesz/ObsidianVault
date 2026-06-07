---
id: launchagent
title: LaunchAgent
layer: server
purpose: |
  A macOS launchd LaunchAgent plist-ek, amelyek a dash-server.mjs-t és
  az events_server.py daemon-t automatikusan elindítják gép induláskor
  és életben tartják (KeepAlive: true). A plist-ek a
  ~/Library/LaunchAgents/ mappában élnek.
depends_on: []
status_endpoint: /health (component: launchagent)
index_schema_version: 1
---

## Miért létezik

A BDOS operational rendszer értéke azon múlik, hogy mindig elérhető —
nem kell emlékezni manuálisan elindítani a szervert. A LaunchAgent
ezt biztosítja: gép bekapcsolásakor automatikusan indul, crash esetén
újraindul, log-ot ír a `/tmp/` mappába.

## Plist fájlok

- `~/Library/LaunchAgents/com.bdos.dash-server.plist` — dash-server.mjs (port 4321)
- `~/Library/LaunchAgents/com.bdos.daemon.plist` — events_server.py (opcionális)

## Karbantartás

```bash
# Betöltés
launchctl load ~/Library/LaunchAgents/com.bdos.dash-server.plist

# Újraindítás
launchctl kickstart -k gui/$(id -u)/com.bdos.dash-server

# Státusz
launchctl list | grep bdos

# Log
tail -f /tmp/bdos-dash-server.log
```

## Kapcsolódó

- [dash-server.mjs node](/_dashboards/_design/system-docs/nodes/server.md)
