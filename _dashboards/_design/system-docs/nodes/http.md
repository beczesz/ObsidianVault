---
id: http
title: HTTP REST
layer: transport
purpose: |
  A localhost:4321-en futó dash-server HTTP rétege. A dashboard-ok
  fetch()-csel hívják a REST végpontokat (GET /health, GET /api/search,
  POST /api/alfred/capture, POST /api/alfred/process, POST /api/cli/run stb.).
depends_on: [server]
status_endpoint: /health (component: http)
index_schema_version: 1
---

## Miért létezik

Az HTTP réteg az a transport csatorna, amelyen keresztül a kliens-oldali
JavaScript kommunikál a szerver-oldali logikával. Minden nem-SSE interakció
ezen megy át: health polling, search queries, capture requests, CLI invocations.

## Főbb endpoint-ok

| Endpoint | Method | Leírás |
|----------|--------|--------|
| `/health` | GET | Komponens-státusz térkép (overall + components) |
| `/api/search` | GET | FTS5 vault keresés (`?q=...`) |
| `/api/alfred/capture` | POST | Gyors inbox append |
| `/api/alfred/process` | POST | AI-alapú task parse + vault write |
| `/api/cli/run` | POST | Ad-hoc Claude CLI hívás |
| `/api/db/schema` | GET | Adatbázis séma (vault.db + obs.db) |
| `/api/reindex` | POST | vault.db újraindexelés |

## Példa

```bash
curl -s http://localhost:4321/health | jq .overall
# "ok"

curl -s "http://localhost:4321/api/search?q=Alfred" | jq '.results[0].title'
```

## Megjegyzés

A dash-server localhost-only — nincs külső hálózati hozzáférés, nincs auth.
Ez egy fejlesztői / személyi operations tool, nem public-facing service.
