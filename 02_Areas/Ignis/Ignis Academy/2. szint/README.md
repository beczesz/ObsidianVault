---
title: "2. szint — Haladó (Műhely) tananyag"
date: 2026-06-03
author: Becze Szabolcs
status: active
description: "Az Ignis Academy AI Kompetencia Program 2. szintjének (Haladó, kódnév Műhely) teljes anyaga: a 4 órás élő, hands-on workshop tananyaga, a TransOffice Trade SRL narratíva adatkészletei (több dry-run verzió), a pozicionálás és a marketing. A korábbi 02_Areas/Ignis/AI Course HBC mappából áthelyezve, 2026-06-03."
id: 426fbba7-6146-49ed-ad91-a569bdf5a3e9
index_schema_version: 1
bdos_index: true
tags: [ignis-academy, kepzes, halado, muhely, 2-szint, tananyag, workshop]
---

# 2. szint — Haladó (Műhely)

> Az **AI Kompetencia Program 2. szintjének** (a weboldalon **Haladó**, a Catalog-ban **Műhely** kódnéven) teljes anyaga. A korábbi `02_Areas/Ignis/AI Course HBC/` mappa **áthelyezve** ide, 2026-06-03.

## Mi ez

Egy **4 órás élő, vezetett, hands-on workshop** („Narrated Live Experience"): a résztvevő egy fiktív erdélyi cég (**TransOffice Trade SRL**) Operations Managereként 6 fázison át jut a 27 kaotikus fájltól egy beadható, 23-mellékletes EU pályázatig, **Claude Cowork + Obsidian + Markdown** segítségével.

Tagline: *„4 óra. 1 fiktív cég. Egy igazi EU pályázat. AI-val."*

## Mappastruktúra

| Mappa | Tartalom |
|---|---|
| **`Haladó/Tananyag/`** | A workshop **curriculuma** (00_Bevezetes … 06_Marketing_Honlap + TransOffice), v2.0, 180+ asset. |
| **`Haladó/Műhely/`** | A workshop **terve és narratívája**: `00_Tervezes/` (Story Book, fázis-tervek, versenytárs-elemzés), fázis-mappák (02–06). |
| **`Haladó/` TransOffice-verziók** | A fiktív cég adatkészletének **dry-run iterációi** (lásd alább a tisztítandó listát). |
| **`Pozicionalas/`** | Pozicionálás és üzenet-architektúra: PRODUCT.md, DESIGN.md, brand-brief, MESSAGING, ernyő-hierarchia. |
| **`Marketing/`** | Marketing anyagok. |

## Hivatkozott helyek

- **Catalog-metaadat (marketing):** [`../Catalog/muhely/COURSE.md`](../Catalog/muhely/COURSE.md)
- **Weboldal-megfelelő:** az `ignis.academy` Haladó képzése (2. szint, 500 RON, Jún 26).
- A vault-on belüli hivatkozások (Catalog, ExarLabs events, dashboards, microsites) **frissítve** az új útvonalra (2026-06-03).

## Áthelyezési napló (2026-06-03)

- A teljes `02_Areas/Ignis/AI Course HBC/` mappa (627 fájl, ~79 MB) **áthelyezve** ide (mv, nem másolás), a belső struktúra megőrzésével.
- A vault 9 hivatkozó fájlja frissítve a régi `…/AI Course HBC/…` útról az új `…/Ignis Academy/2. szint/…` útra.

## ⚠️ Tisztítandó (verzió-burjánzás, NEM töröltem)

A mappa több historikus verziót tartalmaz; **nem dedupláltam**, mert nem egyértelmű melyik a kanonikus. Döntésedre vár:

- **6 TransOffice adatkészlet-verzió:** `TransOfficeCopy/`, `TransOfficeCopy_v3/`, `TransOfficeCopy_v4/`, `TransOfficeDryRun2.0/`, `TransOffice_LIVE/`, `dryrun3/`. Valószínűleg a `TransOffice_LIVE/` és/vagy `dryrun3/` a legfrissebb; a többi régi dry-run.
- **7 db `Tananyag_Halado(ó)_v*.zip`** a `Haladó/` gyökerében (v1.0–v2.0, kétféle írásmóddal — duplikátumok).
- **`Haladó/zivTuib0`** — ideiglenes/szemét fájl, törölhető.

> Ha megmondod melyik TransOffice-verzió a kanonikus, és hogy a ZIP-ek kellenek-e, elvégzem a deduplikálást egy következő körben.
