---
title: Alfred Tasks — BDOS Improvements
date: 2026-05-29
author: Becze Szabolcs
status: active
description: BDOS architektúra-fejlesztési backlog, a 2026-05-29 multi-AI study (ChatGPT + Gemini) javaslataiból destillálva. Prioritás szerint rendezve (now-tier ⏫ = architektúra-higiénia, next-tier 🔼 = capability). Minden tételt egyenként átvizsgálunk (mi az / hogyan / miért / haszon / nettó hatás) implementálás előtt. Forrás: 00_Prompts/BDOS/brainstorm/2026-05-29_bdos-architectural-evolution-analysis.md.
tags: [alfred, todos, bdos, architecture, backlog]
id: a5408853-618d-45c7-ab6f-dacd980dd77f
index_schema_version: 1
bdos_index: true
agent: alfred
schema: alfred.todos.v1
scope: bdos
---

# BDOS Improvements — Tasks

Forrás: [2026-05-29 architectural evolution study](../../../../00_Prompts/BDOS/brainstorm/2026-05-29_bdos-architectural-evolution-analysis.md). Sorrend = a study merged recommendation stack-je.

## Active

### Now-tier (architektúra-higiénia, alacsony súrlódás, magas hatás)
- [x] B1 — Architecture Boundary Document: forrás-az-igazságra szabályok rögzítése data-class-onként ⏫ #bdos → [ARCHITECTURE_BOUNDARIES.md](../../../../00_Prompts/BDOS/ARCHITECTURE_BOUNDARIES.md) (active, 2026-05-29; agent-log split ratifikálva)
- [x] B2 — Local event/state layer (v0.1): events tábla + emit_event() API + WAL/busy_timeout hardening ⏫ #bdos → events.py + events_schema.sql + runtime.connect(); vault.db WAL (2026-05-29). Reactor (event→dispatch) elhalasztva B6-ra.
- [x] B3 — Agent/mód-szaporodás soft-gate + Presto-mód drift-audit ⏫ #bdos → audit: a 26 mód külön skill-fájl + MARKETING_OS_SCHEMAS_v2 kanonikus réteg = nincs monolit-drift. Soft-gate rögzítve a BDOS/CLAUDE.md Alapelvekben (2026-05-29).
- [x] B4 — Per-agent capability/permission modell ⏫ #bdos → [CAPABILITY_MODEL.md](../../../../00_Prompts/BDOS/CAPABILITY_MODEL.md) (active, 2026-05-29; hook bekötve)

### Next-tier (capability, közepes komplexitás)
- [x] B5 — Alfred capture→process slice (v0.1): dashboard capture box → POST /api/alfred/process → Claude Code CLI (Sonnet) decomposes 1 paste → N tasks (scope/due/priority/tags) → todos/<scope>.md → SSE refresh 🔼 #bdos → dash-server.mjs tiered endpoint (CC→Haiku→capture), localhost-only, emit capture.processed (2026-05-29). LIVE Sonnet validálva a user authed Terminal-szerverén (process-cc, 3 task).
- [x] B5.0 — Auto-start + UI integráció: macOS LaunchAgent (com.bdos.dash-server, RunAtLoad+KeepAlive) install/uninstall scriptek + server-launch.sh wrapper; /health alfred_processor tier+auth (launchd-aware); Alfred dashboard masthead tier-pill (v0.4.4). ⚠️ launchd nem éri el a login-keychaint (headless 401) → Sonnet tier SUBSCRIPTION-alapon (NEM API-cost): `claude setup-token` → CLAUDE_CODE_OAUTH_TOKEN a ~/.bdos/anthropic.env-be → kickstart. User-action: token-generálás + beillesztés. Mac: LIVE process-cc validálva subscription-tokennel. Windows-parity: install/uninstall-autostart.ps1 + server-launch.ps1 (Task Scheduler, logon + 5-min supervisor), ugyanaz a CLAUDE_CODE_OAUTH_TOKEN flow (Windows-on futtatandó + tesztelendő). #bdos
- [ ] B6 — Agent execution fabric formalizálása: determinisztikus state machine + validált handoff-sémák 🔼 #bdos
- [ ] B7 — Inkrementális dashboard-fordítás: file-watcher → részleges rebuild, nem teljes vault-parse 🔼 #bdos
- [ ] B8 — Hibrid retrieval ott, ahol az FTS5 elbukik: könnyű lokális vektor-index a Librariannek 🔼 #bdos

## Explicitly deferred / declined (a study alapján)
- Cloud sync / Firebase mint kanonikus store — split-brain kockázat (discouraged)
- Dedikált gráf-DB (Neo4j) — a markdown wiki-linkek a gráf (discouraged)
- Multi-user collaboration — stratégiai később, most túl drága (deferred)

## Archive

<!-- Alfred a kipipált tételeket ide mozgatja. Semmi nem törlődik. -->
