---
title: "Feladat 1.5 (Bónusz): Sztenderd-ellenőrző szabálylista (lektor-mag)"
date: 2026-07-01
author: Becze Szabolcs
status: active
description: "F1 otthoni bónusz: a résztvevő az AI-val ellenőrizteti egy meglévő projekt-mappát a belső sztenderd ellen (elnevezés, mappa-helyesség, formátum), és kap egy eltérés-listát. Ez a jövőbeli lektor-agent magja, de itt még nem agent, csak egy ellenőrző prompt."
id: 9e60f135-7d04-4f85-8c59-3f4e2d6b5a17
index_schema_version: 1
bdos_index: true
tags: [ignis-academy, halado, regio-consult, f1, bonusz, lektor]
---
# Feladat 1.5 (Bónusz): Sztenderd-ellenőrző szabálylista (lektor-mag)

> **Típus:** gyakorolható a Napsugár sandboxon, majd otthon a saját projekten · **Minőségbiztosítás a sztenderdre**

## Cél
Amikor 3 iroda, 21 ember dolgozik ugyanabban a struktúrában, becsúsznak eltérések: rossz helyre tett fájl, elrontott elnevezés, nem-sztenderd formátum. Az AI ezt átnézi és jelzi.

## A Napsugár sandboxban két beültetett hiba van (hogy legyen mit találni)
Gyakorláshoz a `Napsugar_projekt` szándékosan tartalmaz két sztenderd-sértést:
1. `02_Editabil/deviz_regi_ne_hasznald.txt`: rossz elnevezésű (nem a `sorszám_KÓD_...` konvenció), ráadásul `.txt` az Editabil mappában.
2. `03_Documente_de_lucru/THR_Proiect_tehnic_scan_...md`: rossz helyen lévő proiect tehnic scan (a helye a `07_Proiect_tehnic`).

## Feladat
A Napsugár projekten (vagy egy sajáton):

```
Ellenőrizd ezt a projekt-mappát a CLAUDE.md-ben leírt sztenderd ellen:
- minden fájl a helyes mappában van-e,
- az elnevezési konvenciót követik-e a fájlnevek,
- van-e a helyén nem-oda-való vagy régi verziójú fájl.

Adj egy eltérés-listát: fájl → mi a probléma → mi lenne a helyes.
NE javíts semmit, csak jelezd. Én döntök, mit teszünk vele.
```

## Elvárt eredmény (megoldókulcs)
Az AI legalább a két beültetett hibát elkapja: (1) a `deviz_regi_ne_hasznald.txt` rossz elnevezését és típusát az Editabil-ban, (2) a rossz helyen lévő proiect tehnic scan-t. Egy tiszta eltérés-lista, ami alapján te döntesz. Az AI a szem, te a kéz.

## Hova vezet ez (Mester előretekintés)
Ez a **lektor-agent** magja: egy agent, ami folyamatosan figyeli, hogy minden a sztenderd szerint áll-e. Agentet a Haladón nem építünk, de látod, hogy a strukturált rendszeretek pont ideális egy ilyen automatizált őrhöz. Ez a Mester szint iránya.

**Verzió:** 1.0 (Regio adaptáció)
