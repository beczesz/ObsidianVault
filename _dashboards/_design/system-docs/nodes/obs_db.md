---
id: obs_db
title: agent_observability.db
layer: data
purpose: |
  SQLite adatbázis az összes agent operacionális eseményének tárolásához.
  28 oszlopos `agent_logs` tábla, 15 event type, 6 log level.
  A sidecar JSON (`agent_logs.json`) ebből generálódik auto-refresh-csel.
  A dashboardok ezt a sidecar-t olvassák, nem közvetlenül a DB-t.
depends_on: []
status_endpoint: /health (component: obs_db)
index_schema_version: 1
---

## Miért létezik

Az agent-family tevékenységének strukturált naplózása lehetővé teszi
a Maestro számára, hogy mintákat észleljen (reflect mód), és a per-agent
dashboardok számára, hogy megmutassák az agent saját tevékenységét.
Ez az Observability v2 (Phase 5) infrastruktúra alapja.

## Schema (főbb táblák)

- `agent_logs` — 28 oszlop: event_id, agent_name, model, event_type,
  status, message, mode, project, duration_ms, input_tokens, output_tokens,
  session_id, tags, created_at...
- `scheduled_jobs` — job_id, job_name, agent_name, schedule_type,
  last_run_at, next_run_at, enabled, requires_approval

## Writer API

```python
from agent_log import AgentLogger
log = AgentLogger(agent='curator', model='claude-sonnet-4-6')
log.start(mode='tend', project='system-dashboard')
log.dashboard_update('system.html 0.1.0 → 0.2.0')
log.end(status='success', input_tokens=12000, output_tokens=3000)
```

## Sidecar

A `_dashboards/_design/agent_logs.json` fájl auto-refresh-csel frissül
minden insert után. Ez a dashboardok által olvasott read-only export.

## Kapcsolódó

- [Maestro — BDOS Observatory](/_dashboards/maestro/index.html)
- [Scheduler dashboard](/_dashboards/scheduler/index.html)
