---
title: Navigátor Podcast — Publications könyvtár
date: 2026-05-26
author: Becze Szabolcs
status: active
description: A Navigátor Podcast egyedi marketing-publikációinak (presto.publication.v2 schema) tárolója. Minden publikálandó egység — YouTube poszt kísérő szöveg, Facebook poszt, Patreon frissítés — itt él, amíg el nem éri a Published staget.
id: 44192f95-817e-45d0-b165-bb88a8a3cf24
index_schema_version: 1
bdos_index: true
---

# Navigátor Podcast — Publications

Ez a mappa a Navigátor Podcast egyedi publikációinak (`presto.publication.v2` schema) gyűjtőhelye.

## Konvenciók

**Fájlnév:** `pub-<channel>-<YYYYMMDD>-<slug>.md`

Példák:
- `pub-facebook-20260526-ep43-gyasz-launch.md`
- `pub-youtube-20260526-ep43-gyasz-community-post.md`
- `pub-patreon-20260601-ep43-patreon-update.md`

**Életciklus:**
```
Draft → Prepared → Approval → Scheduled → Published (→ 30 nap után Archive)
```

A `publication_status` mező a `presto.publication.v2` frontmatterben követi az állapotot.

## Kapcsolódó fájlok

- `../Pipeline.md` — a kanban nézet, ahol a publikációk stage-ei láthatók
- `../MARKETING_ENGINE.md` — brand-hang és tone-útmutató minden drafthoz
- `../Campaigns/` — kampány-szintű koordináció (ha N publikáció együtt mozog)
