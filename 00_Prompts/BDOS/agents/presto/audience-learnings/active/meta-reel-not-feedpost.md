---
schema: presto.audience-learning.v1
learning_id: meta-reel-not-feedpost
type: format-fit
status: active
scope: cross-project
platforms: [facebook, instagram]
confidence: high
created_at: 2026-05-28
last_applied_at: 2026-05-28
applies_to: "minden vertikális (9:16) videó Meta-platformon (FB + IG)"
description: "Meta vertikális videót mindig Reel-ként kell feltölteni, nem feed-posztként — a feed-poszt 4:5-re vágja és levágja a tetejét/alját. Plusz: kézi borítókocka + középső safe-zone (felső 10% / alsó 20% / jobb 10% kerülendő)."
id: c2d8f6a4-1e73-4b59-9f08-3a5c7d9e2b14
index_schema_version: 1
bdos_index: true
---

# Learning: Meta Reel ≠ feed-poszt (vertikális videó vágás)

## A tanulság

Vertikális (**9:16**) videót a Facebook és az Instagram **Reel-ként** teljes kerettel jelenít meg, de **feed-posztként 4:5-re vágja** — levágja a felső/alsó sávot (fej teteje, alsó felirat). Ezért:

1. **Mindig Reel-ként** tölts fel vertikális videót (FB: *Létrehozás → Reel*; IG: a feltöltőben a *Reel* fül), NEM sima fotó/videó posztként.
2. **Borítókocka (cover) kézi kiválasztása** — a feed-thumbnail akkor is vághat (4:5 / 1:1), ha a teljes Reel 9:16.
3. **Safe-zone a vágásnál ÉS a forgatókönyvnél:** a kulcs-tartalom (fej, fő alany, felirat) a középső zónába kerüljön — felső **~10%**, alsó **~20%**, jobb oldal **~10%** (UI-gombok) kerülendő.

## Evidencia

- 2026-05-28 — Fókuszpont úrnapi reel "levágott" eset: a videó feed-posztként ment fel, a feed-crop levágta a beszélő fej tetejét és beszorította a "letérdeltünk Jézus elé" feliratot. Áron/Sámuel chat-jelzés. (Sámuel független diagnózisa megerősítette: "reels-ként kell feltölteni, ha posztként töltitek, akkor levágja".)

## Hol operacionalizálva

- `02_Areas/Fókuszpont/Marketing/ChannelDNA/Fokuszpont-FB.md` §2 (INS-FP-FB-001/002/003)
- `02_Areas/Fókuszpont/Marketing/ChannelDNA/Fokuszpont-IG.md` §2 (INS-FP-IG-001)
- `01_Projects/Fókuszpont 2026 — Rövidvideók/scripts/VERZIOK_attekintes.md` — technikai megjegyzés (forgatókönyv-szintű safe-zone)

## Alkalmazhatóság más Area-kra

Bármely Meta-n (FB/IG) vertikális videót publikáló projekt: Navigátor Podcast (reel/short cross-post), Deák Húsüzlet, ExarLabs. A szabály platform-szintű igazság, nem projekt-specifikus.
