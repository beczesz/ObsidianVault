---
title: "Feladat 1.3: A CLAUDE.md navigációs lánc (kalandkönyv)"
date: 2026-07-02
author: Becze Szabolcs
status: active
description: "F1 harmadik feladat: a CLAUDE.md fogalmának bemutatása egy háromszintű, láncolt navigáción keresztül. Az 1. prompt felépíti a láncot (gyökér CLAUDE.md a RegioConsult-ban + index CLAUDE.md a Projects-ben), a 2. prompt egy teljesen új munkamenetben, nulla kontextussal kérdez egy Napsugár-részletet (a beruházás összege). Az AI magától végigolvassa a láncot (gyökér, Projects index, projekt CLAUDE.md), és megtalálja a választ. Ez bizonyítja a kontextus-perzisztenciát és a kalandkönyv-navigációt."
id: 7c4e9f13-5b82-4d63-8a37-1e2f0c4d3b95
index_schema_version: 1
bdos_index: true
tags: [ignis-academy, halado, regio-consult, f1, feladat, claude-md, navigacio]
---
# Feladat 1.3: A CLAUDE.md navigációs lánc (kalandkönyv)

> **Típus:** ⏸ STÁCIÓ · **Idő:** ~10 perc · **Mód:** két prompt, kettő közt új munkamenet

---

## Szituáció

A rendrakás (1.2) megszülte a Napsugár projekt saját CLAUDE.md-jét. De a Cowork-nek honnan tudja egy vadonatúj munkamenet, hogy egyáltalán hol keresse? Itt jön a **CLAUDE.md navigációs lánc**: egymásba ágyazott szabálykönyvek, mint a régi kalandkönyvekben, ahol minden szint megmondja, merre menj tovább.

A cél: egy új munkamenetben, **anélkül hogy bármit elmondanánk**, kérdezünk egy Napsugár-részletet, és az AI magától eljut a válaszig, mert végigolvassa a láncot.

## A három szint (a lánc)

1. **`RegioConsult/CLAUDE.md`** (gyökér): elmagyarázza az alap-struktúrát és a standardet, és azt, hogy a projektek a `Projects/` mappában vannak, mindegyiknek saját CLAUDE.md-jével.
2. **`RegioConsult/Projects/CLAUDE.md`** (index): felsorolja a projekteket és a kódjukat (pl. Napsugár Tejüzem → `THR_Napsugar_Tejuzem/`), hogy innen egyből tudni lehessen, melyik mappa melyik projekt.
3. **`RegioConsult/Projects/THR_Napsugar_Tejuzem/CLAUDE.md`** (projekt): a Napsugár konkrét adatai (ez az 1.2-ben született meg).

---

## 1. prompt: építsd fel a láncot

```
A RegioConsult munkakörnyezetben szeretném, hogy egy új munkamenet magától
eligazodjon. Építsük fel a CLAUDE.md navigációs láncot:

1. A RegioConsult gyökerébe írj egy CLAUDE.md-t, ami az Internal_Standard.docx
   alapján elmagyarázza az alap-struktúrát és a standardet (mappa-logika,
   elnevezés, formátum), és leírja, hogy a projektek a Projects/ mappában
   vannak, mindegyiknek saját CLAUDE.md-jével.
2. A Projects/ mappába írj egy CLAUDE.md-t (index): sorold fel a projekteket
   és a kódjukat (pl. Napsugár Tejüzem -> THR_Napsugar_Tejuzem/), hogy innen
   egyből lehessen navigálni a megfelelő projekthez.

A cél: ha valaki új munkamenetben a gyökérből indul, a láncon végigolvasva
eljusson bármelyik projekt saját CLAUDE.md-jéig, anélkül hogy elmondanánk neki
bármit.
```

Az AI megírja a gyökér- és az index-CLAUDE.md-t. Így a lánc teljes: gyökér → Projects index → projekt.

---

## 2. prompt: teszteld a láncot (ÚJ munkamenetben)

Nyiss egy **teljesen új chatet** (zárd be az előzőt), és semmit ne mondj el a projektről. Csak ennyit kérdezz:

```
Új munkamenet, semmit nem mondok el előre. Mennyi a Napsugár beruházás összege?
```

---

## Elvárt eredmény

Az AI **magától** végigmegy a láncon:
- Elolvassa a `RegioConsult/CLAUDE.md`-t → megtudja, hogy a projektek a `Projects/`-ben vannak.
- A `Projects/CLAUDE.md` indexből → megtudja, hogy a Napsugár a `THR_Napsugar_Tejuzem/` mappa.
- A `THR_Napsugar_Tejuzem/CLAUDE.md`-ből (vagy az általa hivatkozott devizből) → megmondja a beruházás összegét: **6 455 000 lej fără TVA** (7 681 450 cu TVA).

Nem kellett elmondanunk, hol keresse. A lánc elvezette.

---

## Önellenőrzés

- [ ] Létrejött a `RegioConsult/CLAUDE.md` (gyökér) és a `Projects/CLAUDE.md` (index).
- [ ] Az új munkamenet **nulla kontextussal** indult (semmit nem mondtunk a projektről).
- [ ] Az AI a láncon át eljutott a Napsugárig, és megmondta a beruházás összegét (6 455 000 lej).

---

## A WOW-pillanat

Egy vadonatúj beszélgetés, egyetlen kérdés, nulla háttér, és az AI mégis pontosan tudja a választ: mert a **rend és a tudás a fájlrendszerben él**, nem a fejünkben, és nem az adott chatben. A kalandkönyv-lánc bármilyen mély hierarchiában elvezeti a megfelelő helyre. Egy új kolléga is így venné át a projektet: a gyökértől lefelé, szintenként.

---

## Tanulás

**A CLAUDE.md nem egy fájl, hanem egy navigációs rendszer.** Egyetlen gyökér-CLAUDE.md-ből, láncolva, az AI eljut akármelyik projekt akármelyik részletéhez, anélkül hogy minden alkalommal elmondanánk, mi hol van. Ez a különbség a **tranzakció** (egy chat, ami elszáll) és a **rendszer** (egy struktúra, ami megmarad és elvezet) között. Ezt a láncot használjuk F2-F6-ig végig.

---

## Mi következik (F2)

A rendszer kész, az AI a gyökértől bármeddig elnavigál. De a napi munkában nem a mappák a kérdés, hanem a teendők. Az F2-ben egy belső egyeztetés leiratából csinálunk mentett, munkamenetek között élő feladatlistát.

## Otthoni elmélyítés
- `Feladat_1.4_Bonusz_Standard_CLAUDE.md`, a teljes belső standard egy workspace-szintű CLAUDE.md-be
- `Feladat_1.6_Bonusz_Biztonsagi_soprop.md`, érzékeny adat keresése minden projektben

**Verzió:** 2.0 (kalandkönyv-navigáció, 3 szintű lánc)
