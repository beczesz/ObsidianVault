---
title: Alfred Prepared-Task Dossier Store — konvenció + queue-index
date: 2026-06-07
author: Becze Szabolcs
status: active
description: Alfred v0.4 Cognitive Triage Engine kimenetének belépője. Leírja a prepared-task dossier sémát (alfred.task.v1), a queue-rendezést (prioritás + státusz), és a multi-agent contribution-tracking konvenciót (közös task_id). A `next` mód ezt a queue-t szolgálja fel riportként; a dashboard napi cockpitja ezt rendereli. Forrás-az-igazságra a markdown.
tags: [alfred, tasks, dossier, triage, queue, convention]
id: 85ab8bb7-3d5e-4e55-8b52-0bb5fffa67ce
index_schema_version: 1
bdos_index: true
agent: alfred
schema: alfred.tasks-index.v1
---

# Alfred Prepared-Task Dossier Store

> **Mi ez:** a `triage` mód kimenete. Egy *dosszié* = egy email-eredetű (vagy manuális) feladat teljes munkaterülete: az eredeti igény, a multi-agent feldolgozás nyoma (timeline), az előkészített válasz-draft, az actionable-ök, és a státusz. Ez az, amit a `next` riportként felszolgál ("most az X feladaton dolgozunk, így próbáltam megoldani, itt tartunk"), és amit a dashboard napi cockpitja renderel.

> **Megkülönböztetés a `todos/`-tól:** a `todos/<scope>.md` az **atomi, egysoros** teendőké. A `tasks/<…>.md` a **kontextusos, multi-agent feladat-csomagoké**. Egy dosszié actionable itemjei `todo`-vá promote-olhatók.

## Dossier-fájl

Egy dosszié: `tasks/<YYYY-MM-DD>_<slug>.md`, séma `alfred.task.v1`. A teljes séma + kötelező body-szekciók: [`../../../../00_Prompts/BDOS/agents/alfred.md`](../../../../00_Prompts/BDOS/agents/alfred.md) §5b. Sablon: [`_template.md`](_template.md).

Frontmatter kulcsmezők: `task_id` (stabil slug = az agent_logs task_id is), `task_status` (prepared/in-review/actioned/done/dismissed), `priority` (high/med/low), `source` (channel/thread_id/subject/from), `agents_involved`.

## Multi-agent contribution-tracking

A dosszié `task_id`-ja a közös kulcs. Minden hozzájárulás (a) beíródik a dosszié `## Agent-hozzájárulások (timeline)` szekciójába (kanonikus, ember-olvasható), és (b) tükröződik az `agent_logs`-ba `AgentLogger(task_id=<slug>)`-gel (queryable). Így „ki, mit, milyen sorrendben" mindkettőből előbányászható:

```sql
SELECT agent_name, event_type, title, timestamp
FROM agent_logs WHERE task_id = '<dosszié-slug>' ORDER BY timestamp;
```

## Queue (prioritás-sorrend)

A `next` mód ezt a sorrendet követi: `priority` (high → med → low), azon belül `due` (közelebbi előrébb), azon belül `received` (régebbi előrébb). Csak a `prepared` és `in-review` dossziék szerepelnek a queue-ban.

### Aktív queue

> Üres. A `triage` mód tölti fel. (Még nem futott éles triage.)

| # | task_id | priority | status | scope | source | due |
|---|---------|----------|--------|-------|--------|-----|
| – | – | – | – | – | – | – |

### Lezárt (archív)

> A `done` / `dismissed` dossziék ide kerülnek a sorrendből (a fájl megmarad a `tasks/`-ban, sosem törlődik).

| task_id | status | lezárva | jegyzet |
|---------|--------|---------|---------|
| – | – | – | – |
