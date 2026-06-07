---
title: "Design Brief — Landing Page Hero Banner"
description: "Design specification for a hero banner promoting Deák Húsüzlet's Founding 50 program on their landing page, with desktop (1440×600px) and mobile (375×500px) layouts, featuring headline, discount offer, availability counter, and CTA button in Hungarian, implemented as CSS-based responsive component rather than static image."
description_source: auto
description_hash: 50166e879f6470ba
deliverable: deakhus.ro hero section
format: 1440×600px (desktop) + 375×500px (mobile)
language: Magyar
date: 2026-04-22
id: 22631def-dca3-4b82-9be8-42cf29979086
index_schema_version: 1
---
# Design Brief: Hero Banner — Founding 50

## Feladat

Készíts egy hero banner designt a deakhus.ro landing oldalához, ami a Founding 50 programot kommunikálja. Ez az első dolog, amit a látogató lát — a konverzió itt kezdődik.

---

## Specifikáció

- **Desktop:** 1440 × 600 px (full-width, fix height)
- **Mobile:** 375 × 500 px (full-width, taller)
- **Formátum:** PNG / JPG + CSS layout javaslat
- **Nyelv:** Magyar
- **Kontextus:** A banner felett a Frappe webapp navigáció van, alatta a termék katalógus

---

## Tartalom / Copy

### Desktop layout elemek:

**Bal oldal (szöveg):**

Főcím:
> Legyél az első 50
> alapító tag között

Alcím:
> Regisztrálj most, és 3 hónapig ingyenes
> kiszállítást kapsz minden rendelésedre
> Székelyudvarhely területén.

Counter:
> ▢ / 50 hely elérhető

CTA gomb:
> Csatlakozom most

Kis megjegyzés:
> 37 kézműves termék • Aznap készül • Házhoz szállítjuk

**Jobb oldal (vizuális):**
- Opció 1: Stilizált illusztráció / fotó kézműves húskészítményekről
- Opció 2: Absztrakt minta a Deák brand színekkel
- Opció 3: A „50" szám dekoratív megjelenítése

### Mobile layout:
- Vertikális stack: cím → alcím → counter → CTA
- Vizuális elem háttérbe vagy elhagyva (a szöveg fontosabb mobilon)

---

## Megjegyzések Claude Design-nak

1. **A banner a Frappe webapp-ba kerül** — a design illeszkedjen egy Vue.js PWA-hoz
2. **A CTA gomb legyen kontrasztos** — ez a fő konverziós elem
3. **A counter dinamikus lesz** — a szám API-ból jön, de a design fix helyet biztosítson neki
4. **Mobilon az olvashatóság az elsődleges** — kisebb képernyőn a szöveg kell domináljon
5. **A Founding 50 modal (DH-153) külön UI elem** — a hero banner NE legyen modal, hanem fix section
6. **Ne használj stock fotót** — inkább grafikus/illusztratív megoldás vagy tiszta tipográfia
7. **A design legyen implementálható CSS-ben** — nem statikus kép lesz, hanem kódolt section
