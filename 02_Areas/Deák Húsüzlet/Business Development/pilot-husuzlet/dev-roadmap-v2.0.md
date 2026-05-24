---
title: DH Development Roadmap
version: 2.0
date: 2026-04-17
author: Becze Szabolcs
status: CANONICAL — egyesített egyetlen forrás igazság
supersedes: dev-roadmap-v1.5.md, sprint-5-6-review-2026-04-11.md, sprint-3-prioritization-2026-04-15.md, v0.4-v0.6-roadmap-plan.md
description: Egyesített DH roadmap Sprint 3 valós scope → v0.6, BMC v2.2 4-réteg mapping, ChatGPT+Claude konszenzus megtartva, Szabolcs tereptapasztalat beépítve.
id: 8272ecde-c467-4f7b-b36b-9e989746a12e
index_schema_version: 1
---

# DH Development Roadmap v2.0 — Canonical

> **„Ne azt optimalizáljátok, hogy mit tud az app — hanem hogy kialakul-e egy heti húsvásárlási szokás."** (ChatGPT + Claude konszenzus)

## 0. Miért v2.0?

Három dokumentum egyszerre élt (v1.5 roadmap, sprint-3-prioritization, v0.4-v0.6-roadmap-plan), amik között **tartalmi feszültségek** voltak:

1. **Sprint 3 scope eltérés** — a prioritization doc 4 ticketet MUST-nak jelölt, amik valójában nincsenek a Jira Sprint 3 scope-ban (DH-51, DH-121, DH-122, DH-139).
2. **v0.4 tartalma** — a régi v1.5 szerint: push + szezonális bundle + referral. Az új terep-alapú döntés: Natív Capacitor mobil app + Push infra + Mobile-first UX.
3. **Online fizetés timing** — v0.5 vagy v0.6? Döntés: **v0.6**, csak SCALE után.
4. **Referral program** — v0.4-ben vagy v0.4.1-ben? Döntés: **v0.4.1** (habit validáció után).

Ez a v2.0 feloldja a feszültségeket. Minden elavult doc `**` prefixet kap.

---

## 1. Stratégiai keret — BMC v2.2 4-réteg architektúra

| Réteg | Neve | Fókusz | DH fázis |
|-------|------|--------|----------|
| **L1** | **Decision Engine** | „Mit, mennyit, mikor" — az első rendelés meghozásához | v0.3 |
| **L2** | **Basket Optimization** | Kosár közben: spórolás, guardrail, swap | v0.3 + v0.4 |
| **L3** | **Habit Engine** | Visszatérés: reorder, familiar favourites, rutin | v0.4 + v0.4.1 |
| **L4** | **Activation & Recovery** | Push, referral, szegmentált újraaktiválás | v0.4.1 + v0.5 |

**North Star KPI:** Second Order Rate 14d ≥40%
**Stop cap:** ~12-13k EUR teljes kockázat
**Beta target:** ~2026-05-15 (v0.3 release után)

---

## 2. Sprint 3 — v0.3 „Savings Engine + Legal" (ACTIVE)

**Jira openSprint 2026-04-17:** 19 feature/task + 2 Epic
**Jelenlegi állás:** 5 Done / 1 IP / 13 To Do (26%)
**Release target:** ~2026-05-15

### 2.1 Savings Engine core (Epic 10 / DH-116 IP) — L1 + L2

| Ticket | Állapot | Leírás | Réteg |
|--------|---------|--------|-------|
| DH-117 | ✅ Done | Running Savings Counter BE | L2 |
| DH-118 | ✅ Done | Running Savings Counter FE | L2 |
| DH-119 | 🟡 IP | Post-order Recap | L3 (híd L2→L3) |
| DH-120 | To Do | Reorder Basket Loader + merge modal | L3 |
| DH-123 | To Do | Rendeléseim — Spórolás badge + újrarendelés | L3 |
| DH-129 | To Do | Savings Engine Firebase eventek (10) | Infra |

### 2.2 Legal & Compliance (Epic DH-138) — beta-blokkoló

| Ticket | Állapot | Leírás |
|--------|---------|--------|
| DH-130 | To Do | ÁSZF |
| DH-131 | To Do | Impresszum |
| DH-132 | To Do | GDPR consent checkbox |
| DH-133 | To Do | Jogi szolgáltató tisztázás (BLOCKER) |
| DH-136 | To Do | ANSVSA szállítási engedély |
| DH-137 | To Do | Cookie policy |

### 2.3 Mérés / Infra

| Ticket | Állapot | Leírás |
|--------|---------|--------|
| DH-145 | To Do | Firebase + GDPR cookie banner spec (web + Capacitor) |

### 2.4 v0.2 maradék / UX

| Ticket | Állapot | Leírás |
|--------|---------|--------|
| DH-112 | To Do | Guest checkout |
| DH-143 | To Do | Vezérlőpult — Wireframe gyorslink |

### 2.5 Sprint 3 nyitott döntés

**DH-51 — Szállítási zóna (Székelyudvarhely + 10 km).** Jelenleg Backlog, de beta előtt MUST. **Javaslat: Sprint 3-ba behúzni** a Delivery Risk mitigáció miatt.

### 2.6 Sprint 3 zárási kritériumok

1. Epic 10 (DH-116) minden child Done
2. Legal sub-track: DH-130→133, 136, 137 Done
3. DH-145 cookie banner implementálva
4. DH-112 + DH-143 Done
5. DH-51 döntés megszületik és (ha Sprint 3) implementálva
6. v0.3 release tag
7. Beta aktiválás: első 30 user meghívása
8. v0.4 ticketesítés megtörténik

---

## 3. v0.3.1 — Post-beta bug fix + QoL (1-2 hét)

**Időkeret:** beta után 2 hét (~máj. 15 – máj. 28)
**Cél:** az első 30 user visszajelzései alapján azonnali stabilizálás.

### 3.1 MUST

- Bug backlog a beta-ból
- DH-139 — Rendelésszám egyszerűsítés (QoL)

### 3.2 SHOULD (ha kapacitás)

- DH-121 — Family Bundles vásárlói nézet
- DH-122 — Family Bundles admin CRUD

**Kihagyva v0.3.1-ből:** minden nem user-facing stabil feature.

---

## 4. v0.4 — „Mobil + Push + Mobile-first UX" (3 hét)

**Időkeret:** ~máj. 28 – jún. 18
**Prioritás: #1 — ez a pilot sorskérdése** (L3 + L4 előkészítés)
**Szabolcs döntés 2026-04-17:** Natív Capacitor mobil app + Push notification infra + Mobile-first UX finomítás

### 4.1 Miért a mobil app a v0.4 magja?

1. **A userek nem tudják, hogyan kell PWA-t installálni** — személyesen látva
2. **URL-t nem fogják beírni a böngészőbe** — nincs visszatérés
3. **Push nélkül nincs non-spam kommunikáció**
4. **A Capacitor verzió már belsőleg létezik** — 1-2 hét, nem hónapok
5. **AI velocity 10x** (velocity-tracker-v1.2 bizonyítva)

### 4.2 v0.4 scope

| Feature | BMC réteg | Forrás | Érv |
|---------|-----------|--------|-----|
| **Natív mobil app (Capacitor)** | L3 + L4 infra | Szabolcs döntés | Nélküle nincs visszatérő user |
| **Push notification infra** | L4 | Base Ideas + ChatGPT | Egyetlen nem-spam csatorna |
| **Mobile-first UX finomítás** | UX | Szabolcs | Néhány screen mobilra optimalizálás |
| **DH-127 Familiar Favourites** | L3 | Base Ideas (promoted MUST) | „Szokásos rendelésem" gomb — habit trigger |

### 4.3 v0.4 pre-kickoff blokkolók (MUST mielőtt az app store-ba kerül)

| Ticket | Leírás |
|--------|--------|
| DH-134 | Privacy Policy frissítés (push + device) |
| DH-135 | App Store developer account + compliance |

### 4.4 v0.4 explicit NEM tartalmaz

- ❌ **Reorder trigger** (user kérés alapján — nem az app-ban, hanem később push-on át)
- ❌ Online fizetés (v0.6)
- ❌ Email drip (Szabolcs: „nem spammelünk")
- ❌ Recommendation engine (nem tudunk eleget 37 termékről)
- ❌ Gamification / streak (túl korai)

---

## 5. v0.4.1 — „Habit validáció + Referral" (2 hét)

**Időkeret:** ~jún. 18 – júl. 2
**Prioritás: #2 — a SCALE döntéshez adat kell** (L3 + L4)
**Arány javaslat:** 60% stabilizálás / 40% új feature (ChatGPT+Claude)

### 5.1 v0.4.1 scope

| Feature | BMC réteg | Forrás | Érv |
|---------|-----------|--------|-----|
| **J3 — Repeatability score** | Belső mérés | Base Ideas (7.65) | Melyik user hányszor rendel, milyen ciklusban |
| **B1 — Heti csomagok v2** | L1 + L3 | Base Ideas (7.45) | ChatGPT: „NEM bundle — ez habit trigger" |
| **C2 — Referral program (egyszerű)** | L4 | Base Ideas (7.55) | Kisváros → network effect, legolcsóbb acquisition |
| **Post-delivery push** (DH-125 adaptálva) | L4 | „Ízlett? Rendeld újra!" | 48 órával szállítás után |

### 5.2 v0.4.1 learning kérdések

- Kialakul-e rutin? (heti? kétheti?)
- Van-e „default order"? (ismétlődő kosár)
- Mikor rendel újra? (milyen trigger után)
- Melyik push működik?

---

## 6. v0.5 — „SCALE döntés" (3 hét, pilot adat-alapú)

**Időkeret:** ~júl. 2 – júl. 23
**Prioritás: #3 — csak ha v0.4/v0.4.1 pozitív**

### 6.1 Döntési logika

| Eredmény | Kritérium | Akció |
|----------|-----------|-------|
| **SCALE** | ≥50 reg + ≥20 visszatérő (14d újra) | v0.5 SCALE branch |
| **PIVOT** | Részben teljesül | Elemzés, modell módosítás |
| **STOP** | <10 reg, <5 rendelés | Pilot lezárás, max 12-13k EUR |

### 6.2 Ha SCALE — v0.5 scope

| Feature | BMC réteg | Érv |
|---------|-----------|-----|
| **Light recommendation** | L1 | „Akik ezt rendelték, ezt is szokták" — rendelési adatból |
| **Shared basket pilot** | L3 | Családi rendelés összevonás |
| **A5 — Seasonal savings** | L2 | Húsvét, grillszezon, karácsony |
| **DH-128 — Swap suggestion MVP** | L2 | „Cseréld erre, X lejt spórolsz" |

### 6.3 Ha PIVOT

- Elemzés: supply? delivery? ár? szokás?
- Possible pivot: B2B irány (éttermek, intézmények)
- Possible pivot: csak bundle/csomag modell

### 6.4 Ha STOP

- Lezárás, tanulságok dokumentálása
- Stop cap: 12-13k EUR-nál nem megyünk tovább

---

## 7. v0.6 — „Növekedés + Payment" (csak SCALE után)

**Időkeret:** ~júl. 23+
**Prioritás: #4**

| Feature | BMC réteg | Érv |
|---------|-----------|-----|
| **Online fizetés** | Infra | Csak ha bizonyított demand. Addig készpénz. |
| **I4 — Margin guardrail** | L2 | Deák nem veszíthet a kedvezményeken |
| **„Szokásos rendelésem" v2** (+ DH-127 extensions) | L3 | Egy gombos rendelés |
| **J4 — Predictive restock** | L4 | „Múlt héten csirkemell — kell megint?" |
| **LocalBasket vízió** (1 platform, 2 mód) | Stratégia | Csak ha DH sikeres |

---

## 8. Kockázatok (ChatGPT megerősítve)

> „A siker NEM a feature-eken múlik."

| # | Kockázat | Hatás | Mitigáció |
|---|----------|-------|-----------|
| 1 | **Supply mismatch** | Nincs elérhető termék → nincs 2nd order | Product availability toggle (Sprint 2 ✅), napi kapacitás egyeztetés |
| 2 | **Delivery experience** | Késik, pontatlan → trust broken | Delivery time slot (v0.5), addig manuális koordináció, DH-51 zóna |
| 3 | **Overpromise savings** | User nem érzi → „átvertek" érzés | Savings guardrail a v0.3-ban, kommunikáció finomítás |
| 4 | **Behavior mismatch** | User nem akar előre tervezni | Első 30 user a válasz — pivot trigger |
| 5 | **Supply-side konfliktus** | Két testvér konfliktusban → operáció leáll | ✅ Revenue share megállapodva 2026-04-15 (Customer 3% / Platform 6.6% / Deák 9.9%), írásbeli formalizálás hátravan |

---

## 9. Amit tudatosan kihagyunk (ChatGPT+Claude konszenzus)

| Ötlet | Miért NEM most |
|-------|---------------|
| Gamification (streak, badge) | Túl korai, „empty calories" |
| Complex recommendation | 37 termék túl kevés |
| Milestone rendszer | Előbb bizonyítsuk a repeat behavior-t |
| NPS | 30 user-nél nincs statisztikai értelme |
| Email drip | Szabolcs: „nem spammelünk" — push jobb |
| Multi-vendor / LocalBasket | Csak ha DH sikerül |

---

## 10. Összesítő timeline

| Fázis | Hét | Verzió | BMC réteg | KPI fókusz |
|-------|-----|--------|-----------|-----------|
| Sprint 3 befejezés | ápr. 17 – máj. 15 | v0.3 | L1+L2+L3 alapok | Sprint completion |
| Beta launch | máj. 15 – máj. 28 | v0.3 beta | L1+L2+L3 mérés | 30 reg / 15 order |
| Post-beta stabilizálás | máj. 28 – jún. 18 | v0.3.1 | bug fix | 2nd order kezdet |
| **Mobil + Push + UX** | jún. 18 – júl. 2 | **v0.4** | **L3+L4 infra** | Repeat behavior |
| Habit + Referral | júl. 2 – júl. 16 | v0.4.1 | L3+L4 | **2nd order ≥40%** |
| **SCALE döntés** | júl. 16 – jún. 6 | v0.5 | — | Pilot outcome |
| (Ha scale) Növekedés | aug. 6+ | v0.6 | L1–L4 teljes | Revenue |

---

## 11. Canonical dokumentumok

| Path | Leírás |
|------|--------|
| `01_PROJECT_STATE.md` | Állapot snapshot (v1.5) |
| `TASKS.md` | Teljes task inventory (Jira sync) |
| `CLAUDE.md` | AI memória |
| `Business Development/pilot-husuzlet/BMC-v2.2.md` | Business Model Canvas |
| `Business Development/pilot-husuzlet/KPI Framework - v1.3.md` | KPI framework |
| `Business Development/pilot-husuzlet/velocity-tracker-v1.2.md` | AI velocity benchmark |
| `Business Development/pilot-husuzlet/legal.md` | Jogi követelmények |
| `Business Development/pilot-husuzlet/sprint-2-retrospective-2026-04-15.md` | Sprint 2 retro |

### Elavult dokumentumok (`**` prefix, törlésre jelölve)

- `**dev-roadmap-v1.5.md`
- `**sprint-5-6-review-2026-04-11.md`
- `**sprint-3-prioritization-2026-04-15.md`
- `**v0.4-v0.6-roadmap-plan.md`

---

## 12. Változás log vs. v1.5

| Téma | v1.5 | v2.0 |
|------|------|------|
| Sprint 3 scope | 22 MUST (paper) | 19 Jira valós + 1 nyitott döntés (DH-51) |
| v0.4 tartalma | Push + bundle + referral | **Natív Capacitor app + Push infra + Mobile-first UX** |
| Reorder trigger | v0.4 | v0.4.1 (post-delivery push) |
| Online fizetés | v0.5 | v0.6 (csak SCALE után) |
| Referral program | v0.4 | v0.4.1 (habit validáció után) |
| Revenue share | Missing (blocker) | ✅ Agreed 2026-04-15 |
| v0.4 mobile blokkolók | Nem említve | **DH-134, DH-135** pre-kickoff MUST |
| Epic 10 (Savings) | Full roadmap | 5/7 child-ben állás: 2 Done + 1 IP + 4 To Do |
| Family Bundles (DH-121, 122) | Sprint 3 MUST | v0.3.1 SHOULD |
| Familiar Favourites (DH-127) | Sprint 3 MUST | v0.4 MUST (promoted) |
| DH-139 egyszerűsítés | Sprint 3 MUST | v0.3.1 QoL |

---

## 13. Egy mondatos irány

> **„Ne azt optimalizáljátok, hogy mit tud az app — hanem hogy kialakul-e egy heti húsvásárlási szokás."**
