---
schema: presto.todo.v1
todo_id: todo-20260528-ep40-thumbnail-swap
id: 3f9a2c7e-1b4d-4e8a-9c6f-5d2a8b3e7f1c
index_schema_version: 1
bdos_index: true
title: "EP40 thumbnail csere (anya-lánya ölelés)"
status: open
urgency: today
created_date: 2026-05-28
due_date: 2026-05-29
area: Navigátor Podcast
channel: youtube
source: user
related_episode: "EP40 — Fegyelmezés / Gál Ildikó"
related_video_published: 2026-04-10
action_type: thumbnail-swap
requires_human: true
description: "Mai teendő (user-kérés): EP40 (Fegyelmezés / Gál Ildikó) YouTube thumbnail cseréje egy nőre, aki a lányát öleli. Manuális csere YouTube Studio-ban (Chrome MCP fallback)."
tags: [navigator-podcast, ep40, thumbnail, todo, gál-ildikó, fegyelmezés]
---

## Teendő

**EP40 — Fegyelmezés / Gál Ildikó** YouTube thumbnail lecserélése.

- **Új vizuál:** egy nő, aki a **lányát öleli**.
- **Régi thumbnail:** (jelenlegi — ellenőrizendő YouTube Studio-ban)
- **Publikálva:** 2026-04-10
- **Csatorna:** Navigátor Podcast (Brand Account)

## Miért

User-kérés (2026-05-28). A fegyelmezés/nevelés téma érzelmi magja a szülő-gyerek kapcsolat — egy anya-lánya ölelés melegebb, kapcsolódóbb vizuális horgony, mint a jelenlegi thumbnail.

## Hogyan (végrehajtás)

1. Új thumbnail-kép beszerzése/kiválasztása (nő a lányát öleli) — **user adja vagy jóváhagyja**.
2. Navigator-YT DNA §4 + §10 thumbnail-szabályok ellenőrzése:
   - max 3-4 szó overlay (ha van), magas kontraszt
   - §10.1 title↔thumbnail synergy (ne ismételje a címet)
   - §10.2 mobile-legibility test (168×94px)
   - forbidden: fake-shocked arc, hamis kontroverzitás
3. Csere YouTube Studio-ban (Data API kvóta 0 → **Chrome MCP → YouTube Studio**, `youtube_set_thumbnail` ha a Data API megoldódna).
4. TODO lezárása: `/pres-todo --op close --id todo-20260528-ep40-thumbnail-swap`

## Státusz-napló

- 2026-05-28 — **ÁTÜTEMEZVE 2026-05-29-re** (due_date). Blocker: az új thumbnail-kép (nő öleli a lányát) — user adja/jóváhagyja.

## Megjegyzés

- EP-azonosítás: a CLAUDE.md epizód-tábla szerint **EP40 = Fegyelmezés / Gál Ildikó** (van egy archivált EP39 is hasonló címkével — az korábbi átszámozás maradványa; a kanonikus az EP40).
- A videó-ID a CLAUDE.md táblában nincs rögzítve EP40-re — végrehajtáskor YouTube Studio-ban azonosítandó cím szerint.
