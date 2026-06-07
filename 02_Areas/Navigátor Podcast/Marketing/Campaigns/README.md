---
title: Navigátor Podcast — Campaigns könyvtár
date: 2026-05-26
author: Becze Szabolcs
status: active
description: A Navigátor Podcast marketing-kampányainak (presto.campaign.v2 schema) tárolója. Kampány = N publikáció koordinált ernyője (pl. EP43 Gyász teljes launch-csomag). Minden kampány saját alkönyvtárban él CAMPAIGN.md primary state fájllal.
id: 1a861893-3afb-4ec7-90fe-40b267aaaf9c
index_schema_version: 1
bdos_index: true
---

# Navigátor Podcast — Campaigns

Ez a mappa a Navigátor Podcast koordinált marketing-kampányainak gyűjtőhelye.

## Mikor kell Campaign — mikor elég Publication?

**Publication elegendő:** egy csatornán egy publikáció (pl. egyetlen Facebook poszt EP43 launch napján).

**Campaign kell:** ha N publikáció koordináltan mozog együtt — pl. EP43 teljes launch-csomag (YouTube community post + Facebook poszt + Patreon update + esetleges Facebook hirdetés).

## Könyvtárstruktúra

```
Campaigns/
└── <campaign-slug>/
    ├── CAMPAIGN.md       ← primary state (presto.campaign.v2)
    ├── brief.md          ← opcionális — /marketing:campaign-plan output
    └── assets/           ← copy-draftok, képek, CSV-k
```

**Slug konvenció:** `ep<szám>-<téma>-launch` — pl. `ep43-gyasz-launch`

## Kapcsolódó fájlok

- `../Pipeline.md` — a kanban nézet, ahol a kampányok stage-ei láthatók
- `../MARKETING_ENGINE.md` — brand-hang és tone-útmutató minden kampányhoz
- `../Publications/` — egyedi publikációk (kampányhoz kapcsolhatók vagy önállóak)
