---
title: "Deák Húsmíves Design System"
description: "Design system documentation for Deák Húsmíves, a Székelyudvarhely butcher shop PWA. Covers typography (Inter and Playfair Display), comprehensive color palette with warm burgundy and cream tones, and spacing standards for developers implementing the brand interface."
description_source: auto
description_hash: b698fcf3d7d04352
version: "2.0"
last_updated: "2026-04-21"
status: "active"
source: "Claude Design + codebase (tailwind.config.js, index.css, Vue components)"
claude_design_url: "https://claude.ai/design/p/de6b98ae-d170-4064-b2f6-e7c0222285b2"
id: 3c01c5ec-de60-482a-94fb-6e2bf27b1546
index_schema_version: 1
---
# Deák Húsmíves -- Design System v2.0

Brand and interface system for **Deák Húsmíves** (deakhus.ro), a local artisan butcher shop based in Székelyudvarhely, Romania (~30,000 population). The product is a **mobile-first PWA** (Vue 3 + Tailwind CSS + Frappe UI) for online ordering and home delivery of meat and prepared foods.

The brand feeling is **warm, earthy, traditional** -- rooted in local craft rather than industrial retail. Burgundi red as the signal color, cream as the ambient background, and a clean card-based UI that never feels sterile.

---

## Források

- **Claude Design projekt:** [Deák Húsmíves Design System](https://claude.ai/design/p/de6b98ae-d170-4064-b2f6-e7c0222285b2)
- **Wireframe gallery:** https://deakhus.netlify.app (Build #29)
- **Live domain:** https://deakhus.ro
- **Codebase:** ExarLabs/deak-butchery (private GitHub repo)
- **Tailwind config:** `frontend/tailwind.config.js` (source of truth for tokens)
- **Global CSS:** `frontend/src/index.css`

---

## 1. Tipográfia

### Font családok

| Család | Típus | Forrás | Használat |
|--------|-------|--------|-----------|
| **Inter / Inter var** | Sans-serif | Self-hosted (`frontend/src/assets/Inter/`, woff2/woff) | Minden UI elem: body, gombok, labelek, számok |
| **Playfair Display** | Serif | Google Fonts import | Brand headings: login screen, hero/section titles, brand name megjelenítés |

Az Inter variable font (`Inter-roman.var.woff2`, `Inter-italic.var.woff2`) a 100-900 weight tartományt fedi le. Statikus woff2/woff fájlok biztosítják a 400/500/600/700/800 weight-eket.

### Playfair Display használata

Kizárólag a `.heading-brand` utility class-szal:
```css
.heading-brand {
  font-family: var(--font-display); /* Playfair Display */
  font-weight: 700;
  letter-spacing: -0.3px;
  color: #7D1A2A; /* primary-800 */
}
```
**Soha nem használjuk** body szövegre vagy UI elemekre.

### Méret skála

Mobile-first méretek. A célcsoport 25-45 éves, digitálisan nyitott helyi vásárlók.

| Szerep | TailwindCSS | Méret | Weight | Line height | Használat |
|--------|-------------|-------|--------|-------------|-----------|
| **Display** | `text-2xl` | 24px | `font-bold` (700) | 32px | Oldal címek |
| **H1** | `text-xl` | 20px | `font-semibold` (600) | 28px | Szekció címek |
| **H2** | `text-lg` | 18px | `font-semibold` (600) | ~21px | Komponens címek, terméknév |
| **Body** | `text-base` | 16px | `font-normal` (400) | 24px | Fő szöveg, leírások |
| **Body strong** | `text-base` | 16px | `font-medium` (500) | 24px | Árak, kiemelések |
| **Small** | `text-sm` | 14px | `font-normal` (400) | 20px | Segédszöveg, timestamps |
| **Caption** | `text-xs` | 12px | `font-medium` (500) | 16px | Badge label, form error |

**Használt weight-ek:** Inter 400 / 500 / 600 / 700 / 800. Playfair 600 / 700 / 800.

Line-height skála: 16 / 20 / 24 / 28 / 32 px -- 4px baseline grid-hez igazítva.

---

## 2. Színpaletta

### Brand színek

| Szerep | HEX | Tailwind token | Leírás |
|--------|-----|----------------|--------|
| **Primary** | `#9B2335` | `primary` | "Butcher Red" -- fő CTA, aktív nav, árak, kiemelések |
| **Primary light** | `#F9E0E3` | `primary-light` / `primary-50` | Hover háttér, out-for-delivery badge |
| **Primary dark** | `#7D1A2A` | `primary-800` | Heading-brand szöveg |
| **Secondary** | `#D4A574` | `secondary` | "Warm Sand" -- kategória badge-ek, ready-for-delivery |
| **Secondary dark** | `#9C7841` | `secondary-dark` | Text-on-light-gold token |

### Háttér színek

| Szerep | HEX | Tailwind token | Leírás |
|--------|-----|----------------|--------|
| **Cream** | `#FFFBF7` | `cream` | App fő háttér -- soha nem pure white |
| **Cream dark** | `#F5EDE5` | `cream-dark` | Finom kontrasztos blokkok |
| **Card** | `#FFFFFF` | `white` | Kártya felszínek |

### Funkcionális színek

| Szerep | HEX | Tailwind token | Light BG | Használat |
|--------|-----|----------------|----------|-----------|
| **Success** | `#2D7A4F` | `success` | `#D4EDDA` | Delivered, savings, pozitív állapotok |
| **Warning** | `#C4841D` | `warning` | `#FEF3C7` | Processing, figyelmeztetések |
| **Error** | `#C4302B` | `error` | -- | Validáció, sikertelen, destruktív |
| **Info** | `#2B6CB0` | `info` | `#DBEAFE` | New order, tájékoztató |

### Szürke skála (Warm Grays)

Meleg szürkék -- enyhe krémszínű tónus, hideg/kékes szürkék helyett.

| Szerep | HEX | Tailwind token | Használat |
|--------|-----|----------------|-----------|
| **Page BG** | `#FAF8F5` | `gray-50` | Alternatív oldal háttér |
| **Border light** | `#E8E2DB` | `gray-200` | Kártya szegélyek, elválasztók |
| **Border strong** | `#C5BCB3` | `gray-300` | Input szegélyek |
| **Text muted** | `#8A8078` | `gray-400` | Másodlagos szöveg, placeholder |
| **Text secondary** | `#5C544C` | `gray-600` | Leírások, segédszövegek |
| **Text primary** | `#2C2825` | `gray-900` | Főszöveg -- majdnem fekete, meleg tónus |

### Tailwind config token-ek (teljes referencia)

```js
// frontend/tailwind.config.js - theme.extend.colors
primary: {
  DEFAULT: '#9B2335',
  50: '#FDF2F4', 100: '#FCE4E8', 200: '#F9CCD3',
  300: '#F4A3AF', 400: '#ED6B80', 500: '#E24360',
  600: '#CF2247', 700: '#AE1B3C', 800: '#7D1A2A',
  900: '#731C30', 950: '#400A14',
  light: '#F9E0E3', pale: '#F4E6E8'
},
secondary: {
  DEFAULT: '#D4A574',
  50: '#FCF8F3', /* ... */ 800: '#6B4D2E', 900: '#5A4027', 950: '#2F2012',
  light: '#F5EDDF', dark: '#9C7841'
},
cream: { DEFAULT: '#FFFBF7', dark: '#F5EDE5' },
success: { DEFAULT: '#2D7A4F', light: '#D4EDDA' },
warning: { DEFAULT: '#C4841D', light: '#FEF3C7' },
info: { DEFAULT: '#2B6CB0', light: '#DBEAFE' },
```

### Szín elvek

- **Ambient cream** mindenhol, ahol nincs kártya -- soha nem pure white page háttér
- **Burgundi piros** takarékosan: CTA-k, aktív nav, ár, szív ikon. Az oldal legyen cream-first
- **Nincs gradient** a UI rétegben -- kizárólag solid színek
- **Nincs pure #000 / #FFF szöveg** -- mindig warm gray

---

## 3. Spacing

### 4px alap egység

Minden spacing értéke 4px többszöröse.

### 3 spacing zóna

| Zóna | Használat | TailwindCSS | Pixel |
|------|-----------|-------------|-------|
| **Tight** | Elemeken belül: ikon-szöveg köz, badge padding, gomb belső tér | `p-1` / `p-1.5` / `p-2` / `gap-1` / `gap-2` | 4-8px |
| **Standard** | Elemek között: kártya szekciók, form mezők, lista itemek | `p-3` / `p-4` / `gap-3` / `gap-4` | 12-16px |
| **Spacious** | Szekciók között: oldal szekciók, header-content köz | `p-6` / `p-8` / `gap-6` / `gap-8` | 24-32px |

### Fix konvenciók (minden oldalra)

| Elem | Spacing | Pixel | Megjegyzés |
|------|---------|-------|------------|
| Oldal szélső padding | `px-4` | 16px | Mindkét oldalon, minden oldalon |
| Kártyák belső padding | `p-4` | 16px | Konzisztens minden kártyánál |
| Kártyák közötti rés | `gap-3` | 12px | Elkülönülnek, de nem esnek szét |
| Form mezők között | `gap-4` | 16px | Jól elkülönülő, nem keverednek össze |
| Szekciók között | `mt-6` / `gap-6` | 24px | Vizuálisan tiszta szekció váltás |
| Bottom nav feletti tér | `pb-20` | 80px | Fix bottom nav ne takarja a tartalmat |
| Bottom nav + CTA feletti tér | `pb-36` | 144px | Fix CTA gomb + bottom nav együtt (pl. product detail) |

### Touch target minimum

**44x44 px** -- nem alkuképes. Bottom nav magassága 65px + iOS safe-area-inset.

---

## 4. Border Radius

Lekerekített, barátságos formák -- illik a meleg, helyi hentes karakterhez.

| Elem | TailwindCSS | Pixel | Használat |
|------|-------------|-------|-----------|
| **Gombok, input** | `rounded-lg` | 8px | Interaktív kis elemek |
| **Kártyák, képek** | `rounded-xl` | 12px | Container elemek |
| **Modal, dialog** | `rounded-2xl` | 16px | Overlay elemek |
| **Badge, tag, pill** | `rounded-full` | 9999px | Pill shape |
| **Bottom navigation** | `rounded-none` | 0px | Szélről szélig |

**Hierarchia:** `rounded-lg` (interaktív) -> `rounded-xl` (container) -> `rounded-2xl` (overlay) -> `rounded-full` (pill)

---

## 5. Árnyékok (Shadows)

Minimális megközelítés -- finom, lágy shadow-ok. A cream háttér és fehér kártyák közötti különbség már önmagában elég kiemelés.

| Szerep | Érték | Használat |
|--------|-------|-----------|
| **Card default** | `0 1px 2px rgba(0,0,0,0.08)` | Kártyák nyugalmi állapotban |
| **Card hover** | `0 3px 12px rgba(155,35,53,0.08)` | Hover tints the shadow brand red-del |
| **Sticky elemek** | `shadow-md` | Bottom nav, sticky header |
| **Bottom nav** | `0 -2px 8px rgba(0,0,0,0.08)` | Fordított irány |
| **Modal** | `shadow-xl` | Felugró réteg, overlay fölé |

**Skála:** Háttér (nincs) -> Kártya (`sm`) -> Aktív/Sticky (`md`) -> Modal (`xl`)

Nincs inner shadow. Nincs extra elevation szint.

---

## 6. Gombok (Buttons)

Frappe UI `<Button>` komponenst használunk.

### 3 típus + disabled

| Típus | Frappe variant | Háttér | Szöveg | Használat |
|-------|----------------|--------|--------|-----------|
| **Primary** | `variant="solid"` | `#9B2335` | `#FFFFFF` | Fő CTA: "Megrendelem", "Hozzáadás" |
| **Secondary** | `variant="outline"` | Átlátszó, `#9B2335` border (2px) | `#9B2335` | Másodlagos: "Vissza", "Szerkesztés" |
| **Danger** | `variant="solid"` + danger | `#C4302B` | `#FFFFFF` | Destruktív: "Törlés", "Rendelés lemondása" |
| **Disabled** | bármely + `:disabled` | `#E8E2DB` | `#8A8078` | Inaktív állapot |

### 2 méret

| Méret | TailwindCSS | Magasság | Használat |
|-------|-------------|----------|-----------|
| **Default** | `h-10 min-h-[40px]` | 40px | Inline gombok, másodlagos akciók |
| **Large** | `h-12 min-h-[48px]` / `h-14` | 48-56px | Fő CTA-k, fix bottom gombok |

### Primary Button (PrimaryButton.vue)

```
w-full h-14 rounded-xl text-base font-semibold
bg-primary hover:bg-primary-800 active:bg-primary-900
```

### Secondary Button (SecondaryButton.vue)

```
w-full h-12 rounded-xl
text-primary border-primary border-2
```

### Fix bottom CTA pattern

A rendelési flow-ban a fő CTA mindig a képernyő alján rögzített:

```
.bottom-action-bar {
  position: fixed;
  bottom: 0;
  left: 0; right: 0;
  padding: 16px;
  padding-bottom: calc(16px + env(safe-area-inset-bottom));
  background: white;
  box-shadow: 0 -2px 8px rgba(0,0,0,0.08);
}
```

A content zónában ilyenkor `pb-36` (144px) -- CTA + bottom nav ne takarja.

---

## 7. Komponensek

### 7.1 StatusBadge

Pill alakú státuszjelző, két méretben.

**Méretek:**
- **sm:** `text-xs px-2.5 py-0.5`
- **md:** `text-sm px-3 py-1`

**6 állapot:**

| Státusz (HU) | Státusz (RO) | Háttér | Szöveg |
|---------------|--------------|--------|--------|
| Új rendelés | Comandă nouă | `#DBEAFE` (info-light) | `#2B6CB0` (info) |
| Folyamatban | În procesare | `#FEF3C7` (warning-light) | `#C4841D` (warning) |
| Kiszállításra kész | Pregătit pentru livrare | `#F5EDDF` (secondary-light) | `#9C7841` (secondary-dark) |
| Szállítás alatt | În curs de livrare | `#F9E0E3` (primary-light) | `#9B2335` (primary) |
| Kiszállítva / Lezárva | Livrat / Închis | `#D4EDDA` (success-light) | `#2D7A4F` (success) |
| Törölve | Anulat | `#EDEAE6` | `gray-600` |

### 7.2 ProductCard

Termék megjelenítő kártya, 2 oszlopos grid.

```
rounded-xl shadow-sm border border-gray-200 bg-white
Kép: aspect-[4/3] bg-gray-200
Body: p-4
Kategória badge: text-xs text-secondary bg-secondary/10 rounded-full
Név: text-lg font-semibold
Ár: text-base font-medium text-primary + "RON"
```

**Nem elérhető állapot:** `bg-gray-900/40` overlay.

### 7.3 OrderCard

Három variáns (customer/admin/courier).

```
Base: rounded-xl shadow-sm border border-gray-200 p-4
Aktív: border-l-[3px] border-l-primary
Lezárt: border-l-[3px] border-l-success
```

### 7.4 QuantitySelector

Két variáns:

| Variáns | Gomb méret | Input méret | Text |
|---------|------------|-------------|------|
| **Full** | `w-12 h-12` | `w-24 h-12` | `text-xl` |
| **Compact** | `w-10 h-10` | `w-16 h-10` | `text-base` |

Mind `rounded-lg border-gray-300`. Focus: `border-primary ring-2 ring-primary/20`. Active: `bg-primary/5 border-primary scale-95`.

### 7.5 NavigationBar (Bottom Tab Bar)

```
position: fixed; bottom: 0;
bg-white, border-t border-gray-200
shadow: 0 -2px 8px rgba(0,0,0,0.08)
pb-[env(safe-area-inset-bottom)]
height: h-16 (64px)
```

**Role-based variánsok:**

| Nézet | Tabok | Ikonok |
|-------|-------|--------|
| **Guest** (3) | Termékek / Kosár / Fiók | home / shopping-cart / user |
| **Customer** (4) | Termékek / Kosár / Rendelések / Fiók | home / shopping-cart / clipboard-list / user |
| **Courier** (2) | Szállítások / Fiók | package / user |
| **Operator** (5) | Áttekintés / Rendelések / Termékek / Szállítások / Fiók | layout-dashboard / clipboard-list / package / truck / user |

**Vizuális:**
- Aktív: `text-primary` (#9B2335), ikon w-6 h-6
- Inaktív: `text-gray-400`
- Cart badge: `absolute -top-1.5 -right-2.5 min-w-[18px] h-[18px] rounded-full bg-primary text-[10px] text-white`

**hideNav:** Checkout flow oldalain (`/checkout/delivery`, `/checkout/confirm`, `/order-success`) elrejtjük a nav-ot. Minden route-on `meta.hideNav` property definiálja.

### 7.6 Form Elements

```css
Input: rounded-lg (12px), border 1px solid #C5BCB3, p-2 px-3, h-12 (48px), text-lg
Focus: border-primary ring-2 ring-primary/20
Error: border-red-600 ring-2 ring-red-600/30
Label: font-medium text-sm, kötelező: * text-primary
```

### 7.7 EmptyState

Ikon (shopping-cart / box / truck): `text-gray-300`, nagy méretű. Főszöveg: `font-semibold text-gray-600`. CTA gomb: `bg-primary text-white rounded-lg px-4 py-3`.

### 7.8 DeliveryDatePicker

Horizontális scroll-ozható nap-választó. Kiválasztott: `bg-primary text-white rounded-full`. Nem elérhető: `text-gray-300`.

### 7.9 TimeSlotSelector

Lista sorok `border rounded-lg px-4 py-3`. Kiválasztott: `border-primary ring-1 ring-primary`. Telt időablak: "Telt" badge, `text-muted`.

---

## 8. Savings Engine (v0.3)

### Küszöbök

- **150 RON** -> ingyenes szállítás (megtakarítás ~10 RON)
- **300 RON** -> + 2% kedvezmény
- 150 alatt: warn nudge. 150-300: green nudge. 300+: gold nudge.

### Progress bar

- Track: 8px magasság, `#E0D8D0`, `border-radius: 4px`
- Fill: gradient `#2E7D32 -> #D4A574`, `border-radius: 4px`, `width` transition 0.5s
- Milestone bubblök: 22x22px körök az 50% és 100% pozíciókban, `border: 2px solid #fff`, `box-shadow: 0 1px 3px rgba(0,0,0,0.15)`
  - Elért: zöld `#2E7D32` + checkmark
  - Nem elért: `#E0D8D0` + `#AAA` label
- Tengelycímkék: `0 RON` / `150 RON` / `300 RON`; alcímkék: `Ingy. szállítás`, `2% kedv.`

### Nudge üzenetek

| Állapot | CSS class | Háttér | Szöveg szín | Copy |
|---------|-----------|--------|-------------|------|
| Küszöb alatt | `.nudge-warn` | `#FFF3E0` | `#E65100` | Adj hozzá termékeket -- 150 RON-tól ingyenes szállítás! |
| Ingyen szállítás elérve | `.nudge-green` | `#E8F5E9` | `#2E7D32` | Ingyenes szállítás! (+ circle-check ikon) |
| Mindkét küszöb | `.nudge-gold` | `linear-gradient(90deg, #E8F5E9, #FFF8E1)` | `#1B5E20` | Teljes kedvezmény! |

Opcionális 12px zöld breakdown sor: `-10 RON megtakarítás (ingyenes szállítás)` / `-16 RON megtakarítás (ingyenes szállítás + 2%)`

### Savings badge (order card-okon)

Zöld kitöltött kör `coins` ikonnal + `-X RON`. Rejtett állapotban `visibility: hidden` (nem `display: none`) -- a kártya ne ugráljon.

### Post-order recap

- 72px zöld success kör, 40px `circle-check`
- `Rendelés leadva ✓` cím + rendelés ID + ETA
- `.savings-big`: 24px / 800 / `#1B5E20` -- nagy savings szám
- Halvány zöld breakdown blokk (`#F6F9F3` bg, `#D4EDDA` border), flex sorok: label bal, zöld `+N RON` jobb
- `Összes megtakarítás` sor: bold, dashed top border-rel elválasztva
- CTA: `Újrarendelés` primary gomb + `rotate-ccw` ikon

### Reorder flow

- **Szokásos rendelésem** CTA: kártya stílus, 40px rounded-rect `primary-light` ikon tile `rotate-ccw`-vel, cím, 12px alcím (tétel szám + utolsó összeg), trailing `chevron-right`
- **Toast:** centered kapszula, 12px radius, zöld `#2D7A4F`, fehér 13px/600, `circle-check` ikon, soft green shadow, 250ms translate-up + fade in
- **Kompakt kosár sorok:** 40px thumbnail, 13px név, 11px meta, pill stepper 26px gombokkal
- **Nem elérhető termék:** `opacity: 0.5`, név `line-through`, `Jelenleg nem elérhető` danger `#C4302B` / 600, stepper `visibility: hidden`

### Bundle kártyák

- 2 oszlopos grid, 10px gap
- Kártya: white, `border-radius: 16px`, `padding: 16px`, 1px `--border`
- Hover: border -> `--primary`, card-hover shadow
- 44px rounded-rect ikon tile `primary-pale` háttérrel, burgundi Lucide ikon
- Név: 16/700; meta: 12/muted; ár: 15/700/primary (pinned bottom `margin-top: auto`)
- **Saving tag:** absolute top-right, `#E8F5E9` bg, `#1B5E20` text, 11/700, 8px radius
- **Threshold badge-ek:** 22px pill chipek a meta alatt: `truck` primary-light (free delivery), `star` gold-light (2% kedv.)

---

## 9. Ikonok (Iconography)

**Lucide SVG, inline, kizárólag.** Nincs icon font, sprite sheet, PNG vagy Unicode helyettesítés.

### Szabályok

- Inline SVG renderelés
- Méretek: **18x18** vagy **20x20 px** UI-ban, 28x28 a savings-coin badge-hez
- Stroke: `stroke-width: 2`, `stroke-linecap: round`, `stroke-linejoin: round`, `fill: none`
- Egyetlen kivétel: kitöltött szív (`fill & stroke: #9B2335`)
- Szín örökli a parent-et -- ikonok soha nem hordozzák a saját color token-jüket

### Gyakori ikonok

`truck`, `circle-check`, `shopping-cart`, `ban`, `package`, `flame`, `pencil`, `lightbulb`, `coins`, `rotate-ccw`, `star`, `heart`, `package-2`, `home`, `clipboard-list`, `user`, `chevron-right`, `layout-dashboard`

### Emoji

**Soha.** Semmilyen felületen. Checkmark-ok és nyilak (Rendelés leadva ✓, Böngéssz ->) **unicode glifák**, nem dekoratív ikonok.

---

## 10. Logo

- **DH monogram** -- burgundi lekerekített négyzet (`#9B2335`) fehér DH jellel
- **Deák Húsmíves** wordmark
- A malac illusztráció **kizárólag print/marketing** -- soha nem jelenik meg a PWA-ban

---

## 11. Tartalom & Szövegezés

### Nyelv

A UI **elsősorban magyar** (Székelyudvarhely magyar közössége). Román másodlagos labelként és jogi szövegekben jelenik meg.

### Hangnem

- **Meleg, közvetlen, praktikus.** Nem corporate, nem aranyos. Mintha egy jó helyi bolt beszélne a törzsvendégéhez.
- **Informális "te" forma** -- `Húzd lejjebb a frissítéshez`, `Böngéssz a termékeink között`, `Menthetjük neked?`
- **Pozitív keretezés:** `Még X RON és leadhatod a rendelést!` -- nem "Minimum rendelési érték nem teljesül"
- **Rövid címek, egysoros magyarázatok.** `Rendelés leadva ✓` fejléc, nyugodt recap alatta
- **Konkrét, nem absztrakt.** `Válassz kényelmes csomagot` > `Fedezd fel csomagjainkat`

### Formázás

- **Sentence case** mindenhol (gombokra, címekre): `Rendeléseim`, `Hozzáadás a meglévőhöz`
- **Nincs ALL CAPS** -- sem title-case marketing header
- Árak: `N RON` szóközzel. Kedvezmény: `-N RON`. Százalék: `2% kedv.`
- Idő/ETA: puha fogalmazás, pl. `a végső ár a mérés alapján változhat`

---

## 12. Animációk & Interakciók

### Elvek

- **Célzott mozgás, soha nem dekoratív**
- Rövid (120-180ms), ease-out, nincs bounce/overshoot
- Oldal átmenetek flatek -- nincs slide-in/out

### Hover / Press

- **Hover:** pale-red tint háttér (`--primary-light`) vagy card shadow vált card-hover-re
- **Press:** nincs shrink/scale-down. Solid gombok sötétebb burgundi, ghost/secondary pale-red fill
- **Disabled:** `#CCC` háttér, default cursor

### Szív animáció (egyetlen dokumentált micro-interaction)

`scale(1) -> 1.2 -> 1`, 140ms ease-out, fill transition egyidejűleg.

### Transparency + blur

Nem használt. Nincs glassmorphism. Modálok flat dark backdrop (`rgba(0,0,0,0.4-0.5)`).

---

## 13. Layout

### Mobile-first szabályok

| Szabály | Érték |
|---------|-------|
| Target szélesség | 375px |
| Max content width | `max-w-md` (448px), `mx-auto` |
| Oldal padding | `px-4` (16px) |
| Content area | `flex-1, overflow-y: auto, padding: 16px` |
| Breakpoint stratégia | Base = mobile, `md:` csak ha szükséges |

### Page struktúra

```
+------------------------+
|  Header (sticky top)   |  h-14, shadow-md, bg-white
+------------------------+
|                        |
|  Content (scroll)      |  px-4, pb-20 (vagy pb-36 ha fix CTA)
|                        |
+------------------------+
|  [Fix CTA gomb]        |  opcionális
+------------------------+
|  Bottom Nav (fixed)    |  h-16, shadow-md, bg-white
+------------------------+
```

### Fix elemek

- **Header:** 56px (h-14), white, 1px bottom border `#E8E2DB`, sticky
- **Bottom nav:** 65px + safe-area-inset, white, top shadow, fixed
- **Modal:** dark backdrop, content centered 12px-radius card

### Képek

- Termékfotók: warm, természetes fény, earth tones -- nincs harsh studio white
- `object-fit: cover` 1:1 vagy 16:9 container-ben
- A kártya lekerekítéséhez illeszkedő felső sarkok

---

## 14. Route struktúra

### Customer (4 tab)

```
Termékek (tab)
+-- Product listing          /products
+-- Product detail           /products/:id

Kosár (tab)
+-- Cart summary             /cart
+-- Delivery form            /checkout/delivery     <- hideNav: true
+-- Order confirmation       /checkout/confirm      <- hideNav: true
+-- Thank you                /order-success         <- hideNav: true

Rendelések (tab)
+-- Order history            /orders
+-- Order detail             /orders/:id

Fiók (tab)
+-- Account / Profile        /account
```

### Courier (2 tab)

```
Szállítások (tab)
+-- Delivery list            /deliveries
+-- Delivery detail          /deliveries/:id

Fiók (tab)
+-- Account                  /account
```

---

## Changelog

| Verzió | Dátum | Változások |
|--------|-------|------------|
| v2.0 | 2026-04-21 | Teljes újraírás: szinkronizálva Claude Design projekttel. Playfair Display hozzáadva. Savings Engine v0.3 komponensek. Magyar UI labels. Cream/secondary token-ek. Wireframe gallery specs (b24). |
| v1.0 | 2026-03-22 | Első verzió a staging showcase alapján |
| v0.5 (old) | 2026-03-11 | design-system-old.md -- spacing zónák, button specs, route struktúra |
