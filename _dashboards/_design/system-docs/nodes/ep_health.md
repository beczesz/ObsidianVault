---
id: ep_health
title: /health endpoint
layer: server
purpose: |
  A dash-server `/health` GET végpontja. JSON választ ad az összes
  komponens aktuális státuszáról: overall (ok/warn/gap) és per-komponens
  {status, detail, metric, last_checked} objektumok. A dashboard-ok
  5 másodpercenként lekérdezik.
depends_on: [server]
status_endpoint: /health
index_schema_version: 1
---

## Miért létezik

A `/health` endpoint az operacionális "truth surface" — minden dashboard
és az AdminBar ebből tudja meg, mi fut és mi nem. Az egységes health API
lehetővé teszi, hogy a System dashboard egy vizuális gráfban jelenítse
meg az összes komponens állapotát.

## Válasz formátum

```json
{
  "overall": "ok",
  "components": {
    "server": { "status": "ok", "detail": "listening on 4321", "metric": null, "last_checked": "2026-05-30T..." },
    "vault_db": { "status": "ok", "detail": "3295 files indexed", "metric": "3295 recs", "last_checked": "..." },
    "claude_cli": { "status": "ok", "detail": "OAuth token valid", "metric": null, "last_checked": "..." }
  }
}
```

## Status értékek

- `ok` — komponens fut és egészséges
- `warn` — fut de degradált (pl. stale index, magas latency)
- `gap` — hiba vagy nem elérhető
- `idle` — opcionális komponens, nem indul el automatikusan

## Példa

```bash
curl -s http://localhost:4321/health | jq '{overall, components: (.components | keys)}'
```
