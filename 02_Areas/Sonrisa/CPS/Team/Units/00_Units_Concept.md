---
title: "CPS Unit-alapú Működés"
date: 2026-03-21
author: Becze Szabolcs
status: active
description: "A CPS unit-alapú működési modelljének draft dokumentuma, amelyből a csapat megérthet egy kis, kliens-dedikált csapatokat létrehozó szervezési megközelítést és annak soft skill fejlesztési lehetőségeit."
description_source: auto
description_hash: 80e5ca0c940c58cc
id: d2929f32-7210-489b-8a18-903c92ea63a2
index_schema_version: 1
bdos_index: true
---
# CPS Unit-alapú Működés

**Verzió:** 0.1 (draft - csapat workshopra)
**Dátum:** 2026-03-21
**Státusz:** Kidolgozás alatt

---

## Mi az a Unit?

Egy Unit egy kis, önállóan működő csapat a CPS-en belül, amely dedikáltan kiszolgál egy klienst vagy kliens-típust. A Unit nem egy merev szervezeti egység, hanem egy működési modell: meghatározza, hogy ki felelős kinek, hogyan kommunikálunk a klienssel, és hogyan szervezzük a munkát.

A BMC-ben (v1.3) megjelenik a "Unit Lead" fogalma: az Essential és magasabb csomagokban a Unit Lead account manager szerepet tölt be, koordinálja a check-ineket és a stratégiai egyeztetéseket.

---

## Miért van szükség unitokra?

### A kettős stratégia logikája

CPS két irányban fog növekedni egyszerre:

**Enterprise kliensek (kevés, nagy):**
- Stabil, hosszú távú, magas bevétel
- Komoly SLA elvárások
- Senior/Expert szintű munka
- Személyes bizalom az alap

**Kis kliensek (sok, kisebb):**
- Kísérletező terep: itt próbáljuk ki az eszközöket, a munkamódszereket
- Ha hibázunk, a hiba hozadéka kicsi
- Juniorok könnyebben bevonhatók, tanulnak éles környezetben
- Előkészíti az enterprise világát: kipróbált módszerek, kész playbook-ok

### A soft skill probléma

Felismertük, hogy **sok kis kliensnél kiemelten fontosak a soft skillek**:
- Más kommunikáció kell egy kis startupnál, mint egy enterprise-nál
- Gyorsabb onboarding, direktebb kapcsolat, kevesebb bürokrácia
- A Unit tagjai tanulnak meg "klienssel dolgozni" alacsony kockázat mellett
- Ez a tapasztalat az enterprise kapcsolatokban hasznosul majd

---

## A Unit felépítése (tervezett)

### Unit Lead
- Felelős a klienskapcsolatért (account manager szerep)
- Koordinálja a Unit munkáját
- Részt vesz a check-ineken és stratégiai egyeztetéseken
- Eszkalál, ha szükséges
- Tipikus szint: Senior/Expert (E5+)

### Unit tagok
- 2-3 engineer per kliens (a csomag méretétől függően)
- Kis kliensnél: 1 Senior/Expert + 1 Junior
- Nagyobb kliensnél: 1 Lead + 1-2 Expert/Advanced
- A Junior tanul, a Senior/Expert minőséget garantál

### Unit összetétel - kliens típus szerint

| Kliens típus | Csomag | Unit Lead szintje | Unit tagok |
|---|---|---|---|
| Kis startup | Essential (€2K) | Advanced/Expert | 1 Expert + 1 Junior |
| Mid-sized | Growth (€4K) | Senior/Lead | 1 Expert + 1 Advanced |
| Enterprise | Scale (€6K+) | Senior Lead | 2 Expert + 1 Advanced |
| Safety Net | Safety Net (€990) | Expert | 1 Expert (shared) |

---

## Soft skill fejlesztés a unitokban

Ez az egyik legfontosabb felismerés: **a soft skilleket tanulni kell, és a kis kliensek az ideális "edzőterep"**.

### Mit kell fejleszteni?
- Kliens elvárások kezelése (mit mond, mit ért alatta)
- Proaktív kommunikáció: nem meglepetés, hanem előre jelzett változás
- Problémák magyarázata nem-technikai embereknek
- Rossz hírek közlése konstruktívan
- Check-in meeting levezetése
- Upsell felismerése és természetes ajánlása

### Hogyan fejlesztjük?
- Juniort mindig visz magával a Unit Lead az első kliens-találkozókra
- Retrospektív minden nagyobb kliens-interakció után (mi ment jól, mi nem)
- Belső soft skill workshop (téma: CPS értékek a kliens kapcsolatban)
- Szerepjáték: szimulált nehéz kliens szituációk

---

## Unit és a két kliens-típus kapcsolata

```
ENTERPRISE kliensek                    KIS kliensek
─────────────────────                  ────────────
Stabil hosszú bevétel          <──>    Kísérletező terep
Senior-heavy Unit                      Junior-inclusive Unit
Kevesebb kliens                        Sok kliens
Magasabb kockázat                      Alacsony kockázat
Kész, bizonyított folyamat      ←───   Tesztelés, tanulás
```

A kis klienseknél kipróbált eszközök, playbook-ok és kommunikációs minták bekerülnek az enterprise működésbe.

---

## Nyitott kérdések (workshopra)

1. **Hány Unit legyen?** Jelenleg hány aktív kliensünk van? Ezek hogyan csoportosíthatók?
2. **Ki legyen Unit Lead?** Ceclan, Szántó, Póda a jelöltek a nagyobb klienseknél -- de a kis kliensnél ki?
3. **Junirok elosztása:** A 2 új E1-es junior melyik unitba kerüljön, és ki mentorál?
4. **Soft skill training formátuma:** Workshop, peer coaching, vagy beépítjük a check-inekbe?
5. **Unit autonómia:** Mennyi döntési jogköre van egy Unit Lead-nek a kliens felé anélkül, hogy eszkalálni kelljen?
6. **Eszközök:** Jira board per Unit? Közös dashboard? Hogyan látjuk a teljes képet?

---

## Következő lépések

- [ ] Mai workshop: unit koncepció megvitatása a csapattal
- [ ] Jelenlegi kliensek felmérése: kik illeszkednek kis vs. enterprise kategóriába
- [ ] Unit Lead szerepkör formalizálása
- [ ] Soft skill fejlesztési terv kidolgozása
- [ ] Pilot: 1-2 kis kliensnél próbáljuk ki a unit modellt

---

*Ez egy élő dokumentum. A mai csapat-megbeszélés után frissítjük.*
