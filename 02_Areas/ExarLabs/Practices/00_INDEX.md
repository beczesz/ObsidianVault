---
schema: exarlabs.practices.index.v1
generated_at: 2026-05-27
description: ExarLabs Practice Areas élő indexe — cross-client kapacitás- és kutatási területek az ExarLabs unit alatt. Forge agent karbantartja. Minden practice area saját mappa NOTES.md-vel, struktúrált subfolderekkel (_inbox, research, patterns, decisions, experiments, proposals, learnings). Példa-szinten létrehozva 2026-05-27, Forge bootstrap idején.
maintained_by: Forge agent (v0.1)
unit: "ExarLabs"
practice_count: 2
id: a8f4c279-6b13-4e85-9d62-5c0a8e3f1b47
index_schema_version: 1
bdos_index: false
---

# ExarLabs Practice Areas — Index

> Élő index, Forge agent tartja karban. Generálás: `/forge-index` (v0.2-ben). Manuálisan most v0.1 boot-állapotban.

## Mi a practice area

**Practice area = stabil szakterület**, amit az ExarLabs team folyamatosan fejleszt, ami **több ügyfél-engagementen ível át**, és ami **research, design patterns, deliverables-mix-ként** él. NEM egyedi ügyfél-projekt (azt `Clients/` tartja). NEM ad-hoc kísérlet.

Az ExarLabs practice area-k a **kapacitás-réteg** ExarLabs-szempontból: research + repeatable deliverable mix. Pl. a Microsites egyszerre **kutatási terület** (hogyan generálunk gyönyörű, AI-asszisztált microsite-okat hatékonyan) ÉS **szolgáltatás** (kliensnek odaadható deliverable).

## Active practice areas (2)

| Practice | Maturity | Status | Owner | Triggered by | Last signal |
|---|---|---|---|---|---|
| [Microsites](Microsites/NOTES.md) | patterns-emerging | active | (TBD ExarLabs lead) | Internal: AI-assisted microsite factory capability (BDOS web-publishing) | 2026-05-27 (bootstrap) |
| [EU Digitalizare Grants](EU-Digitalizare-Grants/NOTES.md) | research | active | (TBD ExarLabs lead) | External: EU digitalizációs grant-call (PR Centru 2.2 Apel 2). Áthelyezve Sales-kohortból. | 2026-05-30 |

## Maturity stages

| Stage | Mit jelent | Practice areas a stage-ben |
|---|---|---|
| `research` | exploratory, nincs még stable pattern | EU Digitalizare Grants |
| `patterns-emerging` | 1-2 pattern már kikristályosodott, evidence < 3 | Microsites |
| `service-ready` | reusable proposalok van, 3+ ügyfél evidence egy patternre | — |
| `mature` | több service-tier, jól árazott, ismétlődő engagement | — |
| `retired` | nincs aktív kereslet, archive státusz | — |

## Candidates / Backlog

Olyan ExarLabs területek, amik felmerülnek, de még NEM kaptak practice area dedikációt:

- **AI Courses / Curriculum Development** — Ignis Academy környékéről átsoroló téma lehet
- **Brand-to-Site Pipeline** — BDOS `brand-to-site` capability ExarLabs-szempontú instantiate-ja
- **Web-Publishing Infrastructure** — Cloudflare / Netlify deploy automation, DNS, SSL
- **Design System Generation** — AI-assisted token + component generation

## Cross-unit / cross-area links

A Microsites practice area összefügg:
- **BDOS capability `web-publishing`** (technikai recept réteg, generic) — Microsites az ExarLabs-szempontú instantiate
- **BDOS capability `brand-to-site`** (upstream design rétg) — Microsites a downstream build/ship réteg
- Potenciálisan **CPS** ha valamely CPS-kliensnek microsite-deliverable kell

## Konvenciók

Lásd Forge canonical: [`00_Prompts/BDOS/agents/forge.md`](../../../00_Prompts/BDOS/agents/forge.md) §5 Storage Convention.

Kötelező subfolderek minden practice area-ban: `_inbox/`, `research/`, `patterns/`, `decisions/`, `experiments/`, `proposals/`, `learnings/`. Kötelező fájlok: `NOTES.md`, `learnings/00_INDEX.md`, `related-projects.md`, `open-questions.md`.

## Maintenance log

| Date | Action | Note |
|---|---|---|
| 2026-05-27 | Bootstrap | Forge v0.1 létrehozva. Első ExarLabs practice area: Microsites (példa-szintű, hogy bemutassuk a struktúrát cross-unit). |
| 2026-05-30 | Új practice | EU Digitalizare Grants felvéve. Áthelyezve a `Sales/Cohorts/regiunea-centru-digitalizare-2026/` Broker-kohortból (helyesen Forge-domain: cross-client, ismétlődő szolgáltatás-vonal). Sales-kohort törölve. Maturity: `research`. |
