---
title: "Regio Consult — beküldött anyagok részletes áttekintése (2026-06-30)"
date: 2026-06-30
author: Becze Szabolcs
status: active
version: 1.0
description: "A Regio Consult által beküldött 2 zip (raw/) részletes technikai áttekintése: belső standard (rulebook), deviz general templét + kitöltött példa, üzleti terv templét + XFA okos-PDF, ajánlatkérés (F1-F4 vektoros + DG/F5/F6 + 226 oldalas szkennelt Oferta) és a Centralizator monitoring Excel. Fájlonkénti katalógus, AI-megvalósíthatósági mátrix a 3 fájdalomra, képzési leképezés, KONFIDENCIÁLIS valódi cégnevek anonimizálási flag, nyitott kérdések egyeztetésre."
id: 9a203731-a399-43c3-9d0f-57768da68a59
index_schema_version: 1
bdos_index: true
tags: [ignis-academy, kepzes, halado, regio-consult, anyag-attekintes, deviz, palyazat, konfidencialis]
---

# Regio Consult — beküldött anyagok áttekintése

> ⚠️ **KONFIDENCIÁLIS.** A `raw/` fájlok valódi ügyfél-adatok (cégnevek: MASTVET SRL sertésfarm, Teleki, „ST"=Sepsi Tej, Abel Tours; CUI-k, összegek). A vault-on belül maradnak, sehova nem kerülnek ki. **Bármilyen tananyagba csak anonimizálva** (kitalált cég, álösszegek). Forrás: a Regio által megosztott 2 zip (`raw/`), 2026-06-30.

## 1. Fájl-katalógus

### A) Belső standard (a „szabálykönyv")
- **`RC_Internal standards_ISZ_06.10.25.docx`** — román nyelvű belső sztenderd. Tartalom: dokumentum-elnevezési konvenció (`dokumentumnév_Iniciálé_dátum`, pl. `01.a_ST_Cerere de finantare_ISz_08.11.2021`), a **kötelező mappa/almappa-hierarchia** (Cerere de finanțare → Editabil → Documente de lucru → Scan → Semnat → C1/C2 edit/scan/semnat → Contract de finanțare + acte adiționale → Proiect tehnic → **Dosare de achiziții 04.01 DAC / 04.02 DAP / 04.03 DAD / 04.04 DAL / 04.05 DAF** → Cereri de plată/rambursare → Monitorizare), kötelező appok (Office365/SharePoint, Outlook, Adobe PDF Pro, e-token, WhatsApp web, **ChatGPT user**, RISCO), kommunikációs szabályok (brand: RegioConsult, **Verdana 9**, email-aláírás, WhatsApp/Teams/Wetransfer), munkaidő 8-19h, szabadság-szabályok, ToDoo/Projektkovetes/Income plan, social media. → **Ez a CLAUDE.md szabálykönyv aranybányája (F1).**

### B) Deviz general — templét + kitöltött (use case #2)
- **`RCM_Deviz RON_PNRR_ISZ_06.06.2025.xlsx`** — **ÜRES TEMPLÉT.** 32 munkalap. A standard HG 907 deviz general: `1_DG` (a fő deviz, 7 kapitulus), `2_DAT`, `3_DU`, `4_DF` (+consultanță/proiectare/diriginte), `5-8_DO1-DO4` (utilaje cu/fără montaj, Dotări), `9_Active necorporale`, `10_DA`, `11_IP`, `12/13_Grafic 24/36 luni`. **Minden lap képletvezérelt és LEVÉDETT (sheet protection).** A `1_DG` cellái kereszthivatkozással húznak a detail-lapokról, TVA-számítás, eligibil/neeligibil bontás.
- **`01. C2_Teleki_HG 907_Devize EUR_BE_30.08.2022.xlsx`** — **KITÖLTÖTT példa** (Teleki projekt, EUR, 36 lap, 2,6 MB). Ugyanaz a struktúra valós adatokkal. (Megj.: 2022-es EUR vs. a templét 2025-ös RON — nem pontosan ugyanaz a verzió, de struktúrában megfeleltethető.)
- **`02._C2_Teleki_PNRR_Activitati_Achizitii_EUR,RON...xlsx`** — beszerzési/aktivitás-terv (Activitati proiect, Activitati-Buget, Achizitii înainte/după CF). A deviz-hez kapcsolódó beszerzési terv.

### C) Üzleti terv — templét + kitöltött okos-PDF (use case #2/#3)
- **`1.a.2_MV_Anexa_B_ISZ_29.01.2024.xlsx`** — **üzleti terv TEMPLÉT** (Anexa B), 13 lap pénzügyi modell: RCM_Venituri, RCM_Cheltuieli, Prognoza veniturilor/cheltuielilor, Cpp, Bilanț, FN An 1-3/1-5 (cash-flow), Indicatori, „Întreprindere în dificultate". Szintén erősen képletezett.
- **`01.e.MV_Anexa_B.pdf`** — **kitöltött „okos PDF".** ⚠️ Ez **XFA dinamikus űrlap** (Adobe LiveCycle). Normál PDF-nézőben/pdftotext-ben ÜRESNEK/1 oldalasnak látszik. **DE a kitöltött értékek az XFA `datasets` XML-csomagban vannak — programatikusan kinyerhetők.** (Fontos megvalósíthatósági nyeremény, lásd lent.)

### D) Ajánlatkérés → ajánlat → monitoring lánc (use case #1 — a fő fájdalom)
Projekt: **EXTINDERE FERMA DE PORCI** (sertésfarm-bővítés). Beneficiar: MASTVET SRL, Proiectant: AEDILISPROIECT SRL.
- **`F1-F4.pdf`** (~173 old., 26 MB) — **VEKTOROS, kinyerhető szöveg** (218 ezer karakter). Az ajánlatkérés központi része: F1 Centralizatorul cheltuielilor pe obiectiv (deviz-kapitulusok listája). ➜ AI-val kinyerhető.
- **`DG.pdf`** (3 old.), **`F5.pdf`** (16 old.), **`F6.pdf`** (2 old.) — **SZKENNELT (kép)**, 0 kinyerhető szöveg. OCR kell.
- **`09.2_MV_PNS_DAL_Oferta.pdf`** (~226 old., 34 MB) — **a kivitelező AJÁNLATA, teljesen SZKENNELT (kép)**. A #1 fájdalom megtestesülése: ezt vetik össze tételesen az ajánlatkéréssel.
- **`01.a.4_MV_DAL_Centralizator SL...xlsx`** — **a kézzel épített CÉL-tábla.** Sorok = deviz-kódok (4.1.2 HALA 1 MATERNITATE, 4.1.6 SILOZURI SI BAZIN DEJECTII, stb.), oszlopok = szerződéses érték + **SL1/SL2/SL3 (situații de lucrări, dátumozott részteljesítések)** + Rest de executat. Ez a „67 ezer köbméterből megvalósult 47 ezer" monitoring pénzben.
- **`_MV_PNS_Centralizator de Contract...xlsx`** — szerződés-centralizátor (14 lap, DASF/DAC/DAA/DAIP/DAMG/DAPT/DAL/DADIR/DAD/Audit/Cote-Taxe bontás).

## 2. AI-megvalósíthatósági mátrix (Haladó scope, agent NÉLKÜL)

| Fájdalom | Részfeladat | Megvalósíthatóság | Megjegyzés / tananyag-kötés |
|---|---|---|---|
| **#1 PDF→adat** | **F1-F4 vektoros deviz → Excel-kapitulusok** | 🟢 **Megy** | Vektoros szöveg, kinyerhető. Itt épül a Centralizator váza. WOW. |
| | 226 old. szkennelt Oferta → tételes adat | 🔴 **Nehéz/részleges** | OCR kell, drága/hibázik. **Reality-check, nem ígérünk túl.** Részleges kísérlet WOW-kontrasztnak. |
| | DG/F5/F6 szkennelt | 🟡 OCR-rel részben | Kis terjedelem, OCR-tesztre jó. |
| | Ajánlatkérés ↔ ajánlat tételes egyezés-check | 🟡 Csak ha mindkettő gépi olvasható | Szkennelt oldalon a #1 korlát. |
| **#2 Templét** | Deviz/üzleti terv struktúra **elmagyarázása** skillben | 🟢 **Megy** | Erősen sztenderd, predikálható szerkezet → ideális skill-tananyag. |
| | Szürke input-cellák kitöltése forrás-adatból | 🟢 **Megy** (a killer-demo) | Templét + kitöltött + forrás hármas a kezünkben. |
| | Levédett/képletes cellák kezelése | 🟡 Óvatosan | Skill tartsa tiszteletben a védett cellákat; csak inputot ír. |
| | **XFA okos-PDF olvasás/kitöltés** | 🟢 **Megy** (datasets XML) | Meglepő nyeremény: a „üres" okos-PDF adata XML-ből kinyerhető. |
| **#3 Pályázatírás** | kiírásból vázlat | 🟢 Megy, de | Haladó-scope-on kívül; csak könnyű érintés (ők már profik, ~10% aktivitás). |

## 3. Képzési leképezés (a `01_adaptacio_strategia_v0.1.md` finomítása)

- **F1 — „Tanítsd be az AI-t, mint új juniort":** a `RC_Internal standards` → gyökér-`CLAUDE.md` + projekt-szintű `CLAUDE.md`-k. A mappa-konvenció (04.01-04.05 dosare de achiziții stb.) 1:1 lefordítható. Lektor-szabály: „minden dokumentum a sztenderd szerint?"
- **F-killer — Excel-skill (Deviz/üzleti terv):** üres `RCM_Deviz` templét + kitöltött `Teleki` + forrás → skill, ami elmagyarázza a kapitulus-logikát és kitölti a szürke cellákat. **Ez a workshop „WOW operál" pillanata.**
- **F-PDF — reality-check stáció:** F1-F4 (megy) vs. Oferta 226 old. szkennelt (nem/alig). A vektoros↔szkennelt különbség élő demója + XFA datasets-trükk.
- **F-monitoring:** Centralizator SL felépítése a deviz-kapitulusokból, SL1/SL2/SL3 részteljesítés-követés. Repetitív Excel = jó skill-jelölt.
- **Skill-modul + Team-megosztás + M365/OneDrive** — ahogy a stratégiában.

## 4. Nyitott kérdések — EGYEZTETÉSRE

1. **OCR-stack a szkennelt PDF-ekre:** vállaljuk-e a workshopon (pl. a 226 old. Oferta részleges OCR-je), vagy csak a vektoros + XFA utat mutatjuk és a szkenneltet őszintén „határ"-ként kezeljük? (Javaslat: utóbbi + 1 rövid OCR-demó.)
2. **Templét-verzió eltérés:** a kitöltött Teleki 2022 EUR ≠ az üres 2025 RON templét. Kérjünk-e **összetartozó** hármast (ugyanaz a projekt: üres + kitöltött + forrás), hogy a killer-demo tiszta legyen? (A meeting-follow-up pont ezt kérte.)
3. **Anonimizálás:** ki készíti a kitalált sandbox-cég adatait? (Javaslat: én generálok egy anonim „sertésfarm/tejgyár" mini-portfóliót a valós struktúra tükrén.)
4. **A levédett deviz-cellák:** a skill csak inputot írjon, a képleteket NE bántsa — ezt szabályként rögzítsük.
5. **Scope-korlát:** mennyit vállalunk a 4 órából monitoring vs. templét vs. PDF-re? (A #2 templét a legmagasabb hozam/erőfeszítés.)

## 5. Mit kérjünk még a Regiótól (a tiszta demóhoz)
- [ ] **Összetartozó** deviz-hármas: ugyanannak a projektnek az üres templétje + kitöltött verziója + a forrás (ajánlat/költségvetés), amiből kitöltötték.
- [ ] (Opcionális) 1-2 **kisebb, részben szöveges** ajánlat-PDF az OCR-határ demójához (a 226 oldalas túl nagy az élő workshopra).
- [ ] Megerősítés, hogy az anonimizált tananyag-használat rendben van.
