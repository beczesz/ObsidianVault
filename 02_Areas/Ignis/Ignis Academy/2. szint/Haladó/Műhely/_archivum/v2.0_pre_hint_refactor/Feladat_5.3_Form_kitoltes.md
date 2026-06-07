---
title: "Feladat 5.3 — Form-kitöltés AI-jal"
date: 2026-05-14
author: Becze Szabolcs
status: active
description: "Instructor demo ahol az AI 90 másodperc alatt kitölt egy 40 mezős EU-s pályázati formularyt az előző fázisok adataiból, szemléltetésként a 1,5 órás kézi munka helyett. A résztvevők figyelnek és a végén páros megbeszélésben értékelik az AI-alapú folyamatok ROI-ját."
description_source: auto
description_hash: 7f2231daf5765f1a
id: 07f14c46-ecad-44b3-9018-ea3d5e3b5b48
index_schema_version: 1
bdos_index: true
---
# Feladat 5.3 — Form-kitöltés AI-jal

> **Típus:** 🎤 OKTATÓI DEMO (a kivetítőről nézed) — A WOW-PILLANAT
> **Idő:** ~4 perc · **Hozzád tartozik:** csak figyelés + páros megbeszélés a végén

---

## Mit látsz a kivetítőn

Az 5.A stáció után **tudjátok** mit kér a form (kategorizálva, ~40 mező).
Az 5.B stáció után **tudjátok** mennyi idő kézzel (1,5-2 óra).

Most az oktató **élőben megmutatja** mit csinál a Cowork:

1. Beírja a promptot
2. **60-90 másodperc** alatt a Cowork **kitölti az összes mezőt** — az eddigi munkából (Plan de afaceri, Dosar complet, Data Completion Board)
3. **CSV** formátumban kiad egy mezőtartalom-listát
4. Az oktató **5-6 mezőt manuálisan átmásol** a form-mockup-ba (vizuálisan látható)

---

## A prompt amit az oktató használ

```
Tölts ki minden mezőt a formular_depunere_AFM_Mobilitate_Verde.html
formban. Használd a Plan de afaceri + Dosar complet + Data Completion
Board adatokat. Generálj egy CSV-t ami minden mezőhöz tartalmazza
az értéket.
```

---

## A nagy üzenet

> *„90 másodperc. A ti becslésetek 90 PERC volt. **60× gyorsabb. És hibátlanul.**"*

Ez a workshop egyik **legértékesebb tanulság-pillanata** — egy konkrét, mérhető ROI.

---

## Mire figyelj

- A Cowork **honnan veszi az adatokat?** (az előző fázisok kimenetéből, automatikusan)
- A kitöltött mezők **konzisztensek-e** egymással? (CUI, árbevétel, alkalmazottak szám — ugyanaz a szám mindenhol)
- Marad-e mező **kitöltetlen**? (5 mező: CNP, CI szám, banki igazolás, és 2 hatósági adat — ezek manuálisan kellnek)

---

## Tanulás

- **A kontextus-folytonosság** az AI „nem új info" — minden adat **már a Cowork memóriájában van** (F1 CLAUDE.md + F3 outputok + F4 Mihaela + F5 Plan de afaceri).
- **A „másodpercek vs órák" kontraszt** itt **mérhető** — egy valós KKV-vezető 1,5 órás munkáját **percekre** csökkentjük.
- **A 5 manuális mező** (CNP, CI, banki igazolás) **megtanítja**: az AI nem helyettesít mindent — **a hatósági / személyes / biztonsági mezők** mindig manuálisak.

---

## Otthoni elmélyítés

A saját pályázataiddal — bónusz feladatok:
- `Feladat_5.4_Bonusz_Plan_B.md` — Plan B-stratégia ha elutasítanak
- `Feladat_5.5_Bonusz_Form_validacio.md` — kitöltött form validáció

---

**Verzió:** 2.0 (instructor-led + stáció modell)
