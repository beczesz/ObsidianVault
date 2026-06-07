---
title: "F4.1 — Szerződés deep-check: a Béla bácsi sztori"
date: 2026-05-13
author: Becze Szabolcs
status: active
description: "Mélyen elemzett esettanulmány, amely azt mutatja, hogy a szerződések felületes ellenőrzése kockázatos lehet. Az AI a TransOffice bérleti szerződésből kiindulva azonosít egy rejtett veszélyt (a tulajdonos potenciális ingatlanértékesítése), amely összevetéskor az AFM 5 éves stabilitási követelményét veszélyezteti, majd proaktív kommunikációval"
description_source: auto
description_hash: 683e5f655349c688
id: b82be628-f6e8-4b81-852e-c64279eca305
index_schema_version: 1
bdos_index: true
---
# F4.1 — Szerződés deep-check: a Béla bácsi sztori

## Kontextus
Az F3 Data Completion Board-jában az M-16 (Telephely-igazolás) **zöld**: van bérleti szerződés (Béla Iosif × TransOffice, 2018-2028, Calea Băieșenilor 22). Első ránézésre minden rendben — 10 éves szerződés, még 3+ év hátra, az AFM kiírás 5 évet kér.

De vajon tényleg rendben van?

## Feladat
Kérd meg a Claude-ot, hogy **mélyebben ellenőrizze** a bérleti szerződést — ne csak a szerződést nézze, hanem az egész TransOffice kontextust.

### Prompt
```
A Data Completion Board alapján az M-16 (Telephely-igazolás) zöld státuszú.
Mielőtt elküldjük a pályázatot, kérlek nézd át mélyebben a bérleti szerződést
(szerzodes_chirie_TransOffice_2018.docx) és vesd össze a teljes
TransOffice/ mappa tartalmával + az AFM pályázati kiírás 5.1.1.7 pontjával.

Vannak-e olyan kockázatok, amik nem nyilvánvalóak a szerződésből magából?
```

### Mi fog történni
A Cowork nem csak a szerződést olvassa — **az egész cég kontextusát átnézi**. És talál egy elhullatott mondatot a meeting transcriptben:

> *"Béla bácsi szilveszterkor mondott valamit, hogy gondolkodik egy-két ingatlana eladásán — utána kéne nézni nehogy a miénk legyen, ahol a raktár van."*

Ezt a mondatot **senki nem vette komolyan** a meetingen. Nem lett belőle TODO. De a Cowork összekapcsolja:
- Béla Iosif = a bérleti szerződés Locator-a
- "ingatlana eladásán gondolkodik" = potenciális tulajdonosváltás
- AFM 5.1.1.7 = 5 év stabilitás kell → ha eladja, az új tulajdonos kérdéses

**Riasztás generálódik.**

### A következő lépés
A Cowork generál egy tisztázó emailt Béla úrnak (románul, professzionális hangon), amiben rákérdezünk:
1. Tervezi-e a Calea Băieșenilor 22 eladását?
2. Ha igen, milyen biztosíték van a bérleti folytonosságra?

### A válasz "megérkezik"
Az oktató megnyitja a `email_exportok/raspuns_bela_iosif_2025-02-26.txt` fájlt — Béla bácsi 2 nap múlva válaszolt:
- A tervezett eladás NEM a TransOffice épülete, hanem egy mezőgazdasági föld
- Felajánlja a szerződés meghosszabbítását 2035-ig
- Felajánl közjegyzői nyilatkozatot a neînstrăinare-ról

**Eredmény:** Nem volt baj — DE most van egy extra biztosíték a pályázathoz.

## Tanulási pont
- **Cross-document analysis**: az AI olyan dolgokra figyel fel, ami egy ügyvédnek sem tűnne fel — mert egy ügyvéd a szerződést olvassa, a Cowork meg az egész cégtörténetet
- **A checkbox mentalitás veszélye**: "Van szerződés? ✓ Kész." — ez kevés. A kontextus számít.
- **AI mint operátor**: nem csak riaszt, hanem generálja az emailt is

## Checkpoint
**WOW:** A zöldre pipált M-16 mögött kockázat van, amit az AI egy meeting-mondat és a szerződés összevetéséből fedez fel
**MICRO HANDS-ON:** Nézd meg Béla bácsi válaszát — mit változtat a Data Completion Board-on?
