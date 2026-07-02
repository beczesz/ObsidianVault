---
title: "Feladat 4.4 (Bónusz): Saját valós szkennelt PDF próbája"
date: 2026-07-01
author: Becze Szabolcs
status: active
description: "F4 otthoni bónusz: a résztvevő a saját valós szkennelt PDF-jén futtatja végig a triázs → OCR → kontroll-összeg folyamatot, egy anonimizált vagy ártalmatlan dokumentumon, és megtapasztalja hol pontos és hol hibázik az OCR a valós anyagán."
id: 45d26c8d-8364-4e4b-9baf-9a1d8c3b7f5e
index_schema_version: 1
bdos_index: true
tags: [ignis-academy, halado, regio-consult, f4, bonusz]
---
# Feladat 4.4 (Bónusz): Saját valós szkennelt PDF próbája

> **Típus:** otthoni gyakorlat · **Saját, valós (de óvatosan kezelt) anyagon**

## Cél
A workshopon a fiktív Napsugár-ajánlaton próbáltuk. Otthon nézd meg, hogy áll a te valós anyagoddal.

## Feladat
Válassz egy **nem érzékeny** vagy anonimizálható szkennelt PDF-et (pl. egy régi, lezárt projekt ajánlata), és futtasd rá ezt a promptot:

```
Itt egy PDF: [saját_fajl.pdf]

1) Mondd meg: vektoros (kinyerhető szövegréteg) vagy szkennelt (kép, OCR kell)?
   Mire alapozod?
2) Ha szkennelt, olvasd ki a benne lévő tételes táblát OCR-rel, oszlophűen
   (tétel, mennyiség, egységár, érték), és mentsd md-be.
3) Ellenőrzés: a tételek összege = a feltüntetett végösszeg? Ahol nem stimmel
   vagy bizonytalan az olvasat, jelöld meg, ne tippelj.
```

Nézd meg: stimmel a végösszeg? Hol jelzett bizonytalanságot?

## Elvárt eredmény
Reális kép arról, mennyire jó az OCR a **ti tényleges** dokumentumaitokon (minőség, tördelés, román szakszavak). Ez alapján tudod eldönteni, melyik dokumentum-típusnál érdemes rá építeni.

## Vigyázz
A beérkező állami / kivitelezői dokumentumok DNA-érzékenyek lehetnek (a kapcsolattartó is jelezte). Gyakorláshoz használj lezárt, anonim vagy saját anyagot, ne élő, harmadik féltől kapott bizalmas ajánlatot.

**Verzió:** 1.0 (Regio adaptáció)
