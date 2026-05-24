---
title: "DH App Flow Map — Funkcionalitás Snapshot"
version: "0.3"
date: "2026-05-02"
author: Claude (Anthropic)
sprint: Sprint 3 (v0.3 — "A spórolás motora")
description: >
  A Deák Húsmíves PWA teljes funkcionalitásának dokumentációja.
  Snapshot verzió — minden velocity tracker frissítésnél és ticket-változásnál aktualizálandó.
  A verzió az app valódi verzióját tükrözi (jelenleg v0.3).
id: 01da8fd4-f74e-438a-a3c7-98ad9b3499b2
index_schema_version: 1
---

# DH App Flow Map v0.3

_Utolsó frissítés: 2026-05-02 | Sprint 3 aktív (70%) | Build #68_

---

## 1. Rendszer áttekintés

### Tech stack

| Réteg | Technológia |
|-------|-------------|
| Frontend | Vue 3 + Composition API (`<script setup>`) |
| Styling | Tailwind CSS (utility-first) |
| UI library | Frappe UI |
| Backend | Frappe Framework (Python) REST API |
| Hosting | deakhus.ro (production), staging.deakhus.ro |
| Analytics | Firebase Analytics (SDK bekötve, DH-104 Done) |
| Auth | Frappe auth token (localStorage) |
| PWA | Installálható, mobile-first (375px target, max 448px content) |

### Architektúra

```
Vásárló (PWA) ──→ Frappe REST API ──→ MariaDB
                      ↑
Mészáros/Futár ───────┘   (ugyanaz az API, role-alapú hozzáférés)
```

### Design tokenek (gyors referencia)

| Token | Érték | Használat |
|-------|-------|-----------|
| Primary | #9B2335 (Burgundi vörös) | CTA, aktív nav, accent |
| Cream BG | #FFFBF7 / #FAF7F4 | App háttér |
| Font | Inter (body) + Playfair Display (display) | Tipográfia |
| Icons | Lucide SVG | Ikonok |
| Border | #E8E2DB | Kártya/elválasztó szegélyek |

---

## 2. Navigációs struktúra

### Bottom Navigation (vásárlói nézet)

```
[ Termékek ]    [ Kosár (badge) ]    [ Fiók ]
```

- 3 fix tab, mindig látható
- Kosár badge: piros kör, aktuális tételszám (pl. "3")
- Aktív tab: primary szín (#9B2335), kitöltött ikon
- Inaktív: szürke (#999)

### Képernyő-térkép (vásárlói flow)

```
/frontend/products (Termékek - HOME)
  ├── /frontend/products/:id (Termék részletek)
  ├── Kategória szűrés (tab-ok, kliens oldali)
  └── Csomagok szekció (felül, kiemelve)

/frontend/cart (Kosár)
  ├── Savings Progress Bar (spórolás haladás)
  ├── Threshold nudge üzenetek
  └── → /frontend/checkout/delivery (Checkout Step 1)
        └── → Rendelés leadás (POST API)
              └── → Visszaigazolás

/frontend/account (Fiók)
  ├── Bejelentkezés (ha nincs session)
  ├── Rendeléseim (bejelentkezve)
  ├── Profil adatok
  └── Kijelentkezés
```

### Képernyő-térkép (mészáros/futár)

```
/butcher-courier (védett route — butcher/courier role)
  ├── Előkészítés tab (alapértelmezett)
  │     ├── Napi rendelési lista
  │     ├── Rendelés előkészítési nézet
  │     └── Termék elérhetőség toggle
  ├── Kiszállítás tab
  │     ├── Napi kiszállítási lista
  │     ├── Kiszállítás részletei
  │     └── Kézbesítés megerősítése
  └── Statisztikák tab
        ├── Összesítő kártyák
        ├── Oszlopdiagram (napi/heti/havi)
        └── Rendelés lista (időszakra)
```

---

## 3. Vásárlói képernyők — részletes leírás

### 3.1 Termékek oldal (`/frontend/products`) — HOME

**Elrendezés (felülről lefelé):**

1. **Header:** "Termékek" felirat + magyar zászló ikon (jobb felső sarok — nyelvválasztó indikátor)

2. **Csomagok szekció** (kiemelt, felül): 2 csomag kártya egymás mellett. Minden kártya: termékfotó kollázs + "+N" badge + név + "N termék, ~X kg" + "Spórolsz X RON" zöld badge + ár + "Részletek" gomb.

3. **Kategória tab sáv** (horizontálisan scrollozható): Összes | Felvágott & Egyéb | Friss Növendékhús | Friss Sertéshús | Füstölt Áruk | Kolbász & Szalámi. Aktív tab: kitöltött háttér, bold szöveg. Kliens oldali szűrés (nincs API hívás tab-váltásnál).

4. **Termék grid** (2 oszlop): Kártya: termékfotó (1:1, WebP) + kategória badge (szín kódolt) + terméknév + ár + "/kg" egység. Kattintásra: termék részletek oldal. Rendezés: backend custom sorrend.

5. **Bottom nav** (fix)

**Guest-first UX:** Termékek bejelentkezés nélkül is láthatók. Login csak checkout-nál szükséges.

---

### 3.2 Termék részletek (`/frontend/products/:id`)

**Elrendezés:**

1. **Vissza gomb** (bal felső) → vissza a termékek listára
2. **Termék fotó** (nagy, full-width, WebP)
3. **Kategória badge** (pl. "Kolbász & Szalámi" — szín kódolt)
4. **Terméknév** (H1, semibold)
5. **Ár** (nagy, bold, primary szín) + "/kg" egység
6. **Leírás** (magyar nyelven, termék részletezése — felhasználási javaslatok, íz, textúra)
7. **Mennyiség választó:** Egész kg egységben VAGY darabra (pl. Pástétom). `[-]` `szám` `[+]` gombok. Minimum: 0.5 kg (súly alapú) vagy 1 db (darab alapú).
8. **"Kosárba" gomb** (full-width, primary CTA) — kattintásra: hozzáadás a kosárhoz, toast notification, kosár badge frissül

---

### 3.3 Kosár (`/frontend/cart`)

**Elrendezés:**

1. **Header:** "Kosár"

2. **Savings Progress Bar** (v0.3 fő feature — Sprint 3): 2 tier threshold rendszer. Progress bar vizuálisan mutatja a haladást. Threshold nudge üzenet a hiányzó összegről (pl. "Még 52 RON az ingyenes szállításig!"). Tierek: 150 RON = Ingyenes szállítás, 300 RON = 2% kedvezmény.

3. **Tétellista:** Minden tétel: termékfotó (kis) + név + ár + mennyiség módosító ([-] N [+]) + törlés gomb. Ár automatikusan frissül mennyiség-változáskor.

4. **Rendelés összesítő:** Részösszeg, szállítási díj (ingyenes ha >= 150 RON, egyébként 1.5 RON/km a 10 km-en túl), végösszeg (bold, nagy).

5. **"Tovább a fizetéshez" gomb** (full-width CTA). Ha nincs bejelentkezve: login oldal, majd redirect vissza. Ha be van jelentkezve: checkout/delivery.

---

### 3.4 Checkout — Szállítási adatok (`/frontend/checkout/delivery`)

**Elrendezés:**

1. **Header:** "Szállítási adatok" + vissza gomb

2. **Szállítási információ banner:** "Székelyudvarhely és +10 km-es körzetében szállítunk. 10 km-en túl 1.5 RON/km díjat számítunk."

3. **Form mezők:**

| Mező | Típus | Kötelező | Megjegyzés |
|------|-------|----------|------------|
| Név | text input | igen | Teljes név |
| Telefonszám | tel input | igen | +40 prefix |
| Település | text/select | igen | Jelenleg szabad szöveges |
| Utca, házszám | text input | igen | Szállítási cím |
| Megjegyzés | textarea | nem | Opcionális kézbesítési megjegyzés |

4. **Fizetési mód:** Jelenleg CSAK készpénz szállításkor (egyetlen opció). Online fizetés tervezett v0.5-ben.

5. **"Rendelés leadása" gomb** (primary CTA). Validáció: minden kötelező mező kitöltve. API: `POST /api/resource/Sales Order`. Sikeres leadás: visszaigazolás képernyő.

---

### 3.5 Fiók (`/frontend/account`)

**Kijelentkezett állapot:** Bejelentkezési form (email/jelszó) + "Regisztráció" link.

**Bejelentkezett állapot:** Profil adatok (név, email, telefon), Rendeléseim lista (korábbi rendelések, státusz badge-ekkel), Founding 50 státusz (ha tag), Kijelentkezés gomb.

---

### 3.6 Founding 50 Popup

**Megjelenés:** Első látogatáskor automatikusan felugrik (ha még van szabad hely).

**Tartalom:** "Légy az első 50 között!" cím, 3 hónap ingyenes szállítás ajánlat, aktuális foglaltság: "14/50 hely elfoglalva", progress bar (14/50), "Csatlakozom" CTA gomb, "Nem érdekel" bezárás.

**Logika:** Cookie/localStorage alapú — ha elutasította, nem jelenik meg újra.

---

## 4. Mészáros & Futár képernyők — részletes leírás

**Hozzáférés:** `/butcher-courier` (védett route, `butcher` vagy `courier` role szükséges)

A pilot fázisban a mészáros = futár (ugyanaz a személy). Egyetlen fiók, mindkét role-lal. A role-switcher bottom tab bar váltja a nézeteket.

### Bottom Tab Bar (operátori nézet)

```
[ Előkészítés ]    [ Kiszállítás ]    [ Statisztikák ]
```

---

### 4.1 Mészáros — Napi rendelési lista

**Route:** `/butcher-courier` (alapértelmezett tab: Előkészítés)

**Elemek:**
1. **Header:** "Előkészítés" + dátum (jobb oldal)
2. **Összesítő csík** (fix, scrollview alatt): kategóriánkénti kg összesítés (pl. "Friss sertés: 12,5 kg | Füstölt: 8,0 kg"), háttér: meleg barna (#F5EDDF)
3. **Szűrő chipek:** `Új rendelés` | `Előkészítés alatt` | `Kiszállításra kész`
4. **Rendelés kártyák** (mészáros variáns): bal accent sáv (3px, primary), rendelésszám + státusz badge, időablak + tételszám + összeg. Kattintásra: előkészítési nézet.

### 4.2 Mészáros — Rendelés előkészítési nézet

**Elemek:**
1. **Header:** "Rendelés #XXXX" + vissza gomb + státusz badge
2. **Termék lista** (személyes adatok NÉLKÜL): termék neve + mennyiség (kg). Ha termék nem elérhető: sárga warning sáv.
3. **Státusz akció gomb:** "Kiszállításra kész" (primary CTA). API: `PUT /api/resource/Sales Order/{id}` → `custom_status: 'Kiszállításra kész'`

### 4.3 Mészáros — Termék elérhetőség toggle

**Elemek:**
1. **Header:** "Termékek" + vissza gomb
2. **Termék lista kategóriánként:** kategória fejléc (uppercase, szürke) + termék sor: név + ár + toggle pill (ON/OFF). Toggle: optimista UI, háttérben PATCH kérés. API: `PATCH /api/resource/Item/{item_code}` → `{ disabled: 0 | 1 }`

---

### 4.4 Futár — Napi kiszállítási lista

**Route:** `/butcher-courier` → Kiszállítás tab

**Elemek:**
1. **Header:** "Kiszállítás" + dátum
2. **Összesítő:** "Kézbesítve: 3 | Úton: 1 | Kész: 5"
3. **Szűrő chipek:** `Kiszállításra kész` | `Úton van` | `Kézbesítve`
4. **Kiszállítási kártyák** (futár variáns): vásárló neve + cím + időablak + tételszám. Kattintásra: kiszállítás részletei.

### 4.5 Futár — Kiszállítás részletei

**Elemek:**
1. **Header:** vásárló neve + vissza gomb
2. **Vásárló adatok:** név, telefon ("Hívás" gomb → `tel:` link), cím
3. **"Megnyitás Google Maps-ben"** gomb (→ `maps/dir/?api=1&destination=...`)
4. **Rendelés összesítő:** tételszám + összeg + collapsible részletek
5. **Státusz gomb:** Ha "Kiszállításra kész": "Kiszállítás indítása" → státusz: "Úton van". Ha "Úton van": "Kézbesítve" → kézbesítés megerősítés.

### 4.6 Futár — Kézbesítés megerősítése

**Elemek:**
1. Vásárló neve + telefon
2. Megerősítési opciók: "Személyesen átadva" / "Ajtó elé hagyva"
3. Megjegyzés textarea (opcionális)
4. "Kézbesítve — Befejezés" gomb. API: `PUT /api/resource/Sales Order/{id}` → `custom_status: 'Kézbesítve'`, `custom_delivery_note`, `custom_delivered_at`

---

### 4.7 Statisztikák

**Route:** `/butcher-courier` → Statisztikák tab

**Elemek:**
1. **Időszak választó** (segmented control): Napi | Heti | Havi
2. **Navigációs sor:** `[←] 2026. márc. 16–22. [→]` (jövőbe nem lapozható)
3. **Összesítő kártyák** (2x2 grid): Rendelések (db), Bevétel (RON), Kiszállított mennyiség (kg, full-width)
4. **Oszlopdiagram** (heti/havi nézetben): bar chart, primary szín (#9B2335), aktív nap kiemelve. Napi nézetben nincs diagram.
5. **Rendelés lista** (az adott időszakra, görgetéssel elérhető)

---

## 5. Terméklista (aktuális, v3.1 — 2026-04-01)

**Összesen: 37 termék + 2 csomag | 5 kategória | Minden termék elérhető**

### Csomagok

| Név | Tartalom | Súly | Ár | Spórolás |
|-----|----------|------|-----|----------|
| Családi Grill | 5 termék | ~4.6 kg | 156,45 RON | 10 RON |
| Maxi Családi Grill | 5 termék | ~9.2 kg | 306,64 RON | 16,26 RON |

### Friss Sertéshús (13 termék)

| Termék | RO név | Ár (RON/kg) |
|--------|--------|-------------|
| Sertés Bélszín | Muschiulet de porc | 40 |
| Sertés Fehérkaraj | Cotlet de porc dezos. | 33 |
| Sertés Comb | Pulpa de porc dezos. | 25 |
| Sertés Tarja | Ceafa de porc | 30 |
| Sertés Oldalas | Coaste de porc | 25 |
| Sertés Dagadó | Piept de porc cu os | 22 |
| Sertés Lapocka | Spata de porc dezos. | 23 |
| Sertés Apróhús | Carne tocata de porc | 22 |
| Sertés Őrölt Hús | Carne tocata de porc | 22 |
| Sertészsír / Háj | Untura / Osanza | 12 |
| Toka Szalonna | Slanina cruda cu sorici | 20 |
| Bordacsont | Os de porc cu carne | 12 |
| Sertés Csülök | Ciolan de porc crud | 18 |

### Friss Növendékhús (1 termék)

| Termék | RO név | Ár (RON/kg) |
|--------|--------|-------------|
| Növendék Velős Csont | Os de vitel cu maduva | 22 |

### Füstölt Áruk (12 termék)

| Termék | RO név | Ár (RON/kg) |
|--------|--------|-------------|
| Füstölt Has | Piept afumat | 47 |
| Füstölt Oldalas | Coaste afumate | 47 |
| Füstölt Fehér Karaj | Cotlet afumat | 49 |
| Füstölt Bélszín | Muschi afumat | 55 |
| Egész Sonka | Sunca afumata intreaga | 55 |
| Füstölt Tarja | Ceafa afumata | 49 |
| Füstölt Lapocka | Spata afumata | 44 |
| Füstölt Csülök csonttal | Ciolan afumat cu os | 35 |
| Füstölt Csülök csont nélkül | Ciolan afumat dezos. | 44 |
| Füstölt Bordacsont | Os afumat cu carne | 16 |
| Abált Szalonna | Slanina fiarta | 35 |
| Füstölt Szalonna | Slanina afumata | 38 |

### Kolbász & Szalámi (7 termék)

| Termék | RO név | Ár (RON/kg) |
|--------|--------|-------------|
| Deák házi Kolbász | Carnati de casa Deák | 45 |
| Székely Kolbász | Carnati secuiesti | 45 |
| Cérna Kolbász | Carnati cu ata | 48 |
| Miccs / Mici | Mititei | 40 |
| Sertés Szalámi | Salam de porc | 43 |
| Házi Szalámi | Salam de casa | 46 |
| Téli Szalámi | Salam de iarna | 68 |

### Felvágott & Egyéb (4 termék)

| Termék | RO név | Ár (RON/egység) |
|--------|--------|-----------------|
| Abált Szalonna | Slanina fiarta | 35/kg |
| Disznó Fősajt | Toba de porc | 35/kg |
| Göngyölt Hús | Rulada de porc | 47/kg |
| Pástétom | Pate de casa | 22/darab |

_Megjegyzés: Az Abált Szalonna a Füstölt Áruk és Felvágott & Egyéb kategóriában is szerepel._

---

## 6. Rendelési státusz flow

```
[Vásárló leadja]   →  Új rendelés (Comanda noua)          info (kék)
       ↓
[Mészáros indítja] →  Előkészítés alatt (In procesare)    warning (sárga)
       ↓
[Mészáros zárja]   →  Kiszállításra kész (Pregatit)       secondary (barna)
       ↓
[Futár indítja]    →  Úton van (In curs de livrare)       primary (burgundi)
       ↓
[Futár zárja]      →  Kézbesítve (Livrat)                 success (zöld)
       ↓
[Rendszer/Admin]   →  Lezárva (Inchis)                    gray
```

---

## 7. Szállítási logika (jelenlegi)

| Paraméter | Érték |
|-----------|-------|
| Szállítási zóna | Székelyudvarhely + 10 km körzet |
| Ingyenes szállítás | Kosárérték >= 150 RON |
| Szállítási díj | 1.5 RON/km a 10 km-en túl |
| Fizetés | Csak készpénz szállításkor |
| Minimum rendelés | Nincs (de a savings engine 150 RON-ra ösztönöz) |

### Savings Engine thresholdok (v0.3)

| Szint | Küszöb | Jutalom |
|-------|--------|---------|
| Tier 1 | 150 RON | Ingyenes szállítás |
| Tier 2 | 300 RON | 2% kedvezmény |

---

## 8. API végpontok (ismert)

### Vásárlói API

| Végpont | Metódus | Leírás |
|---------|---------|--------|
| `/api/resource/Item` | GET | Terméklista lekérése |
| `/api/resource/Sales Order` | POST | Rendelés létrehozása |
| `/api/resource/Sales Order/{id}` | GET | Rendelés részletei |
| `/api/method/login` | POST | Bejelentkezés |

### Operátori API

| Végpont | Metódus | Leírás |
|---------|---------|--------|
| `/api/resource/Sales Order` | GET (filtered) | Napi rendelések (státusz + dátum szűrőkkel) |
| `/api/resource/Sales Order/{id}` | PUT | Státusz frissítés |
| `/api/resource/Item/{code}` | PATCH | Termék elérhetőség toggle |
| `/api/method/dhop.api.get_stats_summary` | GET | Statisztika összesítő |

---

## 9. Firebase Analytics események (v0.2 + v0.3)

### v0.2 (Done — DH-104)

| Esemény | Mikor |
|---------|-------|
| `page_view` | Minden képernyő megnyitásakor |
| `view_item` | Termék részletek megnyitása |
| `add_to_cart` | Kosárba helyezés |
| `begin_checkout` | Checkout indítás |
| `purchase` | Sikeres rendelés |

### v0.3 (tervezett — DH-129)

| Esemény | Mikor |
|---------|-------|
| `savings_tier_reached` | Threshold elérése (tier 1 vagy 2) |
| `savings_progress_view` | Progress bar megtekintése |
| `savings_nudge_shown` | Nudge üzenet megjelenítése |
| `savings_nudge_action` | Vásárló a nudge hatására hozzáad terméket |
| `reorder_click` | Újrarendelés gomb kattintás |
| `bundle_view` | Csomag részletek megtekintése |
| `bundle_add_to_cart` | Csomag kosárba helyezése |
| `founding50_popup_shown` | Founding 50 popup megjelenítése |
| `founding50_joined` | Csatlakozás a Founding 50-hoz |
| `checkout_duration` | Guardrail — checkout időtartam mérés |

---

## 10. Founding 50 Program

| Paraméter | Érték |
|-----------|-------|
| Program | Early adopter toborzás |
| Kapacitás | 50 fő |
| Jelenlegi foglaltság | 14/50 |
| Jutalom | 3 hónap ingyenes szállítás |
| Retention filter | Soft — ha 30 napig inaktív, hely felszabadul |
| Belépési pont | Popup (első látogatás) + Fiók oldal |

---

## 11. Nyelvi támogatás

| Felület | Elsődleges | Másodlagos |
|---------|-----------|------------|
| Vásárlói PWA | Magyar (HU) | Román (RO) terméknév párhuzamosan |
| Mészáros/Futár | Román (RO) státusz nevek | Magyar (HU) interfész |
| Terméknevek | Magyar + Román (zárójelben) | — |

A termékeknél mindkét nyelv megjelenik: "Deák házi Kolbász (Carnati de casa Deák)"

---

## 12. Ismert korlátok (v0.3)

| Korlát | Terv |
|--------|------|
| Csak készpénz fizetés | Online fizetés v0.5-ben |
| Nincs natív mobil app | iOS prioritás v0.4-ben |
| Nincs email drip / marketing | Backlog (DH-124, 125, 126) — nem spammelünk |
| Nincs admin dashboard | Operátori felület (butcher-courier) van, admin dashboard nincs |
| Település szabad szöveges | Settlement dropdown tervezett (falusi pilot-hoz szükséges) |
| Nincs rendelés-módosítás | Vásárló nem módosíthat leadott rendelést |
| Nincs push notification | PWA push notification tervezett v0.4+ |

---

## 13. Screen Catalog (wireframe-ek)

**Build:** #68 | **URL:** https://deakhus.netlify.app

### Képernyők (15 db)

| ID | Név | Sprint |
|----|-----|--------|
| v0.3-savings-counter | Running Savings Counter | Sprint 3 |
| v0.3-threshold-nudge | Threshold Nudge System | Sprint 3 |
| v0.3-post-order-recap | Post-order Recap | Sprint 3 |
| v0.3-reorder-basket-loader | Reorder Basket Loader | Sprint 3 |
| v0.3-family-bundles | Family Bundles | Sprint 3 |
| v0.3-family-bundles-admin | Family Bundles Admin | Sprint 3 |
| v0.3-favourites | Kedvenc Termékek | Sprint 3 |
| v0.3-familiar-favourites | Szokásos Rendelésem | Sprint 3 |
| v0.3-swap-suggestion | Swap Suggestion MVP | Sprint 3 |
| v0.3-my-orders-savings | Rendeléseim Spórolás | Sprint 3 |
| v0.3-legal-aszf | ÁSZF wireframe | Legal |
| v0.3-legal-privacy | Privacy Policy wireframe | Legal |
| v0.4-butcher-courier | Mészáros és Futár | Sprint 4 |
| v0.4-founding50 | Founding 50 Popup | Sprint 4 |
| v0.5-checkout-redesign | Checkout Redesign | Sprint 5 |

### Dokumentáció (2 db)

| ID | Név | Kategória |
|----|-----|-----------|
| v0.2-analytics-dictionary | Analytics Dictionary | Analytics |
| v0.2-bmc | Business Model Canvas | Business |

---

_Ez a dokumentum a DH PWA v0.3 snapshot-ja. Minden velocity tracker frissítésnél és ticket-változásnál aktualizálandó._
