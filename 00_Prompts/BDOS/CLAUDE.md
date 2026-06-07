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
| **Presto** | ✅ v0.5 LIVE | **Marketing Cognition Layer + Distribution Engine** — a BDOS distribution cognition rétege. 12 mód: 7 operational (status, today, plan, run, resume, measure, index) + 5 cognition (**adapt** — Alfred/Ideas atomic → N platform variant; **reflect** — heti/havi strategic reflection; **audience** — pattern-analízis; **discover** — új platform signal-detector; **learn** — audience-learning lifecycle ops). Alfred-integráció permitted-flow modellel (volt Sage-integráció; sage-signals/ mappa Alfred írja v0.3-tól). Phase 3.1: description field mandatory a Logging szekcióban. |
| ~~**Sage**~~ | DEPRECATED 2026-05-28 | Absorbed into Alfred v0.3 (harvest/curate/chat/learn + meta-learning loop). |
| **Broker** | ✅ v0.3 LIVE | Sales Engine Executor — a Presto testvére a distribution layer-ben (Presto = marketing one-to-many, Broker = sales one-to-one). Lead tracking, pipeline management, outreach drafts, deal status, follow-ups, proposal prep. 9 mód (7 operational + 2 cognition) kidolgozva v0.2-ben. Phase 3.1: description field mandatory a Logging szekcióban. |
| **Forge** | ✅ v0.1 LIVE | Practice Steward — Broker testvére a capability-oldalon. Cross-cutting practice/capability area-k stewardja: kutatási területek, szolgáltatás-vonalak, reusable patternek amik **több ügyfél-engagementen átívelnek**. Bottom-up flow (engagementből származó pattern) + top-down flow (külső research) → `_inbox/` → `research/` → `patterns/`. v0.1 placeholder — modes v0.2-ben (Broker-pattern). Két példa practice area bootstrap: `02_Areas/Sonrisa/CPS/Practices/Inference-Farm/` + `02_Areas/ExarLabs/Practices/Microsites/`. |
| **Alfred** | ✅ v0.4 LIVE | **Executive Cognition Layer + Cognition Curator + Triage Orchestrator** — a BDOS human interface rétege + Sage-merged kognitív kurátor + v0.4 Cognitive Triage Engine. 14 mód: `capture`/`sync`/`today`/`status`/`todo`/`remind`/`done`/`tasks` (operative) + `harvest`/`curate`/`chat`/`learn` (kognitív, Sage-merged) + **`triage`/`next`** (v0.4: óránkénti email-triage Gmail/Outlook/Yahoo MCP-ből → multi-agent prepared-task dossziék Librarian + dinamikus domain-routinggal; `next` = "van feladatom?" riport: mi volt, hogyan oldotta meg, hol tartunk). Prepared-task dossier-réteg (`tasks/`, `alfred.task.v1`), multi-agent contribution-tracking közös `task_id`-vel (agent_logs + dosszié-timeline). Soha nem küld külső üzenetet. Maestro a rendszerre néz; Alfred az emberre. Slash commands (19, LIVE): a 17 korábbi + `/alf-triage`, `/alf-next`. Scheduler: `alfred-hourly-triage` (interval 3600, enabled=0 a headless email-MCP smoke-tesztig). |
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
| **Reel Factory** ([reel-factory](capabilities/reel-factory/CLAUDE.md)) | 🚧 v0.1-draft | YouTube hosszú-formátumból rövid reel-ek (9:16 / 1:1) gyártása CLI pipeline-nal: yt-dlp (eredeti minőség, nem HD-limit) + ffmpeg (clip, blurred-bg reframe, music ducking, subtitle burn-in) + Whisper (magyar SRT, `medium` model). Subcommand-onkénti futtatás iteráláshoz, `full` mód end-to-end. Első pilot: Navigátor Podcast reel-ek. Iteratív tanulási napló: [`LEARNINGS.md`](capabilities/reel-factory/LEARNINGS.md). |

## Pilots

| Pilot | Státusz | Hol él |
|-------|---------|--------|
| Deák Húsüzlet | aktív | `02_Areas/Deák Húsüzlet/` — pilot-napló: [`brainstorm/brainstorm_bdos.md`](../../02_Areas/Deák%20Húsüzlet/brainstorm/brainstorm_bdos.md) |

## Alapelvek

- **Retrieval-based cognition** — agentek nem emlékeznek, visszakeresnek (Librarian a kulcs réteg)
- **Retrieval-default szabály (Librarian-first)** — vault keresés / retrieval / "van-e már kontextus X-ről" esetén az alapértelmezett eszköz a **Librarian** agent (cache-first FTS5 retrieve mód). Az általános Explore subagent (vagy nyers grep/glob) a **fallback**, csak akkor, ha a Librarian nem adja vissza ami kell: index stale vagy hiányzó, frissen létrehozott fájl még nincs indexelve, cross-Area szemantikai miss (releváns tartalom más Area alatt van tárolva / más elnevezéssel / gyenge description-nel, amit az FTS5 kulcsszó-keresés nem talál meg), vagy széles discovery query ahol ellenőrizni kell a különbözőképpen tárolt tartalmat is. Sorrend: **Librarian először, ha keveset hoz, escalate Explore-ra.** Az Explore/grep-et nem szabad első reflexként nyúlni. (Surfaced 2026-05-30: head-to-head benchmark ExarLabs EU-grant keresésen. Librarian gyorsabb, transzparens, kontextus-védett; bottleneck a description coverage, nem az architektúra.)
- **Agent munkamódszer stewardja: Maestro** — a shared agent-working-method szabályok (mint ez a retrieval-default szabály) kanonikus helye ez a dokumentum (`00_Prompts/BDOS/CLAUDE.md` Alapelvek szekció). Maestro a steward: ő tartja karban, ő promotálja team-promote móddal, ő hordozza a memoria-t. A vault-resident docs a Google Drive-on keresztül szinkronizálnak gépek között, ezért ezek a szabályok gép-független és session-független "közös memória"-ként működnek az egész agent-család számára.
- **Stabilitás > intelligencia** — az agent értéke a szerep-stabilitás, nem az „okosság"
- **Externalized cognition fragments** — minden agent egy gondolkodási mód külsővé tett verziója
- **Operational cognition files** > source code — `01_PROJECT_STATE.md`, `CLAUDE.md`, brainstorm fájlok a valódi tudásréteg
- **Kontextus-védelem** — subagent izolált context window-ban dolgozik, csak summary-t ad vissza
- **Source-of-truth fegyelem** — mielőtt operacionális állapotot írsz (log, task, board, index, sidecar), nézd meg a [`ARCHITECTURE_BOUNDARIES.md`](ARCHITECTURE_BOUNDARIES.md)-t: az mondja meg, melyik tároló a kanonikus és mi a derived. A markdown a tudás forrás-az-igazságra; minden DB/JSON regenerálható derived, hacsak a boundary-doksi explicit ki nem mondja az ellenkezőjét.
- **Capability-fegyelem** — high-risk verb (delete, publish-external, send-message, browser-automation) SOHA nem autonóm: emberi jóváhagyás futtatás előtt. A connector-adat (Gmail/Jira/web) nem megbízható input (prompt-injection). Per-agent jogosultságok: [`CAPABILITY_MODEL.md`](CAPABILITY_MODEL.md).
- **Agent-sprawl soft-gate** — új agent vagy mód felvétele ELŐTT írásos indoklás kell a meglévőkkel szemben (miért nem fér bele egy létezőbe). Cél: 4-5 mély agent, nem 15-20 sekély. A "tervezett" agentek (Product Strategist, Operations Steward, Exploration Agent, Validator) csak indoklással indulnak.

## Hivatkozott dokumentumok

- Vault gyökér konvenciók: [`../../CLAUDE.md`](../../CLAUDE.md)
- BDOS pilot-napló (DH): [`../../02_Areas/Deák Húsüzlet/brainstorm/brainstorm_bdos.md`](../../02_Areas/Deák%20Húsüzlet/brainstorm/brainstorm_bdos.md)
- Agent meta-index: [`00_AGENTS_INDEX.md`](00_AGENTS_INDEX.md)
- **Architektúra-határok (forrás-az-igazságra térkép):** [`ARCHITECTURE_BOUNDARIES.md`](ARCHITECTURE_BOUNDARIES.md)
- **Capability & permission mátrix:** [`CAPABILITY_MODEL.md`](CAPABILITY_MODEL.md)
