---
title: "Impeccable Prompt — Falusi Route Képernyők Tervezése"
date: 2026-05-02
author: Becze Szabolcs
status: active
description: "Falusi szállítás képernyőinek tervezési promptja a Deák Húsmíves PWA-hoz, amely hat mobilképernyőt definiál: település-választó, route info banner, checkout, kosár, rendelés-visszaigazolás és futári lista. Fejlesztőknek és designereknek hasznos referencia a specifikációk és design szabályok összefoglalásával."
description_source: auto
description_hash: ecd99dad93f18210
id: 859b4d7a-8475-4efe-98e3-025e061868f4
index_schema_version: 1
bdos_index: true
---
# Impeccable Prompt — Falusi Route Képernyők Tervezése

> **Másold be ezt a promptot egy friss Claude Code session-be.**

---

## Prompt

Falusi házhozszállítás (rural delivery) képernyőket kell tervezni a Deák Húsmíves PWA-hoz. Ez egy fix napos, előrendeléses modell: a falvakba csütörtökön szállítunk, rendelési határidő szerda 20:00.

### 1. Kontextus betöltése — olvasd be SORRENDBEN:

1. `design/PRODUCT.md` — brand, userek, anti-referenciák
2. `design/DESIGN.md` — design tokenek, tipográfia, komponensek
3. `Business Development/pilot-husuzlet/rural-delivery/rural-route-spec-v1.0.md` — **EZ A FŐ DOKUMENTUM** — a **4A szekció** tartalmazza az összes funkcionális flow-t (F1–F13) részletesen
4. `design/screen-catalog/screens/v0.3-cart.html` — referencia a meglévő kosár designhoz (ezt kell adaptálni)
5. `design/screen-catalog/screens/v0.3-post-order-recap.html` — referencia a meglévő rendelés visszaigazoláshoz

### 2. Meglévő design rendszer szabályok:

- Mobile-first: 375px széles, max 448px content
- Primary: #9B2335 (burgundi), Cream BG: #FFFBF7
- Font: Inter (body) + Playfair Display (display headings)
- Ikonok: Lucide SVG
- Kártyák: border #E8E2DB, border-radius: 12px, shadow: subtle
- Bottom nav: 56px magas, 4 tab (Termékek, Kosár, Rendeléseim, Profil)
- Back button: `<a href="../index.html" class="back-to-catalog">`
- Screen meta blokk kötelező minden HTML-ben

### 3. Tervezendő képernyők (6 screen, prioritás sorrendben):

#### P0 — Ezek kellenek elsőként:

**Screen 1: Settlement Picker (Település-választó bottom sheet)**
- Spec: F1.1 és F1.2 a rural-route-spec 4A szekcióban
- Bottom sheet (nem új oldal), keresőmező felül
- Két csoport: 🏙️ Város (Udvarhely) + 🏡 Falvak (14 település, csütörtöki route)
- "Nem találom a településem" link alul
- Állapotok: üres (első belépés) + kitöltött (módosítás)

**Screen 2: Route Info Banner (komponens — 4 állapot)**
- Spec: F2.1–F2.3
- Ezt komponensként tervezd meg, nem teljes oldalként
- 4 variáció egy screen-en: Aktív-nyitott (zöld), Aktív-sürgős (narancs), Zárt (szürke), Nem indul (piros)
- Visszaszámláló: "Még 2 nap 4 óra" formátum

**Screen 3: Checkout — Falusi szállítás**
- Spec: F5.1–F5.3
- A meglévő checkout layout adaptálása falusi rendelésre
- 6 blokk: Szállítási adatok + Átadási pont + Összesítő + Fizetés + Megjegyzés + CTA
- Threshold nudge: "Még X RON és ingyenes a szállítás!"
- Ambassador javaslat az átadási pontnál

**Screen 4: Kosár — Falusi adaptáció**
- Spec: F4.1–F4.2
- A meglévő v0.3-cart.html ALAPJÁN — kiegészítve:
  - Route info banner (kompakt, 1 soros) a tetején
  - Szállítási info blokk (település + nap + ablak)
  - Threshold nudge 120 RON-hoz (nem 150!)
  - Cutoff utáni állapot: "Rendelés a következő csütörtökre →" gombszöveg

#### P1 — Második kör:

**Screen 5: Rendelés visszaigazolás — Falusi**
- Spec: F6
- Sikeres rendelés utáni képernyő
- Route-specifikus: szállítási nap, ablak, település, átadási pont
- "A sofőr hív, mielőtt odaér" info

**Screen 6: Futár — Route kiszállítási lista**
- Spec: F9.2
- Települések route-sorrendben (nem ABC!)
- Minden csomagnál: név + cím + összeg + telefon + "Kézbesítve" gomb
- Haladás-sáv alul

### 4. NE tervezd meg most (későbbi kör):

- Admin: Zone kezelés (S6) — admin felület, nem user-facing
- Admin: Route összesítő (S7) — admin felület
- Route nem indul értesítés (S5/F8) — Phase 2 feature
- Mészáros: Előkészítés settlement-csoportosítás (F9.1) — admin felület

### 5. Fájl elnevezés:

Minden screen: `design/screen-catalog/screens/v0.4-[név].html`

- `v0.4-settlement-picker.html`
- `v0.4-route-banner.html`
- `v0.4-checkout-rural.html`
- `v0.4-cart-rural.html`
- `v0.4-order-confirm-rural.html`
- `v0.4-courier-route.html`

### 6. Fontos kontextus:

- A user "falusi" — nem tech-savvy, de nem is idős. 25-45 éves, családos.
- A "település" szó ismerős nekik, NEM "settlement" vagy "zone"
- Magyar nyelvű UI (a spec-ben minden szöveg magyarul van)
- Pilot alatt NINCS minimum rendelésszám — ha valaki rendel, indul a route
- Szállítási díj: 15 RON (120 RON felett ingyenes)
- Fizetés: csak készpénz átvételkor

---

_Generálva: 2026-05-02 | Forrás: rural-route-spec v1.2 + app-flow-v0.3_
