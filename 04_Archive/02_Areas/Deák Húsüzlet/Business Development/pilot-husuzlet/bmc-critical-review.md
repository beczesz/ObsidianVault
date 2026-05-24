---
title: DHOP BMC v2.0 - Kritikus Felülvizsgálat
version: 1.0
date: 2026-03-28
author: Claude (operatív) + ChatGPT (stratégiai)
scope: Üzletfejlesztés - DHOP pilot
---

# DHOP BMC v2.0 — Kritikus Felülvizsgálat

**Módszer:** ChatGPT (stratégiai partner) + Claude (operatív feljegyző) közös elemzés
**Fókusz:** Hol törik el a modell a valóságban?
**Struktúra minden blokkban:** Unvalidált feltevés → Kritikus bottleneck → Kérdések Szabolcsnak

---

## Végső konklúzió (előre, mert fontos)

> A modell **nem marketingen** fog elbukni.
> A modell **nem pricingon** fog elbukni.
> **Hanem itt: Operáció + supply stabilitás.**

---

## 1. KEY RESOURCES × KEY PARTNERS
*(Supply Reliability Audit — a rendszer motorja)*

**Unvalidált feltevés:**
A Deák képes konzisztensen, skálázhatóan, operatívan stabilan kiszolgálni online rendeléseket. Ez jelenleg feltételezés, nem tény.

**Kritikus bottleneck:**
Single supplier dependency + nem standardizált operáció:
- nincs dedikált online fulfillment flow
- nincs validált kapacitás
- nincs fallback
- nincs SLA

**Kérdések Szabolcsnak:**

*Kapacitás:*
- Napi hány rendelést tudnak garantáltan kiszolgálni?
- Mi a max burst (pl. 1 órán belül 10 rendelés)?

*Készlet:*
- Van állandó készlet vagy napi termelés alapján működnek?
- Van külön "online rendelés" folyamat?

*Variabilitás:*
- Mennyire standard a súly / minőség rendelésenként?
- Hány % visszatérés / reklamáció jelenleg a boltban?

*Failure handling:*
- Mi történik, ha egy termék elfogy rendelés után?
- Mi történik, ha késik a kiszállítás?

*Governance:*
- Ki az egyetlen döntéshozó a két testvér közül?
- Ki mondja ki az "igen/nem"-et napi operatív szinten?

---

## 2. CUSTOMER SEGMENTS

**Unvalidált feltevés:**
Az első userek: digitális, időszűkében lévő 25-45 évesek.
Ez logikus feltevés — de nincs validálva.

**Kritikus bottleneck:**
Nincs bizonyítva, hogy ők akarnak online húst rendelni. Ez nem Amazon — itt bizalom, szokás és fizikai élmény dominál.

**Kérdések Szabolcsnak:**
- Ki vásárol most a boltban? (demográfia, hozzávetőleg)
- Hányan kérdeztek már házhozszállítást személyesen?
- Ki az, aki nem jön boltba időhiány miatt (van ilyen típus)?
- Van-e már most "telefonos rendelő" típusú vásárló?

---

## 3. VALUE PROPOSITION

**Unvalidált feltevés:**
Kényelem = a fő driver az első vásárlásnál.

**Kritikus bottleneck:**
Value prop mismatch — lehet, hogy nem kényelem a valódi mozgatórugó, hanem bizalom + minőség. Ha rosszul pozicionálunk: nem rendelnek, vagy nem térnek vissza.

**Kérdések Szabolcsnak:**
- Miért jönnek a jelenlegi vásárlók a boltba? (mit mondanak)
- Mi a legfontosabb nekik: ár / minőség / személyes kapcsolat?
- Mi az a konkrét fájdalom, amit most élnek át (pl. zsúfolt parkoló, sorbanállás)?

---

## 4. CHANNELS

**Unvalidált feltevés:**
Bolt + QR kód = elég az első 30 felhasználóhoz.

**Kritikus bottleneck:**
Konverzió a boltban: az eladó ajánlja-e aktívan? A vevő valóban beszkenneli-e?

**Kérdések Szabolcsnak:**
- Ki mondja el / mutatja meg a QR kódot a boltban?
- Van (lesz) script az eladóknak?
- Hány napi vásárló van átlagosan a 3 boltban összesen?
- Mi a becsült konverziós arány QR mutatás → regisztráció?

---

## 5. CUSTOMER RELATIONSHIPS

**Unvalidált feltevés:**
T+3 napos automatikus trigger visszahozza a felhasználót újravásárlásra.

**Kritikus bottleneck:**
Nincs bizonyított retention mechanizmus — ismeretlen, hogy mi triggereli a húsvásárlási szokást online környezetben.

**Kérdések Szabolcsnak:**
- Milyen gyakran vesz húst egy átlagos vásárló? (hetente? kéthetente?)
- Mi triggereli általában az újravásárlást (tudod-e)?
- Milyen csatornán érhetők el a vásárlók visszacsalogatáshoz: SMS, WhatsApp, email?

---

## 6. REVENUE STREAMS

**Unvalidált feltevés:**
5-12% sávos revenue share működni fog mindkét félnek.

**Kritikus bottleneck:**
Unit economics ismeretlen — nem tudni, hogy a revenue share fenntartható-e a Deák marginja alapján.

**Kérdések Szabolcsnak:**
- Mekkora az átlagos kosárérték a boltban jelenleg?
- Mekkora a jelenlegi bruttó margin a húsüzletnél (hozzávetőleg)?
- Mennyi revenue share fér bele a Deáknak realisztikusan?

---

## 7. KEY ACTIVITIES

**Unvalidált feltevés:**
3 core activity (rendelésfelvétel, fulfillment, kiszállítás) elegendő a launchhoz.

**Kritikus bottleneck:**
Execution gap — nincs validált dry run, nincs playbook, az operáció nincs betanítva.

**Kérdések Szabolcsnak:**
- Volt már valaha teszt rendelés (akár informálisan)?
- Mennyi idő egy rendelés teljes folyamata end-to-end (felvétel → kiszállítás)?
- Hol akadt el, amikor megpróbálták elképzelni a folyamatot?

---

## 8. COST STRUCTURE

**Unvalidált feltevés:**
12-13k EUR stop decision cap elegendő a validációhoz.

**Kritikus bottleneck:**
Runway vs. learning speed — ha lassan gyűlnek a tanulságok, a cap elfogy mielőtt dönteni lehet.

**Kérdések Szabolcsnak:**
- Mennyi ideig bírja az Exar Labs cashflow-ban ezt a projektet?
- Mi a maximális veszteség, amit még vállalsz hiba esetén?
- Mi az a mérföldkő, ami alapján leállítod (ha igen)?

---

## 9. PLATFORM VISION (LocalBasket)

**Unvalidált feltevés:**
A DHOP pilot modell skálázható más helyi termelőkre is.

**Kritikus bottleneck:**
Supply standardization hiánya — minden termelő más, a platform-logika csak akkor működik, ha valamilyen közös nevező van.

**Kérdések Szabolcsnak:**
- A Deák modellje mennyire "templatelhető" más termelőkre?
- Más potenciális supplier mennyire különböző operatívan?
- Ez most releváns kérdés, vagy csak DHOP sikere után?

---

## TOP 5 KRITIKUS KÉRDÉS (ChatGPT prioritizálása)

> Ha ezekre nincs válasz: nem launcholsz — csak reménykedsz.
> Ha ezek megvannak: valódi validáció indul.

1. **Napi hány rendelést tud stabilan kiszolgálni a Deák?**
2. **Mi történik, ha egyszerre 10 rendelés jön?**
3. **Ki az egyetlen döntéshozó a partner oldalon?**
4. **Van-e standard online fulfillment flow?**
5. **Mekkora az átlag kosárérték + jelenlegi margin?**

---

## Összesített nyitott kérdések Szabolcsnak

### Operáció & Supply (KRITIKUS)
1. Napi hány rendelést tudnak garantáltan kiszolgálni?
2. Mi a max burst kapacitás (pl. 1 óra alatt)?
3. Van állandó készlet vagy napi termelés?
4. Van dedikált online fulfillment folyamat?
5. Mennyire standard a súly/minőség rendelésenként?
6. Mi történik, ha elfogy egy termék rendelés után?
7. Mi történik, ha késik a kiszállítás?

### Governance (KRITIKUS)
8. Ki az egyetlen döntéshozó operatív szinten a két testvér közül?

### Vásárlók & Piac
9. Ki vásárol most a boltban (demográfia)?
10. Hányan kérdeztek már házhozszállítást?
11. Milyen gyakran vesz húst egy átlagos vásárló?
12. Mi a legfontosabb vásárlói driver: ár / minőség / kapcsolat?

### Értékesítési csatorna
13. Ki mutatja meg a QR kódot a boltban?
14. Van script az eladóknak?
15. Hány napi vásárló van összesen a 3 boltban?

### Pénzügyek
16. Mekkora az átlagos kosárérték jelenleg?
17. Mekkora a bruttó margin a húsüzletnél (hozzávetőleg)?
18. Mennyi revenue share fér bele a Deáknak?
19. Mennyi ideig bírja az Exar Labs cashflow-ban a projektet?

### Visszatérés & Retention
20. Mi triggereli az újravásárlást a vásárlóknál?
21. Milyen csatornán érhetők el (SMS/WhatsApp/email)?

---

_Összeállítva: 2026-03-28 | Claude + ChatGPT (Üzleti terv értékelés session)_
