---
title: "P2025 SZAMLA — számlás értékesítés profitja időben"
type: synthesis
project: Gergely István
source_file: "P2025 SZAMLAxlsx.xlsx"
sheet: Sheet1
rows: 292
created: 2026-05-21
tags: [synthesis, profit, invoices, timeseries]
id: 92116911-949c-4a69-be60-234ca848d170
index_schema_version: 1
---

# P2025 SZAMLA — számlás (factura) értékesítés profitja, heti/napi bontásban

## Mit tartalmaz
A **számlás B2B értékesítés napi soronkénti elszámolása**, hetekbe (Saptamana 1…53) csoportosítva,
heti és végösszegekkel. Minden nap: hány számla kelt, mennyi az **önköltség** és az **eladási érték**,
és ebből mennyi a **profit** (lej-ben és %-ban). A "Valuta" oszlopok (deviza) végig 0 → csak lejes ügyletek.

| Oszlop | Jelentés |
|---|---|
| Zi | nap / "…total facturi = N" (aznapi számlák száma) |
| cost (LEI) | beszerzési önköltség |
| val. fara TVA | eladási érték áfa nélkül |
| Profit valoare | profit = eladás − önköltség |
| Profit % | profit / eladás |

## Végösszeg (2025)
- Önköltség: **527 326 lei**
- Eladás (áfa n.): **696 177 lei**
- **Profit: 168 851 lei → 24,25%**
- Számlák összesen: **3 499** (napi darabszámok összege)

> Az eladási összeg (**696 177**) gyakorlatilag azonos a [[02_ZGY_partnerek]] végösszegével (695 612)
> → ugyanaz az értékesítés, ott **partner**, itt **idő** szerint bontva.

## Havi trend

| Hónap | Eladás (áfa n.) | Profit | Profit% |
|---|---:|---:|---:|
| 01 | 55 900 | 14 061 | 25,2% |
| 02 | 62 323 | 15 551 | 25,0% |
| 03 | 55 129 | 15 183 | 27,5% |
| 04 | 61 047 | 15 781 | 25,9% |
| 05 | 63 373 | 14 373 | 22,7% |
| 06 | 68 079 | 14 144 | 20,8% |
| 07 | 67 463 | 15 408 | 22,8% |
| 08 | **70 866** | 16 543 | 23,3% |
| 09 | 69 947 | 16 489 | 23,6% |
| 10 | 45 719 | 11 630 | 25,4% |
| 11 | **27 227** | 7 074 | 26,0% |
| 12 | 49 104 | 12 615 | 25,7% |

## Kiemelt megállapítások
- **Szezonalitás**: a forgalom **nyáron csúcsosodik (jún–szept, havi 67–71 e lei)** — egybevág a
  HoReCa/turisztikai vevőkörrel ([[02_ZGY_partnerek]]: panziók, catering, éttermek a fő vevők).
- **November mély gödör (27 e lei)** — a leggyengébb hónap, a nyári csúcs ~40%-a. Érdemes okot keresni
  (szezonvég? egy nagy vevő kiesése? hiányos adat?).
- **Stabil árrés ~24–25%**, ingadozás 20,8% (jún) és 27,5% (márc) között. A profit% nem romlik a
  volumennel — egészséges árazás.
- A napi profit% szór (egyes napokon 15–37%) a termékmix függvényében, de heti szinten kisimul.

## Mire jó
- Cash-flow és szezonalitás tervezés (készletfeltöltés a nyári csúcs elé).
- Árrés-erózió figyelése időben.
- Partner- és időbontás együtt (ZGY + P2025) → teljes kép a számlás csatornáról; ami **hiányzik**: a
  partner × idő kereszttábla és a partnerenkénti profit.

Kapcsolódó: [[00_Attekintes]] · [[02_ZGY_partnerek]] · [[05_GERDIT_szamlaregiszter]]
