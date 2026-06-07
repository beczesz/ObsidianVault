---
title: "F6 — Web redesign · 4 variáns"
date: 2026-05-12
author: Becze Szabolcs
status: active
description: "TransOffice Trade SRL 2025-ös weboldaláról szóló négy HTML-verzió koncepció: modern B2B-kék, klasszikus barna-navy, erdélyi téglavörös-zöld-sárga, és saját lila-sárga kontrasztos variáns. Mindegyik önálló HTML-fájl 22 év, AFM zöld projektcélok és csapatwizuális tartalommal,"
description_source: auto
description_hash: f052b7d5c3b8f955
id: 8d09432c-ab61-4b19-9020-52bb7fdfc609
index_schema_version: 1
bdos_index: true
---
# F6 — Web redesign · 4 variáns
## TransOffice Trade SRL — 2025 új weboldal-koncepciók

> **Forrás:** `Marketing/honlap_szoveg_2012.docx` (a régi 2012-es szöveg) + a teljes F1-F5 munkamenet (TransOffice profilja + AFM proiekt)
> **Generálva:** 2025 · 4 független HTML, mind self-contained (inline CSS, nincs külső dependency)
> **Cél:** A Marton-féle "kínosan retró" 2012-es oldalt cserélni egy modern, márkás digitális arccal.

---

## Áttekintés

| # | Variáns | Hangulat | Célközönség | Fő szín | Ki dönt? |
|---|---|---|---|---|:---:|
| 1 | **Modern (kék B2B)** | Tiszta, professzionális, SaaS-szerű | Tech-érdeklődő KKV-k, IT-cégek (InfoProg, DataSoft) | #1976d2 kék | Márton |
| 2 | **Klasszikus** | Konzervatív, megbízhatóság, intézményi | Önkormányzatok (Felsőboldogfalva, Primării), ügyvédi irodák, kórház | #6b4d28 sötét barna + #2c4870 navy | Márton |
| 3 | **Erdélyi (helyi)** | Meleg, családi, közösségi, kétnyelvű | Helyi vállalkozók, magyar nyelvű ügyfelek, Hegyi Zoli-szerű partner | #b84e2d téglavörös + #3a4d34 sötétzöld + #f0c14a sárga | Márton |
| 4 | **Saját variáns** (kontrasztos) | Energikus, lila-sárga, "growth-mindset" | Fiatal startup-okat tárgyaló cég, márka-előretörés | #6b2db3 lila + #fbcb35 napsárga | dry-run output |

---

## A 4 variáns közös elemei

Mindegyik tartalmazza:
- ✅ **Hero szekció** TransOffice névvel + pozícionálási mondattal
- ✅ **22 év / 28 ügyfél / 24h kiszállítás / 12 fő** trust-számok
- ✅ **3 szolgáltatás-kártya** (papír, kiszállítás, bútor)
- ✅ **AFM Mobilitate Verde 2025 proiekt szekció** (2 e-vehicul + 1 AC + 5,2 t CO₂/év)
- ✅ **Csapat / Despre noi** (Márton, Enikő, Attila, Operations Manager)
- ✅ **Kapcsolat** (Calea Băieșenilor 22, 0266-218945, contact@transoffice.ro)
- ✅ **Felelős mobile-design** (≥ 880px breakpoint)

---

## A variánsok közti **különbségek**

### Variáns 1 — Modern
- **Tipográfia:** Inter / system-ui sans-serif
- **AFM banner:** zöld gradiens (Forest), elkülönített szekció
- **Hierarchia:** info-architektúra (badges, eyebrow-labels, CTA primaer/secondary)
- **Mobilre:** összecsukós, tiszta scroll

### Variáns 2 — Klasszikus
- **Tipográfia:** Palatino / Georgia szerifelt
- **Római számok** szekciók-számára (I, II, III, MMIII, MMXXV)
- **Quote-box** Márton magyar nyelvű idézettel
- **Ornament** (❦ szimbólumok) hero-ban
- **Színek:** krém-háttér + barna nyomtatás + navy heading-ek

### Variáns 3 — Erdélyi
- **Tipográfia:** Lora (modern szerif, magyar diakritika-barát)
- **Magyar-román kétnyelvű strapline** (Helyi cég · Helyi szállítás · Udvarhely)
- **Színpaletta:** téglavörös / sötétzöld / napsárga (autentikus szász-székely kerámia inspirációból)
- **Csapat-leírás kétnyelvű** ("Heti 3 nap, de bármikor visszahív")
- **AFM-card aranykarika ikonnal**, közösségi tónussal ("Reggeli 8 és este 6 között bárki használhatja...")
- **Drop-shadow blokkok** (kézzelfogható, prospekt-szerű hatás)

### Variáns 4 — Saját (kontrasztos)
- **Tipográfia:** Manrope (modern, geometrikus)
- **Hero közvetlenül az AFM projektből indít** ("Most már elektromosan is" — az eredeti 2012-es szöveg semleges marad helyette)
- **Sticky header** lila háttérrel, **sárga CTA** kontraszttal
- **Lebegő "Hívjon most" gomb** mobilon
- **Quote-box dark mode** (sárga szöveg sötét lilán)
- **AFM-checklist** sárga kártyán → action-oriented dizájn

---

## Költségbecslés (a Márton-féle "kérni kell árajánlatot weboldalra" sorra)

| Mód | Idő | Költség |
|---|---|---|
| Tervezőiroda (Kolozsvár / Marosvásárhely) | 4-6 hét | 8 000 – 18 000 RON |
| Freelance designer + fejlesztő | 2-4 hét | 3 500 – 7 000 RON |
| AI-asszisztált (mint most a 4 variáns) | 1 nap | < 500 RON (Claude Pro 90 RON/hó) |

**A 4 HTML variáns most kész**, csak Mártonra vár a választás. Bárhol hosztolható (GitHub Pages, Netlify, vagy egy egyszerű VPS).

---

## Mit nem tartalmaz (és miért nem)

- ❌ **CMS-integráció** (WordPress, Strapi) — KKV-ként nem szükséges, az évi 4-6 frissítés HTML-ben is megoldható
- ❌ **Online webshop** — a TransOffice B2B és szerződéses, nem retail
- ❌ **Cookie-banner / GDPR** — nincs tracking, nincs analytics; egyszerű kapcsolatfelvétel
- ❌ **Animációk** (a 2012-es oldal sok mozgó GIF-jétől szándékosan elhatárolódik)

---

## F6.2 — Diktálási példa a saját variáns elkészítéséhez

A 4. variáns így keletkezett (példa, ahogy egy résztvevő diktálhat a Cowork-nek):

> **Diktálás:**
> "Vedd a 3-as erdélyi variánst alapul. Tedd lila-sárga kontrasztba: a tégla-zöld helyett sötét lila (#1a0e2a, #6b2db3) és napsárga (#fbcb35). A hero-ban vidd előre az AFM projektet — ne csak 3 szekcióval lejjebb legyen. Adj hozzá egy lebegő 'Hívjon most' gombot mobilra. Magyar szlogen legyen: 'Erdély logisztikai partnere'. A többi szerkezet maradjon (csapat, szolgáltatások, kapcsolat). HTML egyetlen fájlban, inline CSS-szel, magyar+román szöveg mix maradhat."

→ **Eredmény:** `variant_4_sajat_kontrasztos.html` — 264 sor, kész.
