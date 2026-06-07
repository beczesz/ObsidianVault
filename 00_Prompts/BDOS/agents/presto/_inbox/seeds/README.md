---
title: Presto Seeds Inbox — README
date: 2026-05-25
author: Becze Szabolcs
status: active
description: Leírja a Presto Seeds inbox szerepét és használatát. Ide kerülnek az összes nyers input-ötletek (URL-ek, idézetek, atomic-refek, képek), amelyekből Publication-ök születnek. A Seed perzisztens — addig marad, amíg a user lezárja.
id: af311f37-edc4-4839-be72-985d722eb943
index_schema_version: 1
bdos_index: true
---

# Presto Seeds Inbox

## Mi ez a könyvtár?

Ez az **elsődleges bemeneti réteg** a Presto Marketing Engine-hez. Ide kerül minden raw input, amelyből Marketing Publication születhet.

## Mit raksz ide?

Bármit, ami publikációs szándék csírája lehet:

- **URL** — cikk, tweet, post, videó, amit meg akarsz osztani vagy ami inspirált
- **Inline szöveg** — gondolat, idézet, megfigyelés, ami kimondásra érdemes
- **Atomic-ref** — Sage atomic gondolat hivatkozása (`Ideas/atomic/*.md`)
- **BMC-quadrant** — Business Model Canvas egy negyedéből következő üzenet
- **Kép-ref** — kép path, amelyből carousel vagy visual story lehet
- **Egyéb** — bármi más, ami nem fér a fenti kategóriákba

## Hogyan kell létrehozni?

1. Hozz létre egy új fájlt: `seed-<YYYY-MM-DD>-<NNN>.md` (pl. `seed-2026-05-25-001.md`)
2. Használd a `presto.seed.v1` schemát (lásd `MARKETING_OS_SCHEMAS_v2.md` §1)
3. Töltsd ki a kötelező mezőket: `seed_id`, `title`, `source_type`, `source_ref`, `captured_at`, `captured_by`, `status`
4. Add a nyers forrás-szöveget/linket a body-ba

Presto is javasolhat Seed-eket (pl. Sage atomic-ból adaptation előtt), de mindig emberi jóváhagyással.

## Ki olvassa?

- **Presto `adapt` módja** — Seed-ből Publication draft-ot generál
- **Presto `today` módja** — aktív Seed-eket listáz, amelyekből még nem született Publication
- **Presto `status` módja** — scanneli az aktív Seed-eket a cross-project riporthoz

## Mikor lép tovább egy Seed?

A Seed **soha nem "lép tovább"** abban az értelemben, hogy eltűnik. Mindig itt marad.

**Állapotok:**
- `status: active` — még dolgozunk belőle, Publication-ök születhetnek
- `status: exhausted` — a user azt mondta: "kinyertük belőle mindent" (manuális döntés)
- `status: archived` — hosszabb inaktivitás után (nem töröljük, csak archivált)

**Egy Seed → N Publication.** Ugyanabból a Seed-ből több Publication születhet különböző Area-kban, különböző intent-ekkel. A `publications_spawned` mező trackeli ezeket.

## Példa

Lásd: `00_Prompts/BDOS/agents/presto/_examples/marketing-engine-v2/seed-bdos-markdown-substrate.md`

## Schema referencia

Teljes schema-spec: `00_Prompts/BDOS/agents/presto/MARKETING_OS_SCHEMAS_v2.md` — §1 `presto.seed.v1`
