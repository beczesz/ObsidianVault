---
title: "DH wireframe → approved screen base mapping"
description: "Reference guide mapping wireframe views to approved screen bases for DH feature development. Designers use this table to identify which existing screen template each new feature view should build upon, ensuring visual consistency and reusing established UI patterns across the product."
description_source: auto
description_hash: e3b383af831ea11d
version: 1.0
date: 2026-05-09
status: living document
purpose: |
  Új wireframe craftolásakor ne kelljen minden alkalommal megmondani, hogy melyik
  approved screen az alap. Ez a mapping rögzíti a kapcsolatokat: melyik feature /
  view mely approved screen szerkezetét veszi át.
id: bfd28a87-f79b-4b7b-8b4e-2863bb4596c4
index_schema_version: 1
---
# DH wireframe → approved screen base mapping

> **Hogyan használd:** Új feature wireframe készítésekor először nézd meg, melyik view-ja melyik approved screen-re épül. A "Default base" oszlop mindig autoritatív, kivéve ha a feature spec mást ír elő.

## 1. Approved screens könyvtár

Helye: `design/approved-sample-screens/`

| Fájl | Mit ad | Jellegzetes minták |
|---|---|---|
| `products.html` | Termék lista | Termékkártya rács, kategória chip-ek, mennyiség kontrol, sticky header |
| `cart.html` | Kosár | Cart-item kártya (img + details + qty), súly disclaimer, savings progress bar, summary, fixed checkout-bar + bottom nav |
| `cart-zone-keresztur.html` | Kosár zónával | Cart + zóna-perzisztens kártya |
| `checkout-delivery.html` | Checkout szállítás (üres) | Form mezők, address picker |
| `checkout-delivery-filled.html` | Checkout szállítás (kitöltve) | Filled form állapot |
| `checkout-confirm.html` | Rendelés visszaigazolás | Order summary, payment confirm |
| `order-success.html` | Sikeres rendelés | Confirmation hero, "köszönjük", tracking link |
| `orders.html` | Rendelések lista | Rendelés kártyák státusz badge-ekkel |
| `login.html` | Bejelentkezés | Auth form, branding |
| `butcher-delivery.html` | Mészáros / futár nézet | Delivery list courier perspectivából |
| `butcher-delivery-polished.html` | Polished mészáros nézet | Stats card, delivery list, status pills (DH-184 base) |
| `butcher-order-detail.html` | Rendelés részletek admin | Customer info, item list, action buttons |
| `component-showcase.html` | Design system katalógus | Buttons, badges, icons, palettes |
| `privacy-policy.html` | Jogi oldal (RO) | Legal copy layout |

## 2. Egyéb in-catalog referenciák

Helye: `design/screen-catalog/screens/`

| Fájl | Mit ad | Jellegzetes minták |
|---|---|---|
| `product_details.html` | Termék részlet (DH-183) | **Phone frame 390×844** dynamic island bezel-lel, header + image + chip + name + price + desc + qty pills + qty stepper + sticky CTA + bottom nav, kg/hibrid/db tab variánsok |
| `v0.4-rural-delivery.html` | Iframe-shell pattern | Top header + tabs + iframe — Több sub-screen összekötése egy fájlba |
| `v0.4-courier-route.html` | Panels grid + dh-crumb + dh-copy | Self-contained panels grid pattern, copyable breadcrumb, panel-meta + per-panel hivatkozás |

## 3. Default base mapping per view

Új wireframe craftolásakor ezeket vedd alapul, kivéve ha a feature spec mást ír elő.

| Új view / feature | Default base | Ok |
|---|---|---|
| **Termékdetail** (új termékprofil, termék variáns) | `screens/product_details.html` | Phone frame 390×844, dynamic island, full chrome — DH-183 már megalapozta |
| **Termék lista** | `approved-sample-screens/products.html` | Termék kártya rács, kategória chip-ek |
| **Kosár** | `approved-sample-screens/cart.html` | 448 wide, cart-item kártya, savings progress, fixed checkout-bar |
| **Checkout flow** | `approved-sample-screens/checkout-delivery*.html` + `checkout-confirm.html` | Form pattern, multi-step wizard |
| **Rendelés visszaigazolás** | `approved-sample-screens/order-success.html` | Confirmation hero |
| **Rendelések lista** | `approved-sample-screens/orders.html` | Order card status pattern |
| **Login / signup** | `approved-sample-screens/login.html` | Auth form |
| **Mészáros / Admin / Futár view** | `approved-sample-screens/butcher-delivery-polished.html` + `butcher-order-detail.html` | Polished admin pattern (DH-184 ref) |
| **Legal oldal** (ÁSZF, Privacy) | `approved-sample-screens/privacy-policy.html` | Long-form legal layout |
| **Iframe-shell** több sub-screen-hez | `screens/v0.4-rural-delivery.html` | Top tabs + iframe pattern |
| **Self-contained panels grid** specimen book stílus | `screens/v0.4-courier-route.html` | Panels grid + dh-crumb + dh-copy |

## 4. Reusable komponensek (újrahasznált patterns)

A következő komponensek minden új wireframe-en konzisztensen használandók:

| Komponens | Forrás | Használat |
|---|---|---|
| `.dh-crumb` + `.dh-copy` (másolható breadcrumb) | `v0.4-courier-route.html` | Minden self-contained katalógus screen tetején |
| Phone frame 390×844 (dynamic island bezel) | `product_details.html` | Self-contained mobile screen mockup |
| Phone frame 448-wide flat (no bezel) | `cart.html` | Lista- és tartalom-orientált screen |
| `.scr-header` / `.scr-body` / `.scr-cta` / `.scr-nav` flex architektúra | `v0.4-courier-route.html` | Belső scroll fix, no absolute pozícionálás |
| `.cart-item` kártya (img + details + qty controls + line total) | `cart.html` | Bármely kosár-szerű listán |
| Savings progress bar (0 / 150 / 300 RON markers) | `cart.html` | Kosár flow |
| Status badge palette (ready / delivering / delivered / cancelled) | DESIGN.md + `butcher-delivery-polished.html` | Rendelés státusz mindenhol |
| `.dh-vg` Variation Group komponens | `screens/v0.4-product-variations.html` (DH-173) | Termék-szintű opció-választás detail és kosár |
| Fixed checkout-bar + bottom nav layered | `cart.html` | Bármely flow-jellegű screen alja |

## 5. Workflow

1. **Új feature spec olvasása** → mit kell ábrázolni, hány view-ban
2. **Default base meghatározás** ezen táblázat 3. szekciója alapján → ha nincs match, használd a courier-route panels grid pattern-t
3. **Reusable komponensek listázása** (4. szekció) → ami már létezik, ne találd ki újra
4. **Wireframe craft** a workflow.md 17. szekciójának konvencióival
5. **Új komponens?** Ha létrehoztál egy újrahasznosítható patternt, dokumentáld ide a 4. szekcióba

## 6. Verzióhistória

| Dátum | Esemény |
|---|---|
| 2026-05-09 | v1.0 létrehozva — DH-173 product-variations craftolása közben |
