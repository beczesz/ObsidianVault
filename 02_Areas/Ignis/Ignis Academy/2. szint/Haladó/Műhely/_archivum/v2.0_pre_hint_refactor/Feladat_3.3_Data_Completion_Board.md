---
title: "Feladat 3.3 — Data Completion Board"
date: 2026-05-14
author: Becze Szabolcs
status: active
description: "Az oktató a Data Completion Board demót mutatja, amely az eligibility és gap analízis outputjaiból összevonja a 14 határidős feladat, 8 felelős és 3 kockázat egy 3-fázisú akciótervre. Ez egy klasszikus projektmenedzsment-eszköz, amely a beadás előtti, alatti és utáni feladatokat szervezeli."
description_source: auto
description_hash: b67a28f1d1e544bf
id: fb51f526-e716-4be2-9fda-461945e8dcfc
index_schema_version: 1
bdos_index: true
---
# Feladat 3.3 — Data Completion Board

> **Típus:** 🎤 OKTATÓI DEMO (a kivetítőről nézed)
> **Idő:** ~3 perc · **Hozzád tartozik:** csak figyelés + átmenetre felkészülés

---

## Mit látsz a kivetítőn

Az oktató összeolvasztja az F3.1 (eligibility tábla) + F3.2 (17 melléklet) outputjait egy **Data Completion Board**-ba:
- **Oszlopok:** Tétel · Felelős · Határidő · Forrás · Státusz
- **Csoportosítás:** BEADÁS ELŐTT / ELBÍRÁLÁS ALATT / MEGVALÓSÍTÁS ALATT

Ez a táblázat **a következő 7 nap akcióterve**. Pontosan tudjuk:
- **8 felelős** (Márton, Enikő, Mihaela, Béla bácsi, Bíró Attila, és pár külső szereplő)
- **14 határidős feladat**
- **3 fő kockázat** (telephely-stabilitás, pénzügyi adatok, bankgarancia)

---

## A prompt amit az oktató használ

```
Az eligibility + gap analízisből generálj Data Completion Board-ot:
oszlopok = Tétel, Felelős, Határidő, Forrás, Státusz. Csoportosítsd
3 fázis szerint: BEADÁS ELŐTT / ELBÍRÁLÁS ALATT / MEGVALÓSÍTÁS ALATT.
```

---

## Üzenet a workshop ritmusához

Az oktató mondja: *„Ezt egy tanácsadó **3000 EUR**-ért adná. 5 perc, ingyen. **De most jön a neheze**: ezeket az adatokat be is kell szerezni. Email a könyvelőnek románul, szerződés-ellenőrzés, prezentáció Mártonnak."*

→ **Átmenet F4-be.**

---

## Tanulás

- A **Data Completion Board** nem új AI-funkció — egy **klasszikus projektmenedzsment-eszköz** (RACI mátrix, action register). Az AI újdonsága: **automatikusan generálja az előző fázisok kimenetéből**.
- A 3-fázisú csoportosítás (beadás előtt / alatt / után) **kockázatkezelés-első** megközelítés: már a beadás napján tudjuk, mire kell figyelni hónapok múlva.

---

**Verzió:** 2.0 (instructor-led + stáció modell)
