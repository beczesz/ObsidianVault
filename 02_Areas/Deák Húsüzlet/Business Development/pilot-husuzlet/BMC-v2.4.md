---
title: Business Model Canvas -- Deák Húsmíves Online Platform (Pilot)
version: 2.4
date: 2026-05-03
author: Becze Szabolcs -- Exar Labs
collaborators: >
  ChatGPT (Deák GPT) -- BMC MEGA Review session (2026-05-03);
  Perplexity -- "Two-engine model" kutatás (15 forrás);
  Claude/Cowork -- szintézis és dokumentáció
description: >
  BMC v2.4 -- "Kétzónás lokális ellátási platform." Stratégiai átkeretezés:
  a DH nem csak városi kényelmi online húsrendelés, hanem egy kétzónás rendszer,
  ahol a város kényelmet, a falu elérhetőséget kap. A Falusi Route Pilot
  új customer segmentet, value propositiont, channel modellt, cost struktúrát
  és success metricseket hoz. Az alapvető döntéstámogató rendszer (v2.3) megmarad
  a városi zónában; a falusi zónában kiegészül elérhetőségi rendszerrel.
predecessor: BMC-v2.2.md (v2.3, 2026-04-04)
id: 99020457-af05-47ca-b417-a0f9ac8b81fb
index_schema_version: 1
---

# Business Model Canvas v2.4 -- Deák Húsmíves Online Platform (Pilot)

_Version: 2.4 | Last updated: 2026-05-03_
_Scope: DH pilot -- az online rendelési csatorna validálása + falusi route pilot._
_Framing: V2.0 = "build product" → V2.1 = "build system that learns" → V2.3 = "döntéstámogató rendszer" → **V2.4 = "kétzónás lokális ellátási platform"**_

---

## PLATFORM MISSZIÓ (FRISSÍTVE v2.4)

> _"A DHOP célja, hogy a friss, megbízható helyi termék ne csak a bolt közelében legyen elérhető, hanem a teljes régió számára kiszámítható módon jusson el az emberekhez. Egy olyan rendszert építünk, amelyben a vásárló időt, pénzt és döntési energiát takarít meg, a termelő stabilabb keresletet lát, a falusi közösségek pedig jobb hozzáférést kapnak minőségi helyi termékekhez."_

**Rövid:** DHOP = helyi friss hús, kiszámíthatóan, városba és falvakba.

**A DH nem a cél -- hanem a bizonyíték, hogy a LocalBasket működhet.**

---

## CORE DEFINÍCIÓ (FRISSÍTVE v2.4 -- kétrétegű)

> **A DH egy kétrétegű rendszer:**
> - **Városban:** döntéstámogató rendszer — optimalizálja a vásárlói döntéseket, az ebből származó margin előnyt visszaadja a felhasználónak.
> - **Falun:** elérhetőségi rendszer — megbízhatóan eljuttatja a minőségi helyi terméket oda, ahol eddig nem volt elérhető.

### Alapelv (változatlan)

- Nem kedvezményt adunk
- Nem akciózunk
- Nem olcsóbbak vagyunk

**→ Városban: jobb döntést segítünk hozni.**
**→ Falun: megbízható hozzáférést adunk.**

### Rendszer cél — kétzónás

| Zóna | Fő érték | Core mechanizmus |
|------|----------|------------------|
| Város (Udvarhely) | Kényelem + okosabb vásárlás | Savings Engine, threshold nudge, reorder |
| Falu (Keresztúri régió) | Elérhetőség + kiszámíthatóság | Fix csütörtöki route, közösségi bizalom |

### Stratégiai pozíció (frissítve v2.4)

| ❌ Nem vagyunk | ✅ Amik vagyunk |
|----------------|-----------------|
| Webshop | Döntéstámogató + elérhetőségi rendszer |
| Marketplace | Supply-demand összhangoló |
| Kedvezményplatform | Margin optimalizáló (város) + access provider (falu) |

### Core Loop — városi (változatlan v2.3-tól)

```
Kosár építés → Progress → Ajánlás → Visszajelzés → Újrarendelés
```

### Core Loop — falusi (ÚJ v2.4)

```
Route-day awareness → Tervezett rendelés → Csütörtöki kiszállítás → Elégedettség → Heti ritmus
```

### 4 rendszerréteg (változatlan v2.3-tól, elsősorban városi)

| Réteg | Név | Tartalom | Cél |
|-------|-----|----------|-----|
| 🔴 L1 | Decision Engine (Core UX) | Running savings counter, threshold nudge, post-order recap | Döntési feedback loop |
| 🟠 L2 | Basket Optimization | Családi csomagok, swap suggestion | Valódi optimalizáció |
| 🟡 L3 | Habit Engine | 1-click reorder, "Szokásos rendelésem" | Ismétlődő viselkedés |
| 🔵 L4 | Activation & Recovery | TTFO engine, post-delivery trigger, savings recap email | Aktiváció + visszahozás |

> **Megjegyzés:** Falun az L1 Savings Engine továbbra is működik (magasabb threshold: 200 RON), de a fő retention driver nem a savings, hanem a route reliability és a közösségi ajánlás.

### Záró elv (frissítve v2.4)

> **A DH nem olcsóbb — hanem okosabb. És nem csak közeli — hanem elérhető.**

---

## 0. Growth Flywheel (FRISSÍTVE v2.4 -- kétzónás)

### Városi flywheel (változatlan)

```
1. Megbízható, stabil supply (mindig van jó termék)
         ↓
2. Pozitív első rendelési élmény (gyors, egyszerű, pontos)
         ↓
3. Második rendelés (habit kezdete)
         ↓
4. Heti rutin kialakul ("csütörtökön rendelek húst")
         ↓
5. Növekvő rendelési volumen
         ↓
6. Supplier stabilabb és olcsóbban tud termelni
         ↓
7. Jobb ár + jobb elérhetőség → erősebb value proposition
         ↓
→ vissza az elejére (flywheel forog)
```

### Falusi Route Flywheel (ÚJ v2.4)

```
1. Elérhetőségi ígéret (fix csütörtök, ismert Deák-termékek)
         ↓
2. Közösségi ajánlás (ambassador + szomszéd)
         ↓
3. Első rendelés, csütörtöki kiszállítás tapasztalat
         ↓
4. Ismétlődő heti/kétheti ritmus kialakulása
         ↓
5. Település-szintű demand density nő
         ↓
6. Route economics javul → több falu, több termék
         ↓
→ vissza az elejére (flywheel forog)
```

**A két flywheel közötti kapcsolat:** A városi flywheel stabilizálja a supply-t és a brand-et; a falusi flywheel kiterjeszti a piacot. Mindkettő erősíti a másikat: nagyobb összvolumen → jobb termelési hatékonyság → jobb ár mindkét zónában.

---

## 1. Customer Segments (FRISSÍTVE v2.4 -- kétzónás)

> **v2.4 változás:** A szegmentálás "job-to-be-done" alapú, nem csak földrajzi. A falusi vásárló nem "kevésbé digitális városi user", hanem külön szegmens, ahol a közösségi bizalom és a kiszámítható heti ritmus erősebb, mint az app UX önmagában.

| Szegmens | Földrajz | Fő pain point | Fő trigger | Elsődleges VP |
|----------|----------|---------------|------------|---------------|
| **Urban Convenience Buyer** | Udvarhely | Nincs idő boltba menni | Napi kiszállítás, gyors rendelés | Kényelem + frissesség |
| **Rural Access Buyer** | Keresztúri régió, 14 falu | Nincs közvetlen hozzáférés Deák-minőséghez | Csütörtöki fix route | Elérhetőség + kiszámíthatóság |
| **Family Basket Planner** | Város + falu | Heti étkezéstervezés, nagyobb háztartási kosár | Családi csomag, free delivery threshold | Spórolás + kevesebb döntés |
| **Early Digital Adopter** | Főleg város | Kíváncsiság, új szolgáltatás kipróbálása | Founding 50 | Ingyenes szállítás + early access |
| **Community-Referred Buyer** | Főleg falu | Bizalmi validáció kell | Ambassador / szomszéd ajánlása | Helyi bizalom |

### Demand signature zónánként

| Jellemző | Város | Falu |
|----------|-------|------|
| Rendelési frekvencia | Heti 1-2x | Heti/kétheti 1x |
| Átlagos kosárérték | Közepes | Magasabb (ritkább, tervezettebb) |
| Árérzékenység | Közepes | Magasabb |
| Döntési trigger | Kényelem, időspórolás | Elérhetőség, "végre megoldódott" |
| Retention driver | Savings Engine, habit | Route reliability, közösségi ajánlás |

### Validált operatív insight (v2.1-ből, változatlan)

A bolti sorok bizonyítják a keresletet. Ez nem market creation -- ez channel shift (offline → online). A falusi zónában viszont ez **market creation**: eddig nem volt elérhető a Deák-termék.

---

## 2. Value Proposition (FRISSÍTVE v2.4 -- zónánkénti VP hierarchia)

> **v2.4 változás:** A VP hierarchia zónánként eltér. Városban speed-first (kényelem), falun access-first (elérhetőség).

### Városi VP (Udvarhely)

| # | Pillér | Üzenet | Szerep |
|---|--------|--------|--------|
| **#1** | **Kényelem** | "Nem kell boltba menned" | Akvizíciós trigger |
| **#2** | **Okosabb döntés** | "Jobban vásárolsz, mint a boltban" | Retention motor |
| **#3** | **Megbízhatóság** | "Mindig van, mindig jön" | Flywheel feltétel |
| **#4** | **Frissesség** | "Hajnalban készül. Ma nálad." | Megkülönböztető |
| **#5** | **Ár** | Online = bolti ár (+ savings engine) | Savings |
| **#6** | **Helyi bizalom** | "A mi húsmívesünk" | Meglévő vásárlóknál |

### Falusi VP (Keresztúri régió) — ÚJ v2.4

| # | Pillér | Üzenet | Szerep |
|---|--------|--------|--------|
| **#1** | **Elérhetőség** | "Végre a falunkba is eljut a Deák-minőség" | Akvizíciós trigger |
| **#2** | **Kiszámíthatóság** | "Minden csütörtökön, fix időben" | Retention motor |
| **#3** | **Helyi bizalom** | "A szomszéd is rendeli" / ambassador ajánlás | Közösségi erősítő |
| **#4** | **Frissesség** | "Hajnalban készül. Csütörtökön nálad." | Megkülönböztető |
| **#5** | **Spórolás** | "Nem kell Udvarhelyre utazni érte" | Rejtett költségmegtakarítás |
| **#6** | **Okosabb döntés** | Savings Engine (200 RON threshold) | Kosárnövelő |

> **Fontos különbség:** Falun a "certainty over immediacy" elv dominál. Nem az a kérdés, milyen gyorsan jön, hanem hogy BIZTOSAN jön-e.

---

## 3. Channels (FRISSÍTVE v2.4 -- kétzónás csatornastratégia)

### Városi csatornák (változatlan v2.1-ből)

| Szint | Csatorna | Funkció | Prioritás |
|-------|----------|---------|-----------|
| DISCOVERY | Bolt + QR + személyes ajánlás | High-intent akvizíció | 🔴 #1 |
| TRUST LAYER | Facebook Group | Bizalom fenntartás, offline↔online híd | 🔴 #2 |
| CONVERSION | App (guest-first UX) | Rendelés leadása | 🔴 #3 |

### Falusi csatornák (ÚJ v2.4)

| Szint | Csatorna | Funkció | Prioritás |
|-------|----------|---------|-----------|
| DISCOVERY | Ambassador (helyi bizalmi személy) | Közösségi akvizíció | 🔴 #1 |
| DISCOVERY | Falusi kisbolt/közösségi hely plakát + QR | Láthatóság | 🟠 #2 |
| AGGREGATION | WhatsApp/Messenger továbbküldhető link | Rendelésgyűjtés, reminder | 🔴 #3 |
| TRUST LAYER | Helyi Facebook-csoport (óvatosan) | Közösségi validáció | 🟡 #4 |
| CONVERSION | App + fix csütörtöki route kommunikáció | Rendelés + kiszállítás | 🔴 #5 |

> **Kulcs különbség:** Falun nincs Deák-bolt → nincs bolti QR. A fő akvizíciós pont a helyi bizalmi háló (ambassador, szomszéd, kisbolt), nem a fizikai bolt.

> **Perplexity javaslat:** "Pre-order digitally, aggregate locally, deliver on fixed days." Ez a falusi channel modell lényege.

### Customer Relationships — frissítve v2.4

**Városi** (változatlan): Guest-first UX, személyes visszajelzés, T+3 trigger, Facebook Group.

**Falusi** (ÚJ):
- Proaktív csütörtöki emlékeztetők (WhatsApp/SMS)
- Ambassador mint személyes kapcsolattartó
- Route-day kommunikáció (mikor, hol, meddig)
- Exception handling: ha route nem indul vagy késik

---

## 4. Revenue Streams (FRISSÍTVE v2.4 -- fix 6,8% + kétzónás)

> **v2.4 kritikus változás:** A sávos revenue share modell ELAVULT. Fix 6,8% platformdíj megállapodva (Contract-cadru v1.2 + Comanda nr.1 v1.3, 2026-04-15).

### Platformdíj

| Elem | Érték | Megjegyzés |
|------|-------|-----------|
| **Platformdíj** | **Fix 6,8%** | Az online forgalomból (retail ár incl. TVA) |
| Alapja | Vânzări eligibile | Contract-cadru v1.2 rögzíti |
| Fizetés | Pilot: készpénz szállításkor (COD) | Online fizetés post-MVP (v0.5) |

### Kétzónás delivery economics

| Elem | Város (Udvarhely) | Falu (Keresztúri régió) |
|------|-------------------|------------------------|
| Szállítási díj | 10 RON | 15 RON |
| Ingyenes szállítási határ | 150 RON | 200 RON |
| Kiszállítási modell | Napi, per-delivery | Heti csütörtök, batch route |
| Route OPEX | — | ~190 RON/route |
| Breakeven | Per-order | ~8 rendelés/route |

> **Pilot döntés (Szabolcs, 2026-05-03):** Phase 1-ben nincs minimum rendelési küszöb a route indításához — akár 1-2 rendelésnél is megyünk, a tanulás érdekében. A route economics majd a pilot adataiból fog kirajzolódni.

> **Delivery fee = partial OPEX recovery + behavior shaping**, nem önálló profit center a pilotban.

---

## 5. Key Resources (FRISSÍTVE v2.4 -- route erőforrásokkal)

| Erőforrás | Tulajdonos | Kritikusság | Megjegyzés |
|-----------|-----------|-------------|-----------|
| **Supply megbízhatóság** | Deák | 🔴 | Explicit -- a flywheel motorja |
| **Digitális platform (PWA)** | Exar Labs | 🔴 | Sprint 3 active (70%), v0.3 beta ~2026-05-15 |
| **Analytics stack** | Exar Labs | 🔴 | v0.2 "Látjuk az adatokat" ✅ kész |
| **Savings Engine** | Exar Labs | 🔴 | v0.3 retention + basket-size driver |
| **Delivery zone logic** | Exar Labs | 🔴 | Városi/Keresztúri threshold + fee |
| **Route jármű** | Deák / operátor | 🔴 | Falusi route fizikai alapja |
| **Hűtőtáska / szállítási hűtés** | Deák / operátor | 🔴 | Minőség + élelmiszerbiztonsági bizalom |
| **Sofőr / courier capacity** | Deák / operátor | 🔴 | **2 sofőr elérhető** (Szabolcs döntés) |
| Termékkatalógus (37 termék) | Exar Labs | 🟠 | HU+RO JSON, WebP fotók |
| Facebook Group (Trust Layer) | Exar + Deák | 🟠 | Bizalom-infrastruktúra |
| Founding 50 program | Exar + Deák | 🟠 | Early adopter base |
| Ambassador hálózat | Helyi személyek | 🟡 | TBD — egyelőre nélkülük is indulunk |

### Single Courier Risk (frissítve v2.4)

> **v2.4 update:** 2 sofőr elérhető a rendszerben (Szabolcs, 2026-05-03). A falusi route-ban a kiesés kritikusabb mint városban — egy csütörtöki route kiesése nem egy rendelést, hanem egy teljes heti falusi kiszállítási ígéretet érint. A 2. sofőr elérhetősége csökkenti ezt a kockázatot.

---

## 6. Key Activities (FRISSÍTVE v2.4 -- route tevékenységekkel)

### Városi Key Activities (változatlan)

| Tevékenység | Felelős | Prioritás |
|-------------|---------|-----------|
| Failure Handling rendszer | Exar Labs | 🔴 |
| Dry run (próbarendelések) | Exar + Deák | 🔴 |
| QR + Facebook Group indítás | Exar + Deák | 🔴 |
| 2. rendelés trigger (manuális) | Exar | 🔴 |
| Savings Engine implementáció | Exar Labs | 🔴 |

### Falusi Route Key Activities (ÚJ v2.4)

| Tevékenység | Felelős | Prioritás |
|-------------|---------|-----------|
| Route planning (útvonal, megállók, sorrend) | Exar + Deák | 🔴 |
| Cutoff szabály kezelés (szerda este) | Exar Labs | 🔴 |
| Csütörtöki route előkészítés (picking/packing) | Deák | 🔴 |
| Kiszállítási kör választó implementáció (hibrid modell) | Exar Labs | 🔴 |
| Checkout település-validáció | Exar Labs | 🟠 |
| Falusi kommunikációs ritmus (emlékeztetők) | Exar | 🟠 |
| Ambassador onboarding (ha/amikor szükséges) | Exar + helyi | 🟡 |
| Route-go/cancel döntés logika | Exar + Deák | 🟡 |

---

## 7. Key Partners (FRISSÍTVE v2.4)

### Deák Húsmíves -- Governance (frissítve)

| Téma | Státusz v2.4 |
|------|-------------|
| Egyetlen kapcsolattartó | ⚠️ Nincs formálisan kijelölve |
| Platformdíj | ✅ **MEGÁLLAPODVA** — 6,8% (Contract-cadru v1.2) |
| Írásbeli megállapodás | ✅ Keretszerződés + Comanda nr.1 aláírva |
| Döntéshozó | Ibi (könyvelő testvér) |

### Partnerek (kiegészítve v2.4)

| Partner | Szerep | Kritikusság |
|---------|--------|-------------|
| Deák Húsmíves | Supply, minőség, feldolgozás, szállítás | 🔴 |
| Exar Labs | Platform fejlesztés, analytics, marketing, growth | 🔴 |
| Falusi ambassadorok | Helyi bizalom, akvizíció, kommunikáció | 🟡 (TBD) |
| Falusi kisboltok/közösségi pontok | Plakát, QR, láthatóság | 🟡 |
| Courier / helyettes sofőr | Route continuity, backup | 🔴 |

> **v2.4 döntés:** Az ambassadorok egyelőre tervben vannak, de nélkülük is indulunk. Ha az első route-ok igazolják a keresletet, akkor lépünk az ambassador onboarding felé.

---

## 8. Cost Structure (FRISSÍTVE v2.4 -- route OPEX-szel)

### Befektetés

| Tétel | Összeg |
|-------|--------|
| MVP fejlesztés | ~4 620 EUR |
| Éves üzemeltetés | ~3 900 EUR |
| Marketing (pilot) | ~500-2 000 EUR |

### Route OPEX (ÚJ v2.4)

| Tétel | Költség | Frekvencia |
|-------|---------|-----------|
| Route üzemanyag + idő | ~190 RON/route | Heti (csütörtök) |
| Hűtőtáska/szállítási eszközök | Egyszeri | Induláskor |
| Route kommunikáció (SMS/WhatsApp) | Minimális | Heti |
| Extra csomagolás | ~5-10 RON/rendelés | Per rendelés |

### Stop Decision Framework (frissítve v2.4)

| Döntés | Feltétel | Timing |
|--------|----------|--------|
| **Folytatás / scale** | ≥50 reg + ≥20 visszatérő | max 3 hónap |
| **Stop** | 3 hónap után nem teljesülnek | max 3 hónap |
| **Bármikor** | Közös döntéssel, penalitás nélkül | — |

> **v2.4 döntés (Szabolcs):** Stop cap frissítés egyelőre nem szükséges — végigvisszük Sprint 5-ig.

---

## 9. Pilot Hypotheses (FRISSÍTVE v2.4 -- falusi hipotézisekkel)

### Városi hipotézisek (változatlan, H1-H5)

| ID | Hipotézis | Validáció | Siker |
|----|-----------|-----------|-------|
| H1 | Van kereslet online húsrendelésre Udvarhelyen | 30 nap | ≥15 rendelés |
| H2 | Founding 50 aktivál early adoptereket | reg + 1. rendelés | 50 reg / 20 első rendelés |
| H3 | Savings Engine növeli a kosárértéket | threshold conversion | AOV nő |
| H4 | Kialakul ismétlő vásárlási habit | ≥2 rendelés/user | ≥5 visszatérő |
| H5 | Bolt + QR a legjobb akvizíciós csatorna | UTM/QR mérés | jelentős forrás |

### Falusi hipotézisek (ÚJ v2.4, H6-H10)

| ID | Hipotézis | Validáció | Siker |
|----|-----------|-----------|-------|
| H6 | Van falusi kereslet Deák-termékekre | Keresztúri route első 4 hét | Növekvő rendelési trend |
| H7 | A csütörtöki fix route érthető és elfogadható | Rendelés + feedback | Alacsony panasz a fix nap miatt |
| H8 | Ambassador modell gyorsítja a falusi akvizíciót | Település szerinti data | Ambassador falvakban több rendelés |
| H9 | Route economics javul a 4. hétre | Order count/route | Közelítés 8 rendelés/route felé |
| H10 | Falusi second order ciklus max 28 napos | Mérés | ≥30% reorder 28 napon belül |

---

## 10. Pilot Success Metrics (FRISSÍTVE v2.4 -- kétzónás KPI-k)

### Városi KPI-k

| Metrika | Cél | Mérés |
|---------|-----|-------|
| Regisztrációk | 50 (Founding 50) | Firebase |
| Leadott rendelések | ≥15 / hó | Firebase |
| Second Order Rate (14 nap) | ≥40% | Firebase |
| Átlagos kosárérték (AOV) | Mérni (baseline TBD) | Firebase |
| TTFO (Time to First Order) | ≤72 óra | Firebase |
| Savings Engine engagement | Threshold nudge conversion | Firebase |

### Falusi KPI-k (ÚJ v2.4)

| Metrika | Cél | Mérés |
|---------|-----|-------|
| Orders per route day | Növekvő trend → 8+ | Admin data |
| Route fill rate | Növekvő | Admin data |
| Revenue per route | > 190 RON contribution | Admin data |
| Village participation rate | ≥3 falu aktív | Per-village tracking |
| Pre-order rate before cutoff | ≥80% | Admin data |
| Cancellation/missed-stop rate | <10% | Admin data |
| Second Order Rate (28 nap) | ≥30% | Firebase |
| Repeat rate by village cohort | Mérni | Firebase |

### Cross-zone KPI-k

| Metrika | Mérés |
|---------|-------|
| Teljes fleet utilization | Admin |
| Inventory waste | Deák reporting |
| Customer service load | Manuális |

> **v2.4 döntés (Szabolcs):** Falun a 28 napos second order rate a mérvadó (14 nap túl szigorú a heti/kétheti vásárlási ritmus miatt).

---

## 11. Kockázatok (FRISSÍTVE v2.4 -- falusi kockázatokkal)

### Meglévő kockázatok (változatlan)

| Kockázat | Súlyosság | Mitigáció |
|----------|-----------|-----------|
| Supply kockázat | 🔴 | Dry run, kapacitás ellenőrzés |
| Single Courier Risk | 🔴 | **2 sofőr elérhető** (v2.4 update) |
| Governance (két testvér) | 🟠 | Keretszerződés aláírva ✅ |
| Overconfidence Risk | 🟠 | Tudatos expectation management |
| Facebook Dependence | 🟠 | Alternatív visszacsalogatás post-pilot |

### Falusi specifikus kockázatok (ÚJ v2.4)

| Kockázat | Leírás | Súlyosság | Mitigáció |
|----------|--------|-----------|-----------|
| Route nem indul | Túl kevés rendelés egy héten | 🟠 | Pilot: nincs minimum, megyünk akár 1-2-vel is |
| Phase 1 veszteséges route-ok | 190 RON OPEX > bevétel | 🟠 | Tudatos tanulási befektetés, Sprint 5-ig |
| Ambassador kiesik | Közösségi akvizíció megáll | 🟡 | Nélkülük is indulunk; nem egypontos függés |
| Időjárás / útviszonyok | Csütörtöki route késik/elmarad | 🟠 | Kommunikáció, backup nap? |
| Hűtés / minőségpercepció | Hosszabb szállítási idő a route-on | 🟠 | Hűtőtáska, frissességi garancia |
| GPS-zóna mismatch | User rossz kiszállítási kört választ | 🟡 | Checkout település-validáció (Phase 2) |
| Falusi user nem érti az appot | Alacsonyabb digitális készség | 🟠 | Egyszerű UX, ambassador-asszisztált rendelés |
| Közösségi negatív visszajelzés | Egy rossz élmény gyorsan terjed | 🔴 | Hibátlan első kiszállítások, proaktív kommunikáció |
| Demand concentration | 1-2 falu viszi az egész route-ot | 🟡 | Per-village tracking, diverzifikáció |

---

## 12. Fejlesztési státusz + Blokkolók (FRISSÍTVE v2.4)

### Fejlesztési státusz

| Verzió | Sprint | Tartalom | Státusz |
|--------|--------|----------|---------|
| v0.1 | Sprint 1 | Az első rendelés — MVP | ✅ KÉSZ |
| v0.2 | Sprint 2 | Látjuk az adatokat — analytics | ✅ KÉSZ (2026-04-15) |
| v0.3 | Sprint 3 | A spórolás motora — Savings Engine | 🔄 ACTIVE (~70%) |
| v0.4 | Sprint 4 | **Route-ready platform + zóna választó** | ⏳ Tervezett |
| v0.5 | Sprint 5 | **Route launch + rural KPIs** | ⏳ Tervezett |

> **v2.4 döntés (Szabolcs):** Sprint 4 = route-ready platform ELSŐ, natív mobil UTÁNA. A falusi route prioritást élvez a natív mobilhoz képest.

### Jira összesítő

- **Összesen:** 153+ ticket (DH-1 → DH-184+)
- **Sprint 2 (CLOSED):** 38/38 Done = 100%
- **Sprint 3 (ACTIVE):** 7/10 Done = 70%

### Blokkolók (frissítve)

| # | Blokkoló | Státusz v2.4 |
|---|----------|-------------|
| 1 | ~~Domain véglegesítése~~ | ✅ KÉSZ — deakhus.ro él (2026-03-30) |
| 2 | ~~Platformdíj véglegesítése~~ | ✅ KÉSZ — 6,8% (2026-04-15) |
| 3 | ~~Revenue share % rögzítése~~ | ✅ KÉSZ — Contract-cadru v1.2 |
| 4 | Írásbeli partnerségi megállapodás | ✅ Keretszerződés aláírva |
| 5 | Marketing budget cap rögzítése | ❌ Nyitott |
| 6 | GDPR consent | 🟡 Legal backlogban |
| 7 | ANSVSA szállítási engedély ellenőrzés | 🟡 Legal backlogban |

---

## 13. Platform Vision -- Post-Pilot (FRISSÍTVE v2.4 -- 5 fázis)

> **v2.4 stratégiai shift:** A következő földrajzi lépés nem automatikusan "második város", hanem "route-sűrűség és régión belüli hozzáférés."

### 5 Fázisú Stratégiai Roadmap

```
Phase 1 — PILOT & VALIDATION (MOST)
  ├── Udvarhelyi online rendelés validálása
  ├── Savings Engine v0.3
  ├── Founding 50 early adopter program
  └── Keresztúri Route Pilot

Phase 2 — ROUTE DENSITY & HABIT
  ├── Városi second order habit stabilizálása
  ├── Keresztúri csütörtöki route stabilizálás
  ├── Ambassador modell validálása (ha szükséges)
  └── Route economics javítása

Phase 3 — REGIONAL EXPANSION
  ├── Új falusi route-ok / régiós klaszterek
  ├── NEM feltétlen 2. város, hanem sűrűbb régiós lefedés
  └── Route playbook kialakítása

Phase 4 — CATEGORY EXPANSION
  ├── Sajt, zöldség, gyümölcs, pékáru
  ├── Ugyanazon route-on több helyi termelő
  └── LocalBasket curated supply modell

Phase 5 — LOCAL MARKET LAYER
  └── Több beszállítós, régiós helyi élelmiszer-platform
```

> **Záró stratégiai mondat:** "DHOP már nem csak azt validálja, hogy Udvarhelyen lehet-e online húst rendelni. Azt is validálja, hogy egy helyi termelő digitális platformmal és fix route-tal képes-e régiós ellátási hálózatot építeni."

---

## Változáskövetés

| Verzió | Dátum | Változás |
|--------|-------|---------|
| 0.1--0.5 | 2026-03-04--05 | Első draftek |
| 1.0 | 2026-03-27 | Átfogó frissítés |
| 2.0 | 2026-03-28 | Operatív élesítés (Flywheel, guest-first UX, sávos revenue share) |
| 2.1 | 2026-03-29 | "Build system that learns." Supply Reliability, Failure Handling, Facebook Trust Layer. |
| 2.2 | 2026-04-03 | Release Roadmap kontextus hozzáadása. |
| 2.3 | 2026-04-04 | "Döntéstámogató rendszer." Core Definíció, 4-rétegű rendszerarchitektúra, Core Loop, VP frissítés. |
| **2.4** | **2026-05-03** | **"Kétzónás lokális ellátási platform."** MEGA Review (ChatGPT + Perplexity + Claude, 16 blokk elemzés). Stratégiai átkeretezés: városi kényelem + falusi elérhetőség. Új: Falusi Route Flywheel, 5 customer szegmens (job-to-be-done), kétzónás VP hierarchia, falusi channel stack, fix 6,8% platformdíj (sávos elavult), route OPEX és economics, 5 új falusi hipotézis (H6-H10), kétzónás KPI-k (28 napos falusi retention), 9 falusi kockázat, 5 fázisú Platform Vision (Phase 3 = regionális, nem 2. város), Sprint 4 = route-ready (nem natív mobil). Szabolcs döntései rögzítve: pilot phase nincs route minimum, 2 sofőr elérhető, ambassador TBD, stop cap változatlan Sprint 5-ig. |
