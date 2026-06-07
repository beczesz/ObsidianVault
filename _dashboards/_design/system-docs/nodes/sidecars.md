---
id: sidecars
title: JSON sidecars
layer: data
purpose: |
  Read-only JSON export fájlok a `_dashboards/_design/` mappában.
  A szerver írja ezeket az adatbázis-változások alapján; a dashboardok
  fetch()-csel olvassák statikus HTTP-n keresztül. Nincs közvetlen DB
  hozzáférés a böngésző oldaláról.
depends_on: []
status_endpoint: /health (component: sidecars)
index_schema_version: 1
---

## Miért létezik

A böngésző nem tud közvetlenül SQLite adatbázishoz csatlakozni.
A sidecar JSON-ok a megoldás: a szerver folyamatosan frissen tartja ezeket
az adatbázis-változások alapján, és a dashboardok egyszerű `fetch()`-csel
olvassák őket — nincs külön API hívás az összetett lekérdezésekhez.

## Létező sidecar fájlok

| Fájl | Tartalom | Frissítés |
|------|----------|-----------|
| `agent_logs.json` | agent_logs tábla sorai + scheduled_jobs | minden agent_log insert után |
| `vault_stats.json` | indexed/total fájlszám, tier2 count, freshness | minden reindex után |
| `marketing_board.json` | Presto marketing kanban állapot | scan_marketing_board.py futásakor |

## Schema (agent_logs.json)

```json
{
  "schema_version": "2",
  "generated_at": "2026-05-30T...",
  "events": [...],
  "scheduled_jobs": [...]
}
```

## Megjegyzés

A sidecar JSON-ok **derived** artifact-ok — a vault_md és az obs_db
a forrás. Ha egy sidecar elvész, a szerver újra generálja.
