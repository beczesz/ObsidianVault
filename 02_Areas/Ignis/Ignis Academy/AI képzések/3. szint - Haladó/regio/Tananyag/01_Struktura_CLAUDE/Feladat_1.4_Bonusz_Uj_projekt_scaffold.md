---
title: "Feladat 1.4 (Bónusz): Új projekt-mappa legyártása a sztenderd szerint"
date: 2026-07-01
author: Becze Szabolcs
status: active
description: "F1 otthoni bónusz: a résztvevő az AI-val legyártatja egy új, üres projekt teljes mappa-vázát (a 10 számozott mappa, projekt-CLAUDE.md, üres helyőrzőkkel) a Regio sztenderd szerint, egyetlen prompttal. Az ismétlődő projekt-indítás automatizálása."
id: 8d5f0e24-6c93-4e74-9b48-2f3e1d5c4a06
index_schema_version: 1
bdos_index: true
tags: [ignis-academy, halado, regio-consult, f1, bonusz, scaffold]
---
# Feladat 1.4 (Bónusz): Új projekt-mappa legyártása a sztenderd szerint

> **Típus:** otthoni gyakorlat · **Ismétlődő munka automatizálása**

## Cél
Minden új ügyfél-projektnél ugyanazt a strukturált mappa-vázat hozzátok létre kézzel. Ez percek, minden alkalommal. Az AI ezt egy prompttal megcsinálja.

## Feladat
A gyökér-CLAUDE.md már leírja a sztenderd struktúrát. Kérd meg az AI-t:

```
A CLAUDE.md-ben leírt sztenderd struktúra alapján hozz létre egy ÚJ, üres
projekt-mappát ezzel a kóddal és névvel: [KÓD]_[Projektnév].
Hozd létre mind a 10 számozott almappát, tedd bele minden mappába egy rövid
README.md-t (mi kerül ide), és a projekt gyökerébe egy projekt-szintű
CLAUDE.md sablont a kitöltendő helyekkel (beneficiar, tárgy, fázis).
Ne másolj bele valós adatot, csak a vázat.
```

## Elvárt eredmény
Egy kész, üres projekt-váz a sztenderd szerint, indulásra kész. Amit eddig kézzel kattintgattál, most 30 másodperc.

## Továbbfejlesztés
Ha ezt gyakran csinálod, ez egy tökéletes **skill**-jelölt (lásd F5): egyszer leírod a projekt-scaffold logikát skillként, és onnantól egyetlen paranccsal hívod.

**Verzió:** 1.0 (Regio adaptáció)
