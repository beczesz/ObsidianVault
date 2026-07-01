---
title: "Feladat 4.4 (Bónusz): Mennyiségi audit a kiírás ellen"
date: 2026-07-01
author: Becze Szabolcs
status: active
description: "F4 otthoni bónusz: a résztvevő az AI-val ellenőrizteti, hogy a kivitelező ajánlatában szereplő mennyiségek (m3 beton, tonna acél, mp) megegyeznek-e a kiírás/antemăsurătoare mennyiségeivel, tételről tételre, és eltérés-listát kap. A meetingen említett konkrét fájdalom (a betonmennyiség nem stimmelt) kezelése."
id: 1c49d1f4-5031-4e9f-8c6a-6b8d4e0c9f7a
index_schema_version: 1
bdos_index: true
tags: [ignis-academy, halado, regio-consult, f4, bonusz, mennyiseg]
---
# Feladat 4.4 (Bónusz): Mennyiségi audit a kiírás ellen

> **Típus:** gyakorolható a mellékelt asseteken, majd otthon a saját anyagon · **A meetingen említett konkrét fájdalom**

## Cél
Nem az árat, hanem a **mennyiségeket** ellenőrizzük: a kiírás mennyisége és az ajánlat mennyisége stimmel-e? A meetingen pont ez volt a példa: „a betonmennyiség nem stimmelt".

## Az assetek (ehhez a feladathoz)
- `antemasuratoare_kiiras_Napsugar.xlsx`: a **kiírás** mennyiség-listája (UM + Cantitate cerută), tételenként.
- A kivitelező ajánlata (az F3-ban OCR-rel kinyert `Pelda_output/oferta_OCR.md`, ami tartalmazza az ajánlat mennyiségeit).

## Feladat
```
Két forrásom van: az antemasuratoare_kiiras_Napsugar.xlsx (a KIÍRÁS mennyiségei)
és a kivitelező ajánlata (oferta_OCR.md, az AJÁNLAT mennyiségei).

Vesd össze őket tételről tételre, DE csak a MENNYISÉGRE (UM + cantitate) figyelj,
ne az árra. Ahol a mennyiség eltér, emeld ki: tétel, kiírás-mennyiség,
ajánlat-mennyiség, különbség. A többit ne listázd, csak az eltéréseket.
```

## Elvárt eredmény (megoldókulcs)
Egyetlen eltérés bukik ki: a **beton (Beton armat fundații și structură)**: a kiírás **820 mc**-t kér, az ajánlat **800 mc**-t tartalmaz, azaz **−20 mc hiány**. A többi 11 tétel mennyisége egyezik. Pontosan ez az a fajta hiba, amit a meetingen említettek, és amit egy 200 tételes ajánlatban kézzel könnyű átugrani.

## Otthoni kiterjesztés
Futtasd le ugyanezt a saját (lezárt, anonim) kiírás-ajánlat páron: az AI a mennyiségeket is percek alatt egyezteti.

## Tanulás
A mennyiségi és az ár-összevetés két külön kérdés. Külön futtatva mindkettő tisztább eredményt ad, mint egyben. Az „csak az eltéréseket mutasd" szűkítés a hosszú listáknál aranyat ér.

**Verzió:** 1.0 (Regio adaptáció)
