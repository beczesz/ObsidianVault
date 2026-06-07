---
title: "F5.2 — Pályázati csomag összeállítása"
date: 2026-05-13
author: Becze Szabolcs
status: active
description: "Útmutató egy 23 tétel alapján teljes pályázati csomag összeszedéséhez és ellenőrzéséhez Claude segítségével, amely valós idejű státuszellenőrzést végez és azonosítja a hiányzó vagy folyamatban lévő dokumentumokat. A projektmenedzsment folyamatban az utolsó szakasz a legkritikusabb a beadás előtt."
description_source: auto
description_hash: d1b5926d5d1fc499
id: 910b2db0-3428-4d7e-8c1d-143dde47bbb6
index_schema_version: 1
bdos_index: true
---
# F5.2 — Pályázati csomag összeállítása

## Kontextus
A Data Completion Board 23 tételt tartalmaz. Az F4-ben a kritikus elemek tisztázódtak (Béla bácsi ✓, könyvelő adatok ✓). Most össze kell rakni az egészet egyetlen, beadásra kész csomaggá.

## Feladat
Kérd meg a Claude-ot, hogy állítsa össze a teljes submission package-et:

```
A Data Completion Board alapján állítsd össze a pályázati csomag végleges ellenőrző listáját.

Minden tételnél:
1. Dokumentum neve (románul, ahogy az AFM kéri)
2. Fájlnév
3. Státusz (✅ kész / ⏳ folyamatban / ❌ hiányzik)
4. Ha kész: hol található a fájlrendszerben
5. Ha hiányzik: ki a felelős és mi a határidő

A végén adj egy összesítést: hány % kész, mi blokkolja a beadást.
```

### A WOW pillanat
A Cowork végigmegy a teljes fájlrendszeren, és **valós időben ellenőrzi** melyik dokumentum van meg és melyik hiányzik. Nem kézzel kell pipálgatni — az AI tudja.

## Tanulási pont
- A Cowork nem csak dokumentumokat generál — **projektmenedzsment eszköz** is
- Az "utolsó mérföld" a legkritikusabb: itt derülnek ki a hiányok
- A checklist nem papír — a Cowork frissíti a Data Completion Board-ot is

## Checkpoint
**WOW:** A 23 tételes csomag státusza egyetlen prompttal — mi kész, mi hiányzik, ki csinálja
**MICRO HANDS-ON:** Kérdezd meg: "Melyik a 3 legkritikusabb hiányzó dokumentum és miért?"
