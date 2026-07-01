---
title: "Feladat 6.3 (Bónusz): Több SL halmozott követése"
date: 2026-07-01
author: Becze Szabolcs
status: active
description: "F6 otthoni bónusz: a résztvevő több situație de lucrări-t (SL1, SL2, SL3) vezet be a Centralizatorba, és követi a halmozott teljesítést, a Rest de executat csökkenését, illetve azt, ha egy SL túllépné a szerződéses tételt (figyelmeztetés)."
id: d8043db1-7253-4b4f-8cc6-8d0e6f2a5b4c
index_schema_version: 1
bdos_index: true
tags: [ignis-academy, halado, regio-consult, f6, bonusz]
---
# Feladat 6.3 (Bónusz): Több SL halmozott követése

> **Típus:** otthoni gyakorlat · **A monitoring valós ritmusa**

## Cél
A valóságban több SL érkezik egymás után. A Centralizatornak halmoznia kell, és jeleznie, ha valami kilóg.

## Feladat
Az F6-ban bevezetett SL1 után:

```
Vezess be még két situație de lucrări-t a Centralizatorba (SL2 és SL3,
tetszőleges reális értékekkel). Számold a halmozott teljesítést és a
Rest de executat-ot minden lépés után. Ha egy tétel halmozott teljesítése
meghaladná a szerződéses értékét, azt EMELD KI, mert az hibát vagy
túlszámlázást jelezhet. Csak a szürke cellákba írj.
```

## Elvárt eredmény
Egy élő, halmozott monitoring-nézet, ami nemcsak összead, hanem **figyelmeztet** a túllépésre. Ez a fajta beépített kontroll az, ami kézzel könnyen kimarad.

## Tanulás
A jó monitoring nem passzív táblázat, hanem **aktív őr**: jelez, ha valami nem stimmel. Az AI ezt a logikát is beleteszi, ha kéred.

**Verzió:** 1.0 (Regio adaptáció)
