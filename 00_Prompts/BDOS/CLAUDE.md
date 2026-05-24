---
title: BDOS — Business Development Operation System
version: 0.1
date: 2026-05-11
author: Becze Szabolcs
status: active
description: A BDOS kanonikus belépő — mi a BDOS, hogyan épül fel, hol vannak az agentek, capability-k, pilotok. Minden BDOS-tartalom első olvasandó dokumentuma.
id: c0eaac29-1f2f-42f8-bf1f-aadd2092813a
index_schema_version: 1
---

# BDOS — Business Development Operation System

## Mi a BDOS

A BDOS **AI-native cognition system** — nem playbook, nem framework. Három rétegből áll:

1. **Agents** — stabil gondolkodási szerepek (`agents/`)
2. **Capabilities** — projekt-független képesség-csomagok (`capabilities/`), amik agentekből + workflow-kból + infra-konvenciókból állnak
3. **Pilots** — élő projektek, ahol a BDOS-t validáljuk (`pilots/`)

A BDOS célja: bármely vault-beli projekt (DH, Sonrisa, Ignis Academy, ExarLabs, Navigátor) ugyanazt az AI-szövetet használja — stabil szerepekkel, perzisztens markdown-állapottal, Claude Code orchestrációval.

A BDOS rétegtípus, **nem** domain. Ezért él a `00_Prompts/` alatt (meta-szint), nem az `02_Areas/`-ban.

## Struktúra

```
00_Prompts/BDOS/
├── CLAUDE.md                  ← ITT — meta, belépő
├── 00_AGENTS_INDEX.md         ← minden agent egy listán (Librarian + tervezettek)
├── principles.md              ← elvek és invariánsok (TODO)
├── agents/
│   ├── librarian.md           ← kanonikus agent-definíciók (`<name>.md`)
│   └── maestro.md             ← Brand-to-Site Conductor (Brand Spine pipeline)
├── capabilities/
│   ├── brand-to-site/         ← Brand Spine — alkotmány→site mentális modell (design)
│   └── web-publishing/        ← AI-assisted microsite factory (kidolgozás alatt)
├── tools/
│   └── INVENTORY.md           ← teljes plugin-leltár: Cowork + Official + 3rd-party, Brand Spine mapping
└── pilots/
    └── deak-husuzlet.md       ← élő pilot pointerek
```

A Claude Code runtime-regisztrációk (thin pointerek) továbbra is a `.claude/agents/` alatt élnek — két fájl/agent (canonical + registration), verzió-szinkronnal. Lásd `00_AGENTS_INDEX.md`.

## Aktív agentek

| Agent | Státusz | Cél |
|-------|---------|-----|
| **Librarian** | ✅ v0.7 LIVE | Knowledge Manager — 6 mód (index, retrieve, tidy, audit, integrate, deep-clean) + PDF olvasás. Phase 3.1: description field mandatory a Logging szekcióban. |
| **Maestro** | ✅ v0.5 LIVE | **Conductor + Reflective Nervous System** — három karmestere a műnek. **Brand-to-Site domain (5 mód):** brand→site projekt-navigáció. **Agent Family domain (4 mód):** team-status / team-audit / **`team-promote`** / **`team-introduce`**. **Observability domain (3 mód — Phase 2 Constitution):** `observe` (aggregálja a 3 family log-streamet — Operational/Learning/Version), `reflect` (minta-felismerés + javaslatok), `optimize` (reflect-javaslat végrehajtása dry-run + confirmation + Version Log). Maestro a BDOS reflektív idegrendszere. Phase 3.1: description field mandatory a Logging szekcióban. |
| **Curator** | ✅ v0.4 LIVE | Representation layer kurátor — a `_dashboards/` HTML dashboard-család mestere, 7 mód (survey, build, tend, retire, audit, serve, promote). Élő index, build a recept + DESIGN_SYSTEM alapján, family-audit, promote a tanult mintára. Phase 3.1: description field mandatory a Logging szekcióban. |
| **Presto** | ✅ v0.5 LIVE | **Marketing Cognition Layer + Distribution Engine** — a BDOS distribution cognition rétege. 12 mód: 7 operational (status, today, plan, run, resume, measure, index) + 5 cognition (**adapt** — Sage atomic → N platform variant; **reflect** — heti/havi strategic reflection; **audience** — pattern-analízis; **discover** — új platform signal-detector; **learn** — audience-learning lifecycle ops). Sage-integráció permitted-flow modellel. Phase 3.1: description field mandatory a Logging szekcióban. |
| **Sage** | ✅ v0.4 LIVE (scheduling pending) | Cognition Curator — a BDOS cognition layer-jének operátora. 5 mód (harvest, curate, chat, learning-ops, info). Naponta 06:00-kor harvest, hétfő 06:05-kor curate. Meta-learning loop. Csend default. Phase 3.1: description field mandatory a Logging szekcióban. |
| **Broker** | ✅ v0.3 LIVE | Sales Engine Executor — a Presto testvére a distribution layer-ben (Presto = marketing one-to-many, Broker = sales one-to-one). Lead tracking, pipeline management, outreach drafts, deal status, follow-ups, proposal prep. 9 mód (7 operational + 2 cognition) kidolgozva v0.2-ben. Phase 3.1: description field mandatory a Logging szekcióban. |
| Product Strategist | tervezett | BD stratégia, retention, second-order probability |
| Operations Steward | tervezett | Sprint, workflow, repo hygiene, deploy safety |
| Exploration Agent | tervezett | Radikális ötletek, fork-szerű exploráció |
| Validator | tervezett | Cross-check, második vélemény |

Részletes meta-index: [`00_AGENTS_INDEX.md`](00_AGENTS_INDEX.md). Cél: **4-5 agent**, nem 15-20 (agent sprawl elkerülése).

## Capabilities

| Capability | Státusz | Mit ad |
|------------|---------|--------|
| **Brand Spine** ([brand-to-site](capabilities/brand-to-site/CLAUDE.md)) | 🚧 design (v0.2) | Mentális modell + munkamódszer: mi rejlik egy komplex, gyönyörű, de letisztult marketing weboldal mögött. v0.2 — 7 rétegű „Decision Spine" + Pulse loop + Lean/Standard/Premium tier-ek (multi-AI brainstorm alapján). Nevesített frameworkök (Dunford, StoryBrand, JTBD, Kapferer, Atomic Design, Content-First) + tool-stack (`brand-toolkit`, `impeccable`, `ui-ux-pro-max`+`ux-pilot`, `designer-skills`, `marketingskills`, `Dembrandt`, `Tokven`). Diagram: [`diagram.html`](capabilities/brand-to-site/diagram.html). Brainstorm: [`brainstorm/brainstorm_brand-spine.md`](brainstorm/brainstorm_brand-spine.md). A Microsite Factory upstream rétege. |
| **Microsite Factory** ([web-publishing](capabilities/web-publishing/CLAUDE.md)) | 🚧 design | AI-assisted microsite factory — generálás → polish → deploy (Cloudflare/Netlify API) → DNS → SSL. Bármely projekthez használható, később Ignis Academy tananyaggá exportálható. A Brand Spine downstream rétege. |
| **Vault Dashboards** ([vault-dashboards](capabilities/vault-dashboards/CLAUDE.md)) | ✅ active (v0.1) | Repeatable módszer élő, read-only, markdown-vezérelt HTML dashboardok építésére bármely vault-egységhez. Két working reference (CPS Sales v0.6, CPS Partnerships v0.1) + a root tree launcher (v0.2) alapján. Tartalmazza: design tokenek, YAML + section parserek, fetch+8s sync, sync indicator, home button, versioning, build recipe + checklist. Bármely "építs dashboardot X-hez" kérés első olvasandó doksija. |
| **Think Engine** ([think-engine](capabilities/think-engine/CLAUDE.md)) | ✅ active (v0.9) | Semi-autonomous multi-AI orkesztráció — Claude mint karmester több AI-t (Opus, GPT-5, Perplexity, Copilot, második Claude-szál) hangol össze, API + Chrome MCP hibrid transporttal. Lényeg: a state file a tartós agy, az AI-ok cserélhető gondolkodási felületek; egy kör hossza = max(leglassabb tag). A vault brainstorm-jai ezzel készülnek. Kanonikus skill: `think-agent-orchestrator-v09`. Csapat-bemutató: [`bemutato.html`](capabilities/think-engine/bemutato.html). |
| **Vault Indexing** ([vault-indexing](capabilities/vault-indexing/CLAUDE.md)) | ✅ active (v0.1) — **Phase 3 first capability** | SQLite read-cache a vault markdown frontmatterjeire + wikilinkjeire. **A markdown forrás-az-igazságra** — az SQLite egy regenerálható cache, NEM write-target. 3295 fájl indexelve ~4 mp alatt, 2.4 MB DB. Lenient YAML fallback (Hungarian-typographic-quote-os fájlokra), FTS5 full-text a description+title-en, backlink graph + orphan detection. Python query API + CLI. Librarian research §3 (token optimization) javaslata: **10-100x retrieve token-reduction** lehetséges, ha agentek cache-first-eznek full-file-read előtt. Roadmap: v0.2 watchdog incremental + Librarian/Maestro integráció. |

## Pilots

| Pilot | Státusz | Hol él |
|-------|---------|--------|
| Deák Húsüzlet | aktív | `02_Areas/Deák Húsüzlet/` — pilot-napló: [`brainstorm/brainstorm_bdos.md`](../../02_Areas/Deák%20Húsüzlet/brainstorm/brainstorm_bdos.md) |

## Alapelvek

- **Retrieval-based cognition** — agentek nem emlékeznek, visszakeresnek (Librarian a kulcs réteg)
- **Stabilitás > intelligencia** — az agent értéke a szerep-stabilitás, nem az „okosság"
- **Externalized cognition fragments** — minden agent egy gondolkodási mód külsővé tett verziója
- **Operational cognition files** > source code — `01_PROJECT_STATE.md`, `CLAUDE.md`, brainstorm fájlok a valódi tudásréteg
- **Kontextus-védelem** — subagent izolált context window-ban dolgozik, csak summary-t ad vissza

## Hivatkozott dokumentumok

- Vault gyökér konvenciók: [`../../CLAUDE.md`](../../CLAUDE.md)
- BDOS pilot-napló (DH): [`../../02_Areas/Deák Húsüzlet/brainstorm/brainstorm_bdos.md`](../../02_Areas/Deák%20Húsüzlet/brainstorm/brainstorm_bdos.md)
- Agent meta-index: [`00_AGENTS_INDEX.md`](00_AGENTS_INDEX.md)
