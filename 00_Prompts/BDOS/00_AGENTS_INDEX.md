---
title: 00_AGENTS_INDEX
description: Meta-index minden BDOS agentről — canonical fájl + Claude Code registration + verzió + státusz egy helyen.
generated_by: human-manual (v0.2 audit-tól: librarian audit mode)
last_updated: 2026-05-30
phase5_observability: 2026-05-24
id: 62038833-2f95-41e5-bae0-a511af158fad
index_schema_version: 1
---

# Agents Index

Minden BDOS agent egyetlen áttekintő listán. **Forráshely** az `audit` mód Librarian futása (a jövőben automatikusan frissül).

> **2026-05-30 reconciliation (Claude audit):** Az index a tényleges canonical + registration + slash-command állapothoz lett igazítva. Két nyitott **verzió-szinkron sérülés** maradt, amit emberi döntés zár le (lásd a Presto és Broker bejegyzést):
> - **Presto**: canonical **v0.9.0 / 24 mód**, registration **v0.6.0 / 19 mód** — a kettő NINCS szinkronban. A 26 élő `pres-*` slash command a canonical (v0.9.0) valóságát igazolja, tehát a registration a stale. Javasolt fix: registration → v0.9.0-ra húzni.
> - **Broker**: canonical + registration szinkronban (**v0.3.3, 9 mód**), de már NEM placeholder — 12 élő `brk-*` parancs van. Az index frissítve.
> - Tényleges slash-command összesen: **83** (pres 26, alf 18, maestro 14, brk 12, dash 7, lib 6).

## Konvenciók

Minden agent két fájlban él:
- **Canonical**: `00_Prompts/BDOS/agents/<name>.md` — részletes, ember-olvasható spec, az "agent személyisége"
- **Registration**: `.claude/agents/<name>.md` — Claude Code runtime regisztráció (YAML config + thin pointer)

A két fájl `version:` mezőjének **szinkronban kell lennie**.

## Active agents

### Librarian — v0.8.3

- **Canonical:** `00_Prompts/BDOS/agents/librarian.md`
- **Registration:** `.claude/agents/librarian.md`
- **Status:** active
- **Created:** 2026-05-10 (v0.1)
- **Last updated:** 2026-05-24 (v0.8.3)
- **Model:** sonnet
- **Tools (registered):** Read, Write, Edit, Glob, Grep, Bash
- **Operation modes (6):** `index`, `retrieve`, `tidy`, `audit`, `integrate`, `deep-clean`
- **Slash commands:** `/lib-index`, `/lib-find`, `/lib-tidy`, `/lib-audit`, `/lib-integrate`, `/lib-deepclean`
- **Példa-hívások:**
  - `/lib-find hol vannak a Sonrisa pricing döntések` — kontextus-védett keresés, csak summary jön vissza
  - `/lib-index 02_Areas/Navigátor Podcast` — 5 index fájl generálása egy scope-ra
  - `/lib-audit` — vault egészségi riport (stale fájlok, hiányzó frontmatter, struktúra)
  - `/lib-tidy` — rendrakás (dry-run default, logol mindent)
- **Capabilities (v0.5):** PDF olvasás `pdftotext`-tel (poppler), SRT szöveg-extrakció, two-tier retrieve (tier-1 vault root + tier-2 unit-szintű scoped indexek), kontextus-védelem (a hívó kontextusa érintetlen marad retrieve módban).
- **Felelősség:** Knowledge Management — olvas, keres, rendez, takarít, integrál külső tartalmat, nagytakarít.
- **Maintenance log:**
  - `2026-05-24: Phase 2.B rollout — Logging requirement + logs/ skeleton (v0.6)`
  - `2026-05-24: Phase 3 — cache-first retrieve protocol (v0.7)`
  - `2026-05-24: Phase 4.A — Memory OS evolution (v0.8). Constitution_PHASE_4 + FRONTMATTER_SCHEMA + vault-indexing v2 schema + migrate_uuid.py (dry-run default).`
  - `2026-05-24: Phase 3.1 description mandate + version bump (v0.7)`
  - `2026-05-24: Phase 5 — Observability v2. ## Observability v2 section added. Operational markdown DEPRECATED for new events. (v0.8.1)`
  - `2026-05-24: Schema realigned to brief — agent_events → agent_logs. 28 columns, 15 event types, 6 log levels. query_duration_ms added. (v0.8.2)`
  - `2026-05-24: Phase 6 — ## Scheduling v1 added. Schedulable modes: index/audit auto; tidy/deep-clean manual+approval. (v0.8.3)`
- **Verzió-szinkron:** canonical v0.8.3 = registration v0.8.3 ✅

### Tier-2 scoped indexes (Librarian által karbantartva)

| Scope | Files | Index version | Last run |
|---|---:|---|---|
| `02_Areas/Deák Húsüzlet/` | 180 | v0.3 | 2026-05-11 |
| `02_Areas/Navigátor Podcast/` | 214 | v0.3 | 2026-05-11 |
| `02_Areas/Sonrisa/` | 167 | v0.3 | 2026-05-11 |
| `02_Areas/Szervezet fejlesztés/` | 62 | v0.3 | 2026-05-11 |
| `02_Areas/Ignis/` | 144 | v0.3 | 2026-05-11 |
| `02_Areas/ExarLabs/` | 48 | v0.3 | 2026-05-11 |
| `02_Areas/Personal Growth/` | 31 | v0.3 | 2026-05-11 |
| `02_Areas/Ignis Academy/` | 33 | v0.5 | 2026-05-11 |
| `03_Resources/` | 73 | v0.3 | 2026-05-11 |
| `04_Archive/` | 32 | v0.3 | 2026-05-11 |
| `00_Prompts/` | 86 | v0.5 | 2026-05-11 |

**Összesen: 11 tier-2 unit indexelve.** (Ignis 144 fájl — a v0.1 globális futás 58 csak top-level számolt; full depth: 144.)

**Tier-2 jelöltek a következő körben:** Ignis Academy (22), Média Műhely (21) — még a 30-fájl küszöb alatt, de növekvő tendencia.

### Maestro — v0.5.5

- **Canonical:** `00_Prompts/BDOS/agents/maestro.md`
- **Registration:** `.claude/agents/maestro.md`
- **Status:** active
- **Created:** 2026-05-14 (v0.1)
- **Last updated:** 2026-05-30 (v0.5.5)
- **Model:** sonnet
- **Tools (registered):** Read, Write, Edit, Glob, Grep, Bash
- **Operation modes (12):** **Brand-to-Site domain (5):** `status`, `next`, `continue`, `start`, `audit`. **Agent Family domain (4):** `team-status`, `team-audit`, `team-promote`, `team-introduce`. **Observability domain (3, Phase 2 új v0.3):** `observe`, `reflect`, `optimize`.
- **Pozíció:** **Conductor + Reflective Nervous System** — három karmestere a műnek: a projektek (Brand-to-Site), a csapat (Agent Family), és a szervezeti reflektivitás (Observability). Curator analógja, csak agentekre: a `team-promote` mód úgy húz rá közös meta-szabályt az agent-családra, ahogy a Curator `promote` a dashboard-családra. **v0.3 új:** Maestro innentől a BDOS reflektív idegrendszere — érzékel (logok), szintetizál (mintafelismerés, token-analitika), javasol (workflow/architektúra optimalizálás), de NEM mutál a hátad mögött.
- **Capabilities (v0.3):**
  - **Brand-to-Site (v0.1 óta):** Brand Spine 7+1 réteg / 3-tier pipeline navigáció. Per-projekt state-fájllal: `<project-area>/brand-spine-state.md`.
  - **Agent Family (v0.2 óta):** Meta-management — verzió-sync, közös meta-szabály propagálás (`team-promote`), új agent scaffold (`team-introduce`).
  - **Observability (v0.3 új):** Phase 2 alkotmány (`CONSTITUTION_PHASE_2.md`) végrehajtása. 3 mód: `observe` (aggregálja a 3 family log-streamet — Operational/Learning/Version — minden agent-ből; read-only riport), `reflect` (mélyebb minta-analízis: duplicated reasoning, token graveyards, prompt drift, collaboration failures stb. — javaslat-generálás), `optimize` (egy konkrét reflect-javaslat végrehajtása dry-run default + confirmation + Version Log audit-trail).
- **Felelősség:** Karmester három domain-ben. NEM stratéga, NEM ízlés-bíró, NEM markdown-rendrakó (Librarian), NEM dashboard-építő (Curator), NEM marketing-futtató (Presto), NEM sales-futtató (Broker). **Önreflexív:** saját canonicalja IS része minden team-promote futásnak, és saját logjait is olvasja az observability módokban.
- **Autonómia:** **Confirmation gate kötelező** minden végrehajtó akció előtt (`continue`, `start`, `team-promote`, `team-introduce`, `optimize`). Info-módok (`status`, `audit`, `team-status`, `team-audit`, `observe`, `reflect`) megerősítés nélkül futnak. Az `optimize` és `team-promote` **dry-run default**.
- **Slash commands (14):** **Brand-to-Site (6):** `/maestro` (legacy), `/maestro-status`, `/maestro-next`, `/maestro-continue`, `/maestro-start`, `/maestro-audit`. **Agent Family (4):** `/maestro-team-status`, `/maestro-team-audit`, `/maestro-team-promote`, `/maestro-team-introduce`. **Observability (3):** `/maestro-observe`, `/maestro-reflect`, `/maestro-optimize`. **Egyéb (1):** `/maestro-portrait` (Pixar-stílusú agent-portré generálás).
- **Példa-hívások:**
  - `/maestro-observe --since=2026-05-17` — utolsó hét aktivitás aggregálva
  - `/maestro-reflect --focus=workflow-bottlenecks` — bottleneck-elemzés + javaslat
  - `/maestro-optimize --recommendation_id=<slug>` — dry-run preview
  - `/maestro-optimize --recommendation_id=<slug> --apply` — végrehajt confirmation után
- **Verzió-szinkron:** canonical v0.5.5 = registration v0.5.5 ✅
- **Phase 2 állapot:** Phase 2.A kész (Maestro v0.3 + log schemas + observability módok). Phase 2.B (family-rollout) **KÉSZ** — minden agent Logging szekciót + logs/ skeletet kapott. Phase 2.C (token-mérés beüzemelése) **SUPERSEDED by Phase 5** — tokens now logged via agent_observability.db.
- **Source-of-truth dokumentumok:**
  - `00_Prompts/BDOS/CONSTITUTION_PHASE_2.md` — Phase 2 alkotmány
  - `00_Prompts/BDOS/LOG_SCHEMAS.md` — 3 log-stream schema
  - `00_Prompts/BDOS/capabilities/brand-to-site/` (Brand Spine v0.2)
  - Agent Family meta-management: `00_AGENTS_INDEX.md`
- **Maintenance log:**
  - `2026-05-23: v0.1 → v0.2 (Agent Family Conductor domain hozzáadva)`
  - `2026-05-24: v0.2 → v0.3 (Observability domain hozzáadva — Phase 2 Constitution végrehajtás)`
  - `2026-05-24: Phase 2.B rollout — Logging requirement + logs/ skeleton (v0.4)`
  - `2026-05-24: Phase 3.1 description mandate + version bump (v0.5)`
  - `2026-05-24: Phase 5 — Observability v2. ## Observability v2 section added. Global reader role documented. (v0.5.1)`
  - `2026-05-24: Schema realigned to brief — agent_events → agent_logs. Global reader now queries agent_logs table. (v0.5.2)`
  - `2026-05-24: Phase 6 — ## Scheduling v1 added. observe (daily auto), reflect (weekly auto), optimize/team-promote/team-introduce manual+approval. (v0.5.3)`
  - `2026-05-30: index reconciled to canonical/registration v0.5.5 (drift fix); /maestro-portrait added to command list (14 total).`
- **Verzió-szinkron:** canonical v0.5.5 = registration v0.5.5 ✅

### Curator — v0.5.4

- **Canonical:** `00_Prompts/BDOS/agents/curator.md`
- **Registration:** `.claude/agents/curator.md`
- **Status:** active
- **Created:** 2026-05-22 (v0.1)
- **Last updated:** 2026-05-25 (v0.5.4 — DS §4a card-copy-ref MANDATORY at build time)
- **Model:** sonnet
- **Tools (registered):** Read, Write, Edit, Glob, Grep, Bash
- **Operation modes (7):** `survey`, `build`, `tend`, `retire`, `audit`, `serve`, `promote`
- **Pozíció:** Representation layer kurátor — a Librarian testvére. A Librarian a persistence layer (vault markdown) kartográfusa; a Curator a representation layer (`_dashboards/` HTML dashboard-család) kurátora.
- **Capabilities (v0.2):** `survey` (élő index (re)generálás → `_dashboards/00_DASHBOARD_INDEX.md`, kontextus-védett), `build` (új dashboard a capability recept + DESIGN_SYSTEM szerint + launcher-regisztráció + index), `tend` (meglévő gondozása, verzió-bump + audit-trail + index), `retire` (archiválás/törlés + launcher-deregisztráció + index, confirmation + dry-run), `audit` (hét törvény + design-system drift mátrix → `_dashboards/00_CURATOR_AUDIT.md`), `serve` (dash-server start/open/status/stop, port 4321), `promote` (kitapasztalt minta → `DESIGN_SYSTEM.md` + ráhúzás az egész családra, confirmation + dry-run). A build-recept nincs duplikálva — a `capabilities/vault-dashboards/CLAUDE.md` a single source of truth.
- **Élő artifactok (a Curator tartja karban):** design system `_dashboards/_design/DESIGN_SYSTEM.md` (v0.1.0) + index `_dashboards/00_DASHBOARD_INDEX.md`. **Hibrid modell:** markdown a stílus-forrás most, `_engine/` extrakció lustán.
- **Felelősség:** Representation layer — dashboardok indexelése/keresése, építése, gondozása, leszerelése, standard- és design-system-auditja, tanult szabály propagálása, és a galéria (lokális szerver) vezérlése. NEM ír markdown tartalmat/adatot (az a Librarian/felhasználó terepe).
- **Autonómia:** `retire` és `promote` **confirmation-gate + dry-run default** (destruktív / család-szintű). Info-módok (`survey`, `audit`) megerősítés nélkül futnak.
- **Slash commands:** `/dash-survey`, `/dash-build`, `/dash-tend`, `/dash-retire`, `/dash-audit`, `/dash-serve`, `/dash-promote` (mind LIVE 2026-05-23 óta).
- **Példa-hívások:**
  - „Curator, survey" — élő dashboard-index regenerálása (`00_DASHBOARD_INDEX.md`)
  - „Curator, építs dashboardot a Navigátor analytics-hez" — új dashboard build a recept + design system szerint
  - „Curator, audit" — hét törvény + design-system drift mátrix
  - „Curator, serve" — lokális szerver indítása/megnyitása a 4321 porton
- **Verzió-szinkron:** canonical v0.5.4 = registration v0.5.4
- **Maintenance log:**
  - `2026-05-24: Phase 2.B rollout — Logging requirement + logs/ skeleton (v0.3)`
  - `2026-05-24: Phase 3.1 description mandate + version bump (v0.4)`
  - `2026-05-24: Phase 5 — Observability v2. ## Observability v2 section added. (v0.5.1)`
  - `2026-05-24: Schema realigned to brief — agent_events → agent_logs. dashboard_update event type for HTML bumps. (v0.5.2)`
  - `2026-05-24: Phase 6 — ## Scheduling v1 added. survey (weekly auto), audit (monthly auto), tend/build/promote/retire manual+approval. (v0.5.3)`
  - `2026-05-25: Promote — DS §4a card-copy-ref MANDATORY at build time. build mode step 4b added explicit. (v0.5.4)`
- **Verzió-szinkron:** canonical v0.5.4 = registration v0.5.4
- **Capability:** `00_Prompts/BDOS/capabilities/vault-dashboards/CLAUDE.md` (Vault Dashboards v0.2) + format contract `02_Areas/Sonrisa/CPS/Sales/DASHBOARD_CONTRACT.md` + design system `_dashboards/_design/DESIGN_SYSTEM.md`

### Presto — canonical v0.9.0 / registration v0.6.0 ⚠️ NINCS SZINKRONBAN

> **⚠️ VERZIÓ-SZINKRON SÉRÜLÉS (nyitott, emberi döntés kell):** A canonical (`agents/presto.md`) **v0.9.0 / 24 mód**, a registration (`.claude/agents/presto.md`) **v0.6.0 / 19 mód**. A 26 élő `pres-*` slash command (seed, draft, prepare, approve, exhaust, publish, channel, insight, template, todo mind létezik) a canonical v0.9.0 valóságát igazolja → a **registration a stale**. **Javasolt fix:** registration leírás + version → v0.9.0-ra húzni (a 24-mód Marketing OS állapotra). Amíg ez nem történik meg, Claude Code a v0.6.0/19-mód leírást tölti be.

- **Canonical:** `00_Prompts/BDOS/agents/presto.md` (v0.9.0)
- **Registration:** `.claude/agents/presto.md` (v0.6.0 — STALE, frissítendő)
- **Status:** active
- **Created:** 2026-05-23 (v0.1 as Herald)
- **Last updated:** 2026-05-30 (index reconcile); canonical utolsó bump v0.9.0
- **Model:** sonnet
- **Tools (registered):** Read, Write, Edit, Glob, Grep, Bash
- **Operation modes (24, canonical v0.9.0):** **Operational (12):** `status`, `today`, `plan`, `seed`, `draft`, `prepare`, `approve`, `exhaust`, `run` (deprecated), `resume`, `measure`, `index`. **Cognition (5):** `adapt`, `reflect`, `audience`, `discover`, `learn`. **Marketing OS (7):** `publish`, `comment-scan`, `comment-reply`, `insight`, `template`, `channel`, `todo`. Publication-as-atom modell, 6-stage kanban (Seed/Draft/Prepared/Approval/Scheduled/Published).
- **Pozíció:** Marketing Cognition Layer + Distribution Engine — a BDOS distribution cognition rétege. Maestro testvére (Maestro = build, Presto = run, Brand Spine Pulse). **v0.3 új:** több, mint executor — átalakítja Sage kogníciót audience-rezonanciává, közönséget tanul, és resonance-signal-eket küld vissza Sage-nek (permitted-flow modell).
- **Capabilities (v0.3):**
  - **Marketing Engine (v0.2 óta):** Markdown-natív kampánymenedzsment per Area, cross-project index, Cowork `marketing` plugin 8 skilljére routing.
  - **Sage integráció (v0.3 új):** Permitted-flow modell — olvassa Sage `thoughts/`, `atomic/`, `curate/` outputjait. NEM ír Sage-be. Resonance-signal-eket küld `Ideas/_inbox/sage-signals/`-be (schema: `presto.sage-signal.v1`) — Sage curate-kor felveheti.
  - **Audience-learnings (v0.3 új):** `agents/presto/audience-learnings/active|proposals|retired/` — Sage learnings mintára, cross-project meta-learning. 8 tanulság-típus: narrative-resonance, format-fit, tone-success, timing-pattern, platform-amplification, audience-rejection, cross-project-pattern, external-context. Cap: 15 active / 2000 token preamble.
  - **Thinking Engine Orchestrator integráció (v0.3 új):** Auto-hívható csak `discover` és `reflect` módokban (logoltan). Trend-validáció, stratégiai uncertainty-resolution. `think-agent-orchestrator-v09` skill.
  - **Distribution transformation (v0.3 új):** `adapt` mód egy atomic-ból N platform-variánst készít (LinkedIn + X + IG + YouTube + Newsletter), platform-natív stílusban. NEM copy-paste distribution.
  - **Visual asset workflow (v0.3 új):** `Campaigns/<slug>/assets/` mappa konvenció.
- **Felelősség:** Marketing distribution + audience cognition. **NEM** publikál (publish/send mindig emberi akció), NEM ír Sage outputjába, NEM ír brand-stratégiát (az Maestro), NEM épít site-ot (az Maestro), NEM sales (az Broker).
- **Autonómia:** `plan`, `run`, `resume`, `adapt`, `learn` (accept/reject/retire/edit) **confirmation-gate**. Info-módok (`status`, `today`, `measure`, `index`, `reflect`, `audience`, `discover`, `learnings` list) megerősítés nélkül. **Thinking Engine auto-hív** csak `discover`/`reflect` módokban.
- **Slash commands (26):** **Pipeline (8):** `/pres-seed`, `/pres-draft`, `/pres-prepare`, `/pres-approve`, `/pres-publish`, `/pres-exhaust`, `/pres-run` (deprecated), `/pres-resume`. **Operational (5):** `/pres-status`, `/pres-today`, `/pres-plan`, `/pres-measure`, `/pres-index`. **Cognition (4):** `/pres-adapt`, `/pres-reflect`, `/pres-audience`, `/pres-discover`. **Marketing OS (4):** `/pres-channel`, `/pres-insight`, `/pres-template`, `/pres-todo`. **Learning-lifecycle (5):** `/pres-learnings`, `/pres-learning-accept`, `/pres-learning-reject`, `/pres-learning-retire`, `/pres-learning-edit`.
- **Példa-hívások:**
  - `/pres-today` — mit kell ma mozdítani (operational)
  - `/pres-adapt --source=atomic/cognition-distribution-wall --platforms=LinkedIn,X,IG --area=ExarLabs` — Sage atomic → 3 platform draft
  - `/pres-reflect --period=weekly` — heti strategic reflection
  - `/pres-audience --area=ExarLabs --period=last90d --dimension=narrative` — pattern-analízis
  - `/pres-discover --area=Navigator --focus=niche-communities` — új platform signal (Thinking Engine auto-hív)
  - `/pres-learnings --proposed` — pending audience-learning review
- **Verzió-szinkron:** ⚠️ canonical v0.9.0 ≠ registration v0.6.0 — SÉRÜLT, reconcile szükséges (lásd a figyelmeztetést a szekció elején)
- **Maintenance log:**
  - `2026-05-24: rename Herald → Presto (rationale: family stylistic fit, Maestro/Presto duet, press + Pixar wordplay)`
  - `2026-05-24: v0.2 → v0.3 (Distribution Cognition Layer evolution — 5 új mód, Sage integráció, Thinking Engine integráció, audience-learnings rendszer, Phase 2 directive execution)`
  - `2026-05-24: Phase 2.B rollout — Logging requirement + logs/ skeleton (v0.4)`
  - `2026-05-24: Phase 3.1 description mandate + version bump (v0.5)`
  - `2026-05-24: Phase 5 — Observability v2. ## Observability v2 section added. (v0.5.1)`
  - `2026-05-24: Schema realigned to brief — agent_events → agent_logs. publish_prepared/publish_completed events added. (v0.5.2)`
  - `2026-05-24: Phase 6 — ## Scheduling v1 added. today/index/measure/reflect/audience auto; plan/run/resume/adapt/learn manual+approval. (v0.5.3)`
  - `2026-05-24 → 05-30: canonical evolved v0.6 → v0.9.0 (Marketing OS: publish/comment-scan/comment-reply/insight/template/channel/todo + pipeline seed/draft/prepare/approve/exhaust). Registration NEM követte (v0.6.0-on ragadt) — reconcile pending.`
  - `2026-05-30: index reconciled — 24 mód, 26 slash command rögzítve; canonical↔registration mismatch flag-elve.`
- **Capability:** `00_Prompts/BDOS/capabilities/marketing-engine/` (Marketing Engine v0.1) + Distribution Cognition Layer (v0.3-vel kerül be)
- **Pilot Area:** ExarLabs (Fázis 2 — folyamatban)
- **Folder skeleton:** `agents/presto/audience-learnings/{active,proposals,retired}/` + `agents/presto/discovery/` + `agents/presto/reflections/` (létrehozva 2026-05-24)
- **Permitted-flow signal-inbox:** `02_Areas/Personal Growth/Ideas/_inbox/sage-signals/` (Sage-nek, Presto írja)
### ~~Sage — v0.4.3~~ DEPRECATED (2026-05-28 — merged into Alfred v0.3)

- **Status:** DEPRECATED — capabilities absorbed into Alfred v0.3
- **Deprecated at:** 2026-05-28
- **Merged into:** Alfred v0.3 (`harvest`, `curate`, `chat`, `learn` módok)
- **What transferred:**
  - `harvest` mód (Referencia chat → Ideas/) → Alfred `harvest`
  - `curate` mód (heti reflexió) → Alfred `curate`
  - `chat` mód (knowledge-base párbeszéd) → Alfred `chat`
  - `learning-ops` mód → Alfred `learn`
  - `learnings/proposals/` (6 db) → `agents/alfred/learnings/proposals/`
  - `state/last_seen.md` → `agents/alfred/state/last_seen.md`
  - Scheduler jobs (sage-daily-harvest, sage-weekly-curate) → disabled; Alfred jobs seeded (alfred-daily-harvest, alfred-weekly-curate)
  - `sage-signals/` mappa ownership → Alfred írja (mappa neve megmarad backward-compat)
- **Files deleted:** `00_Prompts/BDOS/agents/sage.md`, `.claude/agents/sage.md`, `.claude/commands/sage-*.md` (14 db)
- **Files kept (archive):** `00_Prompts/BDOS/agents/sage/` mappa marad (SAGE_DESIGN_v0.1.md, learnings, state, cron) — de Alfred a source-of-truth
- **Maintenance log:**
  - `2026-05-24: Phase 6 — ## Scheduling v1 added. harvest (daily auto) + curate (weekly auto) seeded via seed_sage_jobs(). (v0.4.3)`
  - `2026-05-28: DEPRECATED — absorbed into Alfred v0.3 (Sage-Alfred merge)`

### Broker — v0.3.3

- **Canonical:** `00_Prompts/BDOS/agents/broker.md`
- **Registration:** `.claude/agents/broker.md`
- **Status:** active (v0.2 capability designed — már NEM placeholder)
- **Created:** 2026-05-24 (v0.1)
- **Last updated:** 2026-05-30 (index reconcile; canonical+registration v0.3.3 szinkronban)
- **Model:** sonnet
- **Tools (registered):** Read, Write, Edit, Glob, Grep, Bash
- **Pozíció:** Distribution layer sibling to Presto. Cognition (Sage/Alfred) → distribution (Presto for marketing one-to-many, Broker for sales one-to-one). Fal a cognition és distribution rétegek között érvényes.
- **Operation modes (9):** **Operational (7):** `status`, `today`, `plan`, `run`, `resume`, `measure`, `index`. **Cognition (2):** `learn` (sales-learning lifecycle-ops), `reflect` (heti/havi sales strategic reflection). Per-Area state: `Sales/Cohorts/<slug>/COHORT.md`. Sales-learnings 8 típus: objection-pattern, cycle-timing, cohort-signal, outreach-tone, qualification-criteria, competitor-context, loss-pattern, referral-mechanic.
- **Slash commands (12):** `/brk-status`, `/brk-today`, `/brk-plan`, `/brk-run`, `/brk-resume`, `/brk-measure`, `/brk-index`, `/brk-reflect`, `/brk-learnings`, `/brk-learning-accept`, `/brk-learning-reject`, `/brk-learning-retire`. (Mind LIVE.)
- **Felelősség:** One-to-one sales activities — lead tracking, pipeline management, outreach drafts, deal status, follow-ups, proposal prep. Bidirectional: outbound + incoming prospect responses, objections, signals.
- **Autonómia:** Confirmation-gate minden végrehajtó akció előtt. NEM küld ki üzenetet vagy zár le deal-t emberi jóváhagyás nélkül. NEM lép át marketing (Presto) vagy cognition (Sage) területre.
- **Verzió-szinkron:** canonical v0.3.3 = registration v0.3.3
- **Maintenance log:**
  - `2026-05-24: v0.1 placeholder scaffold via team-introduce. Modes TBD. Slash commands TBD (brk- prefix reserved).`
  - `2026-05-24: Phase 2.B rollout — Logging requirement + logs/ skeleton (v0.2)`
  - `2026-05-24: Phase 3.1 description mandate + version bump (v0.3)`
  - `2026-05-24: Phase 5 — Observability v2. ## Observability v2 section added. (v0.3.1)`
  - `2026-05-24: Schema realigned to brief — agent_events → agent_logs. approval_requested replaces decision for confirmation gates. (v0.3.2)`
  - `2026-05-24: Phase 6 — ## Scheduling v1 added. today/index/measure/reflect auto; plan/run/resume/learn manual+approval. Outreach-always-human documented. (v0.3.3)`
  - `2026-05-30: index reconcile — 9 mód + 12 élő brk-* parancs rögzítve (korábban tévesen "placeholder, 0 parancs"). canonical+registration v0.3.3 szinkronban.`
- **Verzió-szinkron:** canonical v0.3.3 = registration v0.3.3 ✅

### Forge — v0.1.1

- **Canonical:** `00_Prompts/BDOS/agents/forge.md`
- **Registration:** `.claude/agents/forge.md` (created 2026-05-30 via Maestro `team-introduce`, approved by user)
- **Status:** active (placeholder)
- **Created:** 2026-05-27 (v0.1.0)
- **Last updated:** 2026-06-05 (v0.1.1 — bound external repositories §11)
- **Model:** sonnet
- **Tools (registered):** Read, Write, Edit, Glob, Grep, Bash
- **Pozíció:** Capability layer — sibling to Broker. Broker = client-side movement (one-to-one), Forge = capability-side stewardship (cross-client practice area-k). Új réteg a BDOS-ban: a kognitív (Sage) + disztribúciós (Presto + Broker) mellé bekerül a kapacitás-réteg.
- **Operation modes:** TBD — modes to be designed in v0.2 (Broker-pattern). Várható irány: 7 operational (`status`, `today`, `capture`, `refine`, `index`, `measure`, `handoff`) + 2 cognition (`learn`, `reflect`).
- **Slash commands:** None yet. Prefix reserved: `forge-` (pl. `/forge-status`, `/forge-capture`, `/forge-refine`, `/forge-handoff` — de NEM véglegesek, v0.2-ben jönnek).
- **Felelősség:** Cross-cutting practice area-k és kapacitás-területek karbantartása. Két flow:
  - **Bottom-up** — kliens-engagementből származó megfigyelések, logok, tervezési minták filing-ja és refine-olása reusable pattern-né
  - **Top-down** — külső research (vendor-eval, papers, conferences) filing-ja és refine-olása
  - Cross-link engagementekkel `related-projects.md`-n keresztül (Broker territory átfedés)
  - Handoff Brokerhez (proposal-template kész) vagy Presto-hoz (marketing-ready capability)
- **Autonómia:** Confirmation-gate minden filing akció előtt (melyik area, melyik subfolder). NEM módosít kliens-state-fájlt (Broker territory), NEM generál outreach üzenetet (Broker/Presto territory), NEM hoz stratégiai döntést cégszinten (Maestro + user). PII-leak guard: kliens-specifikus részlet csak Broker-folderben, generikus pattern Forge-ben.
- **Storage convention:** `02_Areas/<unit>/Practices/<area>/` per-unit per-area folder struktúrával (NOTES, _inbox, research, patterns, decisions, experiments, proposals, learnings, related-projects, open-questions). Cross-cutting meta-learnings `00_Prompts/BDOS/agents/forge/practice-learnings/` mappában.
- **Két szintű learning architecture:**
  - Per-area learning: `Practices/<area>/learnings/active|proposals|retired/`
  - Cross-practice meta-learning: `agents/forge/practice-learnings/active|proposals|retired/`
  - Mindkettő ugyanaz a `proposed → active → retired` lifecycle, max 15 active / 2000 token preamble (Sage konvenció, Broker-pattern)
- **Verzió-szinkron:** canonical v0.1.1 = registration v0.1.1 ✅
- **Bound repositories (v0.1.1 új):** practice area-k külső git repóhoz köthetők (`bound_repository` frontmatter a practice NOTES-ban). Kötelező git-protokoll: **pull-first, push-last**, soha force-push. Első binding: `ExarLabs/Practices/Microsites` → `Downloads/Work/ExarLabs/microsite-factory` (remote `ExarLabs/microsite-factory`, master, factory v0.6.0, 14 site). A `/microsite-build` skill + `impeccable` + `ui-ux-pro-max` ennek a repónak a `.claude/skills/`-jében él.
- **Maintenance log:**
  - `2026-05-27: v0.1.0 placeholder scaffold via team-introduce-pattern. Identity + Mission + Constraints + Anti-patterns + Storage Convention + Logging + Scheduling + Broker-integráció rögzítve. Slash prefix forge- reserved. Két példa practice area: CPS/Inference-Farm + ExarLabs/Microsites.`
  - `2026-05-30: Runtime registration .claude/agents/forge.md created via Maestro team-introduce. User explicitly authorized. Canonical unchanged (v0.1.0). Registration id: 26d54e1a-2a57-4070-adb1-01aa67ead9ad.`
  - `2026-06-05: v0.1.0 → v0.1.1 — Bound external repositories (§11). Microsite Factory repo a ExarLabs/Microsites practice area-hoz kötve. Git-protokoll: pull-first, push-last. Maestro tanítás, user explicit felhatalmazás. Canonical + registration + practice NOTES + version-log frissítve.`
- **Practice area-k aktiválva (2):**
  - `02_Areas/Sonrisa/CPS/Practices/Inference-Farm/` — Merkantil Discovery-triggered, maturity: `research`
  - `02_Areas/ExarLabs/Practices/Microsites/` — **repo-bound** (microsite-factory v0.6.0), maturity: `patterns-emerging`

### Alfred — v0.4.0

- **Canonical:** `00_Prompts/BDOS/agents/alfred.md`
- **Registration:** `.claude/agents/alfred.md` (v0.4.0 — updated 2026-06-07 Triage Engine)
- **Status:** active
- **Created:** 2026-05-28 (v0.1.0)
- **Last updated:** 2026-06-07 (v0.4.0 — Cognitive Triage Engine: triage + next módok)
- **Model:** sonnet
- **Tools (registered):** Read, Write, Edit, Glob, Grep, Bash (+ Chrome MCP a harvest-csatornákhoz, + Gmail/Outlook/Yahoo MCP a triage-hez)
- **Pozíció:** **Executive Cognition Layer + Cognition Curator + Triage Orchestrator** — a BDOS human interface rétege + Sage-merged kognitív kurátor + v0.4 Cognitive Triage Engine. Maestro a rendszerre néz; Alfred a gazdára.
- **Operation modes (14):** `capture`, `sync`, `today`/`briefing`, `status`, `todo`, `remind`, `done`, `tasks` (v0.2 operative) + `harvest`, `curate`, `chat`, `learn` (v0.3 kognitív, Sage-merged) + **`triage`, `next`** (v0.4 Triage Engine).
- **Két harvest-csatorna + email-triage:** `harvest` = ChatGPT "Referencia chat" (ötletek); `sync` = ChatGPT "Alfred Inbox" (ops dump); `triage` = email (Gmail/Outlook/Yahoo MCP) → multi-agent prepared-task dossziék.
- **Triage Engine (v0.4):** óránként (scheduler) beolvassa az emaileket, kiszűri a választ igénylőket, és a Librariannel (mindig) + dinamikus domain-routinggal (Presto/Broker/Forge/Curator) prepared-task dossziékat készít (`tasks/`, `alfred.task.v1`): válasz-draft + actionable-ök. Multi-agent contribution-tracking közös `task_id`-vel (dosszié-timeline = SoT, agent_logs = queryable tükör). `next` = "van feladatom?" riport. SOHA nem küld, `--auto`-ban Gmail-be sem ír.
- **Felelősség:** Frictionless capture + idea-harvest + personal ops + email-triage. NEM publikál, NEM küld, NEM ír más agent state-jébe. Email = untrusted input (prompt-injection védelem).
- **Autonómia:** Confirmation-gate minden vault-mutáció elott. `capture`, info-módok (`tasks`/`today`/`status`/`next`), és `triage` (csak belső dosszié) megerosítés nélkül. `harvest`/`curate`/`triage` csend default.
- **Slash commands (20, mind LIVE):** **Operative (9):** `/alf-capture`, `/alf-sync`, `/alf-today`, `/alf-status`, `/alf-todo`, `/alf-remind`, `/alf-done`, `/alf-tasks`, `/alf-recap`. **Triage (2):** `/alf-triage`, `/alf-next`. **Kognitív/Sage-merged (4):** `/alf-harvest`, `/alf-curate`, `/alf-chat`, `/alf-learn`. **Learning-lifecycle (5):** `/alf-learnings`, `/alf-learning-accept`, `/alf-learning-edit`, `/alf-learning-reject`, `/alf-learning-retire`.
- **Verzió-szinkron:** canonical v0.4.0 = registration v0.4.0
- **Maintenance log:**
  - `2026-06-07: v0.4.0 — Cognitive Triage Engine. triage + next módok. Prepared-task dossier-réteg (tasks/, alfred.task.v1, §5b). Multi-agent contribution-tracking közös task_id-vel (§8). Scheduler: alfred-hourly-triage (interval 3600, enabled=0 smoke-tesztig) + cron/run_hourly_triage.sh. Heartbeat: state/triage_queue.md. Dashboard → napi cockpit v0.5.0 (Curator). §8 Phase 2→5/6 ref-fix. Slash: /alf-triage, /alf-next.`
  - `2026-05-28: v0.3.0 — Sage-Alfred merge. harvest/curate/chat/learn absorbed. Két csatorna szeparálva. scheduler jobs: alfred-daily-harvest + alfred-weekly-curate. 6 Sage learning-proposal migrálva. sage-signals/ ownership transferred.`
  - `2026-05-28: v0.2.0 — TODO-rendszer + intent-felismerés. 4 mag-mód. Registration létrehozva.`
  - `2026-05-28: v0.1.0 scaffold.`
  - `2026-05-28: 17 alf-* slash commands scaffolded (operative 8 + cognitive 4 + learning-lifecycle 5). All LIVE.`
- **Storage home:** `02_Areas/Personal Growth/Alfred/` (+ `tasks/` dossziék, `state/triage_queue.md`) + `02_Areas/Personal Growth/Ideas/` (idea-output) + `agents/alfred/` (state, learnings, cron)
- **Scheduling:** `alfred-daily-harvest` (daily 04:00 UTC) + `alfred-weekly-curate` (weekly Mon 04:05 UTC) + `alfred-hourly-triage` (interval 3600s, enabled=0). Seeded via `seed_alfred_cognition_jobs()` + `seed_alfred_triage_job()`.

## Planned agents

(Üres egyelőre — v0.x-ban jönnek a következők, ha szükségesek: Product Strategist, Operations Steward, Exploration Agent, Validator stb.)

## Deprecated agents

### Sage — DEPRECATED 2026-05-28

Absorbed into Alfred v0.3. See the `~~Sage — v0.4.3~~` entry in Active agents above for the full transfer manifest.

---

## Hogyan adunk hozzá új agentet (checklist)

1. **Canonical fájl** létrehozása: `00_Prompts/BDOS/agents/<name>.md` — frontmatter (`name`, `version: 0.1`, `date`, `status: active`, `description`), majd a részletes spec
2. **Registration fájl** létrehozása: `.claude/agents/<name>.md` — frontmatter (`name`, `version`, `description`, `tools`, `model`), majd thin system prompt ami a canonical-ra mutat
3. **Bejegyzés ide** az "Active agents" szekcióba (vagy az audit mód majd frissíti)
4. **Verzió-szinkron check** — mindkét fájl ugyanaz a `version:`
5. Új session indításakor a Claude Code felveszi az új `subagent_type`-ot
