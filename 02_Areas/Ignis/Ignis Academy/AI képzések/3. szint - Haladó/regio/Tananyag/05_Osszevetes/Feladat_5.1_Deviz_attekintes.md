---
title: "Feladat 5.1: A deviz átnézése és értelmezése (DEMO)"
date: 2026-07-02
author: Becze Szabolcs
status: active
description: "F5 első feladat: mielőtt bármit összevetnénk, az AI-val átnézetjük és ÉRTELMEZTETJÜK a projekt kiírás-devizét (egy hiteles, HG 907 szerinti deviz general xlsx). Az AI megnyitja a három lapot (0_IG, 1_DG, 5_DO1), elmagyarázza a struktúrát, kiolvassa a kulcsszámokat (TOTAL, Cap.4 investiția de bază, C+M, eligibil/neeligibil), és véleményt mond. Ezzel bebizonyítjuk, hogy a Claude nem csak szöveget, hanem az XLS-formátumot (lapok, képletek, kereszthivatkozások) is érti, és üzletileg értelmezi."
id: 78059eb0-1697-4d5a-8e2c-2d4f0a6e5b3c
index_schema_version: 1
bdos_index: true
tags: [ignis-academy, halado, regio-consult, f5, feladat, deviz, excel, demo]
---
# Feladat 5.1: A deviz átnézése és értelmezése (DEMO)

> **Típus:** 🎤 OKTATÓI DEMO · **Idő:** ~10 perc

---

## Szituáció

Mielőtt bármit összevetnénk, nézzük meg magát a **kiírás-devizt**. Ez egy komplex, HG 907 szerinti deviz general: hét kapitulus, alkapitulusok, kereszthivatkozott lapok, TVA- és eligibil-számítások. Egy szakembernek is percekbe telik átlátni. Nézzük meg, mit kezd vele a Claude, és mennyit ért meg belőle.

Ez egyben egy fontos bizonyíték: a Claude **nem csak szöveget, hanem az Excelt is érti**, a lapokkal, képletekkel, kereszthivatkozásokkal együtt.

---

## A demó menete

### 1. lépés: Az AI átnézi és értelmezi a devizt

```
Nyisd meg a projekt kiírás-devizét (02_Editabil, 01.b_THR_Deviz_general...xlsx),
és értelmezd nekem. Mondd el:
- mi ez a dokumentum, milyen struktúrát követ (kapitulusok),
- mit tartalmaz a három lap (0_IG, 1_DG, 5_DO1), és hogyan függenek össze,
- a kulcsszámok: TOTAL general (fără és cu TVA), a legnagyobb kapitulus, a C+M
  (construcții + montaj) arány, az eligibil/neeligibil bontás,
- a véleményed: mire épül a beruházás, van-e bármi, ami kiugrik vagy magyarázatra
  szorul.
Ne módosíts semmit, csak olvasd, értsd és értelmezd.
```

### 2. lépés: Az eredmény

Az AI ~1-2 perc alatt átlátja a devizt, és többek között ezt mondja:
- **Ez egy deviz general** a HG 907 szerint: 7 kapitulus (teren, utilități, proiectare, investiția de bază, alte, probe, audit).
- **A három lap:** `0_IG` a paraméterek (Cota TVA 19%, curs), `1_DG` a fő összesítő (a Cap. 4 sorai a `5_DO1` obiect-devizből húznak kereszthivatkozással), `5_DO1` a részletes építési tételek.
- **Kulcsszámok:** TOTAL GENERAL **6 455 000 lei** fără TVA (**7 681 450** cu TVA), a **Cap. 4 investiția de bază 5 435 000** a beruházás zöme (84%), a **C+M 3 685 000**, az **eligibil 6 417 000** (a Cap. 5.2 comisioane/taxe 38 000 neeligibil).
- **Vélemény:** erősen **építés-vezérelt** beruházás (a Cap. 4-en belül a construcții 3 190 000 dominál), az active necorporale (szoftver, 60 000) kicsi; a struktúra hiánytalanul követi a HG 907-et.

---

## Amit a résztvevők megfigyelnek
- Hogy a Claude **megnyitja és érti az xlsx-et**: a lapokat, a kereszthivatkozásokat (`5_DO1` → `1_DG`), a képleteket (TVA, összesítők).
- Hogy nem csak felolvassa a számokat, hanem **üzletileg értelmezi** őket (mi a zöm, mi az arány, mi az eligibil).
- Hogy egy szakembernek is időigényes átlátás **percekben** megvan.

---

## Tanulás

A Claude **nem szövegfeldolgozó, hanem dokumentum-értő.** Egy komplex, több lapos, képletvezérelt Excel-devizt megnyit, átlát, és a lényegét elmondja: struktúra, kulcsszámok, arányok, vélemény. Ez a képesség az egész F5-F6 alapja: ha érti a devizt, akkor tud vele **összevetni** (5.2) és **kitölteni** (F6). Előbb az értés, aztán a művelet.

---

## Mi következik (5.2)

Most, hogy az AI érti a devizt, jöhet a valódi kérdés: megfelel-e neki a kivitelező ajánlata? Az 5.2-ben tételesen összevetjük a devizt (ajánlatkérés) és az F4-ban kinyert ajánlatot, és megkeressük az eltérést.

---

## Időkeret
- A deviz megnyitása + értelmezés: 5 perc
- A kulcsszámok + vélemény megbeszélése: 3 perc
- Kérdések: 2 perc
- **Össze: 10 perc**

**Verzió:** 1.0 (deviz-értelmezés, 2026-07-02)
