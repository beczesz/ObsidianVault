---
title: Alfred Triage Heartbeat & Queue State
date: 2026-06-07
author: Becze Szabolcs
status: active
description: Az óránkénti alfred-hourly-triage job heartbeat-állapota és a prepared-task queue összesítője. A dashboard napi cockpitja és a `next`/`status` módok ezt olvassák. Single source of truth a triage frissességéről. NEM tartalmaz dosszié-tartalmat (az a tasks/ alatt él).
tags: [alfred, triage, heartbeat, state, scheduler]
id: 1d562cf9-3d25-4dc0-b1fe-3ce9c5686d91
index_schema_version: 1
bdos_index: true
agent: alfred
schema: alfred.triage-state.v1
last_tick_at: null
last_triage_at: null
pending_count: 0
last_run_status: never_run
sources_status:
  gmail: unknown
  outlook: unknown
  yahoo: unknown
---

# Alfred Triage Heartbeat

> **Mit jelent:** Alfred óránként (amikor a BDOS daemon fut) megnézi az emaileket és előkészíti a válaszra váró feladatokat. Ez a fájl mutatja, mikor futott utoljára, hány előkészített feladat vár, és elérhetők-e a források. A dashboard heartbeat-pillje ebből táplálkozik. Marveen-modell: csendes, csak fontosnál szól.

## Állapot

- **Utolsó tick:** soha (a job `enabled=0`, smoke-teszt után billentjük 1-re)
- **Utolsó valódi triage:** soha
- **Pending (előkészített, döntésre váró) feladat:** 0
- **Utolsó futás státusza:** `never_run`

## Forrás-elérhetőség (legutóbbi `--auto` futás)

| Forrás | Állapot | Megjegyzés |
|--------|---------|------------|
| Gmail (exarlabs@gmail.com) | ismeretlen | headless smoke-teszt nem jutott el a connectorig (auth fal) |
| Outlook / MS365 | ismeretlen | headless smoke-teszt nem jutott el a connectorig (auth fal) |
| Yahoo Mail | ismeretlen | headless smoke-teszt nem jutott el a connectorig (auth fal) |

## Headless smoke-teszt (2026-06-07)

> **Eredmény:** a headless `claude -p` **401 Invalid authentication credentials** hibával elhasalt (ugyanaz a fal, amit a scheduler.py a harvest/curate-nél jelez). Ezért a connector-elérhetőséget headless módban nem sikerült igazolni, és az `alfred-hourly-triage` job **`enabled=0`** marad.
>
> **Az autonóm óránkénti triage bekapcsolásához:** futtasd `claude setup-token` (subscription, ingyenes), állítsd be a `CLAUDE_CODE_OAUTH_TOKEN`-t a BDOS daemon környezetében (ugyanaz a mechanizmus, amit a dash-server.mjs használ launchd alatt), majd egy sikeres `bash 00_Prompts/BDOS/agents/alfred/cron/run_hourly_triage.sh` próba után billentsd a jobot `enabled=1`-re:
> `sqlite3 <agent_observability.db> "UPDATE scheduled_jobs SET enabled=1 WHERE job_id='alfred-hourly-triage';"`
>
> **Addig is:** a `triage` mód **interaktívan** (egy Claude Code session-ben, mint most) teljesen működik — a Gmail/Outlook/Yahoo MCP + a Librarian + a domain-agentek mind elérhetők. Futtasd `/alf-triage` paranccsal, és a dossziék elkészülnek; a `next` felszolgálja őket.

## Futás-napló (utolsó néhány)

> A `triage` mód minden futáskor egy sort fűz ide: `- <ISO> · <forrás-összegzés> · <új dosszié-szám> · <státusz>`.

- 2026-06-07 · headless smoke-teszt: `claude -p` 401 auth fal · 0 dosszié · enabled=0 marad
