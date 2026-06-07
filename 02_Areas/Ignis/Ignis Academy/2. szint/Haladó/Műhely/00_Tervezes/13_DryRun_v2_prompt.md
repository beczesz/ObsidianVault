---
title: "🎬 Dry-Run v2.0 indító prompt — friss sessionhoz"
date: 2026-05-13
author: Becze Szabolcs
status: active
description: "A v2.0 workshop dry-run indító promptja, amely egy új instructor-led és stáció alapú modell teszteléséhez szükséges instrukciók és értékelési kritériumok gyűjteménye. Kurzus-tervezők és oktatásfejlesztők számára készült a workshop aktualizációjának validálásához."
description_source: auto
description_hash: 07d6cee65409717e
id: 13b26711-a32b-4d5d-969e-0c3a8921689e
index_schema_version: 1
bdos_index: true
---
# 🎬 Dry-Run v2.0 indító prompt — friss sessionhoz

> **Hogyan használd:** Nyiss egy ÚJ Cowork sessiont, és illeszd be ezt a teljes promptot egyetlen üzenetként. A session az új **instructor-led + stáció** modell szerint fut le.

---

## A prompt (másold be ezt):

```
Te most egy szimulált dry-runt végzel a 4 órás "Ignis Academy Haladó AI
Workshop" v2.0 verzióján. Az új modell: az OKTATÓ kivetítve végigviszi
a narratívát és minden DEMO-t, a RÉSZTVEVŐK pedig stációknál (F1 után)
3-5 percig izolált mini-feladatokat csinálnak saját laptopukon.

A szerep: te egyszerre vagy
(1) az OKTATÓ aki az élő demókat futtatja,
(2) egy PÁROS aki minden stáció-feladatot megcsinál a saját Cowork-jén,
(3) a META-EVALUÁTOR aki értékeli az élményt és pontoz.

==== 1. LÉPÉS: KONTEXTUS BEOLVASÁSA ====

Olvasd el SORRENDBEN:

1. CLAUDE.md (Haladó/ gyökér)
2. Műhely/00_Tervezes/10_DryRun_kontext.md
3. Műhely/00_Tervezes/00_STORY_BOOK.md — különösen a v2.x bejegyzések
4. Tananyag/00_Bevezetes/Ceg_leiras_TransOffice.md

Miután ezeket beolvastad, írj egy 5-10 mondatos összefoglalót arról,
hogyan változott a workshop az v1.0-ról a v2.0-ra. Ez a megerősítés.

==== 2. LÉPÉS: OKTATÓI SEGÉDLET v2.0 BEOLVASÁSA ====

Olvasd el a `Műhely/00_Tervezes/09_Oktatoi_segedlet_v2.0.md`-t TELJES
egészében. Ez a perces forgatókönyv. Figyelj különösen:

- A 🎤 [OKTATÓ] vs ⏸ [STÁCIÓ] elválasztás minden fázisban
- A 23 prompt az Appendix A-ban (kódblokkokban)
- Az F5 stáció-pár (5.A katalogizáló + 5.B manuális idő-becslés) —
  ez egy új koncepció, kontraszt-pillanat az AI form-kitöltéssel
- F6 stáció: mindenki 3 saját variánst generál különböző stílusban

Miután elolvastad, írj 5 mondatban: mit gondolsz a stáció-modell
újdonságáról? Várhatóan hatékonyabb-e mint a v1.0-os arc?

==== 3. LÉPÉS: A WORKSHOP VÉGREHAJTÁSA ====

Munkamappád: `TransOfficeCopy/` (Haladó/ gyökerében — már elő van
készítve a 34 nyers fájllal).

SZABÁLYOK:
- Mindent a TransOfficeCopy/ mappán belül csinálj
- Hozz létre alfápákat: 01_ceg_attekintes/, 02_meeting_TODO/, ...
- Minden fázisra produkálj TÉNYLEGES OUTPUT-okat:
  * AZ OKTATÓI DEMO-k outputjait (a segédlet 🎤 [OKTATÓ] szekcióiban
    leírt promptokat futtatod)
  * A STÁCIÓ-k outputjait (a segédlet ⏸ [STÁCIÓ] szekcióiban leírt
    promptokat futtatod, mintha a párosod egyik tagja lennél)
- F1 outputjai: ceg_attekintes.md, CLAUDE.md, javasolt_mappa_struktura.md
  (az F1 prompt szerint — Appendix A.1)
- F6-nál generálj 3 teljes weboldal-variánst különböző stílusban

KÜLÖN FIGYELJ:
- Minden STÁCIÓ kimenetét külön mentsd: pl. F2 esetén
  `02_meeting_TODO/STACIO_2A_email_Eniko.md`
- Az OKTATÓI DEMO outputjait: pl. `02_meeting_TODO/DEMO_TODO_lista.md`,
  `DEMO_F4_PPT.pptx`, stb.

Kövesd a sorrendet: F1 → F2 → F3 → F4 → F5 → F6 → Zárás.

==== 4. LÉPÉS: META-JEGYZETEK MENET KÖZBEN ====

Minden fázis VÉGÉN (mielőtt a következőre mész) írj meta-jegyzetet
a `TransOfficeCopy/_DryRun_v2_jelentés/jelentes.md` fájlba:

## F[X] — [Fázis neve]

### Az OKTATÓI flow értékelése
[3-5 mondat: a demók sorrendje logikus? A "Mondom:" idézetek
természetesek? Egy oktatónak könnyen követhető?]

### A STÁCIÓ(K) értékelése
[3-5 mondat: a stáció-prompt működött a sajat Cowork-jén?
A 3-5 perces időkeret reális? Egy résztvevő csinálni tudná
F1 után, izoláltan? Mi a stáció valódi output-értéke?]

### Idő-realizmus
[Az oktatói segédlet ígért-e annyi időt amennyi tényleg kell?
Az F5 5.A + 5.B + DEMO össze 14 perc — összejön?]

### Új javítási ötletek (v2.1-hez)
[1-3 konkrét javaslat amit a v2.0-ra látva még finomítanál]

==== 5. LÉPÉS: VÉGSŐ PONTOZÁS ====

A 6 fázis után `TransOfficeCopy/_DryRun_v2_jelentés/pontozas.md`:

Pontozz minden fázist (Bevezető, F1, F2, F3, F4, F5, F6, Zárás)
ugyanazzal a 7 kritériummal mint az v1.0-ban, **PLUSZ** egy újjal:

1. Érthetőség
2. Új információ (Cowork-spec)
3. Hasznosság
4. Narratív illeszkedés
5. WOW-faktor
6. Hands-on érték
7. Realizmus
8. **ÚJ: Stáció-tisztaság** — a stáció(k) izoláltak? Egy résztvevő
   meg tudja csinálni F1 után anélkül hogy függne a páros előző
   tevékenységétől? (1-10)

Készíts ÖSSZEHASONLÍTÓ TÁBLÁT az v1.0-ás pontozással:
- v1.0 átlag fázisra
- v2.0 átlag fázisra
- különbség
- a legnagyobb javulások hol történtek?

Egy mondatos overall: érdemes volt a v2.0-os átdolgozás?

==== 6. SIKER-KRITÉRIUM ====

A v2.0 dry-run akkor sikeres ha:
- Minden 6 fázis outputjai megvannak (DEMO + STÁCIÓ külön mentve)
- F6 alatt 3 saját variáns generálva (különböző stílusban)
- _DryRun_v2_jelentés/jelentes.md tartalmazza minden fázis 4 alszekcióját
- _DryRun_v2_jelentés/pontozas.md 8 kritériummal + v1.0 vs v2.0 összevetéssel

==== INDULJ ====

Kezdd az 1. lépéssel. Olvasd el a kontext-fájlokat, AZUTÁN írd meg
az első összefoglalót. Onnantól haladj sorban.

Munkára!
```

---

## Mit változott v1.0-hoz képest

| Pont | v1.0 dry-run | v2.0 dry-run |
|---|---|---|
| Szerepek | Student + meta-evaluator | **Oktató + Páros + meta-evaluator** |
| Segédlet | v1.0 (240p, 70/20/10 nominal) | **v2.0** (230p, instructor-led + stációk) |
| Output-szét­választás | 1 mappa fázisonként | **DEMO_*.md + STACIO_*.md** külön mentve |
| F1 modell | Mindenki külön | **Ugyanaz** (változatlan) |
| F6 | 1 saját variáns | **3 saját variáns különböző stílusban** |
| Pontozási kritériumok | 7 | **8** (új: Stáció-tisztaság) |
| Plusz output | — | **v1.0 vs v2.0 összevetés tábla** |

## Várható kimenet

`TransOfficeCopy/_DryRun_v2_jelentés/` mappa:
- `jelentes.md` — minden fázishoz 4 alszekció (OKTATÓ flow / STÁCIÓ / idő-realizmus / javítási ötletek)
- `pontozas.md` — 8×8 tábla + v1 vs v2 összevetés

Plus minden fázis-mappában külön mentve:
- `DEMO_*.md/.pptx/.html` — amit az oktatói segédlet 🎤 [OKTATÓ] szekciója alapján gyártott
- `STACIO_*.md` — amit az ⏸ [STÁCIÓ] szekciók alapján gyártott

Ez alapján **konkrétan látni fogjuk:**
- A stációk valóban izoláltak-e
- A v2.0 átdolgozás megéri-e
- Mit kell még finomítani v2.1-ben

---

**Készült:** 2026-05-12 · **Verzió:** 1.0 (a v2.0 segédlet teszteléséhez)
