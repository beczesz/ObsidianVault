---
title: "Feladat 1.7 (Bónusz): Kuka-ellenőrzés (bízz benne, de ellenőrizd)"
date: 2026-07-02
author: Becze Szabolcs
status: active
description: "F1 otthoni bónusz: a résztvevő átnézeti az AI-val az 1.2 rendrakásban Kukába tett fájlokat, és minden tételre eldönteti, tényleg szemét-e, vagy esetleg fontos dokumentum, ami véletlenül került oda. A cél a bízz benne, de ellenőrizd elv gyakorlása: az AI dönt, de a végső szót az ember mondja ki, kiemelten a kétértelmű esetekben (pl. egy önéletrajz, ami pályázati melléklet is lehet)."
id: b2c4e6f8-0a1b-4c3d-8e5f-6a7b8c9d0e1f
index_schema_version: 1
bdos_index: true
tags: [ignis-academy, halado, regio-consult, f1, bonusz, kuka, ellenorzes]
---
# Feladat 1.7 (Bónusz): Kuka-ellenőrzés

> **Típus:** otthoni gyakorlat · **A bízz benne, de ellenőrizd elv**

## Cél
Az 1.2 rendrakásban az AI szemétnek jelölt fájlokat a Kukába tette. De az AI is dönt, és néha téved. Nézzük át a Kukát: nem került-e véletlenül fontos fájl oda?

## Feladat
```
Nézd át a THR_Napsugar_Tejuzem/Kuka mappát tételről tételre. Minden fájlra mondd
meg: tényleg szemét / oda nem illő, vagy esetleg fontos, és véletlenül került ide?
Ha valamiről úgy ítéled, hogy mégis fontos lehet (pl. egy dokumentum, ami
pályázati melléklet is lehet, mint egy önéletrajz vagy egy szerződés), jelezd,
és javasold, hova tenném a standard szerint.
NE mozgass semmit, csak adj egy javaslat-listát: fájl -> szemét marad / vissza a
projektbe (hova).
```

## Elvárt eredmény
Egy tiszta lista: mi maradhat a Kukában (recept, nyaralás, bevásárlólista, temp, duplikátumok), és van-e olyan, ami inkább vissza a projektbe. Kiemelten érdekes a kétértelmű eset, pl. az **önéletrajz**: az EU-pályázatokban a csapattagok CV-je gyakran kötelező melléklet, tehát lehet, hogy nem szemét, hanem a `01_Cerere_de_finantare`-ba való. Itt te döntesz.

## Tanulás
A destruktív döntéseket (mi a szemét) mindig érdemes visszaellenőrizni. Az AI gyors és következetes, de a **kontextus-függő ítéletet** (egy CV szemét vagy melléklet?) az ember hozza meg. Ezért nem törlünk, csak Kukázunk: a Kuka visszafordítható, a törlés nem.

**Verzió:** 2.0 (Regio adaptáció)
