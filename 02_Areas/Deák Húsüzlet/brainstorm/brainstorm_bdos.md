---
topic: BDOS — Business Development Operation System
created: 2026-05-10
last_updated: 2026-05-11
status: active
id: cf4f9d50-7322-4dcd-9845-25b96b4b8c73
index_schema_version: 1
---

# Brainstorm: BDOS — Business Development Operation System

> **Megjegyzés (2026-05-11):** A BDOS kanonikus belépője átkerült ide: [`00_Prompts/BDOS/CLAUDE.md`](../../../00_Prompts/BDOS/CLAUDE.md). Ez a fájl továbbra is a **DH-specifikus pilot-napló** — döntések, agent-választások, sprint-tapasztalatok a DH-pilot kontextusából. Univerzális BDOS-tartalmat az új belépőben tarts.

## Mission (working definition)

A BDOS **nem** folyamat-framework / playbook. A BDOS **AI-native cognition system**: stabil gondolkodási szerepek (agents) + perzisztens markdown állapot (Obsidian) + sessions, Claude Code-ban orchestrálva. A DH a kísérleti projekt amin validáljuk.

Forrás insight: ChatGPT conversation 2026-05-10 ([Cloud Code Desktop vs CLI](https://chatgpt.com/c/6a004d97-9838-8391-bcdd-e4fac1b1fce5)) — "Az agentek valójában externalized cognition fragments."

## Team (current session)
| AI | Role | URL |
|----|------|-----|
| ChatGPT | Strategist (külső, már gondolkodott a témán) | https://chatgpt.com/c/6a004d97-9838-8391-bcdd-e4fac1b1fce5 |
| Perplexity | Researcher (még nem hívva — prior art / agent-based BD frameworks) | — |
| Claude (Code) | Orchestrator + Executor | — |

Gemini és Copilot kihagyva v0.1-ben.

## Sessions
| Date | Team | Key Outcome |
|------|------|-------------|
| 2026-05-10 | ChatGPT (Strategist) + Claude (Orchestrator) | BDOS reframe: nem playbook, hanem agent system. Librarian v0.1 első agentként megépítve és lefuttatva globális + Deák scoped módban. 5+5 index fájl megírva. |

## Agent paletta (BDOS v0.1 jelöltek)

| Agent | Status | Cél |
|-------|--------|-----|
| **Librarian** | ✅ v0.4 LIVE | Knowledge Manager — 6 mód: index, retrieve, tidy, audit, integrate, deep-clean. Kontextus-védelem. Two-tier indexing. 9 tier-2 unit indexelve. |
| Product Strategist | tervezett | BD stratégia, retention, second-order probability |
| Operations Steward | tervezett | Sprint, workflow, repo hygiene, deploy safety |
| Exploration Agent | tervezett | Radikális ötletek, fork-szerű exploráció |
| Validator / Devil's Advocate | tervezett | Cross-check, második vélemény |

Cél: **4-5 agent**, nem 15-20 (agent sprawl elkerülése).

## Key Insights

- **Retrieval-based cognition** — agentek nem emlékeznek, visszakeresnek. A Librarian a kulcs réteg.
- **Stabilitás > intelligencia** — az agent értéke a szerep-stabilitás, nem az "okosság". A drift az igazi probléma a multi-purpose chatben.
- **Externalized cognition fragments** — minden agent egy saját gondolkodási mód külsővé tett verziója.
- **Operational cognition files** > source code — `01_PROJECT_STATE.md`, `CLAUDE.md`, brainstorm fájlok a "valódi" tudásréteg.
- **DH már félig BDOS** — 20 multi-AI brainstorm fájl, 5 SYNTHESIS doc, `01_PROJECT_STATE.md` v1.6, `TASKS.md` Jira sync, sprint retrospektívák. Csak nincs explicit agent layer fölötte.
- **Forkolás mechanikája** — Claude Code subagent = izolált context window, csak summary-t ad vissza → fő ablak nem hígul.

## Decisions Made

- 2026-05-10 — **Librarian az első agent** (retrieval réteg minden más előtt) — *Szabolcs*
- 2026-05-10 — **Two-tier scope**: global + per-unit scoped index. Cross-talk tiltva scoped módban — *Szabolcs*
- 2026-05-10 — **Librarian írhat/törölhet, de csak rendrakási céllal**, minden akció `00_GAPS.md`-be logolva — *Szabolcs*
- 2026-05-10 — **Agent fájl-hely**: `00_Prompts/BDOS/agents/<name>.md` (canonical) + `.claude/agents/<name>.md` (Claude Code registration) — *Szabolcs*
- 2026-05-10 — **Verziózás** kötelező minden agentnél (`version:` frontmatter + changelog) — *Szabolcs*
- 2026-05-10 — **v0.1 csapat**: ChatGPT + Perplexity + Claude (Gemini/Copilot kihagyva) — *Claude javaslat, Szabolcs implicit elfogadta*
- 2026-05-10 — **Skill stratégia**: v0.1 embedded, v0.3-ban külön skill fájlok ha kell — *Claude javaslat*
- 2026-05-11 — **Librarian v0.2: 4 mód egy agentben** (index/retrieve/tidy/audit) ahelyett hogy szétszednénk több agentre. Indok: KM = egységes szerep. Per-mód constraints biztosítják a stabilitást, nem agent-szeparáció — *Szabolcs*
- 2026-05-11 — **Hierarchikus szervezet (Manager + Workers) elhalasztva** v0.3-ra. 2 worker fölött a Manager prematúr. 3+ worker megjelenésekor élesítjük a Knowledge Manager Master agentet — *Claude javaslat, Szabolcs elfogadta*
- 2026-05-11 — **Kontextus-védelem mint központi alapelv** — a retrieve mód célja: a hívó (te, vagy másik agent) kontextusa érintetlen maradjon, mert a Librarian olvas helyette — *Szabolcs*
- 2026-05-11 — **Agent meta-index** (`00_Prompts/BDOS/00_AGENTS_INDEX.md`) létrehozva — minden agent canonical + registration + verzió egy helyen. Audit mód karbantartja — *Claude javaslat*
- 2026-05-11 — **Areas-dominant PARA konvenció deklarálva** vault-szintű `CLAUDE.md`-ben — *Szabolcs (válaszul a PARA-fájdalom kérdésére)*
- 2026-05-11 — **Sonrisa kanonikus hely: `02_Areas/Sonrisa/`** — `01_Projects/Sonrisa/` törölve, az egyetlen árva fájl áthelyezve — *Szabolcs*
- 2026-05-11 — **Slash command-ok élesben**: `/lib-index`, `/lib-find`, `/lib-tidy`, `/lib-audit` — *Claude implementálta*
- 2026-05-11 — **Two-tier indexing élesben**: tier-1 (vault gyökér) + tier-2 (5 unit scoped index: DH, Navigátor, Sonrisa, Resources, Archive). Librarian v0.3 retrieve algoritmus formalizálva. — *Szabolcs döntött, Claude implementálta*
- 2026-05-11 — **Archive és Resources mostantól indexelhetők** (előzőleg ki voltak zárva). Reference material kereshetővé vált. — *Szabolcs*
- 2026-05-11 — **Tier-2 körök kibővítve**: Szervezet fejlesztés (62), Ignis (144 full depth), ExarLabs (48), Personal Growth (31) → 9 tier-2 unit összesen — *Szabolcs*
- 2026-05-11 — **Librarian v0.4: 2 új mód**: `integrate` (vault-on kívüli mappák felmérése, javaslat-generálás importálható tartalmakra, read-only) + `deep-clean` (nagytakarítás: byte-azonos duplikátum/üres/temp törlés, stale archiválás, cross-reference check, dry-run default). 2 új slash command: `/lib-integrate`, `/lib-deepclean`. — *Claude auto-mode, default-okkal: integrate scope `~/Documents`/`~/Downloads`/`~/Desktop`, md+txt only v0.4, stale_days=180, archive default, byte-azonos+üres+temp törölhető. Felülvizsgálatra váró: csak ha kifogásolja Szabolcs.*
- 2026-05-11 — **Librarian v0.5: PDF olvasási képesség** — `pdftotext` (poppler) telepítve, integrate mód file_types: [md, txt, pdf]. SRT is olvasható. — *Szabolcs kérte*
- 2026-05-11 — **Pályázat hibrid split migráció lezárva**: új `02_Areas/Pályázat/` központi gyűjtő mappa létrehozva, 2 sub-projekttel (Ignis-Academy-EU-275k és Gergely-Istvan-Plan-de-afaceri). 7 fájl mozgatva Ignis Academy-ből + 2 archive meeting UNARCHIVE-olva + Szövetségesek + Gergely PDF + DECIZIE PDF (új import). Akadémia (Research, Business Dev, Startup Learning, dashboard, memory) MARADT Ignis Academy alatt. Cross-link bekerült mindkét CLAUDE.md/README-be. AFM Electromobil maradt Ignis kurzus alatt (tananyag). Veszprém-Kecskemét NEM költözött (önálló maradt). — *Szabolcs döntései szerint*
- 2026-05-11 — **IgnisAcedemy külső mappa megszűnt** (sikeres integráció után). 4 fájl mozgatva: HB067WP15 (Dani HY-DE Model paper) → Ignis Academy/Research/, 2 YC SRT → Ignis Academy/Startup Learning/, DECIZIE pályázat-jóváhagyási határozat → Pályázat/Ignis-Academy-EU-275k/02_dokumentumok/. — *Librarian integrate v0.5 javaslat, manuális végrehajtás*
- 2026-05-11 — **Pályázat split visszafordítva** (~1h után). Szabolcs meggondolta: a pályázat túl szorosan kötődik az akadémiához. `02_Areas/Pályázat/` mappa **MEGSZÜNT**, tartalma `02_Areas/Ignis Academy/Pályázat/` sub-folder-be költözött. Gergely István pályázat (partner-mentoring) **TÖRÖLVE**. A Decizie + 11 fájl (status, meetings, timeline, networking, todo, tasks, naplók) most az Ignis Academy alatti `Pályázat/` mappában él. Cross-link CLAUDE.md-ben frissítve. — *Szabolcs döntése. Tanulság: a "minden pályázat egy helyen" elv nem volt megvédhető — az Ignis Academy = a pályázat tárgya, túl szoros a kötés a két oldal között. Subfolder a tisztább megoldás.*

## Open Questions

- [ ] **PARA-eltérés tudatos?** `01_Projects/` szinte üres, minden Area-ban él. Ha igen, dokumentáljuk vault-szintű `CLAUDE.md`-ben (még nem létezik) — *for: Szabolcs*
- [ ] **Sonrisa CPS kanonikus hely** — `01_Projects/` vagy `02_Areas/`? Mindkettő él, oldani kell — *for: Szabolcs*
- [ ] **Melyik a következő agent?** Product Strategist (DH-specifikus BD gondolkodás) VAGY Operations Steward (sprint/workflow disciplína) VAGY általánosabb BDOS-Strategist (BD bármilyen projektre)? — *for: Szabolcs*
- [ ] **Librarian incremental refresh (v0.2)** — kell-e most, vagy várjunk amíg fáj? — *for: Szabolcs*
- [ ] **DH legal backlog** — bekerüljön Sprint 3-ba? Beta blokkoló — *for: Szabolcs (BD döntés, nem BDOS)*

## Context References

- Canonical agent definition: `00_Prompts/BDOS/agents/librarian.md`
- Claude Code registration: `.claude/agents/librarian.md`
- Global indexes: `0. Ideas Vault/00_INDEX.md`, `00_KNOWLEDGE_MAP.md`, `00_DECISIONS_INDEX.md`, `00_OPEN_QUESTIONS.md`, `00_GAPS.md`
- DH scoped indexes: `02_Areas/Deák Húsüzlet/00_*.md` (ugyanaz az 5)
- ChatGPT eredeti gondolkodás: lásd a beszélgetést a Team táblában

## Raw Notes

### 2026-05-10 — Session 1

- Felhasználó kérése: "Business Development Operation System, Deák a pilot, lépésről lépésre"
- Első Claude javaslat: fázis-térkép (Discovery → Validation → Pilot → Scale) framework — **elvetve** a ChatGPT beszélgetés olvasása után
- ChatGPT insight átvéve: agent = stable cognitive role, nem chat. BDOS = agent + state + session, nem playbook
- Szabolcs döntése: Librarian elsőnek
- Librarian v0.1 definíció megírva (`00_Prompts/BDOS/agents/librarian.md`), regisztrálva (`.claude/agents/librarian.md`)
- Két párhuzamos futás `general-purpose` subagenttel (a `librarian` subagent_type csak következő sessiontől élesedik)
- Global: 1224 fájl, 12 unit, 5 indexfájl
- Deák scoped: 174 fájl, 16+13+8 döntés, ~80 open question, 5 indexfájl
- **Kulcs felismerés a Librarian outputjaiból**: DH-ban már működik egy "brainstorm-perzisztencia" minta (20 brainstorm fájl + 5 SYNTHESIS). Ez a BDOS retrieval réteg konkrét sémájának visszafejtésére alkalmas.
