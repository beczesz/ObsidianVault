---
title: "Feladat 4.1: Formátum-triázs: vektoros vagy szkennelt? (STÁCIÓ)"
date: 2026-07-01
author: Becze Szabolcs
status: active
description: "F4 stáció: a résztvevők megtanulják eldönteni, hogy egy PDF vektoros (kinyerhető szöveg) vagy szkennelt (kép, OCR kell), és megkérdezni az AI-tól, hogy melyikkel van dolguk. Ez az első lépés minden dokumentum-feldolgozásnál: a triázs dönti el, mennyire lesz könnyű vagy drága."
id: 12af395a-503b-4c18-9e7c-6d8a5f0e4d2b
index_schema_version: 1
bdos_index: true
tags: [ignis-academy, halado, regio-consult, f4, feladat, triazs]
---
# Feladat 4.1: Formátum-triázs: vektoros vagy szkennelt? (STÁCIÓ)

> **Típus:** ⏸ STÁCIÓ · **Idő:** ~7 perc

---

## Szituáció

Mielőtt bármit kezdenél egy PDF-fel, egy kérdést kell feltenned: **kép vagy szöveg?** Ez dönti el az egész út nehézségét.

- **Vektoros PDF:** a szöveg mint szöveg van benne. Kimásolható, kereshető, gyorsan és olcsón kinyerhető. 300 oldal is vihető.
- **Szkennelt / kép PDF:** a szöveg valójában egy fénykép a papírról. Nincs szövegréteg. Csak OCR-rel (optikai karakterfelismerés) nyerhető ki, ami lassabb, drágább és hibázhat.

A kettő ránézésre egyforma lehet. A trükk: a vektorosban ki tudod jelölni a szöveget egérrel; a szkenneltben nem (a jelölés az egész oldalt fogja meg mint egy képet).

---

## A stáció prompt

Két fájl van a mappában: `oferta_szkennelt_Napsugar.pdf` és a projektben egy vektoros deviz Excel. Kérdezd meg az AI-t:

```
Nézd meg ezt a fájlt: oferta_szkennelt_Napsugar.pdf

Mondd meg: ez vektoros (kinyerhető szövegréteggel) vagy szkennelt (kép-only)
PDF? Mire alapozod? Ha szkennelt, mit jelent ez arra nézve, hogy milyen
gyorsan és milyen megbízhatóan tudod belőle kinyerni a tételes adatokat?
```

---

## Elvárt eredmény

Az AI megállapítja, hogy a `oferta_szkennelt_Napsugar.pdf` **kép-only** (nincs szövegréteg), és elmagyarázza, hogy ezért OCR kell, ami hibázhat, ezért kontrollra szorul. Ha egy vektoros fájlt is megnézetsz vele, látod a kontrasztot: azt azonnal, pontosan olvassa.

---

## Miért ez a stáció

A ti napi valóságotokban a **legdrágább hiba** azzal kezdődik, hogy valaki egy 300 MB-os szkennelt szörnyet próbál egyben az AI-ra bízni, majd csalódik. A triázs 10 másodperc, és megmondja előre: ez az út könnyű lesz (vektoros), vagy nehéz és ellenőrzést igényel (szkennelt). A profi nem a feldolgozással kezd, hanem a triázzsal.

---

## Tanulás

Nem minden PDF egyenlő. A **formátum** dönti el a feladat nehézségét, nem az oldalszám. Egy 300 oldalas vektoros könnyebb, mint egy 5 oldalas rossz minőségű szken. Ezt a különbséget megtanulni önmagában megspórol sok elpazarolt órát.

## Otthoni elmélyítés
- `Feladat_4.4_Bonusz_Sajat_PDF.md`, a saját valós PDF-jeid triázsa

**Verzió:** 1.0 (Regio adaptáció)
