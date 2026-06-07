---
title: "Ignis Academy — Haladó AI Workshop (HBC)"
date: 2026-05-14
author: Becze Szabolcs
status: active
description: "Ez egy 4 órás interaktív AI workshop tananyaga, amelynek során a résztvevők átveszik egy fiktív cég (TransOffice) vezetési szerepét és végigvezetik azt EU-pályázat beadásáig, miközben megtanulnak AI-val dolgozni a gyakorlatban. Oktatóknak és vállalkozó-résztvevőknek szól; 6 fázisos, élő demó-alapú curriculum, amely ka"
description_source: auto
description_hash: c9751c7d13d1f0ae
id: 46be868a-fbd6-4f6a-ba06-6e955976288b
index_schema_version: 1
bdos_index: true
---
# Ignis Academy — Haladó AI Workshop (HBC)
## Tananyag-csomag

> **Verzió:** 1.2 (2026 pivot + F4 2-pont modell + 5 bónusz/fázis)
> **Kiadás dátuma:** 2026-05-12 (v1.1: dry-run javítások)
> **Időkeret:** 4 óra (1 munkanap)
> **Célközönség:** 10-15 fős HBC csoport — vállalkozók, vezetők, középvezetők
> **Nyelv:** Magyar (a TransOffice cég asseteiben román dokumentumok is)

---

## Mi ez?

Ez egy **élő, vezetett 4 órás AI workshop tananyaga**, amely egy fiktív cég (TransOffice Trade SRL) teljes történetén keresztül mutatja be, mit jelent az AI-val együtt dolgozni egy igazi vállalati helyzetben.

**A workshop egy film:** a résztvevő átveszi a TransOffice új *Operations & Systems Manager* szerepét, és 4 óra alatt végigviszi a céget a káoszból egy beadott EU pályázatig (elektromos járműflotta, AFM Mobilitate Verde 2026).

**Módszer:** *„Narrated Live Experience"* — 70% élő demo, 20% mikro-hands-on, 10% szabad próbálkozás. Az oktató narrál, a résztvevők belépnek a kulcs-pillanatokban.

---

## Hogyan használd ezt a csomagot?

### Oktatóként
1. Olvasd el a `00_Bevezetes/Ceg_leiras_TransOffice.md` fájlt — ez a fiktív cég teljes kontextusa.
2. Menj végig a 6 fázis (01 → 06) `README_FX.md` és `Feladat_X.X.md` fájlain.
3. A `TransOffice/` mappa a workshop **kiindulópontja** — kaotikus, rendezetlen vállalati fájlok.
4. A workshop közben a Cowork-kel ezeket a fájlokat **rendszerezzük, elemezzük, kommunikáljuk és felhasználjuk**.

### Résztvevőként
1. Nyisd meg a `TransOffice/` mappát a Cowork-ben — ez lesz a kiindulási környezeted.
2. Kövesd a feladatleírásokat fázisonként (`01_Ceg_megertes`, `02_Meeting_Productivity`, ... `06_Marketing_Honlap`).
3. Minden fázisnak van egy `README_FX.md` (áttekintés) és 2-3 `Feladat_X.X.md` (konkrét feladatok).

---

## Mappastruktúra

```
Tananyag/
├── README.md                                ← Ez a fájl
├── 00_Bevezetes/                            ← Cégleírás, kontextus
│   └── Ceg_leiras_TransOffice.md
│
├── TransOffice/                             ← A FIKTÍV CÉG ASSETEI (kiindulópont)
│   ├── (sok rendezetlen fájl, Excel, docx, txt)
│   ├── Kovacs_Ilona/                        ← anyu mappája (200+ rendezetlen fájl)
│   ├── Marketing/                           ← marketing-anyagok
│   ├── meetings/                            ← meeting transcriptek
│   └── email_exportok/                      ← email szövegek (.txt fájlok)
│
├── 01_Ceg_megertes/                         ← F1: Rend a fájlok között (20-25p)
│   └── Feladat_1.1.md, ..., Feladat_1.6_Bonusz.md
│
├── 02_Meeting_Productivity/                 ← F2: Rend a TODO-k között (20-25p)
│   ├── README_F2.md
│   ├── Feladat_2.1, 2.2 (LIVE)
│   └── Feladat_2.3, 2.4, 2.5 (OTTHONI BÓNUSZ)
│
├── 03_Dontes_Elemzes/                       ← F3: Adatvadászat + eligibility (25-30p)
│   ├── README_F3.md
│   ├── Feladat_3.1, 3.2, 3.3 (LIVE)
│   ├── Feladat_3.4, 3.5, 3.6, 3.7 (OTTHONI BÓNUSZ)
│   ├── Palyazat_kiiras/                     ← 94 oldalas AFM pályázati kiírás
│   │   ├── Ghidul-solicitantului-Mobilitate-Verde-IMM-2026.md
│   │   └── Ghidul-solicitantului-Mobilitate-Verde-IMM-2026.pdf
│   └── Pelda_outputok/                      ← minta-output 3 fájlja a 3 feladathoz
│       ├── eligibility_check.md
│       ├── mellekletek_gap_analysis.md
│       └── data_completion_board.md
│
├── 04_Legal_Szerzodes/                      ← F4: Kommunikáció + feldolgozás (30-35p)
│   ├── README_F4.md
│   ├── Feladat_4.1 (Legal), 4.2 (Pénzügy), 4.3 (CEO PPT) (LIVE)
│   ├── Feladat_4.4, 4.5, 4.6, 4.7 (OTTHONI BÓNUSZ)
│   └── emails/                              ← Válaszemailek a workshop közben „megérkeznek"
│       ├── bela_bacsi_valasz/email.md
│       └── mihaela_konyvelo_valasz/
│           ├── email.md
│           └── bilant_TransOffice_2024_2025.xlsx
│
├── 05_Kommunikacio_Email/                   ← F5: Pályázat összeállítás (30-35p)
│   ├── README_F5.md
│   ├── Feladat_5.1 (Plan de afaceri), 5.2 (Csomag), 5.3 (Form) (LIVE)
│   ├── Feladat_5.4, 5.5, 5.6, 5.7 (OTTHONI BÓNUSZ)
│   ├── Plan_de_afaceri_TransOffice_AFM_2025.md
│   ├── Dosar_complet_AFM_Mobilitate_Verde_2025.md
│   └── formular_depunere_AFM_Mobilitate_Verde.html  ← MySMIS-form mockup
│
└── 06_Marketing_Honlap/                     ← F6: Web redesign (25-30p)
    ├── README_F6.md
    ├── Feladat_6.1, 6.2 (LIVE)
    ├── Feladat_6.3, 6.4, 6.5 (OTTHONI BÓNUSZ)
    └── website/
        └── old/                             ← TransOffice 2020-as „régi" weboldal
            ├── index.html  (Acasă)
            ├── despre.html
            ├── produse.html
            ├── servicii.html
            └── design-system/
                └── anaf-style.css
```

---

## A 6 fázis a workshop ívén

| # | Fázis | Idő | Lényeg |
|---|-------|-----|--------|
| **F1** | Rend a fájlok között | 20-25p | 200+ kaotikus fájl → rendezett mappa + CLAUDE.md |
| **F2** | Rend a TODO-k között | 20-25p | Kaotikus meeting transcript → mentett TODO-k |
| **F3** | Adatvadászat + eligibility | 25-30p | 94 oldalas pályázati kiírás → eligibility riport + gap analízis + Data Completion Board |
| **F4** | Kommunikáció + feldolgozás | 30-35p | 3 sub-flow: Legal (Béla bácsi sztori), Pénzügy (Mihaela könyvelő), CEO PPT |
| **F5** | Pályázat összeállítás | 30-35p | Üzleti terv + submission csomag + MySMIS form (WOW blokk) |
| **F6** | Web redesign | 25-30p | Régi 2020-as TransOffice weboldal → modern új design |

---

## Mit fogsz csinálni

A workshop végére (4 óra alatt):
1. **Megérted** egy fiktív cég teljes helyzetét (káosz → rendszer)
2. **Beadsz** egy 23-mellékletes EU-pályázatot AFM Mobilitate Verde 2026-re
3. **Generálsz**: üzleti tervet, 3 emailt, 1 jogi cross-check riportot, 1 CEO PPT-t, 1 modern weboldalt
4. **Átéled** mit jelent az AI-val együtt dolgozni — *nem tool-tanulás, hanem perspektíva-váltás*

---

## Mit kell hozzá

- **Claude Pro** ($20/hónap) — a Cowork desktop alkalmazás miatt
- **Obsidian** (ingyenes) — a Markdown-fájlokat itt nyitod meg
- **Egy laptop**, Chrome browser, internet

Részletes előfeltételek: lásd a workshop kezdetén az oktató kézikönyvében.

---

## Licenc és felhasználás

Ez a tananyag az **Ignis Academy** szellemi terméke. A TransOffice Trade SRL **fiktív cég** — minden hasonlóság valódi cégekkel a véletlen műve. A pályázati kiírás (AFM Mobilitate Verde 2026) szintén **fiktív, oktatási célokra készült** — bár a romániai AFM mintáját követi.

A tananyagot kizárólag a megrendelő HBC csoportja használhatja a workshop-on és azt követő gyakorláshoz. Tovább nem terjeszthető.

---

**Verzió:** 1.2 (2026 pivot + F4 2-pont) · **Készítette:** Ignis Academy · **Kapcsolat:** [Szabolcs] · **Utolsó frissítés:** 2026-05-14
