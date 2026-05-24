---
title: "TOTAL GERDIT 2025 — számla-regiszter gestiune-onként"
type: synthesis
project: Gergely István
source_file: "TOTAL GERDIT 2025xlsx.xlsx"
sheet: Sheet1
rows: 3063
created: 2026-05-21
tags: [synthesis, invoices, register]
id: 5c50cfa4-fd7a-42c8-a6f6-b96e6f501474
index_schema_version: 1
---

# TOTAL GERDIT 2025 — tételes számla-regiszter

## Mit tartalmaz
**Tételes számlalista** a 6 gestiune szerint csoportosítva. Soronként egy számla:

| Oszlop | Jelentés |
|---|---|
| Nr. crt. | sorszám az egységen belül |
| Document | bizonylat (pl. `F/3116/17.01.2025` = sorozat/szám/dátum) |
| Valoare fara TVA | érték áfa nélkül |
| Valoare cu TVA | érték áfával |
| Operat | könyvelve? (DA = igen) |

Két számlasorozat figyelhető meg (pl. NAGYKERESKEDES-nél): **4 jegyű (F/3xxx, 118 db)** és
**5 jegyű (F/11xxx, 1 002 db)** — valószínűleg két kassza/sorozat vagy két dokumentumtípus.

## Gestiune-szintű összegzés

| Gestiune | Számlák | Érték áfa nélkül | Érték áfával | Átl. számla (áfa n.) |
|---|---:|---:|---:|---:|
| BIRGITA | 399 | 1 375 802 | 1 579 001 | 3 448 |
| MUSKATLI | 414 | 1 491 778 | 1 703 932 | 3 603 |
| NAGYKERESKEDES | 1 341 | 660 272 | 725 014 | 492 |
| SZEGEDI | 389 | 925 533 | 1 061 249 | 2 379 |
| VEGYESKE | 366 | 891 325 | 1 026 922 | 2 436 |
| ZETEKINCSE | 139 | 278 952 | 324 186 | 2 007 |
| **ÖSSZESEN** | **3 048** | **~5 623 663** | **~6 420 304** | — |

## Kiemelt megállapítások
- **Eltérő profilok az átlagos számlaértékben**: a boltoknál (BIRGITA, MUSKATLI, SZEGEDI, VEGYESKE)
  magas, **2 400–3 600 lei/számla**; a NAGYKERESKEDES-nél alacsony, **~492 lei/számla**, de **sok
  számla (1 341)**. → a nagyker sok kis tételt számláz, a boltok kevesebb, nagyobb bizonylatot.
- **MUSKATLI és BIRGITA a legnagyobb értékű egységek** (1,49 M és 1,38 M áfa nélkül).
- Az áfa-tartalom ~14,5% átlagosan (vegyes 9%/19% kulcsok — élelmiszer 9%, ipari 19%).
- A `Operat = DA` mező a könyvelési státusz; a kivételeket (ha van NU) érdemes szűrni.

## ✅ MEGOLDVA — a GERDIT a teljes ÉRTÉKESÍTÉS (nem beszerzés)
A korábbi nyitott kérdés (eladás vagy beszerzés) **számszerűen feloldva**. A három fájl összege
0,017%-os pontossággal egyezik:

| Forrás | Érték (áfa n.) |
|---|---:|
| `Adaos` kasszás kiskereskedelem | 4 928 463 |
| `P2025` számlás (factura) B2B | 696 177 |
| **Összesen** | **5 624 640** |
| **GERDIT összes** | **5 623 663** |
| Eltérés | −977 (−0,017%) |

→ A **GERDIT a teljes árbevétel telephelyenként** = kasszás nyugták + B2B számlák. Ekkora pontosságú
egyezés nem lehet véletlen, tehát ez **eladási**, nem beszerzési oldal. A [[01_PTOT_keszletmozgas]]
`Intrari` (beszerzés) így **külön** adat marad, nem a GERDIT párja.
A NAGYKERESKEDES alacsony átlagértéke + sok számlája is az eladás mellett szól.

> Maradék finomítás: a −977 lei eltérés valószínűleg kerekítés / egy-két határnapi bizonylat.

## Mire jó
- Telephelyenkénti forgalom/aktivitás összevetése.
- Bizonylat-szintű auditra (sorozatfolytonosság, könyvelési státusz).
- A `P2025` (idő) és `ZGY` (partner) csatornával összevetve a számlás vs. kasszás arány tisztázható.

Kapcsolódó: [[00_Attekintes]] · [[01_PTOT_keszletmozgas]] · [[04_P2025_szamla_profit]]
