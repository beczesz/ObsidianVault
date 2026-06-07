---
title: "Idő-becslés AI nélkül — TransOfficeDryRun2.0 outputok"
date: 2026-05-14
author: Becze Szabolcs
status: active
description: "Egy Operations Manager által AI nélkül készített idő-becslés a TransOfficeDryRun2.0 projekt 29 outputjához, amely 6 funkcionális terület munkaóra-becsléseit tartalmazza: fájlrendezés 16 óra, TODO-kezelés 4 óra, pályázat-analízis 18 óra, kommunikáció 15 óra, pályázat-összeállítás 17"
description_source: auto
description_hash: d59b8fb9b197ca15
id: 8eb1759b-ddaf-49ce-b085-6c25c89e12c2
index_schema_version: 1
bdos_index: true
---
# Idő-becslés AI nélkül — TransOfficeDryRun2.0 outputok

> **Cél:** Egy kompetens Operations Manager AI nélkül (Office, Google, internet, saját szakmai tudás) mennyi munkaóra alatt készítené el ugyanezt a 29 outputot ugyanolyan minőségben?
> **Becslés-perspektíva:** Mid-szintű professzionista, NEM outsource (nem hív könyvelőt PPT-re, nem hív designert weboldalra)
> **Időegység:** munkaóra (1 munkanap = 8 munkaóra)
> **Megjegyzés:** „**ugyanolyan mélységig**" — vagyis a Plan de afaceri 8 fejezetes vázlat-szinten, nem a 40-oldalas pályázati submission-szinten

---

## F1 — Káoszból rendszer (34 fájl rendrakása)

| Output | Mit jelent manuálisan | Munkaóra |
|--------|------------------------|----------|
| 34 fájl áttekintése | Megnyitni minden xlsx/docx/txt/srt-t, érteni mit tartalmaz | 4-6 h |
| Kategorizálás + duplikátum-azonosítás + kuka | 3 ügyféllista összevetése, 2 duplikált meeting, 8 szemét | 2 h |
| `ceg_attekintes.md` (5-7 oldal strukturált) | Cég profilja + 8 alfejezet + 12 kockázat | 4-5 h |
| `CLAUDE.md` (~3-4 oldal) | Szervezeti tudástár, mint hosszú távú memória | 2-3 h |
| `javasolt_mappa_struktura.md` | Strukturált tree + 14 mappa indoklása | 1,5-2 h |
| Fájlok tényleges áthelyezése + backup | Mappázás, jelszókezelő-átvezetés | 0,5 h |
| **F1 ÖSSZ** | | **~16 h** (2 munkanap) |

**Kritikus megjegyzés:** A „**Béla bácsi-szál**" észrevétele (meeting transcript 41. mondat → bérleti szerződés) **kézzel könnyen kicsúszna**. A Cowork ezt **automatikusan** csinálja. Manuálisan ez egy „szerencse" pillanat — vagy a manager észreveszi (extra 1 h), vagy nem (későbbi időpontban kockázat).

---

## F2 — Rend a TODO-k között

| Output | Mit jelent manuálisan | Munkaóra |
|--------|------------------------|----------|
| Meeting transcript átolvasása + jegyzetelés | 7 perces meeting, 73 bemondás, RO+HU keverék | 1-1,5 h |
| 12 TODO + felelős + határidő + függőség | Strukturált prioritás + 4 blokkoló-azonosítás | 1,5-2 h |
| Béla bácsi-utalás felfedezése (40+ sornyi szövegből) | Manuálisan **gyakran kimarad** | 0,5 h |
| TODO-k beírása Trello/Asana/whatever-be | Manuális betűzés | 0,5 h |
| Follow-up email Enikőnek (kollegális, 4-5 mondat) | Fogalmazás + 2-3 javítási kör | 0,5 h |
| **F2 ÖSSZ** | | **~4 h** (fél munkanap) |

---

## F3 — Pályázati elemzés (94 oldalas PDF, románul)

| Output | Mit jelent manuálisan | Munkaóra |
|--------|------------------------|----------|
| 94 oldalas RO pályázati kiírás végigolvasása | Jogias-nyelv, figyelmes olvasás, jegyzetelés | **6-10 h** |
| Eligibility check 12 kritériumra (DEMO F3.1) | Minden kritériumhoz visszakeresés + indoklás + Grila ETF pontozási becslés | 3-4 h |
| 17 melléklet gap analysis (DEMO F3.2) | Inventory + kategorizálás + beszerzési útvonal | 2-3 h |
| Data Completion Board 24 tétel × 5 oszlop × 3 fázis (DEMO F3.3) | Strukturált projektterv-szerű tábla | 3-4 h |
| STÁCIÓ 3.A CR-08 (5 mondat indoklás) | Rövid analízis | 0,3 h |
| STÁCIÓ 3.B M-11 beszerzés (6 mondat folyamat) | Rövid folyamat-leírás | 0,5 h |
| **F3 ÖSSZ** | | **~18 h** (2-2,5 munkanap) |

**Kritikus megjegyzés:** Egy pályázatíró-tanácsadó óradíja 100-200 EUR — vagyis ez **~1.800-3.600 EUR-os** tanácsadói munka.

---

## F4 — Multi-persona kommunikáció

| Output | Mit jelent manuálisan | Munkaóra |
|--------|------------------------|----------|
| F4.1a Bérleti szerződés + cross-doc (top 5 kockázat + Béla bácsi-szál) | 4 oldal szerződés + **mind a 34 másik fájl visszanézése** keresztreferencia-vadászatra | 3-5 h |
| F4.1b Levél Béla bácsinak (magyar, 70 éves embernek) | Gondos megfogalmazás, 2-3 javítási kör | 0,7 h |
| STÁCIÓ 4.A Köszönő-válasz (5 mondat) | Rövid de érzelmileg súlyos | 0,3 h |
| F4.2a Email Mihaelának (RO, 5 pontos) | Kétnyelvű kompetencia szükséges | 1 h |
| F4.2b Bilanț Excel-elemzés (EBITDA + marzs + trend + 3 KPI) | Manuális Excel-számolás + értelmezés | 2-3 h |
| STÁCIÓ 4.B EBITDA margin | Egyszerű képlet | 0,1 h |
| F4.3 CEO PPT 6 slide (Forest&Moss paletta, hero, táblák, infografika) | **A PPT-design a legnagyobb tétel itt** | **6-10 h** |
| **F4 ÖSSZ** | | **~15 h** (~2 munkanap) |

**Kritikus megjegyzés:** A PPT-design 6-10 órás becslés **kompromittált minőséget** feltételez. Egy presentation specialist 1-2 napot tölt ugyanezzel egy referenciaszintű kivitelezésre.

---

## F5 — Pályázat összeállítás

| Output | Mit jelent manuálisan | Munkaóra |
|--------|------------------------|----------|
| F5.1 Plan de afaceri 8 fejezet (RO, 4-5 oldal vázlat) | Pályázatírási szakember 3-5 napja egy teljes 40-oldalas verzióra; **vázlat-szinten 8-12 h** | **9-12 h** |
| F5.2 23-tételes csomag-checklist | Strukturált inventory + felelősök + forrás | 2 h |
| STÁCIÓ 5.A Form-katalogizáló (55 mező × kategória × format) | A HTML-form végignézése + táblázat | 2 h |
| STÁCIÓ 5.B Manuális idő-becslés | Számolás + magyarázat | 0,3 h |
| F5.3 Form autofill CSV (55 mező × tényleges érték) | Adatok visszakeresése a CLAUDE.md + Plan de afaceri-ből + manuális betűzés | 1,5-2 h |
| **F5 ÖSSZ** | | **~17 h** (~2 munkanap) |

**Kritikus megjegyzés:** Egy professzionális pályázati Plan de afaceri **valódi pályázathoz** kb. 24-40 munkaórát igényel. Itt **csak a workshop-szinthez** közelít a becslés.

---

## F6 — Web redesign (4 teljes HTML)

| Output | Mit jelent manuálisan | Munkaóra |
|--------|------------------------|----------|
| DEMO modern HTML (~280 sor, hero + grid + green + team + form + footer, responsive) | Design + kódolás + tartalom + tesztelés | **8-12 h** |
| STÁCIÓ 1 — Klasszikus variáns | Custom typography + szín-koncepció + content adaptation | **8-12 h** |
| STÁCIÓ 2 — Erdélyi variáns | **HU+RO copywriting** + warm palette + decorative motifs | **10-14 h** |
| STÁCIÓ 3 — Zen variáns | Japán-minimalism filozófia + kanji-jelek + radikálisan más layout | **8-12 h** |
| **F6 ÖSSZ** | | **~32-40 h** (4-5 munkanap) |

**Kritikus megjegyzés:** Egy front-end designer **1 oldalra 1-2 napot szán**. Itt **4 különböző stíluskoncepcióban** dolgozó valaki: ~5 munkanap. Ez **a legnagyobb manuális tétel** a workshopban.

---

## Bevezető + Zárás (oktatói tartalom)

| Output | Munkaóra |
|--------|----------|
| Bevezető monológ + Márton-szituáció + film-metafora-előkészítés | 1,5 h |
| Zárás visszatekintés + „1 mondat" facilitáció + bónusz feladatok bemutatása | 1 h |
| **Meta ÖSSZ** | **~2,5 h** |

---

# 🎯 ÖSSZESÍTŐ TÁBLA

| Fázis | Munkaóra (AI nélkül) | Munkanap (8h) |
|-------|:--------------------:|:--------------:|
| Bevezető + Zárás | 2,5 h | 0,3 nap |
| F1 — Káoszból rendszer | 16 h | 2,0 nap |
| F2 — TODO-k | 4 h | 0,5 nap |
| F3 — Pályázati elemzés | 18 h | 2,3 nap |
| F4 — Multi-persona | 15 h | 1,9 nap |
| F5 — Pályázat összeállítás | 17 h | 2,1 nap |
| F6 — Web redesign | 35 h | 4,4 nap |
| **ÖSSZESEN** | **~108 munkaóra** | **~13,5 munkanap** |

---

## Mit jelent ez a workshop kontextusában?

| Mérés | Érték |
|-------|-------|
| AI nélkül (kompetens 1 fő, lineárisan) | **~108 munkaóra** (~2,7 munkahét) |
| AI-val (a 4 órás workshop alatt) | **4 munkaóra** (egy résztvevő szempontjából) |
| **Tömörítési arány** | **~27× gyorsabb** |

Vagyis amit egy ember **2,7 munkahét alatt** csinálna meg lineárisan és kompetensen — a **TransOffice fiktív Operations Manager szerepében** —, azt a workshop résztvevője **4 óra alatt megéli** (és **a kulcs-outputjait el is viszi**).

---

## Honest caveats (átláthatóság miatt)

1. **A 108 óra "kompetens mid-szintű"** — egy junior több időt kérne (~150-180 h), egy szenior tanácsadó kevesebbet (~70-90 h, de drágábban).
2. **Outsource esetén** a Plan de afaceri könyvelő/pályázatíró + a PPT consultant + a 4 weboldal designer ≈ 80-120 h **fizetett munka**, **2-3 hét naptári idővel** (függőség: ki ér rá), **összköltség 3.000-6.000 EUR** közti tartományban.
3. **A „minőség-mélység"** ami megjelenik a 29 outputban a workshop-szintje, NEM a végső submission-szintje — egy igazi AFM-beadásra 1,5-2× ennyi idő kell még a finomításra (hivatalos sablon-egyezés, jogi ellenőrzés, dupla ellenőrzés).
4. **Egy igazi pályázat-projekt** elapsed-time-ra (nem munka-órára) **5-10 munkanap** kell **AI nélkül**, mert sok a függőség (könyvelő, notár, beszállító-ajánlat). **AI-val 4-5 munkanap** elegendő, mert a strukturált outputok és emailek **azonnal készek**, csak a külső válaszokra kell várni.

---

**Készült:** 2026-05-13, a v2.0 dry-run kiegészítéseként

---

# 🧠 KIEGÉSZÍTÉS: Naptári idő (a koncentráció-limit figyelembevételével)

## Miért irreális a "108 munkaóra = 13,5 munkanap"?

Egy embernél a 8 órás munkanap **NEM 8 óra deep-work** — Cal Newport (Deep Work, 2016) és más kutatások szerint:

- **Napi 3-4 óra** a maximum mély-fókusz tudásmunkára
- A többi: email-tisztítás, beszélgetés, kávészünet, telefon, ebéd, *context switch recovery* (15-23 perc minden megszakítás után), és az este-fáradtság (a 6-8. órában a hatékonyság **40-60%-kal** esik)
- Kreatív/cognitív feladatra **2-3 mély-óra/nap** a realisztikus

Vagyis a 108 "tiszta munkaóra" valójában **annyi naptári nap, ahányszor 3-4 mély-órányi feladat tartozik benne** — és nem minden feladat ugyanúgy érzékeny a megszakításra.

---

## Fázisonkénti újrabecslés — deep-work intenzitás szerint

| Fázis | Munkaóra | Deep-work hányad | Tiszta deep-work | Naptári napszükséglet (4h deep/nap) |
|-------|:--------:|:----------------:|:----------------:|:-------------------------------------:|
| F1 — 34 fájl + 3 output | 16 h | 50% (sok rutin: mappázás, mentés) | 8 h deep | **2 nap** |
| F2 — TODO + email | 4 h | 70% (transcript-megértés) | 2,8 h deep | **1 nap** |
| F3 — 94 oldal RO pályázati kiírás | 18 h | **90%** (legalese-olvasás kemény fókusz) | 16 h deep | **4 nap** |
| F4 — Multi-persona (PPT + cross-doc + Excel + RO email) | 15 h | 75% (mix) | 11 h deep | **3 nap** |
| F5 — Plan de afaceri RO + form | 17 h | **90%** (RO kreatív írás + pénzügy) | 15 h deep | **4 nap** |
| F6 — 4 HTML weboldal | 35 h | 80% (kreatív + kódolás) | 28 h deep | **7 nap** |
| Bevezető + Zárás (oktatói) | 2,5 h | 70% | 1,8 h | 0,5 nap |
| **ÖSSZESEN** | **108 h** | átlag ~80% | **~83 h deep** | **~21-22 nap deep-work** |

---

## A naptári idő — több réteggel

### 1. Lineáris egy ember + reális deep-work limit
21-22 mély-fókuszú munkanap = **~4,5 naptári munkahét** = **~5-6 naptári hét** (hétvégékkel)

### 2. + Hétvégék, ünnepek, váratlan napok
Egy 4-6 hetes projektben átlagosan **1-2 nap kiesik** (betegnap, váratlan ügyfél-meeting, családi esemény, áramszünet, stb.)

### 3. + Külső függőségek
A workshop narratíva szerint **5 munkanap** alatt fut le minden, **DE** ez azért hihető, mert:

- A könyvelő (Mihaela) **48 órán belül válaszol** — valóságban gyakran 5-7 nap
- A notár (Munteanu) **3 napra van időpontunk** — valóságban 1-2 hét
- A 3 jármű-ajánlat (Renault / Maxus / Citroen) **3 napon belül érkezik** — valóságban 1-2 hét (különösen elektromos járművekre)
- Az ANAF cert. fiscal **azonnali** — ez tényleg pár óra ✓
- A Béla bácsi-válasz **2 nap** — családi viszonyban hihető ✓

**Realisztikusan + függőségekkel:** a 108 munkaórás projekt **2-3 hónap naptári időben** zárul **AI nélkül**.

### 4. + Minőség-romlás a project végére
A 21-22 deep-work nap **utolsó 25%-ában** a hatékonyság és minőség drasztikusan esik:

- F6 (az utolsó fázis) **a legnagyobb tételű** (7 nap deep) — épp amikor az ember **a legfáradtabb**
- A Plan de afaceri (F5) **3-4 revíziós kör** kell egy AFM-beadásra — minden kör +1-2 nap
- A kritikus fejezetek (eligibility, EBITDA-elemzés) **dupla-ellenőrzést** igényelnek

**Hatás:** további +20-30% extra idő → összesen **~130-145 munkaóra** "tisztességes minőségben" tartva.

---

## 🎯 Új összefoglaló — a realisztikus naptári kép

| Mérés | Érték |
|-------|-------|
| **Tiszta munkaóra** (eredeti becslés) | ~108 h |
| **Tiszta deep-work órák** (~80%) | ~83 h |
| **Deep-work napok** (4h/nap maximum) | ~21 nap |
| **+ Hétvégék + betegnapok + minőség-revízió** | ~5-6 naptári hét |
| **+ Külső függőségek (notár, könyvelő, ajánlatok)** | **2-3 hónap naptári idő** |
| **Realisztikus minőségben tartott összóra** | ~130-145 munkaóra |

---

## Mit jelent ez AI-val összevetve?

| Forgatókönyv | AI nélkül | AI-val (workshop) |
|-------------|-----------|-------------------|
| **Tiszta munkaóra a 29 outputra** | ~108 h | ~4 h (workshop alatt) |
| **Naptári idő** (függőségek nélkül) | 5-6 hét | **1 nap** |
| **Naptári idő** (függőségekkel: notár, könyvelő, ajánlatok) | **2-3 hónap** | **5-7 nap** (csak a külső válaszokra vár) |
| **Minőség a project végén** | romló (a fáradtság miatt) | konzisztens |
| **Hibakockázat** (kihagyott cross-doc, elnézett klauzula) | **magas** | alacsony |

**A kulcs-megfigyelés:** AI-val a *munkaóra-megtakarítás* drasztikus (27×), de **a naptári idő megtakarítása még drasztikusabb** (~12-20× függőségek nélkül; **~20-30× függőségekkel** együtt), mert:

1. **Eltűnik a koncentráció-limit** — AI 24/7 dolgozik, nem fárad
2. **Eltűnik a context-switch költség** — AI nem felejt el dolgokat ahogy más task-ra vált
3. **Csökken a függőség-várás** — AI a strukturált emaileket és checklisteket azonnal generálja, így az ember a fennmaradó időben a külső partnerekkel beszélhet
4. **Stabil minőség** — nem fáradtság-függő

---

## Honest caveat: ahol az AI **NEM** spórol időt

- **A notár megnyitása** — ez naptári idő, AI-val sem gyorsabb
- **A könyvelő válasza** — Mihaela-tól, AI nem helyettesíti
- **Az ANAF SPV portál böngészése** — manuális kattintgatás, ha nincs API
- **A jármű-szállító válasza** — emberi tárgyalás, AI csak az emailt írja meg

Vagyis a teljes pályázati projekt **AI-val sem 1 nap** — a strukturált tartalmi munka **igen 1-2 nap**, de **a beszerzések 1-2 hét**, és **a notár 3-7 nap**.

**Realisztikus AI-val:** 5-7 naptári nap.
**Realisztikus AI nélkül:** 2-3 naptári hónap.

A workshop **filmesített 4 órában** mutatja a 5-7 napos AI-val-projektet — ez a workshop **dramaturgiai trükkje**.

