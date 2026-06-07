---
title: "(Bónusz) Feladat 5.5 — Pályázati form ön-validáció"
date: 2026-05-14
author: Becze Szabolcs
status: active
description: "Bónusz feladat, amely egy Cowork AI asszisztens segítségével történő pályázati forma ön-validációt mutat be. A feladat célja a beadás előtti utolsó percekben az adatkonzisztencia, logikai hibák, formátumproblémák és hiányzó mezők kiszűrése színkódolt riport formátumban, valamint egy szigorú bírálói szimuláció futtatása."
description_source: auto
description_hash: 739066fbd8931320
id: 21546aaa-c37d-43f1-8ded-22c4302ab781
index_schema_version: 1
bdos_index: true
---
# (Bónusz) Feladat 5.5 — Pályázati form ön-validáció

## Szituáció

Az F5.3-ban kitöltöttük a pályázati formot — de a beadás előtti **utolsó 10 percben** mindig van egy stresszes pillanat: "tényleg jó minden? semmit sem felejtettem el? a szám-mezők stimmelnek?"

A pályázati portálok rugalmatlanok: ha egy mezőben elgépelsz, a rendszer **visszadob** és minden el van veszve. A Cowork **átnézi és ellenőrzi**, mielőtt a Submit gombot megnyomod.

## Feladat

Tedd a Cowork elé a kitöltött pályázati form-tartalmat (vagy egy export-ot a portálból), és kérj egy alapos ön-validációt.

## Hint

Add a Cowork-nek a kitöltött pályázati form-tartalmat, és kérd hogy játssza el a 'bíráló-előellenőr' szerepét: adatkonzisztencia, logikai check, hiányzó mezők, formátum-hibák. Piros/sárga/zöld jelzéssel + top 3 javítás.


## Elvárt kimenet

`palyazat_validacio_riport.md`:

### Összegzés
- 1. Adatkonzisztencia: 🟢 Zöld
- 2. Logikai ellenőrzés: 🟡 Sárga (lásd: alkalmazotti adó számítás)
- 3. Hiányzó mezők: 🟢 Zöld
- 4. Formátum: 🟡 Sárga (lásd: dátum formátum)
- 5. Eligibility: 🟢 Zöld
- 6. Mellékletek: 🔴 Piros (lásd: a form-ban 7M RON árbevétel, az Excel-ben 1.8M)

### Top 3 dolog BEADÁS ELŐTT

1. **🔴 KRITIKUS — Árbevétel eltérés:** Form szerint 7M, az Excel-ben 1.8M → ez egy elgépelés (7M valószínűleg 1.7M kellene)
2. **🟡 Logikai — Alkalmazotti adó:** A "salarii brutte" mező 350k RON, de a "contributii" csak 56k → ennek 100k körül kellene lennie. Ellenőrizd a Mihaela számokkal.
3. **🟡 Formátum — Dátumok:** "15.06.2025" és "15/06/2025" keverve. Pályázati portálok általában csak az egyiket fogadják el.

### Részletes jelentés mezőnként
[mezőrőll mezőre]

## Extra kihívás

Egy második prompt a validáció után:
> "Most simulálj egy szigorú bírálót aki MIND a 100 pontot meg akarná dobni rólunk. Mit kérdezne, mit kifogásolna? Adj 5 ilyen kifogást — hadd lássam mire kell felkészülnöm."

## Tipp

**Ezt a validációt soha ne hagyd ki** — minden 200 EUR-os pályázati tanácsadó ezt csinálja az utolsó fázisban, és **itt menthető meg az egész pályázat**. A Cowork ugyanezt 5 percben megcsinálja.

**Mindig** mentsd el a validáció riportot — ha a pályázatot esetleg elutasítják, ebből látod **hol vesztettünk**.

## Tanulás

- Az AI mint **harmadik szempár** — nem az aki kitölti, hanem aki utánanéz
- A leggyakoribb pályázati elutasítási ok: **technikai hiba** (formátum, ellentmondás, hiányzó mező) — NEM tartalmi
- A "bíráló-szimuláció" extra kihívás = elővételezett védelem
- Ez az **utolsó 5 perc** ami eldönti a pályázat sorsát, és most automatizálható
