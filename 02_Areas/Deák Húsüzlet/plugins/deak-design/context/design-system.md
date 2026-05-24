# DH Design System
> Forrás: `staging.deakhus.ro` – feltérképezve 2026-03-22, frissítve 2026-04-18 (Kosár screen audit)

---

## 1. Alapok

### Font
```
font-family: InterVar, Inter, system-ui, sans-serif
```

| Szint | Méret | Súly | Line-height | Használat |
|-------|-------|------|-------------|-----------|
| Display | 24px | 700 | 32px | Oldal főcím (`heading-brand text-2xl`) |
| H1 | 20px | 600 | 28px | Szekció cím |
| H2 | 18px | 600 | 20.7px | Komponens cím |
| Body | 14px | 600 | snug | Terméknév kártyában (`text-base font-semibold`) |
| Body SM | 13px | 400–500 | — | Ár/kg, muted count (`text-sm`) |
| Caption | 11px | 400 | — | Progress bar label (`text-[11px]`) |

Letter-spacing H2: `0.18px`

---

## 2. Színpaletta

### Szemantikus színek
| Token | Hex | RGB | Leírás |
|-------|-----|-----|--------|
| `primary` | `#9B2335` | rgb(155, 35, 53) | Fő szín – burgundi vörös |
| `primary-light` | `#F9E0E3` | rgb(249, 224, 227) | Halvány piros háttér |
| `success` | `#2D7A4F` | rgb(45, 122, 79) | Sikeres állapot, „Elérhető" badge |
| `success-light` | `#D4EDDA` | rgb(212, 237, 218) | Halvány zöld háttér |
| `error` | `#C4302B` | rgb(196, 48, 43) | Hiba |
| `warning` | `#C4841D` | rgb(196, 132, 29) | Figyelmeztetés (InfoNotice ikon + border) |
| `warning-light` | `#FEF3C7` | rgb(254, 243, 199) | Halvány sárga háttér |
| `info` | `#2B6CB0` | rgb(43, 108, 176) | Infó |
| `info-light` | `#DBEAFE` | rgb(219, 234, 254) | Halvány kék háttér |
| `secondary` | `#D4A574` | rgb(212, 165, 116) | ⚠️ KORRIGÁLT: Amber arany (kategóriabadge) |
| `orange-700` | `#BD3E0C` | rgb(189, 62, 12) | Progress hint szöveg (`text-orange-700`) |

> ⚠️ **Korábbi dokumentumokban `secondary: #96724A` szerepelt — ez HELYTELEN.**
> Staging-en mért valódi érték: `#D4A574` (amber arany, kategóriabadge-ek háttere).

### Szürke skála
| Token | Hex | Leírás |
|-------|-----|--------|
| `surface-white` | `#FFFFFF` | Kártyák, inputok |
| Background (meleg) | `#FAF8F5` | App fő wrapper háttere |
| `surface-gray-2` | `#F3F3F3` | Disabled gomb háttér |
| `outline-gray-2` | `#E2E2E2` | Kártya border |
| `border-default` | `#E8E2DB` | Általános border (meleg) |
| `border-gray-300` | `#D1D5DB` | Input, stepper gombok border |
| `text-ink` / `text-gray-900` | `#2C2825` | Fő szövegszín |
| `text-muted` / `text-gray-400` | `#8A8078` | Másodlagos szöveg, ár/kg |
| `text-gray-500` | `#999999` | Disabled szöveg, milestone label |
| `bg-gray-200` | `#E0D8D0` | Thumbnail placeholder, progress track |

### Outline token-ek
```
--outline-red-3: #E03636
--outline-green-1: #A6EFC0
--outline-amber-1: #FBDB73
--outline-blue-1: #A7D7FD
--outline-orange-1: #F4B07F
```

---

## 3. Spacing

A projekt **Tailwind CSS**-t használ.

| Class | px | Használat |
|-------|----|-----------|
| `gap-1` | 4px | Ikonok közti |
| `gap-2` | 8px | Elem belső padding |
| `gap-3` | 12px | Elemek közti |
| `gap-4` | 16px | Szekciók közti |
| `p-4` | 16px | Kártya padding |
| `px-4` | 16px | Oldalsó padding |
| `py-3` | 12px | Függőleges padding |
| `pb-40` | 160px | Cart scroll tartalom bottom padding |

---

## 4. Border Radius

| Méret | Érték | Tailwind class | Használat |
|-------|-------|----------------|-----------|
| Full / Pill | 9999px | `rounded-full` | Product detail CTA, chip-ek, progress fill |
| XL | 16px | `rounded-xl` | Kártyák, Cart CTA, info hint pill |
| LG | 12px | `rounded-lg` | Thumbnail, input, stepper, InfoNotice |
| MD | 8px | `rounded` | Kis elemek |

> ⚠️ **Kétféle CTA gomb radius:**
> - **Product detail „Kosárba"**: `rounded-full` (pill, 9999px)
> - **Cart „Tovább a fizetéshez"**: `!rounded-xl` (16px)

---

## 5. Árnyék (Shadow)

| Neve | Érték | Használat |
|------|-------|-----------|
| Card shadow | `shadow-sm` (`0 1px 2px rgba(0,0,0,0.10)`) | Kártyák (CartItem, ProgressBar) |
| Bottom nav | `0 -2px 8px rgba(0,0,0,0.08)` | Alsó navigáció |
| Header | `shadow-md` | Sticky cart header |

---

## 6. Komponensek

### 6.1 StatusBadge
Pill alakú státuszjelző.

```html
<span class="inline-flex items-center rounded-full font-medium whitespace-nowrap text-xs px-2.5 py-0.5
             bg-{color}-light text-{color}">
  Státusz neve
</span>
```

| Státusz (HU) | BG hex | Text hex |
|---------|--------|----------|
| Új rendelés | `#DBEAFE` | `#2B6CB0` |
| Előkészítés alatt | `#FEF3C7` | `#C4841D` |
| Kiszállításra kész | `#F5EDDF` | `#96724A` |
| Úton van | `#F9E0E3` | `#9B2335` |
| Kézbesítve | `#D4EDDA` | `#2D7A4F` |
| Lezárva | `#EDEAE6` | gray-muted |

---

### 6.2 ProductCard
2 oszlopos grid-ben megjelenő termék kártya.

- Container: `rounded-xl border border-[#E8E2DB] shadow-sm bg-white`
- Kép: `aspect-[4/3]` ⚠️ (NEM négyzetes!) — `rounded-lg bg-gray-200 object-cover`
- Kategória badge: `bg-[#D4A574] text-white text-xs rounded-full px-2.5 py-0.5`
- Terméknév: `font-semibold text-sm text-gray-900`
- Ár: `text-primary font-semibold` (pl. `47,00 RON / kg` — vesszős decimális formátum)
- Egység: `text-muted text-sm`

---

### 6.3 QuantitySelector (két variáns)

**Product detail variáns (chip-alapú):**
- Preset chip-ek: `0,5 kg | 1 kg | 2 kg | 3 kg | 5 kg`
- Aktív chip: `border border-primary text-primary rounded-full`
- Inaktív chip: `border border-gray-300 text-gray-600 rounded-full`
- Fine-tune stepper: `−` / értékmező / `+`
- Számítás sor: `0,50 kg × 47,00 RON/kg = 23,50 RON` — `text-sm text-muted text-center`

**Cart variáns (inline stepper):**
- `−`/`+` gomb: `w-10 h-10 min-h-[40px] min-w-[40px] rounded-lg border border-gray-300 text-gray-900 flex items-center justify-center active:bg-primary/5 active:border-primary`
- Érték mező: **INPUT elem** — `w-16 h-10 min-h-[40px] rounded-lg border border-gray-300 text-center text-base font-semibold text-gray-900 bg-white focus:border-primary focus:ring-2 focus:ring-primary/20 outline-none transition-all`

---

### 6.4 AvailabilityBadge ⭐ ÚJ
Termék elérhetőség jelzője (product detail oldal, a kategória badge mellé).

```html
<span class="inline-flex items-center rounded-full font-medium whitespace-nowrap text-xs px-2.5 py-0.5
             bg-success-light text-success">
  Elérhető
</span>
```
- bg: `#D4EDDA`, text: `#2D7A4F`

---

### 6.5 InfoNotice ⭐ ÚJ
Figyelmeztetés box.

```html
<div class="flex items-start gap-2 mt-4 p-3 bg-warning/5 rounded-lg border border-warning/20">
  <!-- circle-info SVG ikon, warning szín -->
  <p>A végső súly és ár ±10%-kal eltérhet</p>
</div>
```
- bg: `rgba(196, 132, 29, 0.05)` (nagyon halvány amber)
- border: `1px solid rgba(196, 132, 29, 0.2)`
- border-radius: 12px (`rounded-lg`)

---

### 6.6 SavingsProgressBar ⭐ ÚJ
Kosárban megjelenő haladásjelző — szállítási és kedvezmény küszöbök.

```html
<div class="bg-white rounded-xl shadow-sm border border-gray-200 p-4">
  <div class="relative h-2 bg-gray-200 rounded-full mb-10">

    <!-- Fill: width inline % -->
    <div class="h-full rounded-full transition-all duration-500"
         style="width: 16.83%; background: #9B2335;"></div>

    <!-- Milestone dot (elért: primary, el nem ért: #E0D8D0) -->
    <div class="absolute top-1/2 w-[22px] h-[22px] rounded-full border-2
                flex items-center justify-center text-white text-xs font-bold shadow-sm z-[2]"
         style="left: 50%; transform: translateY(-50%);">
    </div>

    <!-- RON label -->
    <div class="absolute top-[20px] text-[11px] whitespace-nowrap text-gray-500"
         style="left: 50%;">150 RON</div>

    <!-- Jutalom label -->
    <div class="absolute top-[34px] text-[11px] whitespace-nowrap text-gray-500"
         style="left: 50%;">Ingy. száll.</div>

    <!-- Start label -->
    <div class="absolute top-[20px] left-0 text-[11px] text-gray-500">0 RON</div>
  </div>

  <!-- Hint szöveg -->
  <p class="mt-2 px-3.5 py-2.5 rounded-xl text-[13px] bg-orange-50 text-orange-700">
    Még 99.5 RON → ingyenes szállítás
  </p>
</div>
```

**Küszöbök:** 150 RON = Ingy. száll. | 200 RON = 1% kedv. | 300 RON = 2% kedv.

| Elem | Token |
|------|-------|
| Track | `h-2 bg-gray-200 rounded-full` (8px) |
| Fill | `#9B2335`, `transition-all duration-500` |
| Dot mérete | 22×22px, `border-2`, `shadow-sm` |
| Elért dot | `bg-primary border-primary` |
| El nem ért dot | `#E0D8D0` (bg + border) |
| Label | 11px, `text-gray-500` |
| Hint pill | `bg-orange-50 text-orange-700 rounded-xl`, 13px |

---

### 6.7 CartItemCard ⭐ ÚJ

```html
<div class="bg-white rounded-xl shadow-sm border border-gray-200 p-4 relative transition-opacity duration-200">
  <!-- Thumbnail -->
  <div class="w-20 h-20 rounded-lg overflow-hidden flex-shrink-0 bg-gray-200 cursor-pointer">
    <img class="w-full h-full object-cover" />
  </div>

  <!-- Termék infó -->
  <p class="text-base font-semibold text-gray-900 leading-snug line-clamp-2 flex-1 cursor-pointer">Füstölt Has</p>
  <p class="text-sm font-normal text-gray-400">47,00 RON / kg</p>

  <!-- Delete (jobb felső, absolute) -->
  <button class="w-10 h-10 flex items-center justify-center rounded-lg active:bg-gray-100 transition-colors absolute top-3 right-3">
    <!-- Trash SVG -->
  </button>

  <!-- Inline stepper -->
  <button class="w-10 h-10 min-h-[40px] min-w-[40px] rounded-lg border border-gray-300 flex items-center justify-center active:bg-primary/5 active:border-primary">−</button>
  <input class="w-16 h-10 rounded-lg border border-gray-300 text-center text-base font-semibold bg-white focus:border-primary focus:ring-2 focus:ring-primary/20" value="0,50" />
  <button class="w-10 h-10 min-h-[40px] min-w-[40px] rounded-lg border border-gray-300 flex items-center justify-center active:bg-primary/5 active:border-primary">+</button>

  <!-- Sor összeg -->
  <span class="text-base font-medium text-gray-900 flex-shrink-0 whitespace-nowrap ml-auto">23,50 RON</span>
</div>
```

| Elem | px | Radius |
|------|----|--------|
| Thumbnail | 80×80 | 12px |
| Delete gomb | 40×40 | 12px |
| Qty input | 64×40 | 12px |
| Stepper gomb | 40×40 | 12px |
| Kártya padding | 16px | 16px |

| Szöveg | Osztály | px/súly | Szín |
|--------|---------|---------|------|
| Terméknév | `text-base font-semibold text-gray-900` | 14/600 | `#2C2825` |
| Ár/kg | `text-sm font-normal text-gray-400` | 13/400 | `#8A8078` |
| Sor összeg | `text-base font-medium text-gray-900` | 14/500 | `#2C2825` |

---

### 6.8 CartCTA gomb

| Állapot | Háttér | Szöveg | Radius | Magasság |
|---------|--------|--------|--------|----------|
| Aktív | `#9B2335` | fehér | 16px (`!rounded-xl`) | 56px (`!h-14`) |
| Disabled | `#F3F3F3` | `#999999` | 16px | 56px |

> ⚠️ **Nem pill!** Csak a product detail „Kosárba" gomb pill (`rounded-full`).

---

### 6.9 OrderCard (v0.3 Savings variáns)

- Bal oldali `3px border-l-primary` accent vonal
- Top sor: StatusBadge bal + dátum (`text-muted text-xs`) jobb
- Termék összefoglaló: `text-xs text-muted`
- Ár sor: összeg `font-bold` bal + SavingsBadge jobb (ha saving > 0)
- CTA: `btn-primary` fehér SVG ↻ ikonnal

---

### 6.10 SavingsBadge (Malacpersely)
Csak ha saving > 0 RON.

| Token | Érték |
|-------|-------|
| Háttér | `#2D7A4F` (success) |
| Szöveg | white |
| Méret | 52×44px ovális |
| Összeg font | 11px / 800 |
| Felirat | 8px / opacity 0.85 |

---

### 6.11 EmptyState
- Ikon: `text-gray-300`, nagy méret
- Főszöveg: `font-semibold text-gray-600`
- CTA: `bg-primary text-white rounded-lg px-4 py-3`

---

## 7. Navigáció

### Bottom Tab Bar
```
height: 65px
background: white
border-top: 1px solid #E8E2DB
box-shadow: 0 -2px 8px rgba(0,0,0,0.08)
padding-bottom: env(safe-area-inset-bottom)
```

- **Nem bejelentkezett:** 3 tab — Termékek / Kosár / Fiók
- **Bejelentkezett:** 4 tab — Termékek / Kosár / Rendeléseim / Fiók
- Aktív: `text-primary` + kitöltött ikon
- Kosár badge: piros kör, fehér szám belül

### Cart Header (sticky)
```
height: 56px (h-14)
background: white
box-shadow: shadow-md
position: sticky top-0 z-40
```
- Cím: „Kosaram" — `heading-brand text-2xl`
- Tétel szám: „3 termék" — `text-sm font-medium text-gray-400` (13px, muted)
- Jobb: nyelv toggle (🇭🇺)

---

## 8. Design elvek

1. **Meleg, organikus esztétika** — Háttér: `#FAF8F5`, primary: `#9B2335`.
2. **Mobile-first** — 390px körüli szélességre.
3. **Könnyen tapintható** — Min. 44×44px célterület.
4. **Magyar szöveg** — Vásárlói felület magyar nyelvű.
5. **Tailwind utility-first** — Nincs custom CSS.
6. **InterVar font** — Variable font.

---

## 9. Ikon szabályok

1. **Piros gombon:** fehér ikon (`stroke="white"`)
2. **Fehér/secondary gombon:** piros ikon (`stroke="#9B2335"`)
3. **Emoji TILOS** gombszövegben — mindig SVG
4. **Méret:** 16×16px gombban, 20×20px önálló ikonként

---


## 11. Login Screen (`dhop-*` CSS rendszer)

> ⚠️ A login oldal **NEM Tailwind-alapú** — külön `dhop-*` custom CSS osztályokat használ (Frappe auth page). A vizuális tokenek azonban konzisztensek a fő app-pal.

### Struktúra
```
dhop-auth-page          ← oldal wrapper (bg: #FAF8F5)
  dhop-auth-back        ← vissza link (< Termékek)
  dhop-auth-title       ← "Bejelentkezés" H1
  dhop-auth-card        ← fehér kártya (max-width 448px)
    dhop-social-buttons ← social gombok konténer
    dhop-social-btn     ← Facebook / Google gomb
    dhop-divider        ← "vagy" elválasztó
    dhop-input-group    ← email input wrapper
    dhop-input          ← email mező
    dhop-card-cta       ← CTA terület
    dhop-btn-primary    ← "Folytatás email-lel"
  dhop-below-card       ← kártya alatti terület
    dhop-lang-toggle    ← RO / HU konténer
    dhop-lang-btn       ← egyes nyelv gombok
```

### Design tokenek

| Elem | Osztály | Érték |
|------|---------|-------|
| Oldal háttér | `dhop-auth-page` | `#FAF8F5` — azonos a fő app-pal ✅ |
| Kártya | `dhop-auth-card` | white, radius 12px, padding 24px, max-width 448px |
| Kártya árnyék | — | `rgba(0,0,0,0.06) 0px 1px 2px 0px` (halvány) |
| Cím | `dhop-auth-title` | H1, 24px/700, `#2C2825` |
| Vissza link | `dhop-auth-back` | `rgb(92, 84, 76)` muted, `< Termékek` |
| Social gomb | `dhop-social-btn` | white bg, `1px solid #C5BCB3`, radius 8px, 50px magas |
| Social gomb szöveg | — | 16px/400, `#2C2825`, ikon bal oldalon |
| Divider | `dhop-divider-text` | „vagy", muted szöveg, vízszintes vonalak |
| Email input | `dhop-input` | 50px magas, radius 8px, `1px solid #C5BCB3` |
| Primary gomb | `dhop-btn-primary` | `#9B2335`, white, **radius 8px**, 48px, 16px/600 |
| Aktív lang btn | `dhop-lang-btn` aktív | bg `#E8E2DB`, radius 6px |
| Inaktív lang btn | `dhop-lang-btn` | transparent bg, muted szöveg |

### ⚠️ Gomb radius inconsistency (ismert design drift)
| Oldal | Gomb | Radius |
|-------|------|--------|
| Login | `dhop-btn-primary` | **8px** |
| Product detail | „Kosárba" | **9999px** (pill) |
| Cart | „Tovább a fizetéshez" | **16px** |

Ha egységesíteni kell: a `dhop-btn-primary` radius-t 16px-re kellene frissíteni.

## 10. Auditált screen-ek

| Screen | Dátum | Státusz |
|--------|-------|---------|
| Termékek lista | 2026-04-17 | ✅ Kész |
| Termék detail | 2026-04-17 | ✅ Kész |
| Kosár | 2026-04-18 | ✅ Kész |
| Checkout | — | ⏳ Függő |
| Rendeléseim | — | ⏳ Függő |
| Fiók | — | ⏳ Függő |


---

## 12. Wireframe CSS Token Referencia

> A HTML wireframe fájlok (`design/wireframes/*.html`) **nem Tailwind-alapúak** — saját CSS változókat használnak. A vizuális értékek azonban konzisztensek a staging app-pal.

```css
:root {
  --bg: #F5F0EB;         /* Meleg háttér (staging: #FAF8F5) */
  --card: #FFFFFF;
  --primary: #7B2D3B;    /* Wireframe primary (staging: #9B2335 — kismértékű eltérés) */
  --primary-light: #9B4D5B;
  --primary-pale: #F4E6E8;  /* Halvány primary — kiemelésre, ikon bg-re */
  --text: #2D2D2D;
  --text2: #777777;
  --border: #E8E0D8;
  --green: #2E7D32;       /* = staging success */
  --green-light: #E8F5E9;
  --green-dark: #1B5E20;
  --gold-light: #FFF8E1;
  --warn: #E65100;
  --warn-bg: #FFF3E0;
}
```

> ⚠️ Wireframe primary (`#7B2D3B`) vs staging (`#9B2335`): a staging az authoritativ forrás. Jövőbeli wireframe-ekben a staging értéket kell használni.

---

## 13. Profil Screen komponensek

> Forrás: `v0.3-legal-info-profile.html` (wireframe)

### 13.1 ProfileHero
A Profil tab tetején megjelenő felhasználói kártya.

```html
<div class="profile-hero">
  <!-- bg: --card, border-radius: 16px, padding: 16px, flex, gap: 14px -->
  <div class="avatar">SB</div>
  <div class="profile-info">
    <div class="name">Szabolcs Becze</div>
    <div class="email">user@example.com</div>
  </div>
</div>
```

**Avatar specs:**
- Méret: 52×52px, `border-radius: 50%`
- Háttér: `linear-gradient(135deg, var(--primary), var(--primary-light))`
- Szöveg: fehér, `font-weight: 700`, `font-size: 20px`
- Tartalom: monogram (pl. „SB") vagy profilkép

**ProfileInfo szövegek:**
- `.name`: 15px / 700, `--text`
- `.email`: 12px / 400, `--text2`, `margin-top: 2px`

---

### 13.2 MenuGroup + MenuGroupLabel
Csoportosított navigációs lista (Profil screen szekcióihoz).

```html
<div class="menu-group-label">Fiókom</div>
<!-- 11px, uppercase, letter-spacing: 0.06em, --text2, padding: 0 6px 6px, margin-top: 4px -->

<div class="menu-group">
<!-- bg: --card, border-radius: 16px, border: 1px solid --border, overflow: hidden -->
  <div class="menu-row">
    <div class="menu-icon">
      <!-- 32×32px, border-radius: 8px, bg: --primary-pale, color: --primary -->
      <!-- SVG: 18×18px, stroke-width: 2 -->
    </div>
    <div class="menu-label">Saját adatok</div>
    <!-- 14px / 500 -->
    <span class="menu-chevron">›</span>
    <!-- 18px, --text2 -->
  </div>
</div>
```

**MenuRow állapotok:**

| Állapot | Háttér | Extra |
|---------|--------|-------|
| Alapértelmezett | transparent | `border-bottom: 1px solid --border` |
| Hover | `var(--bg)` | — |
| **Highlighted** (aktív) | `var(--primary-pale)` | `box-shadow: inset 3px 0 0 var(--primary)`; ikon: primary bg + white stroke |
| Danger (kilépés) | transparent | label + ikon: `color: var(--primary)` |

**Jobb oldali értékkijelzés** (pl. Nyelv):
```html
<span style="font-size: 12px; color: var(--text2); font-weight: 500; margin-left: auto; margin-right: 6px;">Magyar</span>
<span class="menu-chevron">›</span>
```

---

### 13.3 SectionHeader
Szekció elválasztó cím (Profil, Jogi infó, dokumentum screeneknél).

```css
.section-header {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--text2);
  padding: 14px 6px 8px;
}
/* Első szekciónál: padding-top: 4px */
```

---

### 13.4 DocRow
Dokumentum link sor (ÁSZF, Adatvédelmi, Cookie).

```html
<div class="doc-row">
<!-- flex, padding: 13px 16px, border-bottom: 1px solid --border, hover bg: --bg -->
  <div class="doc-icon aszf">
  <!-- 36×36px, border-radius: 10px; ÁSZF: bg #E8E0F5 / color #5E3B9C -->
    <svg><!-- 18×18px --></svg>
  </div>
  <div class="doc-info">
    <div class="doc-title">Felhasználási Feltételek (ÁSZF)</div>
    <!-- 14px / 600 -->
    <div class="doc-sub">Utoljára frissítve: 2026.04.17</div>
    <!-- 11px, --text2 -->
  </div>
  <span class="menu-chevron">›</span>
</div>
```

**DocIcon színkombinációk:**

| Dokumentum | BG | Ikon szín |
|------------|-----|-----------|
| ÁSZF | `#E8E0F5` | `#5E3B9C` (lila) |
| Privacy Policy | `#E8F5E9` | `#2E7D32` (zöld) |
| Cookie Policy | `#FFF8E1` | `#8B6914` (arany) |

---

### 13.5 CompanyCard
Jogi entitás adatkártya.

```html
<div class="company-card">
<!-- bg: --card, border-radius: 16px, padding: 16px -->
  <div class="company-name">EXARGROUPS S.R.L.</div>
  <!-- 15px / 700 -->
  <span class="company-role">PLATFORM</span>
  <!-- 10px / 700, bg: --primary-pale, color: --primary, padding: 2px 8px, radius: 6px, letter-spacing: 0.05em -->
  <div class="company-data">
  <!-- 13px, line-height: 1.7 -->
    <div>
      <span class="label">CUI:</span>
      <!-- 11px, --text2, min-width: 70px, display: inline-block -->
      <span class="value">RO41839221</span>
      <!-- font-weight: 500 -->
    </div>
  </div>
</div>
```

**Szerepkör badge értékek:**
- `PLATFORM` — Exar mint üzemeltető
- `ELADÓ · ANSVSA engedély` — Deák mint termékfelelős

---

### 13.6 LangSeg (Nyelvi Szegmentált Vezérlő)

```html
<div class="lang-seg">
<!-- display: flex, bg: --bg, border-radius: 10px, padding: 3px -->
  <button class="active">Magyar</button>
  <button>Română</button>
  <button>English</button>
</div>
```

| Állapot | Háttér | Szöveg | Árnyék |
|---------|--------|--------|--------|
| Aktív | `--card` (white) | `--primary` | `0 1px 3px rgba(0,0,0,0.08)` |
| Inaktív | transparent | `--text2` | — |

Gomb: `flex: 1, border-radius: 8px, font-size: 12px, font-weight: 600`.

---

### 13.7 TocList (Tartalomjegyzék)

```html
<div class="toc-list">
<!-- bg: --card, border-radius: 12px, border: 1px solid --border -->
  <div class="toc-item">
  <!-- display: flex, gap: 10px, padding: 10px 14px, font-size: 13px, border-bottom: 1px solid --border -->
    <span class="toc-num">1.</span>
    <!-- 11px, --primary, font-weight: 700, min-width: 18px -->
    Általános rendelkezések
  </div>
</div>
```

---

### 13.8 ExtRow (Külső Hivatkozás)

```html
<div class="ext-row">
<!-- flex, padding: 13px 16px, hover bg: --bg, border-bottom: 1px solid --border -->
  <div class="ext-icon">
  <!-- 32×32px, border-radius: 8px, bg: --primary-pale, color: --primary -->
    <svg><!-- 16×16px --></svg>
  </div>
  <div class="ext-info">
    <div class="ext-title">ANPC</div>
    <!-- 13px / 600 -->
    <div class="ext-url">anpc.ro ↗</div>
    <!-- 11px, --text2 -->
  </div>
</div>
```

---

### 13.9 AppVersion Footer

```css
.app-version {
  text-align: center;
  padding: 20px 0 10px;
  font-size: 11px;
  color: var(--text2);
}
```
Pl.: `Deák Húsmíves app · v0.4.0 (Build 142)` vagy `Legea 365/2002 · EU 2000/31/EK`

---

## 14. Savings Engine komponensek

> Forrás: `v0.3-wireframes-v3.html` (wireframe)

### 14.1 Nudge (Döntéstámogató Üzenet)
Kosárban megjelenő haladásjelző szöveg — 3 variáns.

```css
.nudge { padding: 10px 14px; border-radius: 12px; font-size: 13px; }
.nudge-warn  { background: var(--warn-bg); color: var(--warn); }
.nudge-green { background: var(--green-light); color: var(--green); }
.nudge-gold  { background: linear-gradient(135deg, var(--green-light), var(--gold-light)); color: var(--green-dark); font-weight: 600; }
```

**Küszöbök és üzenetek:**

| Összeg | Variáns | Üzenet |
|--------|---------|--------|
| 0 RON | — | EmptyState CTA |
| < 150 RON | warn | „Még X RON és leadhatod a rendelést!" |
| 150–299 RON | green | „Ingyenes szállítás!" + breakdown |
| 300+ RON | gold | „Teljes kedvezmény!" + breakdown |

**Breakdown sorok** (nudge alatt):
```html
<div class="breakdown">-10 RON megtakarítás (ingyenes szállítás)</div>
<!-- 12px, color: --green -->
<div class="breakdown-hint">Még 120 RON a 2% kedvezményhez</div>
<!-- 11px, --text2, font-style: italic -->
```

---

### 14.2 BundleCard (Családi Csomag Kártya)

```html
<div class="bundle-grid">
<!-- display: grid, grid-template-columns: 1fr 1fr, gap: 10px -->
  <div class="bundle-card">
  <!-- bg: --card, border-radius: 16px, padding: 16px, border: 1px solid --border, position: relative -->
    <!-- Savings tag: absolute top-right -->
    <div class="bundle-saving">
      <span class="bundle-saving-tag">-10 RON</span>
      <!-- 11px / 700, bg: --green-light, color: --green-dark, radius: 8px, padding: 2px 8px -->
    </div>
    <div class="bundle-name">Családi csomag</div>   <!-- 16px / 700 -->
    <div class="bundle-meta">4 fős, 6 termék</div>  <!-- 12px, --text2 -->
    <div class="bundle-price">~250 RON</div>          <!-- 15px / 700, --primary -->
    <!-- Icon badge-ek: szöveges labelekkel -->
    <div class="icon-badges"><!-- flex, gap: 8px -->
      <div class="icon-badge-item"><!-- flex-col, align-center, gap: 2px -->
        <div class="icon-badge icon-badge-truck">
        <!-- 28×28px, border-radius: 50%, bg: --green-light, color: --green -->
          <!-- truck SVG, 14×14px -->
        </div>
        <span class="ib-label">Ingyenes</span>
        <!-- 8px, --green, font-weight: 600 -->
      </div>
      <!-- Ha >= 300 RON: -->
      <div class="icon-badge-item">
        <div class="icon-badge-pct">
        <!-- 30×30px kör, bg: --gold-light, csillag clip-path dekorációval -->
          <span>2%</span><!-- 9px / 800, --green-dark -->
        </div>
        <span class="ib-label">Kedvezm.</span>
      </div>
    </div>
  </div>
</div>
```

---

### 14.3 EtaCard (Szállítási Időablak)

```html
<div class="eta-card">
<!-- bg: --card, border-radius: 12px, padding: 12px 16px, border: 1px solid --border, flex, gap: 12px -->
  <div><!-- truck SVG, 40×40px, stroke: --primary, stroke-width: 1.5 --></div>
  <div class="eta-text">
    <strong>Szállítás holnap, 14:00–16:00</strong>   <!-- 14px -->
    <span>SMS-ben értesítünk a pontos időről</span>   <!-- 12px, --text2 -->
  </div>
</div>
```

---

### 14.4 Toast (Sikeres Értesítés)

```html
<div class="toast">
<!-- bg: --green, color: white, border-radius: 12px, padding: 12px 16px -->
<!-- font-size: 13px / 600, flex, align-center, justify-center, gap: 8px -->
  <!-- circle-check SVG, 16×16px -->
  Csomag sikeresen mentve!
</div>
```

---

### 14.5 ReturnBanner (Visszatérési Prompt)
Főoldalon, terméklista felett.

```html
<div class="return-banner">
<!-- bg: --card, border-radius: 16px, padding: 14px 16px, border: 1px solid --border -->
<!-- flex, align-items: center, justify-content: space-between -->
  <div>
    <div style="font-size: 12px; color: var(--text2)">Utolsó rendelésed</div>
    <div style="font-size: 14px; font-weight: 600">3 termék · ~110 RON</div>
    <!-- Ha saving > 0: -->
    <div style="font-size: 11px; color: var(--green)">+10 RON megtakarítás</div>
  </div>
  <button class="return-banner-btn">Újrarendelem →</button>
  <!-- padding: 10px 16px, border-radius: 10px, bg: --primary, color: white, 13px / 600 -->
</div>
```

---

### 14.6 Modal (Megerősítő Párbeszédablak)

```html
<div class="modal-overlay">
<!-- bg: rgba(0,0,0,0.4), border-radius: 16px, padding: 20px -->
  <div class="modal-inner">
  <!-- bg: --card, border-radius: 16px, padding: 20px -->
    <h3>A kosaradban már van termék</h3>
    <!-- 16px / 700, margin-bottom: 8px -->
    <p>DEAK-ORD-00042 · ápr. 3 · 3 termék. Mit szeretnél?</p>
    <!-- 13px, --text2, margin-bottom: 16px -->
    <button class="btn btn-primary">Hozzáadás a meglévőhöz</button>
    <button class="btn btn-secondary">Kosár cseréje</button>
    <button class="btn btn-ghost">Mégse</button>
  </div>
</div>
```

**Gomb hierarchia Modal-ban:**
1. `btn-primary` — fő akció
2. `btn-secondary` — alternatíva
3. `btn-ghost` — mégse / cancel (`text-decoration: underline, color: --primary-light`)

---

### 14.7 UnavailableItem (Nem Elérhető Termék)

```html
<div class="cart-item unavailable"><!-- opacity: 0.5 -->
  <div class="cart-item-img">
    <!-- ban SVG, 32×32px, stroke: #CCC — NEM termékkép -->
  </div>
  <div class="cart-item-info">
    <div class="cart-item-name">Füstölt Csülök</div>
    <!-- text-decoration: line-through -->
    <span class="badge badge-warn">Nem elérhető</span>
    <div style="font-size: 11px; color: var(--primary-light); cursor: pointer">Hasonló termékek →</div>
  </div>
</div>
```

---

### 14.8 LoadedMsg (Kosár Betöltve Visszajelzés)

```html
<div class="loaded-msg">
<!-- bg: --green-light, color: --green, padding: 8px 12px, border-radius: 10px -->
<!-- font-size: 12px, text-align: center -->
  Betöltve a DEAK-ORD-00042 rendelésből (ápr. 3)
</div>
```

---

### 14.9 Gomb rendszer (Wireframe változat)

```css
.btn           { width: 100%; padding: 14px 20px; border-radius: 12px; font-size: 15px; font-weight: 600; }
.btn-primary   { background: var(--primary); color: white; border: none; }
.btn-primary:disabled { background: #CCC; cursor: default; }
.btn-secondary { background: transparent; color: var(--primary); border: 2px solid var(--primary); }
.btn-ghost     { background: transparent; color: var(--primary-light); border: none; text-decoration: underline; }
/* Egymás után: .btn + .btn { margin-top: 10px; } */
```

> Wireframe gombradius: `12px` — staging Cart CTA: `16px`. Jövőbeli wireframe-ekben `16px` preferált.

---

### 14.10 OrderSummaryRows (Kosár összesítő)

```html
<!-- Alapsor -->
<div class="total-row"><!-- flex, justify-content: space-between, padding: 4px 0, font-size: standard -->
  <span>Becsült összeg</span><span>~120,00 RON</span>
</div>
<!-- Szállítás — csak ha >= 150 RON: -->
<div class="total-row" style="color: var(--green)">
  <span>Szállítás</span>
  <span><s style="color: var(--text2); margin-right: 4px">10 RON</s> Ingyenes</span>
</div>
<!-- Kedvezmény — csak ha >= 300 RON: -->
<div class="total-row" style="color: var(--green-dark)">
  <span>2% kedvezmény</span><span>-7 RON</span>
</div>
<!-- Összesen: -->
<div class="total-row total-main"><!-- font-size: 16px, font-weight: 700, margin-top: 8px -->
  <span>Összesen</span><span>~113,00 RON</span>
</div>
```
