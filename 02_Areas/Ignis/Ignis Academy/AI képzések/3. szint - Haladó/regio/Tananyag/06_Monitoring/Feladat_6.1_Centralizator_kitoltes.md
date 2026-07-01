---
title: "Feladat 6.1: SL bevezetése a Centralizatorba (STÁCIÓ)"
date: 2026-07-01
author: Becze Szabolcs
status: active
description: "F6 stáció: a résztvevők bevezetik az első situație de lucrări-t (SL1, kb. 610 000 lej) a monitoring Centralizatorba, a Valoare contract oszlop az ajánlatból (5 375 000 lej), és a Rest de executat automatikusan frissül. A kivitelezés-követés automatizálása, csak a szürke cellákba írva."
id: b6e21b9e-5031-4f29-8aa4-6f8b4c0d3e2f
index_schema_version: 1
bdos_index: true
tags: [ignis-academy, halado, regio-consult, f6, feladat, station]
---
# Feladat 6.1: SL bevezetése a Centralizatorba (STÁCIÓ)

> **Típus:** ⏸ STÁCIÓ · **Idő:** ~12 perc

---

## Szituáció

A Napsugár kivitelezése elindult. Megjött az első situație de lucrări (SL1): a kivitelező igazolja, mennyit teljesített eddig, kb. 610 000 lej értékben. Ezt be kell vezetni a **Centralizatorba**, ami a szerződés-értékhez (az F4-ből ismert ajánlat, 5 375 000 lej) méri a megvalósulást, és mutatja a `Rest de executat`-ot (mennyi van hátra). Ma ezt kézzel vezetitek, minden SL-nél.

---

## A stáció prompt

Nyisd meg a `06_monitorizare_Centralizator_URES.xlsx`-et a Cowork Excel-pluginnal:

```
Ez egy monitoring Centralizator. A Valoare contract oszlopba az ajánlat
tételei kerülnek (a kivitelezői ajánlat, összesen 5 375 000 lei fără TVA).
Vezesd be az első situație de lucrări-t (SL1) az SL1 oszlopba: a teljesített
tételek, összesen kb. 610 000 lei. A Rest de executat oszlop automatikusan
számolódik (contract mínusz a teljesített SL-ek). Csak a szürke input-cellákba
írj, a képleteseket ne bántsd. A végén mondd meg az összes teljesített értéket
és a teljes Rest de executat-ot.
```

---

## Elvárt eredmény

A Centralizator (vö. `07_...KITOLTOTT`): a Valoare contract oszlop kitöltve az ajánlatból, az SL1 bevezetve, és a `Rest de executat` automatikusan mutatja a maradványt. Kontroll: a contract összege = 5 375 000, az SL1 összege ~610 000, a maradvány a kettő különbsége.

---

## Miért ez a stáció

A monitoring a pályázati életciklus egyik legismétlődőbb, leghosszabb kézi munkája: minden SL-nél végigvezetni a tételeket, számolni a maradványt, több projekten át. Pont az a fajta feladat, amit egyszer megérteni és utána gépiesíteni érdemes, mert **sokszor jön vissza**. Csak a szürke cellákba írsz, a képletek dolgoznak (mint a devizben).

---

## Tanulás

A repetitív Excel-kitöltés (statisztika, monitoring, frissítés) az AI egyik legerősebb terepe: nem fárad, nem téveszt sort, és a képletek maguktól aggregálnak. Ha ez a Centralizator egy skillbe kerül (F5-tanulság), az összes jövőbeli SL bevezetése egyetlen hívás lesz.

## Otthoni elmélyítés
- `Feladat_6.3_Bonusz_Tobb_SL.md`, több SL halmozott követése
- `Feladat_6.5_Bonusz_Szamla_orakbol.md`, számla ledolgozott órákból

**Verzió:** 1.0 (Regio adaptáció)
