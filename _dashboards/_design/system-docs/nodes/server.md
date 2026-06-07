---
id: server
title: dash-server.mjs
layer: server
purpose: |
  A BDOS központi Node.js szervere (zero-dep, ES module). Port 4321-en
  fut, és egyszerre látja el a REST API, az SSE stream, a statikus
  fájlszolgáltatás és a fs.watch feladatokat — egy folyamatban.
  launchd LaunchAgent tartja életben a gép indulásától.
depends_on: [ep_health, ep_process, ep_capture, ep_search, static_server, fs_watch]
status_endpoint: /health
index_schema_version: 1
---

## Miért létezik

A dash-server az a folyamat, amely összeköti a vault markdown-tartalmát
a böngésző-alapú dashboardokkal. Szándékosan zero-dependency Node.js: nincs
Express, nincs npm install, nincs build step — csak Node beépített moduljai
(`http`, `fs`, `path`, `child_process`). Ez garantálja, hogy bármely macOS
gépen elindítható egyetlen `node` paranccsal.

A single-server modell (2026-05-29 óta) megszüntette a port 4322-es
`events_server.py` különválasztást — az SSE most is a 4321-es porton fut.

## Főbb feladatok

- **Routing**: URL path alapján a megfelelő handler-nek adja a kérést
- **SSE broadcast**: kliens-listát tart fenn, változáskor mindenkinek küld
- **Static file serving**: a `/_dashboards/` URL-prefix alatt statikus HTML-t és JS-t szolgál
- **Health aggregation**: a `/health` válaszba összegyűjti az összes komponens státuszát
- **Child process management**: Claude CLI spawn + timeout kezelés

## Indítás

```bash
node "/path/to/0. Ideas Vault/_dashboards/_tools/dash-server.mjs"
# Listening on http://localhost:4321
```

launchd plist: `~/Library/LaunchAgents/com.bdos.dash-server.plist`

## Kapcsolódó fájlok

- `_dashboards/_tools/dash-server.mjs` — a forrás
- `_dashboards/_tools/start.sh` — kényelmi indító script
