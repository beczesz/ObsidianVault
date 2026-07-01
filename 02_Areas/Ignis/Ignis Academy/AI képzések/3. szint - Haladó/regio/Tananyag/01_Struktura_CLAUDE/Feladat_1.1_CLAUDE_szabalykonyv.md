---
title: "Feladat 1.1: A gyökér-CLAUDE.md: írd le a Regio sztenderdjét"
date: 2026-07-01
author: Becze Szabolcs
status: active
description: "F1 fő feladat: a résztvevők egyetlen prompttal leíratják az AI-val a Regio strukturált projekt-felépítését és belső sztenderdjét egy gyökér-CLAUDE.md szabálykönyvben, majd új session-ben tesztelik, hogy az AI valóban emlékszik-e rá. A meglévő fájlokat nem módosítjuk."
id: 5a2c7e91-3f68-4d40-b915-8c0e6a2d1f73
index_schema_version: 1
bdos_index: true
tags: [ignis-academy, halado, regio-consult, f1, feladat, claude-md]
---
# Feladat 1.1: A gyökér-CLAUDE.md: írd le a Regio sztenderdjét

> **Idő:** 12 perc · **Mód:** oktatói demó, majd mindenki saját gépén · **Eredmény:** egy `CLAUDE.md`, ami leírja a struktúrát és a belső sztenderdet

---

## Szituáció

Laci, a senior odaül melléd:

> *„Figyelj, minden projektünk ugyanígy néz ki, ez a mi erősségünk. De ha az AI-t akarjuk használni, valahogy meg kellene neki tanítani, hogy hogyan is működik nálunk minden. Hogy tudja, hova mit teszünk, mi a Verdana 9, meg az egész logika. Nem kézzel akarom elmagyarázni minden alkalommal."*

Megnyitod a `Napsugar_projekt/` mappát a Cowork-ben. Ott a teljes strukturált rendszer: `00_General_info`, `Projects/THR_Napsugar_Tejuzem/` a tíz alszámozott mappával. Az AI látja a fájlokat, de a **logikát** még nem érti.

---

## Cél

Egyetlen prompttal az AI:
- Végignézi a `Napsugar_projekt/` struktúráját.
- Felismeri a mintát (minden projekt azonos, számozott mappák, elnevezési konvenció).
- Ír egy **gyökér-`CLAUDE.md`-t**, ami leírja: kik vagytok, hogy néz ki egy projekt, mi a mappa-logika, mi az elnevezési és formátum-szabály (Verdana 9), hogyan navigáljon.
- **Semmit nem mozgat, nem módosít.** Csak leírja, ami már van, plusz párhuzamosan hozzáad egy szabálykönyvet.

---

## Hogyan csináld

### 1. lépés: Nyisd meg a Cowork-öt
- Indítsd el a Claude Cowork desktop alkalmazást.
- Add hozzá projekt-kontextusként a `Napsugar_projekt/` mappát a saját gépedről (OneDrive / SharePoint-ról szinkronizálva).
- Nyiss egy üres chat-tabot.

### 2. lépés: Másold be a promptot

```
A Regio Consult pályázati tanácsadó cégnél dolgozom. Minden projektünk
ugyanabban a strukturált, számozott mapparendszerben él (01_Cerere_de_finantare,
02_Editabil, ... 10_Monitorizare), és van egy belső sztenderdünk.

Nézd át a Napsugar_projekt mappát, és értsd meg a szervezési logikát:
- milyen mappák vannak és mi kerül melyikbe,
- mi az elnevezési konvenció a fájloknál,
- hogyan navigálnál egy konkrét projekthez.

Ezután írj egy CLAUDE.md fájlt a Napsugar_projekt gyökerébe, ami ezt a
szabálykönyvet tartalmazza, hogy minden új munkamenetben elsőként ezt
olvasva azonnal tudd, hogyan működünk. Fontos:

1. NE mozgass és NE módosíts egyetlen meglévő fájlt sem. Csak leírod, ami van.
2. A CLAUDE.md legyen rövid és gyakorlati (kb. 40-60 sor).
3. Írd bele a formátum-szabályt is: minden dokumentum Verdana 9.
4. A végére tegyél egy „navigáció" szekciót: ha egy konkrét projekten
   dolgozom, hova menj és mit olvass el ott.

Ha valami nem világos a struktúrából, kérdezz vissza.
```

### 3. lépés: Nézd meg mit csinál
Az AI ~1-2 perc alatt végigmegy a mappán és megírja a `CLAUDE.md`-t. Közben figyeld:
- Helyesen ismerte-e fel, mi kerül a `02_Editabil`-ba vs. `03_Documente_de_lucru`-ba?
- Elkapta-e a `04.04_DAL_Lucrari` beszerzési dosszié logikáját?
- Bekerült-e a Verdana 9 és az elnevezési konvenció?

### 4. lépés: Teszteld új session-ben (a WOW)
Nyiss egy **új chat-tabot** és írd be:

```
Új munkamenet. Olvasd el a CLAUDE.md-t, és mondd el röviden: kik vagyunk,
hogy néz ki egy projekt nálunk, és milyen formátum-szabályt kell követned.
```

Az AI most **fejből, a CLAUDE.md-ből** válaszol, anélkül hogy újra elmagyaráztad volna. Ez a memória.

---

## Önellenőrzés

- [ ] Létrejött a `Napsugar_projekt/CLAUDE.md`.
- [ ] Egyetlen meglévő fájl sem mozdult el (a struktúra érintetlen).
- [ ] A CLAUDE.md-ben szerepel a mappa-logika, az elnevezési konvenció és a Verdana 9.
- [ ] Új session-ben az AI a CLAUDE.md alapján helyesen összefoglalja a működést.

---

## A WOW-pillanat

Egy új munkatársnak fél nap, mire átlátja a rendszereteket. Az AI ezt **egyetlen olvasásból** megteszi, és **minden jövőbeli session-ben tudni fogja**. Nem kell újra elmondanod. A struktúra, amit néha tehernek éreztek, itt lesz a legnagyobb előny: pont azért írható le pontosan, mert tudatosan sztenderd.

---

## Tanulás

**A CLAUDE.md a kulcs.** Ez különbözteti meg a Cowork-öt a chatablaktól. Egyszer leírod a szabályokat, és az AI onnantól követi őket, generáljon bármit. A markdown azért ideális erre, mert ember és gép is olvassa: te szerkeszted, az AI érti.

**Bízz benne, de ellenőrizd.** Az AI leírta, ahogy értette. Ha valamit félreértett (pl. mi kerül az `Editabil`-ba), mondd meg, és javítsa. A szabálykönyv a tiéd, az AI csak megfogalmazza.

---

## Mi következik (F2)

A rendszer megvan, az AI tudja hogy néz ki egy projekt. De a napi munkában nem a mappák a kérdés, hanem a teendők. Épp most volt egy belső egyeztetés a Napsugárról, tele feladattal, kissé kaotikusan. Az F2-ben ezt alakítjuk mentett, session-ök között élő feladatlistává.

---

## Időkeret

- Bevezetés + prompt indítása: 3 perc
- AI dolgozik + átolvasás: 5 perc
- Új session teszt (WOW): 2 perc
- Kérdések: 2 perc
- **Össze: 12 perc**

**Verzió:** 1.0 (Regio adaptáció)
