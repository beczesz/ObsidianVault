---
title: "_build — dashboard pipeline"
date: 2026-05-22
author: Becze Szabolcs
status: active
description: "Reprodukálható adatfeldolgozási folyamat a Dashboard_2025.html-hez: Python-scripteken keresztül év-kulcsolt adatrétegből, Excel-problémalistából és önálló offline HTML-dashboardból. Fejlesztők és adatkezelők számára az adat-pipeline és verziókezelés dokumentációja."
description_source: auto
description_hash: e5e59eee2d3254b9
id: 00192110-b7d4-47b6-a302-0c34528828bb
index_schema_version: 1
bdos_index: true
---
# _build — dashboard pipeline

Reprodukálható adat-pipeline a `Dashboard_2025.html`-hez. **A v2 az aktuális.**

## Aktuális pipeline (v2)
1. `python3 _build/extract_v2.py` → `_build/data_v2.json`
   (év-kulcsolt adatréteg, termék-kategorizálás, meta-csoportok, heti ritmus, készlet-listák)
2. `python3 _build/make_excel.py` → `Keszlet_problemak_2025.xlsx`
3. `python3 _build/make_dashboard_v2.py` → `Dashboard_2025.html`
   (önálló offline HTML; beágyazza a `data_v2.json`-t és a `chart.umd.min.js`-t)

A forrás-Excelek frissítése után fenti 3 parancs → minden regenerálódik.

## 2024 (vagy újabb év) behúzása
- Másold az `extract_v2.py`-t, állítsd a `YEAR` és `FILES` változókat a 2024-es fájlokra,
  futtasd, majd a két év `years` blokkját **egy JSON-ba** fűzd (`years: {"2024":..., "2025":...}`,
  `meta.elerheto_evek: ["2024","2025"]`). A dashboard év-választója automatikusan kezeli.

## Régi (v1, archív)
`extract.py`, `make_dashboard.py`, `dashboard_data.json` — az első verzió. Megtartva referenciának;
a dashboardot már a v2 generálja. Törölhető, ha nem kell.

## Köztes fájlok
`keszlet_negativ.json`, `keszlet_holt.json` — a v1 Excel-hez; a v2 a `data_v2.json`-ba ágyazza ezeket.
