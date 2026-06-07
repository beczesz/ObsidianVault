---
title: "(Bónusz) Feladat 4.6 — Excelből vezetői dashboard"
date: 2026-05-14
author: Becze Szabolcs
status: active
description: "Gyakorlati feladat egy Excel pénzügyi adattáblából vezetői dashboard készítésére a Cowork segítségével, amely KPI csempéket, grafikonokat és szöveges elemzést tartalmaz HTML formátumban."
description_source: auto
description_hash: 2c7c3b4a2b08e0e0
id: 402a9d60-7565-4976-9f05-550515ce9c89
index_schema_version: 1
bdos_index: true
---
# (Bónusz) Feladat 4.6 — Excelből vezetői dashboard

## Szituáció

Az F4.2-ben Mihaela elküldött egy strukturált Excel-t pénzügyi adatokkal. De a nyers Excel **nem mond el semmit** Mártonnak — szám-tenger, oszlopok, sorok.

A Cowork képes az Excel-adatból azonnal **vezetői dashboardot** generálni — egy egyoldalas vizuális összefoglalót, ami a fontos számokat látványosan mutatja.

## Feladat

Vegyél egy számokkal teli Excel-fájlt (lehet TransOffice-ból, lehet saját életedből — banki kivonat, költségvetés, projekt-controlling tábla) és kérd meg a Cowork-öt, hogy dashboard-ot generáljon belőle.

### Forrás lehet:
- TransOffice: `eves_jelentes_2022.xlsx` vagy a Mihaela által visszaküldött Excel
- Saját banki kivonat (CSV vagy XLSX)
- Saját költségvetés-tábla
- Egy projektben használt controlling-tábla
- Egy értékesítési riport

### Javasolt prompt:

> "Itt egy Excel pénzügyi adatokkal. Készíts belőle egy **egyoldalas vezetői dashboardot** HTML-ben, ami a fontos számokat **vizuálisan** mutatja:
>
> 1. 3-4 nagy KPI csempe a tetején (pl. árbevétel, költség, profit, ügyfélszám)
> 2. 1-2 idősoros grafikon (havi vagy negyedéves bontás)
> 3. 1 kategória-szerinti megoszlás (kördiagram vagy oszlopdiagram)
> 4. Egy szöveges összefoglaló — 'Mi a 3 legfontosabb dolog' szekció
>
> Stílus: tiszta, modern, üzleti. Színek: kék/szürke/zöld. Mobil-barát."

## Elvárt kimenet

`dashboard_[YYYY_MM].html` — egy önálló HTML fájl ami:
- Megnyitható böngészőben
- Vizuálisan vonzó
- 1 képernyőre fér
- Print-barát (PDF-ként ki lehet menteni)

## Extra kihívás

Miután megvan a dashboard, kérdezd meg:
> "Adj egy 'business commentary' szöveget hozzá (max 200 szó) — egy CEO-stílusú elemzés a számok mögötti történetről. Mi a jó, mi az aggasztó, mi a következő lépés?"

A Cowork így nemcsak vizualizál, hanem **értelmezi** is a számokat.

## Tipp

A dashboard HTML formátum azért hasznos, mert:
- Megnyitható bármelyik gépen, nem kell külön szoftver
- E-mailben elküldhető (mellékletként vagy beágyazva)
- PDF-ré nyomtatható
- Reprodukálható havonta (új Excel + ugyanaz a prompt = új dashboard)

## Tanulás

- A Cowork **összekapcsolja az adatot és a vizualizációt** — nincs köztes lépés (Power BI, Tableau, etc.)
- Egy havi dashboard előállítása 2 perc → érdemes **havi rituálévá** tenni
- A "business commentary" az igazi érték: nem a számok, hanem a **mit jelentenek**
- Ha sablonossá teszed, a Cowork akár automatizálhatja (havi scheduled task)
