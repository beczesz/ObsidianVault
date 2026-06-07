---
from: server
to: obs_db
protocol: SQL write/read
direction: server → SQLite (write-primary)
payload: agent event rows
label: agent events
id: 208c8919-e677-4b55-a12f-197c16a3b10e
index_schema_version: 1
---

## Kapcsolat

A dash-server `agent_log.py` writer API-ján keresztül írja az operacionális
eseményeket az `agent_observability.db` `agent_logs` táblájába. A sidecar
JSON (`agent_logs.json`) auto-refresh-csel frissül minden insert után.

## Writer API

```python
from agent_log import AgentLogger, log_event

log = AgentLogger(agent='curator', model='claude-sonnet-4-6')
log.start(mode='tend', project='system-dashboard')
log.tool('Edit', 'system.html version bump', duration_ms=45)
log.dashboard_update('system.html 0.1.0 → 0.2.0 — graph layout')
log.end(status='success', input_tokens=12000, output_tokens=3000)
```

## INSERT séma (fő mezők)

```sql
INSERT INTO agent_logs
  (event_id, agent_name, model, event_type, status, message, mode,
   project, duration_ms, input_tokens, output_tokens, tags, created_at)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, datetime('now'));
```

## Sidecar auto-refresh

Minden INSERT után a Python writer újragenerálja a sidecar JSON-t:

```python
with open('_dashboards/_design/agent_logs.json', 'w') as f:
    json.dump({
        'schema_version': '2',
        'generated_at': datetime.utcnow().isoformat(),
        'events': rows,
        'scheduled_jobs': jobs
    }, f)
```

## Olvasás (dashboardból)

```js
const r = await fetch('/_dashboards/_design/agent_logs.json', { cache: 'no-store' });
const { events, scheduled_jobs } = await r.json();
const curatorEvents = events.filter(e => e.agent_name === 'curator');
```
