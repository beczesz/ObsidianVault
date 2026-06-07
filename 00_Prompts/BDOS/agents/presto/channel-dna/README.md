---
title: channel-dna — deprecated location notice
date: 2026-05-26
author: Becze Szabolcs
status: deprecated
description: Ez a mappa a Channel DNA fájlok korábbi, globális tárolási helye volt. A per-Area migrációval (2026-05-26) minden Channel DNA fájl az adott Area Marketing/ChannelDNA/ mappájába költözött.
id: e7a2c3f1-9b4d-4e8a-b2f6-1d3a5c7e9f01
index_schema_version: 1
bdos_index: false
---

# Channel DNA — Deprecated Location

Ez a mappa **2026-05-26-tól nem tartalmaz aktív Channel DNA fájlokat.**

## Miért költöztek el?

A globális, agent-szintű Channel DNA tárolás nem tükrözte a csatornák Area-specifikus valóságát. Egy Navigator YouTube DNA-nak nem ugyanazok a tone-, audience- és forbidden-pattern-szabályai, mint egy jövőbeni Deák Húsüzlet YouTube csatornának — még ha mindkettő ugyanazon a platformon él is.

A per-Area model:
- közelebb tartja a DNA-t a csatorna tényleges üzemeltetőjéhez
- lehetővé teszi a `channel` mód `area:` szűrését
- elkülöníti a platform-általános szabályokat (presto.md §6.18) a csatorna-specifikus tanultságoktól

## Ahol most élnek a Channel DNA fájlok

```
02_Areas/<ProjectName>/Marketing/ChannelDNA/
└── <Platform-Slug>.md        # presto.channel-dna.v2 schema
```

**Aktív fájlok:**

| Area | Platform | Fájl |
|------|----------|------|
| Navigátor Podcast | YouTube | `02_Areas/Navigátor Podcast/Marketing/ChannelDNA/Navigator-YT.md` |

## Hogyan referál erre Presto?

A `channel` mód (`list`, `view`, `update-tone`) az `area:` paramétert használja a megfelelő ChannelDNA/ mappa megtalálásához. Ha `area:` nem adott, az összes Area ChannelDNA/ mappáját bejárja.

---

*Migrálta: Presto v0.8.0 — 2026-05-26*
