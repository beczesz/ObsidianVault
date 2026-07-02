---
title: "Feladat 1.5 (Bónusz): Új projekt legyártása a standard szerint"
date: 2026-07-02
author: Becze Szabolcs
status: active
description: "F1 otthoni bónusz: a résztvevő az AI-val legyártatja egy új, üres projekt teljes mappa-vázát (a 10 számozott mappa, projekt-CLAUDE.md sablon, README-k) a RegioConsult standard szerint, a két rendezett projekt mintájára, egyetlen prompttal. Az ismétlődő projekt-indítás automatizálása."
id: 9e60f135-7d04-4f85-8c59-3f4e2d6b5a17
index_schema_version: 1
bdos_index: true
tags: [ignis-academy, halado, regio-consult, f1, bonusz, scaffold]
---
# Feladat 1.5 (Bónusz): Új projekt legyártása a standard szerint

> **Típus:** otthoni gyakorlat · **Ismétlődő munka automatizálása**

## Cél
Minden új ügyfél-projektnél ugyanazt a standard mappa-vázat hozzátok létre kézzel. Ez percek, minden alkalommal. Az AI ezt egy prompttal megcsinálja, a két rendezett projekt (PAN, KER) mintájára.

## Feladat
```
A Internal_Standard.docx és a rendezett PAN/KER projektek mintája alapján hozz
létre egy ÚJ, üres projekt-mappát a RegioConsult/Projects/ alatt, ezzel a kóddal
és névvel: [KÓD]_[Projektnév].
Hozd létre mind a 10 számozott mappát, tedd bele minden mappába egy rövid
README.md-t (mi kerül ide), a 08_Dosare_de_achizitii-ba az 5 beszerzési
alkönyvtárat (DAC/DAP/DAD/DAL/DAF), és a projekt gyökerébe egy projekt-CLAUDE.md
sablont a kitöltendő helyekkel (beneficiar, tárgy, fázis). Ne másolj bele valós
adatot, csak a vázat.
```

## Elvárt eredmény
Egy kész, üres projekt-váz a standard szerint, indulásra kész. Amit eddig kézzel kattintgattál, most 30 másodperc, és garantáltan compliant lesz (az 1.1 audit zöld pipát adna rá).

## Továbbfejlesztés
Ha ezt gyakran csinálod, ez tökéletes **skill**-jelölt (lásd F5): egyszer leírod a projekt-scaffold logikát skillként, és onnantól egyetlen paranccsal hívod.

**Verzió:** 2.0 (Regio adaptáció)
