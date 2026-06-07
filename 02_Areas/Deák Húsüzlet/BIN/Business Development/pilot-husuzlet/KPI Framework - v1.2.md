---
title: DH Metrics & KPI Framework
description: "Egy DH (Digital Handl?) pilot projekt 30 napos mérési és KPI keretrendszere, amely a hipotetikus feltételezéseket (BMC) validálja valós adatokkal; döntésre hangsúlyozva a 14 napos Second Order Rate-et mint North Star metrikus az igazi felhasználó visszatérésének mérésére."
description_source: auto
description_hash: 6aad2e6fcebdefa9
version: 1.2
date: 2026-04-04
project: DH (Deák Húsmíves Online Platform)
collaborators: ChatGPT (GPT-4o) — "Üzleti terv értékelés" session, Claude (Sonnet 4.6)
status: active
id: 5dafce42-6443-4197-a6f9-8e259310ce62
index_schema_version: 1
---
# DH Metrics & KPI Framework
### Pilot fázis — első 30 nap

---

## Alapelv

> **Nem "mindent mérünk."**
> Csak azt mérjük, ami döntést változtat.

**A DH metrics rendszer 2 rétegből áll:**

1. **BMC = hipotézis** — mit feltételezünk
2. **KPI layer = validáció** — mi történik valójában

Együtt: **Operating Business System** — egy tanuló rendszer, nem csak egy app.

---

## North Star KPI

```
Second Order Rate (14 napon belül)
= % of users who place 2nd order within 14 days
```

**Miért ez?**
- Az első rendelés = kíváncsiság / novelty
- A második rendelés = döntés, bizalom, értékelés
- A harmadik+ = habit

> "Nem az számít, hogy rendelnek-e. Hanem hogy visszajönnek-e rendelni 14 napon belül."

---

## Definíciók (lezárt döntések)

| Fogalom | Definíció |
|---------|-----------|
| **Retained user** | User aki 14 napon belül újra rendel |
| **Magic Moment** | Második sikeres rendelés 14 napon belül |
| **Activation Moment** | Első rendelés + sikeres kiszállítás + nincs friction |
| **Power user** | User aki 7 napon belül újra rendel |
| **Silent Churn** | User aki egyszer rendel, de 14 napig nem tér vissza |

---

## A 4-rétegű mérési modell

```
Acquisition → Activation → Retention → Economics
```

---

## 🔴 1. Acquisition — "bejönnek-e?"

### KPI #1 — QR → Visit

| Mutató | Cél | Megjegyzés |
|--------|-----|------------|
| QR scan / nap | 10-20 | UTM tracked |
| Visit → Registration | 30-50% | konverzió |

**Implementáció — UTM tracking (kötelező!):**

A QR kódok ne sima URL-re mutassanak. Minden forráshoz külön URL:

| Forrás | URL paraméter |
|--------|--------------|
| Bolt pult | `?utm_source=qr_counter&utm_medium=offline&utm_campaign=store` |
| Bolt ablak | `?utm_source=qr_window&utm_medium=offline&utm_campaign=store` |
| Szórólap | `?utm_source=qr_flyer&utm_medium=offline&utm_campaign=launch` |
| Facebook | `?utm_source=facebook&utm_medium=social&utm_campaign=store` |

**Session persistence szabály:** A `visitor_id` és `utm_source` az első érintésnél mentendő `localStorage`-ba és registration-kor backendnek elküldendő. **First-touch attribution** alkalmazandó.

**Döntési kérdés amit megválaszol:** "Ez az entry point működik-e?"

---

## 🟠 2. Activation — "az első rendelés megtörténik-e?"

### KPI #2 — Registration → First Order

| Mutató | Cél |
|--------|-----|
| Registration → First Order | ≥ 50% |

### KPI #3 — Time to First Order (TTFO) [PILOT DIAGNOSZTIKAI KPI]

| Mutató | Cél | Ha nem teljesül... |
|--------|-----|-------------------|
| Medián TTFO | ≤ 48 óra (v0.3) → < 24 óra (v0.4) | UX friction → javítandó |
| TTFO > 3 nap | < 20% | Nincs elég bizalom / urgency |

**Miért kritikus:** Ha a user nem rendel az első 24 órában, valószínűleg nem fog visszajönni. Ez a "lost conversion" legkorábbi jelzője.

**Döntési kérdés:** "Elég jó a value prop? Elég egyszerű a checkout?"

---

## 🟡 3. Retention — "visszajönnek-e?"

**Ez a legfontosabb réteg. Ez dönti el: van-e business.**

### KPI #4 — Second Order Rate (North Star)

| Mutató | Cél |
|--------|-----|
| Second Order Rate (14 nap) | ≥ 40-60% |


### KPI #4b — Threshold Achievement Rate [v1.2 NEW — SAVINGS ENGINE]

| Mutató | Cél |
|--------|-----|
| 150 RON Threshold Achievement Rate | ≥ 30% |
| 300 RON Achievement Rate (opcionális) | ≥ 10-15% |

**Definíció:** `threshold_achieved_150 / checkout_completed` — hány rendelés éri el az ingyenes szállítás küszöbét.

**Miért fontos:** Ez a Savings Engine core mechanic-jának validálása. Ha a threshold nudge nem működik, az egész L1 Decision Engine kérdéses.

### KPI #4c — Suggestion Acceptance Rate [v1.2 NEW — SAVINGS ENGINE]

| Mutató | Cél |
|--------|-----|
| Bundle acceptance rate | ≥ 15% |
| Reorder usage rate | mérendő |

**Definíció:** `bundle_added_to_cart / bundle_viewed` — hány user fogadja el az ajánlatot.

### KPI #5 — Retention rétegek

| Réteg | Ablak | Szerepe |
|-------|-------|---------|
| **Power user** | 7 nap | Habit formation, high-value segment |
| **Core retention** (fő KPI) | 14 nap | Elsődleges visszatérési definíció |
| **Stability / churn** | 30 nap | Hosszú távú életképesség |

**Ne a heti rendelést optimalizáld — hanem a 14 napos visszatérést.**
- Heti = túl agresszív (hamis negatív)
- Havi = túl lassú (késői tanulás)
- 14 nap = sweet spot

### KPI #6 — T+3 Trigger hatása

| Mutató | Cél |
|--------|-----|
| Response rate T+3 triggerből | ≥ 50% |
| Time Between Orders | validálja a heti 1-2x feltételezést |

### KPI #7 — Silent Churn Rate [PILOT DIAGNOSZTIKAI KPI]

```
Silent Churn = user aki egyszer rendel, de 14 napig nem tér vissza
```

**Ez a valódi veszteség metric.** A user nem panaszkodik — csak nem rendel újra.

---

## 🟣 4. Operáció — "összeomlik-e?"

### KPI #8 — Order Failure Rate [PILOT DIAGNOSZTIKAI KPI]

```
Order Failure Rate = (stock-out + késés + cancel) / összes rendelés
```

| Mutató | Cél | Riasztási küszöb |
|--------|-----|-----------------|
| Order Failure Rate | < 10% | > 20% = kritikus |
| Failure Response Time | < 30 perc | > 1 óra = rendszer probléma |

**Supply-side KPI-k (Deák teljesítmény):**

| KPI | Számítás | Cél |
|-----|----------|-----|
| **Fulfillment Rate** | sikeresen teljesített / összes rendelés | ≥ 95% |
| **Stock-out Rate** | stockout rendelés / összes rendelés | < 5% |
| **On-time Delivery Rate** | időben kiszállított / összes rendelés | ≥ 90% |
| **Issue Rate** | problémás rendelés / összes rendelés | < 10% |

> "Ha ezek rosszak → nincs retention → nincs business."

**Döntési kérdés:** "Össze fog omlani az operáció? Megbízható-e Deák mint partner?"

---

## 🔵 5. Economics — "értelmes-e pénzügyileg?"

*Ez a réteg másodlagos az elején, de az adatokat már most gyűjtjük.*

| KPI | Cél / Kérdés |
|-----|-------------|
| **AOV** (Average Order Value) | Nagyobb mint bolt? Trend? |
| **Orders / User / Week** | Habit kialakul-e? |
| **Revenue / Order** | Exar share kiszámítható legyen |
| **Cost per Retained User** | CAC = nem signup cost, hanem visszatérő user cost |
| **Contribution margin / order** | Revenue - szállítás - csomagolás - issue cost |

**Fontos:** A margin modell most optimista bias-os. Hiányzó költségek:
- Csomagolás
- Kiszállítás idő (koordináció)
- Hibák kezelési ideje (telefon, refund)

---

## 📊 Minimál KPI Dashboard — első 7 nap

Ha csak ezt méred, elég:

| # | KPI | Cél | Riasztás |
|---|-----|-----|----------|
| 1 | QR scans / nap | 10-20 | < 5 |
| 2 | Registration rate (%) | 30-50% | < 20% |
| 3 | First order rate (%) | ≥ 50% | < 30% |
| 4 | **Second order rate (%)** ⭐ | ≥ 40% | < 20% |
| 5 | Orders per user | növekvő trend | csökken |
| 6 | Order failure rate (%) | < 10% | > 20% |
| 7 | AOV | > bolt érték | n/a |

**Dashboard struktúra (Frappe Script Report):**

```
[ FŐ FUNNEL — középen, nagy ]
QR → Visit → Registration → First Order → Second Order

[ RETENTION ]      [ OPERATIONS ]      [ ECONOMICS ]
Returning: 12/30   Total orders: 30    AOV: 85 RON
Repeat: 40%        Failures: 5 (16%)  Orders/user: 1.6
Days btw: 4.2d     Stock-out: 3       Revenue (Exar): 120 EUR
```

**Színjelölés:**
- 🟢 jó — megyünk tovább
- 🟡 figyelni kell
- 🔴 probléma — beavatkozás szükséges

---

## 🧠 Döntési logika (Go/No-Go)

| Állapot | Feltételek | Teendő |
|---------|-----------|--------|
| 🟢 **GREEN — scale** | ≥30 reg, ≥15 order, ≥5 visszatérő, ≥40% second order | Következő 30 nap tervezése |
| 🟡 **YELLOW — tanulunk** | Van order, de nincs retention | UX, trust, supply javítás |
| 🔴 **RED — stop/pivot** | Nincs first order VAGY nincs second order | Alapvető feltételezés téves |

---

## 📡 Event Tracking Architektúra

### Event lista (Firebase Analytics — logEvent())

| Event neve | Mikor tüzel | Prioritás |
|-----------|------------|-----------|
| `landing_view` | QR megnyitás / oldal betöltés | P0 |
| `product_list_view` | Terméklista megtekintés | P0 |
| `product_detail_view` | Termék részletek | P1 |
| `add_to_cart` | Kosárba helyezés | P0 |
| `checkout_started` | Checkout folyamat kezdése | P0 |
| `login_started` | Login/reg oldal megnyitás | P1 |
| `registration_completed` | Sikeres regisztráció | P0 |
| `order_created` | Sikeres rendelés | P0 |
| `order_delivered` | Sikeres kiszállítás | P0 |
| `order_cancelled` | Lemondott rendelés | P0 |
| `order_failed_stockout` | Nincs készlet | P0 |
| `order_failed_delay` | Késés | P1 |
| `repeat_order_created` | Visszatérő rendelés | P0 |
| `order_reason_selected` | WHY DID YOU ORDER? prompt válasz | P1 |

### Mezők (Firebase event parameters)

```
event_name       string
event_time       datetime
visitor_id       string (anonim azonosító)
session_id       string (session azonosító)
user_id          string (ha regisztrált)
order_id         string (ha rendelés kapcsolódik)
utm_source       string
utm_medium       string
utm_campaign     string
page             string
metadata_json    json (extra adatok)
```



### v0.3 Savings Engine eventek (Firebase Analytics — logEvent()) [v1.2 NEW]

| Event neve | Mikor tüzel | Prioritás |
|-----------|------------|-----------|
| `savings_counter_viewed` | Savings progress bar megjelenik a kosárban | P0 |
| `threshold_achieved_150` | User eléri a 150 RON küszöböt (ingyenes szállítás) | P0 |
| `threshold_achieved_300` | User eléri a 300 RON küszöböt (2% kedvezmény) | P0 |
| `bundle_added_to_cart` | Családi csomag hozzáadva a kosárhoz | P0 |
| `reorder_clicked` | Újrarendelés gomb kattintás (Rendeléseim) | P0 |
| `basket_loaded` | Basket Loader betölt egy korábbi rendelést | P0 |
| `recap_viewed` | Post-order savings recap megjelenik | P0 |
| `recap_reorder_clicked` | Recap képernyőn újrarendelés kattintás | P0 |
| `checkout_started` | Checkout folyamat kezdése (guardrail: checkout_duration) | P0 |
| `checkout_completed` | Checkout sikeresen befejezve (guardrail: checkout_duration) | P0 |

**Guardrail mérés:**
- `checkout_duration` = `checkout_completed.timestamp - checkout_started.timestamp`
- Baseline mérés v0.2-ben → v0.3 feature-ök nem növelhetik
- Margin tracking: backend számolja (nem Firebase) — `order.savings` objektumban

### Identity stitching logika

```
Fázis A — anonim:  visitor_id + session_id + utm_source
Fázis B — azonosított:  visitor_id → linked to user_id (regisztrációkor)
```

**7 lépéses funnel ugyanazon a useren:**
1. QR scan → `landing_view` + `visitor_id` létrejön
2. Böngészés → `product_list_view` (ugyanaz a `visitor_id`)
3. Kosár → `add_to_cart`
4. Checkout → `checkout_started`
5. Regisztráció → `registration_completed` + `user_id` kapcsolva
6. Első rendelés → `order_created` (user_id + order_id)
7. Második rendelés → `repeat_order_created`

### A 7 KPI technikai kiszámítása

| KPI | SQL logika |
|-----|-----------|
| QR scans / visit | `COUNT(visitor_id) WHERE utm_source LIKE 'qr_%'` |
| Registration rate | `registration_completed / landing_view` |
| First order rate | `order_created / registration_completed` |
| Second order rate | `repeat_order_created / first_order_users` |
| Orders per user | `COUNT(order_created) GROUP BY user_id` |
| Failure rate | `order_failed_* / order_created` |
| AOV | `SUM(order_total) / COUNT(order_created)` |

---

## 💬 "WHY DID YOU ORDER?" — Implementáció

**Mikor:** Közvetlenül az első rendelés leadása után (post-order screen)

**Forma:** In-app micro prompt — opcionális (skip-elhető)

**Kérdés:** "Miért döntöttél úgy, hogy most rendelsz?"

**Válaszok:**
1. Elfogyott otthon
2. Kipróbálni akartam
3. Kényelmesebb mint boltba menni
4. Láttam Facebookon
5. Egyéb... (free text)

**Technikai megvalósítás:**
- Frappe form submit utáni popup/inline blokk
- Esemény: `order_reason_selected` mentve az Analytics Event DocType-ba
- Csak first order után jelenik meg
- **Haladó (post-MVP):** Second order után "Miért rendeltél újra?" — ez még értékesebb adat

---

## 📈 Analytics Tool Stratégia

### Fázis 1 — Pilot (0-50 user, 0-100 rendelés)

**Eszköz: Firebase Analytics** (2026-03-31 döntés — DH-104 In Progress)

| Pro | Miért |
|-----|-------|
| Zero custom kód | SDK bekötés ~félnap |
| Automatikus UTM tracking | Csatorna attribution beépítve |
| Real-time dashboard | Firebase Console |
| Event-based | Custom eventek egyszerűen logolhatók |

**Megtakarítás a Frappe Script Report-hoz képest: ~8-13 munkanap → ~félnap.**

A KPI dashboard (DH-82 Done) és Failure tracking (DH-81 Done) Firebase Console-ban valósul meg a custom Frappe DocType helyett.

### Fázis 2 — Váltás feltételei

**Válts PostHog-ra ha:**
- Több mint 1 acquisition csatorna van (QR + Facebook + flyer + ads)
- Funnel kérdések jelennek meg ("hol esik ki a user?")
- Cohort analysis kell ("QR-ről jöttek vs. Facebook-ról?")
- Nincs már idő manuális elemzésre

**DH trigger:** ~30-50 user / ~20-30 rendelés elérése után érdemes bekötni.

**Végső architektúra:**
```
Frappe = source of truth (rendelések, userek, supply adatok)
PostHog = analysis layer (funnel, attribution, cohorts)
```

---

## 🗓 Implementációs ütemterv

### Következő 7 nap (launch előtt kötelező)

| Feladat | Prioritás | Státusz | DH ticket |
|---------|-----------|---------|-----------|
| Retention definíció rögzítése | P0 | ✅ DONE (14 nap) | — |
| Magic Moment definíció | P0 | ✅ DONE (2. rendelés 14 napon belül) | — |
| Firebase Analytics SDK bekötése | P0 | 🔄 In Progress | DH-104 |
| UTM/QR forráskövetés + Firebase UTM | P0 | 🔄 Sprint 2 To Do | DH-80 |
| KPI dashboard (Firebase Console) | P0 | ✅ DONE | DH-82 |
| Failure event tracking | P0 | ✅ DONE | DH-81 |
| QR tracking kiértékelés | P1 | ⏳ Sprint 2 To Do | DH-109 |
| "WHY DID YOU ORDER?" popup | P1 | ⏳ Sprint 2 To Do | DH-83 |
| Supply KPI manuális naplózás (Deák) | P1 | TODO | — |

### Launch után (első 2-4 hét)

| Feladat | Prioritás |
|---------|-----------|
| NPS kérdés bevezetése (egyszerű, post-order) | P2 — v0.4 |
| Unit economics tracking per rendelés | P2 |
| CAC redefiníció (retained user cost) | P2 |
| Channel → retention mapping (QR vs. Facebook) | P2 |

### Scale előtt

| Feladat | Prioritás |
|---------|-----------|
| Supplier Playbook — SLA, onboarding, conflict handling | P3 |
| Governance formalizálás (revenue share írásban) | P3 |
| PostHog bekötése | P3 |
| Pricing strategy finalizálása | P3 |

---

## ⚠️ Nyitott kérdések (még átbeszélendő)

Ezek még nincsenek lezárva — következő megbeszélés agenda:

1. **Magic Moment validálása** — az "első sikeres rendelés" tényleg az Activation Moment? Vagy az amikor a minőséget tapasztalja?
2. **Retention period** — a 14 napos választás validált a vásárlási szokásból? (heti 1-2x feltételezés)
3. **Margin reality** — mi a valódi inkrementális margin ha beleszámítjuk a csomagolást és koordinációs időt?
4. **Supplier conflict risk** — Ibi bevonása és szerepe a supply KPI-k teljesítésében
5. **Scaling threshold** — milyen metrikák elérésekor terjeszkednek városba?
6. **App split vs. unified?** — 2 app (Daily + Local Market) vs. 1 platform — mikor releváns kérdés?

---


---

## 📋 Mérési lefedettség ellenőrzés (v1.1, 2026-04-03)

| Mérési terület | Lefedettség | Megjegyzés |
|---------------|-------------|-----------|
| QR → Visit tracking | ✅ Firebase UTM | DH-80, DH-104 |
| Registration conversion | ✅ Firebase event | registration_completed |
| First order tracking | ✅ Firebase event | order_created |
| Second order tracking | ✅ Firebase event | repeat_order_created |
| Order failure tracking | ✅ Frappe Desk | DH-81 Done |
| KPI dashboard | ✅ Firebase Console | DH-82 Done |
| "Miért rendeltél?" prompt | ⏳ Sprint 2 To Do | DH-83 |
| QR forrás kiértékelés | ⏳ Sprint 2 To Do | DH-109 |
| Supply KPI (Deák oldal) | ❌ Hiányzik | Manuális naplózás szükséges |
| Csomagolási/szállítási költség | ❌ Hiányzik | Margin modellhez kellene |
| NPS / elégedettség | ❌ Post-launch | Első 2-4 hétben bevezetendő |
| Cohort analysis | ❌ PostHog váltáskor | ~30-50 user után |

| Savings counter tracking | ✅ Firebase event | savings_counter_viewed (v1.2) |
| Threshold achievement tracking | ✅ Firebase event | threshold_achieved_150/300 (v1.2) |
| Bundle tracking | ✅ Firebase event | bundle_added_to_cart (v1.2) |
| Reorder tracking | ✅ Firebase event | reorder_clicked, basket_loaded (v1.2) |
| Recap engagement tracking | ✅ Firebase event | recap_viewed, recap_reorder_clicked (v1.2) |
| Checkout duration (guardrail) | ✅ Firebase event | checkout_started/completed delta (v1.2) |
| "User feels smarter" | ❌ v0.4-re halasztva | Lean: recap thumbs up/down |

**Konklúzió (v1.2 frissítés):** A digitális mérés nagyrészt lefedett a Firebase váltással. A hiányzó területek az operatív oldalon vannak (supply KPI, költségek) — ezek manuális adatgyűjtést igényelnek a pilot alatt.

## BMC ↔ KPI Megfeleltetés

| BMC blokk | KPI |
|-----------|-----|
| Customer Segments | Activation rate |
| Value Proposition | Conversion + NPS |
| Channels | CAC per channel |
| Revenue | ARPU + margin |
| Customer Relationship | Retention (14 nap) |
| Key Activities | Order success rate |
| Key Partners | Supply reliability (Deák) |

---

*Forrás: ChatGPT "Üzleti terv értékelés" session (2026-03-29) + YC Consumer Startup Metrics anyag elemzése + Claude (Sonnet 4.6) szintézis*


### Változásnapló (v1.2, 2026-04-04)

**Forrás:** Claude KPI Alignment Audit + ChatGPT (Savings Engine Koncepció session) stratégiai értékelés

**Változások:**
- **v0.3 Savings Engine Firebase eventek hozzáadva** (10 új event: savings_counter_viewed, threshold_achieved_150/300, bundle_added_to_cart, reorder_clicked, basket_loaded, recap_viewed, recap_reorder_clicked, checkout_started/completed)
- **Threshold Achievement Rate KPI** hozzáadva (#4b) — cél: ≥30% (150 RON), ≥10-15% (300 RON)
- **Suggestion Acceptance Rate KPI** hozzáadva (#4c) — cél: ≥15% (bundle)
- **TTFO target frissítve:** <24 óra → ≤48 óra (v0.3), tighten to <24 óra v0.4-ben (nincs email/push trigger v0.3-ban)
- **Guardrail mérés definiálva:** checkout_duration = checkout_completed - checkout_started timestamp delta; margin: backend számolja
- **NPS eltávolítva a v0.3 siker kritériumokból** → v0.4-re halasztva (nincs infra)
- **"User feels smarter" metrika** v0.4-re halasztva — lean alternatíva: recap screen thumbs up/down
- **Mérési lefedettség tábla frissítve** 7 új sorral (Savings Engine coverage)
