---
title: "F1 — Káoszból rendszer"
date: 2026-05-12
author: Becze Szabolcs
status: active
description: "Az F1 modul bemutatja, hogy az AI hogyan rendez meg egy kaotikus fájlhalmazt (30+ dokumentum) egyetlen strukturált prompttal, és hogyan építi fel a CLAUDE.md-t mint hosszútávú memóriát."
description_source: auto
description_hash: 03845d53e78a534e
id: 62816adb-0f3d-4af5-a10c-230f92328062
index_schema_version: 1
bdos_index: true
---
# F1 — Káoszból rendszer
**Időkeret:** 20-25 perc · **Fázis a workshopban:** 1/6 — a workshop első tapasztalata

## Narratív összefoglaló
**F1 = rend a fájlok között. F2 = rend a TODO-k között. F3 = rend a döntésben.**

Az első nap reggele. Márton kávéval fogad, lerakja a laptopot eléd:

> *„Ez lesz a géped. Rádobtam egy mappát mindennel ami van. Igazából fogalmam sincs mi van benne pontosan — anyám rakta össze. Csütörtökön lesz egy meeting egy pályázati tanácsadóval — valami AFM elektromos járműflotta pályázat. Tudnom kéne mi a helyzet a cégnél rendszer-szinten. És tegyél valami rendet is."*

A `TransOffice/` mappa: **30+ fájl**, kaotikus. 5 ügyféllista, kéziratos cetlik, dupla szerződések, Ilona receptjei és unokafotója a „fontos dokumentumok" között.

Itt kezdődik a workshop **első tapasztalata**: az AI **nem csak válaszol kérdésekre** — átnéz egy egész fájlhalmazt, strukturált összefoglalót készít, és **emlékezni fog rá** a következő sessionben is.

## A v2.0 koncepció — páros mód

A workshop **páros-módban** fut (2 ember / pad, mindenki saját laptopon):
- **F1 kivétel:** mindenki saját TransOffice-on, párhuzamosan, ugyanazt a prompt-ot futtatja → mindenki saját CLAUDE.md-t kap
- **F2-F6:** felváltva ti vezetitek a Cowork-öt — egyik fázist az A pilot, másikat a B pilot (független feladatok)

Az F1 a **közös setup** ami stabilizálja minden résztvevő kontextusát — a CLAUDE.md innen él tovább F6-ig.

## Tanulási célok

1. **Multi-file kezelés** — a Cowork egyszerre több tucat fájlt olvas és értelmez
2. **CLAUDE.md koncepció** — az AI „hosszútávú memóriája" egy markdown fájlban
3. **Inkonzisztencia-felismerés** — a Cowork észreveszi ha 3 ügyféllista 3 különböző számot mutat
4. **AI mint kontextus-építő** — nem egyszeri lekérdezés, hanem perzisztens rendszer
5. **Copy-paste prompt-tanulás** — a tanulók egy jól megírt promptot **látnak végig kódblokkban**, nem maguk improvizálnak

## A fő feladat

| # | Feladat | Idő | Output |
|---|---------|-----|--------|
| **1.1** | **Káoszból rendszer (1 prompt → 3 output)** | **20-25p** | rendezett mappa + Kuka + kivonat + CLAUDE.md |

**Csak ez az 1 feladat fut élesben.** Mindenki saját laptopon, párhuzamosan. A prompt a `Feladat_1.1.md`-ben kódblokkban van — copy-paste-elhető.

## Otthoni bónusz feladatok (a Tananyagban maradnak)

| # | Bónusz | Idő | Output |
|---|--------|-----|--------|
| 1.3 | Inkonzisztencia audit | otthon | `audit_inkonzisztenciak.md` |
| 1.4 | Ügyfél adategységesítés | otthon | egységes ügyféllista |
| 1.5 | Szerződéskockázat (BicoToner) | otthon | jogi kockázati riport |
| 1.6 | Pályázati one-pager | otthon | összefoglaló dokumentum |

## Kulcs üzenet

A ChatGPT-ben minden új beszélgetés tiszta lap. A Cowork-ben a **CLAUDE.md egy állandó memória** — másnap, jövő héten is itt van a kontextus. **Ez a különbség a tranzakció és a folyamat között.**

## Delivery design

| Fázis | Ki | Mit | Idő |
|-------|-----|------|-----|
| Bemutatás | Te (oktató) | Mártonnak monológ + a TransOffice mappa megnyitása + a feladat felvezetése | ~3p |
| **HANDS-ON** | Ők (mindenki saját laptopon) | Prompt másolása + Cowork dolgozik + outputok átolvasása + finomítás | ~15p |
| Páros megbeszélés | Ők (párokban) | „Mi volt különböző a 2 outputban?" | ~3-5p |
| Átkötés F2-be | Te | „A fájlok rendben. De a meetingekből semmi nem marad meg..." | ~2p |

**Hands-on arány:** ~70% (a workshop legaktívabb fázisa F6 mellett).

## Átmenet F2-be

*„A fájlok rendben, a CLAUDE.md megvan. De nem a fájlok a fő probléma — hanem hogy Márton most jött be: csütörtökön a tanácsadói meeting **kiderítette**, hogy ez a pályázat már 2 hónapja a radarjuk alatt van, és **a forrás kifut**. Most viszont sürgős meeting Enikővel — kaotikus, sok TODO, kérdés: ki fogja ezeket nyomon követni?"*

## Asset-ek

- `Tananyag/TransOffice/` (vagy `TransOfficeCopy/` ami résztvevőnként előre lemásolódik) — a 30+ kaotikus fájl, a kiindulópont
- `Tananyag/00_Bevezetes/Ceg_leiras_TransOffice.md` — a fiktív cég teljes kontextusa (oktatói referencia)
- `Tananyag/01_Ceg_megertes/Feladat_1.1.md` — **a fő feladat, copy-paste prompt belül**

**Verzió:** 2.0 (páros-mód, unified feladat) · Korábbi v1.0: `Műhely/_archivum/01_Ceg_megertes/`
