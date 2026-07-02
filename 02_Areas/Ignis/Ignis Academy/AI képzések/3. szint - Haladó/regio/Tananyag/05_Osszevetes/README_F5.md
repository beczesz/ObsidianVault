---
title: "F5: A deviz értelmezése és az ajánlat összevetése"
date: 2026-07-02
author: Becze Szabolcs
status: active
description: "Az F5 modul: előbb az AI-val ÁTNÉZETJÜK és értelmeztetjük a hiteles HG 907 kiírás-devizt (bizonyítva, hogy a Claude az Excelt is érti), majd tételesen ÖSSZEVETJÜK a devizt (ajánlatkérés) az F4-ban kinyert ajánlattal, és megtaláljuk az eltérést (a 60 000 lej 4.6 Active necorporale, ami a devizben van, de az ajánlatból hiányzik). Végül eltérés-riport a beneficiárnak. 2 demó + 1 stáció + otthoni bónuszok."
id: 78059eb0-1697-4d5a-8e2c-2d4f0a6e5b3c
index_schema_version: 1
bdos_index: true
tags: [ignis-academy, halado, regio-consult, f5, deviz, osszevetes, excel]
---
# F5: A deviz értelmezése és az ajánlat összevetése
**Időkeret:** 30 perc · **Fázis a workshopban:** 5/6

## Modell

🎤 **2 DEMO** + ⏸ **1 stáció**.

| # | Fájl | Típus | Idő |
|---|---|---|---|
| **4.1** | `Feladat_5.1_Deviz_attekintes.md` | 🎤 DEMO (a deviz értelmezése, az AI érti az XLS-t) | ~10p |
| **4.2** | `Feladat_5.2_Tetelenkenti_osszevetes.md` | 🎤 DEMO (tételes kereszt-összevetés) | ~12p |
| **4.3** | `Feladat_5.3_Elteres_riport.md` | ⏸ STÁCIÓ (eltérés-riport / tisztázó kérdés) | ~8p |

## Narratív összefoglaló

Az F4-ban a szkennelt ajánlatból gépi-olvasható tábla lett (OCR-md). Most jön a kérdés: megfelel-e az ajánlat a kiírásnak?

Előbb magát a **kiírás-devizt** nézzük meg (5.1): egy hiteles, HG 907 szerinti deviz general (7 kapitulus, kereszthivatkozott lapok, TVA- és eligibil-számítás). Az AI megnyitja, átlátja és értelmezi, ezzel bizonyítva, hogy **nem csak szöveget, hanem az Excelt is érti**.

Aztán jön a tényleges összevetés (5.2): a deviz **Cap. 4** (investiția de bază, az ajánlatkérés) vs. a kivitelező ajánlata. A demó csúcspontja: megtalálja a **4.6 Active necorporale (szoftver, 60 000 lej)** tételt, ami a devizben szerepel, de az ajánlatból hiányzik. Pont ezt jelezték az F2 egyeztetésen, és pont ezt könnyű külön-külön olvasva átugorni.

Végül (5.3) az eltérésből cselekvés lesz: egy riport vagy egy tisztázó kérdés a beneficiárnak.

## Tanulási célok
1. **Excel-értés**, az AI megnyit és értelmez egy komplex, több lapos, képletvezérelt devizt (nem csak szöveg).
2. **Több forrás keresztellenőrzése**, az AI egyszerre tart két dokumentumot, és sorpárokat vet össze.
3. **Az eltérés megtalálása**, nem csak az egyezést erősíti meg, hanem a hiányt is kiszúrja.
4. **Kontroll-fegyelem**, a végösszegek tie-out-ja (5 435 000 vs. 5 375 000, eltérés 60 000).
5. **Ember dönt**, az AI jelzi az eltérést, a tisztázás emberi döntés.

## Otthoni bónuszok

| # | Bónusz | Output |
|---|---|---|
| 4.4 | `Feladat_5.4_Bonusz_Harom_ajanlat.md` | Három ajánlat összevetése (bírálat-segéd) |
| 4.5 | `Feladat_5.5_Bonusz_Mennyiseg_audit.md` | Mennyiségi audit a kiírás (antemăsurătoare) ellen |
| 4.6 | `Feladat_5.6_Bonusz_Sajat_osszevetes.md` | Saját valós ajánlat-pár összevetése |

## Átmenet F6-be

*„A devizt értjük, az eltérést megtaláltuk, tisztázzuk a beneficiárral. De most jön a workshop csúcspontja: a legáltalánosabb fájdalmatok, a levédett deviz-templét kitöltése. És nem kézzel, hanem egy skillel, amit a csapatod megoszthat."*

## Asset-ek
- A projekt **kiírás-devize** (hiteles, HG 907): `RegioConsult/Projects/THR_Napsugar_Tejuzem/02_Editabil/01.b_THR_Deviz_general...xlsx` (0_IG, 1_DG, 5_DO1).
- Az F4-ban kinyert **ajánlat**: `.../08_Dosare_de_achizitii/04.04_DAL_Lucrari/04.04.d_THR_Oferta_kivitelezo_OCR...md`.
- `Pelda_output/osszevetes_EREDMENY.md`, a tételes összevetés (megoldókulcs).

**Verzió:** 2.0 (deviz-értelmezés + hiteles HG 907 deviz, 2026-07-02)
