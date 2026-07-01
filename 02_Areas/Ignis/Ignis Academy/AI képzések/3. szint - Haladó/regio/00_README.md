---
title: "Regio Consult — haladó képzés adaptáció (mester-index)"
date: 2026-07-01
author: Becze Szabolcs
status: active
version: 1.0
description: "Belépő a Regio Consult AI haladó-képzés adaptációjához: a teljes anyag térképe (alap-meeting, adaptációs stratégia, anyag-áttekintés, OCR/konverzió, fiktív Napsugár példakészlet, sandbox, Regio-specifikus deck) és a workshop F1-F6 terve a Napsugár Tejüzem fiktív fonálon."
id: 8634a580-d3b5-478a-b364-0c7d40bc2bc3
index_schema_version: 1
bdos_index: true
tags: [ignis-academy, halado, regio-consult, index, workshop-terv, adaptacio]
---

# Regio Consult — haladó képzés (mester-index)

> Az Ignis Academy Haladó (3. szint) workshop **Regio Consultra szabott** változata. Az eredeti (TransOffice) anyag változatlanul megvan a `../original/`-ban. Ez a mappa az adaptáció. **Konfidenciális:** a `raw/` valós ügyféladat; minden tananyag-asset a fiktív „Napsugár Tejüzem" példára épül.

## Az út (dokumentumok sorrendben)
1. [`00_meeting_alap_2026-06-29.md`](00_meeting_alap_2026-06-29.md) — az igényfelmérő meeting átirata + összegzése (ki a Regio, 3 fájdalom).
2. [`01_adaptacio_strategia_v0.1.md`](01_adaptacio_strategia_v0.1.md) — a keret-eltolás (pályázó → tanácsadó), fázis-remap.
3. [`02_anyag_attekintes_2026-06-30.md`](02_anyag_attekintes_2026-06-30.md) — a beküldött valós fájlok + AI-megvalósíthatóság a 3 fájdalomra.
4. [`03_konverzio_es_OCR_strategia_2026-06-30.md`](03_konverzio_es_OCR_strategia_2026-06-30.md) — szkennelt PDF → md, token-mérleg, vektorizálás vs. md.
5. `fiktiv_pelda/` — a teljes fiktív példakészlet (lásd lent). Ez az assetek fejlesztői forrása (mint az eredeti `Műhely/`).
6. **[`Tananyag/`](Tananyag/README.md) — a KÉSZ tanulói csomag** (önálló, zip-elhető): fő README + `00_Bevezetes` (cégleírás) + `Napsugar_projekt/` sandbox + 6 fázis (`01_Struktura_CLAUDE` … `06_Monitoring`), fázisonként `README_FX.md` + `Feladat_X.X.md` copy-paste promptokkal, önellenőrzéssel, WOW-checkpointtal és otthoni bónuszokkal, plusz `ZARAS.md`. Az eredeti Haladó `Tananyag/` pedagógiájára építve, Napsugár-adaptálva.
7. `deck-regio/` — a Regio-specifikus prezentáció (`index.html`).
8. `raw/` — a valós, konfidenciális Regio-fájlok (referencia, nem tananyag).

## A workshop fonala: „Napsugár Tejüzem" (fiktív)
A résztvevő egy Regio-tanácsadó, aki egy ügyfél-projektet (tejfeldolgozó-beruházás) visz a strukturált céges rendszerben. A 4 óra a 3 fő fájdalmat oldja meg, egyetlen összefüggő projekten.

| Fázis | Regio-téma | Anyag a `fiktiv_pelda/`-ban |
|---|---|---|
| **F1** | Tanítsd be az AI-t a strukturált rendszeredre (CLAUDE.md) | `regio_sandbox/` (navigálható struktúra + gyökér/projekt CLAUDE.md) |
| **F2** | Egyeztetés → feladatlista | `F2_meeting_egyeztetes_Napsugar.md` → `F2_feladatok_EREDMENY.md` |
| **F3** | Szkennelt ajánlat → használható adat (OCR → md) | `oferta_szkennelt_Napsugar.pdf` → `oferta_szkennelt_Napsugar_OCR.md` |
| **F4** | Ajánlatkérés ↔ ajánlat tételes összevetése | deviz + OCR-md → `F4_osszevetes_EREDMENY.md` |
| **F5** | Deviz/üzleti terv templét kitöltése (killer-demo) | `02/03_deviz…`, `04/05_anexaB…` (üres + kitöltött) + `01_forras…` |
| **F6** | Monitoring Centralizator kitöltése | `06/07_monitorizare_Centralizator…` (üres + kitöltött) |

A `fiktiv_pelda/README.md` az end-to-end lánc (szkennelt → md → Excel → monitoring) leírása és a fiktív projekt kontroll-számai.

## Számok (fiktív, konzisztens az egész készleten)
- Deviz general TOTAL: **6 455 000 lej** fără TVA (7 681 450 cu TVA, 19%)
- Kivitelezői ajánlat: **5 375 000 lej** (Cap. 4.1-4.5)
- F4 eltérés: **60 000 lej** (4.6 active necorporale, az ajánlatból hiányzik)
- Napsugár üzleti terv: An1 profit net 1 369 200 lej

## A deck futtatása
- Preview / böngésző: `.claude/launch.json` → **`ignis-halado-regio-deck`** (port 8153), teljes képernyő (F11).
- Vagy: `python -m http.server 8153 --directory "…/regio/deck-regio"`.
- Dia-terv: `deck-regio/00_dia-terv.md`.

## Verifikáció (2026-07-01)
- **Deck:** böngészőben lefuttatva (46 dia, 6 animáció), nulla konzol-hiba; a pig-farm maradványok kitakarítva, számok konzisztensek. (Screenshot ebben a környezetben időtúllépett, ezért DOM/konzol-alapú ellenőrzés.)
- **Friss-session szimuláció:** egy tiszta, előzmény nélküli session végigcsinálta mind a 6 feladatot csak a kész fájlokból → **mind PASS**, minden kimenet egyezik a megoldókulccsal. Számok tie-out: ajánlat 5 375 000, deviz Cap4 5 435 000, deviz TOTAL 6 455 000, F4 eltérés 60 000.
- **Elvárás-kezelés a workshopra:** a képlet-újraszámolás és a levédett cellák a **Cowork Excel-pluginnal (élő Excel)** működnek; egy fejlesztői python/openpyxl script viszont nem számol képletet és nem kényszeríti a lapvédelmet írásnál. A workshop-út (Cowork) rendben; ez csak script-oldali tudnivaló.

## Nyitott döntések (a képzés véglegesítéséhez)
- **Scope:** a 4 órából a #2 (templét-kitöltés) vs. #1 (szkennelt→monitoring lánc) aránya.
- **Obsidian:** csak markdown + SharePoint, vagy Obsidian is opcióként.
- **Létszám (21 fő):** co-facilitator vagy páros-mód.
- **Net-infra:** előzetes wifi-teszt (az éles visszajelzés P0-ja).
