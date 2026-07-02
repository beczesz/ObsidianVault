---
title: "F4: Szkennelt ajánlat → használható adat (reality-check)"
date: 2026-07-01
author: Becze Szabolcs
status: active
description: "Az F4 modul a Regio legnehezebb napi fájdalmát kezeli: egy állami platformról letöltött, kép-only szkennelt ajánlatból (200 oldal körül) hogyan lesz gépi-olvasható, tételes adat. Megtanítja a vektoros vs. szkennelt PDF különbséget, az OCR korlátait, a formátum-triázst és a token-mérleget. Őszinte elvárás-kezelés: mit tud az AI, mit nem (még)."
id: 016e2892-4f26-4a07-8e5b-5d6a4f8e3c1a
index_schema_version: 1
bdos_index: true
tags: [ignis-academy, halado, regio-consult, f4, ocr, szkennelt-pdf]
---
# F4: Szkennelt ajánlat → használható adat (reality-check)
**Időkeret:** 35 perc · **Fázis a workshopban:** 4/6 (a legfontosabb napi fájdalom)

## Modell

🎤 **DEMO** + ⏸ **2 stáció** a résztvevőknek.

| # | Fájl | Típus | Idő |
|---|---|---|---|
| **4.1** | `Feladat_4.1_Formatum_triazs.md` | ⏸ STÁCIÓ (vektoros vs. szkennelt felismerés) | ~7p |
| **4.2** | `Feladat_4.2_OCR_kiolvasas.md` | 🎤 OKTATÓI DEMO (OCR élőben) | ~12p |
| **4.3** | `Feladat_4.3_Token_merleg.md` | ⏸ STÁCIÓ (mit ér meg, hol a határ) | ~8p |

## Narratív összefoglaló

Az imént az F3-ban élőben láttuk beérkezni a kivitelező emailjét az ajánlattal. Csakhogy az ajánlat **szkennelt PDF, 200 oldal körül**, és pont ez a feladatlista első, legkeményebb tétele. Az állami platformról (e-licitatie / SEAP) letöltött dokumentumokat sem ti exportáljátok, hanem kapjátok, és gyakran kép-only. Kézzel, tételről tételre kell egyeztetni. Ma 100% manuális.

Ez a fázis **őszinte**. Nem ígérjük túl. Megtanítjuk a különbséget a **vektoros** (kinyerhető szöveg) és a **szkennelt / kép** (OCR-re szoruló) PDF között, megmutatjuk mit tud az OCR és hol a határa, és egy token-mérleggel érzékeltetjük, mikor éri meg az AI-ra bízni és mikor a vektoros / Excel-export beszerzése a helyesebb út.

**Ez maga egy WOW-kontraszt:** „ezt tudja / ezt nem (még)". A csalódás elkerülésének a kulcsa, hogy pontosan tudjátok, melyik dokumentummal mire számíthattok.

## Tanulási célok
1. **Formátum-triázs**, ránézésre eldönteni: vektoros vagy szkennelt? (És hogyan kérdezd meg az AI-tól.)
2. **OCR a gyakorlatban**, egy kép-PDF-ből tábla, a korlátokkal (hibalehetőség, ezért kontroll-összeg).
3. **Token-mérleg**, miért drága 300 oldal kép, és mi a költséghatékony alternatíva.
4. **Kontroll-fegyelem**, az OCR-adatot mindig ellenőrizzük egy végösszeggel, mielőtt döntünk rá.

## Otthoni bónuszok

| # | Bónusz | Output |
|---|---|---|
| 4.4 | `Feladat_4.4_Bonusz_Sajat_PDF.md` | Saját valós szkennelt PDF próbája |
| 4.5 | `Feladat_4.5_Bonusz_Tabla_kinyeres.md` | Egy konkrét tábla kinyerése + kontroll |
| 4.6 | `Feladat_4.6_Bonusz_Vektoros_export.md` | A vektoros / Excel-export beszerzési útja |

## Átmenet F5-be

*„Most már gépi-olvasható az ajánlat (md táblában). De ez önmagában még nem válasz a kérdésre: megfelel-e az ajánlat a kiírásnak? Az F5-ben az ajánlatkérést (deviz) tételesen összevetjük az ajánlattal, és megkeressük az eltérést."*

## Asset-ek
- `oferta_szkennelt_Napsugar.pdf` / `.png`, a fiktív szkennelt (kép-only) ajánlat.
- `Pelda_output/oferta_OCR.md`, az OCR-eredmény, kontroll-összeggel (megoldókulcs).

**Verzió:** 1.0 (Regio adaptáció)
