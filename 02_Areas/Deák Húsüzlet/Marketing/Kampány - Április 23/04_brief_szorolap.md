---
title: "Design Brief — Szórólap A5 duplex"
deliverable: Founding 50 szórólap
format: 148×210mm (A5), duplex (eleje + hátoldal)
language: Magyar
date: 2026-04-22
reference: Marketing/szorolap/szorolap_v11_eleje.html, szorolap_v11_hatoldal.html
id: 62e9734b-6b54-4ac8-b189-2429f7c5d09a
index_schema_version: 1
---

# Design Brief: Szórólap — Founding 50

## Feladat

A meglévő v11-es szórólap alapján készíts egy frissített verziót, amely a Founding 50 programot kommunikálja. A v11 design-nyelve, színvilága és struktúrája a kiindulópont, de **Claude Design gondolja újra** a layoutot, tipográfiát és vizuális megoldásokat.

---

## Specifikáció

- **Méret:** 148 × 210 mm (A5, álló)
- **Oldalak:** 2 (eleje + hátoldal) — duplex nyomtatás
- **Nyomtatás:** Xerox VersaLink C7120 irodai nyomtató, A4-en 2×A5
- **Nyomtatási margó:** ~4mm non-printable area minden oldalon
- **Nyelv:** Magyar

---

## A meglévő v11 design összefoglaló

### Eleje (v11)
- Felső piros sáv (7mm, gradient #C0392B → #E74C3C)
- Deák Húsmíves logó (28mm, középre igazítva)
- Főcím: „Kézműves minőség" + csillag ikon
- Alcím: „Házhoz szállítjuk Székelyudvarhelyen"
- 4 érték-blokk ikonokkal (Frissen készül / Kézműves eljárás / Házhozszállítás / Gondosan kézzel)
- QR kód → deakhus.ro?source=qr
- Alsó piros sáv lábléc (Deák Húsmíves • Székelyudvarhely • www.deakhus.ro)

### Hátoldal (v11)
- „Amit NEM teszünk a húsunkba" — 6 kategória ipari adalékanyagokkal
- „Mit használunk?" info box
- „Kézműves minőség, ipari kompromisszumok nélkül." tagline
- Alsó piros sáv lábléc

---

## Founding 50 frissítés — mi változik

### Eleje — Founding 50 CTA hozzáadása

Az eleje megtartja az alap brand üzenetet, DE kiegészül a Founding 50 felhívással:

**Új elem — Founding 50 blokk (az érték-blokkok és a QR kód között, vagy alattuk):**

> **Legyél az első 50 alapító tag között!**
> Regisztrálj most, és 3 hónapig ingyenes kiszállítást kapsz.

**QR kód frissítés:**
- URL: `deakhus.ro?utm_source=qr_flyer&utm_medium=offline&utm_campaign=founding50`
- A QR alatti szöveg: „Szkenneld be és regisztrálj!" (a korábbi „Rendelj online!" helyett)

**Opcionális:** A 4 érték-blokk lehet 3-ra csökkentve, hogy helyet adjunk a Founding 50 blokknak.

### Hátoldal — maradhat a v11

A hátoldal („Amit NEM teszünk") maradhat változatlanul, mert:
- Ez önálló értéket ad (brand diferenciálás)
- Nem kampány-specifikus
- A vásárló megtartja a szórólapot emiatt

**VAGY** Claude Design javasolhat egy alternatív hátoldalt is, ha a Founding 50-nek több helyre van szüksége.

---

## Szövegek (pontos copy)

### Eleje:

**Logó felett/mellett:** (semmi, csak a logó)

**Főcím:**
> Kézműves minőség

**Alcím:**
> Házhoz szállítjuk Székelyudvarhelyen

**Érték-blokkok (3 vagy 4):**

| Ikon | Cím | Leírás |
|------|-----|--------|
| Nap/hajnal | Frissen készül | Minden termékünk aznap készül |
| Kéz | Kézműves eljárás | Hagyományos receptek, ipari adalékok nélkül |
| Ház/kocsi | Házhozszállítás | Online rendelés, aznapi kiszállítás |
| *(opcionális 4.)* | Gondosan, kézzel | 37 termék, mindegyik kézzel készítve |

**Founding 50 blokk:**
> **Legyél az első 50 alapító tag között!**
> Regisztrálj most a deakhus.ro oldalon,
> és 3 hónapig ingyenes kiszállítást kapsz.
> Csak 50 hely van.

**QR kód label:**
> Szkenneld be és regisztrálj!

**QR kód alatti URL:**
> www.deakhus.ro

**Lábléc:**
> Deák Húsmíves • Székelyudvarhely • www.deakhus.ro

### Hátoldal (változatlan v11):

(Lásd a teljes HTML-t: `Marketing/szorolap/szorolap_v11_hatoldal.html`)

---

## Technikai megjegyzések

1. **Duplex nyomtatás:** Flip-on-short-edge → a hátoldal 180°-kal forgatva kell legyen az A4 nyomtatási layout-on
2. **A4 layout:** 2×A5 egymás mellett, vágási vonalakkal, 96% scale a printer margó kompenzálásra
3. **Lábléc pozíció:** A szöveg a sáv felső harmadában legyen (`padding: 2.5mm 4mm 5mm 4mm`), mert az alsó ~2mm levágódik nyomtatáskor
4. **Font:** Sans-serif család (Segoe UI / Helvetica Neue / Arial)
5. **QR kód:** A kampány UTM-mel generálandó (founding50 campaign)
6. **A v11 HTML referencia fájlok a `Marketing/szorolap/` mappában vannak** — ezeket használd kiindulásnak

---

## Megjegyzések Claude Design-nak

1. **A v11 a kiindulópont, de gondold újra** — jobb layout, jobb tipográfia, jobb vizuális hierarchia
2. **A Founding 50 blokk legyen feltűnő de ne lógjon ki** — illeszkedjen a design nyelvbe
3. **Az „50" szám kaphat különleges vizuális kezelést** — nagyobb, más szín, dekoratív elem
4. **Ne legyen zsúfolt** — inkább kevesebb info, de jól olvasható
5. **Nyomtatásra kész legyen** — nem képernyőre optimalizálunk, hanem A5 papírra
6. **A hátoldalhoz is javasolhatsz alternatívát**, de a v11 hátoldal is maradhat
