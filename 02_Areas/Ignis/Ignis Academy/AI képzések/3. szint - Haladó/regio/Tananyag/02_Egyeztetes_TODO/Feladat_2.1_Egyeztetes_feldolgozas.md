---
title: "Feladat 2.1: Egyeztetés-leirat → mentett feladatlista (DEMO)"
date: 2026-07-01
author: Becze Szabolcs
status: active
description: "F2 oktatói demó: egy nyers Napsugár-egyeztetés leiratából az AI felelősökkel, forrásokkal és határidőkkel ellátott feladatlistát készít, elmenti a projektbe, majd új session-ben visszaidézi. A kontextus-perzisztencia bemutatása."
id: b18f3357-9026-4a07-8e7b-5d6f4e8c3c19
index_schema_version: 1
bdos_index: true
tags: [ignis-academy, halado, regio-consult, f2, feladat, demo]
---
# Feladat 2.1: Egyeztetés-leirat → mentett feladatlista (DEMO)

> **Típus:** 🎤 OKTATÓI DEMO (a résztvevők figyelnek, kérdeznek) · **Idő:** ~12 perc

---

## Szituáció

Az egyeztetésen Laci és Kinga átvették a Napsugár állását: megjött a szkennelt ajánlat, a deviz 4.6-os sora hiányzik, az SL1 még nincs bevezetve a Centralizatorba, a monitorizare raport a hónap végéig kell, és egy fájl rossz helyen van. Ez egy tipikus, gyors, kissé kaotikus megbeszélés, tele apró teendővel, amiket másnapra mindenki felében elfelejt.

A leirat itt van: `egyeztetes_Napsugar.md`.

---

## A demó menete

### 1. lépés: Az AI kinyeri a feladatokat

Az oktató bemásolja:

```
Itt egy belső egyeztetés leirata a Napsugár projektről: egyeztetes_Napsugar.md

Olvasd el, és készíts belőle egy strukturált feladatlistát. Minden feladathoz:
- mi a teendő (röviden, cselekvő megfogalmazásban),
- ki a felelős,
- van-e határidő,
- melyik fájl / mappa a forrás vagy az érintett hely.

A kimenet checkbox-os markdown lista legyen. Mentsd el a projektbe
feladatok_Napsugar.md néven. A belső sztenderdet (Verdana 9) itt még nem
kell alkalmazni, ez belső munkajegyzet.
```

Az AI ~1 perc alatt kiadja a strukturált listát (vö. `Pelda_output/feladatok_EREDMENY.md`): 5 nyitott feladat, felelősökkel (Kinga / Laci), forrásokkal (Scan mappa, deviz), és a formátum-emlékeztetővel (Verdana 9 a kimenő raportnál).

### 2. lépés: A WOW: emlékszik (kontextus-perzisztencia)

Az oktató nyit egy **új chat-tabot**:

```
Új munkamenet. A Napsugár projekten dolgozom. Mik a nyitott feladataim?
```

Az AI a mentett `feladatok_Napsugar.md`-ből válaszol, priorizálva. Nem kellett újra bemásolni a leiratot: a feladat a projektben él, a következő alkalommal is ott lesz.

---

## Amit a résztvevők megfigyelnek

- Hogyan bontja szét az AI a folyó beszédet **cselekvő feladatokra** (nem szó szerinti idézet, hanem teendő).
- Hogyan párosít **felelőst** és **forrást** anélkül, hogy külön megmondanánk.
- Hogyan válik a lista **perzisztenssé**: a chat bezárható, a feladat marad.

---

## Tanulás

Egy megbeszélés értéke a **utólagos rögzítésben** van, és pont ez az, ami a napi hajtásban elveszik. Az AI a nyers leiratból percek alatt csinál számonkérhető listát, és a Cowork-ben ez **nem egy eldobható chat**, hanem a projekt része. Holnap, jövő héten is ott lesz.

---

## Mi következik (F2 stáció)

Most a résztvevők jönnek: a kinyert feladatlistából mindenki készít egy saját follow-up dokumentumot (feladat-kártya vagy rövid státusz-jegyzet), immár a belső sztenderddel.

---

## Időkeret
- Feladat-kinyerés demó: 4 perc
- Új session / emlékszik (WOW): 3 perc
- Megbeszélés, kérdések: 5 perc
- **Össze: 12 perc**

**Verzió:** 1.0 (Regio adaptáció)
