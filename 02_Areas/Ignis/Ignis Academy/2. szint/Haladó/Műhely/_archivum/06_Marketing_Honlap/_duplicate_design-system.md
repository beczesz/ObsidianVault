---
title: "ANAF SPV Design System — javított, valós minta alapján"
date: 2026-05-12
author: Becze Szabolcs
status: active
description: "Az ANAF SPV webalkalmazás valós design rendszere: sötét-lila indigo alapszín, fehér háttér, modern sans-serif tipográfia. Tartalmazza a pontos hexadecimális színkódokat, nyolc módosított layout-sémát és az összes komponensspecifikációt."
description_source: auto
description_hash: a7d93597afc9bca9
id: 65ddd259-5f8e-4f7c-9543-4541966ca943
index_schema_version: 1
bdos_index: true
---
# ANAF SPV Design System — javított, valós minta alapján

> **Forrás:** [ANAF Spațiu Privat Virtual oldal](https://www.anaf.ro/anaf/internet/ANAF/servicii_online/inregistrare_utilizatori/)
> **Letöltés + screenshot:** 2026-05-12 (Chrome MCP)
> **Verzió:** v2 (a v1-et elvetettük — hibás kék paletta + bal sidebar volt)

---

## 1. Általános vizuális jellemzők (HELYES)

Az ANAF SPV teljesen más mint amit először feltételeztem. A jellemzők:

- **Fehér háttér** dominánsan — kontrasztosan tiszta
- **Sötét-lila / indigo** brand-szín (~#3a3b78) — NEM kék, hanem mélylila
- **Nincs bal oldali sidebar** — helyette **floating bal-jobb oldali kis ikonsor** sticky pozícióban
- **Nagy kép-tile-ok középen** — 4 oszlopos grid, sötét-lila háttér + fehér grafika
- **Lila gombos top-nav** vízszintesen — fehér szöveggel, vékony fehér elválasztással
- **Modern, tiszta layout** — nem 2010-es kormányzati, hanem inkább **2018-2020-as redesign**
- **Modern fontok** — sans-serif, valószínűleg Open Sans vagy hasonló (nem Arial)

---

## 2. Pontos színpaletta

```css
/* Brand */
--anaf-indigo: #3a3b78;           /* Top-nav háttér, gombok */
--anaf-indigo-dark: #2f3068;      /* Hover állapot */
--anaf-indigo-light: #5658a0;     /* Halványabb akcent */
--anaf-indigo-hover-cell: #4a4d8a; /* Hover-en kép-tile alcím */

/* Háttér + szöveg */
--white: #ffffff;
--off-white: #f9f9f9;
--text: #333333;
--text-muted: #666666;

/* Linkek + akcent */
--link: #3a3b78;
--link-hover: #c9302c;     /* sötét piros */
--red-accent: #c9302c;     /* "Depunere declarație" gomb */

/* Bordrur, separator */
--border-light: #e5e5e5;
--border: #cccccc;

/* Egyéb */
--breadcrumb-bg: #3a3b78;
--success-green: #5cb85c;
--warning-yellow: #fffabc;
```

---

## 3. Tipográfia

- **Font-család:** sans-serif modern (Open Sans / Roboto / Lato / Helvetica)
- **Body szöveg:** 14-15px
- **Top-nav gombok:** 13-14px, **bold**, **fehér**
- **H1 (oldal-cím):** 22-24px, **bold**, sötét-lila vagy fehér (kontextustól függő)
- **Breadcrumb:** 12-13px, **bold**, fehér

---

## 4. Layout (HELYES)

### Globális struktúra

```
┌────────────────────────────────────────────────────────────────────┐
│ HEADER (fehér háttér, ~120px)                                        │
│  [ANAF logó pajzs] (bal-közép)        [🔍] [Autent.gombok 2×2] [🇷🇴🇬🇧] │
└────────────────────────────────────────────────────────────────────┘
┌────────────────────────────────────────────────────────────────────┐
│ BREADCRUMB BAR (sötét-lila, ~32px)  ANAF > Servicii Online > ...   │
└────────────────────────────────────────────────────────────────────┘
┌────────────────────────────────────────────────────────────────────┐
│ TOP-NAV (sötét-lila, ~50px)                                          │
│  [Despre ANAF] [Asistență Contribuabili] [Servicii Online] ...      │
└────────────────────────────────────────────────────────────────────┘
┌────────────────────────────────────────────────────────────────────┐
│ SECTION TITLE (sötét-lila, ~50px) — pl. "Inregistrare utilizatori"  │
└────────────────────────────────────────────────────────────────────┘
                                                                      
┌────┬───────────────────────────────────────────────────────────┬──┐
│    │                                                             │  │
│ B  │            MAIN CONTENT (fehér háttér)                       │ J│
│ A  │                                                             │ O│
│ L  │   ┌──────────┬──────────┬──────────┬──────────┐            │ B│
│    │   │  Tile 1  │  Tile 2  │  Tile 3  │  Tile 4  │            │ B│
│ I  │   │ (kép)    │ (kép)    │ (kép)    │ (kép)    │            │  │
│ K  │   │ FEHÉR    │ FEHÉR    │ FEHÉR    │ FEHÉR    │            │ I│
│ O  │   │ CÍM      │ CÍM      │ CÍM      │ CÍM      │            │ K│
│ N  │   └──────────┴──────────┴──────────┴──────────┘            │ O│
│ O  │                                                             │ N│
│ K  │                                                             │ O│
│    │                                                             │ K│
└────┴───────────────────────────────────────────────────────────┴──┘
                                                                      
┌────────────────────────────────────────────────────────────────────┐
│ Lent jobb: chatbot lila kerek gomb ("Ana, asistent virtual")        │
└────────────────────────────────────────────────────────────────────┘
```

### Bal oldali "floating" ikonsor

**Sticky pozíció**, fehér háttér, vízszintes középvonalon:
- 📧 Formular contact
- 👩 Call Center
- 📅 Calendar
- 📊 Strukturált info
- 🖱 Login
- 📡 RSS
- 🇪🇺 GDPR
- 🔗 Share

### Jobb oldali "floating" ikon

**Sticky**, csak 1 ikon: ♿ Accessibility (kerek kék).

### Header — jobb felső gombok

**2×2 grid** sötét-lila gombok:
```
[Autentificare Ro e-Factura ...]  [Autentificare certificat]
[Autentificare utilizator]        [Depunere declarație unica ...] (piros)
```

### Section title bar

Egy önálló sötét-lila csík amiben fehér középre igazított szöveggel kiírják a szekció címét (pl. "Inregistrare utilizatori"). Általában az aktuális oldal teljes szélességű — szélén lekerekített sarkokkal (~4px).

---

## 5. Komponensek (HELYES)

### Top-nav cella

```css
.top-nav-cell {
  background: #3a3b78;
  color: white;
  padding: 12px 18px;
  font-size: 14px;
  font-weight: bold;
  border-right: 2px solid white;  /* vékony fehér separator */
  text-align: center;
  vertical-align: middle;
}

.top-nav-cell:hover {
  background: #4a4d8a;
}

.top-nav-cell.active {
  background: #2f3068;
}
```

### Auth-gomb (jobb felső)

```css
.auth-btn {
  background: #3a3b78;
  color: white;
  padding: 9px 16px;
  font-size: 11px;
  font-weight: bold;
  text-align: center;
  text-transform: none;
  border: 0;
  text-decoration: none;
  display: inline-block;
  line-height: 1.3;
}

.auth-btn.red {
  background: #c9302c;  /* Depunere declarație */
}
```

### Nagy kép-tile

```css
.image-tile {
  width: 250px;
  height: 380px;
  background: #3a3b78;
  position: relative;
  overflow: hidden;
}

.image-tile .tile-title {
  position: absolute;
  top: 30px;
  left: 0;
  right: 0;
  text-align: center;
  color: white;
  font-size: 14px;
  font-weight: bold;
  letter-spacing: 0.5px;
  text-transform: uppercase;
  background: rgba(255,255,255,0.08);  /* halvány keret-fény */
  padding: 12px 8px;
}

.image-tile .tile-image {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 75%;
  background-size: cover;
  background-position: center;
}

.image-tile .tile-hover-desc {
  /* Hover-en megjelenő alcím sáv */
  display: none;
  position: absolute;
  top: 90px;
  left: 0;
  right: 0;
  padding: 16px;
  text-align: center;
  color: white;
  font-size: 13px;
  background: rgba(74, 77, 138, 0.92);
}

.image-tile:hover .tile-hover-desc {
  display: block;
}
```

### Breadcrumb bar

```css
.breadcrumb {
  background: #3a3b78;
  color: white;
  padding: 8px 20px;
  font-size: 13px;
  font-weight: bold;
}

.breadcrumb a {
  color: white;
  text-decoration: none;
}

.breadcrumb .separator {
  margin: 0 8px;
  color: rgba(255,255,255,0.7);
}
```

### Section title bar

```css
.section-title {
  background: #3a3b78;
  color: white;
  padding: 14px 20px;
  font-size: 17px;
  font-weight: bold;
  text-align: center;
  margin: 16px auto;
  max-width: 1100px;
  border-radius: 3px;
}
```

### Floating ikon (bal/jobb)

```css
.floating-icons-left {
  position: fixed;
  left: 12px;
  top: 50%;
  transform: translateY(-50%);
  z-index: 100;
}

.floating-icons-left .icon-item {
  display: block;
  width: 50px;
  text-align: center;
  margin-bottom: 14px;
  font-size: 11px;
  color: #666;
  text-decoration: none;
}

.floating-icons-left .icon-item img {
  width: 36px;
  height: 36px;
  display: block;
  margin: 0 auto 4px;
}
```

### Chatbot gomb

```css
.chatbot-btn {
  position: fixed;
  bottom: 20px;
  right: 80px;
  background: #3a3b78;
  color: white;
  padding: 14px 24px;
  border-radius: 30px;
  font-size: 14px;
  font-weight: bold;
  display: inline-block;
  box-shadow: 0 4px 12px rgba(0,0,0,0.2);
}
```

---

## 6. A TransOffice régi weboldal — adaptáció

A TransOffice „régi" weboldal **NEM lesz kormányzati Lotus-stílus**, hanem **ANAF SPV-stílusú** — vagyis ami az ANAF 2018-2020-as redesignja után kinéz:

- **Fehér háttér mindenhol**
- **Sötét-lila brand** (#3a3b78) — top-nav, breadcrumb, section title, image-tile-ok
- **4 nagy kép-tile**: termék-kategóriáknak (Cartușe, Hârtie, Mobilier, Echipamente IT)
- **Logó pajzs**: stilizált "TO" pajzs sötét-lila háttéren, fehér betűkkel
- **Bal oldali floating ikonsor**: Contact, Call Center, Catalog PDF, RSS, GDPR, Share
- **Jobb felső gombok 2×2 grid**: Comandă rapidă, Catalog PDF, Login client, **piros**: Cerere ofertă
- **Top-nav 9 cella**: Acasă, Despre noi, Produse, Servicii, Parteneri, Cariere, Galerie, Contact, Carte de oaspeți
- **Section title bar**: "Bun venit la TransOffice Trade SRL"
- **Chatbot gomb**: jobb alsó sarokban, "Asistent online"

Ez **realisztikusabb** mint a 2010-es Lotus-stílus — mert egy 2018-2020-as romániai KKV pontosan ilyen layoutot vesz át (gov-stílus, modern, tiszta).
