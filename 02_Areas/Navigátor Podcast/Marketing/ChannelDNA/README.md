---
title: Navigátor Podcast — ChannelDNA mappa
date: 2026-05-26
author: Becze Szabolcs
status: active
description: A Navigátor Podcast per-Area Channel DNA fájljainak tárolóhelye. Minden fájl egy platform-specifikus csatorna-identitást ír le a presto.channel-dna.v2 sémával — tone, audience, forbidden patterns, posting rhythm, execution capabilities.
id: a4b8c2d6-e1f3-4a7b-9c5d-2e0f8a1b3c5d
index_schema_version: 1
bdos_index: true
---

# Navigátor Podcast — Channel DNA

Ez a mappa a Navigátor Podcast összes aktív platform-csatornájának Channel DNA fájljait tartalmazza.

## Konvenció

Minden fájl neve: `<ProjectName>-<Platform>.md`, például `Navigator-YT.md`.

Schema: `presto.channel-dna.v2` — a v1-hez képest kiegészítve:
- `area:` mező (melyik Area-hoz tartozik)
- `audience_data_source:` (honnan jönnek a demográfiai adatok)
- `insights:` blokk (Area-specifikus operacionalizált tanulságok)
- `anti_examples:` (konkrét, csatorna-specifikus tiltott formátumok)

## Aktív fájlok

| Platform | Fájl | Státusz |
|----------|------|---------|
| YouTube | `Navigator-YT.md` | proposal → elfogadandó |
| Facebook | `Navigator-FB.md` | proposal → elfogadandó |

## Hogyan frissül?

- Presto `channel update-tone` mód szerkeszti a `tone_overrides` mezőt
- Presto `insight operationalize` mód írja az `insights:` blokkot
- Emberi jóváhagyás szükséges minden strukturális változtatáshoz (`status: proposal → active`)

---

*Létrehozva: Presto v0.8.0 — per-Area Channel DNA migráció — 2026-05-26*
