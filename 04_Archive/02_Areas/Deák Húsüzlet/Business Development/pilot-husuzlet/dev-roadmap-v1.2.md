---
title: Development Roadmap – DHOP MVP
version: 1.2
date: 2026-03-25
author: Becze Szabolcs – Exar Labs
description: >
  v1.2: Architektúra változás — az admin/operátor felület (mészáros + futár) nem külön alkalmazás,
  hanem a fő PWA-n belüli külön nézet, role-based tab bar váltással (DHOP-52 Epic).
  DHOP-29 (Courier login) és DHOP-34 (Admin login) redundánssá váltak — törölt ticketek.
  DHOP-30–33 courier ticketek beolvadnak a DHOP-52 Epicbe.
  Új fázisok: 5 (Butcher & Courier Interface), 6 (Statisztikák + Analytics), 7 (UX Polish + GDPR).
  v1.1: DHOP-9 Facebook OAuth optional/post-MVP; phase exit criteria hozzáadva.
---

# Development Roadmap – DHOP MVP

_Version: 1.2 | Last updated: 2026-03-25_

---

## Áttekintés

Ez a roadmap meghatározza, hogy a Jira ticketek milyen sorrendben és fázisokban kerüljön implementálásra. A sorrend nem önkényes: a dependencia-lánc és a kockázatcsökkentés logikája diktálja.

**Alapelv:** Amit nem lehet párhuzamosan csinálni, azt sorban kell. Amit igen, párhuzamosan kell. A kritikus út: infrastruktúra → auth + adatmodell → katalógus → rendelési folyamat → admin/futár nézet → indítás.

### ⚠️ Architektúra változás (v1.2)

Az admin és futár felület **nem külön alkalmazás** — a fő Vue 3 PWA-n belüli külön nézet, amelyre a „Contul meu" oldalon lévő mode switcher (DHOP-67) vált át. A tab bar felváltódik:

- **Vásárló mód:** Produse · Coș · Comenzi · Cont
- **Operator mód:** Pregătire · Livrare · Statistici · Cont

Ebből következik:
- **DHOP-34 (Admin login) → TÖRÖLT** — ugyanaz az auth rendszer, role-based redirect kezeli
- **DHOP-29 (Courier login) → TÖRÖLT** — ugyanaz az auth rendszer, role-based redirect kezeli
- **DHOP-30–33** courier ticketek → beolvadnak a **DHOP-52 Epicbe** (5. fázis)

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

### 4. FÁZIS – Rendeléskezelés + Admin operátor nézet (3. hét)

**Cél:** A rendelések kezelhetők az operátor módból. Customer követi a rendelése állapotát.

**Architektúra változás (v1.2):** Az admin felület **nem külön app** — a főappba épített operátor nézetből érhető el, role-based tab bar váltással. A **DHOP-34 (Admin login) ticket törölt** — az auth (DHOP-12) a role alapján automatikusan elérhetővé teszi az operátor módot a Contul meu-ból.

**Miért most?** A rendelési folyamat (3. fázis) kész, tehát már van mit kezelni. Az admin nézet és az order lifecycle egymással párhuzamosan fejleszthető — mindkettő a DHOP-22 és DHOP-24 meglétét feltételezi.

| Ticket      | Feladat                           | Párhuzamos?                            |
| ----------- | --------------------------------- | -------------------------------------- |
| DHOP-25     | Customer order history            | ✅ Párhuzamos DHOP-35-tel               |
| DHOP-26     | Order detail view (customer)      | ❌ DHOP-25 után                         |
| DHOP-27     | Status change by admin            | ✅ Párhuzamos DHOP-28-cal               |
| DHOP-28     | Status change by courier          | ✅ Párhuzamos DHOP-27-tel               |
| ~~DHOP-34~~ | ~~Admin login~~                   | 🚫 **TÖRÖLT** — role-based auth kezeli |
| DHOP-35     | Orders dashboard (operátor nézet) | ✅ Párhuzamos DHOP-25-tel               |
| DHOP-36     | Order detail & status management  | ❌ DHOP-35 + DHOP-27 után               |
| DHOP-37     | Customer list (admin)             | ✅ Párhuzamos DHOP-35-tel               |
| DHOP-38     | Product management (admin)        | ✅ Párhuzamos DHOP-35-tel               |
| DHOP-16     | Product availability toggle       | ❌ DHOP-38 után                         |

**Megjegyzés:** DHOP-27 (admin status change) és DHOP-28 (courier status change) ugyanazt a backend validációs logikát használja — érdemes egyszerre implementálni, közös service-réteggel.

**Kimenet:** Admin role-lal rendelkező felhasználó az operátor módba váltva látja az összes rendelést, tud státuszt váltani, terméket kezelni. Customer látja a rendelése állapotát.

**Fázis exit criteria:** Admin teljes körű rendeléskezelési folyamat tesztelve (New Order → Delivered); customer oldali order history megjelenik; product availability toggle működik; operátor mód elérhető a Contul meu-ból.

---

### 5. FÁZIS – Butcher & Courier Operational Interface (3–4. hét)

**Cél:** A mészáros és a futár a telefonján kezeli az előkészítést és a kiszállításokat — az ugyanazon appba épített operátor nézetből.

**Architektúra (v1.2):** Ez a fázis a **DHOP-52 Epic** implementációja. Nincs külön app, nincs külön login. A **DHOP-29 (Courier login) ticket törölt** — az auth (DHOP-12) role-based módon adja az elérést. A korábban önálló DHOP-30–33 courier ticketek beolvadnak ebbe az epicbe.

A felület 3 tabból áll (+ állandó Cont tab):
- 🔪 **Pregătire** — mészáros nézet
- 🚚 **Livrare** — futár nézet
- 📊 **Statistici** — operátori statisztikák

**Státusz flow:**
```
Új rendelés → Előkészítés alatt → Kiszállításra kész → Úton van → Kézbesítve → Lezárva
```

#### Mészáros nézet (Pregătire tab)

| Ticket | Feladat | Párhuzamos? |
|--------|---------|-------------|
| DHOP-53 | Mészáros + futár role hozzáadása az auth rendszerhez | ✅ Párhuzamos DHOP-54-gyel |
| DHOP-54 | Role switcher tab bar UI (Pregătire/Livrare/Statistici/Cont) | ❌ DHOP-53 után |
| DHOP-55 | Mészáros – napi rendelési lista (Screen 1) | ❌ DHOP-54 után |
| DHOP-56 | Mészáros – rendelés előkészítési nézet (Screen 2) | ❌ DHOP-55 után |
| DHOP-57 | „Kiszállításra kész" státuszgomb (Screen 2 akció) | ❌ DHOP-56 + DHOP-27 után |
| DHOP-58 | Termék elérhetőség toggle (Screen 3) | ✅ Párhuzamos DHOP-55-tel (DHOP-38 után) |

#### Futár nézet (Livrare tab)

| Ticket | Feladat | Párhuzamos? | Megjegyzés |
|--------|---------|-------------|-----------|
| ~~DHOP-29~~ | ~~Courier login~~ | 🚫 **TÖRÖLT** | role-based auth kezeli |
| DHOP-30 | Napi kiszállítási lista (Screen 4) | ✅ Párhuzamos DHOP-55-tel | korábban önálló ticket |
| DHOP-31 | Kiszállítás részletei (Screen 5) | ❌ DHOP-30 után | |
| DHOP-32 | Google Maps deep link (Screen 5 akció) | ✅ Párhuzamos DHOP-33-mal | |
| DHOP-33 | Kézbesítés megerősítése – Mark as Delivered (Screen 6) | ✅ Párhuzamos DHOP-32-vel | |

**Kimenet:** Mészáros látja a napi rendeléseket, le tudja zárni az előkészítést. Futár látja a kiszállításait, meg tudja nyitni a navigációt, le tudja zárni a kézbesítést. Státuszok azonnal frissülnek.

**Fázis exit criteria:** Teljes mészáros-folyamat tesztelve (Új rendelés → Kiszállításra kész); teljes futár-folyamat tesztelve mobilon (Kiszállításra kész → Kézbesítve); Google Maps deep link tesztelve Android és iOS rendszeren; státuszfrissítés < 2s.

---

### 6. FÁZIS – Statisztikák + Analytics (4. hét)

**Cél:** Pilot KPI tracking — mind az operátor saját munkájának visszajelzője, mind Szabolcs admin szintű áttekintője.

**Két réteg:**
- **Operátori statisztikák** (DHOP-59–61): a Statistici tab a butcher-courier felületen — a mészáros/futár saját napi/heti/havi adatai
- **Admin analytics** (DHOP-39, DHOP-42): pilot KPI dashboard Szabolcs számára

| Ticket | Feladat | Párhuzamos? |
|--------|---------|-------------|
| DHOP-59 | Statistici tab – PeriodSelector + összesítő kártyák (Screen 7) | ✅ Párhuzamos DHOP-60-nal |
| DHOP-60 | Statistici tab – Oszlopdiagram heti/havi nézetben (Screen 7) | ✅ Párhuzamos DHOP-59-cel |
| DHOP-61 | Statistici tab – Rendelési lista adott időszakra (Screen 8) | ❌ DHOP-59 + DHOP-60 után |
| DHOP-39 | Statistics dashboard (admin pilot KPI nézet) | ✅ Párhuzamos DHOP-42-vel |
| DHOP-42 | Basic analytics integration | ✅ Párhuzamos DHOP-39-cel |

**Kimenet:** Szabolcs naponta meg tudja nézni a pilot előrehaladását (regisztrációk, rendelések, visszatérők). Az operátor látja a saját teljesítményét.

**Fázis exit criteria:** Analytics dashboard mutatja a pilot KPI-okat; legalább 1 teszt rendelés átmegy az analytics funnel-en; Statistici tab heti/napi/havi nézetben működik.

---

### 7. FÁZIS – UX Polish + Bug fixes + GDPR (4. hét)

**Cél:** Az app launch-ready állapotba kerül — vizuális hibák javítva, GDPR-megfelelőség biztosítva, verziózás és admin mód váltó implementálva.

**Miért itt?** Ezek a ticketek nem blokkolják az alap funkcionalitást, de launch előtt kötelezők — különösen a GDPR (személyes adatok kezelése jogi kötelezettség) és az admin mode switcher (DHOP-67, amely a teljes operátor hozzáférés belépési pontja).

| Ticket | Feladat | Párhuzamos? |
|--------|---------|-------------|
| DHOP-63 | Bug: Frappe default login branding → Deák specifikus | ✅ Párhuzamos a többivel |
| DHOP-64 | CR: PrimaryButton min-height 56px + primary color (#9B2335) minden screenen | ✅ Párhuzamos |
| DHOP-65 | Bug: Mobile zoom letiltása (viewport meta tag) | ✅ Párhuzamos |
| DHOP-66 | FR: Contul meu – Verzió szekció (v0.1.23) + Contact mailto link | ✅ Párhuzamos |
| DHOP-67 | FR: Admin operator mód váltó – Contul meu tab bar csere | ❌ DHOP-53 + DHOP-54 után |
| DHOP-68 | FR: GDPR consent képernyő regisztráció után + Privacy Policy oldal | ✅ Párhuzamos |
| DHOP-69 | FR: Adattörlési lehetőség a Contul meu oldalon (GDPR Art. 17) | ❌ DHOP-68 után |

**Megjegyzés DHOP-67-ről:** Ez a ticket az egész operátor mód belépési pontja a vásárlói appból. Csak akkor implementálható, ha a DHOP-54 (tab bar infrastructure) és DHOP-53 (role auth) már készen van.

**Kimenet:** Az app vizuálisan konzisztens, mobilon zoom nélkül használható, GDPR-kompatibilis, az admin mode switcher működik.

**Fázis exit criteria:** Minden vizuális bug javítva; GDPR consent flow tesztelve új regisztrációnál; admin mode switcher működik Admin role-lal; verzió és contact megjelenik Contul meu-on.

---

### 8. FÁZIS – Indítás előkészítés (4–5. hét)

**Cél:** Minden marketing és launch infrastruktúra készen áll. Az app live-ban van, és az akquisíciós csatornák aktívak.

**Fontos:** DHOP-43 (QR kódok) és DHOP-44 (Facebook CTA) csak akkor generálható le véglegesen, ha a domain DHOP-40-ben már végleges.

| Ticket | Feladat | Párhuzamos? |
|--------|---------|-------------|
| DHOP-43 | QR code generation | ✅ Párhuzamos DHOP-44-gyel |
| DHOP-44 | Facebook page CTA & launch post | ✅ Párhuzamos DHOP-43-mal |

**Kimenet:** QR kódok nyomtatásra kész állapotban. Facebook oldal frissítve. Launch poszt jóváhagyva és ütemezve.

**Fázis exit criteria (= Launch Go/No-Go checklist):** Production domain él HTTPS-en; QR kódok mobilon tesztelve (mindkét platform); Facebook bio frissítve; Szabolcs jóváhagyta a launch posztot; admin és futár felhasználók létrehozva production-ben.

---

## Összefoglaló táblázat

| Fázis | Hét | Fő ticketek | Blokkoló? |
|-------|-----|------------|-----------|
| 0 – Alapok | 1. | DHOP-40, DHOP-24 | ✅ Minden más erre vár |
| 1 – Auth + Környezet | 1–2. | DHOP-41, 8, 10, 11, 12 (DHOP-9 optional) | ✅ Feature dev erre vár |
| 2 – Termékkatalógus | 2. | DHOP-13, 14, 15, 17 | Nem blokkolja a rendelési folyamatot |
| 3 – Rendelési folyamat | 2–3. | DHOP-18, 19, 20, 21, 22, 23 | ✅ Admin/futár erre vár |
| 4 – Rendeléskezelés + Admin nézet | 3. | DHOP-25, 26, 27, 28, 35, 36, 37, 38, 16 | ✅ Operátor interface erre vár |
| 5 – Butcher & Courier Interface | 3–4. | DHOP-52 Epic: 53–58, 30–33 | ✅ Statistici + DHOP-67 erre vár |
| 6 – Statisztikák + Analytics | 4. | DHOP-59, 60, 61, 39, 42 | Nem blokkolja az indítást |
| 7 – UX Polish + GDPR | 4. | DHOP-63–69 | ✅ Launch előtt kötelező |
| 8 – Launch prep | 4–5. | DHOP-43, 44 | ✅ Indítás erre vár |

### Törölt ticketek

| Ticket | Ok |
|--------|----|
| DHOP-29 (Courier login) | Redundáns — ugyanaz az app, role-based auth kezeli |
| DHOP-34 (Admin login) | Redundáns — ugyanaz az app, role-based auth kezeli |

---

## Kritikus út (Critical Path)

A következő lánc a leghosszabb egymástól függő ticket-sorozat. Ha bármelyik csúszik, az egész launch csúszik:

```
DHOP-40 (hosting)
  → DHOP-41 (env config)
  → DHOP-8/10 (auth)
    → DHOP-12 (session + role routing)
      → DHOP-18 (cart)
      → DHOP-53 (butcher/courier role) ← új kritikus út ág
        → DHOP-54 (tab bar switcher)
          → DHOP-67 (admin mode switcher – Contul meu)
    → DHOP-11 (profile)
      → DHOP-20 (delivery form)
  → DHOP-24 (order schema)
    → DHOP-22 (order placement) ← DHOP-21 ← DHOP-19 ← DHOP-18
      → DHOP-35 (orders dashboard)
        → DHOP-36 (order detail + status mgmt)
          → DHOP-27/28 (status change)
            → DHOP-57 (Kiszállításra kész gomb)
            → DHOP-33 (Mark as Delivered)
```

---

## Javaslatok a csapatnak

**1. Ne kezdjetek feature-t infra és auth előtt.** A 0. és 1. fázis ugyan nem látványos, de nélkülük semmi nem tesztelhető end-to-end.

**2. DHOP-22 (order placement) a legfontosabb backend task.** Erre fordítsátok a legtöbb figyelmet és tesztelési időt. Idempotency és hibakezelés kritikus.

**3. DHOP-24 (order data model) design review szükséges.** Mielőtt bárki kódot ír, az egész csapat olvassa át és hagyja jóvá. Egy rosszul megtervezett séma komoly refactort okozhat.

**4. DHOP-53 (role auth) és DHOP-54 (tab bar) az operátor interface alapja.** Mindkét mészáros, futár és admin feature ezektől függ — DHOP-67 (mode switcher) sem implementálható nélkülük.

**5. Facebook App Meta review — opcionális, post-MVP.** A Meta approval folyamata napokat vagy heteket vehet igénybe. Az MVP pilot Google OAuth-szal és email/password-del elindítható Facebook OAuth nélkül (DHOP-9 prioritása: Low).

**6. Domain véglegesítés.** A QR kódok csak a végleges domain után generálhatók. Minél hamarabb döntsük el a URL-t, annál kevesebb utolsó pillanatos munkát jelent.

**7. Pilot bevezetés sorrend:** Tesztelés → Soft launch (10-15 ismerős) → Kemény launch (Facebook + QR kódok). Ne engedjük 100 emberre egyszerre mielőtt az admin és a futár kipróbálta.
