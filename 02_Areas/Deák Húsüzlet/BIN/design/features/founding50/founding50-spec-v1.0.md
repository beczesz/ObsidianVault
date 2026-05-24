# Founding 50 Program — Feature Specification

**Jira ticket:** DH-150
**Verzió:** v1.0
**Dátum:** 2026-04-22
**Forrás:** Szabolcs + ChatGPT (Deák GPT) brainstorm session
**Target release:** v0.3 Beta launch (~2026-05-15)

---

## 1. Összefoglaló

A Founding 50 program egy limitált, exkluzív early adopter toborzási kísérlet, amelyben az első 50 regisztrált felhasználó 3 hónapig ingyenes kiszállítást kap. Ez NEM klasszikus marketing kampány, hanem egy kontrollált user cohort kísérlet, amelynek célja:

- Rendszeres rendelési szokás kialakítása (repeat behavior)
- Mérhető adatok gyűjtése (retention, AOV, frequency)
- Közvetlen felhasználói visszajelzés (product iteration)
- Az első aktív, visszatérő user bázis felépítése

---

## 2. Koncepció

### Paraméterek

| Paraméter | Érték | Indoklás |
|-----------|-------|----------|
| Max létszám | **50 fő** | 30k-s kisvárosban reális; elég nagy kohort a méréshez |
| Időtartam | **3 hónap / user** | Rövid, intenzív; elegendő a szokás kialakulásához |
| Jutalom | **Ingyenes szállítás** | Alacsony költség, magas perceived value |
| Soft feltétel | **Havonta min. 2 rendelés** | Nem kommunikált; backend-based retention filter |
| Inaktivitási küszöb | **30 nap rendelés nélkül** | Státusz elvesztése → hely felszabadul |
| Waitlist | **Igen** | Betelt program → várólistára kerül; kiesőt pótolni |

### Design elvek

1. **Ne kommunikálj kötelezettséget** — "aktív tagok" elég
2. **Scarcity kötelező** — counter nélkül nem működik
3. **Ne overengineereld** — gyors launch > tökéletes rendszer
4. **Behavior > feature** — cél: rendelés, nem regisztráció
5. **Egy kampány, egy link, egy cohort** — később jöhetnek újabb hullámok

---

## 3. User Flow

### 3.1 Belépési flow

```
Kampány forrás (QR / Facebook / személyes ajánlás)
  → UTM paraméterrel: ?utm_source=X&utm_campaign=founding50
    → Termékek oldal betöltődik
      → 2-3 sec delay VAGY első scroll után:
        → Kampány modal megjelenik
          → "Csatlakozom most" → Regisztráció oldal
            → Google / Facebook / Email regisztráció
              → Founding member státusz beállítása
                → Vissza termékek oldalra
                  → Gratuláció modal
          → "Talán később" → Modal eltűnik, termékek maradnak
```

### 3.2 Modal megjelenési logika

- **Feltétel:** UTM campaign = "founding50" VAGY direct landing
- **Timing:** 2-3 másodperc delay VAGY első scroll event — amelyik hamarabb
- **Nem jelenik meg ha:** user már regisztrált VAGY program betelt és nincs waitlist
- **Ismétlődés:** Ha "Talán később" → NEM jelenik meg újra ugyanabban a session-ben (sessionStorage flag)

### 3.3 Állapotok

| Állapot | Counter | CTA | Szöveg |
|---------|---------|-----|--------|
| Van hely (< 50 reg.) | "X / 50 hely betelve" | Aktív | Standard |
| Betelt (50/50) | "50 / 50 — Betelt!" | Disabled | "Jelentkezz várólistára" |
| User már tag | — | — | Badge megjelenítés, no modal |
| Lejárt (3 hó után) | — | — | Badge eltűnik, normál szállítási díj |

---

## 4. UI Komponensek

### 4.1 Kampány Modal

**Nyelv: Magyar (elsődleges — Székelyudvarhely)**

**Cím:**
> Legyél az első 50 alapító tag között

**Leírás:**
> Csatlakozz a Deák Húsmíves online rendelési programjához Székelyudvarhelyen, és 3 hónapig ingyenes kiszállítást kapsz. Már csak kevés hely maradt.

**Counter:**
> 🔢 37 / 50 hely betelve (dinamikus)

**CTA gomb:** "Csatlakozom most"
**Secondary action:** "Talán később"

### 4.2 Gratuláció Modal (regisztráció után)

**Cím:**
> Üdv az alapító tagok között!

**Leírás:**
> Gratulálunk! Mostantól 3 hónapig ingyenes kiszállítást kapsz minden rendelésedre Székelyudvarhely területén. Rendelj most és próbáld ki!

**CTA gomb:** "Megnézem a termékeket"
**Kiegészítő info:** "Az ingyenes szállítás [DÁTUM]-ig érvényes."

### 4.3 User Badge — "Alapító tag"

- Megjelenik: Profilban (Contul meu), rendelési felületen, checkout oldalon
- Design: Kis badge/chip "🏅 Alapító tag" szöveggel
- Szállítási díj soron: "Szállítás: ~~15 RON~~ INGYENES (Alapító tag)"

### 4.4 Betelt állapot modal

**Cím:**
> Az alapító program betelt

**Leírás:**
> Sajnos az 50 hely már betelt. Iratkozz fel a várólistára, és értesítünk, ha hely szabadul fel!

**CTA:** "Feliratkozom a várólistára"
**Secondary:** "Rendben, nézem a termékeket"

### 4.5 Román nyelvű verziók

**Kampány modal:**
- Cím: "Fii printre primii 50 de membri fondatori"
- Leírás: "Alătură-te programului de comenzi online Deák Húsmíves din Odorheiu Secuiesc și beneficiezi de livrare gratuită timp de 3 luni. Au mai rămas puține locuri."
- CTA: "Mă înscriu acum"
- Secondary: "Poate mai târziu"

**Gratuláció modal:**
- Cím: "Bun venit în rândul membrilor fondatori!"
- Leírás: "Felicitări! De acum ai livrare gratuită timp de 3 luni pentru toate comenzile tale în Odorheiu Secuiesc. Comandă acum și încearcă!"
- CTA: "Văd produsele"

---

## 5. Adatmodell

### 5.1 User mezők (Frappe DocType kiterjesztés)

| Mező | Típus | Leírás |
|------|-------|--------|
| `founding_member` | Boolean | Aktív founding tag-e |
| `founding_start_date` | Date | Program belépés dátuma |
| `founding_expiry_date` | Date | founding_start_date + 90 nap |
| `founding_campaign` | Link → Campaign | Melyik kampányból jött |
| `founding_waitlist` | Boolean | Várólistán van-e |
| `founding_inactive_date` | Date | Mikor vesztette el a státuszt (ha volt) |

### 5.2 Campaign DocType (új)

| Mező | Típus | Leírás |
|------|-------|--------|
| `name` | Data | Kampány azonosító (pl. "founding50-wave1") |
| `title` | Data | Megjelenítendő név |
| `max_members` | Int | Maximum létszám (50) |
| `current_members` | Int (computed) | Jelenlegi aktív tagok |
| `benefit_type` | Select | "free_delivery" / "percentage_discount" / "fixed_discount" |
| `benefit_duration_days` | Int | Jutalom időtartama (90) |
| `status` | Select | "active" / "full" / "closed" |
| `utm_campaign` | Data | UTM campaign paraméter |
| `start_date` | Date | Kampány indulás |
| `end_date` | Date | Kampány lezárás (opcionális) |

### 5.3 Delivery fee logika (pseudo-code)

```python
def get_delivery_fee(user, order):
    if user.founding_member:
        if frappe.utils.today() <= user.founding_expiry_date:
            return 0  # Ingyenes szállítás
    return STANDARD_DELIVERY_FEE  # 15 RON
```

### 5.4 Inaktivitási logika (scheduled job, napi)

```python
def check_founding_inactivity():
    """Napi job: 30 napja nem rendelt founding member → kiesik"""
    threshold = frappe.utils.add_days(frappe.utils.today(), -30)
    inactive = frappe.get_all("User", filters={
        "founding_member": 1,
        "last_order_date": ["<", threshold]
    })
    for user in inactive:
        frappe.db.set_value("User", user.name, {
            "founding_member": 0,
            "founding_inactive_date": frappe.utils.today()
        })
        # Waitlist-ről pótlás (v2-ben automatikus, MVP-ben manuális)
```

---

## 6. Kampány forrás tracking (UTM)

### 6.1 UTM paraméterek

| Forrás | URL minta |
|--------|-----------|
| Bolt QR kód | `deakhus.ro?utm_source=qr_store&utm_campaign=founding50` |
| Facebook post | `deakhus.ro?utm_source=facebook&utm_campaign=founding50` |
| Személyes ajánlás | `deakhus.ro?utm_source=referral&utm_campaign=founding50` |
| Szórólap | `deakhus.ro?utm_source=flyer&utm_campaign=founding50` |

### 6.2 Frontend UTM kezelés

- URL-ből kinyert UTM paraméterek → sessionStorage-ba mentés
- Regisztrációkor → user record-ba mentés (acquisition_source, acquisition_campaign)
- Firebase Analytics event: `founding50_modal_shown`, `founding50_cta_clicked`, `founding50_registered`

---

## 7. KPI-k és mérés

### 7.1 Program szintű KPI-k

| KPI | Cél | Mérés módja |
|-----|-----|-------------|
| Regisztráció → első rendelés (TTFO) | ≤ 72 óra | founding_start_date vs first_order_date |
| Second order rate (14 napon belül) | ≥ 40% | Frappe query |
| Orders / user / hónap | ≥ 2 | Átlag számítás |
| Retention (30 nap) | ≥ 60% | Aktív tagok / összes tag |
| AOV (average order value) | ≥ 80 RON (min. kosár) | Átlag rendelésérték |
| Inaktivitás miatti kiesés | ≤ 20% | Kiesett tagok / összes |

### 7.2 Firebase Analytics események

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

## 8. Budget becslés

### Szállítási költség kalkuláció

| Paraméter | Érték |
|-----------|-------|
| Founding tagok | 50 fő |
| Időtartam | 3 hónap |
| Várható rendelés/fő/hó | 2 |
| Összes rendelés | 50 × 3 × 2 = **300 rendelés** |
| Szállítási díj / rendelés | ~15 RON |
| **Teljes szállítási költség** | **~4.500 RON (~900 EUR)** |

Ez a stop cap (~12-13k EUR) részeként kezelhető. A tényleges költség alacsonyabb lehet ha:
- Nem mindenki rendel 2×/hó
- Kiesők hamarabb elhagyják a programot
- A szállítási költség amúgy is kalkulált az árakban

---

## 9. Implementációs terv (sub-ticketek)

### Phase 1 — MVP (Sprint 3 / Beta launch)

| Sub-ticket | Típus | Leírás | Effort |
|-----------|-------|--------|--------|
| **Backend: Campaign DocType + User mezők** | Task | Új Campaign DocType, User model kiterjesztés, delivery fee override | M |
| **Backend: Inaktivitási scheduler** | Task | Napi job: 30 napos inaktivitás check, státusz elvétel | S |
| **Frontend: Kampány modal** | Story | Modal UI (szövegek, counter, CTA), megjelenési logika (delay/scroll), UTM detection | M |
| **Frontend: Gratuláció modal + badge** | Story | Sikeres regisztráció utáni modal, "Alapító tag" badge, checkout szállítási díj override UI | S |
| **Frontend: Betelt állapot + waitlist** | Story | Betelt state UI, waitlist regisztráció | S |
| **Analytics: Firebase events** | Task | 8 founding50 event bekötése | S |
| **QR / UTM: Kampány linkek generálása** | Task | 4 UTM link + QR kódok nyomtatásra | XS |

### Phase 2 — Post-MVP (v0.3.1+)
- Automatikus waitlist pótlás
- Founding 50 #2 wave indítás
- Push notification a lejárat előtt
- Részletes kohort riport

---

## 10. Kockázatok

| Kockázat | Valószínűség | Hatás | Mitigáció |
|----------|-------------|-------|-----------|
| Kevesebb mint 50 regisztráció | Közepes | Program nem tölti be célját | Aktívabb toborzás, deadline kitolás |
| Magas churn (>40%) | Közepes | ROI csökken | Inaktivitási filter már benne van |
| Szállítási kapacitás nem bírja | Alacsony | Fulfillment probléma | Max 300 rendelés / 3 hó = ~25/hét — kezelhető |
| Tech debt a kampány rendszerben | Közepes | Bonyolultabb lesz scale-elni | MVP minimális, Phase 2-ben refaktor |

---

*Dokumentum készítette: Claude (Cowork) + ChatGPT (Deák GPT) szintézis*
*Szabolcs eredeti ötlete és döntései alapján*
