---
id: scheduler
title: Scheduler
layer: daemon
purpose: |
  A BDOS agent scheduler — ütemezett feladatokat futtat az
  agent_observability.db `scheduled_jobs` táblájában definiált
  időzítés szerint. Cron-like trigger logika, a dash-server.mjs-be
  integrálva.
depends_on: [server, obs_db]
status_endpoint: /health (component: scheduler)
index_schema_version: 1
---

## Miért létezik

Az agent-ek periodikus feladatai (pl. Curator weekly survey, Librarian
index frissítés) nem igényelnek emberi beavatkozást — az ütemező
automatikusan aktiválja őket a megadott időpontokban.

## Ütemezett feladatok (példák)

| Job | Mikor | Agent |
|-----|-------|-------|
| curator-weekly-survey | Hétfő 5:30 | Curator |
| curator-monthly-audit | Havonta 6:00 | Curator |
| librarian-index-refresh | Naponta 4:00 | Librarian |

A teljes lista a Scheduler dashboard "Jobs" tabján látható.

## Konfiguráció

```sql
INSERT INTO scheduled_jobs
  (job_id, job_name, agent_name, schedule_type, command, requires_approval, enabled)
VALUES
  ('curator-weekly-survey', 'Curator Weekly Survey', 'curator',
   'weekly', '/path/to/run_survey.sh', 0, 1);
```

## Kapcsolódó

- [Scheduler dashboard](/_dashboards/scheduler/index.html)
