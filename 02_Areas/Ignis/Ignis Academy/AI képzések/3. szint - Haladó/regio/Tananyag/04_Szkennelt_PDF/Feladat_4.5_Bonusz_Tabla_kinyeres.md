---
title: "Feladat 4.5 (Bónusz): Egy konkrét tábla kinyerése + kontroll"
date: 2026-07-01
author: Becze Szabolcs
status: active
description: "F4 otthoni bónusz: a résztvevő egy szkennelt dokumentum EGY konkrét tábláját (pl. antemăsurătoare, deviz-részlet) nyeri ki tiszta, számolható Excel/md formába, és több kontroll-összeggel (soronkénti és végösszeg) validálja az OCR pontosságát."
id: 56e37d9e-9475-4d5a-8cba-0b2e9d4c8f6a
index_schema_version: 1
bdos_index: true
tags: [ignis-academy, halado, regio-consult, f4, bonusz, tabla]
---
# Feladat 4.5 (Bónusz): Egy konkrét tábla kinyerése + kontroll

> **Típus:** otthoni gyakorlat · **A pontosság mélyítése**

## Cél
Nem az egész dokumentum, csak egyetlen fontos tábla, de azt **fillérpontosan**.

## Feladat
Vegyél egy szkennelt oldalt egy tételes táblával (antemăsurătoare, deviz-részlet). Kérd:

```
Ezen az oldalon egy tételes tábla van. Olvasd ki pontosan, oszlophűen,
és add vissza számolható formában (md tábla vagy Excel). Ellenőrzés:
1. minden sorra: cantitate × preț = valoare (egyezik-e?),
2. az összes valoare összege = a feltüntetett végösszeg (egyezik-e?).
Ahol az ellenőrzés nem stimmel, jelöld meg a sort, mert ott OCR-hiba lehet.
```

## Elvárt eredmény
Egy validált tábla, ahol az AI maga jelzi, hol lehet félreolvasás (mert a soron belüli szorzat vagy a végösszeg nem jön ki). Ez a **kétszintű kontroll** a legjobb védelem az OCR-hiba ellen.

## Tanulás
A soronkénti (`cantitate × preț = valoare`) és a végösszeg-kontroll együtt szinte minden OCR-hibát elkap. Ezt építsd be reflexből minden számolós kiolvasásba.

**Verzió:** 1.0 (Regio adaptáció)
