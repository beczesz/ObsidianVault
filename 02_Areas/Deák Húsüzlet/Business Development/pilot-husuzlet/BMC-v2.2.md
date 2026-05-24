---
title: Business Model Canvas -- Deák Húsmíves Online Platform (Pilot)
version: 2.3
date: 2026-04-04
author: Becze Szabolcs -- Exar Labs
collaborators: ChatGPT (GPT-4o) -- "Üzleti terv értékelés" + "Savings Engine Koncepció" sessions
description: >
  BMC v2.3 -- "Döntéstámogató rendszer." Paradigmaváltás: a DH nem webshop, nem marketplace,
  nem kedvezményplatform — hanem egy optimalizáló rendszer, amely jobb döntéseket segít hozni,
  és az ebből származó margin előnyt visszaadja a felhasználónak.
  v2.2 változásai megmaradnak (Supply Reliability, Failure Handling, Facebook Trust Layer).
  Újdonság: Core Definíció + 4-rétegű rendszerarchitektúra (Decision Engine, Basket Optimization,
  Habit Engine, Activation & Recovery) + Core Loop + Stratégiai pozicionálás.
predecessor: BMC-v2.2.md (v2.2, 2026-04-03)
id: 6f819495-0eaa-4658-89cc-10f10eca8ea8
index_schema_version: 1
---

# Business Model Canvas v2.3 -- Deák Húsmíves Online Platform (Pilot)

_Version: 2.3 | Last updated: 2026-04-04_
_Scope: DH pilot -- az online rendelési csatorna validálása._
_Framing: V2.0 = "build product" → V2.1 = "build system that learns" → V2.3 = **"döntéstámogató rendszer"**_

---

## PLATFORM MISSZIÓ

> _"Összekötjük a helyi termelőket a vásárlókkal, hogy a mindennapi élelmiszer egyszerűen, frissen és közvetlenül jusson el az emberekhez. Egy olyan rendszert építünk, ahol a helyi gazdaság erősödik, és mindenki nyer: a vásárló, a termelő és a közösség."_

**A DH nem a cél -- hanem a bizonyíték, hogy a LocalBasket működhet.**

---

## CORE DEFINÍCIÓ (v2.3 — paradigmaváltás)

> **A DH egy döntéstámogató rendszer, amely optimalizálja a vásárlói döntéseket és a háttérben a termelést, logisztikát és készletet — az ebből származó margin előnyt pedig visszaadja a felhasználónak.**

### Alapelv

- Nem kedvezményt adunk
- Nem akciózunk
- Nem olcsóbbak vagyunk

**→ Jobb döntést segítünk hozni.**

### Rendszer cél

Margin leakage csökkentése 4 fő területen:

| # | Terület | Példa |
|---|---------|-------|
| 1 | Feldolgozás | waste, reprocessing csökkentés |
| 2 | Logisztika | delivery, bolt költség optimalizálás |
| 3 | Mennyiség | batch inefficiency eliminálás |
| 4 | Készlet / kereslet | carcass balance, idő-optimalizálás |

### Stratégiai pozíció

| ❌ Nem vagyunk | ✅ Amik vagyunk |
|----------------|-----------------|
| Webshop | Optimalizáló rendszer |
| Marketplace | Döntéstámogató eszköz |
| Kedvezményplatform | Supply + demand összhangoló |

### Core Loop

```
Kosár építés → Progress → Ajánlás → Visszajelzés → Újrarendelés
```

1. **Kosár építés** → user termékeket ad hozzá
2. **Progress** → "Még X RON → jobb döntés"
3. **Ajánlás** → threshold, bundle, swap
4. **Visszajelzés** → "X RON-t optimalizáltál"
5. **Újrarendelés** → 1-click reorder + trigger

### 4 rendszerréteg

| Réteg | Név | Tartalom | Cél |
|-------|-----|----------|-----|
| 🔴 L1 | Decision Engine (Core UX) | Running savings counter, threshold nudge, post-order recap | Döntési feedback loop |
| 🟠 L2 | Basket Optimization | Családi csomagok, swap suggestion | Valódi optimalizáció |
| 🟡 L3 | Habit Engine | 1-click reorder, "Szokásos rendelésem" | Ismétlődő viselkedés |
| 🔵 L4 | Activation & Recovery | TTFO engine, post-delivery trigger, savings recap email | Aktiváció + visszahozás |

### Savings → Feature mapping

| Savings forrás | Feature |
|----------------|---------|
| Logisztika | Threshold nudge |
| Mennyiség | Bundle |
| Carcass balance | Swap suggestion |
| Idő / frissesség | "Ma ajánlott" (future) |
| Demand stabilizálás | Reorder |

### Siker definíció

> A felhasználó érzi, hogy: **"jobban vásároltam, mint legutóbb"**
>
> Ha ez teljesül → repeat jön → AOV nő → rendszer skálázódik.

### Záró elv

> **A DH nem olcsóbb — hanem okosabb.**

---

## 0. Growth Flywheel (változatlan v2.0-tól)

```
1. Megbízható, stabil supply (mindig van jó termék)
         ↓
2. Pozitív első rendelési élmény (gyors, egyszerű, pontos)
         ↓
3. Második rendelés (habit kezdete) -- T+3 nap trigger
         ↓
4. Heti rutin kialakul ("csütörtökön rendelek húst")
         ↓
5. Növekvő rendelési volumen (kosárérték és frekvencia nő)
         ↓
6. Supplier stabilabb és olcsóbban tud termelni
         ↓
7. Jobb ár + jobb elérhetőség → erősebb value proposition
         ↓
→ vissza az elejére (flywheel forog)
```

**A flywheel 3 kulcskomponense:**
- **Supply Stability** -- mindig van készlet (mostantól explicit erőforrás -- lásd 6. szekció)
- **Fast First Order** -- 2-3 perc alatt rendelés (guest-first UX)
- **Second Order Trigger** -- T+3 napos manuális emlékeztető az első 30 usernél

---

## 1. Customer Segments (változatlan v2.0-tól)

### Elsődleges early adopter szegmens (pilot: első 30 user)

> **"Digitálisan nyitott, időszűkében lévő helyi vásárlók, 25-45 éves korosztály"**

| Jellemző | Leírás |
|----------|--------|
| Kor | 28-45 év |
| Foglalkozás | Irodai dolgozó, vállalkozó |
| Fájdalom | Nincs idő a bolti vásárlásra |
| Digitális szokás | Már rendel futárral; Google login nem probléma |
| Döntési sebesség | Gyors (alacsony ellenállás az online próbával) |
| Vásárlási mód | Tervezett (heti 1-2x), nem impulzus |

### Validált operatív insight (v2.1 újdonság)

**A bolti sorok bizonyítják a keresletet.** Ez nem market creation -- ez **channel shift**: offline → online. Nem kell piacot teremteni, csak a vásárlási szokást átterelni egy kényelmesebb csatornára.

### Szegmens térkép (pilot → scale, változatlan)

| Szegmens | Pilot szerep | Scale szerep |
|----------|-------------|-------------|
| **Időszűkében lévők** (25-45) | ✅ Elsődleges | ✅ Core |
| **Korai digitális userök** | ✅ Enabler | ✅ Amplifier |
| **Egészségtudatosak** | ⚠️ Másodlagos | ✅ Fontos |
| **Családok** (35-55) | ❌ Nem első 30 | ✅ Fő scale szegmens |

---

## 2. Value Proposition (FRISSÍTVE v2.3-ban)

> **v2.3 paradigmaváltás:** A value proposition nem a termékről szól, hanem a döntésről. A kényelem továbbra is az akvizíciós trigger, de a retention és differenciáció motorja az "okosabb vásárlás" élmény.

| # | Pillér | Üzenet | Sorrend indoka |
|---|--------|--------|----------------|
| **#1** | **Kényelem** | "Nem kell boltba menned" | Akvizíciós trigger — az első rendelés oka |
| **#2** | **Okosabb döntés** | "Jobban vásárolsz, mint a boltban" | 🆕 A retention motorja — a második rendelés oka |
| **#3** | **Megbízhatóság** | "Mindig van, mindig jön" | A flywheel forogásának feltétele |
| **#4** | **Frissesség** | "Hajnalban készül. Ma nálad." | Erős megkülönböztető, az első rendelés UTÁN válik igazán értékessé |
| **#5** | **Ár** | Online = bolti ár (+ optimalizálási előny) | A savings engine teszi láthatóvá |
| **#6** | **Helyi bizalom** | "A mi húsmívesünk" | Meglévő vásárlóknak azonnal releváns |

---

## 3. Channels (STRUKTURÁLISAN FRISSÍTVE -- v2.1 kulcsváltozás)

### Háromszintes csatornastratégia

A v2.0-ban a Facebook opcionális volt. **A v2.1-ben a Facebook Core Trust Layer -- nem marketing csatorna, hanem bizalom-infrastruktúra.**

**Channels BMC megfogalmazás:**
> _"Offline-to-online conversion via in-store QR and assisted onboarding, reinforced by a Facebook Group acting as a continuous trust and visibility layer."_

### A 3 szint

| Szint | Csatorna | Funkció | Prioritás |
|-------|----------|---------|-----------|
| **1. DISCOVERY** | Bolt + QR + személyes ajánlás | Fő akvizíció -- high-intent traffic | 🔴 #1 |
| **2. TRUST LAYER** | Facebook Group ("Deák Húsmíves -- friss hús naponta") | Folyamatos jelenlét, bizalom fenntartás, offline↔online híd | 🔴 #2 |
| **3. CONVERSION** | App (guest-first UX) | Rendelés leadása | 🔴 #3 |

### Trust Layer részletei (v2.1 újdonság)

**Miért Group, nem Page?**
- Group = közösség, nem broadcast
- Tartalom: "ma ezt vágtuk", "holnap elérhető", "rendelések nyitva"
- A vásárló érzi, hogy belülről lát -- nem reklámot kap

**Retention csatorna:** Facebook a leginkább elfogadható visszacsalogatási mód (telefon/WhatsApp túl személyes a vásárlók számára).

**Hirdetések az első 30 usernél:** ❌ NEM. Organikus, személyes.

### Csatorna térkép (pilothoz rangsorolva)

| Csatorna | Timing | Prioritás |
|----------|--------|-----------|
| Bolti QR + személyes ajánlás | Azonnal | 🔴 #1 |
| Facebook Group (Trust Layer) | Launch-tól párhuzamosan | 🔴 #2 |
| Szájról szájra | Folyamatosan | 🟠 #3 |
| Szórólap (A5) | Launch | 🟠 #4 |
| Facebook Page (posztok) | Post-launch | 🟡 #5 |
| Helyi Facebook csoportok | 2-3. hét | 🟡 #6 |

---

## 4. Customer Relationships (kiegészítve v2.1-ben)

### Onboarding -- Guest-first UX (változatlan v2.0-tól)

```
Termékek megjelenítése azonnal (login nélkül)
    ↓
Böngészés, kosárba rakás (regisztráció nélkül)
    ↓
Checkout: ITT kér login-t az app
    ↓
Szállítási adatok (előtöltve visszatérő usernél)
    ↓
Rendelés leadva → Köszönöm oldal
```

### Kapcsolat fenntartása -- Retention (v2.1 kiegészítés)

**Validált frekvencia:** Átlagos vásárló heti 1-2x vásárol húst. Ez azt jelenti:

| Időpont | Akció | Eszköz |
|---------|-------|--------|
| T+0 (kiszállítás után) | Személyes visszajelzés kérés | Facebook Group üzenet |
| T+3 nap | Emlékeztető: "mikor rendelsz legközelebb?" | Facebook Messenger (manuálisan) |
| T+7 nap | Ha nem rendelt: friss termék post a Groupban | Facebook Group |

> **Pilot fázisban: személyes kapcsolat az első 30 usernél, nem automatizmus.**

### Order Failure Kapcsolat (v2.1 ÚJDONSÁG)

Ha a rendelés nem teljesíthető (stock-out, késés, cancel):
- Telefonos kapcsolat a vásárlóval (telefonszám megvan a regisztrációból)
- App-szintű cancel funkció: **mind a vásárló, mind Deák oldaláról** _(új DH ticket szükséges -- lásd 13. szekció)_

---

## 5. Revenue Streams (KIEGÉSZÍTVE -- tárgyalási stratégia v2.1)

### Sávos Revenue Share modell (változatlan v2.0-tól)

| Havi forgalom | Revenue Share % | Megjegyzés |
|---------------|----------------|-----------|
| 0-2 000 EUR | **5%** | Pilot -- tanulási fázis |
| 2 000-5 000 EUR | **8%** | Stabil fázis |
| 5 000+ EUR | **10-12%** | Scale fázis |

### Revenue Split (v2.1 újdonság -- Szabolcs modellje)

Az online forgalom 3 részre osztódik:
1. **Platform (Exar Labs)** -- revenue share a fenti sáv szerint
2. **Deák Húsmíves profit** -- a maradék az ő inkrementális nyereségük
3. **Vásárló kedvezmény** -- hosszú távon, volumen esetén (post-pilot)

### Tárgyalási stratégia Ibivel (v2.1 kulcsbetét)

**Kulcs mondat Ibinek:**
> _"Ez most nem profit optimalizáció, hanem új csatorna validáció."_

**Miért ne kérj túl sokat az elején:**
- Magas share → ellenállás + mikro-management
- Alacsony share → partner elkötelezett, tanulunk, aztán emelünk

**Javasolt tárgyalási keret:**
- Phase 1 (pilot, 30 nap): 5-8% -- cél: tanulás, nem profit
- Phase 2 (validated, 30+ nap, ha metrikák teljesülnek): növekvő share
- Pontos % Ibi válasza alapján véglegesítendő _(jövő hétre ígérte)_

### Inkrementális margin -- realitás (v2.1 korrekció)

Az online forgalom elméletben inkrementális (a fix termelési cost a boltokból megtérül). **A valóságban vannak rejtett operatív költségek:**

| Rejtett költség | Megjegyzés |
|-----------------|-----------|
| Csomagolás ideje | Deák egyedül csinálja, idő = pénz |
| Szállítás (üzemanyag + idő) | Egyenlőre Deák saját autója |
| Koordinációs komplexitás | Hibák, visszahívások, stock-out kezelés |

> **A margin jobb lesz, de nem "ingyen pénz."** A rejtett költségeket figyelembe kell venni a revenue share tárgyalásnál.

---

### Release Roadmap kontextus (v2.2 újdonság)

A DH fejlesztés sprint-alapú verziókezelésre állt át:

| Verzió | Fázis | Tartalom |
|--------|-------|----------|
| v0.1 | ✅ Kész | MVP — az első rendelés proof of concept |
| v0.2 | 🔄 Sprint 2 (aktív) | Analytics, UTM/QR, bugfixek, cancel flow |
| v0.3 | ⏳ Sprint 3 | Savings engine — háztartási spóroló eszköz |
| — | ⏳ 2 hét szünet | Management tesztelés + natív mobil előkészítés |
| v0.4 | ⏳ Sprint 4 | Natív mobil experience (iOS prioritás) |
| v0.5 | ⏳ Sprint 5 | Online fizetés, multi-supplier |

A Savings engine (v0.3) a kulcsfontosságú differenciáló: a webshopból döntéstámogató rendszerré alakítja a platformot. A 4-rétegű architektúra (Decision Engine → Basket Optimization → Habit Engine → Activation & Recovery) a v0.3-ban kerül bevezetésre.


## 6. Key Resources (STRUKTURÁLISAN FRISSÍTVE -- v2.1 kulcsváltozás)

### Supply Reliability mint explicit #1 erőforrás (v2.1 újdonság)

A v2.0-ban a supply reliability implicit volt. **A v2.1-ben ez a rendszer legkritikusabb explicit erőforrása.**

**Key Resources #1 megfogalmazás:**
> _"Operational supply reliability: consistent availability, predictable fulfillment, single-day delivery promise."_

**Validált kapacitás (v2.1 újdonság):**
- Jelenlegi: 5 fél disznó/nap (reggel 5-től 8-ig feldolgozva)
- Skálázható: 10 fél disznóra egyedül, azon túl alkalmazott kell
- **Pilot szinten: a kapacitás nem bottleneck**

**Kézbesítési modell (validált):**
- D+1 kézbesítés (ma rendel → holnap szállít)
- Időablak: 11-17 között
- Kiszállítás: Deák egyszemélyben (pilot fázis)

### Erőforrás térkép (frissítve)

| Erőforrás | Tulajdonos | Kritikusság | Megjegyzés |
|-----------|-----------|-------------|-----------|
| **Supply megbízhatóság** | Húsüzlet | 🔴 #1 | Explicit -- a flywheel motorja |
| **Kapacitás (5→10 fél disznó/nap)** | Húsüzlet | 🔴 #1b | Pilot szinten nem bottleneck |
| **Digitális platform (PWA)** | Exar Labs | 🔴 #2 | 64% kész (72/112 ticket Done), beta: ápr 14-17 |
| **Guest-first UX** | Exar Labs | 🔴 #3 | Konverzió kulcsa |
| AI-alapú fejlesztési módszertan | Exar Labs | 🟠 | 12x, 92% olcsóbb |
| Termékkatalógus (37 termék) | Exar Labs | 🟠 | HU+RO JSON, WebP fotók |
| Facebook Group (Trust Layer) | Exar Labs + Húsüzlet | 🟠 | Bizalom-infrastruktúra |
| Brand identity + marketing anyagok | Exar Labs | 🟡 | Szórólap nyomtatásra kész |
| Helyi márka bizalom + termékminőség | Húsüzlet | 🟡 | Generációs szakértelem |

### Legkritikusabb erőforrás-kockázat (frissítve)

> ⚠️ **Supply + Single Courier kockázat:** Ha Deák beteg, túlterhelt, vagy a rendelések száma eléri a tipping pointot (~10-12 rendelés/nap), a rendszer megáll. **Ez az egyetlen erőforrás-kombináció, ami az Exar Labstól függetlenül leállíthatja a pilotot.**

---

## 7. Key Activities (STRUKTURÁLISAN FRISSÍTVE -- v2.1 kulcsváltozás)

### TOP 3 -- Most, beta launch előtt (frissítve)

**#1 -- End-to-end rendelési dry run**
- 5-10 próbarendelés valódi körülményekkel
- Cél: 0 kritikus hiba a core loopon (browse → cart → order → deliver)
- Referencia: `DH_OPERATIONS/order_lifecycle_stress_test.md` _(létrehozandó)_

**#2 -- Failure Handling rendszer felállítása (v2.1 ÚJDONSÁG)**
- Stock-out: telefon + app-szintű cancel funkció (DH ticket szükséges)
- Késés: proaktív értesítés a vásárlónak
- User cancel: app-ból mind a vásárló, mind Deák oldaláról
- ⚠️ Ez az első hely ahol elromlik az élmény, ha nincs kezelve

**#3 -- Bolt + QR + Facebook Group párhuzamos indítás**
- Scriptelt ajánlás a pultnál (egységes mondat mindenkitől)
- Facebook Group létrehozása és első posztok (tartalom: mit vágtunk, mikor szállítunk)
- Napi cél: 10-20 megkeresett → 3-5 regisztráció

### Teljes tevékenységtérkép (frissítve)

| Tevékenység | Felelős | Timing | Prioritás |
|-------------|---------|--------|-----------|
| **Failure Handling rendszer** (stock-out, cancel, késés) | Exar Labs | MOST (blocker) | 🔴 #1 |
| Dry run (5-10 próba) | Exar Labs + Húsüzlet | Launch előtt | 🔴 #2 |
| QR + scriptelt ajánlás + Facebook Group indítás | Exar Labs setup + Húsüzlet kivitel | Launch | 🔴 #3 |
| 2. rendelés trigger (manuális, T+3) | Exar Labs | Post-launch | 🔴 #4 |
| Írásbeli partnerségi megállapodás | Exar Labs | AZONNAL (blocker) | 🔴 Blocker |
| Domain véglegesítése | Exar Labs | AZONNAL (blocker) | 🔴 Blocker |
| MVP fejlesztés befejezése (44% hátra) | Exar Labs | Ápr 14-17 | 🟠 |
| GDPR consent + adattörlés | Exar Labs | Launch előtt kötelező | 🟠 |
| Order Lifecycle Stress Test elvégzése | Exar Labs + Húsüzlet | Dry run során | 🟠 |
| Pilot mérés (KPI dashboard) | Exar Labs | Launch-tól | 🟡 |

---

## 8. Key Partners (kiegészítve v2.1-ben)

### Deák Húsmíves -- Governance frissítés (v2.1)

| Téma | Státusz |
|------|---------|
| Egyetlen kapcsolattartó | ⚠️ Nincs formálisan kijelölve |
| Döntéshozó | Ibi (könyvelő testvér) -- erősebb akarat, pénzügyek |
| Ibi blokkolja a launchet? | ❌ Nem várható |
| Szabolcs tárgyalási pozíciója | Nő az online forgalommal -- jelenleg korlátozott |
| Pénzügyi adatok (margin) | Ibi jövő hétre ígérte |

**Governance kockázat (v2.1 pontosítás):**
> _"Nem fog blokkolni" = remény, nem kontroll._ A megállapodás írásbeli rögzítése ezért különösen kritikus, mielőtt a forgalom növekedésével tárgyalási pozíció alakul ki.

**Minimális írásbeli megállapodás tartalma** (változatlan v2.0-tól, de sürgőssége nőtt):
- Revenue share % + elszámolás
- Árpolitika (online = bolti ár)
- Szerepek: Deák (készlet/minőség/szállítás), Exar (platform/marketing)
- Failure handling: mi történik stock-out / késés esetén
- COD folyamat
- Egyetlen kijelölt kapcsolattartó a Deák részéről
- Felmondási feltételek (7 napos határidő)

---

## 9. Cost Structure (frissítve v2.1-ben)

### Befektetés (változatlan)

| Tétel | Összeg |
|-------|--------|
| MVP fejlesztés | ~4 620 EUR |
| Éves üzemeltetés | ~3 900 EUR |
| Marketing (pilot) | ~500-2 000 EUR |
| **Stop cap (összes kitettség)** | **~12-13 000 EUR** |

### Runway (v2.1 validált)

- **Exar Labs:** több hónapig, akár 1 évig finanszírozható
- **Ha pályázat bejön:** évekig
- **Tanulság:** a runway nem limitáló faktor -- lehet tanulni, nem kell túloptimalizálni

### Stop Decision Framework (változatlan)

| Döntés | Feltétel | Timing |
|--------|----------|--------|
| **Folytatás / scale** | ≥50 reg + ≥20 visszatérő (14 napon belül újrarendel) | max 3 hónap |
| **Stop** | 3 hónap után nem teljesülnek a kritériumok | max 3 hónap |
| **Bármikor** | Közös döntéssel, penalitás nélkül | — |
| **Hard stop** | 3 hónap után nincs kialakult heti habit | 90 nap |

---

## 10. Pilot Hypotheses (v2.1 kiegészítés)

| ID | Hipotézis | Validáció | Siker |
|----|-----------|-----------|-------|
| H1 | Van kereslet online húsrendelésre | 30 napos pilot | ≥15 rendelés |
| H2 | Vásárlók hajlandóak friss húst online rendelni | Regisztrációk | ≥30 regisztráció |
| H3 | Online kosárérték > bolti | Összehasonlítás | ≥20%-kal magasabb |
| H4 | Kialakul ismétlő vásárlási habit | ≥2 rendelés/user | ≥5 visszatérő |
| H5 | Bolt + QR a legjobb akvizíciós csatorna | UTM tracking | QR ≥40% regisztrációk |
| H6 | Kényelem az erősebb marketing üzenet | A/B teszt | Kényelem CTR > Frissesség |
| H7 | T+3 napos trigger hozza a 2. rendelést | WhatsApp + mérés | ≥50% emlékeztetőre rendel |
| **H8** | **Facebook Group növeli a visszatérési arányt** | Group tagok vs. nem tagok rendelési aránya | Group tagok 2x nagyobb visszatérési arány |
| **H9** | **A Failure Handling minősége befolyásolja a bizalmat** | Reklamáció utáni újrarendelés aránya | ≥60% újrarendel helyes kezelés után |

---

## 11. Pilot Success Metrics (frissítve v2.1-ben)

| Metrika | Cél | Mérés |
|---------|-----|-------|
| Regisztrációk | 30 | DH-42 |
| Leadott rendelések | 15 | DH-39 |
| Visszatérő vásárlók (≥2 rendelés) | 5 | DH-39 |
| Átlagos kosárérték | Mérni (bázis nélkül) | DH-39 |
| Rendelés visszavonás | < 20% | DH-39 |
| 2. rendelés aránya (T+3 trigger) | ≥50% | Manuális |
| **Stock-out / failure esetek kezelési ideje** | < 30 perc | Manuális |
| **Facebook Group tagszám** | ≥30 (= regisztráltak) | Facebook |

---

## 12. Kockázatok (FRISSÍTVE -- v2.1 új kockázatok)

### Meglévő kockázatok (v2.0-tól)

| Kockázat | Súlyosság | Mitigáció |
|----------|-----------|-----------|
| Supply kockázat (Deák nem szállít stabilan) | 🔴 Kritikus | Dry run, kapacitás ellenőrzés |
| Governance (Ibi) | 🟠 Közepes | Írásbeli megállapodás, egy kapcsolattartó |
| Domain blokkoló | 🟠 | Azonnal megoldandó |
| Pénzügyi adatok hiánya | 🟠 | Ibi jövő hétre |

### Új kockázatok (v2.1 azonosítva)

| Kockázat | Leírás | Mitigáció |
|----------|--------|-----------|
| **"Rejtett komplexitás"** | 5 rendelés = ok, 12 rendelés = káosz. A tipping point nagyon közel van | Stress test elvégzése launch előtt |
| **Single Courier Risk** | Deák egyedül szállít -- betegség, túlterhelés = system down | B terv: ki helyettesít? |
| **Overconfidence Risk** | "Van demand → működni fog" -- de a channel shift más bizalom-mechanikát igényel | Tudatos expectation management |
| **Facebook Dependence** | Retention = Facebook Group -- zajos, nem kontrollált csatorna | Alternatív visszacsalogatás tervezése post-pilot |

---

## 13. Fejlesztési státusz + Blokkolók (v2.1 naprakész)

### Fejlesztési státusz

| Fázis | Tartalom | Státusz |
|-------|----------|---------|
| 0 -- Alapok | Hosting, order schema | ✅ Kész |
| 1 -- Auth + Profil | Google OAuth, email auth, session | ~90% |
| 2 -- Termékkatalógus | Product listing, detail, kosár | ~80% |
| 3 -- Rendelési flow | Cart, checkout, order placement | ~85% |
| 4 -- Admin alap | Rendeléskezelés, státusz | Folyamatban |
| 5 -- Mészáros + Futár | Pregătire + Livrare tabok | Tervezett |
| 6 -- Statisztikák | KPI dashboard | Tervezett |
| 7 -- UX + GDPR | Guest-first, GDPR consent, Nézet váltó | Tervezett |
| 8 -- Launch prep | QR, Facebook Group, domain | Blokkolva |

> **Összesített haladás: 56% | Beta céldátum: 2026. április 14-17.**

### Blokkolók (v2.1 naprakész állapot)

| # | Blokkoló | Státusz v2.1 |
|---|----------|-------------|
| 1 | **Domain véglegesítése** | ❌ Nyitott |
| 2 | **Írásbeli partnerségi megállapodás** | ❌ Nyitott |
| 3 | **Revenue share % rögzítése** | 🟡 Várunk Ibire (jövő hét) |
| 4 | **Marketing budget cap** | ❌ Nyitott |
| 5 | **Reklamációs / failure handling folyamat** | 🟡 Részben (telefon megvan, app cancel ticket hiányzik) |
| 6 | **GDPR consent** (DH-68, DH-69) | 🟡 Fejlesztés alatt |
| 7 | **Guest-first UX** | 🟡 Fejlesztés alatt |
| **8** | **Order cancel funkció (app)** | ❌ **ÚJ TICKET SZÜKSÉGES** -- vásárló + Deák oldaláról egyaránt |

---

## 14. Order Lifecycle Stress Test (link -- külön dokumentum)

> ⚠️ **Az Order Lifecycle Stress Test NEM BMC elem -- ez dinamikus validáció.**
> A BMC statikus modell. A Stress Test az első "reality engine" a rendszerben.

**Dokumentum helye:** `DH_OPERATIONS/order_lifecycle_stress_test.md` _(létrehozandó)_

**Szimuláció tartalma:**
- 10 rendelés/nap
- 2 stock-out eset
- 1 késés
- 1 user cancel

**Cél:** Megtalálni hol szakad el a rendszer, mielőtt valódi vásárlókkal találkozunk.

---

## 15. Platform Vision -- Post-Pilot (változatlan v2.0-tól)

> ⚠️ Ez a szekció a jövőbe mutat. Most kizárólag a Phase 1-re fókuszálunk.

### 4 Fázisú Stratégiai Roadmap

```
Phase 1 -- PILOT & VALIDATION (MOST)
  ├── Deák Húsmíves app beta (ápr 14-17)
  ├── 30 regisztráció, 15 rendelés, 5 visszatérő user
  └── Pricing, kosárérték, failure handling tanulása

Phase 2 -- CATEGORY EXPANSION (Curated Supply)
  ├── 1 sajtos, 1 zöldséges, 1 gyümölcsös partner
  └── Supply reliability validálása multi-vendor szinten

Phase 3 -- GEOGRAPHIC EXPANSION
  └── 2. város pilot, supplier onboarding playbook

Phase 4 -- LOCAL MARKET LAYER (Discovery)
  └── Multi-vendor marketplace UX, premium kategória
```

---

## Változáskövetés

| Verzió | Dátum | Változás |
|--------|-------|---------|
| 0.1--0.5 | 2026-03-04--05 | Első draftek |
| 1.0 | 2026-03-27 | Átfogó frissítés |
| 2.0 | 2026-03-28 | Operatív élesítés (Flywheel, guest-first UX, sávos revenue share) |
| **2.3** | **2026-04-04** | **"Döntéstámogató rendszer."** Paradigmaváltás: Core Definíció szekció (döntéstámogató rendszer, nem webshop); 4-rétegű rendszerarchitektúra (L1-L4); Core Loop; Stratégiai pozicionálás (❌ webshop/marketplace/discount → ✅ optimalizáló rendszer); Value Proposition frissítés (#2 "Okosabb döntés" beillesztés); Savings→Feature mapping; Siker definíció. |
| **2.2** | **2026-04-03** | Release Roadmap kontextus hozzáadása (v0.1-v0.5 mérföldkövek). |
| **2.1** | **2026-03-29** | **"Build system that learns."** Strukturális változások: Supply Reliability explicit #1 erőforrásként; Failure Handling mint kötelező Key Activity + app cancel ticket (ÚJ DH); Facebook Trust Layer (Channel átírás 3 szintre); Tárgyalási stratégia Ibivel ("nem profit optim., hanem csatorna validáció"); Inkrementális margin realitás (rejtett költségek); 4 új kockázat (rejtett komplexitás, single courier, overconfidence, Facebook dependence); H8 + H9 hipotézisek; Order Lifecycle Stress Test külön dokumentumba (link a 14. szekcióban); Validált operatív adatok: D+1 szállítás, 11-17 időablak, 5→10 fél disznó/nap kapacitás, heti 1-2x vásárlási frekvencia, runway = nem limitáló. |
