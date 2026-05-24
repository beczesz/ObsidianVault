---
title: Development Roadmap – DHOP MVP
version: 1.1
date: 2026-03-05
author: Becze Szabolcs – Exar Labs
description: Szöveges fejlesztési roadmap a DHOP MVP ticketjeihez — fázisok, sorrend, dependenciák magyarázattal. v1.1: DHOP-9 Facebook OAuth optional/post-MVP; phase exit criteria hozzáadva; Meta App Review megjegyzés javítva.
---

# Development Roadmap – DHOP MVP

_Version: 1.1 | Last updated: 2026-03-05_

---

## Áttekintés

Ez a roadmap meghatározza, hogy a 44 Jira ticket (7 Epic + 37 Task) milyen sorrendben és fázisokban kerüljön implementálásra. A sorrend nem önkényes: a dependencia-lánc és a kockázatcsökkentés logikája diktálja.

**Alapelv:** Amit nem lehet párhuzamosan csinálni, azt sorban kell. Amit igen, párhuzamosan kell. A kritikus út: infrastruktúra → auth + adatmodell → katalógus → rendelési folyamat → admin/futár → indítás.

---

## Fázisok

### 0. FÁZIS – Alapok (1. hét)
**Cél:** Van egy élő staging szerver és egy elfogadott adatmodell, mielőtt bármilyen feature-fejlesztés elkezdődik.

**Miért ez az első?** Fejlesztők nem tudnak értelmes módon dolgozni staging nélkül. Az order data model (DHOP-24) pedig olyan döntéseket tartalmaz, amelyek kihatnak szinte minden más ticketre — ha ez later változik, sok munkát kell újracsinálni.

| Ticket | Feladat | Párhuzamos? |
|--------|---------|-------------|
| DHOP-40 | Hosting & deployment setup | ✅ Igen |
| DHOP-24 | Order status data model (design + séma) | ✅ Igen — párhuzamos az infra-val |

**Kimenet:** Staging szerver él HTTPS-en, order schema dokumentált és jóváhagyott.

**Fázis exit criteria:** Staging URL elérhető HTTPS-en; order schema pull request-ként review-zva és mergelve; minden fejlesztő hozzáfér a staging környezethez.

---

### 1. FÁZIS – Auth + Környezet (1–2. hét)
**Cél:** Bármelyik szerepkörű felhasználó be tud jelentkezni, a session kezelés működik, és a környezet biztonságos.

**Miért itt?** Az összes többi feature — katalógus, rendelés, admin, futár — authenticated felhasználót feltételez. Amíg ez nem megy, semmi más nem tesztelhető end-to-end.

| Ticket | Feladat | Párhuzamos? |
|--------|---------|-------------|
| DHOP-41 | Environment configuration | ✅ Párhuzamos a többivel (DHOP-40 után) |
| DHOP-8 | Google OAuth | ✅ Párhuzamos DHOP-10-zel |
| DHOP-9 | Facebook OAuth | ⚠️ **[OPTIONAL / post-MVP]** — ne blokkoljuk a launch-ot erre |
| DHOP-10 | Email + password auth | ✅ Párhuzamos |
| DHOP-11 | User profile setup screen | ❌ DHOP-8, 9, 10 után |
| DHOP-12 | Session management + role routing | ❌ DHOP-8, 9, 10 után |

**Fontos megjegyzés:** DHOP-12 (session) és DHOP-11 (profil) egymással párhuzamosan implementálható, mindkettő az auth trojka (8+10) után. DHOP-9 (Facebook OAuth) opcionális — a pilot elindítható nélküle.

**Kimenet:** Bejelentkezés Google OAuth-szal és email/password-del működik. Profilkitöltés megjelenik. Session 30 napig él. Admin és futár nem ér el customer route-okat.

**Fázis exit criteria:** Legalább 1 auth módszer (Google vagy email/password) end-to-end tesztelve staging-en, beleértve a role-based routing-ot.

---

### 2. FÁZIS – Termékkatalógus (2. hét)
**Cél:** A customer látja a termékeket és tud mennyiséget választani.

**Miért most?** A katalógus az egyetlen nagyobb feature-blokk, ami nem függ az order data model-től. Párhuzamosan indítható az auth-tal, de az auth kell hozzá a "bejelentkezve láthatod" feltétel miatt.

| Ticket | Feladat | Párhuzamos? |
|--------|---------|-------------|
| DHOP-13 | Product listing page | ✅ Párhuzamos DHOP-17-tel |
| DHOP-17 | Category support | ✅ Párhuzamos DHOP-13-mal |
| DHOP-14 | Product detail view | ❌ DHOP-13 után |
| DHOP-15 | Quantity selector component | ❌ DHOP-14 után (de reusable komponens, lehet előre is) |

**Megjegyzés DHOP-16-ról (availability toggle):** Ez az admin product management-tel (DHOP-38) szorosan össze van kötve. Implementálandó a 4. fázisban az adminnal együtt.

**Kimenet:** Customer böngészhet termékeket, szűrhet kategória szerint, product detail oldalon lát mindent.

**Fázis exit criteria:** Termékek betöltése < 2s staging-en; quantity selector működik mobilon; legalább 3 termék és 2 kategória feltöltve teszteléshez.

---

### 3. FÁZIS – Rendelési folyamat (2–3. hét)
**Cél:** A customer le tud adni egy rendelést. Ez az MVP magjának elkészítése.

**Miért ez a sorrend?** A cart (DHOP-18) az order schemától (DHOP-24) és a session-től (DHOP-12) függ. A checkout flow lépései egymásra épülnek — cart → summary → delivery form → confirmation → placement. Ezek nem párhuzamosíthatók egymással.

| Ticket | Feladat | Párhuzamos? |
|--------|---------|-------------|
| DHOP-18 | Shopping cart (add/remove/update) | ❌ DHOP-12 + DHOP-24 után |
| DHOP-19 | Cart summary view | ❌ DHOP-18 után |
| DHOP-20 | Delivery details form | ✅ Párhuzamos DHOP-19-cel (mindkettő DHOP-11 után) |
| DHOP-21 | Order confirmation screen | ❌ DHOP-19 + DHOP-20 után |
| DHOP-22 | Order placement (backend endpoint) | ❌ DHOP-21 + DHOP-24 után |
| DHOP-23 | Post-order thank you page | ❌ DHOP-22 után |

**Ez a fázis a legkritikusabb.** Ha DHOP-22 (order placement) nem stabil és idempotent, semmi más nem érdemes tesztelni. Erre kell a legtöbb tesztelési erőforrás.

**Kimenet:** Egy customer képes terméket választani, kosárba tenni, kiszállítási adatot megadni, megerősíteni és beküldeni a rendelést. Admin kap értesítést.

**Fázis exit criteria:** Teljes rendelési folyamat end-to-end tesztelve staging-en (mobilon); DHOP-22 idempotency tesztelve (dupla submit nem hoz létre dupla rendelést); rendelés megjelenik az admin panelen.

---

### 4. FÁZIS – Rendelés kezelés + Admin alap (3. hét)
**Cél:** Admin látja és kezeli a bejövő rendeléseket. Customer követi a rendelése állapotát.

**Miért most?** A rendelési folyamat (3. fázis) kész van, tehát már van mit kezelni. Az admin felület és az order lifecycle egymással párhuzamosan fejleszthető — mindkettő a DHOP-22 és DHOP-24 meglétét feltételezi.

| Ticket | Feladat | Párhuzamos? |
|--------|---------|-------------|
| DHOP-25 | Customer order history | ✅ Párhuzamos DHOP-34-gyel |
| DHOP-26 | Order detail view (customer) | ❌ DHOP-25 után |
| DHOP-27 | Status change by admin | ✅ Párhuzamos DHOP-28-cal |
| DHOP-28 | Status change by courier | ✅ Párhuzamos DHOP-27-tel |
| DHOP-34 | Admin login | ✅ Párhuzamos DHOP-25-tel |
| DHOP-35 | Orders dashboard (admin) | ❌ DHOP-34 után |
| DHOP-36 | Order detail & status management (admin) | ❌ DHOP-35 + DHOP-27 után |
| DHOP-37 | Customer list (admin) | ✅ Párhuzamos DHOP-35-tel |
| DHOP-38 | Product management (admin) | ✅ Párhuzamos DHOP-35-tel |
| DHOP-16 | Product availability toggle | ❌ DHOP-38 után (itt kerül be) |

**Megjegyzés:** DHOP-27 (admin status change) és DHOP-28 (courier status change) ugyanazt a backend validációs logikát használja — érdemes egyszerre implementálni, közös service-réteggel.

**Kimenet:** Admin be tud lépni, látja az összes rendelést, tud státuszt váltani, terméket kezelni. Customer látja a rendelése állapotát.

**Fázis exit criteria:** Admin teljes körű rendeléskezelési folyamat tesztelve (New Order → Delivered); customer oldali order history megjelenik; product availability toggle működik.

---

### 5. FÁZIS – Futárfelület (3–4. hét)
**Cél:** A futár a telefonján kezeli az összes kiszállítást.

**Miért a 4. fázis után?** A futár csak akkor tud dolgozni, ha (a) vannak rendelések (3. fázis) és (b) az admin már "Ready for Delivery" státuszba tette őket (4. fázis). Technikai dependency: DHOP-28 (courier status backend) kell a DHOP-33-hoz.

| Ticket | Feladat | Párhuzamos? |
|--------|---------|-------------|
| DHOP-29 | Courier login | ✅ Párhuzamos DHOP-30-cal (mindkettő DHOP-12 után) |
| DHOP-30 | Today's delivery list | ❌ DHOP-29 után |
| DHOP-31 | Delivery detail view | ❌ DHOP-30 után |
| DHOP-32 | Google Maps deep link | ✅ Párhuzamos DHOP-33-mal (mindkettő DHOP-31 után) |
| DHOP-33 | Mark as Delivered | ✅ Párhuzamos DHOP-32-vel |

**Kimenet:** Futár be tud lépni, látja a mai kiszállításait, meg tudja nyitni a navigációt, és le tudja zárni a kiszállítást. Rendelés státusza azonnal frissül.

**Fázis exit criteria:** Teljes futár-folyamat tesztelve mobilon valós körülmények között (vagy szimulálva); Google Maps deep link tesztelve Android és iOS rendszeren; státuszfrissítés < 2s.

---

### 6. FÁZIS – Admin kiegészítések + Analytics (4. hét)
**Cél:** Pilot KPI tracking, statisztikák, analytics integráció.

**Miért itt?** Ezek nem blokkolják az alapfunkcionalitást, de szükségesek a pilot kiértékeléséhez. Párhuzamosan fejleszthetők a futár-felülettel.

| Ticket | Feladat | Párhuzamos? |
|--------|---------|-------------|
| DHOP-39 | Statistics dashboard (admin) | ✅ Párhuzamos DHOP-42-vel |
| DHOP-42 | Basic analytics integration | ✅ Párhuzamos DHOP-39-cel |

**Kimenet:** Szabolcs naponta meg tudja nézni a pilot előrehaladását (regisztrációk, rendelések, visszatérők).

**Fázis exit criteria:** Analytics dashboard mutatja a pilot KPI-okat (regisztrációk, rendelések, avg basket value, visszatérő vásárlók); legalább 1 teszt rendelés átmegy az analytics funnel-en.

---

### 7. FÁZIS – Indítás előkészítés (4–5. hét)
**Cél:** Minden marketing és launch infrastruktúra készen áll. Az app live-ban van, és az akquisíciós csatornák aktívak.

**Fontos:** DHOP-43 (QR kódok) és DHOP-44 (Facebook CTA) csak akkor generálható le véglegesen, ha a domain DHOP-40-ben már végleges. Ezért ezek az utolsó fázisban vannak.

| Ticket | Feladat | Párhuzamos? |
|--------|---------|-------------|
| DHOP-43 | QR code generation | ✅ Párhuzamos DHOP-44-gyel |
| DHOP-44 | Facebook page CTA & launch post | ✅ Párhuzamos DHOP-43-mal |

**Kimenet:** QR kódok nyomtatásra kész állapotban. Facebook oldal frissítve. Launch poszt jóváhagyva és ütemezve.

**Fázis exit criteria (= Launch Go/No-Go checklist):** Production domain él HTTPS-en; QR kódok mobilon tesztelve (mindkét platform); Facebook bio frissítve; Szabolcs jóváhagyta a launch posztot; admin és futár felhasználók létrehozva production-ben.

---

## Összefoglaló táblázat

| Fázis | Hét | Tickets | Blokkoló? |
|-------|-----|---------|-----------|
| 0 – Alapok | 1. | DHOP-40, DHOP-24 | ✅ Minden más erre vár |
| 1 – Auth + Környezet | 1–2. | DHOP-41, DHOP-8, 10, 11, 12 (DHOP-9 optional) | ✅ Feature dev erre vár |
| 2 – Termékkatalógus | 2. | DHOP-13, 14, 15, 17 | Nem blokkolja a rendelési folyamatot |
| 3 – Rendelési folyamat | 2–3. | DHOP-18, 19, 20, 21, 22, 23 | ✅ Admin/futár erre vár |
| 4 – Order mgmt + Admin | 3. | DHOP-25, 26, 27, 28, 34, 35, 36, 37, 38, 16 | ✅ Futár erre vár |
| 5 – Futárfelület | 3–4. | DHOP-29, 30, 31, 32, 33 | Nem blokkolja az indítást |
| 6 – Analytics + Stats | 4. | DHOP-39, 42 | Nem blokkolja az indítást |
| 7 – Launch prep | 4–5. | DHOP-43, 44 | ✅ Indítás erre vár |

---

## Kritikus út (Critical Path)

A következő lánc a leghosszabb egymástól függő ticket-sorozat. Ha bármelyik csúszik, az egész launch csúszik:

```
DHOP-40 (hosting)
  → DHOP-41 (env config)
  → DHOP-8/9/10 (auth)
    → DHOP-12 (session)
      → DHOP-18 (cart)
    → DHOP-11 (profile)
      → DHOP-20 (delivery form)
  → DHOP-24 (order schema)
    → DHOP-22 (order placement) ← DHOP-21 ← DHOP-19 ← DHOP-18
      → DHOP-35 (orders dashboard)
        → DHOP-36 (order detail + status mgmt)
          → DHOP-27 (admin status change)
            → (customer notification → futár tud dolgozni)
```

---

## Javaslatok a csapatnak

**1. Ne kezdjetek feature-t infra és auth előtt.** A 0. és 1. fázis ugyan nem látványos, de nélkülük semmi nem tesztelhető end-to-end.

**2. DHOP-22 (order placement) a legfontosabb backend task.** Erre fordítsátok a legtöbb figyelmet és tesztelési időt. Idempotency és hibakezelés kritikus.

**3. DHOP-24 (order data model) design review szükséges.** Mielőtt bárki kódot ír, az egész csapat olvassa át és hagyja jóvá. Egy rosszul megtervezett séma komoly refactort okozhat.

**4. Facebook App Meta review — opcionális, post-MVP.** A Meta approval folyamata (email permission jóváhagyás) napokat vagy heteket vehet igénybe. Az MVP pilot Google OAuth-szal és email/password-del elindítható Facebook OAuth nélkül. Ha a Meta review elvégzésre kerül, az post-MVP feladat (DHOP-9 prioritása: Low).

**5. Domain véglegesítés.** A QR kódok csak a végleges domain után generálhatók. Minél hamarabb döntsük el a URL-t, annál kevesebb utolsó pillanatos munkát jelent.

**6. Pilot bevezetés sorrend:** Tesztelés → Soft launch (10-15 ismerős) → Kemény launch (Facebook + QR kódok). Ne engedjük 100 emberre egyszerre mielőtt az admin és a futár kipróbálta.
