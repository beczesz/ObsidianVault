---
title: "Feladat 3.2: OCR élőben: szkennelt ajánlat → md tábla (DEMO)"
date: 2026-07-01
author: Becze Szabolcs
status: active
description: "F3 oktatói demó: a szkennelt (kép-only) Napsugár-ajánlatból az AI OCR-rel gépi-olvasható, tételes markdown táblát nyer ki, és rögtön kontroll-összeggel ellenőrzi. A demó őszinte: bemutatja, hol pontos és hol hibázhat az OCR, és miért kell mindig ellenőrizni."
id: 23b04a6b-6142-4d29-8f8d-7e9b6a1f5e3c
index_schema_version: 1
bdos_index: true
tags: [ignis-academy, halado, regio-consult, f3, feladat, demo, ocr]
---
# Feladat 3.2: OCR élőben: szkennelt ajánlat → md tábla (DEMO)

> **Típus:** 🎤 OKTATÓI DEMO · **Idő:** ~12 perc

---

## Szituáció

A triázs kimondta: a `oferta_szkennelt_Napsugar.pdf` kép-only. Most jön a valódi kérdés: mit tudunk belőle mégis kinyerni? Ez a fájl a fiktív kivitelező ajánlata a Napsugár-beruházásra, tételekkel (beton, finisaje, instalatii, utilaje, dotari), objektumonként.

---

## A demó menete

### 1. lépés: Az AI OCR-rel kiolvassa

Az oktató bemásolja:

```
A oferta_szkennelt_Napsugar.pdf egy szkennelt, kép-only ajánlat a kivitelezőtől.
Olvasd ki OCR-rel a tételes tartalmat, és add vissza egy strukturált markdown
táblában, ezekkel az oszlopokkal: Nr, Obiect, Categorie, Denumire, UM, Cantitate,
Preț unitar, Valoare. Minden érték fără TVA, lei.

A végén számold össze a Valoare oszlopot, és írd oda kontroll-összegként,
hogy egyezik-e a dokumentumban feltüntetett végösszeggel. Ha egy szám
bizonytalanul olvasható, jelöld meg, ne tippelj.
```

### 2. lépés: Az eredmény

Az AI kiadja a táblát (vö. `Pelda_output/oferta_OCR.md`): 12 tétel, objektumonként, a végén **kontroll-összeg 5 375 000 lei**, ami egyezik a feltüntetett végösszeggel. Ez a „operál" pillanat: a kép-halmazból tételes, számolható adat lett.

### 3. lépés: Az őszinte rész (a reality-check lelke)

Az oktató szándékosan rámutat: az OCR **hibázhat**. Egy 800-as mennyiség lehet, hogy 300-nak olvasódott, egy tizedespont elcsúszhat. Ezért van a **kontroll-összeg**: ha a tételek összege nem egyezik a feltüntetett végösszeggel, tudod, hogy valahol hiba van, és rá kell nézni. Az AI a szem, de a szem csalhat, ezért a fegyelmezett kontroll nem opció, hanem kötelező.

---

## Amit a résztvevők megfigyelnek
- Hogy a kép-PDF-ből tényleg lesz tábla, de nem varázslat: OCR fut a háttérben.
- Hogy a **kontroll-összeg** hogyan fogja meg azonnal, ha valami félreolvasódott.
- Hogy hol mondja az AI, hogy „ez bizonytalan": ez az őszinte munka jele.

---

## Tanulás

A szkennelt PDF nem reménytelen, de **nem is vak bizalom kérdése**. A helyes munkafolyamat: OCR → tábla → **kontroll-összeg** → emberi ránézés a jelzett pontokra. Így a legnehezebb fájdalmatokból is használható adat lesz, anélkül hogy vakon megbíznál egy félreolvasott számban.

---

## Mi következik (F3 stáció + F4)
A résztvevők most maguk mérlegelik, mikor éri meg ez a munka és mikor jobb a vektoros export (3.3). Aztán az F4-ben ezt a kinyert adatot összevetjük a kiírással.

---

## Időkeret
- OCR demó: 5 perc
- Az eredmény + kontroll-összeg: 3 perc
- Az őszinte rész (korlátok): 4 perc
- **Össze: 12 perc**

**Verzió:** 1.0 (Regio adaptáció)
