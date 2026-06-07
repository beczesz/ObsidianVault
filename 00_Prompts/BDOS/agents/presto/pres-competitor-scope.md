---
title: /pres-competitor — Presto skill scope (design)
date: 2026-05-28
author: Becze Szabolcs
status: draft
version: 0.1.0
description: Scope/design doc egy új Presto módhoz (/pres-competitor) — versenytárs-csatorna gap-analízis. A claude-youtube `competitor` 4-agent recipe + a /watch (claude-video) mint vizuális data-source kombinációja. Magyar podcast-versenytársakra adaptálva. NEM kész skill — scope-döntésre vár.
id: b3e8c1d4-5a2f-4e9b-9c3d-7f1a8e6b4c2d
index_schema_version: 1
bdos_index: true
tags: [bdos, presto, competitor-analysis, skill-scope, navigator]
---

# /pres-competitor — Presto skill scope (design)

> **Státusz: draft scope.** A `claude-youtube` skill-értékelés (2026-05-28) anchor-findingje: a `competitor` sub-skill az egyetlen, amire nincs alternatívánk a BDOS-ben. Ez a doc scope-olja, hogyan lenne belőle natív Presto mód.

## Miért

A Presto jelenleg **kifelé** terjeszt (distribution), de **nincs versenytárs-intelligencia** módja. A `claude-youtube:competitor` sub-skill 4-agent recipe-je (top-video / keyword-gap / format-gap / audience-gap) bizonyítottan hiányt tölt be — de generikus US-creator-kontextusú és angol. Egy natív `/pres-competitor` mód:
- magyar podcast-versenytársakra kalibrált,
- a `/watch` (claude-video) skill-lel **vizuálisan is** elemzi a versenytárs-hookokat (nem csak metaadat),
- a Presto Channel DNA + audience-learning rendszerbe csatol vissza (resonance signal, nem write-back Sage-be).

## Pozíció a Presto módok között

| Mód | Irány | Most |
|-----|-------|------|
| adapt / draft / prepare / publish | kifelé (distribution) | ✅ |
| audience / measure / reflect | befelé (saját teljesítmény) | ✅ |
| discover | kifelé (új platform/community signal) | ✅ |
| **competitor** | **kifelé (versenytárs-intelligencia)** | 🆕 javasolt |

`discover` testvére: a `discover` új *platformot/közösséget* keres; a `competitor` adott *versenytárs-csatornákat* elemez gap-ekért.

## Input

```
/pres-competitor --area <Area> --competitors <handle1,handle2,...> [--depth quick|full] [--visual]
```

- `--area` — melyik Area DNA-jához viszonyítunk (pl. Navigátor Podcast)
- `--competitors` — max 3 csatorna (handle vagy URL)
- `--depth` — `quick` (metaadat only) vagy `full` (4-agent + visual)
- `--visual` — `/watch`-csal a top-videók hook-jainak frame+transcript elemzése

## 4-agent recipe (claude-youtube competitor-ból adaptálva)

| Agent | Mit néz | Data-source |
|-------|---------|-------------|
| A — Top-video | top 10 videó cím/thumbnail/téma-minta | `mcp__youtube__` Analytics (közvetett) + Chrome MCP / `/watch` |
| B — Keyword-gap | versenytárs kulcsszavak vs. saját lefedettség | cím/leírás-elemzés + (opcionális) DataForSEO |
| C — Format-gap | formátumok (interjú/szóló/panel/short) teljesítmény-relatíve | manuális + Analytics |
| D — Audience-gap | komment-bányászat: panaszok, kérdések, kérések | Chrome MCP komment-olvasás |

**Visual réteg (`--visual`):** a top-videók első 30s-ét `/watch`-csal (frame + lokális magyar Whisper) — a tényleges hook-stratégia, NEM a leírásból kitalálva.

## Magyar versenytárs-lista bootstrap (Navigátor)

Kiindulási kandidátusok (validálandó, hogy tényleg adjacent niche):
- **Csakabaj** — magyar long-form podcast (a vault Synthesis/Csakabaj már tartalmaz 51-epizód referencia-térképet → meglévő baseline!)
- **Bulvár Pszichológia** — pszichológia-fókusz, részleges téma-átfedés (S-tier Navigator-téma)
- **Hangoló** / hasonló magyar mélyinterjú-csatornák — validálandó

> Megjegyzés: a Csakabaj-ra már van `02_Areas/Navigátor Podcast/Synthesis/Csakabaj/synthesis_map.md` (PopScore + HostScore). Ez a `/pres-competitor` első éles futásának ideális tesztalanya — van mihez hasonlítani.

## Transport-döntés

| Adat | Transport | Megjegyzés |
|------|-----------|------------|
| Versenytárs metaadat | DataForSEO MCP (ha lesz) VAGY Chrome MCP | Data API kvóta 0 |
| Komment-bányászat | Chrome MCP (YouTube web) | Data API kvóta 0 |
| Vizuális hook | `/watch` (lokális, ingyen) | frame + magyar Whisper |
| Saját baseline | `mcp__youtube__` Analytics API | működik |

## Output

`02_Areas/<Area>/Marketing/Competitor/<competitor-slug>-<date>.md` — gap-analízis report:
1. Versenytárs-profilok (subs, cadence, formátum-mix)
2. Top-video minták (cím/thumbnail/téma)
3. Content-gap map (ők lefedik, mi nem)
4. Format-gap
5. Audience-gap (komment-igények)
6. Outlier-videók (3x+ csatorna-átlag)
7. Differenciálási szögek (NEM másolás — pozicionálás)

Plusz: **resonance/insight signal** a Presto audience-learning rendszerbe (proposed insight, emberi review-ra).

## Guardrails (Presto-konzisztens)

- **Confirmation gate** minden futás előtt (mit elemzünk, mely csatornákat)
- **NEM másol** — gap-eket és pozicionálást ad, nem "csináld ugyanazt"
- **Read-only** a versenytárs-tartalomra (komment-olvasás, NEM komment-írás)
- A `competitor-context` mint sales-learning-típus már létezik Broker-nél — itt **marketing-insight** ekvivalens

## Nyitott kérdések

| # | Kérdés | Döntésre vár |
|---|--------|--------------|
| 1 | DataForSEO MCP integráljuk-e (keyword-volume valós adat)? | költség vs. érték — most Chrome MCP fallback |
| 2 | A 4-agent tényleg parallel sub-agent legyen, vagy szekvenciális inline? | context-budget; Navigator-méretnél inline elég lehet |
| 3 | Külön slash-command (`/pres-competitor`) vagy `/pres-discover --mode competitor`? | mód-sprawl elkerülése |
| 4 | Milyen gyakran fusson? (negyedéves competitor-benchmark?) | cadence-döntés |

## Következő lépés (ha zöld)

1. Presto canonical (`presto.md`) — új mód-szekció + `presto.competitor.v1` output-séma
2. Slash-command scaffold (`.claude/commands/pres-competitor.md`)
3. Első éles futás: Csakabaj (van baseline) `--visual`-lal
4. Eredmény → Navigator-YT DNA differenciálási insight

## Hivatkozott

- Skill-értékelés: [`../../_inbox/youtube-skill-integration-candidates.md`](../../_inbox/youtube-skill-integration-candidates.md)
- Navigator-YT DNA: [`../../../../02_Areas/Navigátor Podcast/Marketing/ChannelDNA/Navigator-YT.md`](../../../../02_Areas/Navigátor%20Podcast/Marketing/ChannelDNA/Navigator-YT.md)
- /watch patch: [`../../capabilities/reel-factory/patches/README.md`](../../capabilities/reel-factory/patches/README.md)
- Presto canonical: [`../presto.md`](../presto.md)
