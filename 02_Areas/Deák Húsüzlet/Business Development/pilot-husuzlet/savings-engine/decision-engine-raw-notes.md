---
title: "Decision Engine — Nyers gondolatok"
version: 0.1
date: 2026-04-03
author: Becze Szabolcs
description: A DH decision engine alapgondolatai és a 10 optimalizálási lehetőség (jelenlegi modell + DH rendszer).
id: dbd9c0aa-812c-4e45-b8a9-c1a7f40526b8
index_schema_version: 1
---

# Decision Engine — Nyers gondolatok

## Alap gondolat

Az applikáció segít a felhasználónak okos döntéseket hozni → olcsóbban jut a húshoz → mérjük és kijelezzük a felhasználónak.

Nem azon spórol a vásárló, hogy olcsóbban adjuk a húst, hanem hogy **kioptimizáljuk a folyamatokat**.

---

## Optimalizálási lehetőségek - hol folyik el a margin?

### Jelenlegi modell — Min tud spórolni a vásárló?

#### 1. Feldolgozás

Ha a Deák biztosan el tudja adni a termékét még aznap és nem kell 2x feldolgozza.

- Régebb beszállította az üzletbe, ott a meg nem vásárolt húst visszavitte
- Tartósította
- Újra üzletbe
- A meg nem vásárolt tartósított hús pedig veszteség

#### 2. Logisztika

Az üzletek drágák: kb. **8.800 RON**

- Fizetés
- Bér
- Rezsi
- Egyéb

Ha könnyebben, direkt a felhasználóhoz tudna jutni az étel, akkor olcsóbb lenne.

#### 3. Mennyiség

Nyilván, ha keveset vásárol, akkor 150g szalámi csomagolva veszteségesebb, mint 2kg szalámi csomagolva.

Bizonyos termékeket — mint pl. a virsli — nem is éri meg, hogy kis adagokban legyenek elkészítve, emiatt szezonális termékek.

#### 4. Teljes állat

Egy disznóban vannak könnyen eladható részek és kevésbé könnyen eladható részek.

**Probléma:** ha a user csak a "jó részeket" veszi → a többi veszteség.

**Savings opportunity:** Ha a rendszer ajánlja a kevésbé népszerű részeket, vagy bundle-be teszi → **teljes állat jobban monetizálódik**.

#### 5. Demand volatility

Ma nem tudják pontosan, mit vesznek → túltermelés / alultermelés.

**Savings:** preorder + early signal → kevesebb waste.

---

### DH rendszer — Új spórolási lehetőségek

#### 6. Time-to-sell

Minél tovább áll a hús, romlik az értéke és nő a kockázat.

**Savings:** *"Ma ezt vedd"* → gyorsabb forgás = jobb economics.

#### 7. Picking & packing cost

Online minden rendelést külön kell összeszedni.

**Savings:** nagyobb kosár + standardizált csomag → kevesebb munka / rendelés.

#### 8. SKU complexity

Sok variáció → sok hiba, sok overhead.

**Savings:** bundle + standard kosár.

#### 9. Payment / failed delivery risk

Nem veszi át → cash flow probléma.

**Savings:** előre fizetés ösztönzés + megbízható user behavior.

#### 10. Marketing cost

Ha minden usert külön kell megszerezni → drága.

**Savings:** group order + referral-like behavior.

