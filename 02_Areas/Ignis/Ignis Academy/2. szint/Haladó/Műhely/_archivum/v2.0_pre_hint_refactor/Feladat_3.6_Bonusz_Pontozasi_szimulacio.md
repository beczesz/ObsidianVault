---
title: "(Bónusz) Feladat 3.6 — Pontozási szimuláció"
date: 2026-05-14
author: Becze Szabolcs
status: active
description: "Pontozási szimulációs feladat, amely azt mutatja meg, hogy a TransOffice pályázata hány pontot érne a 100 pontos értékelési skálán, és mely kritériumok fejlesztésével lehetne javítani az esélyek. Projektmenedzsereknek és pályázatíróknak ajánlott a beadás előtt elvégezni."
description_source: auto
description_hash: 4c485f8a03ad9c31
id: 4e754de2-6646-4202-800f-c21ca88bbb3d
index_schema_version: 1
bdos_index: true
---
# (Bónusz) Feladat 3.6 — Pontozási szimuláció

## Szituáció

A pályázati kiírásban (`Ghidul-solicitantului-Mobilitate-Verde-IMM-2025.md`) van egy **pontozási rendszer**: 100 pontos skála különböző kritériumok szerint. A legtöbb pályázó **soha nem nézi meg ezt** beadás előtt — pedig itt látszik, hogy a benyújtott anyag valószínűsíthetően mennyi pontot ér.

A Cowork-kel pár perc alatt szimulálható: ha most beadnánk, hány pontot kapnánk és **min lehetne még javítani**.

## Feladat

Kérd meg a Cowork-öt egy pontozási szimulációra:

### Javasolt prompt:

> "Olvasd át a pályázati kiírásban a pontozási kritériumokat (általában a 'Criterii de evaluare' vagy 'Punctare' szekció). Listázd ki minden kritériumot a maximum pontszámával.
>
> Aztán a TransOffice cégadatok és a már elkészült anyagok (üzleti terv, F3 outputok, F4 Mihaela Excel) alapján **becsüld meg pontonként hány pontot kapnánk** ma. Indokold.
>
> A végén:
> 1. Becsült összpontszám
> 2. Top 3 kritérium ahol a legtöbbet veszítünk
> 3. Minden TOP-3 kritériumhoz konkrét javaslat: mit változtassunk hogy +5-10 pontot kapjunk"

## Elvárt kimenet

`palyazat_pontozasi_szimulacio.md`:

### Pontozás táblázat

| Kritérium | Max pont | Becsült | Mit írna nálunk | Hogyan javítható |
|-----------|----------|---------|-----------------|------------------|
| Penetrare comercială | 15 | 11 | Stabil ügyfélkör (40+), 22 év | Erősebb növekedési narratíva |
| Sustenabilitate financiară | 20 | 15 | Pozitív cash flow, kis tartalék | Bankgarancia hozzákapcsolása |
| Impact ecologic | 25 | 22 | 4 elektromos jármű = 18t CO2/év | Bővítsd: 5 év CO2 csökkenés |
| ... | ... | ... | ... | ... |
| **ÖSSZESEN** | **100** | **74** | | |

### Top 3 fejlesztési pont

1. **Sustenabilitate financiară (-5 pont):** Csatoljunk bankgaranciát vagy IFOM finanszírozási előjegyzést → +4-6 pont
2. **Plan de afaceri – inovare (-4 pont):** Adjunk hozzá egy "Smart Routing" digitalizációs alfejezetet → +3-5 pont
3. **Echipa managerială (-3 pont):** Mihaela CV-jét emeljük ki konkrét számokkal → +2-3 pont

### Cél pontszám: 74 → 86

## Tipp

A pályázati nyertesi küszöb gyakran **70-80 pont** körül van. Ha a szimuláció 65-öt mutat, **van mit dolgozni a beadás előtt**. Ha 85-öt, **csak fésülni kell**.

## Tanulás

- A pontozási kritériumokat **senki nem olvassa** — pedig itt van a játéktábla
- Az AI nem fog tudni 100 pontot ígérni — de **a hézagokat megmutatja**, és ez a fontos
- Egy iterációs ciklus: szimuláció → fejlesztés → új szimuláció → +10 pont
- Realista becslés: az AI általában optimistább mint a valós bírálók, **számolj le 5-10 pontot** a biztosság kedvéért
