---
title: "Feladat 1.1: Audit, rendben vannak-e a projektek? (DEMO + hands-on)"
date: 2026-07-02
author: Becze Szabolcs
status: active
description: "F1 első feladat: a résztvevők a Internal_Standard.docx alapján auditáltatják az AI-val a RegioConsult 3 projektjét. A két rendezett projekt (PAN, KER) zöld pipát kap, a Napsugár (THR) nem: az AI listázza az eltéréseket (hiányzó mappák, rossz fájlnevek, duplikátumok, oda nem illő és érzékeny fájlok, pl. jelszavak.txt). Semmit nem módosít, csak jelez."
id: 5a2c7e91-3f68-4d40-b915-8c0e6a2d1f73
index_schema_version: 1
bdos_index: true
tags: [ignis-academy, halado, regio-consult, f1, feladat, audit, standard]
---
# Feladat 1.1: Audit, rendben vannak-e a projektek? (DEMO + hands-on)

> **Idő:** 10 perc · **Mód:** oktatói demó, majd mindenki saját gépén · **Eredmény:** egy audit-riport, projektenként zöld/piros

---

## Szituáció

Laci, a senior odaül melléd:

> *„Három aktív projektünk fut. Kettő rendben van, de a Napsugárba a nyáron mindenki csak bedobálta a fájlokat, és most katasztrófa. Van egy írott belső standardünk, az `Internal_Standard.docx`. Meg tudnád nézni az AI-jal, hogy melyik projekt felel meg neki és melyik nem? Egyelőre ne javíts semmit, csak mondd meg, hol a baj."*

Megnyitod a `RegioConsult/` mappát a Cowork-ben. Látod a három projektet és a standard-dokumentumot.

---

## Cél

Az AI:
- Elolvassa a `Internal_Standard.docx`-et (mi a mérce: mappa-struktúra, elnevezés, formátum, tiltott fájlok, CLAUDE.md).
- Végignézi a három projektet, és mindegyikre megmondja: **megfelel-e a standardnek** (zöld) vagy **nem** (piros), és ha nem, **pontosan miért**.
- **Semmit nem módosít.** Csak auditál.

---

## Hogyan csináld

### 1. lépés: Nyisd meg a Cowork-öt
- Add hozzá kontextusként a `RegioConsult/` mappát.
- Nyiss egy üres chatet.

### 2. lépés: Másold be a promptot

```
A RegioConsult mappában, a Projects/ alatt három projekt van. Van egy írott
belső standardünk is: Internal_Standard.docx.

Olvasd el a standardet, majd nézd át mind a három projektet, és döntsd el
magad, melyik felel meg neki és melyik nem. Nem én mondom meg, mit keress:
te hasonlítsd össze a projekteket a standarddal, és amit találsz, azt jelezd.

A végén adj egy összefoglalót projektenként:
- ✅ ha a projekt megfelel a standardnek,
- ❌ ha nem, és alatta sorold fel pontosan, mit találtál, ami eltér.

Ne javíts és ne mozgass semmit, csak nézz és jelezz.
```

### 3. lépés: Nézd meg az eredményt
Az AI ~1-2 perc alatt kiadja a riportot. Amit várunk:
- **PAN_Malomkert_Panzio**: ✅ megfelel (10 mappa, szabályos nevek, CLAUDE.md, nincs szemét).
- **KER_Zold_Kerteszet**: ✅ megfelel.
- **THR_Napsugar_Tejuzem**: ❌ nem felel meg. Az AI listázza: nincs meg a 10 mappás struktúra (minden a gyökérben van), rossz fájlnevek (`deviz general JAVITOTT vegleges.xlsx`), duplikátumok (`Copy of anexa b.xlsx`, régi `NE HASZNALD`), nincs CLAUDE.md, és oda nem illő fájlok (`paprikas_krumpli_recept.txt`, `csaladi nyaralas 2024.txt`). **Kiemelten:** `jelszavak.txt` érzékeny adat, biztonsági kockázat.

---

## Önellenőrzés

- [ ] Az AI elolvasta a `Internal_Standard.docx`-et (hivatkozik a szabályokra).
- [ ] A két rendezett projekt **zöld** (megfelel).
- [ ] A Napsugár **piros**, konkrét eltérés-listával.
- [ ] Külön jelezte a **jelszavak.txt** biztonsági kockázatát.
- [ ] Semmit nem módosított (a fájlok érintetlenek).

---

## A WOW-pillanat

Egy standard-audit kézzel, három projekten, fájlról fájlra, fél óra fejfájás. Az AI a **leírt standardből** (docx) percek alatt megmondja, melyik projekt hol tér el, sőt a **biztonsági kockázatot** is kiszúrja, amit egy fáradt szem könnyen átugrik. És mindezt úgy, hogy egyetlen fájlhoz sem nyúl: előbb látjuk a bajt, csak utána döntünk a javításról.

---

## Tanulás

A jó munkafolyamat először **auditál**, csak utána **javít**. Az AI ideális auditor: nem fárad el, a leírt szabályt következetesen alkalmazza, és a kényes dolgokat (érzékeny adat) is jelzi. A két rendezett projekt itt egyben a **mérce** is: megmutatja, hogy néz ki a jó, amihez a Napsugárt igazítjuk.

---

## Mi következik (1.2)

Most, hogy tudjuk pontosan hol a baj, jöhet a rendrakás: a Napsugárt a standard szerint rendbe tesszük, biztonságba helyezzük a jelszavakat, a szemetet Kukába tesszük, és a rendet beírjuk egy CLAUDE.md-be.

---

## Időkeret
- Bevezetés + prompt: 3 perc
- AI auditál + átolvasás: 4 perc
- Megbeszélés (mi a piros és miért): 3 perc
- **Össze: 10 perc**

**Verzió:** 2.0 (standard-audit ív)
