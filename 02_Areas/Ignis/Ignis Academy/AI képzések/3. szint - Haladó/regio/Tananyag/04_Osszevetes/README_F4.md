---
title: "F4: Ajánlatkérés vs. ajánlat tételes összevetése"
date: 2026-07-01
author: Becze Szabolcs
status: active
description: "Az F4 modul: az AI egyszerre nézi az ajánlatkérést (a deviz general Cap. 4 = investiția de bază) és a kivitelező ajánlatát (az F3-ban kinyert OCR-md), majd tételesen összeveti, és megtalálja az eltérést, amit külön-külön olvasva kihagynál (a 60 000 lej 4.6 Active necorporale). Oktatói demó + résztvevői stáció az eltérés-riportra."
id: 78059eb0-1697-4d5a-8e2c-2d4f0a6e5b3c
index_schema_version: 1
bdos_index: true
tags: [ignis-academy, halado, regio-consult, f4, osszevetes, cross-doc]
---
# F4: Ajánlatkérés vs. ajánlat tételes összevetése
**Időkeret:** 25 perc · **Fázis a workshopban:** 4/6

## Modell

🎤 **DEMO** + ⏸ **1 stáció** a résztvevőknek.

| # | Fájl | Típus | Idő |
|---|---|---|---|
| **4.1** | `Feladat_4.1_Tetelenkenti_osszevetes.md` | 🎤 OKTATÓI DEMO (kereszt-összevetés) | ~12p |
| **4.2** | `Feladat_4.2_Elteres_riport.md` | ⏸ STÁCIÓ (eltérés-riport / tisztázó kérdés) | ~8p |

## Narratív összefoglaló

Az F3-ban a szkennelt ajánlatból gépi-olvasható tábla lett (OCR-md). De ez még nem válasz a kulcskérdésre: **megfelel-e az ajánlat a kiírásnak?** A kiírás a **deviz general Cap. 4** (investiția de bază), az ajánlat a kivitelező tételsora. A kettőt tételesen kell egyeztetni: minden mennyiség, minden összeg stimmel-e.

Ez ma a kollégáknál 100% kézi, tétel a tétel után. Az AI egyszerre nézi a két forrást, és **tételesen** összeveti. A demó csúcspontja: megtalálja a **4.6 Active necorporale (szoftver, 60 000 lej)** tételt, ami a devizben szerepel, de az ajánlatból hiányzik. Pont ez az a tétel, amit az F2 egyeztetésen is jeleztek, és pont az, amit külön-külön olvasva könnyű átugorni.

## Tanulási célok
1. **Több forrás keresztellenőrzése**, az AI egyszerre tart két dokumentumot, és sorpárokat vet össze.
2. **Az eltérés megtalálása**, nem csak az egyezést erősíti meg, hanem a hiányt is kiszúrja.
3. **Kontroll-fegyelem**, a végösszegek tie-out-ja (5 435 000 vs. 5 375 000, eltérés 60 000).
4. **Ember dönt**, az AI jelzi az eltérést, a tisztázás (beneficiár, külön beszerzés) emberi döntés.

## Otthoni bónuszok

| # | Bónusz | Output |
|---|---|---|
| 4.3 | `Feladat_4.3_Bonusz_Harom_ajanlat.md` | Három ajánlat összevetése (bírálat-segéd) |
| 4.4 | `Feladat_4.4_Bonusz_Mennyiseg_audit.md` | Mennyiségi (m3, tonna) audit a kiírás ellen |
| 4.5 | `Feladat_4.5_Bonusz_Sajat_osszevetes.md` | Saját valós ajánlat-pár összevetése |

## Átmenet F5-be

*„Megvan az eltérés, tisztázzuk a beneficiárral. De most jön a workshop csúcspontja: a legáltalánosabb fájdalmatok, a levédett deviz-templét kitöltése. És nem kézzel, hanem egy skillel, amit a csapatod megoszthat."*

## Asset-ek
- `Pelda_output/osszevetes_EREDMENY.md`, a tételes összevetés (megoldókulcs).
- Forrás: az F3 OCR-eredménye (`../03_Szkennelt_PDF/Pelda_output/oferta_OCR.md`) + a projekt deviz (`../Napsugar_projekt/.../02_Editabil/`).

**Verzió:** 1.0 (Regio adaptáció)
