---
title: DH Savings Engine — Kockázatok
version: 1.1
date: 2026-04-15
note: Sprint 2 close után frissítve. Néhány kockázat csökkent (analytics létezik), néhány új (élesben mérünk).
id: c7ca3e3e-2a50-4ab7-92de-6ef66f517fa4
index_schema_version: 1
---

# DH Savings Engine — Kockázat audit (v1.1)

## 1. Supply nincs bekötve

→ jelenleg:
- frontend okos
- backend vak

→ ez hosszú távon bukás

**Megoldás:**
- v0.3 Savings Engine: a Decision Engine (L1) és Basket Optimization (L2) feature-ök frontendje épül
- v0.4-v0.5: backend supply visibility (carcass balance, készlet sync)

---

## 2. Complexity explosion

→ 60 feature = unusable product

**Megoldás:**
→ 1 core loop:

Kosár → Progress → Ajánlás → Reward

→ v0.3 max 6-7 feature (lásd v0.3-release-plan.md)

---

## 3. ✅ Megoldva — Analytics vakság

> ~~A KPI-okat mérjük, de nincs valós idejű dashboard.~~
>
> **Sprint 2 close (2026-04-15):** Firebase Analytics SDK + UTM/QR tracking + KPI dashboard (DH-82) mind TELEPÍTVE. A v0.3 fejlesztés infra-kész, de a valódi mérés a beta launch (v0.3 után, ~máj. 15) kezdődik.

---

## 4. ÚJ — A pilot adatai megcáfolják a hipotézist

> **Új kockázat (Sprint 2 close óta):** Most már mérünk. Lehet, hogy a 30 napos pilot adatai NEM támogatják a Savings Engine hipotézist (Decision Engine ≠ Discount).

**Mérési kritérium (30 nap után):**
- Threshold achievement rate ≥30% → működik
- Suggestion acceptance rate ≥15% → működik
- Ha mindkettő <50% target → újragondolás kell a Sprint 3 mid-pointban

**Megoldás:** Mid-sprint review (Sprint 3 közepén, ~ápr. 30) → ha az adatok nem támogatják, scope csökkentés (csak NEW-1, NEW-3, NEW-4 kerül v0.3-ba).

---

## 5. Over-gamification

→ grocery ≠ játék

**Megoldás:** A "savings counter" funkcionális (RON), nem pontalapú. A "threshold nudge" ajánlás, nem badge. NEM gamification, hanem informáló UX.

---

## 6. ÚJ — Email policy ütközik a Savings Engine-nel

> A CLAUDE.md szigorú email policy-t ír elő: "max 1 értesítő email / user / hét."
>
> A Savings Engine NEW-6, NEW-7, NEW-8 ticketek mind email-alapúak.

**Megoldás:** Backlogban marad a 3 email-alapú ticket (DH-124, 125, 126). A v0.3 csak in-app savings recap-et használ (NEW-3 = DH-119). Email csak a pilot adatai alapján kerül ki.

---

## 7. Két testvér konfliktus → operatív blokk

> A Deák Húsmíves két tulajdonosa konfliktusban. Döntéshozó tisztázatlan.
>
> Ha a Savings Engine bevezetése változást igényel a működésben (pl. családi csomagok = új SKU), és nincs aki dönt → fejlesztés készen áll, de nem indul.

**Megoldás:** Sprint 3 elején (ápr. 16) találkozó kell egy döntésképes személlyel a Deák Húsmíves részéről. Ha nincs → csak az in-app feature-ök fejleszthetők (counter, threshold), a bundle/swap halasztandó.

---

## Összefoglaló — Risk register (frissítve 2026-04-15)

| # | Kockázat | Súly (1-5) | Trend Sprint 2 óta | Mitigation |
|---|----------|-----------|-------------------|-----------|
| 1 | Supply nincs bekötve | 4 | → | v0.4 backend supply visibility |
| 2 | Complexity explosion | 3 | ↓ csökkent | Max 6-7 feature v0.3-ban |
| 3 | Analytics vakság | — | ✅ MEGOLDVA | Sprint 2 close |
| 4 | Pilot adatok megcáfolják hipotézist | 3 | ↑ ÚJ | Mid-sprint review |
| 5 | Over-gamification | 2 | → | Funkcionális UX, nem pont |
| 6 | Email policy ütközés | 2 | ↑ ÚJ | 3 email ticket backlog |
| 7 | Partner döntés blokk | **5** | → | Találkozó kell ápr. 16 |
