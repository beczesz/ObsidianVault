---
title: "Feladat 1.2: Kalandkönyv: projekt-szintű CLAUDE.md a Napsugárra"
date: 2026-07-01
author: Becze Szabolcs
status: active
description: "F1 mikro-stáció: a résztvevők egy projekt-szintű CLAUDE.md-t készíttetnek az AI-val a Napsugár projekthez, ami a gyökér-szabálykönyv fölé rétegződik. Így alakul ki a kalandkönyv-navigáció: minden mappaszinten egy plusz CLAUDE.md ad kontextust, és az AI automatikusan ugrál benne."
id: 6b3d8f02-4a71-4e52-9c26-7d1f0b3e2c84
index_schema_version: 1
bdos_index: true
tags: [ignis-academy, halado, regio-consult, f1, feladat, navigacio]
---
# Feladat 1.2: Kalandkönyv: projekt-szintű CLAUDE.md a Napsugárra

> **Típus:** ⏸ STÁCIÓ (mikro) · **Idő:** ~6 perc · **Mód:** saját gépen, copy-paste prompt

---

## Szituáció

A gyökér-CLAUDE.md megvan: az AI tudja, hogy néz ki egy Regio-projekt általában. De a Napsugárnak vannak **saját** jellemzői: ez egy tejfeldolgozó-bővítés, implementation fázisban, aktív monitoringgal, egy konkrét kivitelezővel. Ezt nem a gyökérbe írjuk, hanem **a projekt mappájába**, egy külön CLAUDE.md-be.

Ez a **kalandkönyv-elv**: ahogy az AI belép egy mappába, ott egy újabb CLAUDE.md várja plusz kontextussal. Gyökér → projekt → almappa, mindegyik szint pontosan annyit mond, amennyi ott kell.

---

## A stáció prompt

```
A Napsugar_projekt/Projects/THR_Napsugar_Tejuzem/ mappában dolgozunk.
Ez a Napsugár Tejüzem projekt (kód: THR), egy tejfeldolgozó-üzem bővítése,
implementation fázisban.

Nézd át a projekt mappáit, és írj egy projekt-szintű CLAUDE.md-t
EBBE a projekt-mappába (ne a gyökérbe). Ebben:

1. Utalj rá, hogy a gyökér CLAUDE.md általános szabályai itt is érvényesek,
   és itt csak a projekt-specifikumok vannak.
2. Foglald össze a projekt lényegét (beneficiar, tárgy, fázis).
3. Írd le, hol mi van EBBEN a projektben (melyik mappában a deviz, hol a
   szkennelt ajánlat, hol a Centralizator).
4. Sorold fel a tipikus feladatokat, amiket itt kérni fogok.

Röviden, gyakorlatiasan. Ne módosíts meglévő fájlt.
```

---

## Elvárt eredmény

Az AI 1 perc alatt ír egy `Projects/THR_Napsugar_Tejuzem/CLAUDE.md`-t, ami a gyökér fölé rétegződik. Ezután, ha egy új session-ben azt mondod „a Napsugáron dolgozom", az AI a **két CLAUDE.md-t egymás után** olvassa: előbb az általánost, majd a projekt-specifikusat, és azonnal tudja a teljes képet.

---

## Miért ez a stáció

Egy komplex, sokprojektes rendszerben nem egy óriási szabálykönyv kell, hanem **rétegzett kontextus**: minden szint annyit mond, amennyi ott releváns. Így akármilyen mély a mappa-hierarchia, az AI mindig épp a megfelelő mennyiségű kontextust kapja, és nem fullad bele. Ez skálázódik 20+ projektre is.

---

## Tipp

Ha az AI túl hosszúra írja, kérd: *„Vedd feleannyira, csak a projekt-specifikumok maradjanak, az általános szabályokat a gyökér már tartalmazza."*

---

## Otthoni elmélyítés
- `Feladat_1.3_Bonusz_Belso_sztenderd.md`, a valós belső sztenderd → CLAUDE.md
- `Feladat_1.4_Bonusz_Uj_projekt_scaffold.md`, új projekt-mappa a sztenderd szerint

**Verzió:** 1.0 (Regio adaptáció)
