---
title: BDOS Primer — Session Bootstrap Document
date: 2026-05-24
author: Becze Szabolcs
status: active
version: 1.0
description: Önálló, másolható primer egy új Claude Code session indításához. Minden BDOS-fejlesztés első olvasandó dokumentuma. Tartalmazza az alapfilozófiát (cognition stack, fal), a 6 aktív agentet részletesen, az architekturális invariánsokat, a naming convention-t, a state/audit trail mechanizmusokat, a meta-learning loop-ot, a dashboard architektúrát, a pending munka listáját, és a kritikus fájlok read-list-jét.
tags: [BDOS, primer, documentation, bootstrap, agents, cognition]
id: a826b2e8-b512-4892-aa84-e942a73630e0
index_schema_version: 1
---

# BDOS — Business Development Operation System
## Primer egy új session-höz

> **Másold be ezt a teljes dokumentumot egy új Claude Code chat elejére. Minden további fejlesztés (új agent, új dashboard, új capability) ennek a kontextusnak az ismeretében történjen.**
>
> **Vault gyökér:** `/Users/becze-mac/My Drive (beczesz.szabolcs@gmail.com)/0. Ideas Vault/`
> **Olvasd be a 13. szekcióban listázott fájlokat mielőtt bármit csinálsz.**

---

## 1. Mi a BDOS?

A BDOS egy **AI-native cognition operating system**. NEM playbook, NEM framework, NEM productivity-tool. Egy olyan rendszer, amiben **stabil gondolkodási szerepek** (agentek) **stabil markdown-állapotokra** (vault) működnek, **Claude Code orchestrátoron** át.

A BDOS belépője: `00_Prompts/BDOS/CLAUDE.md`

### Az alapfelismerés (cognition stack brainstorm, 2026-05-23)

Egy AI-native rendszer rétegekben él:

```
capture → processing → cognition → distribution → feedback → learning
```

**Kritikus invariáns:** a **cognition** és a **distribution** réteg között **fal** van. A marketing/sales soha nem dönti el, hogy mit kell gondolni — csak fordít kifelé. Ha ez a fal leomlik, a rendszer engagement-optimalizálttá válik és deformálja magát a gondolkodást.

Ez a fal a BDOS legfontosabb tervezési elve. Minden agentdöntésnél figyelni kell rá.

**Filozófia:** a vault egy **augmented cognition loop**, NEM autonóm intelligencia. Az AI olvas, struktúrál, javasol. **Az ember dönt** — minden publikálás, sales-aktus, fontos prioritás emberi jóváhagyáshoz kötött.

---

## 2. A vault szervezeti elv (PARA-modified)

| Mappa | Szerep |
|---|---|
| `01_Projects/` | Rövid távú, deadline-os, cross-cutting feladatok. Általában majdnem üres. |
| `02_Areas/` | **A vault zöme** — tartós felelősségi körök (Sonrisa, Navigátor Podcast, Deák Húsüzlet, ExarLabs, Personal Growth, stb.) |
| `03_Resources/` | Külső input: könyvek, podcastok, transcriptek. |
| `04_Archive/` | Inaktív. Nem indexeljük. |
| `05_DailyNotes/` | Napi jegyzetek. |
| `00_Prompts/` | Agent-definíciók, plugin-ok, capabilityk, BDOS belépő. |
| `Templates/` | Új fájl sablonok. |
| `_dashboards/` | HTML dashboard-család (live-fetch read-only nézetek a vault-ról). |

**Indoklás:** a user manager/operátor — a "projektek" nála **éveken át tartó kapcsolatok**, nem 3-hónapos sprintek. Ezért az Area-szintű csoportosítás logikusabb mint orthodox PARA.

---

## 3. A két nézőpont — Areas + Agents

A vault **egyetlen organikus rendszer**, de **két nézőpontból olvasható**:

| Nézet | Mit ad | Ki gondozza |
|---|---|---|
| **Areas** (statikus) | Projekt-struktúra: miről szól a munka | Curator (a dashboard-családon át) |
| **Agents** (dinamikus) | Agent-csapat: ki dolgozik a munkán | Maestro (team-* módokon át) |

A főnaptár-dashboard (`_dashboards/index.html`, v0.7.0) ennek a kettősségnek a belépője — tab-szwitcherrel váltható.

---

## 4. Az aktív agentek (6 db)

Minden agent **két fájlban** él:
- **Canonical:** `00_Prompts/BDOS/agents/<name>.md` — részletes spec, ember-olvasható
- **Registration:** `.claude/agents/<name>.md` — Claude Code runtime regisztráció (YAML + thin pointer)

A két fájl `version:` mezőjének **szinkronban kell lennie**. Forrás-az-igazságra: `00_Prompts/BDOS/00_AGENTS_INDEX.md`.

### 4.1 Librarian — v0.5 LIVE
**Funkció:** Knowledge Manager. A vault retrieval/tidy/audit operátora.
**Módok (6):** `index`, `retrieve`, `tidy`, `audit`, `integrate`, `deep-clean`
**Slash:** `/lib-find`, `/lib-index`, `/lib-tidy`, `/lib-audit`, `/lib-integrate`, `/lib-deepclean`
**Pozíció:** persistence layer kartográfusa. Két szinten indexel: tier-1 (vault root) + tier-2 (per-Area scoped).
**Speciális:** kontextus-védett retrieve — a hívó kontextusa nem hízik fel, csak a summary jön vissza.

### 4.2 Maestro — v0.2 LIVE
**Funkció:** Dual Conductor.
- **Brand-to-Site domain (5 mód):** `status`, `next`, `continue`, `start`, `audit` — Brand Spine 7+1 réteg / 3-tier pipeline (Lean/Standard/Premium) felmérése, következő lépés javaslata, projekt-state karbantartás per-projekt `brand-spine-state.md`-ben.
- **Agent Family domain (4 mód):** `team-status`, `team-audit`, `team-promote`, `team-introduce` — meta-management. `team-promote` közös szabályt húz az egész család-tagra (analóg Curator promote-tal). `team-introduce` új agent scaffoldol.

**Speciális:** önreflexív — saját canonicalja is része minden `team-promote`-nak.

### 4.3 Curator — v0.2 LIVE
**Funkció:** Representation layer kurátor. `_dashboards/` HTML dashboard-család mestere.
**Módok (7):** `survey`, `build`, `tend`, `retire`, `audit`, `serve`, `promote`
**Slash:** `/dash-survey`, `/dash-build`, `/dash-tend`, `/dash-retire`, `/dash-audit`, `/dash-serve`, `/dash-promote`
**Pozíció:** Librarian testvére — Librarian a persistence layer kartográfusa, Curator a representation layer kurátora.
**Speciális:** `_dashboards/_design/DESIGN_SYSTEM.md` a forrás-az-igazságra a stílusokra. Dashboard-server portja: 4321.

### 4.4 Sage — v0.2 LIVE (scheduling pending)
**Funkció:** Cognition Curator. A BDOS cognition layer operátora.
**Módok (5):** `harvest`, `curate`, `chat`, `learning-ops`, info-csoport (`status`, `summary`, `find`, `edit`, `promote`, `index`)
**Slash (14):** `/sage-status`, `/sage-harvest`, `/sage-curate`, `/sage-summary`, `/sage-find`, `/sage-chat`, `/sage-edit`, `/sage-promote`, `/sage-index`, `/sage-learnings`, `/sage-learning-accept`, `/sage-learning-reject`, `/sage-learning-retire`, `/sage-learning-edit`

**Mit csinál:**
- Naponta 06:00-kor a **ChatGPT "Referencia chat"-ből** (Chrome MCP-vel) gondolatokat extractál
- Strukturált note-okká alakítja → `02_Areas/Personal Growth/Ideas/thoughts/`
- Atomic note-okat ápol history-szekcióval → `02_Areas/Personal Growth/Ideas/atomic/`
- Hétfő 06:05-kor `curate` mód: trend-analízis, kategória-revízió, kapcsolat-keresés, Librarian-kérések main Claude orchestrátoron át

**Innováció — meta-learning loop:** Sage explicit, user-reviewable tanulságokat ír a saját munkájáról (`00_Prompts/BDOS/agents/sage/learnings/proposals|active|retired`). Cap: 15 active / 2000 token preamble. Ez NEM rejtett súly — minden tanulság markdown, user edit/törölheti.

**Csend default:** Sage csak akkor notifikál, ha minta van. Inkább 1 erős signal, mint 10 zaj.

**Teljes design:** `00_Prompts/BDOS/agents/sage/SAGE_DESIGN_v0.1.md` (v0.2 állapotban).

**Vault output home:** `02_Areas/Personal Growth/Ideas/` (thoughts/ + atomic/ + _inbox/ + _journal/ + curate/ + 00_INDEX.md + 00_CATEGORIES.md).

**Referencia chat URL:** `https://chatgpt.com/g/g-p-67987afa409c8191b7ce9f798c887544-szemelyes-gondolatok/c/6a1265db-8910-83eb-8677-1e977c03fc01`

**Status:** placeholder fájlok mind a helyén, **scheduling pending** — a remote/local cron architektúra-kérdés miatt halasztva. Lokális macOS launchd plist a tervezett megoldás (smoke test után).

### 4.5 Presto — v0.2 LIVE (formerly Herald)
**Funkció:** Marketing Engine Executor. Distribution layer egyik fele (one-to-many).
**Módok (7):** `status`, `today`, `plan`, `run`, `resume`, `measure`, `index`
**Slash:** `/pres-status`, `/pres-today`, `/pres-plan`, `/pres-run`, `/pres-resume`, `/pres-measure`, `/pres-index`

**Mit csinál:** több projekten átívelő kampánymenedzsment markdown-natív engine-nel:
- `Marketing/MARKETING_ENGINE.md` per Area
- `Marketing/Pipeline.md` per Area
- `Marketing/Campaigns/<slug>/CAMPAIGN.md` per kampány
- Cross-project aggregátor: `_dashboards/00_MARKETING_INDEX.md`

A Cowork `marketing` plugin 8 skilljéből választ (`campaign-plan`, `draft-content`, `brand-review`, `competitive-brief`, `seo-audit`, `performance-report`, `email-sequence`, `content-creation`).

**Maestro testvére:** Maestro = **build** (brand→site), Presto = **run** (site→piac). Együtt a Brand Spine Pulse-rétegét hajtják.

**Etimológia:** olasz zenei tempó-jelölés (presto = gyors). Plusz: press + Pixar Presto mágus-short = három réteg jelentés. Maestro/Presto duett — karmester + tempó.

**Pilot:** ExarLabs Fázis 2.

### 4.6 Broker — v0.1 LIVE (placeholder)
**Funkció:** Sales Engine Executor. Distribution layer másik fele (one-to-one).
**Módok:** TBD — várhatóan Presto-mintát követi (`status`, `today`, `plan`, `run`, `resume`, `measure`, `index`), de NEM lockolt.
**Slash:** **nincs még** — prefix `brk-` foglalt, fájlok v0.2-ben jönnek.

**Mit csinál (tervezett):** one-to-one sales — lead tracking, pipeline management, outreach drafts, deal status, follow-ups, proposal prep. Kétirányú: outbound + prospect-válaszok befogadása.

**Presto testvére:** Presto = marketing distribution (one-to-many), Broker = sales distribution (one-to-one). A cognition/distribution fal mindkettőre érvényes.

**Status:** placeholder canonical + registration. Capability-fejlesztés Presto-mintára iteratív lesz.

---

## 5. Tervezett agentek (még nincsenek)

A `00_AGENTS_INDEX.md` "Planned agents" szekciója:
- Product Strategist — BD stratégia, retention, second-order probability
- Operations Steward — Sprint, workflow, repo hygiene, deploy safety
- Exploration Agent — Radikális ötletek, fork-szerű exploráció
- Validator — Cross-check, második vélemény

**Cél: 4-5 aktív agent**, nem 15-20 (agent sprawl elkerülése). Jelenleg 6 — épp a felső határnál vagyunk.

---

## 6. Az agentek közti kapcsolatok (a graph élei)

A főnaptár Agents-tabján (force-directed graph) ezek élként renderelődnek:

- **Maestro → mindenki** (orchestrates the family, team-* módok)
- **Maestro ↔ Curator** (dual view of the family: dynamic vs static)
- **Curator → mindenki** (representation layer építője az összesnek)
- **Sage → Librarian** (curate-kor Sage kéréseket fogalmaz, main Claude továbbít)
- **Sage → Presto** (cognition → distribution, permitted flow a falon át — szigorú szabályokkal)
- **Sage → Broker** (ugyanaz a wall + permitted flow)
- **Presto ↔ Broker** (sibling distribution agents)

**Flat orchestration:** a BDOS jelenleg flat — agentek nem hívják egymást direkt. Main Claude orchestrál. Hierarchia akkor élesedik, ha 3+ worker egy domain alatt (jelenleg messze vagyunk).

---

## 7. Architekturális invariánsok (NEM tárgyalható szabályok)

1. **A cognition és distribution között fal van.** A marketing soha nem dönti el, mit kell gondolni.
2. **Minden publikálás emberi jóváhagyáshoz kötött.** Sem Presto, sem Broker, sem bármely jövőbeli agent nem publikál autonóm módon.
3. **Markdown-natív state.** Minden agent-állapot `.md` fájlokban él, frontmatter YAML-lel. Soha nem JSON-only.
4. **Flat orchestration.** Agent nem hív agentet direkt — main Claude közvetít.
5. **Verzió-szinkron.** Canonical (`00_Prompts/BDOS/agents/<name>.md`) és registration (`.claude/agents/<name>.md`) verzió-mezője mindig egyezzen.
6. **No hardcode dashboardokban.** A `_dashboards/*` HTML soha nem tartalmaz konkrét tartalmat — minden adat futásidőben jön a `.md` source-of-truth fájlokból.
7. **Sage csend default.** Sage csak akkor notifikál, ha minta van. Inkább elcsendesedik, mint zajos.
8. **Inbox > false positive.** Minden agent: bizonytalan művelet → `_inbox/`, soha hallucinált note/akció.
9. **Append-only journal.** Minden agent-akció auditolt egy `_journal/`-ban (vagy adat-jellegű audit trail-ben).
10. **A főnaptár-dashboard a vault élő tükre.** Ha valamit nem ír egy markdown fájl, az nem jelenik meg a dashboardon.

---

## 8. Naming convention (családi stílus)

A 6 agent neve **5 etimológiai forrásból**, **stilisztikailag koherens**:

| Agent | Etimológia | Mit kódol |
|---|---|---|
| **Librarian** | angol, funkcionális | knowledge manager |
| **Maestro** | olasz, zenei (karmester) | orchestrator |
| **Curator** | latin, szerep | representation kurátor |
| **Sage** | angol, bölcsesség | cognition érlelő |
| **Presto** | olasz, zenei (tempó) + press + Pixar | marketing executor |
| **Broker** | angol, funkcionális | sales intermediary |

**Mintázat:** keverék angol funkcionális (Librarian, Sage, Broker) + latin/szerep (Curator) + olasz/zenei (Maestro, Presto). Egy új agent névadásakor érdemes a meglévő mintázathoz illeszkedni vagy újabb réteget tudatosan bevezetni.

**Slash prefix konvenció:** 3-4 betű, kebab-case (`lib-`, `dash-`, `pres-`, `brk-`, `maestro-`, `sage-`).

---

## 9. State és audit trail

Minden agent egy **single source of truth** fájlt tart karban, amit a dashboard élőben olvas:

| Agent | State fájl |
|---|---|
| Sage | `00_Prompts/BDOS/agents/sage/state/last_run.md` (schema: `sage.lastrun.v1`) |
| Presto | `02_Areas/<area>/Marketing/Pipeline.md` per Area |
| Curator | `_dashboards/00_DASHBOARD_INDEX.md` |
| Maestro | `<project-area>/brand-spine-state.md` per projekt + `00_AGENTS_INDEX.md` |
| Librarian | tier-1 index + tier-2 unit indexek |
| Broker | TBD (v0.2-ben) |

**Schema-zás:** minden state-fájl frontmatterben jelöli a séma-verzióját (pl. `schema: sage.lastrun.v1`). Backward-compatible bővítés engedélyezett, törlés tilos.

---

## 10. Meta-learning loop (Sage innovációja)

Ez az **egyetlen agent** ami **a saját munkájáról** is tanul — explicit, human-readable módon.

**Helye:** `00_Prompts/BDOS/agents/sage/learnings/`
**Életciklus:** `proposed → active → retired`
**Cap:** max 15 active / 2000 token preamble
**Védelmek:** kötelező evidence-szel (min. 2 journal-hivatkozás), user-reviewable, retirable

**Tanulság-típusok (8):** `harvest-pattern`, `category-naming`, `atomic-detection`, `user-taste`, `voice-style`, `failure-mode`, `linking-pattern`, `signal-noise`

**Filozófia:** Sage tanul, **de láthatóan tanul**. Minden tanulság markdown. Nem rejtett súly. **Sage javaslattevő, te döntéshozó** — pont mint a publish-gate marketing oldalon.

Ez a minta **kiterjeszthető más agentekre** (Presto editorial taste, Broker negotiation patterns, stb.) — de jelenleg csak Sage rendelkezik vele.

---

## 11. Dashboard architektúra

**Belépő:** `_dashboards/index.html` v0.7.0 — kétnézetes tab-switcher.

| Tab | Tartalom |
|---|---|
| **Areas** | A meglévő area-hierarchia (Sonrisa, Navigátor, ExarLabs, stb.) |
| **Agents** | d3.js v7 force-directed graph 6 agent-csomóponttal, 4 színkódolt élkategóriával, draggable, kattintható |

**Per-agent detail dashboards:**
- **Sage:** `_dashboards/sage/index.html` v0.1.0 — 9 panel, élő-fetch, zero hardcode, schema `sage.lastrun.v1`-ből olvas
- **Többi (Librarian, Maestro, Curator, Presto, Broker):** **nincs még** — "Detail page coming soon" overlay a kártyán

**Design system:** `_dashboards/_design/DESIGN_SYSTEM.md` (Curator karbantartja, v0.1.0).

**Server:** localhost:4321, indít/megáll: `/dash-serve` (Curator SERVE mód).

**Auto-refresh:** 8s polling konvencionálisan az egész családban. SSE change events ha a dash-server fut.

---

## 12. Pending work — mi következik

### Sage
- [ ] **Smoke test:** user beilleszti a mockolt referenciát a Referencia chatbe (lásd `00_Prompts/BDOS/agents/sage/REFERENCE_FORMAT.md` §smoke test). Aztán kézzel `/sage-harvest`, megnézzük a dashboardon.
- [ ] **Local scheduling:** macOS launchd plist írása `~/Library/LaunchAgents/`-be — daily 06:00 (`sage-harvest`) + hétfő 06:05 (`sage-curate`). NE Anthropic cloud routine — Sage Chrome MCP-t és lokális fájlrendszert igényel.
- [ ] **Első éles futás után** — figyelni az első learning-proposalokra, finomítani.

### Broker
- [ ] **v0.2 design:** modes spec, slash commands generálása (`brk-status`, `brk-today`, stb. — Presto-mintára), `SalesEngine.md` template a per-Area state-hez, `_dashboards/00_SALES_INDEX.md` cross-project aggregátor.
- [ ] Plugin kiválasztása sales-skillekhez (Cowork sales plugin? külön?)

### Detail dashboardok
- [ ] Per-agent dashboard build (Librarian, Maestro, Curator, Presto, Broker) — mind élő-fetch, hardcode-mentes, a Sage dashboard mint reference implementation
- [ ] Curator-on át (`/dash-build`), 1-2 per session ütemben

### Tervezett agentek (a 4-5 cap miatt csak akkor, ha tényleg kellenek)
- Product Strategist
- Operations Steward
- Exploration Agent
- Validator

---

## 13. Kritikus fájlok — first-read list új session-höz

A leggyorsabb ramp-up sorrend:

1. `00_Prompts/BDOS/CLAUDE.md` — BDOS belépő, agent-tábla
2. `00_Prompts/BDOS/00_AGENTS_INDEX.md` — minden agent meta-state
3. `00_Prompts/BDOS/00_BDOS_PRIMER.md` — ez a dokumentum (ha még nem olvastad)
4. `00_Prompts/BDOS/brainstorm/brainstorm_cognition_stack_2026-05-23.md` — a cognition stack felismerés (alap-filozófia)
5. `CLAUDE.md` (vault root) — vault konvenciók, PARA
6. `00_Prompts/BDOS/agents/sage/SAGE_DESIGN_v0.1.md` — a legrészletesebb agent-spec (v0.2 állapotban)
7. `_dashboards/_design/DESIGN_SYSTEM.md` — dashboard design system
8. `_dashboards/index.html` — főnaptár (Areas/Agents tabs)

---

## 14. Hogyan fejleszd tovább a BDOS-t

### Új agent szervezése
```
/maestro-team-introduce --name=<slug> --description="..." --modes=mode1,mode2,...
```
Maestro scaffoldolja: canonical + registration + AGENTS_INDEX + BDOS/CLAUDE.md + (opcionálisan) slash command csomag.

### Meglévő agent bővítése (új mód, új capability)
1. Edit canonical: `00_Prompts/BDOS/agents/<name>.md`
2. Sync version mindkét fájlon (`00_Prompts/...` és `.claude/agents/...`)
3. Új slash command(ok) hozzáadása `.claude/commands/<prefix>-<mode>.md`-ként
4. AGENTS_INDEX frissítése
5. Ha a teljes család-ra hat: `/maestro-team-promote` mód a változás propagálására

### Új dashboard építése
```
/dash-build --target=<path> --recipe=...
```
Curator a `_dashboards/_design/DESIGN_SYSTEM.md` + recipe alapján generál. Audit + launcher-regisztráció + index-frissítés automatikus.

### Új vault-area indexelése (tier-2)
```
/lib-index 02_Areas/<area-neve>
```
Librarian 5 index-fájlt generál (00_INDEX, KNOWLEDGE_MAP, DECISIONS, OPEN_QUESTIONS, GAPS).

### Vault egészségi check
```
/lib-audit
```
Stale fájlok, hiányzó frontmatter, struktúra-anomáliák.

### Agent család egészségi check
```
/maestro-team-audit
```
Verzió-sync, AGENTS_INDEX-konzisztencia, broken cross-referencia.

---

## 15. Záró elv

> **Ne építs autonóm intelligenciát. Építs külsősített kogníció-infrastruktúrát.**
>
> **Az AI megfigyel, struktúrál, javasol. Az ember dönt, ízlést gyakorol, irányt tart.**
>
> **Az érték nem a sebességben, hanem a stabilitásban. Inkább 5 jól kalibrált agent évek óta működve, mint 50 agent amik egymást túlordibálják.**

---

## Quick reference — slash command leltár

**Librarian (6):** `/lib-find`, `/lib-index`, `/lib-tidy`, `/lib-audit`, `/lib-integrate`, `/lib-deepclean`

**Maestro (10):** `/maestro`, `/maestro-status`, `/maestro-next`, `/maestro-continue`, `/maestro-start`, `/maestro-audit`, `/maestro-team-status`, `/maestro-team-audit`, `/maestro-team-promote`, `/maestro-team-introduce`

**Curator (7):** `/dash-survey`, `/dash-build`, `/dash-tend`, `/dash-retire`, `/dash-audit`, `/dash-serve`, `/dash-promote`

**Sage (14):** `/sage-status`, `/sage-harvest`, `/sage-curate`, `/sage-summary`, `/sage-find`, `/sage-chat`, `/sage-edit`, `/sage-promote`, `/sage-index`, `/sage-learnings`, `/sage-learning-accept`, `/sage-learning-reject`, `/sage-learning-retire`, `/sage-learning-edit`

**Presto (7):** `/pres-status`, `/pres-today`, `/pres-plan`, `/pres-run`, `/pres-resume`, `/pres-measure`, `/pres-index`

**Broker (0):** placeholder, slash command-ek v0.2-ben

**Összesen:** 44 slash command (6+10+7+14+7+0).

---

## Verzió-történet

| Verzió | Dátum | Változás |
|---|---|---|
| 1.0 | 2026-05-24 | Első kiadás — 6 aktív agent (Librarian v0.5, Maestro v0.2, Curator v0.2, Sage v0.2, Presto v0.2, Broker v0.1 placeholder). Főnaptár v0.7.0 Areas/Agents tabs. Sage dashboard v0.1.0. |

**Frissítendő:** új agent érkezésekor, meglévő agent major-verzió ugrásakor, vagy ha architekturális invariáns változik.
