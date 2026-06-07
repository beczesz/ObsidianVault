---
schema: presto.campaign.v2
campaign_id: urnapja-2026
title: "Fókuszpont — Úrnapja 2026"
id: 1a51bd58-cdb3-4f60-ae8e-7f4a9d356272
index_schema_version: 1
bdos_index: true
description: "Fókuszpont Úrnapja 2026 esemény-promóciós kampány — trailer (publikálva 2026-05-25, FB/IG/TT/YT) + Meghívó v1 (2026-05-28, FB/IG/TT/YT). 4 csatornás, esemény-vezérelt."
seed_id: null

intents:
  - goal: announcement
    area: Fókuszpont
    notes: "Úrnapja 2026 esemény bejelentése és promóciója — trailer + meghívó"
  - goal: community
    area: Fókuszpont
    notes: "Erdélyi magyar keresztény közösség elérése és aktiválása az eseményre"

areas:
  - Fókuszpont
channels:
  - facebook
  - instagram
  - tiktok
  - youtube

publications:
  - publication_id: pub-facebook-2026-05-25-001
    area: Fókuszpont
    channel: facebook
    publication_status: published
  - publication_id: pub-instagram-2026-05-25-001
    area: Fókuszpont
    channel: instagram
    publication_status: published
  - publication_id: pub-tiktok-2026-05-25-001
    area: Fókuszpont
    channel: tiktok
    publication_status: published
  - publication_id: pub-youtube-2026-05-25-001
    area: Fókuszpont
    channel: youtube
    publication_status: published
  - publication_id: pub-facebook-2026-05-28-001
    area: Fókuszpont
    channel: facebook
    publication_status: published
  - publication_id: pub-instagram-2026-05-28-001
    area: Fókuszpont
    channel: instagram
    publication_status: published
  - publication_id: pub-tiktok-2026-05-28-001
    area: Fókuszpont
    channel: tiktok
    publication_status: published
  - publication_id: pub-youtube-2026-05-28-001
    area: Fókuszpont
    channel: youtube
    publication_status: published
  - publication_id: pub-facebook-2026-05-29-001
    area: Fókuszpont
    channel: facebook
    publication_status: scheduled
  - publication_id: pub-instagram-2026-05-29-001
    area: Fókuszpont
    channel: instagram
    publication_status: scheduled
  - publication_id: pub-tiktok-2026-05-29-001
    area: Fókuszpont
    channel: tiktok
    publication_status: scheduled
  - publication_id: pub-youtube-2026-05-29-001
    area: Fókuszpont
    channel: youtube
    publication_status: scheduled

stage: active
status: in_progress
start_date: 2026-05-25
target_end_date: 2026-06-03
event_date: 2026-06-03
event_location: "Székelyudvarhely, Márton Áron tér"
event_url: "https://www.facebook.com/events/2215942259153261/"
kpi_targets: {}
owner: Becze Szabolcs
tags: [fokuszpont, urnapja, 2026, event-promo]
---

## Brief

Az **Úrnapja 2026** Fókuszpont imaesemény köré épülő, négy csatornás (Facebook elsődleges, Instagram, TikTok, YouTube) promóciós kampány. Cél a közösségi elérés és az eseményre való meghívás — nem algoritmikus növekedés.

A kampány tartalom-hullámokból áll:
1. **Trailer** — előzetes, publikálva **2026-05-25** mind a 4 csatornán. ✅
2. **Meghívó v1** — hivatalos meghívó, publikálva **2026-05-28** mind a 4 csatornán. ✅
3. **Meghívó v2** — második meghívó, ütemezve **2026-05-29 (péntek)** mind a 4 csatornára. 🗓

## Esemény

- **Mit:** Fókuszpont imaest — „Minden szem Jézuson."
- **Mikor:** 2026. június 3.
- **Hol:** Székelyudvarhely, Márton Áron tér
- **Facebook esemény:** https://www.facebook.com/events/2215942259153261/

Referencia-caption a videókhoz (copy-paste): [`assets/caption-reference.md`](assets/caption-reference.md).

## Coordination notes

- Egységes narratíva mind a 4 csatornán; a formátum platform-natív (FB video, IG reel, TikTok rövidvideó, YouTube videó).
- Esemény pontos dátuma TBD — a `target_end_date` az esemény napjára frissítendő, amint megvan.
- Brand-tone és vizuál: lásd [`../../MARKETING_ENGINE.md`](../../MARKETING_ENGINE.md).

## Results summary

(a kampány lezárásakor — per-publication analytics linkekkel)

## Iteration history

- 2026-05-28 — created by presto (plan mód) — engine bootstrap + kampány-esernyő + 8 publication felvitele a boardra. Trailer 4 csatornán published (2026-05-25), Meghívó v1 4 csatornán scheduled (2026-05-28).
- 2026-05-28 — esemény-adatok rögzítve (presto): dátum 2026-06-03, helyszín Székelyudvarhely / Márton Áron tér, FB esemény-link. Referencia-caption létrehozva (`assets/caption-reference.md`).
- 2026-05-28 — Meghívó v1 mind a 4 csatornán publikálva (manual) → status scheduled→published. Meghívó v2 beütemezve 2026-05-29-re (péntek) mind a 4 csatornára (pub-{facebook,instagram,tiktok,youtube}-2026-05-29-001).
