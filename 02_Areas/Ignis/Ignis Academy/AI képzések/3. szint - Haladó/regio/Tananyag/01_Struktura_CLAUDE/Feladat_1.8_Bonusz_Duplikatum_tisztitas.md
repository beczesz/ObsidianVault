---
title: "Feladat 1.8 (Bónusz): Duplikátum- és verzió-tisztítás az egész workspace-en"
date: 2026-07-02
author: Becze Szabolcs
status: active
description: "F1 otthoni bónusz: a résztvevő az AI-val átsöpörteti mind a három RegioConsult projektet duplikátumok és elavult verziók után (Copy of..., NE HASZNALD, regi, két hasonló nevű fájl egymás mellett), és kap egy konszolidációs javaslatot: melyik az aktuális, melyik a felesleges és miért. Az AI nem töröl, csak javasol."
id: c3d5e7f9-1b2c-4d6e-8f0a-3b5c7d9e1f2a
index_schema_version: 1
bdos_index: true
tags: [ignis-academy, halado, regio-consult, f1, bonusz, duplikatum, verzio]
---
# Feladat 1.8 (Bónusz): Duplikátum- és verzió-tisztítás

> **Típus:** otthoni gyakorlat · **Áttekintés több projekt fölött**

## Cél
Amikor 3 iroda, 21 ember dolgozik ugyanabban a rendszerben, könnyen keletkeznek duplikátumok és régi verziók (`Copy of...`, `... NE HASZNALD`, `... regi`, két hasonló fájl egymás mellett). Ezek zavarják a tisztánlátást és hibához vezetnek (rossz verzióval dolgozik valaki). Söpörjük át az egészet.

## Feladat
```
Söpörd át mind a három projektet (Projects/ alatt) duplikátumok és elavult
verziók után: pl. "Copy of ...", "... NE HASZNALD", "... regi", vagy két hasonló
nevű fájl egymás mellett ugyanabban a mappában.

Minden találatra mondd meg: melyik az aktuális/megtartandó, melyik a felesleges,
és miből gondolod (dátum, tartalom, elnevezés). Adj egy tiszta konszolidációs
javaslatot, de ne törölj és ne mozgass semmit magadtól.
```

## Elvárt eredmény
Egy konszolidációs lista: minden duplikátum-párnál melyik marad, melyik mehet a Kukába, és miért (pl. a `deviz regi 2019 NE HASZNALD` a régi, a `deviz general` az aktuális). A tiszta rendszerben minden dokumentumból egyetlen, egyértelmű aktuális verzió van.

## Tanulás
A duplikátum a merev rendszer csendes ellensége: ha két verzió van, valaki előbb-utóbb a rosszal dolgozik. Az AI gyorsan felszínre hozza őket, de a **döntést** (melyik az aktuális) az ember hozza meg, tartalom és dátum alapján. Ez pont az a repetitív, hibázós munka, amit érdemes rendszeresen, AI-jal átfuttatni.

**Verzió:** 2.0 (Regio adaptáció)
