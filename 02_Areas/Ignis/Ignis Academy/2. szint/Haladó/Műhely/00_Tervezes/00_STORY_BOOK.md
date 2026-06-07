---
title: "📖 STORY BOOK — Ignis Academy Haladó AI Workshop (HBC)"
date: 2026-05-14
author: Becze Szabolcs
status: active
description: "The Ignis Academy Advanced AI Workshop's narrative framework document, featuring a 4-hour guided experience where participants role-play an operations manager solving a real company's administrative chaos and urgent grant application deadline simultaneously. Includes character profiles, story structure across 8 acts, and teaching assets."
description_source: auto
description_hash: 5519a56a09fe6d57
id: b5406470-0cd1-4340-be8a-9ba74c3eb373
index_schema_version: 1
bdos_index: true
---
# 📖 STORY BOOK — Ignis Academy Haladó AI Workshop (HBC)

> **Ez a fő narratíva-dokumentum.** Minden session elején ezt olvasd be először.
> Ez a workshop **élő sztorija** — ahogy finomítjuk, ezt frissítjük.
>
> **Utolsó frissítés:** 2026-05-09
> **Verzió:** v1.0

---

## 🎬 A WORKSHOP MINT FILM

Ez nem tool training. Ez egy **4 órás guided future experience** — egy mini-film, amelyben a résztvevő (Te) átveszed egy fiktív cég Operations & Systems Manager szerepét, és egy kaotikus helyzetből egy beadott pályázatig viszed a vállalkozást.

**A film címe:** *„A Nap, Amikor A Káosz Rendszerré Vált"*

**Stílus:** Apple keynote × HBO mini-sorozat. Sok demo, kevés tutorial, sűrű narratíva.

**Szabály:** ne akadj fenn azon, hogy 10-15 ember mit csinál pontosan. Te vezeted a történetet — ők belépnek a checkpoint-okon (MICRO HANDS-ON), aztán visszaülnek és nézik a flow-t.

---

## 🎭 A SZEREPLŐK

| Név | Szerep | Karakter |
|-----|--------|----------|
| **Te** | Operations & Systems Manager (új) | A hős. Első napja a TransOffice-nál. Tud AI-t használni. |
| **Kovács Márton** | Ügyvezető (33) | Tech-érdeklődő, türelmetlen, eredményorientált. Bukarestben tanult, most Udvarhelyen. Pályázat-mániás. |
| **Szabó Enikő** | Könyvelő (45) | Precíz, csak a számlákkal foglalkozik. "Részmunkaidős, heti 3 nap." |
| **Bíró Attila** | Raktárvezető (50) | Megbízható, papíron dolgozik. "Mondjátok meg, megcsinálom." |
| **Kovács Ilona** | Volt admin (Márton anyja) | Visszavonult 2024-ben. Telefonon elérhető. "Azt hiszem abban a zöld mappában volt..." |
| **Béla bácsi (Béla Iosif)** | A telephely tulajdonosa | Családi ismerős, kis város. 2018 óta bérli a TransOffice a csarnokát. **Kulcsszereplő F4-ben.** |
| **Külsős könyvelő** | Pénzügyi szolgáltató | Csak emailen érhető el. **Kulcsszereplő F4-ben** (EBITDA tisztázás). |

---

## 🏢 A HELYSZÍN — TransOffice Trade SRL

- **Hol:** Székelyudvarhely, Hargita megye
- **Mi:** B2B irodai kellék kereskedelem (papír, toner, írószerek)
- **Mióta:** 2003 óta (Kovács István alapította)
- **Méret:** 12 alkalmazott, ~360k EUR éves árbevétel (2022 alapján)
- **Helyzet:** A 2024-es generációváltás (Márton átvette + Ilona visszavonult) → admin káosz
- **Telephely:** Calea Băieșenilor 22, Odorheiu Secuiesc — bérlet Béla Iosiftól, 2018-2028

---

## 🎯 A KÜLDETÉS

A film első percében Márton odadob neki egy laptopot egy mappával. **Egy igazi kihívás van:**

> "Tegnap este mondta valaki, hogy van egy AFM pályázat — elektromos autókra, 70-80% támogatás. **De már majdnem lezárták.** Ha bele tudunk csúszni, gyorsan kell. De a céget is rendbe kéne tenni közben — anyu visszavonult, semmi nincs a helyén."

Két párhuzamos szál fut:
1. **Rendszerépítés** (a káoszt rendezni)
2. **Pályázat beadás** (sürgető, konkrét, mérhető)

**A két szál a film végére ÖSSZEFONÓDIK** — a rendszer az ami lehetővé teszi a pályázat időben való beadását.

---

## 📋 A FILM 8 FELVONÁSA

### 🎬 NYITÁNY — Bevezető (30 perc)

**Mit látunk:**
- Az oktató személyes hookja: "február óta ezzel dolgozok, és néha megállok és azt mondom: ez nem lehet igaz."
- A "mi változott?" — nem új AI, hanem **új munkamódszer**: Cowork.
- A 3 pillér: AI + Markdown + Obsidian = mini operációs rendszer
- Az **eszterga metafora**: ChatGPT volt a gőzgép, a Cowork a precíziós szerszámgép.
- Záró ígéret: "Nem egy eszközt fogtok megtanulni. Egy érzést fogtok átélni: amikor az AI együtt dolgozik veled."

**Asset:** `Preparation/02_ChatGPT szintézis - Workshop struktúra.md` (a 8 blokkos bevezető script)

---

### 🎬 1. FELVONÁS — F1: Káoszból rend (20-25 perc)

**Helyzet (cold open):** Márton kávéval, Te a laptop előtt:
> "Ez lesz a géped. Rádobtam egy mappát mindennel. Igazából fogalmam sincs mi van benne — anyám rakta össze. Ha kérdésed van, szólj — de nekem 11-kor meetingem van."

**Te:** Megnyitod a `TransOffice/` mappát. **27 fájl**: 5 verzió ügyféllista, kéziratos cetlik, dupla szerződések, Ilona receptjei és unokafotója a "fontos dokumentumok" között.

**Akció:**
- Cowork beolvas mindent egyszerre
- Strukturált mappa-javaslat
- `CLAUDE.md` készítés (cégösszefoglaló + kontextus minden jövőbeni session-höz)
- Inkonzisztencia-azonosítás (3 ügyféllista, 3 különböző szám)

**Output:** `ceg_attekintes.md` + struktúrált mappa + CLAUDE.md

**WOW:** *"Ez 2 nap kézi munka volt — most 5 perc."*

**MICRO HANDS-ON (5 perc):** mindenki beolvas 3 fájlt és kér egy mini-summary-t.

**Átmenet F2-be:** *"A fájlok rendben vannak. De Márton most jött át — nem a fájlok a fő probléma, hanem hogy a meetingekből semmi nem marad meg."*

**Asset-ek:**
- `Tananyag/01_Ceg_megertes/TransOffice/` (27 kaotikus fájl)
- `Tananyag/01_Ceg_megertes/Feladat_1.1.md` ... `Feladat_1.6_Bonusz.md`

---

### 🎬 2. FELVONÁS — F2: Rend a TODO-k között (20-25 perc)

**Helyzet:** Márton ideges. Az AFM elektromos járműflotta-pályázat **már hónapok óta a radarjuk alatt volt**, de senkinek nem volt rá ideje rendesen ránézni. Most kiderül, hogy **vagy ezen a héten beadják, vagy lemaradnak** — a forrás kimerülőben, és a teljes apel április 30-án lezárul. Sürgős meeting Enikővel.

> **Márton:** *"Figyelj, tudom hogy ezt el kellett volna kezdeni 2 hónapja, de senki nem ért rá. Most vagy összerakjuk ezen a héten, vagy elfelejthetjük. 70-80% támogatás 2 elektromos autóra — ezt nem hagyhatjuk veszni."*

**Az asset:** `meeting_transcript_20250224.md` — egy kaotikus, valódi-stílusú beszélgetés.
- Márton: "Vannak pár autónk… 3? 4? Nem tudom pontosan."
- Enikő: "Pár? Ez már probléma."
- Sok TODO, kevés rendszer.
- **🌟 A meeting-ben Márton elhullat egy mondatot Béla bácsiról** (eladás-szándék) — *itt rejtjük el a F4 Legal-sztori csíráját*.

**Akció:**
- Productivity plugin aktiválás
- Transcript → strukturált TODO-k MENTVE (nem csak listázva)
- Új session megnyitása: "mik a nyitott feladataim?" → a Cowork tudja

**Output:** mentett TODO-k + follow-up emailek (Enikőnek, könyvelőnek)

**WOW:** *"A ChatGPT elfelejti. A Cowork emlékszik. Másnap is itt vannak a TODO-k."*

**Átmenet F3-ba:** *"A TODO-k megvannak. De a meeting-en kiderült: van egy 96 oldalas pályázati kiírás. Hogyan értünk hozzá?"*

**Asset-ek:**
- `Tananyag/01_Ceg_megertes/TransOffice/meetings/meeting_transcript_20250224.md` (a Béla bácsi-mondattal!)
- `Tananyag/02_Meeting_Productivity/Feladat_2.1.md` ... `Feladat_2.3.md`
- `Tananyag/02_Meeting_Productivity/README_F2.md`

---

### 🎬 3. FELVONÁS — F3: Adatvadászat + eligibility (25-30 perc)

**Helyzet:** Másnap reggel. Márton már 7-kor az irodában a kinyomtatott pályázati kiírással.
> "Egész éjjel ez járt a fejemben. Ha ennek nincs értelme, ne is kezdjünk bele. Ha tényleg pályázhatunk, futunk. Nézd meg gyorsan."

**Az asset:** `Ghidul-solicitantului-Mobilitate-Verde-IMM-2026.pdf` — fiktív, hiteles AFM pályázati kiírás. **94 oldal románul**, 12 eligibility kritérium + 17 kötelező melléklet + 6 nyilatkozat + pontozási rendszer + Cod Civil-szerű hivatkozások.

**Akció (3 lépés):**

#### F3.1 — Eligibility check (8-10p)
- Cowork beolvas: pályázati kiírás + CLAUDE.md (cégadatok)
- 12 kritériumra ✅/⚠️/❌ válasz indoklással
- **TransOffice eredmény:** simán befér 2 elektromos autóra, **DE** 4-5 ponton a könyvelővel kell egyeztetni (EBITDA, D/E ratio, de minimis, ANAF tartozás)
- **Hargita megye = +5 puncte bónusz** (zona deficit)
- Pontozási becslés: 65-75 pont (kell min. 60)

#### F3.2 — Adatvadászat / gap analysis (8-10p)
- 23 elemes táblázat: melléklet × van-e nálunk?
- 🟢 ~6 zöld, 🟡 ~11 sárga, 🔴 ~6 piros
- A 🔴-ek: M-11 járműflotta-leltár, M-13 üzleti terv, M-03 UBO közjegyző

#### F3.3 — Data Completion Board (7-10p)
- Strukturált akcióterv: dashboard + felelősök + Gantt + kritikus út + kockázatok
- 23 sor TODO, 8 felelős, 5 hetes ütemterv
- **Élő munkaeszköz** — másnap is itt lesz

**Output:**
- `eligibility_check.md`
- `mellekletek_gap_analysis.md`
- `data_completion_board.md`

**WOW:** *"3 nap munkája volt — most 30 perc. És a Cowork emlékszik mindenre."*

**Átmenet F4-be:** *"Megvan a tábla. Most jön a kemény része: 11 sárga + 6 piros TODO-ból emaileket kell írni, szerződést jogiagy ellenőrizni, CEO-nak prezit készíteni."*

**Asset-ek:**
- `Tananyag/03_Dontes_Elemzes/Palyazat_kiiras/Ghidul-solicitantului-Mobilitate-Verde-IMM-2026.md` + `.pdf` (94 oldal)
- `Tananyag/03_Dontes_Elemzes/Feladat_3.1_Eligibility_check.md` + `Feladat_3.2_Adatvadaszat.md` + `Feladat_3.3_Data_Completion_Board.md`
- `Tananyag/03_Dontes_Elemzes/README_F3.md`

---

### 🎬 4. FELVONÁS — F4: Kommunikáció + feldolgozás (30-35 perc) ✅ ASSETEK + FELADATLEÍRÁSOK KÉSZ

**Helyzet:** A Data Completion Board megvan. Most cselekszünk.

**3 sub-flow párhuzamosan / sorban:**

#### 4.A — Pénzügy: könyvelő-email + EBITDA tisztázás
- A Data Board szerint a 4-5 könyvelő-igényelte ponthoz emailt kell írni
- Cowork generál egy email-tervezetet a külsős könyvelőnek (mérleg + EK 2023-2024 + EBITDA + D/E ratio)
- Workshop manipuláció: a könyvelő válaszol Excel-mellékletekkel
- AI elemzi az Excel-eket → eligibility-checklist 4-5 pontja kipipálva
- **Plot twist:** a 2024-es EBITDA negatív, de a 2023-as pozitív → EGY pozitív év elég → ✓ megfelel

**Status:** 🚧 narratíva tervezve, asset-ek és feladatleírás még nem

#### 4.B — Legal: bérleti szerződés Cowork cross-doc check ✨ KIDOLGOZVA
- A Data Board szerint a M-16 (Telephely) **🟢 zöld** — bérleti szerződés OK
- DE: a Cowork (Legal plugin) mélyebb ellenőrzést végez
- **Cross-document felfedezés:**
  - Beolvas: `szerzodes_chirie_TransOffice_2018.docx` → Locator: Béla Iosif
  - Beolvas: `meeting_transcript_20250224.md` → Márton elhullatott megjegyzés Béla bácsi eladási szándékáról
  - Cross-check: AFM kiírás 5.1.1.7 → 5 év stabilitás kell
  - **Riasztás:** lehetséges kockázat
- Cowork tisztázó email-tervezet → résztvevő küldi
- Workshop manipuláció: Béla bácsi 2 nap múlva válaszol (`raspuns_bela_iosif_2025-02-26.txt`):
  - "A Calea Băieșenilor 22 családi tulajdon, NEM eladásra"
  - "Felajánlom a contract prelungire 2035-ig + közjegyzői declarație"
- **Eredmény:** nem kell módosítani a szerződést, de van EXTRA biztosíték

**Status:** ✅ asset-ek elkészültek, feladatleírás még nem
**Részletes narratíva:** `Preparation/06_F4_narrativa_legal_plugin.md`

#### 4.C — CEO update: 5-slide PPT Mártonnak
- Az eligibility + gap + Cowork-felfedezések összefoglaló
- Cowork generál egy 5 slide-os PPT-t (template alapján)
- Slide-ok: helyzet / döntés / kockázatok / akcióterv / következő lépések

**Status:** 🚧 narratíva tervezve, asset-ek és feladatleírás még nem

**WOW az F4 egészéhez:** *"Egy munkanap alatt a Cowork 4 emailt fogalmazott, 1 jogi kockázatot felfedezett, 1 PPT-t összerakott. Egy ember 1 hét alatt csinálná."*

**Átmenet F5-be:** *"Az adatok megvannak. A jogi tisztázás megvan. Most jön az összerakás."*

**Asset-ek (eddig):**
- ✅ `Tananyag/01_Ceg_megertes/TransOffice/szerzodes_chirie_TransOffice_2018.docx` (4 oldal)
- ✅ `Tananyag/01_Ceg_megertes/TransOffice/email_exportok/raspuns_bela_iosif_2025-02-26.txt`
- 🚧 könyvelő válasz-email + Excel mellékletek (mérleg 2023-2024)
- 🚧 PPT template (5 slide)

---

### 🎬 5. FELVONÁS — F5: Pályázat összeállítás + beadás (30-35 perc) ✅ ASSETEK + FELADATLEÍRÁSOK KÉSZ

**Helyzet:** Az adatok megvannak. Az M-13 üzleti terv a legnagyobb tétel.

**Akció:**
- Cowork generál: M-13 üzleti terv (8 kapitulus, az Anexa 6 sablont követve)
- Cowork generál: M-7 Macheta financiară (5 foaie, az Anexa 7 sablont követve)
- Cowork generál: M-13 Plan de înnoire a parcului auto (Anexa 13)
- Submission package: PDF konszolidáció
- Form kitöltés MySMIS-ben (DEMO — esetleg Chrome MCP-vel)

**WOW (a film WOW BLOKKJA):** *"AI tölt ki egy űrlapot magától a böngészőben. A telephelyi információkat ismeri, a CUI-t ismeri, az üzleti tervet csatolja."*

**Asset-ek (kell):**
- 🚧 MySMIS portál mockup (HTML vagy screenshot sorozat)
- ❌ kitöltött Plan de afaceri minta (a 8 kapitulus alapján)
- ❌ kitöltött Macheta financiară minta (Excel)

---

### 🎬 6. FELVONÁS — F6: Web redesign (25-30 perc) 🚧 ASSET KÉSZ, FELADATLEÍRÁSOK HIÁNYOZNAK

**Helyzet:** A pályázat be van adva. Várakozás közben Márton: *"A weboldalunk 2012-es. Tényleg kínos."*

**Az asset:** `transoffice_old_website.html` — egy "klasszikus" 2012-es vállalati oldal (Comic Sans, animált GIF-ek, "Best viewed in IE6", táblázatos layout).

**Akció:**
- Cowork elemzés: "Mi a baj a régi oldallal?"
- 3 design variáns: modern / klasszikus / "erdélyi" (vidéki-meleg)
- HTML generálás
- Pályázati info beillesztése (új flotta = új kommunikációs üzenet)

**WOW (vizuális payoff):** *"5 perc alatt 3 weboldal, mind működő, mind másféle."*

**Hands-on:** mindenki lefuttat egy saját variánst.

**Asset-ek (kell):**
- ❌ Régi TransOffice weboldal HTML (kínosan retro)
- ❌ 2-3 ihletkép modern weboldalakhoz (opcionális)

---

### 🎬 EPILÓGUS — Zárás (10-15 perc)

**Reflexió:**
- "Mit csináltunk az elmúlt 4 órában? Megértettétek, rendszereztétek, döntéseket hoztatok, kommunikáltatok, **és egy pályázatot beadtatok.**"
- Kontraszt: *"Ez normál esetben napok vagy hetek lett volna."*

**Személyes bizonyíték:**
- Az oktató: "februárban kezdtem így dolgozni... és néha megállok és azt mondom: ez nem lehet igaz."

**A mém:** metró-videó AI-analógiával: *"Nyilván nem ő tolja a metrót. De pont így érződik."*

**Záró ígéret:**
- *"Nem lettetek varázslók. Csak kaptatok egy rendszert ami megsokszorozza az erőtöket."*

---

## 🎨 NARRATÍVA-ÍVEK ÁTKAPCSOLÁSAI

### A "Béla bácsi" sztori — több fázis kapcsolata

| Fázis | Mi történik a Béla bácsi szállal? |
|-------|-----------------------------------|
| F1 | A bérleti szerződés bekerül a kaotikus mappába (rendezve, de nem kiemelt) |
| F2 | A meeting transcript-ben Márton elhullat egy mondatot Béla bácsi eladási szándékáról |
| F3 | A Data Completion Board-on M-16 zöld (telephely OK) — felszínes ellenőrzés |
| **F4 (Legal)** | **🌟 A Cowork cross-doc analízise felfedezi a kockázatot, tisztázó email, Béla bácsi válasz** |
| F5 | Béla bácsi declarație notarială bekerül a submission package-be |

### Az "EBITDA" sztori

| Fázis | EBITDA állapot |
|-------|----------------|
| F1 | Ilona-féle eves_jelentes_2022.xlsx megtalálva (de csak 2022-ig) |
| F2 | Enikő utal: "az idei… hát…" — adatok hiányoznak |
| F3 | Eligibility check ⚠️ sárga: "könyvelő szükséges" |
| **F4 (Pénzügy)** | **🌟 Email a könyvelőnek → válasz Excel mellékletekkel → AI elemzés → eligibility ✅** |

---

## 📁 ÉLŐ ASSET TÉRKÉP

### Készen vannak ✅ (v1.5 — mappastruktúra-átszervezés után)

```
Tananyag/                                       ← ZIP-elhető tanulói csomag
├── README.md                                   ← v1.0 verzió + leírás
├── 00_Bevezetes/
│   └── Ceg_leiras_TransOffice.md
├── TransOffice/                                ← Rootba költöztetve (volt: 01/TransOffice_Admin/)
│   ├── meetings/meeting_transcript_20250224.md ← Béla bácsi mondat itt
│   ├── szerzodes_chirie_TransOffice_2018.docx  ← F4 asset
│   ├── email_exportok/raspuns_bela_iosif_2025-02-26.txt
│   └── ... (27+ kaotikus fájl)
├── 01_Ceg_megertes/                            ← csak feladatleírások
│   └── Feladat_1.1.md ... Feladat_1.6_Bonusz.md
├── 02_Meeting_Productivity/
│   ├── README_F2.md
│   └── Feladat_2.1 ... 2.3.md
├── 03_Dontes_Elemzes/
│   ├── README_F3.md, Feladat_3.1 ... 3.3.md
│   ├── Palyazat_kiiras/                        ← 94 oldalas pályázati kiírás MD+PDF
│   └── Pelda_outputok/                         ← 3 minta-output
├── 04_Legal_Szerzodes/
│   ├── README_F4.md, Feladat_4.1, 4.2, 4.3.md
│   └── emails/{bela_bacsi_valasz, mihaela_konyvelo_valasz}/
├── 05_Kommunikacio_Email/
│   ├── README_F5.md, Feladat_5.1, 5.2, 5.3.md
│   ├── Plan_de_afaceri_TransOffice_AFM_2025.md (260 sor)
│   ├── Dosar_complet_AFM_Mobilitate_Verde_2025.md (114 sor)
│   └── formular_depunere_AFM_Mobilitate_Verde.html (1530 sor)
└── 06_Marketing_Honlap/
    └── website/old/                            ← 4 menü-oldal ANAF design-rendszerrel
        ├── index.html (Acasă), despre.html, produse.html, servicii.html
        └── design-system/anaf-style.css
```

```
Műhely/                                         ← Fejlesztői backstage (NEM kerül zip-be)
├── README.md
├── 00_Tervezes/                                ← Volt: Preparation/
│   ├── 00_STORY_BOOK.md (ez a fájl)
│   ├── 01_Logisztika...md, 02_ChatGPT_szintezis...md, 03_Jelen_beszelgetes...md,
│   │   04_Feladat 1...md, 05_ChatGPT_szintezis_v0.3...md
│   ├── 06_F4_narrativa_legal_plugin.md
│   └── 07_Versenytars_elemzes_ThrivenExus.md (+pdf)
├── 03_Dontes_Elemzes/Palyazat_kiiras_BUILD/    ← Python build-szkriptek
├── 04_Legal_Szerzodes/Szerzodes_BUILD/         ← docx-js generálás
└── 06_Marketing_Honlap/
    ├── website_design_source/                  ← ANAF CSS bundle + design-system source
    └── _archive_v1_Comic_Sans/                 ← első retro verzió archív
```

### Kell még 🚧

- Prompt library (egységes gyűjtés F1-F6)
- Próba-futtatás (saját mock workshop)
- F4 CEO PPT minta-fájl (.pptx) generálás

---

## 🎚️ DELIVERY DESIGN — FILMSZERŰ HOZZÁÁLLÁS

### Arányok (a v0.3 alapján)

| Mit | Arány |
|------|------|
| Te (oktató) demózol filmesen | **70%** |
| Közös micro hands-on (5 MUST HAVE checkpoint) | **20%** |
| Szabad próbálgatás | **10%** |

### 5 MUST HAVE hands-on pillanat

| # | Mikor | Mi | Mit éreznek |
|---|------|----|-------------|
| 1 | F1 | Első prompt 3 fájlra | "wow, működik" |
| 2 | F2 | Meeting summary | "wow, érti" |
| 3 | F3 / F4 | Excel insight | "wow, elemzi" |
| 4 | F5 | Form autofill | "wow, operál" |
| 5 | F6 | Web variánsok | "wow, kreál" |

### Checkpoint pedagógia

Minden fázisnál:
1. **WOW hullám** (60-70%) — Te demózol
2. **MICRO HANDS-ON** (20-25%) — Ők kipróbálnak EGY dolgot
3. **FLOW tovább** (5-10%) — Te haladsz, nem várod be a leszakadókat

---

## 🛤️ KIDOLGOZÁSI ÚTITERV

| Lépés | Mi | Státusz |
|-------|-----|---------|
| 1 | Master plan + filozófia | ✅ kész (`02_*` + `05_*`) |
| 2 | Bevezető + zárás script | ✅ kész |
| 3 | F1 asset-ek + feladatleírások (27 fájl + 6 feladat) | ✅ kész |
| 4 | F2 asset-ek + feladatleírások (urgency-narratíva frissítve) | ✅ kész |
| 5 | F3 asset-ek + feladatleírások (94 oldal pályázati kiírás MD+PDF) | ✅ kész |
| 6 | F3→F4 átmenet — 3 minta-output szimulálva (`Pelda_outputok/`) | ✅ kész |
| 7 | F4 README + 3 feladatleírás (Legal + Pénzügy + CEO) | ✅ kész |
| 8 | F4 asset-ek (Legal — Béla bácsi: szerződés + transcript + válaszemail) | ✅ kész |
| 9 | F4 asset-ek (Pénzügy — Mihaela könyvelő válaszemail + bilanț Excel) | ✅ kész |
| 10 | F4 asset-ek (CEO sub-flow — PPT generálás minta) | 🚧 finishing |
| 11 | F5 README + 3 feladatleírás (üzleti terv + csomag + form) | ✅ kész |
| 12 | F5 asset: Plan de afaceri (~260 sor románul) | ✅ kész |
| 13 | F5 asset: Dosar complet checklist (~114 sor) | ✅ kész |
| 14 | F5 asset: formular_depunere HTML (~1530 sor, MySMIS-mockup) | ✅ kész |
| 15 | F6 asset: régi 2012-es weboldal HTML (~802 sor, kínosan retro) | ✅ kész |
| 16 | F6 README + feladatleírás (analízis + 3 design variáns + új HTML) | 🚧 következő |
| 17 | Prompt library (egységes gyűjtés F1-F6) | ❌ |
| 18 | Próba-futtatás (saját mock workshop) | ❌ |
| **MELLÉKLET** | Versenytárs-elemzés (ThriveNexus) + beárazási javaslat | ✅ kész (PDF+MD) |

---

## 📝 FRISSÍTÉSI SZABÁLYOK

**Mikor frissítsük ezt a dokumentumot:**
- Új asset készül
- Új narratíva-elem (mint a Béla bácsi sztori)
- Egy korábbi ötlet elvetésre kerül (pl. az Art. 8.3 klauzula a F4-ben)
- Új sub-flow vagy fázis-átstrukturálás
- A delivery time-budget változik

**Hogyan frissítsük:**
1. A vonatkozó felvonás (Act) leírását módosítjuk
2. Az ÉLŐ ASSET TÉRKÉP-et frissítjük
3. A KIDOLGOZÁSI ÚTITERV státusát frissítjük
4. A versionhistory-be (alul) egy sort beírunk

---

## 📜 VERZIÓ-ELŐZMÉNYEK

| Dátum | Változás |
|-------|----------|
| 2026-05-09 | **v1.0** — Story Book létrehozva. Bele került az F1-F3 teljes narratíva (kész állapotból), az F4 Legal-sub-flow (új), valamint a 4-6 fázis tervezett vázai. |
| 2026-05-09 | **v1.1** — F2 felvonás módosítva (urgency-narratíva: 'meg vannak csúszva, ezen a héten kell beadni'). Meeting transcript intro frissítve, hogy 2 hónapja a radarjuk alatt van a pályázat. |
| 2026-05-09 | **v1.2** — F3→F4 átmenet szimulálva: 3 minta-output létrehozva a `Pelda_outputok/` mappában (eligibility_check.md, mellekletek_gap_analysis.md, data_completion_board.md). A 12 eligibility-kritériumból 10 ✅ és 2 ⚠️ (4.A pénzügy + 4.B telephely) — pont az F4 indítási pontja. |
| 2026-05-09 | **v1.3** — Versenytárs-elemzés (ThriveNexus Claude Mastery) készült el (PDF). Pozicionálás: nem ugyanaz a szegmens — beárazási javaslat 30.000 RON / HBC csoport. |
| 2026-05-12 | **v1.4** — F6 weboldal-asset elkészült (régi 2020-as TransOffice site ANAF SPV designjával): 4 menü-oldal (Acasă, Despre noi, Produse, Servicii), saját design-system. |
| 2026-05-12 | **v1.5** — MAPPASTRUKTÚRA-ÁTSZERVEZÉS: Tananyag/ (zip-elhető tanulói csomag) és Műhely/ (fejlesztői backstage) szétválasztva. TransOffice/ rootba költöztetve. CLAUDE.md frissítve a struktúra magyarázatával. README.md hozzáadva mindkét mappához. |
| 2026-05-12 | **v1.7** — F6 weboldal-csere: a Comic Sans-os retró verzió visszahozva a Tananyag/-ba (jobban illik a film-narratívába, a kontraszt erősebb). Az ANAF SPV-stílusú 4-oldalas verzió a Műhely _archivum/_v2_ANAF_SPV/ alá került. F6.1 + F6 README újra-frissítve a Comic Sans jellemzőkre. |
| 2026-05-12 | **v1.6** — Dry-run szimuláció + 12 probléma javítása: F2.3 archívba, F2.2 átnevezve, F3.1+README hibás fájl-hivatkozás javítva, „AFM Electromobil Plus"→„AFM Mobilitate Verde" mindenhol, „12 oldal"→„94 oldal" konzisztencia, F1.1+F1.6 digitalizációs→elektromos járműflotta narratíva, F2 README+F2.1 urgency-narratíva v1.5-höz igazítva, F1 README létrehozva, cégleírásban Székelyudvarhely (Odorheiu Secuiesc) kettős név, Tananyag README v1.1. |
| 2026-05-12 | **v1.4** — Felfedezve hogy egy korábbi sessionben már elkészült: az F4 teljes README + 3 feladatleírás, Mihaela könyvelő válaszemail + bilanț Excel (EBITDA számítással), F5 teljes README + 3 feladatleírás + 260 soros Plan de afaceri + Dosar complet checklist + 1530 soros MySMIS formular-mockup HTML, F6 802 soros régi 2012-es weboldal Comic Sans-ban. Tehát csak az F6 README + feladatleírások hiányoznak még. Story Book frissítve a valós helyzetre. |
| 2026-05-12 | **v1.8** — Bónusz feladatok kidolgozva F2-F6 minden fázishoz: F2 (3 db), F3 (4 db), F4 (4 db), F5 (4 db), F6 (3 db) — összesen 18 új otthoni gyakorló feladat. Mindegyik fázis README frissítve a LIVE/OTTHON jelöléssel. Hands-on érték növelő javaslat-dokumentum létrehozva (Műhely/00_Tervezes/08_HandsOn_javitas.md) az F2.2, F4.3 és F5.3 megerősítésére. Tananyag README v1.3-ra frissítve. |
| 2026-05-12 | **v1.9** — Meeting transcript v2.0 (színdárab-formátum): a `meeting_transcript_20250224.md` újraformázva 9 időkódolt jelenetre (10:15 → 10:55), karakterek nagybetűsen (MÁRTON, ENIKŐ), színészi instrukciók dőlt zárójelben, felolvasói útmutató a végén. Tartalom 99% megőrizve, plusz: Mihaela neve explicit, „új ember = Operations Manager” egyértelműsítve. Korábbi v1.0 archiválva: `Műhely/_archivum/02_Meeting_Productivity/`. |
| 2026-05-12 | **v2.0** — Meeting transcript SRT formatum (AI transcribe szimulacio): `meeting_transcript_20260825.srt` keszult, 73 bemondas, ossze 7 perc, csak Speaker A (Marton) / Speaker B (Eniko), minden meta info nelkul. Idobelyegek 00:00:02 -> 00:07:00. A .md valtozat is megmarad (felolvasasra v2.0). |
| 2026-05-12 | **v2.1** — Transcript fajl-szervezes: csak az .srt marad a Tananyagban (AI-feldolgozasra), a .md (felolvasasi) atkerult Muhely/02_Meeting_Productivity/-be. Szinezett PDF generalva (Speaker A kek #1565c0, Speaker B piros #c62828, csak labelek szinesek), 5 oldal, A4, nyomtathato. Build script + HTML preview a Muhely/02_Meeting_Productivity/srt_to_pdf_BUILD/-ben. |
| 2026-05-12 | **v2.2** — Dry-Run elokeszitese friss sessionhoz: TransOfficeCopy/ munkamappa letrehozva a Halado/ gyokereben (34 nyers fajl bemasolva a kaotikus TransOffice-bol). Ket uj tervezesi doksi: 10_DryRun_kontext.md (olvasmany-lista a sessionnek), 11_DryRun_prompt.md (a copy-paste-elheto indito prompt). A friss session feladata: STUDENT + META-EVALUATOR egyben, 6 fazis outputjai + 3 weboldal variáns + jelentes + pontozas 7 kriterium szerint. |
| 2026-05-12 | **v2.3** — Paros-mod koncepcio bevezetese F1-tol: 2 fo/pad, mindenki sajat laptopon, felvaltva pilot/navigator szerep F2-F6-ban. F1 = mindenki sajat laptopon parhuzamosan ugyanazt a prompt-ot futtatja. F1 ujratervezve v2.0-ra: 1 unified feladat (Feladat_1.1.md), copy-paste prompt kodblokkban, 3 output (ceg_attekintes.md + CLAUDE.md + javasolt_mappa_struktura.md). Regi F1.2 archivalva (osszeolvad F1.1-be). README_F1 v2.0. |
| 2026-05-12 | **v2.4** — F1.1 prompt akciokozpontu atirasa (v2.1): a hosszabb, diagnosztikus prompt helyett 5 lepeses, baratsagos prompt amit kezdok is meg tudnak ertheni. A Cowork nem csak elemzi, hanem ténylegesen rendet rak (backup, Kuka mappa, atrendez, kivonat, CLAUDE.md). 'Mit nem szabad' lista eltavolitva (nem tudunk semmit a fileokrol elore). Feladat_1.1.md 196 sor -> 142 sor. |
| 2026-05-12 | **v2.5** — Oktatoi segedlet v2.0: instructor-led + stacio modell. Az oktato kivetitve vegigviszi a narrativat es a demokat; a resztvevok F1 utan stacionkent 3-5 percig izolalt feladatokat csinalnak sajat laptopjukon. F1 kivetel (mindenki egyszerre dolgozik). Uj idoosztas: Bev 22p, F1 25p, F2 25p, F3 30p, F4 37p, F5 35p, F6 18p, Zaras 13p. Uj F5 stacio-par: form-katalogizalo + manualis ido-becsles → kontraszt-pillanat. 23 prompt egy helyen az Appendix A-ban. v1.0 archivalva. |
| 2026-05-12 | **v2.6** — F2-F6 Feladat-fajlok atalakitva a v2.0 stacio-modellre. Minden Feladat_X.X.md mostantol egyertelmuen jelolt [OKTATOI DEMO] vagy [STACIO] tipus, valamennyi STACIO copy-paste prompttal kodblokkban. F5 specialis: az 5.1 es 5.2 atalakult form-katalogizalo + idobecsles parra (a Plan de afaceri es Csomag-checklist most oktatoi DEMO). F6.1 = 3 sajat varians (mindenki). README-k frissitve a v2.0 stacio-jelolesre. Tananyag README v2.0. Backup: Muhely/_archivum/F2_F6_v1.0/. |
| 2026-05-14 | **v2.7** — Kotelezo vs opcionalis tagolas: a 4 DEMO-fajlhoz (F2.1, F3.3, F4.3, F5.3) hozzaadva 'Otthoni valtozat' szekcio teljes copy-paste prompttal. A 22 bonusz fajlbol eltavolitva a 'Javasolt prompt' kodblokk, helyette 1-2 mondatos 'Hint' szekcio. Az opcionalis feladatok igy mar inkabb kiserletezesi keret, nem mechanikai prompt-masolas. |


