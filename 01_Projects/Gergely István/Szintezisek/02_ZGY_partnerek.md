---
title: "2025 ZGY — B2B vevők (partnerek) rangsora"
description: "2025-ben számlázott B2B értékesítés 37 partner szerinti lebontása (695,6 ezer lei), ahol az első öt vevő az összes forgalom 53%-át adja, jellemzően éttermi, turisztikai és kiskereskedelmi ügyfelek. Függőségi kockázat azonosítására és kulcsvevő-menedzsmentre használható."
description_source: auto
description_hash: 0355dd5581f20b32
type: synthesis
project: Gergely István
source_file: "2025ZGYxlsx.xlsx"
sheet: Sheet1
rows: 38
created: 2026-05-21
tags: [synthesis, sales, customers, b2b]
id: a51e8564-2341-4e86-9245-97fceea9584d
index_schema_version: 1
---
# 2025 ZGY — partnerenkénti értékesítés (áfa nélkül)

## Mit tartalmaz
A **számlás (factura) értékesítés vevő szerinti bontása**, áfa nélküli értéken.
Két oszlop: `Partener` (név + település), `Valoare fara TVA`. **37 partner + végösszeg.**

- **ÖSSZESEN: 695 612 lei** (áfa nélkül).
- Ez gyakorlatilag **megegyezik a [[04_P2025_szamla_profit]] összegével (696 177 lei)** → ugyanaz
  az értékesítés, ott idő szerint, itt **partner szerint** bontva.

## Top 10 vevő

| # | Partner | Település | Érték (áfa n.) | Részesedés |
|---|---|---|---:|---:|
| 1 | EAST COMERCIAL COMPANY SRL | Sub Cetate | 90 941 | 13,1% |
| 2 | JAZZ-SERV-COM SRL | Odorheiu Secuiesc | 90 592 | 13,0% |
| 3 | LORD KING SRL | Odorheiu Secuiesc | 70 102 | 10,1% |
| 4 | PARK REST CATERING SRL | Odorheiu Secuiesc | 65 662 | 9,4% |
| 5 | DESAGTOURS SRL | Sub Cetate | 54 437 | 7,8% |
| 6 | LARICI ABC SRL | Vârșag | 44 933 | 6,5% |
| 7 | LAPROLEM SRL | Odorheiu Secuiesc | 44 013 | 6,3% |
| 8 | FUNDATIA CASA DE BATRANI REF. | Odorheiu Secuiesc | 34 774 | 5,0% |
| 9 | LUKY-IMPEX SRL | Odorheiu Secuiesc | 32 927 | 4,7% |
| 10 | PENSIUNEA SUGO SRL | Odorheiu Secuiesc | 29 106 | 4,2% |

## Kiemelt megállapítások
- **Erős koncentráció**: a top 5 vevő a forgalom **~53%-át**, a top 10 a **~80%-át** adja.
  → Függőségi kockázat: 1-2 nagy vevő elvesztése érzékenyen érintené a számlás csatornát.
- **Vevőprofil**: éttermek/catering (PARK REST CATERING, DESAGTOURS), panziók/turizmus
  (PENSIUNEA SUGO, ABEL TOURS, CSORGOKO PANZIO), ABC-boltok (LARICI ABC, kis viszonteladók),
  intézmények (öregek otthona alapítvány, egyházközség). → **HoReCa + kisbolt + intézmény** vegyes B2B kör.
- **Hosszú farok**: ~27 partner egyenként <30 000 lei; a lista alja apró tételek (pl. SEPTIMIA 848 lei,
  PAROHIA 602 lei). Egy sor gyakorlatilag 0 (ASOCIATIA SPORTIVA "FEEL GOOD", 1,5e-14 ≈ kerekítési maradék).
- Földrajzi súlypont: **Odorheiu Secuiesc (Székelyudvarhely)** és környéke (Sub Cetate, Zetea, Vârșag).

## Mire jó
- Kulcsvevő-menedzsment, koncentrációs kockázat mérése.
- A profit-oldalhoz párosítva (lásd [[04_P2025_szamla_profit]]) megmondható, **mely vevő mennyire jövedelmező** —
  ehhez a partner-szintű költség kellene, ami itt nincs.

Kapcsolódó: [[00_Attekintes]] · [[04_P2025_szamla_profit]]
