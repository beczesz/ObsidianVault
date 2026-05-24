---
title: 00_AGENTS_INDEX
description: Meta-index minden BDOS agentről — canonical fájl + Claude Code registration + verzió + státusz egy helyen.
generated_by: human-manual (v0.2 audit-tól: librarian audit mode)
last_updated: 2026-05-24
phase5_observability: 2026-05-24
id: 62038833-2f95-41e5-bae0-a511af158fad
index_schema_version: 1
---

# Agents Index

Minden BDOS agent egyetlen áttekintő listán. **Forráshely** az `audit` mód Librarian futása (a jövőben automatikusan frissül).

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
- **Verzió-szinkron:** canonical v0.8.3 = registration v0.8.3 (updated above)
- **Maintenance log:**
  - `2026-05-24: Phase 2.B rollout — Logging requirement + logs/ skeleton (v0.6)`
  - `2026-05-24: Phase 3 — cache-first retrieve protocol (v0.7)`
  - `2026-05-24: Phase 4.A — Memory OS evolution (v0.8). Constitution_PHASE_4 + FRONTMATTER_SCHEMA + vault-indexing v2 schema + migrate_uuid.py (dry-run default).`
  - `2026-05-24: Phase 3.1 description mandate + version bump (v0.7)`
  - `2026-05-24: Phase 5 — Observability v2. ## Observability v2 section added. Operational markdown DEPRECATED for new events. (v0.8.1)`
  - `2026-05-24: Schema realigned to brief — agent_events → agent_logs. 28 columns, 15 event types, 6 log levels. query_duration_ms added. (v0.8.2)`
  - `2026-05-24: Phase 6 — ## Scheduling v1 added. Schedulable modes: index/audit auto; tidy/deep-clean manual+approval. (v0.8.3)`
- **Verzió-szinkron:** canonical v0.8.3 = registration v0.8.3

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

### Maestro — v0.5.3

- **Canonical:** `00_Prompts/BDOS/agents/maestro.md`
- **Registration:** `.claude/agents/maestro.md`
- **Status:** active
- **Created:** 2026-05-14 (v0.1)
- **Last updated:** 2026-05-24 (v0.5.3 — Phase 6 Scheduling v1)
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
- **Slash commands:** **Brand-to-Site (6):** `/maestro` (legacy), `/maestro-status`, `/maestro-next`, `/maestro-continue`, `/maestro-start`, `/maestro-audit`. **Agent Family (4):** `/maestro-team-status`, `/maestro-team-audit`, `/maestro-team-promote`, `/maestro-team-introduce`. **Observability (3):** `/maestro-observe`, `/maestro-reflect`, `/maestro-optimize`.
- **Példa-hívások:**
  - `/maestro-observe --since=2026-05-17` — utolsó hét aktivitás aggregálva
  - `/maestro-reflect --focus=workflow-bottlenecks` — bottleneck-elemzés + javaslat
  - `/maestro-optimize --recommendation_id=<slug>` — dry-run preview
  - `/maestro-optimize --recommendation_id=<slug> --apply` — végrehajt confirmation után
- **Verzió-szinkron:** canonical v0.5.3 = registration v0.5.3
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
- **Verzió-szinkron:** canonical v0.5.3 = registration v0.5.3

### Curator — v0.5.3

- **Canonical:** `00_Prompts/BDOS/agents/curator.md`
- **Registration:** `.claude/agents/curator.md`
- **Status:** active
- **Created:** 2026-05-22 (v0.1)
- **Last updated:** 2026-05-24 (v0.5.3 — Phase 6 Scheduling v1)
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
- **Verzió-szinkron:** canonical v0.5.3 = registration v0.5.3
- **Maintenance log:**
  - `2026-05-24: Phase 2.B rollout — Logging requirement + logs/ skeleton (v0.3)`
  - `2026-05-24: Phase 3.1 description mandate + version bump (v0.4)`
  - `2026-05-24: Phase 5 — Observability v2. ## Observability v2 section added. (v0.5.1)`
  - `2026-05-24: Schema realigned to brief — agent_events → agent_logs. dashboard_update event type for HTML bumps. (v0.5.2)`
  - `2026-05-24: Phase 6 — ## Scheduling v1 added. survey (weekly auto), audit (monthly auto), tend/build/promote/retire manual+approval. (v0.5.3)`
- **Verzió-szinkron:** canonical v0.5.3 = registration v0.5.3
- **Capability:** `00_Prompts/BDOS/capabilities/vault-dashboards/CLAUDE.md` (Vault Dashboards v0.2) + format contract `02_Areas/Sonrisa/CPS/Sales/DASHBOARD_CONTRACT.md` + design system `_dashboards/_design/DESIGN_SYSTEM.md`

### Presto — v0.5.3

- **Canonical:** `00_Prompts/BDOS/agents/presto.md`
- **Registration:** `.claude/agents/presto.md`
- **Status:** active
- **Created:** 2026-05-23 (v0.1 as Herald)
- **Last updated:** 2026-05-24 (v0.5.3 — Phase 6 Scheduling v1)
- **Model:** sonnet
- **Tools (registered):** Read, Write, Edit, Glob, Grep, Bash
- **Operation modes (12):** **Operational (7):** `status`, `today`, `plan`, `run`, `resume`, `measure`, `index`. **Cognition (5, v0.3 új):** `adapt` (Sage atomic → N platform variant), `reflect` (heti/havi strategic reflection — NEM optimization theater), `audience` (pattern-analízis Sage atomic-cross-link), `discover` (új platform signal-detector, 4-feltétel-szűrő), `learn` (audience-learning lifecycle).
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
- **Slash commands (16):** **Operational (7):** `/pres-status`, `/pres-today`, `/pres-plan`, `/pres-run`, `/pres-resume`, `/pres-measure`, `/pres-index`. **Cognition (9, v0.3 új):** `/pres-adapt`, `/pres-reflect`, `/pres-audience`, `/pres-discover`, `/pres-learnings`, `/pres-learning-accept`, `/pres-learning-reject`, `/pres-learning-retire`, `/pres-learning-edit`.
- **Példa-hívások:**
  - `/pres-today` — mit kell ma mozdítani (operational)
  - `/pres-adapt --source=atomic/cognition-distribution-wall --platforms=LinkedIn,X,IG --area=ExarLabs` — Sage atomic → 3 platform draft
  - `/pres-reflect --period=weekly` — heti strategic reflection
  - `/pres-audience --area=ExarLabs --period=last90d --dimension=narrative` — pattern-analízis
  - `/pres-discover --area=Navigator --focus=niche-communities` — új platform signal (Thinking Engine auto-hív)
  - `/pres-learnings --proposed` — pending audience-learning review
- **Verzió-szinkron:** canonical v0.5.3 = registration v0.5.3
- **Maintenance log:**
  - `2026-05-24: rename Herald → Presto (rationale: family stylistic fit, Maestro/Presto duet, press + Pixar wordplay)`
  - `2026-05-24: v0.2 → v0.3 (Distribution Cognition Layer evolution — 5 új mód, Sage integráció, Thinking Engine integráció, audience-learnings rendszer, Phase 2 directive execution)`
  - `2026-05-24: Phase 2.B rollout — Logging requirement + logs/ skeleton (v0.4)`
  - `2026-05-24: Phase 3.1 description mandate + version bump (v0.5)`
  - `2026-05-24: Phase 5 — Observability v2. ## Observability v2 section added. (v0.5.1)`
  - `2026-05-24: Schema realigned to brief — agent_events → agent_logs. publish_prepared/publish_completed events added. (v0.5.2)`
  - `2026-05-24: Phase 6 — ## Scheduling v1 added. today/index/measure/reflect/audience auto; plan/run/resume/adapt/learn manual+approval. (v0.5.3)`
- **Verzió-szinkron:** canonical v0.5.3 = registration v0.5.3
- **Capability:** `00_Prompts/BDOS/capabilities/marketing-engine/` (Marketing Engine v0.1) + Distribution Cognition Layer (v0.3-vel kerül be)
- **Pilot Area:** ExarLabs (Fázis 2 — folyamatban)
- **Folder skeleton:** `agents/presto/audience-learnings/{active,proposals,retired}/` + `agents/presto/discovery/` + `agents/presto/reflections/` (létrehozva 2026-05-24)
- **Permitted-flow signal-inbox:** `02_Areas/Personal Growth/Ideas/_inbox/sage-signals/` (Sage-nek, Presto írja)
### Sage — v0.4.3

- **Canonical:** `00_Prompts/BDOS/agents/sage.md`
- **Registration:** `.claude/agents/sage.md`
- **Design:** `00_Prompts/BDOS/agents/sage/SAGE_DESIGN_v0.1.md` (v0.2 állapotban)
- **Status:** active (scheduler jobs seeded — harvest daily + curate weekly)
- **Created:** 2026-05-24 (v0.2 — design + meta-learning loop együtt érkezett)
- **Last updated:** 2026-05-24 (v0.4.3 — Phase 6 Scheduling v1)
- **Model:** sonnet
- **Tools (registered):** Read, Write, Edit, Glob, Grep, Bash
- **Operation modes (5):** `harvest`, `curate`, `chat`, `learning-ops`, `index`/`status`/`summary`/`find`/`edit`/`promote`
- **Pozíció:** Cognition Curator — a BDOS cognition layer-jének operátora. **NEM** publikál, **NEM** kommunikál külvilággal. Olvas, struktúrál, kapcsol, javasol. Csend default — inkább egy fontos signal, mint folyamatos zaj.
- **Capabilities (v0.2):** Daily harvest a ChatGPT "Referencia chat"-ből (Chrome MCP) → strukturált gondolat-note-ok a `02_Areas/Personal Growth/Ideas/`-be. Atomic note ápolás (history-szekcióval). Heti curate (hétfő 06:05) — trend-analízis, kategória-revízió, kapcsolat-keresés, Librarian-kérések main Claude orchestrátoron át. **Meta-learning loop:** Sage saját munkájáról explicit, user-reviewable tanulságokat ír (`learnings/proposals|active|retired`), cap 15 / 2000 token preamble. Markdown-natív state, dashboard-ready (`state/last_run.md` single source of truth).
- **Felelősség:** Cognition layer karbantartása. Distribution layer-rel fal van köztük (lásd cognition stack brainstorm).
- **Autonómia:** `harvest` és `curate` **csend default** + notify csak ha minta van. `chat`/`edit`/`promote`/`curate` confirmation-gate. Info-módok (`status`, `summary`, `find`, `learnings`) megerősítés nélkül.
- **Slash commands (14):** `/sage-status`, `/sage-harvest`, `/sage-curate`, `/sage-summary`, `/sage-find`, `/sage-chat`, `/sage-edit`, `/sage-promote`, `/sage-index`, `/sage-learnings`, `/sage-learning-accept`, `/sage-learning-reject`, `/sage-learning-retire`, `/sage-learning-edit` (mind LIVE 2026-05-24 óta).
- **Példa-hívások:**
  - `/sage-status` — utolsó futás riport, never_run figyelmeztetés (jelen állapot)
  - `/sage-harvest` — kézi napi harvest a Referencia chatből
  - `/sage-curate` — heti reflexió (drága, ~15-20 perc, confirmation kötelező)
  - `/sage-chat` — beszélgetés a tudásbázisról
  - `/sage-learnings --proposed` — pending learning-javaslatok review-ja
- **Verzió-szinkron:** canonical v0.4.3 = registration v0.4.3; design fájl v0.2 — design doc külön verziózott
- **Maintenance log:**
  - `2026-05-24: Phase 2.B rollout — Logging requirement + logs/ skeleton (v0.3)`
  - `2026-05-24: Phase 3.1 description mandate + version bump (v0.4)`
  - `2026-05-24: Phase 5 — Observability v2. ## Observability v2 section added. _journal/ alias note preserved. (v0.4.1)`
  - `2026-05-24: Schema realigned to brief — agent_events → agent_logs. learning + reflection event types explicitly used. (v0.4.2)`
  - `2026-05-24: Phase 6 — ## Scheduling v1 added. harvest (daily auto) + curate (weekly auto) seeded via seed_sage_jobs(). launchd deprecated. (v0.4.3)`
- **Verzió-szinkron:** canonical v0.4.3 = registration v0.4.3
- **Scheduling (Phase 6):** harvest (daily 04:00 UTC / 06:00 Budapest summer, `requires_approval=0`), curate (weekly Monday 04:05 UTC, `requires_approval=0`). Seeded via `scheduler.py seed_sage_jobs()`. Dashboard-resident — runs while server is active.
- **Vault output home:** `02_Areas/Personal Growth/Ideas/` (`thoughts/`, `atomic/`, `_inbox/`, `_journal/`, `curate/`, `00_INDEX.md`, `00_CATEGORIES.md`)
- **Dashboard-readiness:** lásd `SAGE_DESIGN_v0.1.md §7` — Curator későbbi input

### Broker — v0.3.3

- **Canonical:** `00_Prompts/BDOS/agents/broker.md`
- **Registration:** `.claude/agents/broker.md`
- **Status:** active (placeholder)
- **Created:** 2026-05-24 (v0.1)
- **Last updated:** 2026-05-24 (v0.3.3 — Phase 6 Scheduling v1)
- **Model:** sonnet
- **Tools (registered):** Read, Write, Edit, Glob, Grep, Bash
- **Pozíció:** Distribution layer sibling to Presto. Cognition (Sage) → distribution (Presto for marketing one-to-many, Broker for sales one-to-one). Fal a cognition és distribution rétegek között érvényes.
- **Operation modes:** TBD — modes to be designed in v0.2. Várható irány: 7 mód, Presto mintájára, de sales one-to-one természetéhez igazítva.
- **Slash commands:** None yet. Prefix reserved: `brk-` (pl. `/brk-status`, `/brk-today`, `/brk-run` — de NEM véglegesek, v0.2-ben jönnek).
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
- **Verzió-szinkron:** canonical v0.3.3 = registration v0.3.3

## Planned agents

(Üres egyelőre — v0.x-ban jönnek a következők, ha szükségesek: Product Strategist, Operations Steward, Exploration Agent, Validator stb.)

## Deprecated agents

(Üres.)

---

## Hogyan adunk hozzá új agentet (checklist)

1. **Canonical fájl** létrehozása: `00_Prompts/BDOS/agents/<name>.md` — frontmatter (`name`, `version: 0.1`, `date`, `status: active`, `description`), majd a részletes spec
2. **Registration fájl** létrehozása: `.claude/agents/<name>.md` — frontmatter (`name`, `version`, `description`, `tools`, `model`), majd thin system prompt ami a canonical-ra mutat
3. **Bejegyzés ide** az "Active agents" szekcióba (vagy az audit mód majd frissíti)
4. **Verzió-szinkron check** — mindkét fájl ugyanaz a `version:`
5. Új session indításakor a Claude Code felveszi az új `subagent_type`-ot
