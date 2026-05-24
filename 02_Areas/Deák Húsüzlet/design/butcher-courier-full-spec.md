---
title: "DH – Mészáros & Futár Interfész — Teljes Spec"
version: 3.0
date: 2026-04-04
author: Claude (Anthropic) + Szabolcs
predecessor: butcher-courier-interface.md (v2.0) + design-handoff.md (v1.0)
description: >
  Összevont dokumentum: a funkcionális spec (korábban butcher-courier-interface.md)
  és a fejlesztői handoff (korábban design-handoff.md) egyetlen referenciává egyesítve.
  Tartalmazza: rendszer áttekintés, szerepkörök, auth, státusz flow, design tokenek,
  komponens specifikációk, screen-by-screen interakciók, animációk, hibaállapotok,
  accessibility, edge case-ek, API, i18n, fájlstruktúra.
id: 9880a9e3-d40a-4937-97b7-50efd14f7d48
index_schema_version: 1
---

# DH – Mészáros & Futár Interfész — Teljes Spec v3.0

_Összevonva: butcher-courier-interface.md (v2.0) + design-handoff.md (v1.0) → egyetlen referencia._

---

# I. RÉSZ — Rendszer áttekintés

## 1. Összefoglaló

Egyetlen bejelentkezéssel elérhető operatív felület a mészáros és a futár számára.
A pilotban ugyanaz a személy tölti be mindkét szerepkört, ezért egy **role-switcher bottom tab bar** váltja a két nézetet — külön bejelentkezés nélkül.

A felület **három fő szekciót** tartalmaz:
1. **Mészáros nézet** (🔪 Előkészítés) – rendelések előkészítése, termékkezelés
2. **Futár nézet** (🚚 Kiszállítás) – kiszállítások kezelése, státuszfrissítések
3. **Statisztika nézet** (📊 Statisztikák) – rendelési adatok havi/heti/napi bontásban

---

## 2. Szerepkörök

| Szerepkör | Helyszín | Eszköz | Fő feladat |
|-----------|----------|--------|------------|
| Mészáros (Butcher) | Üzem / konyha | Tablet | Rendelések előkészítése, státusz frissítés |
| Futár (Courier) | Úton, autóban | Telefon | Kiszállítás navigálása, kézbesítés megerősítése |

**Megjegyzés:** A pilot fázisban a mészáros = futár. Egyetlen felhasználói fiók, `butcher` + `courier` role-lal.

---

## 3. Hozzáférés és auth

- **Route:** `/butcher-courier` (védett route, `butcher` VAGY `courier` role szükséges)
- **Bejelentkezés:** Ugyanaz a login flow mint a vásárlóknál, de role-alapú redirect
- **Session kezelés:** Frappe auth token, localStorage-ben tárolva
- **Nem elérhető:** Admin dashboard (`/admin`) – ez külön, Admin role-hoz kötött

---

## 4. Státusz flow

```
[Vásárló leadja] → Új rendelés
       ↓
[Mészáros indítja] → Előkészítés alatt
       ↓
[Mészáros zárja] → Kiszállításra kész
       ↓
[Futár indítja] → Úton van
       ↓
[Futár zárja] → Kézbesítve
       ↓
[Rendszer/Admin] → Lezárva
```

**StatusBadge megfeleltetés:**

| Magyar | Román (appban) | Badge szín |
|--------|---------------|------------|
| Új rendelés | Comandă nouă | info-light / info |
| Előkészítés alatt | În procesare | warning-light / warning |
| Kiszállításra kész | Pregătit pentru livrare | secondary-light / secondary |
| Úton van | În curs de livrare | primary-light / primary |
| Kézbesítve | Livrat | success-light / success |
| Lezárva | Închis | gray |

---

## 5. Role Switcher (Bottom Tab Bar)

```
[ 🔪 Előkészítés ]  [ 🚚 Kiszállítás ]  [ 📊 Statisztikák ]
```

**Megvalósítás:**
```css
height: 65px
background: white
border-top: 1px solid #E8E2DB
box-shadow: 0 -2px 8px rgba(0,0,0,0.08)
padding-bottom: env(safe-area-inset-bottom)
```

**Aktív tab:** `text-primary` (`#9B2335`), kitöltött ikon
**Inaktív tab:** `text-gray-400`, outline ikon

**Vue implementáció:**
```vue
<script setup>
const activeTab = ref('butcher') // 'butcher' | 'courier' | 'stats'
</script>

<template>
  <div class="flex-1 overflow-hidden">
    <ButcherView v-if="activeTab === 'butcher'" />
    <CourierView v-if="activeTab === 'courier'" />
    <StatsView v-if="activeTab === 'stats'" />
  </div>
  <BottomTabBar v-model="activeTab" :tabs="operatorTabs" />
</template>
```

---

---

# II. RÉSZ — Tech Stack & Design

## 2. Tech Stack

| Réteg | Technológia | Megjegyzés |
|-------|-------------|------------|
| Framework | Vue 3 + Composition API | `<script setup>` szintaxis |
| Styling | Tailwind CSS | Utility-first, design tokenek CSS változókban |
| Font | InterVar (variable font) | CDN: `fonts.bunny.net` vagy bundled |
| Icons | Heroicons v2 | Már telepítve |
| Charts | CSS bar chart (vagy Chart.js fallback) | CSS bar chart egyszerűbb, kevesebb dependency |
| Backend | Frappe REST API | `/api/resource/`, `/api/method/` |
| i18n | vue-i18n v9 | Locale: `ro` (primary), `hu` (fallback) |
| Router | Vue Router 4 | Hash mode |
| State | `ref` / `computed` (lokális) | Nincs Pinia szükséges a pilothoz |

---

## 3. Design Tokenek

Minden token CSS custom property formában érhető el. **Értékek soha ne legyenek hardcode-olva** — mindig token hivatkozást használj.

### Színek
```css
--primary:           #9B2335;   /* Burgundi vörös — CTA, active nav, accent */
--primary-light:     #F9E0E3;   /* Halvány burgundi — badge BG, chart bar inactive */
--success:           #2D7A4F;   /* Zöld — kézbesítve státusz */
--success-light:     #D4EDDA;
--warning:           #C4841D;   /* Sárga-barna — figyelmeztetés, előkészítés badge */
--warning-light:     #FEF3C7;
--info:              #2B6CB0;   /* Kék — új rendelés badge */
--info-light:        #DBEAFE;
--secondary:         #96724A;   /* Meleg barna — kiszállításra kész badge */
--secondary-light:   #F5EDDF;
--error:             #C4302B;   /* Piros — validáció hiba */

--bg-app:            #FAF7F4;   /* App háttér (meleg krém) */
--surface-white:     #FFFFFF;   /* Kártyák, header */
--border-default:    #E8E2DB;   /* Kártyák, elválasztók */
--border-input:      #C5BCB3;   /* Input mezők */
--text-ink:          #2C2825;   /* Fő szöveg */
--text-muted:        #999999;   /* Másodlagos szöveg */
--text-muted-dark:   #6B6560;   /* Közepes szürke */
```

### Tipográfia
```css
/* Font */
font-family: InterVar, Inter, system-ui, sans-serif;

/* Szintek */
Display: 24px / 700 / line-height: 32px    /* Oldal főcím */
H1:      20px / 600 / line-height: 28px    /* Screen header */
H2:      18px / 600 / line-height: 20.7px  /* Kártya cím */
Body:    16px / 400 / line-height: 24px    /* Alap szöveg */
Body SM: 14px / 400 / line-height: 20px   /* Másodlagos */
Caption: 12px / 500 / line-height: 16px   /* Badge, label */
```

### Spacing (Tailwind)
```
gap-1 = 4px   | gap-2 = 8px   | gap-3 = 12px
gap-4 = 16px  | gap-6 = 24px  | gap-8 = 32px
p-4   = 16px  | px-4  = 16px  | py-3  = 12px
px-2.5 py-0.5 = badge padding (10px / 2px)
```

### Border radius
```
rounded-full = 9999px  → Badge, pill toggle
rounded-xl   = 16px    → Kártyák, fő konténerek
rounded-lg   = 12px    → Input mezők, kisebb kártyák
rounded      = 8px     → Gombok, kis elemek
```

### Árnyék
```
Card:        box-shadow: 0 1px 2px rgba(0,0,0,0.10)
Bottom nav:  box-shadow: 0 -2px 8px rgba(0,0,0,0.08)
```

---

## 4. Layout alap

### Képernyőméretek
```
Mobile:  375px szélesség (fő target)
Tablet:  768px (mészáros tablet)
Desktop: nem szükséges (operatív eszköz)
```

### Alaplayout struktúra
```
┌─────────────────────────┐ height: 100dvh
│ Status bar (44px)       │ iOS safe area
│─────────────────────────│
│ Screen header (56px)    │ bg-white, border-bottom
│─────────────────────────│
│                         │
│ Screen content          │ flex-1, overflow-y: auto
│ (scrollozható)          │ padding: 16px
│                         │
│─────────────────────────│
│ Bottom tab bar (65px)   │ bg-white, border-top
│ + safe-area-inset       │ padding-bottom: env(safe-area-inset-bottom)
└─────────────────────────┘
```

### Screen header
```css
height: 56px;
background: white;
padding: 12px 16px;
display: flex;
align-items: center;
gap: 10px;
border-bottom: 1px solid #E8E2DB;

/* Vissza gomb */
.back-btn: font-size: 18px; color: #9B2335; min-tap-target: 44px;

/* Cím */
.title: font-size: 17px; font-weight: 600; flex: 1;

/* Jobb oldali elem (dátum, badge) */
.header-right: margin-left: auto;
```

---

---

# III. RÉSZ — Komponens specifikációk

## 5. Komponens Specifikációk

### 5.1 BottomTabBar
```
Fájl: components/BottomTabBar.vue

CSS:
  height: 65px
  background: white
  border-top: 1px solid #E8E2DB
  box-shadow: 0 -2px 8px rgba(0,0,0,0.08)
  padding-bottom: env(safe-area-inset-bottom)
  display: grid; grid-template-columns: repeat(3, 1fr)

Tab elem:
  display: flex; flex-direction: column; align-items: center
  gap: 2px; padding: 8px 0; min-height: 44px (tap target)

  Aktív:  color: #9B2335; font-weight: 600
  Inaktív: color: #999999; font-weight: 400

  Ikon: font-size: 20px
  Label: font-size: 10px

Props:
  modelValue: 'butcher' | 'courier' | 'stats'
  tabs: Array<{ key, icon, label }>

Emit: update:modelValue

i18n labelek: nav.butcher | nav.courier | nav.stats
```

### 5.2 StatusBadge
```
Fájl: components/StatusBadge.vue

CSS:
  display: inline-flex; align-items: center
  border-radius: 9999px; font-weight: 500
  white-space: nowrap; font-size: 12px
  padding: 2px 10px

Állapot → szín megfeleltetés:
  Comandă nouă          → bg: #DBEAFE  text: #2B6CB0
  În procesare          → bg: #FEF3C7  text: #C4841D
  Pregătit p. livrare   → bg: #F5EDDF  text: #96724A
  În curs de livrare    → bg: #F9E0E3  text: #9B2335
  Livrat                → bg: #D4EDDA  text: #2D7A4F
  Închis                → bg: #EDEAE6  text: #6B6560

Props:
  status: string  (Frappe custom_status értéke)

Accessibility:
  role="status"
  aria-label="{{ t(`status.${statusKey}`) }}"
```

### 5.3 OrderCard (Mészáros variáns)
```
Fájl: components/OrderCard.vue (variant="butcher")

CSS:
  background: white
  border: 1px solid #E8E2DB
  border-left: 3px solid #9B2335   ← bal accent
  border-radius: 16px
  padding: 16px
  box-shadow: 0 1px 2px rgba(0,0,0,0.10)
  cursor: pointer

Tartalom:
  Sor 1: [Rendelésszám — font-semibold 14px] [StatusBadge — jobb]
  Elválasztó: border-bottom 1px solid #E8E2DB, margin: 8px 0
  Sor 2: [Időablak — font-medium 14px]
  Sor 3: [N termék · X RON — text-muted 12px] [› — primary, jobb]

Hover/Active:
  background: #FAF7F4 (--bg-app)
  transition: background 150ms ease

Props:
  order: { id, status, timeSlot, productCount, total }
  variant: 'butcher'

Emit: click
```

### 5.4 OrderCard (Futár variáns)
```
Fájl: components/OrderCard.vue (variant="courier")

CSS: ugyanaz mint mészáros, DE:
  border-left: nincs (3px accent hiányzik)

Tartalom:
  Sor 1: [Vásárló neve — font-semibold 16px] [StatusBadge — jobb]
  Sor 2: [Cím — text-muted 14px]
  Sor 3: [Időablak · N termék — text-muted 12px] [› — primary, jobb]

Props:
  order: { id, customerName, address, timeSlot, productCount, status }
  variant: 'courier'
```

### 5.5 PrimaryButton
```
Fájl: components/PrimaryButton.vue

CSS (default):
  background: #9B2335; color: white
  border-radius: 12px; padding: 14px 20px
  font-size: 16px; font-weight: 600
  width: 100%; display: block
  transition: background 150ms ease, opacity 150ms ease
  min-height: 52px (tap target)

Állapotok:
  Hover:    background: #82192A (10% sötétebb)
  Active:   background: #6E1524, scale: 0.98
  Disabled: background: #E8E2DB, color: #999, cursor: not-allowed
  Loading:  Disabled + spinner ikon balra + label: t('loading.status')

Props:
  label: string
  loading: boolean = false
  disabled: boolean = false
  variant: 'primary' | 'success' | 'secondary'

Variant success: background: #2D7A4F
Variant secondary: background: transparent, border: 1px solid #9B2335, color: #9B2335
```

### 5.6 FilterChips
```
Fájl: components/FilterChips.vue

CSS (inaktív):
  border: 1px solid #E8E2DB
  border-radius: 9999px
  padding: 6px 14px; font-size: 13px; font-weight: 500
  color: #6B6560; background: white
  cursor: pointer

CSS (aktív):
  background: #9B2335; color: white; border-color: #9B2335

Scroll: vízszintes görgetés, gap: 8px, padding: 0 16px
Snap: scroll-snap-type: x mandatory (opcionális)

Props:
  options: Array<{ key, label }>
  modelValue: string (aktív key)
Emit: update:modelValue
```

### 5.7 SummaryStrip
```
Fájl: components/SummaryStrip.vue

CSS:
  background: --secondary-light (#F5EDDF) vagy --primary-light (#F9E0E3)
  padding: 10px 16px; display: flex; gap: 12px; flex-wrap: wrap
  font-size: 13px; border-bottom: 1px solid #E8E2DB

Variáns (mészáros): secondary-light háttér, kg értékek
Variáns (futár): primary-light háttér, kézbesített/úton/kész számlálók
```

### 5.8 ProductToggleRow
```
Fájl: components/ProductToggleRow.vue

CSS (sor):
  display: flex; align-items: center; justify-content: space-between
  padding: 12px 0; border-bottom: 1px solid #E8E2DB

Toggle pill:
  width: 44px; height: 26px; border-radius: 9999px
  transition: background 200ms ease

  ON:  background: #9B2335; knob position: right (translate: 18px)
  OFF: background: #E8E2DB; knob position: left (translate: 2px)

  Knob: 22px × 22px; border-radius: 9999px; background: white
        box-shadow: 0 1px 3px rgba(0,0,0,0.3)
        transition: transform 200ms ease

Kategória fejléc:
  font-size: 12px; font-weight: 700; color: #6B6560
  text-transform: uppercase; letter-spacing: 0.08em
  padding: 12px 0 4px; margin-top: 8px

Optimista UI: toggle azonnal vált, PATCH request háttérben
Hiba esetén: toggle visszaáll, toast error

Props:
  product: { code, name, price, disabled }
Emit: toggle(productCode, newState)
```

### 5.9 EmptyState
```
Fájl: components/EmptyState.vue

CSS:
  display: flex; flex-direction: column; align-items: center
  justify-content: center; padding: 48px 24px; gap: 12px; text-align: center

  Ikon: font-size: 48px; color: #E8E2DB (vagy emoji)
  Cím: font-size: 16px; font-weight: 600; color: #6B6560
  Subtitle: font-size: 14px; color: #999999; max-width: 260px

Props:
  icon: string (emoji vagy heroicon)
  title: string
  subtitle: string (opcionális)
```

### 5.10 StatsSummaryCards
```
Fájl: components/stats/StatsSummaryCards.vue

CSS (grid):
  display: grid
  grid-template-columns: 1fr 1fr
  gap: 8px

Kártya:
  background: white; border: 1px solid #E8E2DB
  border-radius: 16px; padding: 14px
  box-shadow: 0 1px 2px rgba(0,0,0,0.10)

  Label: font-size: 12px; color: #999; margin-bottom: 4px
  Érték: font-size: 24px; font-weight: 700; color: #2C2825
  Egység: font-size: 12px; color: #6B6560

Wide kártya (kg összesen):
  grid-column: 1 / -1   ← teljes szélességű
```

### 5.11 StatsBarChart
```
Fájl: components/stats/StatsBarChart.vue

CSS (konténer):
  background: white; border: 1px solid #E8E2DB
  border-radius: 16px; padding: 14px
  box-shadow: 0 1px 2px rgba(0,0,0,0.10)

Chart terület:
  display: flex; align-items: flex-end
  height: 80px

  Heti nézet: gap: 5px (7 bar)
  Havi nézet: gap: 2px (31 bar)

Oszlop:
  flex: 1; min-width: 0
  display: flex; flex-direction: column; align-items: center
  gap: 4px; justify-content: flex-end

Bar:
  width: 100%; border-radius: 4px 4px 0 0; min-height: 4px
  transition: height 400ms ease-out

  Aktív (mai nap / folyó hét): background: #9B2335
  Inaktív: background: #F9E0E3

Label (heti): font-size: 9px; color: #999
Label (havi): font-size: 7px; color: #999; csak 1, 5, 10, 15, 20, 25, 30, 31

Props:
  data: DailyStats[]
  period: 'weekly' | 'monthly'
  title: string

Animáció: bar magasság 0-ról tölt fel, amikor a komponens mountol
  transition: height 400ms cubic-bezier(0.4, 0, 0.2, 1)
```

### 5.12 PeriodSelector
```
Fájl: components/stats/PeriodSelector.vue

Segmented control CSS:
  display: grid; grid-template-columns: repeat(3, 1fr)
  background: #EDEAE6; border-radius: 10px; padding: 3px
  gap: 2px

Button:
  border-radius: 8px; padding: 7px 0; font-size: 13px; font-weight: 500
  border: none; cursor: pointer; transition: all 150ms ease

  Aktív:  background: white; color: #9B2335; font-weight: 600
          box-shadow: 0 1px 3px rgba(0,0,0,0.15)
  Inaktív: background: transparent; color: #6B6560

Period navigator:
  display: flex; align-items: center; justify-content: space-between
  padding: 10px 0

  Arrow: font-size: 22px; color: #9B2335; min-tap-target: 44px
  Arrow (disabled): color: #999; pointer-events: none
  Label: font-size: 15px; font-weight: 600; color: #2C2825

Props:
  modelValue: 'daily' | 'weekly' | 'monthly'
  currentDate: Date
Emit: update:modelValue, periodChange(from: Date, to: Date)
```

---

---

# IV. RÉSZ — Képernyők

## A. Funkcionális leírás (forrás: interface spec)

### Mészáros nézet

## 6. Mészáros nézet (🔪 Előkészítés)

### 6.1 Képernyő 1 – Napi rendelési lista

**Útvonal:** `/butcher-courier` (alapértelmezett tab)

**Header:**
```
[ Előkészítés ]                    [ 📅 dátum ]
```
- Cím: H1 semibold
- Dátum: `font-medium text-muted`, mai nap (mai nap alapértelmezett)

**Összesítő csík** (ScrollView alatt, fixált):
```
[ 🐷 Friss sertés: 12,5 kg ]  [ 🥩 Füstölt: 8,0 kg ]
[ 🌭 Kolbász: 4,5 kg ]        [ 🥓 Felvágott: 3,0 kg ]
```
- Háttér: `bg-secondary-light` (`#F5EDDF`)
- Egységek: kg, 1 tizedes jegyig
- Adatforrás: az adott nap összes "Előkészítés alatt" + "Kiszállításra kész" rendelés összesítése

**Rendelési lista:**
- OrderCard variáns: "mészáros" (nincs személyes adat, csak rendelésszám + termékek)
- Rendezés: időablak szerint (legkorábbi elöl)
- Szűrők: `Új rendelés` | `Előkészítés alatt` | `Kiszállításra kész` (chip-ek)
- Üres állapot: EmptyState komponens, "Nincs mai rendelés" szöveggel

**OrderCard mészáros variáns:**
```
DH-ORD-XXXX                    [ Státusz badge ]
──────────────────────────────────────────────────
10:00 - 12:00
3 termék · 125,50 RON
                                        [ > ]
```
- Bal oldali accent: `border-l-[3px] border-l-primary`
- Kattintásra: Rendelés előkészítési nézet

---

### 6.2 Képernyő 2 – Rendelés előkészítési nézet

**Header:**
```
[ ← ]   Rendelés #1041             [ státusz badge ]
```

**Termék lista** (személyes adatok NÉLKÜL):
```
┌─────────────────────────────────────────────────┐
│ Érlelő kolbász                           1,0 kg │
│ Sertés comb                              2,0 kg │
│ Tríi szalámi                             0,5 kg │
│                                                  │
│ ⚠️ Figyelem: egyes termék nem elérhető           │
└─────────────────────────────────────────────────┘
```
- Termék sor: `flex justify-between`, termék neve + mennyiség (kg)
- Ha egy termék nem elérhető: sárga warning sáv (`bg-warning-light`)

**Státusz akció gomb:**
```
[ ✓ Kiszállításra kész ]
```
- `bg-primary text-white rounded-xl py-4 font-semibold`
- Csak ha státusz = "Előkészítés alatt"
- Ha státusz = "Kiszállításra kész": gomb disabled/hidden, zöld megerősítés szöveg

**API hívás státuszváltáshoz:**
```js
PUT /api/resource/Sales Order/{id}
{ custom_status: 'Kiszállításra kész' }
```

---

### 6.3 Képernyő 3 – Termék elérhetőség toggle

**Header:**
```
[ ← ]   Termékek
```

**Termék lista kategória szerint:**
```
Friss sertés
  Sertés comb (2,5 kg)              [ ● ]  (ON)
  Pulpă de porc dezosată            [ ○ ]  (OFF)

Füstölt
  Slănină afumată                   [ ● ]  (ON)
  ...
```
- Toggle: `<input type="checkbox">` styled as pill toggle
- Szín: aktív = `bg-primary`, inaktív = `bg-gray-300`
- Mentés: optimista UI, debounced PATCH request
- API:
```js
PATCH /api/resource/Item/{item_code}
{ disabled: 0 | 1 }
```

---

### Futár nézet

## 7. Futár nézet (🚚 Kiszállítás)

### 7.1 Képernyő 4 – Napi kiszállítási lista

**Header:**
```
[ Kiszállítás ]                    [ 📅 dátum ]
```

**Összesítő:**
```
[ ✅ Kézbesítve: 3 ]  [ 🚛 Úton: 1 ]  [ ⏳ Kész: 5 ]
```
- Háttér: `bg-primary-light`

**Kiszállítási lista:**
- OrderCard courier variáns (TimeSlot, vásárló neve, cím)
- Rendezés: időablak → státusz (Úton van elöl)
- Szűrők: `Kiszállításra kész` | `Úton van` | `Kézbesítve`

**OrderCard futár variáns:**
```
Kovács Péter                        [ Státusz badge ]
──────────────────────────────────────────────────
Széchenyi utca 12.
10:00 - 12:00 · 3 produse
                                        [ > ]
```

---

### 7.2 Képernyő 5 – Kiszállítás részletei

**Header:**
```
[ ← ]   Kovács Péter
```

**Adatok:**
```
┌─────────────────────────────────────────────────┐
│ Kovács Péter                                     │
│ +40 742 123 456              [ 📞 Hívás ]        │
│ Széchenyi utca 12., Újvárhely                    │
│                                                   │
│        [ 🗺 Megnyitás Google Maps-ben ]           │
└─────────────────────────────────────────────────┘

Rendelés összesítő:
  3 termék · 125,50 RON
  [ Részletek mutatása ▼ ]  (collapsible)
```

**Státusz gomb:**
```
[ 🚚 Kiszállítás indítása ]   →  státusz: "Úton van"
```
- Ha már "Úton van": gomb = "[ ✓ Kézbesítve ]"

**Telefonos hívás:**
```js
window.location.href = `tel:${order.phone}`
```

**Google Maps:**
```js
const url = `https://www.google.com/maps/dir/?api=1&destination=${encodeURIComponent(order.address)}`
window.open(url, '_blank')
```

---

### 7.3 Képernyő 6 – Kézbesítés megerősítése

**Header:**
```
[ ← ]   Kézbesítés megerősítése
```

**Tartalom:**
```
Kovács Péter
+40 742 123 456

Megerősítési lehetőségek:
  ☑ Személyesen átadva
  ☑ Ajtó elé hagyva (vásárló kérése)

[ Megjegyzés hozzáadása... ]     (textarea, opcionális)

         [ ✓ Kézbesítve – Befejezés ]
```

**API:**
```js
PUT /api/resource/Sales Order/{id}
{
  custom_status: 'Kézbesítve',
  custom_delivery_note: 'megjegyzés...',
  custom_delivered_at: new Date().toISOString()
}
```

---

### Statisztika nézet

## 8. Statisztika nézet (📊 Statisztikák)

### 8.1 Áttekintés

A mészáros/futár számára saját operatív statisztikák: havi/heti/napi bontásban láthatja az összes kiszállított rendelést, mennyiséget és értéket. **Ez nem admin dashboard** — csak az operatív személy saját munkájának visszajelzője.

---

### 8.2 Képernyő 7 – Statisztika főnézet

**Header:**
```
[ Statisztikák ]
```

**Időszak választó (segmented control):**
```
[ Napi | Heti | Havi ]
```
- Aktív: `bg-primary text-white rounded-lg`
- Inaktív: `bg-surface-gray-2 text-muted`
- Alapértelmezett: Heti

**Navigációs sor (időszak lapozó):**
```
[ ← ]   2026. márc. 16 – 22.   [ → ]
```
- Havi: "2026. március"
- Heti: "2026. márc. 16 – 22."
- Napi: "2026. március 22. (vasárnap)"
- `[ → ]` le van tiltva ha a jövőbe mutatna (max: mai hét/hónap/nap)

**Összesítő kártyák:**
```
┌──────────────────┐  ┌──────────────────┐
│  Rendelések      │  │  Bevétel         │
│  23 db           │  │  2.840 RON       │
└──────────────────┘  └──────────────────┘
┌──────────────────────────────────────────┐
│  Kiszállított mennyiség                  │
│  68,5 kg                                 │
└──────────────────────────────────────────┘
```
- Kártyák: `rounded-xl border border-[#E8E2DB] p-4 bg-white shadow-sm`
- Szám: `text-2xl font-bold text-ink`
- Label: `text-sm text-muted`

**Oszlopdiagram** (Havi és Heti nézetben):
- Havi nézetben: X tengely = hét napjai a hónapban (1-31), Y = RON érték
- Heti nézetben: X tengely = 7 nap (H/K/Sz/Cs/P/Sz/V), Y = RON érték
- Napi nézetben: **nincs diagram** (egy nap = egy összesítő)
- Oszlop szín: `bg-primary` (`#9B2335`)
- Aktív/kiválasztott nap/hét: `bg-primary`, többi: `bg-primary-light` (`#F9E0E3`)
- Chart library: `Chart.js` (már használt a projektben) VAGY egyszerű CSS bar chart

**Vue implementáció példa (CSS bar chart):**
```vue
<div class="flex items-end gap-1 h-32">
  <div
    v-for="day in chartData"
    :key="day.label"
    class="flex-1 flex flex-col items-center gap-1"
  >
    <div
      class="w-full rounded-t-sm transition-all"
      :class="day.isToday ? 'bg-primary' : 'bg-primary-light'"
      :style="{ height: `${(day.value / maxValue) * 100}%` }"
    />
    <span class="text-[10px] text-muted">{{ day.label }}</span>
  </div>
</div>
```

---

### 8.3 Képernyő 8 – Rendelés lista (adott időszakban)

A statisztika főnézet alatt, görgetéssel elérhető (nem külön oldal).

**Fejléc:**
```
Rendelések (23)
```

**Lista:**
```
┌─────────────────────────────────────────────────┐
│ DH-ORD-1041            [ Kézbesítve ] badge   │
│ Kovács Péter · 125,50 RON · 3,0 kg             │
│ 2026. márc. 20. · 10:00 – 12:00                │
│                                           [ > ] │
└─────────────────────────────────────────────────┘
```
- OrderCard mini variáns (compact, csak a legfontosabb adatok)
- Kattintásra: Kiszállítás részletei nézet (csak olvasható, ha már Kézbesítve)

---

### 8.4 API — Statisztika adatok

```js
// Rendelések lekérése időszakra
GET /api/resource/Sales Order?
  filters=[
    ["custom_status","in",["Kézbesítve","Kiszállításra kész","Úton van"]],
    ["delivery_date",">=","2026-03-16"],
    ["delivery_date","<=","2026-03-22"]
  ]&
  fields=["name","customer_name","grand_total","custom_total_kg",
          "custom_status","delivery_date","custom_time_slot"]

// Chart adatok (összesített naponta)
// Frappe-ban: Report vagy custom API endpoint
GET /api/method/dhop.api.get_stats_summary?
  from_date=2026-03-16&to_date=2026-03-22
```

**Visszaadott adat struktúra (frontend):**
```ts
interface DailyStats {
  date: string         // "2026-03-20"
  label: string        // "K" (kedd)
  orderCount: number   // 4
  totalRon: number     // 520.00
  totalKg: number      // 15.5
}

interface PeriodSummary {
  totalOrders: number
  totalRon: number
  totalKg: number
  days: DailyStats[]
}
```

---

## B. Interakciós specifikáció (forrás: handoff)

## 6. Képernyők — Interakciós specifikáció

### Screen 1: Napi rendelési lista (Mészáros)
```
Route: /butcher-courier/preparation

Betöltés:
  1. Skeleton loader megjelenik (3 OrderCard skeleton)
  2. GET /api/resource/Sales Order (today, butcher filters)
  3. Skeleton → lista animáció: fade-in 200ms

Szűrő változás:
  Chip kattintás → lista filter (kliens oldalon, nincs új API hívás)

OrderCard kattintás:
  router.push('/butcher-courier/preparation/:orderId')
  Animáció: slide-in jobbról 250ms

Pull-to-refresh:
  Támogasd: @vueuse/core useSwipe vagy natív
  Threshold: 70px lefelé húzás → refresh spinner
  Frissítés után: toast ('Actualizat' / 'Frissítve') ha van változás

Élő frissítés:
  Polling: 30 másodpercenként (pilot fázis, WebSocket helyett)
  Változás esetén: nem ugrik vissza az elejére, csak az adatok frissülnek

Üres állapot:
  EmptyState komponens: 📦 ikon + t('screen1.empty.title') + subtitle
```

### Screen 2: Rendelés előkészítési nézet
```
Route: /butcher-courier/preparation/:orderId

Státusz gomb logika:
  Comandă nouă    → "Începe prepararea"  → PUT custom_status: 'În procesare'
  În procesare    → "Pregătit p. livrare" → PUT custom_status: 'Pregătit...'
  Pregătit...     → gomb hidden, zöld szöveg: t('screen2.status.alreadyReady')
  Livrat+         → gomb hidden, read-only nézet

Státuszváltás flow:
  1. Confirmation dialog megjelenik (13.1 vagy 13.2 a ui-strings.md-ből)
  2. Confirm → gomb: loading state
  3. PUT API hívás
  4. Siker: toast + state frissítés + gomb eltűnik/változik
  5. Hiba: toast error + gomb visszaáll

Warning sáv (termék nem elérhető):
  Ha bármelyik termék disabled=true → sárga sáv a termék neve fölött
  bg: #FEF3C7; border-left: 3px solid #C4841D; border-radius: 8px; padding: 8px 12px
```

### Screen 3: Termék elérhetőség toggle
```
Route: /butcher-courier/preparation/products

Toggle viselkedés:
  1. Kattintás → azonnal vált (optimista UI)
  2. PATCH /api/resource/Item/{code} { disabled: 0|1 }
  3. Siker: toast t('screen3.toast.saved') 2 másodpercre
  4. Hiba: toggle visszaáll + toast error

Kategória fejlécek: sticky pozíció scroll közben (position: sticky, top: 0)

Üres kategória: EmptyState mini variáns (nincs ikon, csak text)
```

### Screen 4: Napi kiszállítási lista (Futár)
```
Route: /butcher-courier/delivery

Rendezés: Úton van → Kiszállításra kész → Kézbesítve
Azonos státuszon belül: időablak szerint (legkorábbi elöl)

Szűrők: kliens oldali, ugyanolyan mint Screen 1

OrderCard kattintás:
  router.push('/butcher-courier/delivery/:orderId')
```

### Screen 5: Kiszállítás részletei
```
Route: /butcher-courier/delivery/:orderId

Hívás gomb:
  window.location.href = `tel:${order.phone}`
  iOS: rendszer telefon app nyílik
  Android: call picker jelenik meg

Google Maps gomb:
  const url = `https://maps.google.com/?q=${encodeURIComponent(address)}`
  window.open(url, '_blank')

Collapsible rendelés részletek:
  Zárt: "Arată detalii ▼" — lista hidden (height: 0, overflow: hidden)
  Nyitott: "Ascunde detalii ▲" — lista látható (height: auto)
  Animáció: max-height transition 250ms ease (nem height: auto)

Kiszállítás indítása gomb:
  Confirmation dialog (13.3 ui-strings.md)
  PUT custom_status: 'În curs de livrare'
  Siker: gomb label → t('screen5.cta.delivered')

Kézbesítve jelölés gomb:
  router.push('/butcher-courier/delivery/:orderId/confirm')
```

### Screen 6: Kézbesítés megerősítése
```
Route: /butcher-courier/delivery/:orderId/confirm

Validáció:
  Checkbox (min. 1 kötelező) — ha egyik sincs kipipálva:
  Gomb inaktív (disabled) + t('screen6.validation.noMethod') megjelenik

Végleges megerősítés:
  1. Confirmation dialog (13.4 ui-strings.md) — "Ez nem vonható vissza"
  2. Confirm → loading state a gombon
  3. PUT: { custom_status: 'Livrat', custom_delivery_note, custom_delivered_at }
  4. Siker: navigálj vissza a listára + toast t('toast.delivery.confirmed')
  5. Hiba: toast error, marad az oldalon

Back gomb viselkedés:
  Ha már visszaigazolva → back letiltva (replace: true navigáció)
```

### Screen 7–9: Statisztika (Heti / Havi)
```
Route: /butcher-courier/stats

Alapértelmezett: Heti nézet, aktuális hét

Period váltás (Napi/Heti/Havi):
  Animáció: kártyák és chart fade-out 150ms → adatok cserélődnek → fade-in 150ms

Period navigáció (← →):
  › disabled ha aktuális hetet/hónapot/napot mutatja (jövőbe nem navigálhat)
  ‹ nincs limit (múltba visszamehet)
  API újrahívás minden navigációnál

API hívás:
  GET /api/method/dhop.api.get_stats_summary?from_date=...&to_date=...
  Skeleton loader: kártyák és chart helyén

Chart animáció:
  Bar-ok 0px magasságról töltődnek fel mountkor és period változáskor
  duration: 400ms, easing: cubic-bezier(0.4, 0, 0.2, 1)

Havi nézet day labels:
  31 nap, csak 1, 5, 10, 15, 20, 25, 30, 31 jelölve
  Betű méret: 7px (nem minden nap fér ki)
```

### Screen 10: Statisztika Napi nézet
```
Napi nézet különbségek:
  - Nincs diagram (info note jelenik meg helyette)
  - Order lista: az adott nap rendelései
  - Period label formátum: "Duminică, 22 mar." / "Vasárnap, márc. 22."
  - API ugyanaz, from_date == to_date
```

---

---

# V. RÉSZ — Technikai implementáció

## 9. Technikai specifikáció

### Stack
- **Framework:** Vue 3 + Composition API
- **Styling:** Tailwind CSS (utility-first, a showcase alapján)
- **Font:** InterVar (CDN vagy bundled)
- **Backend:** Frappe REST API (`/api/resource/`, `/api/method/`)
- **Chart:** Chart.js VAGY CSS bar chart (egyszerűbb)
- **Icons:** Heroicons (már telepítve van)

### Vue Router konfiguráció
```js
{
  path: '/butcher-courier',
  component: ButcherCourierLayout,
  meta: { requiresAuth: true, roles: ['butcher', 'courier'] },
  children: [
    { path: '', redirect: 'preparation' },
    { path: 'preparation', component: ButcherView },
    { path: 'preparation/:orderId', component: OrderPrepView },
    { path: 'preparation/products', component: ProductToggleView },
    { path: 'delivery', component: CourierView },
    { path: 'delivery/:orderId', component: DeliveryDetailView },
    { path: 'delivery/:orderId/confirm', component: DeliveryConfirmView },
    { path: 'stats', component: StatsView },
  ]
}
```

### Scroll viselkedés
```js
// router/index.js
const router = createRouter({
  scrollBehavior(to, from, savedPosition) {
    return savedPosition || { top: 0 }
  }
})
```

### Státusz frissítés minta
```js
// composables/useOrderStatus.js
export function useOrderStatus() {
  const updateStatus = async (orderId, newStatus) => {
    await frappeRequest({
      method: 'PUT',
      url: `/api/resource/Sales Order/${orderId}`,
      body: { custom_status: newStatus }
    })
  }
  return { updateStatus }
}
```

### Szerepkör ellenőrzés
```js
// composables/useAuth.js
const hasRole = (role) => user.value?.roles?.includes(role) ?? false
const isBoth = computed(() => hasRole('butcher') && hasRole('courier'))
```

---

## 7. Animációk összefoglalója

| Elem | Trigger | Animáció | Időtartam | Easing |
|------|---------|----------|-----------|--------|
| Screen megjelenés | router push | slide-in jobbról | 250ms | ease-out |
| Screen eltűnés | router back | slide-out jobbra | 200ms | ease-in |
| Lista betöltés | API success | fade-in | 200ms | ease |
| Bar chart | mount / period change | height 0 → érték | 400ms | cubic-bezier(0.4,0,0.2,1) |
| Toggle pill | kattintás | translate knob | 200ms | ease |
| Bottom tab váltás | tab kattintás | content fade | 150ms | ease |
| Stats period váltás | selector | fade-out + in | 150ms | ease |
| Toast megjelenés | trigger | slide-up + fade | 200ms | spring |
| Toast eltűnés | 2s timeout | fade-out | 150ms | ease |
| Confirmation dialog | CTA kattintás | scale-up + fade-in | 200ms | spring |

---

## 8. Hibaállapotok megjelenítése

### Toast (2 másodpercig látható)
```
Pozíció: bottom: 80px (bottom nav fölött), center
Min szélesség: 200px, max: 320px, padding: 12px 16px
Border radius: 12px; box-shadow: 0 4px 16px rgba(0,0,0,0.15)

Success toast: background: #2D7A4F; color: white; ikon: ✓
Error toast:   background: #C4302B; color: white; ikon: ✕
Info toast:    background: #2B6CB0; color: white; ikon: ℹ

Auto dismiss: 2500ms success, 4000ms error
```

### Inline hiba (lista betöltési hiba)
```
Ha az API nem válaszol:
  Lista helyén megjelenik:
  Ikon: ⚠️ (warning)
  Szöveg: t('error.orders.load')
  Gomb: "Încearcă din nou" / "Újrapróbál" → retry API call
```

### Network banner
```
Ha nincs internet kapcsolat:
  Fixed banner a screen header alatt
  background: #C4302B; color: white; padding: 8px 16px; font-size: 13px
  Szöveg: t('error.network')
  Auto eltűnik ha visszajön a kapcsolat
```

### Session lejárat
```
Ha 401-es válasz érkezik:
  Full-screen overlay (nem navigálható)
  t('error.session.expired')
  "Autentifică-te din nou" gomb → router.push('/login')
```

---

## 9. Üres állapotok megjelenítése

| Screen | Üres állapot trigger | EmptyState icon | Title key | Subtitle key |
|--------|---------------------|-----------------|-----------|--------------|
| Screen 1 | Nincs mai rendelés | 📦 | `screen1.empty.title` | `screen1.empty.subtitle` |
| Screen 1 | Filter aktív, nincs találat | 🔍 | `empty.orders.filtered` | — |
| Screen 4 | Nincs mai kiszállítás | 🚚 | `screen4.empty.title` | `screen4.empty.subtitle` |
| Screen 4 | Filter aktív | 🔍 | `empty.deliveries.filtered` | — |
| Screen 7–10 | Időszakban nincs rendelés | 📊 | `empty.stats.period` | — |

---

---

# VI. RÉSZ — Accessibility & Edge Cases

## 10. Accessibility

### ARIA és Szerepkörök
```
BottomTabBar:  role="tablist"
  Tab elem:    role="tab", aria-selected="true/false"
  Panel:       role="tabpanel", aria-labelledby="{tabId}"

StatusBadge:   role="status", aria-label="{lokalizált státusz neve}"
Toggle pill:   role="switch", aria-checked="true/false",
               aria-label="{t('screen3.toggle.available/unavailable')}"
FilterChip:    role="radio", aria-checked="true/false"
FilterGroup:   role="radiogroup"
PeriodNav ‹:   aria-label="Perioada anterioară" / "Előző időszak"
PeriodNav ›:   aria-label="Perioada curentă" (disabled) / "Perioada următoare"
Dialog:        role="dialog", aria-modal="true", aria-labelledby="{title id}"
```

### Fókusz sorrend
```
Screen 1: FilterChips → OrderCard-ok (top-down) → BottomTabBar
Screen 2: Back gomb → Termékek lista → Akció gomb
Screen 6: Back gomb → Checkbox 1 → Checkbox 2 → Textarea → Confirm gomb
```

### Érintési célterületek
```
Minden interaktív elem: min. 44px × 44px
Bottom tab: 65px magas → megfelelő
OrderCard: teljes kártya koppintható (padding: 16px mindenhol)
Toggle: 44px × 26px + extra invisible hit area (padding: 9px 0)
```

### Kontraszt
```
Primary (#9B2335) fehér háttéren: 7.2:1 ✓ (WCAG AAA)
text-muted (#999) fehér háttéren: 2.8:1 ✗ — csak másodlagos infóhoz
text-muted-dark (#6B6560) fehér: 4.6:1 ✓ (WCAG AA)
text-ink (#2C2825) fehér: 14.5:1 ✓ (WCAG AAA)
```

---

## 11. Edge Case-ek

| Helyzet | Viselkedés |
|---------|-----------|
| Nagyon hosszú vásárló neve (30+ karakter) | Truncate: `text-overflow: ellipsis; overflow: hidden; white-space: nowrap` max-width: calc(100% - 90px) |
| Nagyon hosszú cím | 2 sornyi truncate (`-webkit-line-clamp: 2`) |
| 0 RON összegű rendelés | "0,00 RON" jelenik meg (ne legyen üres) |
| Rendelés módosult miközben az oldalon volt | 409 Conflict → `error.status.conflict` toast + soft reload |
| Havi nézet, hónap csak 28 nap (február) | Chart: 28 bar, labelek 1, 5, 10, 15, 20, 25, 28 |
| Sok rendelés (50+) a listán | Virtuális lista (vue-virtual-scroller) post-MVP; pilotban egyszerű lista elég |
| Román szöveg 15%-kal hosszabb | Gombok: min-height: 52px, width: 100%, ne fix szélesség |
| Offline állapot | Network banner, retry gomb, cached adatok megmaradnak |
| Dupla kattintás a státusz gombra | Debounce 300ms, loading state alatt gomb disabled |

---

---

# VII. RÉSZ — API & i18n

## 12. API Összefoglaló

```js
// === MÉSZÁROS ===

// Rendelések lekérése (ma)
GET /api/resource/Sales Order
  ?filters=[["delivery_date","=","2026-03-22"],
            ["custom_status","!=","Închis"]]
  &fields=["name","custom_status","custom_time_slot",
           "items","grand_total","custom_total_kg"]

// Státuszváltás
PUT /api/resource/Sales Order/{orderId}
  body: { custom_status: "În procesare" | "Pregătit pentru livrare" }

// Termék toggle
PATCH /api/resource/Item/{itemCode}
  body: { disabled: 0 | 1 }

// === FUTÁR ===

// Kiszállítási lista (ma)
GET /api/resource/Sales Order
  ?filters=[["delivery_date","=","today"],
            ["custom_status","in",
             ["Pregătit pentru livrare","În curs de livrare","Livrat"]]]
  &fields=["name","customer_name","shipping_address_name",
           "custom_phone","custom_status","custom_time_slot","items","grand_total"]

// Kézbesítés rögzítése
PUT /api/resource/Sales Order/{orderId}
  body: {
    custom_status: "Livrat",
    custom_delivery_note: "megjegyzés",
    custom_delivered_at: "2026-03-22T10:30:00.000Z"
  }

// === STATISZTIKA ===

GET /api/method/dhop.api.get_stats_summary
  ?from_date=2026-03-16&to_date=2026-03-22

// Response:
{
  totalOrders: 23,
  totalRon: 2840.00,
  totalKg: 68.5,
  days: [
    { date: "2026-03-16", label: "L", orderCount: 3, totalRon: 380, totalKg: 9.5 },
    ...
  ]
}
```

---

## 13. i18n Implementáció

```js
// i18n/index.js
import { createI18n } from 'vue-i18n'

const i18n = createI18n({
  locale: 'ro',         // alapértelmezett
  fallbackLocale: 'hu', // ha ro string hiányzik
  messages: {
    ro: () => import('./locales/ro.json'),
    hu: () => import('./locales/hu.json'),
  }
})

// Dátum formázás
const dateFormatter = new Intl.DateTimeFormat('ro-RO', {
  weekday: 'long', day: 'numeric', month: 'short'
})

// Számformázás
const currencyFormatter = new Intl.NumberFormat('ro-RO', {
  minimumFractionDigits: 2,
  maximumFractionDigits: 2
})
// → "125,50" (NEM pont, hanem vessző!)
```

---

---

# VIII. RÉSZ — Fájlstruktúra & Jira

## 14. Fájlstruktúra

```
src/
├── views/
│   ├── butcher/
│   │   ├── ButcherView.vue          ← Screen 1
│   │   ├── OrderPrepView.vue        ← Screen 2
│   │   └── ProductToggleView.vue    ← Screen 3
│   ├── courier/
│   │   ├── CourierView.vue          ← Screen 4
│   │   ├── DeliveryDetailView.vue   ← Screen 5
│   │   └── DeliveryConfirmView.vue  ← Screen 6
│   └── stats/
│       └── StatsView.vue            ← Screen 7–10 (period alapján)
├── components/
│   ├── BottomTabBar.vue
│   ├── StatusBadge.vue
│   ├── OrderCard.vue                ← variant: 'butcher' | 'courier'
│   ├── PrimaryButton.vue
│   ├── FilterChips.vue
│   ├── SummaryStrip.vue
│   ├── ProductToggleRow.vue
│   ├── EmptyState.vue
│   └── stats/
│       ├── StatsSummaryCards.vue
│       ├── StatsBarChart.vue
│       └── PeriodSelector.vue
├── composables/
│   ├── useOrderStatus.js            ← státuszváltás logika
│   ├── useAuth.js                   ← role check
│   └── useStats.js                  ← stats API + period calc
├── layouts/
│   └── ButcherCourierLayout.vue     ← tab bar + route outlet
├── i18n/
│   ├── index.js
│   └── locales/
│       ├── ro.json                  ← ELSŐDLEGES (minden string itt)
│       └── hu.json                  ← MÁSODLAGOS (fallback)
└── router/
    └── butcherCourier.js            ← route config
```

---

## 11. Jira ticketek

| Ticket | Cím |
|--------|-----|
| DH-52 | Epic 8 – Butcher & Courier Operational Interface |
| DH-53 | Mészáros role hozzáadása az auth rendszerhez |
| DH-54 | Role switcher UI – Mészáros ↔ Futár ↔ Statisztikák váltó |
| DH-55 | Mészáros – napi rendelési lista |
| DH-56 | Mészáros – rendelés előkészítési nézet |
| DH-57 | Mészáros – "Kiszállításra kész" státuszgomb |
| DH-58 | Mészáros – termék elérhetőség toggle |
| DH-59* | Statisztika nézet – PeriodSelector + összesítő kártyák |
| DH-60* | Statisztika nézet – Oszlopdiagram (heti/havi) |
| DH-61* | Statisztika nézet – Rendelési lista időszakra |

*DH-59-61 új ticketek, jóváhagyás után hozzáadandó

---

## 12. Wireframe hivatkozások

- **Wireframe v1** (2026-03-21): `design/wireframes/butcher-courier-wireframe.html`
- **Wireframe v2** (2026-03-22): `design/wireframes/butcher-courier-wireframe-v2.html`
- **Screenshot v2**: `design/wireframes/butcher-courier-wireframe-v2-screenshot.png`

---

## Változásnapló

| Verzió | Dátum | Változás |
|--------|-------|---------|
| 3.0 | 2026-04-04 | Összevonás: butcher-courier-interface.md (v2.0) + design-handoff.md (v1.0) egyetlen dokumentumba |
| 2.0 | 2026-03-22 | Interface spec v2 (korábban butcher-courier-interface.md) |
| 1.0 | 2026-03-22 | Handoff spec v1 (korábban design-handoff.md) |
