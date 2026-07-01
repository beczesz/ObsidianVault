---
title: "Feladat 5.2: Érti-e az AI a levédett templétet? (STÁCIÓ)"
date: 2026-07-01
author: Becze Szabolcs
status: active
description: "F5 stáció: a résztvevők megnyittatják az AI-val az üres deviz-templétet, és megkérdezik, felismeri-e a szerkezetét: melyik lap mit csinál (0_IG paraméterek, 1_DG aggregátum, 5_DO1 tételek), hol vannak a szürke input-cellák és hol a levédett képletek, honnan húz a TVA. Ez a kitöltés előfeltétele: ha érti a struktúrát, ki tudja tölteni."
id: 508dc538-9475-4bd3-8aae-0f2b8c4a7d6e
index_schema_version: 1
bdos_index: true
tags: [ignis-academy, halado, regio-consult, f5, feladat, station]
---
# Feladat 5.2: Érti-e az AI a levédett templétet? (STÁCIÓ)

> **Típus:** ⏸ STÁCIÓ · **Idő:** ~10 perc

---

## Szituáció

A deviz general templét egy „szörny": a valósban 32 lap, itt a tananyagban 3 lapra egyszerűsítve, **de ugyanazzal a logikával**. Levédett cellák, kereszthivatkozások, TVA-képletek. Mielőtt kitöltetnéd, ellenőrizd: **érti-e az AI, hogyan épül fel?** Ha érti a szerkezetet, ki tudja tölteni; ha nem, előbb el kell magyaráznod.

---

## A stáció prompt

Nyisd meg a `02_deviz_general_URES_templet.xlsx`-et a Cowork Excel-pluginnal, és kérdezd:

```
Ez egy üres deviz general templét, három lappal (0_IG, 1_DG, 5_DO1).
Nézd meg a szerkezetét, és magyarázd el nekem:
- melyik lap mire való,
- hol vannak a szürke input-cellák (ahova írni lehet) és hol a levédett,
  képletes cellák (amiket nem bántunk),
- honnan húzza a TVA-t és hogyan aggregál a Cap. 4 az 5_DO1-ből.
Ne írj bele semmit, csak értsd meg és magyarázd el a logikát.
```

---

## Elvárt eredmény

Az AI leírja a struktúrát:
- **`0_IG`**: info general + paraméterek (Cota TVA, curs EUR). Innen húz minden TVA-képlet.
- **`1_DG` Deviz General**: 7 kapitulus (HG 907), a Cap. 4 sorai **nem kézi értékek**, hanem az `5_DO1` detail-lapról húznak.
- **`5_DO1` Devizul obiectului**: itt élnek a tényleges építési tételek objektumonként; az objektum-subtotalok adják a Cap. 4-et.
- A szürke cellákba írunk, a képleteseket békén hagyjuk.

---

## Miért ez a stáció

Egy komplex, levédett Excel nem fekete doboz az AI-nak, **ha megérti a logikát**. Ez a felismerés-lépés a kitöltés előfeltétele, és egyben a legfontosabb tanulság: nem az adat-bepötyögés a nehéz, hanem a **struktúra megértése**. Ha az AI (a skill segítségével) érti, hogy hol mi van és mi hova húz, a kitöltés már gépies.

---

## Tanulás

A ti templétjeitek nem azért nehezek, mert sok cella van, hanem mert **komplex a logikájuk** (kereszthivatkozás, levédés, TVA-lánc). Ha ezt a logikát egyszer megérteti az ember az AI-val (és egy skillbe önti), a kitöltés a legkevésbé nehéz rész. Ezért működik a hármas-minta: az üres + kitöltött + forrás pont a logikát tanítja meg.

## Otthoni elmélyítés
- `Feladat_5.4_Bonusz_Sajat_skill.md`, saját templéted logikájának skillbe öntése

**Verzió:** 1.0 (Regio adaptáció)
