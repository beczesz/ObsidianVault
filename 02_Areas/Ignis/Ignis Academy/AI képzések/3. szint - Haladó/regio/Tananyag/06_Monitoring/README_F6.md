---
title: "F6: Monitoring: Centralizator + dokumentum-generálás"
date: 2026-07-01
author: Becze Szabolcs
status: active
description: "Az F6 modul zárja a láncot: a kivitelezés követése egy monitoring Centralizatorban (a szerződéshez mérve, situații de lucrări SL1/SL2/SL3 + Rest de executat), majd egy dokumentum generálása a saját sztenderdben (pl. számla ledolgozott órákból vagy egy monitorizare-jegyzet). Résztvevői stáció a Centralizator-kitöltésre + oktatói demó a dokumentum-generálásra."
id: a5d10a8d-4920-4e18-9ff3-5e7a3b9c2d1e
index_schema_version: 1
bdos_index: true
tags: [ignis-academy, halado, regio-consult, f6, monitoring, centralizator]
---
# F6: Monitoring: Centralizator + dokumentum-generálás
**Időkeret:** 25 perc · **Fázis a workshopban:** 6/6

## Modell

⏸ **1 stáció** + 🎤 **1 DEMO**.

| # | Fájl | Típus | Idő |
|---|---|---|---|
| **6.1** | `Feladat_6.1_Centralizator_kitoltes.md` | ⏸ STÁCIÓ (SL bevezetése) | ~12p |
| **6.2** | `Feladat_6.2_Dokumentum_generalas.md` | 🎤 OKTATÓI DEMO (számla / jegyzet a sztenderdben) | ~10p |

## Narratív összefoglaló

A pályázati életciklus utolsó, monitoring fázisa. A kivitelezés zajlik, jönnek a situații de lucrări (SL, részteljesítési igazolások). Ezeket be kell vezetni a **Centralizatorba**, a szerződéshez mérve, hogy lásd: mennyi valósult meg, mennyi a `Rest de executat`. A meetingen ez volt az egyik legnagyobb, kézzel végzett fájdalom: „ez volt az eredeti költségvetés, ezek a szerződések, eddig ennyit kértem, ennyit fizettek".

A stáció: a résztvevő bevezeti az SL1-et a Centralizatorba (a szerződés az F4-ből ismert 5 375 000 lej ajánlat, az SL1 kb. 610 000 lej), és a `Rest de executat` automatikusan frissül. A demó: az AI generál egy dokumentumot a **saját sztenderdetekben** (pl. számla ledolgozott órákból, vagy egy rövid monitorizare-jegyzet), Verdana 9-cel, ahogy a belső szabály előírja.

## Tanulási célok
1. **Ismétlődő Excel-kitöltés**, az SL bevezetése a Centralizatorba, a képletek követik.
2. **Contract → megvalósulás követése**, mennyi valósult meg, mennyi a maradvány.
3. **Dokumentum-generálás a sztenderdben**, a kimenő dokumentum a belső formátumot (Verdana 9) követi.
4. **A teljes lánc lezárása**, szkennelt ajánlat → OCR → összevetés → deviz → monitoring, egy összefüggő projekten.

## Otthoni bónuszok

| # | Bónusz | Output |
|---|---|---|
| 6.3 | `Feladat_6.3_Bonusz_Tobb_SL.md` | Több SL bevezetése + halmozott követés |
| 6.4 | `Feladat_6.4_Bonusz_Progres_raport.md` | Monitorizare progres-riport generálása |
| 6.5 | `Feladat_6.5_Bonusz_Szamla_orakbol.md` | Számla generálása ledolgozott órákból |
| 6.6 | `Feladat_6.6_Bonusz_Palyazat_vazlat.md` | Pályázat-vázlat a kiírásból (a 3. fájdalom könnyű érintése) |

## Átmenet a zárásba

*„Innen indultunk: egy strukturált rendszer és három napi fájdalom. Ide értünk: az AI érti a struktúrádat, kiolvas, összevet, kitölt, követ, és generál, mindezt a te sztenderdedben. A kérdés már nem az, hogy mit csinál az AI, hanem hogy mit csinálsz vele te."* (Lásd: `../ZARAS.md`.)

## Asset-ek
- `06_monitorizare_Centralizator_URES.xlsx`, üres monitoring-tábla (Valoare contract + SL1-3 + Rest, képletekkel).
- `07_monitorizare_Centralizator_KITOLTOTT.xlsx`, kitöltött megoldókulcs (contract az ajánlatból + SL1 minta).

**Verzió:** 1.0 (Regio adaptáció)
