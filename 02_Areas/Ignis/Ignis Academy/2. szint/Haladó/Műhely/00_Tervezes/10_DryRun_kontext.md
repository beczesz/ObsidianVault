---
title: "🎯 Dry-Run Kontext — kötelező olvasmány-lista"
date: 2026-05-14
author: Becze Szabolcs
status: active
description: "A 4 órás Haladó AI Workshop dry-run-jához szükséges olvasmányok és step-by-step útmutató. Először 5 percben el kell olvasni az öt kritikus fájlt, majd fázisonként haladni a tananyagokon, miközben egy TransOfficeCopy/ mappában generálj valódi outputokat."
description_source: auto
description_hash: a178e8f6fad6f890
id: 8958e08c-82c8-475e-a8a9-db428f930362
index_schema_version: 1
bdos_index: true
---
# 🎯 Dry-Run Kontext — kötelező olvasmány-lista

> **Cél:** Egy friss Cowork-sessionnek minden szükséges kontextus megadása ahhoz, hogy a 4 órás Haladó AI Workshop teljes folyamatát végig tudja vinni — a student és a meta-evaluator szerepében egyszerre.

---

## 1. ELŐSZÖR olvasd el (sorrend kötelező — 5 perc)

| # | Fájl | Miről szól | Miért fontos |
|---|------|------------|--------------|
| 1 | `CLAUDE.md` | Project root, struktúra-magyarázat | Tudd hol vagyunk a két-mappa rendszerben |
| 2 | `Tananyag/README.md` | A tanulói csomag áttekintése (v1.3) | A 6 fázis íve, mit fogsz csinálni |
| 3 | `Tananyag/00_Bevezetes/Ceg_leiras_TransOffice.md` | A fiktív cég teljes kontextusa | TransOffice, Márton, Béla bácsi, Mihaela, Enikő — kulcs-NPC-k |
| 4 | `Műhely/00_Tervezes/00_STORY_BOOK.md` | A workshop teljes narratívája | A "film" — milyen érzelmi ívben halad |
| 5 | `Műhely/00_Tervezes/09_Oktatoi_segedlet_v1.0.md` | **Step-by-step facilitator forgatókönyv** | Ez vezet végig — a sorrend, demó vs hands-on arány, átkötések |

**Megjegyzés:** A `09_Oktatoi_segedlet_v1.0.md` a legkritikusabb — ez tartalmazza a percre lebontott idővonalat és a konkrét promptokat. Az Appendix A (Prompt library) különösen fontos.

---

## 2. FÁZISONKÉNT, csak amikor odaérsz (a Tananyag/-ban)

### F1 — Rend a fájlok között
- `Tananyag/01_Ceg_megertes/README_F1.md`
- `Tananyag/01_Ceg_megertes/Feladat_1.1.md` (fő feladat: cég-áttekintés)
- `Tananyag/01_Ceg_megertes/Feladat_1.2.md` (CLAUDE.md generálás)
- *(A F1.3-F1.6 bónuszokat NE csináld a dry-runban — csak ha bőven van időd)*

### F2 — Rend a TODO-k között
- `Tananyag/02_Meeting_Productivity/README_F2.md`
- `Tananyag/02_Meeting_Productivity/Feladat_2.1_Meeting_transcript_feldolgozas.md`
- `Tananyag/02_Meeting_Productivity/Feladat_2.2_Followup_es_action_items.md`

### F3 — Pályázati elemzés
- `Tananyag/03_Dontes_Elemzes/README_F3.md`
- `Tananyag/03_Dontes_Elemzes/Feladat_3.1_Eligibility_check.md`
- `Tananyag/03_Dontes_Elemzes/Feladat_3.2_Adatvadaszat.md`
- `Tananyag/03_Dontes_Elemzes/Feladat_3.3_Data_Completion_Board.md`
- **Asset:** `Tananyag/03_Dontes_Elemzes/Palyazat_kiiras/Ghidul-solicitantului-Mobilitate-Verde-IMM-2026.md` (94 oldalas pályázati kiírás)

### F4 — Kommunikáció (multi-persona)
- `Tananyag/04_Legal_Szerzodes/README_F4.md`
- `Tananyag/04_Legal_Szerzodes/Feladat_4.1_Legal_szerzodes_check.md`
- `Tananyag/04_Legal_Szerzodes/Feladat_4.2_Penzugyi_email_Excel.md`
- `Tananyag/04_Legal_Szerzodes/Feladat_4.3_CEO_update_PPT.md`
- **„Beérkező" emailek** (a workshop dramatikus pillanataiban — Béla bácsi és Mihaela válaszol):
  - `Tananyag/04_Legal_Szerzodes/emails/bela_bacsi_valasz/email.md`
  - `Tananyag/04_Legal_Szerzodes/emails/mihaela_konyvelo_valasz/email.md` + `bilant_TransOffice_2024_2025.xlsx`

### F5 — Pályázat összeállítás
- `Tananyag/05_Kommunikacio_Email/README_F5.md`
- `Tananyag/05_Kommunikacio_Email/Feladat_5.1_Uzleti_terv.md`
- `Tananyag/05_Kommunikacio_Email/Feladat_5.2_Palyazati_csomag.md`
- `Tananyag/05_Kommunikacio_Email/Feladat_5.3_Form_kitoltes.md`
- **Referencia minta-output:** `Tananyag/05_Kommunikacio_Email/Plan_de_afaceri_TransOffice_AFM_2025.md`
- **Form mockup:** `Tananyag/05_Kommunikacio_Email/formular_depunere_AFM_Mobilitate_Verde.html`

### F6 — Web redesign
- `Tananyag/06_Marketing_Honlap/README_F6.md`
- `Tananyag/06_Marketing_Honlap/Feladat_6.1_Redesign_es_variaciok.md`
- `Tananyag/06_Marketing_Honlap/Feladat_6.2_Sajat_varians.md`
- **A régi weboldal:** `Tananyag/06_Marketing_Honlap/website/old/transoffice_old_website.html` (Comic Sans 2012-es rémálom)

---

## 3. AZ ASSET-MAPPA — itt dolgozz!

**Munkamappa:** `TransOfficeCopy/` (a Haladó/ gyökerében)

Ez egy frissen másolt példánya a kaotikus TransOffice fájloknak (~34 fájl). **Itt élj egy student módra:**
- Olvasd be a fájlokat a Cowork-be
- Generálj outputokat (Cowork artifact / .md / .docx / .html, ahogy a feladat kéri)
- A te outputjaidat mentsd a TransOfficeCopy/-on belül létrejövő alfanapokra:
  - `TransOfficeCopy/01_ceg_attekintes/`
  - `TransOfficeCopy/02_meeting_TODO/`
  - `TransOfficeCopy/03_palyazati_elemzes/`
  - `TransOfficeCopy/04_kommunikacio/`
  - `TransOfficeCopy/05_palyazat_csomag/`
  - `TransOfficeCopy/06_weboldal/`
  - `TransOfficeCopy/_DryRun_jelentés/` (a meta-jegyzeteid és pontozásod)

**Az eredeti TransOffice/-ot ne piszkold.** A Tananyag csak referencia.

---

## 4. HOGYAN GONDOLKODJ — két szerep egyszerre

### Szerep 1: STUDENT (résztvevő)
- Légy a fiktív Operations & Systems Manager
- Csináld meg amit a feladatok kérnek
- Ne csak válaszolj — **TÉNYLEGES OUTPUT-OKAT** hozz létre (.md, .docx, .html, .pptx)
- Az F6-nál **3 különböző weboldal-variánst** generálj (Modern / Klasszikus / Erdélyi)
- A bónusz feladatokat NE csináld meg (csak fő feladatok F1.1-F1.2, F2.1-F2.2, F3.1-F3.3, F4.1-F4.3, F5.1-F5.3, F6.1 a 3 variánssal + F6.2 maradhat)

### Szerep 2: META-EVALUÁTOR (a workshop tervezője)
- Minden fázis után **3-5 mondatos jegyzet:**
  - Mi volt **WOW** itt? (az élmény oktatói szemmel)
  - Mi nem ment olajosan? (technikai vagy narratív probléma)
  - Az oktató mennyit dolgozott vs. a tanuló mennyit? (becsült arány %-ban)
- A workshop végén: **pontozás 1-10-ig** 7 kritérium szerint (lásd alább)

---

## 5. PONTOZÁSI KRITÉRIUMOK (workshop végén)

Minden FÁZISra adj pontot (F1, F2, F3, F4, F5, F6 + Bevezető + Zárás) ezekhez:

| Kritérium | Mit néz | Skála |
|-----------|---------|-------|
| 1. Érthetőség | Egy résztvevő követheti? Nem túl bonyolult? | 1-10 |
| 2. Új információ | A Cowork-spec funkciókból mennyit mutat be? | 1-10 |
| 3. Hasznosság | Valós üzleti életbe transzferálható? | 1-10 |
| 4. Narratív illeszkedés | A film-íven hol vagyunk? Stimmel? | 1-10 |
| 5. WOW-faktor | "Hűha" élmény van? | 1-10 |
| 6. Hands-on érték | A tanuló tényleg dolgozik vagy csak néz? | 1-10 |
| 7. Realizmus | Egy valós cégnél így működne? | 1-10 |

**Átlag** a fázisra, **össze átlag** az egész workshopra.

---

## 6. AMIT NEM KELL OLVASNI (de tudd hogy ott van)

- `Műhely/00_Tervezes/02_ChatGPT szintézis...` — régi master plan, már beolvadt a Story Book-ba
- `Műhely/00_Tervezes/05_*`, `06_*` — régi tervezési doksik
- `Műhely/00_Tervezes/07_Versenytars_elemzes_ThrivenExus.*` — versenytárs-elemzés, nem releváns dry-run szempontjából
- `Műhely/00_Tervezes/08_HandsOn_javitas.md` — érdekes lehet ha kíváncsi vagy, de NE KÖVESD a végrehajtás során (a tananyagban még nincs beépítve)
- `Műhely/_archivum/` — régi verziók

---

## 7. SIKER-KRITÉRIUM

A dry-run akkor sikeres ha a végén van:
1. **6 fázis outputjai** a `TransOfficeCopy/0X_*/` mappákban
2. **3 weboldal-variáns** (modern, klasszikus, erdélyi) a `TransOfficeCopy/06_weboldal/`-ban
3. **`TransOfficeCopy/_DryRun_jelentés/jelentes.md`** — meta-jegyzetek minden fázisról
4. **`TransOfficeCopy/_DryRun_jelentés/pontozas.md`** — pontozás a 7 kritérium szerint

---

**Készült:** 2026-05-12 · **Verzió:** 1.0
