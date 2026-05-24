---
title: "Design Referencia — Deák Húsmíves vizuális rendszer"
date: 2026-04-22
purpose: "Claude Design-nak: minden vizuális adat egy helyen"
id: 279ca0dd-b1b5-4ad0-b474-679716d19e6c
index_schema_version: 1
---

# Design Referencia — Deák Húsmíves

Ez a dokumentum összefoglalja a Deák Húsmíves vizuális identitását és a meglévő design elemeket. Claude Design számára referencia.

---

## 1. Színpaletta

| Szín | Hex | Használat |
|------|-----|-----------|
| **Deák piros** | #C0392B | Elsődleges brand szín, címek, sávok, CTA |
| **Világos piros** | #E74C3C | Gradient másik vége, hover állapot |
| **Fehér** | #FFFFFF | Háttér, szöveg piros felületen |
| **Sötétszürke** | #2C2C2C | Törzsszöveg |
| **Középszürke** | #666666 | Alcímek, másodlagos szöveg |
| **Világos szürke** | #444444 | Leírások |
| **Halvány rózsaszín** | #FDF2F0 | Info box háttér, kiemelés |

### Gradient
```css
background: linear-gradient(90deg, #C0392B, #E74C3C);
```
Ezt használjuk a felső és alsó sávokon.

---

## 2. Tipográfia (a v11 szórólap alapján)

| Elem | Méret (nyomtatás) | Súly | Szín |
|------|-------------------|------|------|
| Logó | 28mm magas | — | — |
| Főcím | 10mm | 900 (Black) | #C0392B |
| Alcím | 4.2mm | 700 (Bold) | #2C2C2C |
| Érték cím | 3.6mm | 700 | #C0392B |
| Érték leírás | 3.2mm | 400 | #666 |
| Kategória cím | 3.6mm | 700 | #C0392B, uppercase |
| Kategória tartalom | 3.2mm | 400 | #444 |
| Lábléc | 3.2mm | 400 | #FFFFFF |
| Tagline | 4.5mm | 800 | #C0392B |
| QR URL | 4.2mm | 800 | #C0392B |

**Font család:** 'Segoe UI', 'Helvetica Neue', Arial, sans-serif

---

## 3. Logó

Elérhető formátumok a `Marketing/` mappában:
- `Deak Husmives logo.png` — eredeti PNG (1195 KB)
- `Deak Husmives logo transparent.png` — átlátszó háttér (1318 KB)
- `Deák Logo Final.svg` — végleges SVG (181 KB)
- `Deak Husmives logo_clean.svg` — tisztított SVG (532 KB)
- `Deak Husmives logo.pdf` — PDF formátum
- `logo_layers/` — rétegezett változatok

A logó tartalmaz egy stilizált bikafej ikont és a „Deák Húsmíves" feliratot.

---

## 4. Meglévő design elemek (v11 szórólap)

### Felső sáv
- Magasság: 7mm
- Gradient: #C0392B → #E74C3C (balról jobbra)

### Alsó sáv (lábléc)
- Gradient: #C0392B → #E74C3C
- Szöveg pozíció: felső harmad (`padding: 2.5mm 4mm 5mm 4mm`)
- Tartalom: „Deák Húsmíves • Székelyudvarhely • www.deakhus.ro"

### Elválasztó vonal
- Szélesség: 24mm, magasság: 0.5mm
- Szín: #C0392B
- Középre igazítva

### Info box (hátoldal)
- Háttér: #FDF2F0
- Border-radius: 2mm
- Bal szegély: 1.2mm solid #C0392B
- Padding: 3.5mm 4mm

### ✕ Ikon (hátoldal kategóriák)
- Unicode: ✖ (&#x2716;)
- A kategória címek előtt

---

## 5. Brand voice összefoglaló

**Egy mondatban:** Egy megbízható helyi mesterember, aki keveset beszél, de amit mond, igaz.

**Így hangzunk:**
- „Hajnalban készül. Kézműves minőség. Ma nálad."
- „Friss. Tiszta. Házhoz."
- „37 kézműves termék, minden nap frissen."

**Így NEM hangzunk:**
- „HIHETETLEN AKCIÓ! RENDELD MOST!"
- „Prémium artizanális húskészítmények omnichannel disztribúciója."
- „Forradalmi e-commerce platform debütál Hargita megyében."

**Kulcsszavak:** őszinte, helyi, egyszerű, megbízható, kézműves, friss

---

## 6. QR kód specifikáció

A szórólapon és plakáton QR kód van, ami a deakhus.ro-ra mutat UTM paraméterekkel.

**Founding 50 kampány URL-ek:**

| Forrás | URL |
|--------|-----|
| Szórólap | `https://www.deakhus.ro?utm_source=qr_flyer&utm_medium=offline&utm_campaign=founding50` |
| Plakát | `https://www.deakhus.ro?utm_source=qr_poster&utm_medium=offline&utm_campaign=founding50` |
| Bolt pult | `https://www.deakhus.ro?utm_source=qr_counter&utm_medium=offline&utm_campaign=founding50` |

A QR kódnak kontrasztosnak és legalább 25×25mm méretűnek kell lennie szórólapon, 50×50mm plakáton.

---

## 7. A termékkínálat (referencia)

- 37 termék, 5 kategória
- Kézműves húskészítmények: kolbász, szalámi, sonka, virsli, felvágott stb.
- Minden nap frissen készül
- Székelyudvarhelyen házhozszállítás
- Minimum kosárérték: 80 RON
- Szállítási díj: 15 RON (Founding 50 tagoknak: INGYENES)

---

## 8. Meglévő fájlok referencia

| Fájl | Mi ez |
|------|-------|
| `Marketing/szorolap/szorolap_v11_eleje.html` | A5 szórólap eleje (aktuális) |
| `Marketing/szorolap/szorolap_v11_hatoldal.html` | A5 szórólap hátoldal (aktuális) |
| `Marketing/szorolap/szorolap_v11_eleje_A4.html` | A4 nyomtatási layout (2×A5) |
| `Marketing/szorolap/szorolap_v11_hatoldal_A4.html` | A4 nyomtatási layout, 180° forgatva |
| `Marketing/brand_voice.md` | Teljes brand voice dokumentum |
| `Marketing/sales/messaging_ervrendszer_v1.1.md` | Messaging érvrendszer |
| `Marketing/kutatas_ipari_hus_adalekanyagok.md` | Adalékanyag kutatás (hátoldal alapja) |
