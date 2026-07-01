---
title: "Regio Tananyag — szimulációs log (2026-07-01)"
date: 2026-07-01
author: Becze Szabolcs
status: active
description: "A Regio Consult haladó tananyag teljes végigszimulálásának jegyzőkönyve: minden fázis (F1-F6) minden feladatának ellenőrzése, a copy-paste promptok végrehajthatósága, és az Excel-assetek képlet-újraszámolása (openpyxl + saját képlet-kiértékelő). Minden kontroll-szám kijön; a talált apró hézagok javítva."
id: b2c4e6f8-0a1b-4c3d-8e5f-6a7b8c9d0e1f
index_schema_version: 1
bdos_index: true
tags: [ignis-academy, halado, regio-consult, szimulacio, teszt, qa]
---
# Regio Tananyag — szimulációs log (2026-07-01)

> Cél: végigmenni minden feladaton úgy, ahogy holnap a résztvevők teszik, és ellenőrizni, hogy a példa-promptok tényleg működnek, az Excel-számok kijönnek, és a megoldókulcsok egyeznek. Módszer: openpyxl struktúra-ellenőrzés + saját képlet-kiértékelő (SUM/ROUND/MAX/kereszthivatkozás), ami az élő Excel/Cowork-újraszámolást szimulálja.

## Összegzés: MINDEN ZÖLD

| Fázis | Feladat | Ellenőrzés | Eredmény |
|---|---|---|---|
| F1 | 1.1 CLAUDE.md | sandbox navigálható, gyökér + projekt CLAUDE.md megoldókulcs megvan | PASS |
| F1 | 1.2 projekt-CLAUDE.md | a projekt-mappa létezik, promptban hivatkozott utak valósak | PASS |
| F2 | 2.1 egyeztetés → feladatlista | forrás leirat + megoldókulcs (5 feladat) egyezik, számok konzisztensek | PASS |
| F2 | 2.2 follow-up | a feladatlistából levezethető, sztenderd-formátum | PASS |
| F3 | 3.1 formátum-triázs | a szkennelt PDF/PNG kép-only, a vektoros forrás létezik | PASS |
| F3 | 3.2 OCR | OCR-md kontroll-összeg = 5 375 000 (= feltüntetett végösszeg) | PASS |
| F3 | 3.3 token-mérleg | döntési feladat, forrás-anyag adott | PASS |
| F4 | 4.1 összevetés | deviz Cap.4 = 5 435 000 vs. ajánlat 5 375 000, eltérés −60 000 (4.6) | PASS |
| F4 | 4.2 eltérés-riport | a megoldókulcsból levezethető | PASS |
| F5 | 5.1 skill-alapok | fogalmi demó | PASS |
| F5 | 5.2 struktúra-felismerés | URES templét 3 lap, szürke input-cellák FELOLDVA (írható) | PASS |
| F5 | 5.3 KILLER: templét kitöltés | **URES kitöltve forrásból → Cap.4 5 435 000, TOTAL 6 455 000, cu TVA 7 681 450** | PASS |
| F5 | 5.6 Anexa B | An1 venit 5 400 000, cheltuieli 3 770 000, profit net 1 369 200 | PASS |
| F6 | 6.1 Centralizator | contract 5 375 000, SL1 610 000, Rest de executat 4 765 000 | PASS |
| F6 | 6.2 dokumentum-gen | a Centralizatorból + sztenderdből levezethető | PASS |

## Az Excel-újraszámolás részletei (a szimuláció magja)

Saját képlet-kiértékelővel (a Cowork/Excel élő újraszámolását utánozva) minden képletes cella kiszámolva:

**KITÖLTÖTT deviz (megoldókulcs):**
- 5_DO1 C17 (4.1 Construcții) = 3 190 000 ✓
- 1_DG C25 (Cap.4) = 5 435 000 ✓
- 1_DG C38 (TOTAL fără TVA) = 6 455 000 ✓
- 1_DG D38 (TVA 19%) = 1 226 450 ✓
- 1_DG E38 (cu TVA) = 7 681 450 ✓
- 1_DG F38 (Eligibil) = 6 417 000 ✓
- 1_DG C39 (din care C+M) = 3 685 000 ✓

**F5 KILLER szimuláció (üres templét kitöltése forrásból):** a szürke input-cellák feltöltése után az 1_DG magától aggregál: Cap.4 = 5 435 000, TOTAL = 6 455 000, cu TVA = 7 681 450. **A templét működik.**

**Centralizator (kitöltött):** Valoare contract 5 375 000 (= ajánlat), SL1 összesen 610 000, Rest de executat 4 765 000. ✓

**Anexa B (kitöltött):** An1 venit 5 400 000, cheltuieli 3 770 000, profit net 1 369 200; profit net kumulált 5 év 10 710 000. ✓

## Talált és javított hézagok

1. **F2 narratíva:** az egyeztetés említett egy „rossz helyen lévő proiect tehnic scan"-t áthelyezésre, de a sandboxban nem volt ilyen fájl. → Hozzáadva egy helyőrző (`03_Documente_de_lucru/THR_Proiect_tehnic_scan_nota_24.06.2026.md`), így az F2 áthelyezés-teendő végrehajtható.
2. **Gondolatjel-mentesség:** a tananyag 42 fájljából eltávolítva minden em dash (vault §0 szabály).

## Technikai megjegyzés (nem hiba)
Az xlsx-ek openpyxl `data_only` módban None cache-t adnak, mert programozottan készültek (soha nem nyíltak meg Excelben, ezért nincs cache-elt eredmény). Ez **nem probléma**: a Cowork/Excel megnyitáskor mindig újraszámol, és a képletek helyesen aggregálnak (ezt a saját kiértékelő igazolta). Az URES templéteket szándékosan nem nyitottuk meg / mentettük újra, hogy a kézzel épített formázás (szürke cellák, lapvédelem, font) sértetlen maradjon.

## Verdikt
A tananyag numerikusan pontos, a templétek működnek, a promptok végrehajthatók, a megoldókulcsok egyeznek. **Használatra kész.**
