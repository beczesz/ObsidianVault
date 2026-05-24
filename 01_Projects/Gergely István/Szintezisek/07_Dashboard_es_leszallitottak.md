---
title: "Dashboard és leszállított anyagok"
type: deliverable-index
project: Gergely István
created: 2026-05-21
tags: [dashboard, deliverable, output]
id: 9b5e9456-4015-4269-bdaf-3c4a43670c60
index_schema_version: 1
---

# Leszállított anyagok

## 📊 Interaktív dashboard v2 — `Dashboard_2025.html`
Önálló, **offline futó** HTML (Chart.js + adat beágyazva, internet nem kell). Dupla kattintásra
megnyílik böngészőben. **Teljesen interaktív, drill-down architektúra.**

**Globális vezérlők (fejlécben):** termék-kereső · év-választó (2025; **2024 később egy gombnyomással
behúzható**) · telephely-szűrő · **light/dark mód** kapcsoló.

**7 tab:**
1. **Áttekintés** — KPI-k (kattinthatók), csatorna-bontás, telephelyi árbevétel (kattints → al-dashboard),
   „mire költenek" mini, adat-rekonciliáció.
2. **Telephely** — szűrő nélkül összevetés; egy telephelyre kattintva **al-dashboard** nyílik
   (havi árbevétel jan–dec, top termékek, készletprobléma) az adott telephelyre szűrve.
3. **Mire költenek** — költési csoportok (meta-kategóriák, **valós érték + %**) → csoportra kattintva
   kategóriák → kategóriára kattintva **kategória-részlet** (forgalom, %, árrés, benne lévő termékek).
4. **Termékek** — **kereső**: bármely termékre keresve teljes termék-kártya (kategória, költési csoport,
   telephelyenkénti készletmozgás %-okkal).
5. **B2B & partnerek** — Pareto, HHI, partnerlista; partnerre kattintva részlet.
6. **Idő & ritmus** — teljes árbevétel vs. B2B havonta (jan–dec 2025), **heti ritmus** (kedd+péntek = szállítónapok), profit%.
7. **Készlet** — negatív/holt KPI-k → **kattintva szűrhető tételes lista** (név + kategória szűrő);
   problémák telephelyenként, szortiment-átfedés.

**Tervezési elvek:** „**ne becsülj semmit**" — a becsült profit/üzlet kikerült; minden szám tény.
Ahol egy nézet csak hálózati szinten létezik (kategória, partner, B2B), a panel ezt **őszintén jelzi**
telephely-szűrő mellett. Újrahasználható komponensek (kártya, panel, chart, tábla, modal), év-kulcsolt
adatréteg a többéves bővítéshez.

### Mire költenek a vásárlók (kasszás, valós érték — nem becslés)
| Költési csoport | Forgalom | % | Árrés% |
|---|---:|---:|---:|
| Friss élelmiszer | 1 726 933 | 35,0% | 24,1% |
| Alkohol & dohány | 1 129 202 | 22,9% | 15,4% |
| Édesség & snack | 570 573 | 11,6% | 26,5% |
| Háztartás & vegyiáru | 493 005 | 10,0% | 25,5% |
| Alap- és száraz élelmiszer | 382 970 | 7,8% | 24,8% |
| Üdítő, víz, kávé/tea | 375 179 | 7,6% | 27,2% |
| Non-food egyéb | 156 136 | 3,2% | 26,3% |
| Egyéb / technikai | 94 467 | 1,9% | 68,7% |

> A termék→kategória besorolás kulcsszavas, **~74% lefedettség**; a maradék „besorolatlan". A pontos
> besoroláshoz az adatkérő lista #3 (cikktörzs árucsoporttal) kell.

## 📄 `Keszlet_problemak_2025.xlsx`
Tételes, telephely szerinti lista a tulajdonosnak: **267 negatív** + **1 159 holt** készlet,
összefoglaló füllel és teendőkkel.

## ⚙️ `_build/` (reprodukálható pipeline)
- `extract.py` — minden aggregátum kinyerése → `dashboard_data.json`
- `make_excel.py` — készlet-Excel
- `make_dashboard.py` — HTML generálás (adat + Chart.js beágyazva)
- A forrás-Excelek frissítésekor a három script újrafuttatásával minden regenerálódik.

## Új felismerések (a dashboardban vizualizálva)
- **Forgási sebesség**: BIRGITA 24,9× a leggyorsabb, ZETEKINCSE 10,6× (új bolt, felfutóban).
- **Szortiment**: csak **140 cikk** közös mind a 6 boltban; **2 496 cikk** csak egyetlen boltban → erős lokális kínálat.
- **Partner-koncentráció (HHI)** és Pareto a B2B függőségi kockázathoz.
- **Áfa-szerkezet**: ~2,45 M lej a 9%-os (élelmiszer), ~2,32 M a 19–21%-os sávban.
- **Szezonalitás kettéválik**: a novemberi gödör csak a B2B csatornáé, a teljes árbevételé nem.

Kapcsolódó: [[00_Attekintes]] · [[06_Tovabbi_felismeresek]]

## Következő lépés a komplexebb dashboard felé
- **Cikkszintű árrés**: a PTOT cikkek kategóriához rendelése (kategória-árrés rávetítés) → konkrét
  termék-jövedelmezőség. Ehhez cikk→kategória megfeleltetés kell (a PTOT-ban nincs kategória oszlop).
- **Telephelyenkénti árrés**: jelenleg hálózati átlag; gestiune-szintű árréshez gestiune-bontott Adaos kell.
- **Partner × idő**: a ZGY (partner) és P2025 (idő) önmagában nem köthető össze; a számlaszintű
  (partner+dátum) export oldaná meg.
- **Több év** összevetése, ha lesz 2024/2026 adat → trendek, növekedés.
