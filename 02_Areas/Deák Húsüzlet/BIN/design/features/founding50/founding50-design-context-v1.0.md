---
title: "Founding 50 Program — Teljes Feature Kontextus"
version: "1.0"
created: 2026-04-22
purpose: "Claude Design átadás — egyetlen fájlban a teljes feature kontextus"
jira_tickets: [DH-150, DH-151, DH-152, DH-153, DH-154, DH-155, DH-156]
sprint: "DH Sprint 3"
target_release: "v0.3 Beta (~2026-05-15)"
id: cab3a3bc-2124-464e-b75c-3c31d2759e47
index_schema_version: 1
---

# Founding 50 Program — Teljes Feature Kontextus

> **Cél:** Ez a dokumentum egyetlen helyre gyűjti a Founding 50 feature teljes kontextusát, hogy Claude Design (vagy bármilyen design tool) számára átadható legyen wireframe, UI design és UX flow készítéshez.

---

## 1. PROJEKT KONTEXTUS

### Mi a Deák Húsmíves Online Platform (DH)?
- Kézműves húsüzem online rendelési + házhozszállítási rendszere
- Helyszín: Székelyudvarhely (Odorheiu Secuiesc), ~30.000 lakos
- Tech stack: Frappe (Python backend) + Vue 3 PWA frontend
- Jelenlegi állapot: v0.2 KÉSZ (analytics), Sprint 3 aktív (Savings Engine)
- Domain: deakhus.ro (éles), staging.deakhus.ro (staging)

### Design rendszer
- **Primary color:** #9B2335 (bordó/vörös)
- **Background:** #F5F0EB (meleg bézs)
- **Text:** #2D2D2D (sötét), #777 (secondary)
- **Border:** #E8E0D8
- **Font:** Segoe UI / system-ui / sans-serif
- **Mobile-first:** 375px szélességben renderel
- **Ikonok:** Lucide SVG (inline, NEM emoji)
- **Nyelv:** Magyar elsődleges, román másodlagos (HU/RO toggle)

### Meglévő wireframe-ek (referencia)
- Gallery: https://deakhus.netlify.app
- Savings engine: v0.3-wireframes-v3.html
- Reorder: reorder-list.html, reorder-loaded-cart.html
- Consent/GDPR: v0.3-consent-gdpr.html
- Legal info profile: v0.3-legal-info-profile.html

---

## 2. FEATURE ÖSSZEFOGLALÓ

### Mi a Founding 50?
Limitált, exkluzív early adopter toborzási kísérlet: az első 50 regisztrált felhasználó 3 hónapig ingyenes kiszállítást kap. **NEM marketing kampány** — kontrollált user cohort kísérlet.

### Paraméterek

| Paraméter | Érték | Indoklás |
|-----------|-------|----------|
| Max létszám | **50 fő** | 30k-s kisvárosban reális; elég nagy kohort a méréshez |
| Időtartam | **3 hónap / user** | Rövid, intenzív; elegendő a szokás kialakulásához |
| Jutalom | **Ingyenes szállítás** | Alacsony költség (~900 EUR), magas perceived value |
| Soft feltétel | **Havonta min. 2 rendelés** | NEM kommunikált upfront; backend-based retention filter |
| Inaktivitási küszöb | **30 nap rendelés nélkül** | Státusz elvesztése, hely felszabadul |
| Waitlist | **Igen** | Betelt → várólistára; kiesőt pótolni (MVP-ben manuális) |

### Design elvek
1. **Ne kommunikálj kötelezettséget** — "aktív tagok" elég
2. **Scarcity kötelező** — counter nélkül nem működik
3. **Ne overengineereld** — gyors launch > tökéletes rendszer
4. **Behavior > feature** — cél: rendelés, nem regisztráció
5. **Egy kampány, egy link, egy cohort** — később jöhetnek újabb hullámok

---

## 3. USER FLOW

### 3.1 Teljes belépési flow

```
Kampány forrás (QR kód boltban / személyes ajánlás / szórólap)
  → UTM paraméterrel: ?utm_source=X&utm_campaign=founding50
    → Termékek oldal betöltődik (guest-first UX, login nem kell böngészéshez)
      → 2-3 sec delay VAGY első scroll után:
        → KAMPÁNY MODAL megjelenik
          → "Csatlakozom most" → Regisztráció oldal
            → Google / Facebook / Email regisztráció
              → Founding member státusz auto-beállítás
                → Vissza termékek oldalra
                  → GRATULÁCIÓ MODAL megjelenik
          → "Talán később" → Modal eltűnik, session-ben nem tér vissza
```

### 3.2 Modal megjelenési logika
- **Trigger:** UTM campaign = "founding50" VAGY direct landing
- **Timing:** 2-3 sec delay VAGY első scroll event (amelyik hamarabb)
- **NEM jelenik meg ha:** user már regisztrált / founding member / program betelt
- **Session rule:** "Talán később" → sessionStorage flag, nem tér vissza

### 3.3 Állapotok

| Állapot | Counter kijelzés | CTA | Leírás |
|---------|-----------------|-----|--------|
| Van hely (< 50) | "X / 50 hely betelve" | "Csatlakozom most" | Standard flow |
| Betelt (50/50) | "50 / 50 — Betelt!" | "Feliratkozom a várólistára" | Waitlist flow |
| User már tag | — (no modal) | — | Badge megjelenítés |
| Lejárt (3 hó után) | — | — | Badge eltűnik, normál szállítási díj |

---

## 4. UI KOMPONENSEK — RÉSZLETES SPEC

### 4.1 Kampány Modal

**Layout:** Centered modal, overlay backdrop, mobile-first (375px)

**Magyar verzió:**
- **Cím:** "Legyél az első 50 alapító tag között"
- **Leírás:** "Csatlakozz a Deák Húsmíves online rendelési programjához, és 3 hónapig ingyenes kiszállítást kapsz. Már csak kevés hely maradt."
- **Counter:** "X / 50 hely betelve" (dinamikus, API-ból, progress bar vizualizáció)
- **CTA gomb (primary):** "Csatlakozom most" → navigáció regisztrációs oldalra
- **Secondary action (text link):** "Talán később" → modal bezárás

**Román verzió:**
- **Cím:** "Fii printre primii 50 de membri fondatori"
- **Leírás:** "Alătură-te programului de comenzi online Deák Húsmíves din Odorheiu Secuiesc și beneficiezi de livrare gratuită timp de 3 luni. Au mai rămas puține locuri."
- **CTA:** "Mă înscriu acum"
- **Secondary:** "Poate mai târziu"

**Vizuális javaslatok:**
- Counter: progress bar vagy számláló (37/50 stílus), scarcity érzet
- Háttér: #9B2335 primary vagy fehér card sötét overlay-jel
- Lucide ikon: `gift`, `users`, vagy `star`

---

### 4.2 Gratuláció Modal (sikeres regisztráció után)

**Magyar verzió:**
- **Cím:** "Üdv az alapító tagok között!"
- **Leírás:** "Gratulálunk! Mostantól 3 hónapig ingyenes kiszállítást kapsz minden rendelésedre Székelyudvarhely területén. Rendelj most és próbáld ki!"
- **CTA:** "Megnézem a termékeket"
- **Kiegészítő:** "Az ingyenes szállítás [DÁTUM]-ig érvényes."

**Román verzió:**
- **Cím:** "Bun venit în rândul membrilor fondatori!"
- **Leírás:** "Felicitări! De acum ai livrare gratuită timp de 3 luni pentru toate comenzile tale în Odorheiu Secuiesc. Comandă acum și încearcă!"
- **CTA:** "Văd produsele"

**Vizuális javaslatok:**
- Ünneplős feeling: confetti vagy badge animáció
- Szín: zöld/arany success tónus a #9B2335 primary mellett
- Lucide ikon: `party-popper`, `award`, `badge-check`

---

### 4.3 Alapító Tag Badge

**Megjelenési helyek:**
1. **Profil oldal** (Contul meu) — badge a név mellett
2. **Checkout oldal** — szállítási díj soron
3. **Rendelési felület** — opcionális kis indikátor

**Badge design:**
- Chip/tag stílus: "Alapító tag" / "Membru fondator"
- Szín: arany/bronz tónus vagy primary (#9B2335) háttérrel fehér szöveg
- Lucide ikon: `award` vagy `shield-check`

**Checkout szállítási díj override:**
```
Szállítás:  ~~15 RON~~  INGYENES (Alapító tag)
```
- Áthúzott eredeti ár + "INGYENES" zöld highlight + badge hivatkozás

---

### 4.4 Betelt Állapot Modal

**Magyar verzió:**
- **Counter:** "50 / 50 — Betelt!"
- **Cím:** "Az alapító program betelt"
- **Leírás:** "Sajnos az 50 hely már betelt. Iratkozz fel a várólistára, és értesítünk, ha hely szabadul fel!"
- **CTA:** "Feliratkozom a várólistára"
- **Secondary:** "Rendben, nézem a termékeket"

---

## 5. ADATMODELL (fejlesztői referencia)

### User DocType kiterjesztés

| Mező | Típus | Leírás |
|------|-------|--------|
| `founding_member` | Boolean | Aktív founding tag-e |
| `founding_start_date` | Date | Program belépés dátuma |
| `founding_expiry_date` | Date | founding_start_date + 90 nap |
| `founding_campaign` | Link → Campaign | Melyik kampányból jött |
| `founding_waitlist` | Boolean | Várólistán van-e |
| `founding_inactive_date` | Date | Mikor vesztette el a státuszt |

### Campaign DocType (új)

| Mező | Típus | Leírás |
|------|-------|--------|
| `name` | Data | Kampány azonosító (pl. "founding50-wave1") |
| `title` | Data | Megjelenítendő név |
| `max_members` | Int | Maximum létszám (50) |
| `current_members` | Int (computed) | Jelenlegi aktív tagok |
| `benefit_type` | Select | free_delivery / percentage_discount / fixed_discount |
| `benefit_duration_days` | Int | 90 nap |
| `status` | Select | active / full / closed |
| `utm_campaign` | Data | UTM campaign paraméter |
| `start_date` | Date | Kampány indulás |
| `end_date` | Date | Kampány lezárás (opcionális) |

### API endpoint

```
GET /api/method/founding50_status
→ { slots_total: 50, slots_taken: 37, slots_remaining: 13, is_member: false, expiry_date: null }
```

### Delivery fee override (pseudo-code)

```python
if user.founding_member AND today <= user.founding_expiry_date:
    delivery_fee = 0  # Ingyenes
else:
    delivery_fee = 15  # RON
```

### Inaktivitási job (napi scheduled)

```python
# Ha founding_member = true ÉS last_order > 30 napja → founding_member = false
```

---

## 6. UTM / KAMPÁNY FORRÁS TRACKING

| Forrás | URL minta |
|--------|-----------|
| Bolt QR kód | `deakhus.ro?utm_source=qr_store&utm_campaign=founding50` |
| Facebook post | `deakhus.ro?utm_source=facebook&utm_campaign=founding50` |
| Személyes ajánlás | `deakhus.ro?utm_source=referral&utm_campaign=founding50` |
| Szórólap | `deakhus.ro?utm_source=flyer&utm_campaign=founding50` |

Frontend: UTM → sessionStorage → regisztrációkor user record-ba mentés

---

## 7. FIREBASE ANALYTICS ESEMÉNYEK

| Event | Trigger | Paraméterek |
|-------|---------|-------------|
| `founding50_modal_shown` | Modal megjelenik | utm_source, utm_campaign |
| `founding50_cta_clicked` | "Csatlakozom most" kattintás | — |
| `founding50_dismissed` | "Talán később" kattintás | — |
| `founding50_registered` | Sikeres regisztráció + founding member | user_id, slot_number |
| `founding50_waitlisted` | Várólistára kerülés | — |
| `founding50_order` | Founding member rendel | order_value, order_number |
| `founding50_expired` | 3 hónap lejárt | total_orders_during |
| `founding50_churned` | 30 napos inaktivitás | days_since_last_order |

---

## 8. KPI-K ÉS SIKER KRITÉRIUMOK

| KPI | Cél | Mérés módja |
|-----|-----|-------------|
| Regisztráció → első rendelés (TTFO) | ≤ 72 óra | founding_start_date vs first_order_date |
| Second order rate (14 napon belül) | ≥ 40% | Frappe query |
| Orders / user / hónap | ≥ 2 | Átlag számítás |
| Retention (30 nap) | ≥ 60% | Aktív tagok / összes tag |
| AOV (average order value) | ≥ 80 RON | Átlag rendelésérték |
| Inaktivitás miatti kiesés | ≤ 20% | Kiesett tagok / összes |

---

## 9. BUDGET

| Paraméter | Érték |
|-----------|-------|
| Founding tagok | 50 fő |
| Időtartam | 3 hónap |
| Várható rendelés/fő/hó | 2 |
| Összes rendelés | 300 |
| Szállítási díj / rendelés | ~15 RON |
| **Teljes szállítási költség** | **~4.500 RON (~900 EUR)** |

---

## 10. JIRA TICKETEK

**Jira projekt:** DH (Deák Húsmíves) -- https://exarlabs.atlassian.net/browse/DH
**Sprint:** DH Sprint 3 (2026-04-15 -- 2026-05-11)
**Board:** https://exarlabs.atlassian.net/jira/software/projects/DH/boards/100

### Ticket mátrix

| Ticket | Típus | Summary | Effort | Státusz | Design wireframe |
|--------|-------|---------|--------|---------|-----------------|
| [DH-150](https://exarlabs.atlassian.net/browse/DH-150) | Task | Founding 50 Program (PARENT) | L | To Do | -- |
| [DH-151](https://exarlabs.atlassian.net/browse/DH-151) | Task | Backend: Campaign DocType + User mezők + delivery fee override | M | To Do | N/A (backend) |
| [DH-152](https://exarlabs.atlassian.net/browse/DH-152) | Task | Backend: Inaktivitási scheduler (30 napos retention filter) | S | To Do | N/A (backend) |
| [DH-153](https://exarlabs.atlassian.net/browse/DH-153) | Story | Frontend: Kampány modal (counter + CTA + megjelenési logika) | M | To Do | **TBD -- DESIGN FELADAT** |
| [DH-154](https://exarlabs.atlassian.net/browse/DH-154) | Story | Frontend: Gratuláció modal + Alapító tag badge + checkout override UI | S | To Do | **TBD -- DESIGN FELADAT** |
| [DH-155](https://exarlabs.atlassian.net/browse/DH-155) | Story | Frontend: Betelt állapot UI + waitlist regisztráció | S | To Do | **TBD -- DESIGN FELADAT** |
| [DH-156](https://exarlabs.atlassian.net/browse/DH-156) | Task | Analytics: Firebase events (8 új event) | S | To Do | N/A (analytics) |

### Részletes ticket leírások

#### [DH-150](https://exarlabs.atlassian.net/browse/DH-150) -- Founding 50 Program (PARENT TICKET)
- **Típus:** Task | **Sprint:** DH Sprint 3
- A teljes Founding 50 feature parent ticketje. Tartalmazza az összefoglalót, user flow-t, UI spec-et, adatmodellt, budget-et.
- Minden sub-ticket erre hivatkozik.

#### [DH-151](https://exarlabs.atlassian.net/browse/DH-151) -- Backend: Campaign DocType + User mezők + delivery fee override
- **Típus:** Task | **Effort:** M (Medium)
- Új Campaign DocType létrehozása (name, max_members, benefit_type, status, utm_campaign)
- User DocType kiterjesztés (founding_member, founding_start_date, founding_expiry_date, founding_campaign, founding_waitlist)
- Delivery fee override logika: `if founding_member AND today <= expiry -> fee = 0`
- API endpoint: `/api/method/founding50_status` -> slots_total, slots_taken, slots_remaining, is_member, expiry_date

#### [DH-152](https://exarlabs.atlassian.net/browse/DH-152) -- Backend: Inaktivitási scheduler
- **Típus:** Task | **Effort:** S (Small)
- Napi scheduled job (hooks.py): 30+ napja nem rendelő founding member -> `founding_member = false`
- Admin értesítés kiesésről
- MVP: waitlist pótlás manuális

#### [DH-153](https://exarlabs.atlassian.net/browse/DH-153) -- Frontend: Kampány modal
- **Típus:** Story | **Effort:** M (Medium)
- **WIREFRAME SZÜKSÉGES** -- ez a fő design feladat
- Kampány modal: cím, leírás, dinamikus counter (X/50), CTA + secondary
- Megjelenési logika: UTM detection -> sessionStorage, 2-3 sec delay VAGY első scroll
- Session flag: "Talán később" -> nem tér vissza
- Betelt állapot kezelés (50/50)
- Kétnyelvű: HU + RO

#### [DH-154](https://exarlabs.atlassian.net/browse/DH-154) -- Frontend: Gratuláció modal + badge + checkout override
- **Típus:** Story | **Effort:** S (Small)
- **WIREFRAME SZÜKSÉGES**
- Gratuláció modal: sikeres founding regisztráció után, ünneplős feeling
- "Alapító tag" / "Membru fondator" badge: profil + checkout + rendelési felület
- Checkout szállítási díj sor: ~~15 RON~~ INGYENES (Alapító tag)
- Kétnyelvű: HU + RO

#### [DH-155](https://exarlabs.atlassian.net/browse/DH-155) -- Frontend: Betelt állapot + waitlist
- **Típus:** Story | **Effort:** S (Small)
- **WIREFRAME SZÜKSÉGES**
- Betelt állapot modal (50/50 counter)
- Waitlist regisztráció flow
- Admin waitlist nézet (MVP: manuális pótlás)

#### [DH-156](https://exarlabs.atlassian.net/browse/DH-156) -- Analytics: Firebase events
- **Típus:** Task | **Effort:** S (Small)
- 8 új Firebase event: founding50_modal_shown, _cta_clicked, _dismissed, _registered, _waitlisted, _order, _expired, _churned
- Firebase Debug View-ban ellenőrizhető
- UTM paraméterek átadódnak

### Design feladat összefoglaló

A design munkából **3 ticket** igényel wireframe-et:

| Ticket | Mi kell | Prioritás |
|--------|---------|-----------|
| **[DH-153](https://exarlabs.atlassian.net/browse/DH-153)** | Kampány modal (counter + CTA + megjelenési logika) | **MAGAS** -- ez az első amit a user lát |
| **[DH-154](https://exarlabs.atlassian.net/browse/DH-154)** | Gratuláció modal + badge + checkout override | KÖZEPES -- sikeres regisztráció utáni flow |
| **[DH-155](https://exarlabs.atlassian.net/browse/DH-155)** | Betelt állapot + waitlist regisztráció | ALACSONY -- csak ha betelt a program |

A wireframe-ek a meglévő DH design rendszerrel készüljenek (lásd 1. szekció: Design rendszer).

---

## 11. KOCKÁZATOK

| Kockázat | Valószínűség | Hatás | Mitigáció |
|----------|-------------|-------|-----------|
| Kevesebb mint 50 regisztráció | Közepes | Program nem tölti be célját | Aktívabb toborzás, deadline kitolás |
| Magas churn (>40%) | Közepes | ROI csökken | Inaktivitási filter benne van |
| Szállítási kapacitás nem bírja | Alacsony | Fulfillment probléma | Max ~25 rendelés/hét — kezelhető |
| Tech debt | Közepes | Nehezebb scale-elni | MVP minimális, Phase 2-ben refaktor |

---

## 12. BRAINSTORM EREDET

**Forrás:** Szabolcs + ChatGPT (Deák GPT) brainstorm session (2026-04-22)
**ChatGPT link:** https://chatgpt.com/g/g-p-69cbee4a04c481918a2a738959b92361-deak/c/69da0a38-ce68-8391-bfb4-a2bbf24a66e7 (msg 74-95)

### Szabolcs eredeti ötlete
Tesztelési hullámok, early adopterek toborzása kedvezményekkel. Cél: forgalom generálás + közvetlen feedback + retention. Többféle hullámban gondolkodik (alpha, beta, mobil app teszterek).

### ChatGPT finomítások
- 50 fő (nem 100) — Szabolcs döntése
- 3 hónap (nem 6) — Szabolcs döntése
- "Founding 50" branding — ChatGPT javaslat
- Soft retention filter (30 nap inaktivitás = kiesés, de NEM kommunikált) — ChatGPT javaslat
- Scarcity counter kötelező — ChatGPT javaslat, Szabolcs elfogadta
- Badge rendszer — ChatGPT javaslat

### Szabolcs UX döntései (msg 86, 92)
- UTM source tracking kötelező
- Kampány modal a termékek oldalon (NEM landing page)
- Regisztráció = csatlakozás (nincs külön "founding form")
- Gratuláció modal visszavezetés termékekhez

---

## 13. NYITOTT KÉRDÉSEK

- [ ] Pontos kampány indulás dátum — v0.3 beta után (~2026-05-15)?
- [ ] Toborzási csatorna részletek: bolt + QR + személyes? Facebook is?
- [ ] QR kód design és nyomtatás
- [ ] Founding badge pontos vizuális design
- [ ] Counter animáció / progress bar design

---

*Dokumentum generálva: 2026-04-22, Claude (Cowork)*
*Szabolcs + ChatGPT brainstorm, Jira ticketek, és founding50-spec-v1.0.md alapján*
