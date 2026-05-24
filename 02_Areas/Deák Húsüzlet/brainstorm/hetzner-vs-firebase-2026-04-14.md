---
title: Hetzner vs Firebase költségelemzés (DH platform)
version: 1.0
date: 2026-04-14
author: Becze Szabolcs
description: Elméleti hosting költség összehasonlítás Hetzner Cloud és Firebase Blaze között a DH platform 3 forgalmi szcenáriójára.
id: 8ac0fe13-a474-47e7-9e5b-512a31bdcf88
index_schema_version: 1
---

# Hetzner vs Firebase költségelemzés

**Kontextus:** A DH platform jelenleg Hetzner Cloud VPS-en fut. Kérdés: mibe kerülne ugyanez Firebase-en (Blaze tarifa).

**Fontos disclaimer:** Architektúrális összehasonlítás, NEM 1:1 migráció. Frappe (Python ERP, MariaDB, monolitikus) és Firebase (NoSQL Firestore + Cloud Functions + Hosting) gyökeresen más rendszerek. A számok azonos kapacitású szolgáltatásra vonatkoznak.

---

## 1. Hetzner Cloud (jelenlegi setup)

### Egy CX VPS havi költsége (2026. áprilisi árak, EUR)

| Tétel | Költség / hó | Költség / év |
|------|-------------:|-------------:|
| CX22 VPS (2 vCPU, 4 GB RAM, 40 GB SSD, 20 TB traffic) | 3.79 EUR | 45.48 EUR |
| CX32 VPS (4 vCPU, 8 GB RAM, 80 GB SSD, 20 TB traffic) | 6.80 EUR | 81.60 EUR |
| Backup (kb. 20 % hozzáadás) | +0.80-1.40 EUR | +10-17 EUR |
| Floating IP (opcionális) | 0.50 EUR | 6 EUR |
| Snapshot storage (~10 GB) | ~0.10 EUR | ~1 EUR |
| **Összesen (CX22 + backup)** | **~5 EUR** | **~60 EUR** |
| **Összesen (CX32 + backup)** | **~8 EUR** | **~96 EUR** |

**Megjegyzés:** Hetzner ára átalány, a forgalom 20 TB-ig benne van. Ez a szint pilot- és skálázási fázisban is bőven elég.

### Mit nem fed le a Hetzner ár
- DevOps idő (mi telepítjük, mi mentjük)
- Monitoring (Grafana, UptimeRobot stb. külön)
- Külső CDN (jelenleg nincs, deakhus.ro statikus tartalmat is a Frappe szolgálja ki)

---

## 2. Firebase Blaze (pay-as-you-go) – referencia árak

| Szolgáltatás | Free tier | Túl a free tier-en |
|--------------|-----------|---------------------|
| Firestore reads | 50 000 / nap (= 1.5 M / hó) | 0.18 USD / 100 000 |
| Firestore writes | 20 000 / nap (= 600 k / hó) | 0.18 USD / 100 000 |
| Firestore deletes | 20 000 / nap | 0.02 USD / 100 000 |
| Firestore storage | 1 GB | 0.26 USD / GB / hó |
| Cloud Functions invocations | 2 M / hó | 0.40 USD / M |
| Cloud Functions egress | 5 GB / hó | 0.12 USD / GB |
| Hosting storage | 10 GB | 0.026 USD / GB |
| Hosting bandwidth | 10 GB / hó | 0.15 USD / GB |
| Authentication | 50 k MAU (Identity Platform free) | tier szerint |
| Cloud Storage | 5 GB | 0.026 USD / GB / hó |

USD/EUR árfolyam (becslés): 1 USD ≈ 0.92 EUR (2026 április).

---

## 3. Három forgatókönyv – Firebase becslés

### Feltevések egy átlagos vásárlói munkamenetre
- 1 page view ≈ 8-12 Firestore read (kategória, termékek, cart, user)
- 1 rendelés ≈ 5 write (order, items, status, user history, log)
- Cart művelet ≈ 1 write
- Átlagos oldalméret ≈ 1.5 MB (kép + JS + HTML)
- Hosting bandwidth = page views × oldalméret

### A) Pilot (első 30 nap)
- 30-100 user, 15-50 rendelés, 5-10 k oldalmegtekintés / hó

| Tétel | Mennyiség | Költség |
|-------|----------:|--------:|
| Firestore reads | ~100 k | free |
| Firestore writes | ~5 k | free |
| Storage | <100 MB | free |
| Functions invocations | ~20 k | free |
| Hosting bandwidth | 5-10 GB | free |
| Auth (MAU) | 100 | free |
| **Firebase összesen** | | **0 USD / hó** |

### B) Sikeres pilot után (3-6 hó) ← **ezt kérted**
- 200-500 user, 100-300 rendelés, 30-50 k oldalmegtekintés / hó

| Tétel | Mennyiség | Költség |
|-------|----------:|--------:|
| Firestore reads | ~500 k / hó | free (1.5 M határ alatt) |
| Firestore writes | ~5 k / hó | free |
| Storage | ~10 MB | free |
| Functions invocations | ~100 k | free (2 M határ alatt) |
| Functions egress | ~3 GB | free |
| Hosting bandwidth | ~60 GB → 50 GB excess | 50 × 0.15 = **7.50 USD** |
| Auth (MAU) | 350 | free |
| **Firebase összesen** | | **~7-10 USD / hó (~7-9 EUR)** |

### C) Skálázott (1+ év, többségi forgalom)
- 1000+ user, 500+ rendelés, 100 k+ oldalmegtekintés / hó

| Tétel | Mennyiség | Költség |
|-------|----------:|--------:|
| Firestore reads | ~1.5-2 M / hó | 0-9 USD |
| Firestore writes | ~20 k / hó | free |
| Storage | ~50 MB | free |
| Functions invocations | ~300 k | free |
| Functions egress | ~10 GB → 5 GB excess | 0.60 USD |
| Hosting bandwidth | ~150 GB → 140 GB excess | 140 × 0.15 = 21 USD |
| Auth (MAU) | 1000 | free |
| **Firebase összesen** | | **~25-35 USD / hó (~23-32 EUR)** |

---

## 4. Direkt összehasonlítás

| Szcenárió | Hetzner / hó | Firebase / hó | Diff |
|-----------|-------------:|--------------:|-----:|
| A) Pilot (első 30 nap) | ~5 EUR | ~0 EUR | Firebase −5 EUR |
| **B) Sikeres pilot (3-6 hó)** | **~5 EUR** | **~7-9 EUR** | **Firebase +2-4 EUR** |
| C) Skálázott (1+ év) | ~5-8 EUR | ~23-32 EUR | Firebase +18-24 EUR |

**Éves szinten (B szcenárió):**
- Hetzner: ~60 EUR
- Firebase: ~85-110 EUR
- Különbség: +25-50 EUR / év Firebase javára (drágább)

---

## 5. Mit NEM mutat ki a számolás (rejtett tényezők)

### Firebase javára (Hetzner ezt nem tartalmazza)
- Auto-skálázás csúcsterhelésnél (Hetzner egy VPS, te kezeled)
- Globális CDN ingyen (Hetzner egy lokáció, gyorsabb letöltés Magyarországról)
- Managed mentés (Hetzner backup külön opció és csak snapshot)
- Kevesebb DevOps idő (nincs OS update, nincs nginx config, nincs MariaDB tuning)
- Built-in Auth (Frappe-ban kell írni)

### Hetzner javára (Firebase nem mutatja)
- Architektúra váltás KÖLTSÉGE: a Frappe-t újra kell írni Firestore-ra. Ez 2-4 ember-hónap (~10-20 k EUR fejlesztői költség). Ez 200+ év hosting megtakarításnak felel meg a B szcenárióban.
- Vendor lock-in: a Firebase API saját, kilépés drága
- Ár-előrejelezhetőség: Hetzner fix, Firebase egy pánikrendelési hullám = váratlan számla
- Frappe ERP-jellegű képességek (szerepkörök, workflow, riport) elvesznek
- Tárolási határ Firestore-on: dokumentum max. 1 MB, kollekció query 1 MB / oldal — termékadat OK, de hosszabb lista nem stream-elhető szabadon
- EU adatlokáció: Firebase europe-west régiók 8-12 % drágábbak az amerikainál; ezt belekalkuláltam? **Nem**, az árak USA-régióval számolnak. EU régióban kb. +10 %.

### Egy nagyon fontos kockázat
A Firebase Hosting bandwidth ($0.15/GB) az, ami legtöbbször elszállna. Ha egy termékfotó vagy videó vírusra megy, vagy a deployment méret nő, **könnyű 100+ EUR / hó** felé futni. Hetzneren a 20 TB-os átalány miatt ez csendben meg sem mozdul.

---

## 6. Javaslat

A pilot fázisban (B szcenárió) a két opció **gyakorlatilag egyenlő** havi szinten (5 vs 7-9 EUR), de:

1. **A Firebase-re váltás 10-20 k EUR fejlesztői költség** — ez egy stop cap-en (~12-13 k EUR teljes pilot kockázat) belül **önmagában elvinné a teljes pilot büdzsét.**
2. Skálázott szcenárióban a Firebase ~3-5x drágább / hó.
3. **Marad a Hetzner**, de érdemes Firebase-ből egy szeletet beszúrni:
   - **Firebase Hosting** csak a frontend statikus build-jére → globális CDN, gyors loading. 10 GB free, valószínűleg ingyen marad.
   - **Firebase Auth** ha nehézzé válik a Frappe felhasználókezelése. 50 k MAU free.
   - **Firebase Analytics** (DH-104 amúgy is nyitott ticket) → már most is ezt tervezi a csapat.

A backendet (rendelések, készlet, admin) tartsuk Frappe-ban Hetzneren — gyors, olcsó, ismert.

---

## 7. Hivatkozások
- [Hetzner Cloud Pricing 2026](https://datacentrenews.uk/story/hetzner-unveils-new-cloud-server-plans-from-eur-3-79-per-month)
- [Hetzner CX árak (CostGoat)](https://costgoat.com/pricing/hetzner)
- [Firebase Pricing (Google)](https://firebase.google.com/pricing)
- [Firebase Hosting árak](https://firebase.google.com/docs/hosting/usage-quotas-pricing)
- [Firestore pricing (Google Cloud)](https://cloud.google.com/firestore/pricing)
- [SuperTokens: Firebase pricing breakdown](https://supertokens.com/blog/firebase-pricing)
