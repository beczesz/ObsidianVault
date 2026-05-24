---
title: "DH UI Audit — v0.1.24+90 állapot"
version: 1.0
date: 2026-04-04
author: Claude (Anthropic)
description: >
  A deakhus.ro összes screen dokumentálása a v0.1.24+90 verzióban.
  Funkcionális és design jegyzet a v0.3 savings engine tervezéséhez.
id: a4954937-9b17-4979-8159-0a2ea2868bc4
index_schema_version: 1
---

# DH UI Audit — v0.1.24+90

## App architektúra

A DH két fő nézetből áll, amelyek a Fiók screen "Operátor hozzáférés" switcher-en keresztül válthatók:

| Nézet | Bottom nav tabok | URL prefix |
|-------|-----------------|------------|
| **Vásárlói** | Termékek · Kosár · Rendelések · Fiók | /frontend/products, /cart, /orders, /account |
| **Mészáros/Futár** | Előkészítés · Kiszállítás · Statisztikák · Fiók | /frontend/butcher-courier/* |

---

## Vásárlói nézet — Screenek

### 1. Termékek lista (/frontend/products)

**Layout:** 2-oszlopos grid, termékképpel, kategória badge-dzsel, névvel és árral (RON/kg).
**Szűrés:** Horizontálisan görgethető kategória chipek felül (Összes, Felvágott & Egyéb, Friss Növendékhús, Friss Sertéshús, Füstölt Áruk, Kolbász & Szalámi).
**Fejléc:** "Termékek" cím + magyar zászló (nyelv indikátor).
**Nincs:** Keresés, rendezés, szűrés ár szerint, "Elérhető/Nem elérhető" filter.

**Design megjegyzés:** Tiszta, meleg színvilág (bézs háttér, bordó akcentusok). A kártya design egyszerű, nincs "Kosárba" gyorsmenü a listából — a termékre kell kattintani.

### 2. Termék részletező (/frontend/products/:id)

**Layout:** Teljes szélességű termékkép felül, alatta: kategória + "Elérhető" badge, terméknév, ár (RON/kg), leírás szöveg.
**Mennyiség választó:** Preset chipek (0,5 kg · 1 kg · 2 kg · 3 kg · 5 kg) + finomhangolás –/+ gombokkal + numerikus input.
**Ár kalkuláció:** Valós idejű: "0,50 kg × 35,00 RON/kg = 17,50 RON".
**Kosárba státusz:** Ha már a kosárban van: "0,5 kg a kosárban" szöveg jelenik meg.
**CTA:** "Kosárba" gomb alul (sticky footer).
**Navigáció:** Vissza nyíl + terméknév a fejlécben.

**⭐ SAVINGS COUNTER RELEVÁNS:** Ez a screen az egyik hely, ahol a savings counter megjelenhet — a mennyiség választó és az ár kalkuláció mellett.

### 3. Kosár (/frontend/cart)

**Layout:** Termék kártyák listája, mindegyiken: termékkép (thumbnail), név, ár/kg, –/input/+ mennyiség, részösszeg, törlés ikon.
**Figyelmeztetések:**
- "A végső súly és ár ±10%-kal eltérhet" (info badge)
- "A minimum rendelési érték 80,00 RON. Még 62,50 RON hiányzik." (warning badge, narancssárga)
**Összeg:** "Becsült összeg: 17,50 RON" + "1 termék · becslés a kiválasztott mennyiségek alapján"
**CTA:** "Tovább a fizetéshez" gomb (inactive ha minimum alatt van).

**⭐⭐ SAVINGS COUNTER FŐ HELYSZÍN:** A kosár screen a legfontosabb hely a savings counter számára:
- A "Becsült összeg" rész mellett/alatt jelenhet meg a savings feedback
- A minimum rendelési érték figyelmeztetés már threshold nudge jellegű — ezt kell kiterjeszteni
- Threshold szintek: 80 RON (min) → 150 RON (ingyenes szállítás) → 300 RON (2% kedvezmény) → 600 RON (5%)

### 4. Checkout (/frontend/checkout)

**Nem tesztelve** — a minimum rendelési érték alatt a "Tovább a fizetéshez" gomb inaktív.

### 5. Rendeléseim (/frontend/orders)

**Layout:** Rendelés kártyák listája. Minden kártya: rendelés szám (DEAK-ORD-XXXXX), dátum, termékek száma, becsült összeg, státusz badge.
**Státuszok:** "Feldolgozás alatt" (sárga).
**Fejléc:** "Rendeléseim" + magyar zászló.

**⭐ SAVINGS COUNTER RELEVÁNS:** A post-order savings recap itt jelenhet meg — a rendelés kártyán vagy a részletezőben.

### 6. Rendelés részletező (/frontend/orders/:id)

**Layout:** 4 szekció kártyákban:
1. **Státusz stepper** — vizuális progress: Új → Feldolg. → Kész → Szállítás → Kiszáll. → Lezárva + szöveges leírás
2. **Megrendelt termékek** — terméknév, ár/kg, mennyiség, részösszeg
3. **Becsült összeg** + ±10% figyelmeztetés
4. **Szállítási adatok** — cím + dátum + időablak
5. **Állapot története** — timeline (timestamp + státusz változás)

**⭐ SAVINGS COUNTER RELEVÁNS:** A "Becsült összeg" mellett jelenhet meg: "Ezzel a rendeléssel X RON-t optimalizáltál" (post-order recap).

### 7. Fiók — vásárlói (/frontend/account)

**Layout:** Profil kártya (teljes név, telefonszám, szállítási cím) + "Szerkesztés" gomb + Operátor hozzáférés szekció + verzió + kapcsolat.
**Operátor switcher:** "ADMIN" badge + "Váltás operátor módba" gomb (bordó, kitöltött).
**Verzió:** v0.1.24+90

---

## Mészáros/Futár nézet — Screenek

### 8. Előkészítés (/frontend/butcher-courier/preparation)

**Layout:** Fejléc "Előkészítés" + dátum. Összesítő sáv: "Friss Sertéshús: 0,5 kg | Friss Növendékhús: 0,0 kg".
**Szűrő chipek:** Összes (2) · Új (0) · Folyamatban (2) · Kész (0) · Kézbesítve (0).
**Progress bar:** Vizuális haladásjelző.
**Rendelés kártyák:** Rendelés szám, vásárló név, dátum + időablak, termékszám + összeg, státusz badge ("Feldolgozás alatt").

### 9. Kiszállítás (/frontend/butcher-courier/delivery)

**Layout:** Fejléc "Kiszállítás" + dátum. Összesítő sáv: Kész (0) · Úton (0) · Kézbesítve (0).
**Szűrő chipek:** Összes (0) · Kiszállításra kész (0) · Úton (0) · Kézbesítve (0).
**Üres állapot:** Teherautó ikon + "Ma nincs ütemezett szállítás."

### 10. Statisztikák (/frontend/butcher-courier/stats)

**Layout:** Időszak váltó (Napi · Heti · Havi) + dátum navigátor.
**KPI kártyák:** Rendelések (2 db) · Bevétel (190,00 RON) · Átlagos kosár (95,00 RON).
**Oszlopdiagram:** Napi bevétel (RON) — hét napjai.
**Rendelések lista:** Alul a rendelés kártyák.

### 11. Fiók — operátor (/frontend/account, operátor módban)

Megegyezik a vásárlói fiókkal, de a switcher gomb: "Vissza az alkalmazásba" + "Operátor módban vagy" szöveg.

---

## Design System észrevételek

| Elem | Jelenlegi megvalósítás |
|------|----------------------|
| Színvilág | Meleg bézs (#FDF6EC-szerű) háttér, bordó (#8B1A2B) akcentus, arany (#C4A35A) kategória badge-ek |
| Tipográfia | Serif címek (Playfair-szerű), sans-serif body |
| Kártyák | Fehér háttér, enyhe shadow, rounded corners |
| Bottom nav | 4 tab, ikon + label, aktív: bordó |
| Badge-ek | Lekerekített chipek, kategória szín kódolva (bordó, arany, zöld) |
| Gombok | Bordó filled (CTA), fehér outlined (secondary) |
| Figyelmeztetések | Info (szürke ikon), Warning (narancssárga, kitöltött háttér) |
| Üres állapot | Ikon + szöveg, középre igazítva |

---

## Megjegyzések a v0.3 tervezéshez

1. A **Kosár screen a legtermészetesebb hely** a savings counter számára — már van "Becsült összeg" és threshold figyelmeztetés (min 80 RON).
2. A **termék részletező** jó hely kiegészítő savings info-nak (pl. "Ha 1 kg-ot rendelsz, X RON-t spórolsz kg-onként").
3. A **rendelés részletező** ideális a post-order recap-nek.
4. A **Termékek lista** jelenleg NEM mutat savings-jellegű infót — itt lehetne "Ma ajánlott" badge vagy hasonló (future).
5. Nincs checkout screen tesztelve — a savings counter összegzés ott is fontos lesz.
