---
title: "F5.1 — Üzleti terv generálása a pályázathoz"
date: 2026-05-13
author: Becze Szabolcs
status: active
description: "Üzleti terv generálása az AFM Mobilitate Verde pályázathoz, amely az F1-F4 fázisokból gyűjtött cégadatok, pénzügyi számok és eligibility információk szintézisével készül el. Az AI-nak egy komplex érvelést kell felépítenie: miért szükséges az elektromos kisteherautó-beruházás, hogyan térül meg 5 év alatt a valós üzem"
description_source: auto
description_hash: 1cae8f22c88d8bf5
id: 58580992-498e-4acf-a733-6983147e6eb5
index_schema_version: 1
bdos_index: true
---
# F5.1 — Üzleti terv generálása a pályázathoz

## Kontextus
Az AFM pályázat egyik legsúlyosabb melléklete az **üzleti terv** (M-13, Anexa 6 sablon). Ez a dokumentum, ami megmutatja az AFM-nek, hogy a TransOffice komolyan gondolja: miért kell elektromos autó, hogyan illeszkedik az üzletbe, és mi a megtérülés.

Normál esetben egy tanácsadó 2-3 napot tölt el egy üzleti tervvel. Mi az eddigi munkából (F1-F4) összegyűjtött adatokból generáljuk — mert a Cowork ismeri a céget.

## Feladat
Kérd meg a Claude-ot, hogy az eddigi kontextusból írjon üzleti tervet:

```
Az AFM Mobilitate Verde pályázathoz kell egy üzleti terv.
A Cowork ismeri a TransOffice-t az F1-es cégfájlokból, az F3-as eligibility checkből,
és az F4-es pénzügyi adatokból.

Készíts egy üzleti tervet az alábbi struktúrával:
1. Cég bemutatása (tevékenység, piaci pozíció)
2. Jelenlegi járműpark és logisztikai helyzet
3. A beruházás leírása (2 db N1 elektromos kisteherautó + 1 AC töltőállomás)
4. Indoklás (költségcsökkentés, környezetvédelem, ügyfélszolgálat javítás)
5. Pénzügyi terv (megtérülés kalkuláció 5 évre)
6. Kockázatelemzés
7. Fenntarthatóság

Használd a TransOffice valós adatait a bilanț Excel-ből és a Data Completion Board-ból.
```

## Tanulási pont
- A Cowork **szintetizál**: nem kell újra elmondani a cég adatait — ismeri az F1-F4 kontextusból
- Az üzleti terv nem sablon-kitöltés, hanem **érvelés** — az AI érti, mit akar hallani az AFM
- Megtérülés kalkuláció: az AI az Excel számaiból kiszámolja (üzemanyag vs. elektromos költség, 5 év)

## Checkpoint
**WOW:** Az eddigi 3 óra munkájából → kész üzleti terv, ami egy tanácsadónak 2 nap lenne
**MICRO HANDS-ON:** Adj hozzá egy bekezdést: "Mi történik ha NEM kapjuk meg a pályázatot — van-e B-terv?"
