---
title: "PTOT 2025 — készletmozgás-elemzés"
type: synthesis
project: Gergely István
source_file: "2025 PTOT xlsx.xlsx"
sheet: Sheet1
rows: 17420
created: 2026-05-21
tags: [synthesis, inventory, stock]
id: 20d57d85-35aa-4581-85e5-5ab7c5aa5082
index_schema_version: 1
---

# 2025 PTOT — készletmozgás (Productie/Total mozgás)

## Mit tartalmaz
Cikkszintű **mennyiségi készletmozgás-jelentés** (nem érték, hanem darab/UM), gestiune-onként csoportosítva.

| Oszlop | Jelentés |
|---|---|
| Poz. | sorszám az egységen belül |
| Articol | cikk megnevezése |
| UM | mértékegység (Buc = darab, KG, L…) |
| Stoc initial | nyitókészlet |
| Intrari | bevételezés (beszerzés/áthelyezés be) |
| Iesiri | kiadás (eladás/áthelyezés ki) |
| Stoc final | zárókészlet |
| Greutate | súly (többnyire 0) |

**Alapazonosság minden sorra:** `Stoc final = Stoc initial + Intrari − Iesiri`.

## Gestiune-szintű összegzés (mennyiség, vegyes UM-mel összeadva — csak nagyságrend!)

| Gestiune | Cikkszám | Nyitó | Bevét (Intrari) | Kiadás (Iesiri) | Záró |
|---|---:|---:|---:|---:|---:|
| BIRGITA | 3 516 | 14 546 | 316 173 | 319 646 | 11 073 |
| MUSKATLI | 4 426 | 18 245 | 287 301 | 289 119 | 16 426 |
| NAGYKERESKEDES | 278 | 20 365 | 499 087 | 494 626 | 24 826 |
| SZEGEDI | 3 250 | 12 607 | 165 090 | 164 969 | 12 729 |
| VEGYESKE | 3 323 | 10 072 | 154 215 | 154 547 | 9 740 |
| ZETEKINCSE | 2 620 | 0 | 61 905 | 52 061 | 9 844 |

> A mennyiségek **különböző mértékegységeket kevernek** (db, kg, l), ezért az összeg csak
> nagyságrendi jelzés, nem pénzügyi mutató.

## Kiemelt megállapítások
- **NAGYKERESKEDES = a forgási motor**: mindössze 278 cikk, de a legnagyobb mennyiségi
  átáramlás (~499 e bevét / 495 e kiadás). Kevés SKU, nagy volumen → klasszikus nagyker.
- **MUSKATLI a legszélesebb választék** (4 426 cikk), BIRGITA hasonló (3 516).
- **ZETEKINCSE nyitó = 0** → **év közben indult** új egység; év végére már ~9 844 záró.
- A boltok **kiadás ≈ bevétel** (kiegyensúlyozott forgás, nincs nagy készletfelhalmozás).
  BIRGITA enyhén csökkenő készlet (záró < nyitó), ZETEKINCSE növekvő (feltöltés alatt).

## Mire jó ez a fájl
- Forgási sebesség / lassan mozgó (holt) készlet azonosítása cikkszinten.
- Leltáreltérés-vizsgálat (a `Stoc final` képletellenőrzéssel).
- A **mennyiségi** oldalt adja; az **érték/árrés** oldalhoz lásd [[03_Adaos_arres]].

## Nyitott kérdés
- Az `Intrari` keveri-e a **beszerzést** és a **gestiune-ok közti áthelyezést**? Ha igen, a
  hálózati nettó beszerzés kisebb, mint a gestiune-onkénti Intrari összege.

Kapcsolódó: [[00_Attekintes]] · [[03_Adaos_arres]] · [[05_GERDIT_szamlaregiszter]]
