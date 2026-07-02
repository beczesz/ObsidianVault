---
title: "F1: Rendrakás és standard-ellenőrzés"
date: 2026-07-02
author: Becze Szabolcs
status: active
description: "Az F1 modul új íve: a RegioConsult munkakörnyezetben 3 projekt van, kettő rendezett (megfelel a belső standardnek), a Napsugár Tejüzem viszont káosz (szétdobált fájlok, rossz nevek, oda nem illő és érzékeny fájlok, pl. jelszavak.txt). A résztvevő 1.1-ben auditálja a projekteket a Internal_Standard.docx ellen (2 zöld pipa, Napsugár piros), 1.2-ben rendet rakat (CLAUDE.md megszületik, jelszó-figyelmeztetés, szemét a Kukába), 1.3-ban felépíti a háromszintű CLAUDE.md navigációs láncot (gyökér, Projects index, projekt), és egy új munkamenetben nulla kontextussal megtalálja a Napsugár beruházás összegét."
id: 3c7a1e58-9d24-4b60-8f13-6a2e0c9d5b41
index_schema_version: 1
bdos_index: true
tags: [ignis-academy, halado, regio-consult, f1, standard, rendrakas, claude-md]
---
# F1: Rendrakás és standard-ellenőrzés
**Időkeret:** 35 perc · **Fázis a workshopban:** 1/6 (a workshop első tapasztalata és közös setup)

## Narratív összefoglaló

Megnyitod a `RegioConsult/` munkakörnyezetet. Három projekt van benne:
- **PAN_Malomkert_Panzio** és **KER_Zold_Kerteszet**: szépen rendezett, a belső standard szerint (mind a 10 mappa a helyén, szabályos fájlnevek, CLAUDE.md, semmi oda nem illő).
- **THR_Napsugar_Tejuzem**: **káosz.** Szétdobált fájlok a projekt gyökerében, rossz nevek (`deviz general JAVITOTT vegleges.xlsx`, `Copy of anexa b.xlsx`), duplikátumok, és oda egyáltalán nem illő fájlok: `paprikas_krumpli_recept.txt`, `csaladi nyaralas 2024.txt`, és a legveszélyesebb: `jelszavak.txt`.

A cégnek van egy írott belső standardje: `Internal_Standard.docx`. Ez a mérce. Az F1 három lépése:
1. **Ellenőrzés (audit):** az AI a standard alapján megnézi, rendben van-e a három projekt. Kettő zöld pipát kap, a Napsugár nem.
2. **Rendrakás:** az AI rendet rak a Napsugárban a standard szerint. Közben megszületik a `CLAUDE.md`, figyelmeztet a `jelszavak.txt`-re, a szemetet a Kukába teszi.
3. **Navigáció (kalandkönyv):** felépítjük a háromszintű CLAUDE.md láncot (gyökér → Projects index → projekt), majd egy új munkamenetben, nulla kontextussal kérdezünk egy Napsugár-részletet (a beruházás összegét). Az AI a láncon át magától eljut a válaszig.

## A kulcs-belátás

A cég rendszere **strukturált** (a két rendezett projekt ezt bizonyítja), de egy projekt elsodródott a káoszba. Az AI itt kétféleképpen segít: **auditál** (megmondja, hol tért el a standardtől), majd **helyreállít** (a standard szerint rendet rak, és a rendet egy CLAUDE.md-be is beleírja, hogy onnantól magától tartsa). A `jelszavak.txt` megtalálása külön fontos: az AI nem csak rendez, hanem a **biztonsági kockázatot is jelzi**.

## Tanulási célok

1. **Standard mint mérce**, egy írott sztenderd (docx) alapján auditálni egy fájlrendszert.
2. **Cowork alapok**, mi a plugin, lokális fájlrendszer, összekötés OneDrive / SharePoint-tal, mi a markdown.
3. **Rendrakás AI-val**, kategorizálás, duplikátum, szemét (Kuka), a standard szerinti mappa-struktúrába rendezés.
4. **Biztonság-tudatosság**, érzékeny adat (jelszavak) felismerése és jelzése.
5. **CLAUDE.md mint memória**, a rend beírása, hogy az AI minden session elején tudja.

## A feladatok

| # | Feladat | Típus | Idő |
|---|---|---|---|
| **1.1** | Audit: rendben vannak-e a projektek a standard szerint? | 🎤 DEMO + mindenki saját gépén | ~10p |
| **1.2** | Rendrakás a Napsugárban (CLAUDE.md, jelszó-figyelés, Kuka) | ⏸ STÁCIÓ + demó | ~12p |
| **1.3** | A CLAUDE.md navigációs lánc: 2 prompt, közte új munkamenet | ⏸ STÁCIÓ | ~10p |

## Otthoni bónusz feladatok

| # | Bónusz | Output |
|---|--------|--------|
| 1.4 | `Feladat_1.4_Bonusz_Standard_md.md` | A standard md-vé alakítása + a CLAUDE.md lánc frissítése (md-natív rendszer) |
| 1.5 | `Feladat_1.5_Bonusz_Uj_projekt_scaffold.md` | Új, üres projekt legyártása a standard szerint |
| 1.6 | `Feladat_1.6_Bonusz_Biztonsagi_soprop.md` | Biztonsági söprés: érzékeny adat minden projektben |
| 1.7 | `Feladat_1.7_Bonusz_Kuka_ellenorzes.md` | Kuka-ellenőrzés: nem került-e fontos fájl a szemétbe (bízz benne, de ellenőrizd) |
| 1.8 | `Feladat_1.8_Bonusz_Duplikatum_tisztitas.md` | Duplikátum- és verzió-tisztítás a 3 projekten |
| 1.9 | `Feladat_1.9_Bonusz_Standard_bovites.md` | A standard bővítése új szabállyal + újra-audit |

## Átmenet F2-be

*„A Napsugár rendben, a CLAUDE.md megvan, a jelszavak biztonságba kerültek. De a napi munkában nem a mappák a kérdés, hanem a teendők. Épp most volt egy belső egyeztetés a Napsugárról, tele feladattal. Ki fogja ezeket nyomon követni?"*

## Asset-ek

- `RegioConsult/Internal_Standard.docx`, a belső standard (a mérce).
- `RegioConsult/Projects/PAN_Malomkert_Panzio/` és `KER_Zold_Kerteszet/`, a két rendezett (compliant) referencia-projekt.
- `RegioConsult/Projects/THR_Napsugar_Tejuzem/`, a káosz (a rendrakás tárgya).

**Verzió:** 2.0 (rendrakás + standard-audit ív, 2026-07-02)
