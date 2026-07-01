---
title: "Fiktív deviz-példa — Napsugár Tejüzem (killer-demo alap)"
date: 2026-06-30
author: Becze Szabolcs
status: active
version: 1.0
description: "Teljesen fiktív, de a valós RC deviz general (HG 907) struktúrát hűen tükröző tananyag-példa a Regio haladó képzés Excel-templét-kitöltő demójához. Három fájl: forrás-ajánlat, üres deviz-templét (szürke input-cellák, levédett lapok), kitöltött deviz. Tartalmazza a demó-forgatókönyvet és a deviz-struktúra magyarázatát (skill-seed)."
id: c7e2a4d1-3b9f-4e62-9a18-2f6b8c0d5e41
index_schema_version: 1
bdos_index: true
tags: [ignis-academy, kepzes, halado, regio-consult, fiktiv-pelda, deviz, killer-demo, skill]
---

# Fiktív deviz-példa — „Napsugár Tejüzem"

> **Teljesen fiktív.** Kitalált cég, kitalált számok. Sehol nincs valós RC-ügyféladat, ezért **szabadon használható tananyagban, microsite-on, újra más ügyfélnél.** A valós referenciák a `../raw/`-ban maradnak, konfidenciálisan. A struktúra hűen követi a valós `RCM_Deviz RON_PNRR` (HG 907) felépítését.

## A fiktív projekt
- **Beruházás:** Extindere fabrică de procesare lapte (tejfeldolgozó-bővítés)
- **Beneficiar:** SC NAPSUGÁR TEJÜZEM SRL (fiktív) · CUI RO12345678 · Cristuru Secuiesc, Harghita
- **Proiectant:** SC PLANTERV STUDIO SRL (fiktív)
- Finanszírozási logika: PNRR-szerű építési beruházás, TVA 19%, curs 4,97 lei/EUR.

## A három fájl (a killer-demo „hármasa")
| Fájl | Mi ez | Szerep a demóban |
|---|---|---|
| `01_forras_oferta_Napsugar.xlsx` | Kivitelezői ajánlat / antemăsurătoare: lapos tételsor (obiect, categorie, UM, cantitate, preț, valoare) | **A FORRÁS** — ezt „kapja" a résztvevő |
| `02_deviz_general_URES_templet.xlsx` | A deviz general üres templétje: 3 lap (`1_DG`, `0_IG`, `5_DO1`), **szürke input-cellák**, képletek készen, **lapvédelem bekapcsolva** (jelszó: `rcm`) | **AZ ÜRES TEMPLÉT** — ezt tölti ki az AI |
| `03_deviz_general_KITOLTOTT.xlsx` | Ugyanaz, kitöltve a forrásból | **A CÉL / megoldókulcs** — ezzel vetjük össze |

## A demó forgatókönyve (F-killer)
1. Megnézzük az **üres templétet**: 32-lapos szörny helyett itt 3 lap, de ugyanaz a logika. Megmutatjuk, hogy **csak a szürke cellákba lehet írni** (a többi levédett, képletes) — pont mint náluk.
2. Megnézzük a **forrás-ajánlatot**: lapos tételsor, objektumonként.
3. Az AI-nak adunk egy **skillt** (lásd lent), ami **elmagyarázza a deviz struktúráját**, és megkérjük: töltsd ki az üres templét `5_DO1` szürke celláit a forrás-ajánlatból.
4. A `1_DG` automatikusan aggregál (kereszthivatkozás `5_DO1`-re, TVA-számítás, eligibil/neeligibil).
5. Összevetjük a `03_KITOLTOTT`-tal → **WOW: „operál".**

## A deviz-struktúra dióhéjban (ez a skill magja)
- **`0_IG`** — info general + paraméterek: **Cota TVA (B9)**, curs EUR. Minden TVA-képlet innen húz.
- **`1_DG` Deviz General** — 7 kapitulus a HG 907 szerint:
  - Cap 1 teren, Cap 2 utilități, Cap 3 proiectare/consultanță, **Cap 4 investiția de bază** (a zöm), Cap 5 alte (organizare, taxe, diverse, publicitate), Cap 6 probe, Cap 7 audit.
  - Oszlopok: Valoare fără TVA → **TVA = ROUND(C × cota,2)** → cu TVA → Eligibil → Neeligibil (= C − Eligibil).
  - Cap 4 sorai **nem kézi értékek**, hanem a `5_DO1` detail-lapról húznak (`='5_DO1'!C17` stb.).
- **`5_DO1` Devizul obiectului** — itt élnek a tényleges építési tételek objektumonként (Hala, Depozit, Centrală, Amenajări), objektum-subtotal = SUM(leveles sorok), és innen jön a Cap 4.1/4.2/4.3/4.5.

## Ellenőrző számok (kitöltött, lei)
- 5_DO1 Construcții total (4.1): **3 190 000**  (Hala 2 330 000 + Depozit 380 000 + Centrală 270 000 + Amenajări 210 000)
- Cap 4 összesen: 5 435 000 · Cap 1: 125 000 · Cap 2: 220 000 · Cap 3: 335 000 · Cap 5: 285 000 · Cap 6: 25 000 · Cap 7: 30 000
- **TOTAL GENERAL fără TVA: 6 455 000** · TVA 19%: 1 226 450 · **cu TVA: 7 681 450**
- Eligibil: 6 417 000 (az 5.2 taxe 38 000 neeligibil) · din care C+M: 3 685 000

## A teljes fiktív készlet
| Fájl | Szerep |
|---|---|
| `01_forras_oferta_Napsugar.xlsx` | forrás-ajánlat (vektoros) |
| `02_deviz_general_URES_templet.xlsx` | üres deviz-templét (szürke input, levédett) |
| `03_deviz_general_KITOLTOTT.xlsx` | kitöltött deviz (megoldókulcs) |
| `04_anexaB_uzleti_terv_URES_templet.xlsx` | üres üzleti terv (Ipoteze → Venituri/Cheltuieli/CPP/Indicatori) |
| `05_anexaB_uzleti_terv_KITOLTOTT.xlsx` | kitöltött üzleti terv |
| `oferta_szkennelt_Napsugar.pdf/.png` | **fiktív szkennelt** ajánlat (kép-only, OCR-hez) |
| `oferta_szkennelt_Napsugar_OCR.md` | OCR-eredmény + kontroll-összeg |
| `06_monitorizare_Centralizator_URES.xlsx` | üres monitoring-tábla (Valoare contract + SL1-3 + Rest, képletekkel) |
| `07_monitorizare_Centralizator_KITOLTOTT.xlsx` | kitöltött monitoring (contract az ajánlatból + SL1 minta) |

## Teljes lánc a #1 fájdalomra (end-to-end demo)
`oferta_szkennelt_Napsugar.pdf` (kép) → **OCR** → `..._OCR.md` (strukturált) → **md + `06_...URES` Centralizator** → az AI kitölti a „Valoare contract" oszlopot (ajánlat-tétel → deviz-kód leképezés) → a `07_...KITOLTOTT` a végeredmény: SL-enként követhető részteljesítés + `Rest de executat` automatikusan. Kontroll: a TOTAL = 5 375 000 = az ajánlat végösszege. ✓

**Anexa B ellenőrző számok (kitöltött):** An1 venit 5 400 000, cheltuieli 3 770 000, profit net 1 369 200 lei (impozit 16%). 5 év növekvő kihasználtsággal (60→90%).

## Megjegyzés a tananyaghoz
A valós `RCM_Deviz` 32 lap; ez a fiktív 3 lapra egyszerűsít, **de a logika (kereszthivatkozás, levédett cellák, TVA, eligibil-bontás) ugyanaz**. Az Anexa B üzleti terv szintén egyszerűsített, de hű pénzügyi modell. A szkennelt PDF konverzió / OCR token-stratégia külön dokumentumban: [[03_konverzio_es_OCR_strategia_2026-06-30]].
