---
title: "(Bónusz) Feladat 6.5 — Social media kampány-csomag"
date: 2026-05-14
author: Becze Szabolcs
status: active
description: "Egy 30 napos társadalmi média kampány tervezési feladat a TransOffice zöld átállásához, amely tartalmi naptárt, platformspecifikus mintaposztokat, vizuális koncepciókat, sajtóközleményeket és hashtag-stratégiát igényel a Cowork AI segítségével."
description_source: auto
description_hash: db327f78ebeb6385
id: c9c575cc-6e27-44ab-8603-d9f024361683
index_schema_version: 1
bdos_index: true
---
# (Bónusz) Feladat 6.5 — Social media kampány-csomag

## Szituáció

Az új weboldal és a zöld átállás **megérdemli a közlést**. De a legtöbb kis cég itt akad el: **„nincs időm Facebook-posztokat írni"**, „nem tudok grafikát készíteni", „melyik platformon mit?".

A Cowork **teljes social media csomagot** generál — szövegeket, képi koncepciókat, ütemezést — egyetlen promptban.

## Feladat

Készítsd elő a TransOffice 30-napos **„Zöld átállás" social kampányát** a Cowork-kel.

### Javasolt prompt:

> "Készíts egy **30-napos social media kampánytervet** a TransOffice 'Zöld átállás' projektjéhez. A kampány célja: hírverés a regionális közösségben + B2B ügyfélbizalom + álláshirdetés-támogatás.
>
> **Platformok:** Facebook (fő), Instagram (vizuális), LinkedIn (B2B), TikTok (Gen Z / fiatal sofőr-jelöltek).
>
> **Generálj nekem:**
>
> 1. **Tartalmi naptár** — Excel-szerű táblázat: Dátum | Platform | Poszt típus | Headline | Body | CTA | Vizuális koncepció
>
> 2. **8 minta-poszt** teljes szöveggel (2 db / platform):
>    - Facebook: hosszabb, történet-mesélő
>    - Instagram: rövid, érzelmes, hashtag-ekkel
>    - LinkedIn: szakmai, számokkal
>    - TikTok: rövid, hook-első, fiatalos
>
> 3. **5 vizuális koncepció leírás** (mintha grafikus tervezné):
>    - 'Hős' jármű-fotó koncepció
>    - 'Csapat' fotó koncepció
>    - Infografika a CO2 csökkenésről
>    - Behind-the-scenes idővonal-grafika
>    - Idézet-grafika ('Márton: ...')
>
> 4. **3 sajtóközlemény változat** (rövid, közepes, hosszú)
>
> 5. **Hashtag stratégia** — 10 általános + 5 specifikus hashtag
>
> Hangnem: **büszke, közösségi, hiteles**. Nyelv: **magyar + román kétnyelvű minta-posztokkal**."

## Elvárt kimenet

Egy `social_kampany_zold_atallas/` mappa:

- `tartalmi_naptar.md` — 30 napos táblázat
- `posztok/` — 8 db .md fájl (post_01_facebook.md, etc.)
- `vizualis_koncepciok.md` — 5 koncepció leírás
- `sajtokozlemeny_rovid.md`, `_kozepes.md`, `_hosszu.md`
- `hashtag_strategia.md`

## Extra kihívás

Két második prompt:

> "A 8 minta-poszt közül melyik **3 a legmegkapóbb** és miért? Adj egy rangsorot ezekhez a kritériumokhoz: érzelmi rezonancia, megosztásra inspiráló, márkaérték-építés."

És:
> "Mi az a **3 közönségi csoport** akiket kifejezetten nem szólítunk meg a kampánnyal de talán kellene? Készíts egy gyorsteszt: ha ezt a kampányt látom mint [helyi anyuka / 50+ vásárló / városi értelmiségi] mit éreznék?"

## Tipp

A 30-napos terv ne **mind az 30 napra előre legyen kőbe vésve** — 60% legyen rögzített, 40% rugalmas. Mindig hagyj helyet **valós eseményekre reagálásra** (pl. a pályázati nyertesi értesítés napján egy reaktív poszt).

A Cowork ezt **havonta újrafuthatja** — minden hónapban új trendekkel, új eseményekkel.

## Tanulás

- A social media **rendszer, nem dühroham** — egy 30-napos terv 80%-ban automatizálható
- A Cowork **nemcsak posztokat ír — vizuális koncepciókat is**, amit egy grafikusnak/dizájnernek mehet brief-ként
- A **kétnyelvű (HU+RO) anyag** kétszerez a célközönséget — kicsi extra munka, dupla hatás
- A "ki kit nem szólítok meg" extra-kihívás → **kritikai gondolkodás** a marketing-jelenléten
- Ez a feladat **újraindítható havonta** — egy folyamatos kampány-pipeline alapja
