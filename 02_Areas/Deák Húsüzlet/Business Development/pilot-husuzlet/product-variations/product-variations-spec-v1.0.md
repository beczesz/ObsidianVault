---
title: "Termék testreszabás és preferencia mentés — Feature Spec"
version: 1.0
date: 2026-05-07
author: Szabolcs (Exar Labs) + Cowork session
status: DRAFT v1.0 — termelői meeting után konszolidált
sprint: "Sprint 4"
jira_ticket: "DH-173"
prerequisite: "DH-183 (DONE)"
folder: "Business Development/pilot-husuzlet/product-variations/"
predecessor: "savings-engine/Ideas/v0.4-product-preferences-spec.md (v0.1)"
description: >
  Termékenkénti opciók (pácolt/pácolatlan, szeletelés, zsírosság, méret, alapanyag stb.)
  kiválasztása rendeléskor + preferenciák mentése per user per termék + automatikus
  alkalmazás újrarendelésnél. „A hentes beszélgetés digitalizálása."
id: 44cb466d-f5a3-4d0d-86c3-b14ab299d391
index_schema_version: 1
---

# Termék testreszabás és preferencia mentés — Feature Spec v1.0

> **Jira:** [DH-173](https://exarlabs.atlassian.net/browse/DH-173) | **Sprint:** 4 | **Status:** To Do
> **Prerequisite:** DH-183 (DONE — terméktípusok modellezése)

---

## 1. Probléma és hipotézis

### Probléma

Egy hagyományos kézműves húsüzletben a mészáros **ismeri a törzsvásárlót**:
- Tudja, hogy Kati néni a darált húst soványabban szereti
- Hogy a karajt vékonyra szeletelve kéri
- Hogy a csülköt mindig pácolatlanul viszi

Ez a **személyes kapcsolat versenyelőny**. De az online rendelés jelenlegi verziójában **teljesen hiányzik**:
- A vásárló nem tudja megadni, hogyan készítsék elő a terméket
- A rendszer nem emlékszik a korábbi választásaira
- Minden rendelés „idegen" érzésű marad

### Hipotézis

Ha a rendszer **digitalizálja a hentes beszélgetést** — termékenként relevant opciókat kínál, és emlékszik a választásokra — akkor:

- **G1**: ≥60% rendelésnél legalább 1 opció kiválasztva (30 napon belül beta után)
- **G2**: 2.+ rendelésnél az előző választás automatikusan default-ként megjelenik
- **G3**: Reorder flow-ban 0 extra kattintás a visszatérő preferenciáknál
- **G4**: Kvalitatív feedback a beta-ban: „itt ismernek engem"
- **G5**: Mészáros admin nézeten egyértelmű utasítást kap

**Ez a DH legerősebb retention drivere lehet** — a váltási költség nő, a visszatérés természetessé válik.

---

## 2. Az opció-típus modell (4 típus, admin-konfigurálható)

| Type                | UI elem                      | Példa termék                                             | Példa értékek                             |
| ------------------- | ---------------------------- | -------------------------------------------------------- | ----------------------------------------- |
| **`single_select`** | Radio gombok / chip selector | Sertés Csülök → Méret                                    | kisebb / közepes / nagyobb                |
| **`single_select`** | Radio gombok                 | Sertés Csontos Karaj → Pácolás                           | nem_pacolt / hagyomanyos / barbecue       |
| **`multi_level`**   | Cascading selectors          | (Future: Szeletelés egész vs vékony/közepes/vastag)      | egész / szeletelt → vékony/közepes/vastag |
| **`text`**          | Text input (max 100 char)    | (Future: Egyéb megjegyzés a mészárosnak)                 | "Vékonyabb szeletet kérek"                |

> **Megjegyzés (2026-05-07):** A `multi_level` és `text` típusokat MD szinten támogatjuk de az aktuális 15 terméken **csak `single_select` van használva**. Ez egyszerűsíti a Phase 1-et.

---

## 3. A 15 termék mátrixa (összefoglaló)

> **Részletes per-termék lista:** `product-options-matrix-v1.0.md`

| # | Termék | Kód | Opciók | Variation count |
|---|--------|-----|--------|-----------------|
| 1 | Sertés nyakaskaraj | 014 | Forma + Pácolás | 5 érték |
| 2 | Sertés Csontos Karaj | 016 | Pácolás | 3 érték |
| 3 | Sertés Csülök | 007 | Méret | 3 érték |
| 4 | Sertés Fehér Karaj | 015 | Szeletelés + Pácolás | 5 érték |
| 5 | Sertés Hasrész Csontnélkül | 019 | Szeletelés + Pácolás | 5 érték |
| 6 | Sertés Oldalas | 020 | Szeletelés + Pácolás | 5 érték |
| 7 | Sertés Őrölt Hús | 902 | Zsírosság (csak — alapanyag később) | 3 érték |
| 8 | Füstölt Csülök | 945 | Méret | 3 érték |
| 9 | Füstölt Csülök Csont Nélkül | 945.1 | Méret | 3 érték |
| 10 | Füstölt Fehér Karaj | 949 | Vastagság | 3 érték |
| 11 | Füstölt Has | 946 | Vastagság + Pácolás | 6 érték |
| 12 | Füstölt Nyakas Karaj | 948 | Szeletelés | 2 érték |
| 13 | Házi Szalámi | 991 | Vastagság | 3 érték |
| 14 | Sertés Szalámi | 917 | Vastagság | 3 érték |
| 15 | Téli Szalámi | 9904 | Vastagság | 3 érték |
| | | | **15 termék** | **~59 érték** |

**A maradék 31 termék** (a 46-ból) NEM rendelkezik DH-173 opciókkal — ezeket a vásárló simán kilóra/db rendel.

---

## 4. User Stories

### Vásárló perspektíva

**US-1 — Opció-választás**
> Mint vásárló, amikor egy terméket a kosárba teszek, szeretném látni a releváns opciókat („Cum să-ți pregătim?") és kiválasztani a preferenciámat, mielőtt hozzáadom.

**US-2 — Visszatérő preferencia**
> Mint visszatérő vásárló, amikor ugyanazt a terméket újra megnyitom, a rendszer ajánlja fel az előző választásomat default-ként, „Ultima ta alegere" jelzéssel.

**US-3 — Reorder kompatibilitás**
> Mint vásárló, amikor az „Újrarendelem" gombot használom (DH-120), a korábbi rendelés preferenciái automatikusan betöltődjenek minden terméknél.

**US-4 — Kosár nézet**
> Mint vásárló, a kosárban látni akarom a kiválasztott opciókat minden terméknél (pl. „Sertés comb — 1 kg — *feliat subțire · marinate*").

**US-5 — Default érvényes**
> Mint vásárló, ha nem akarok opciót választani, a rendszer egy ésszerű default-ot alkalmazzon és ne blokkolja a rendelést.

### Admin / Mészáros perspektíva

**US-6 — Admin konfiguráció**
> Mint admin, termékenként be akarom állítani, milyen opciók érhetők el (Frappe DocType-on keresztül), és ezek értékeit.

**US-7 — Mészáros munkalap**
> Mint mészáros, a rendelés részletezőben világosan látni akarom a vásárló preferenciáit, hogy tudjam, hogyan készítsem elő a terméket — nyomtatható formátumban.

---

## 5. UX flow

### 5.1 Termékdetail oldal — opció-választó

A „Kosárba" gomb előtt jelenik meg a `Cum să-ți pregătim?` szekció, ha a terméknek vannak opciói:

```
┌─────────────────────────────────────────┐
│ Cum să-ți pregătim?                     │
├─────────────────────────────────────────┤
│ Forma                                   │
│ ◉ Simplă         ◯ Dublă                │
│                                         │
│ Marinare                                │
│ ◉ Nemarinate  ◯ Tradițional  ◯ Barbecue │
└─────────────────────────────────────────┘
        ┌────────────────┐
        │  Adaugă în coș │
        └────────────────┘
```

- **Default:** admin által beállított VAGY user korábbi preferenciája (ha be van jelentkezve)
- **„Ultima ta alegere"** badge ha a default a user mentett preferenciája
- Nem kötelező opciók kihagyhatók — a default érvényes

### 5.2 Kosár — opciók megjelenítése

```
🥩 Sertés nyakaskaraj  · 1 kg                  33 RON
   forma: dublă · marinare: tradițional
                           [✏️ Modifică] [🗑️]
```

### 5.3 Reorder flow (DH-120)

Az „Újrarendelem" használatakor a korábbi rendelés opciói automatikusan betöltődnek. Ha a termék opciói megváltoztak (admin módosította), a régi értéket mutatja jelzéssel: **„Această opțiune nu mai este disponibilă"**.

### 5.4 Admin / Mészáros nézet

Rendelés részletezőben minden terméknél:

| Termék | Mennyiség | Pregătire |
|--------|-----------|-----------|
| Sertés nyakaskaraj | 1 kg | dublă · tradițional |
| Sertés Csülök | 1 buc (~1.5 kg) | mărime: mediu |
| Sertés Apróhús | 0.5 kg | Standard |

Ha nincs opció: **„Standard"**.

### 5.5 Variációs UX szövegek (RO)

| Kontextus | Szöveg |
|-----------|--------|
| Opció szekció cím | `Cum să-ți pregătim?` |
| Forma | `Formă` → `Simplă` / `Dublă` |
| Pácolás | `Marinare` → `Nemarinate` / `Tradițional` / `Barbecue` |
| Szeletelés | `Tăiere` → `Întreg` / `Feliat` |
| Vastagság | `Grosime` → `Subțire` / `Mediu` / `Gros` |
| Méret | `Mărime` → `Mai mic` / `Mediu` / `Mai mare` |
| Zsírosság | `Conținut de grăsime` → `Mai slab` / `Normal` / `Mai gras` |
| Default badge | `Ultima ta alegere` |
| Kosár formátum | `*forma · marinare · grosime*` (italic, smaller) |
| Mészáros nézet | `Pregătire: {opciók}` (vagy `Standard`) |

---

## 6. Adatmodell (Frappe)

### 6.1 Új Child DocType: `Deak Product Option`

Parent: `Deak Product`

| Mező | Type | Megjegyzés |
|------|------|-----------|
| `option_id` | Data | snake_case (pl. `pacolas`) |
| `option_name_hu` | Data | „Pácolás" |
| `option_name_ro` | Data | „Marinare" |
| `option_type` | Select | `single_select` / `multi_level` / `text` |
| `default_value` | Data | a default érték `value_id`-ja |
| `required` | Check | bool — default `0` |
| `display_order` | Int | sorrend a UI-ban |
| `values` | Table → `Deak Product Option Value` | a választható értékek |

### 6.2 Új Child DocType: `Deak Product Option Value`

Parent: `Deak Product Option`

| Mező | Type | Megjegyzés |
|------|------|-----------|
| `value_id` | Data | snake_case (pl. `nem_pacolt`) |
| `value_label_hu` | Data | „Pácolatlan" |
| `value_label_ro` | Data | „Nemarinate" |
| `producer_note` | Data (opcionális) | belső megjegyzés (pl. „24h előrendelés") |
| `weight_range_min` | Float (opcionális) | méret-opciónál a min kg |
| `weight_range_max` | Float (opcionális) | méret-opciónál a max kg |

### 6.3 Új DocType: `Deak User Product Preference`

| Mező | Type | Megjegyzés |
|------|------|-----------|
| `user` | Link → User | bejelentkezett vásárló |
| `product` | Link → Deak Product | melyik termékhez |
| `preferences` | JSON | `{"pacolas": "hagyomanyos", "forma": "dupla"}` |
| `last_updated` | Datetime | utolsó rendelés/módosítás |
| `source` | Select | `order` / `manual` |

**Trigger:** Sikeres rendelés után (`Sales Invoice submitted`) a kiválasztott opciók ide mentődnek/frissülnek.

### 6.4 Sales Invoice Item bővítés

A rendelési tételen rögzíteni kell a kiválasztott opciókat:

| Mező | Type | Megjegyzés |
|------|------|-----------|
| `selected_options` | JSON | `{"pacolas": "hagyomanyos", "forma": "dupla"}` |
| `selected_options_display_ro` | Data | „dublă · tradițional" (denormalizált a printout-hoz) |

---

## 7. Schema kapcsolat (v1.2 előkészítés)

### Jelenlegi (v1.1)
A `_schema-v1.1.json` **NEM** tartalmazza az `options[]` mezőt a `product` definícióban. Az opciók most **MD-only metadata** a MASTER MD-kben.

### Jövőbeli (v1.2 — DH-173 fejlesztéssel együtt)

A schema bump v1.2 hozzáadja az `options[]` opcionális mezőt a `product` definícióhoz:

```json
"options": {
  "type": "array",
  "items": { "$ref": "#/definitions/product_option" }
}
```

A `product_option` definíció:

```json
"product_option": {
  "type": "object",
  "required": ["option_id", "option_name_hu", "option_name_ro", "option_type"],
  "properties": {
    "option_id": { "type": "string", "pattern": "^[a-z][a-z0-9_]*$" },
    "option_name_hu": { "type": "string" },
    "option_name_ro": { "type": "string" },
    "option_type": { "enum": ["single_select", "multi_level", "text"] },
    "default_value": { "type": "string" },
    "required": { "type": "boolean", "default": false },
    "values": {
      "type": "array",
      "items": { "$ref": "#/definitions/option_value" }
    }
  }
}
```

A build.py frissítése: az MD `## Opciók` szekciót parsolja és exportálja a JSON-ba.

---

## 8. Phases / Rollout

### Phase 1 — MVP (Sprint 4 fókusz)

- **Backend:** `Deak Product Option` + `Deak Product Option Value` + `Deak User Product Preference` DocType-ok
- **Schema bump:** v1.1 → v1.2 — `options[]` mező + build.py update
- **Migráció:** A 15 termék MD-ből az `options` MD-only adatok bekerülnek a JSON-ba és a Frappe-be
- **Frontend:** `Cum să-ți pregătim?` szekció a termékdetail oldalon — `single_select` típus
- **Kosár:** opciók megjelenítése
- **Admin:** rendelés részletező — opciók kiírása

### Phase 2 — Reorder + Memory

- **DH-120 integráció:** Reorder flow-ban a preferenciák betöltése
- **Preferencia mentés:** sikeres rendelés után automatikusan
- **„Ultima ta alegere"** badge a visszatérő preferenciánál

### Phase 3 — Advanced (P1)

- **`multi_level` típus** — cascading selectors (ha kell, pl. szeletelés vékony/közepes/vastag mint sub-érték)
- **`text` típus** — szabad megjegyzés a mészárosnak (max 100 char)

### Phase 4 — Nice to Have (P2)

- **Guest user preferencia** localStorage-ban (bejelentkezéskor migrál)
- **„Leggyakrabban választott"** badge ha >70% ugyanazt választja
- **Felár opcióért** (jelenleg NEM, későbbi döntés)
- **AI-alapú preferencia javaslat** (v0.6+)

---

## 9. Firebase Analytics

| Event | Trigger | Params |
|-------|---------|--------|
| `product_option_selected` | User kiválaszt egy opciót | `product_id`, `internal_code`, `option_name`, `value` |
| `product_option_changed` | User megváltoztatja (nem default) | `product_id`, `internal_code`, `option_name`, `old_value`, `new_value` |
| `preference_loaded` | Mentett preferencia betöltődik | `product_id`, `preference_count` |
| `preference_overridden` | User felülírja mentett preferenciát | `product_id`, `option_name` |
| `option_section_skipped` | User nem érintette az opciókat | `product_id`, `option_count` |

---

## 10. Kockázatok + mitigáció

| # | Kockázat | Hatás | Mitigáció |
|---|----------|-------|-----------|
| 1 | Túl sok opció → döntési paralízis | Lassabb rendelés, alacsonyabb konverzió | Max 3 opció termékenként; default mindig van |
| 2 | Mészáros nem olvassa az opciókat | Rossz előkészítés → trust break | Admin UI kiemelten + nyomtatható rendelési lap |
| 3 | Opció-választás lassítja a flow-t | TTFO nő | Opciók opcionálisak, default érvényes |
| 4 | Visszatérő user preferencia outdated | Nem elérhető opció → hiba | Graceful fallback: „Această opțiune nu mai este disponibilă" |
| 5 | Mobile UI túl zsúfolt | Vásárló elveszik | Reszponzív design, kis komponens, default-tal eltüntethető |
| 6 | Termelői oldalon mégis nehézkes (pl. minden Méret kategória terhelő) | Rossz mészáros UX | Phase 1 alatt manuálisan átnézzük az admin nézetet, finomítjuk |

---

## 11. Mérés / sikerkritérium

### Phase 1 (4-6 hét beta)

- ≥60% rendelésnél legalább 1 opció kiválasztva
- Funnel drop a `Cum să-ți pregătim?` szekciónál < 5%
- TTFO **NEM nő** számottevően az opció-választás miatt (max +10s)
- 0 mészáros panasz a rendelési lapon a hiányzó opció-info miatt
- Kvalitatív: ≥3 user mond olyat hogy „itt ismernek engem"

### Phase 2 (preferencia-memory aktív)

- 2+ rendelést leadó user-ek 70%-ánál a default = mentett preferencia (azaz a rendszer ténylegesen tanult)
- Reorder flow-ban a preferenciák 95%-ban érvényesek (nem outdated)

---

## 12. Nyitott kérdések

| # | Kérdés | Felelős | Határidő |
|---|--------|---------|----------|
| Q1 | Felár szeletelésért / pácolásért? Phase 1-ben NEM, de változhat | Szabolcs + Deák | Sprint 4 indulás előtt |
| Q2 | Maximum hány opció termékenként (most max 2, de Phase 1-ben max 3-ban gondolkodunk) | Szabolcs | UX review |
| Q3 | Szabadszöveg megjegyzés (ha bevezetjük) emailben menjen-e a mészárosnak? | Szabolcs + Deák | Phase 3 előtt |
| Q4 | Guest user preferencia mennyire fontos? P0 vagy P2? | Szabolcs | Phase 1 scope |
| Q5 | Kell-e nyomtatható rendelési lap az opciókkal a mészárosnak? | Deák mészáros | Sprint 4 design review |
| Q6 | A `multi_level` típus szükséges Phase 1-ben (pl. „szeletelt → vékony/közepes/vastag" cascading), vagy elég 2 külön `single_select`? | Szabolcs | Backend design |

---

## 13. Függőségek

| Irány | Ticket / Feature | Kapcsolat |
|-------|------------------|-----------|
| **Függ ettől:** | DH-183 (DONE) — Terméktípusok modellezése | A `product_type` határozza meg, mely opciók relevánsak |
| **Függ ettől:** | DH-120 — Reorder Basket Loader | Reorder-nél a preferenciák betöltése |
| **Bővíti:** | DH-127 — Familiar Favourites | A „szokásos rendelésem" a preferenciákat is tartalmazza |
| **Bővíti:** | DH-119 — Post-order Recap | Recap-ben opciók megjelenítése |
| **Kapcsolódik:** | DH-174 — Admin ár-korrekció | Súlyeltérés flow (hybrid termékeknél) |
| **Schema dependency:** | `_schema-v1.1.json` → `v1.2` | `options[]` mező hozzáadása |

---

## 📚 Hivatkozások

- **MASTER MD-k:** `Products/MASTER/products/*.md` (15 termékben rögzítve a `## Opciók` szekció)
- **Excel review:** `Products/products_v1.1_review.xlsx` (Variációk oszlop teljes bontással)
- **Termelői meeting:**
  - `Products/meetings/DH - Mikado - Termek variációk-transcript-full.srt` (43 perc)
  - `Products/meetings/2026-05-07_decisions.md` (kivonat)
  - `Products/meetings/2026-05-07_internal-product-codes.md` (belső kódlista)
- **Per-termék mátrix:** `product-options-matrix-v1.0.md` (ebben a mappában)
- **Előd-spec:** `savings-engine/Ideas/v0.4-product-preferences-spec.md` (v0.1, archív)
- **Jira:** [DH-173](https://exarlabs.atlassian.net/browse/DH-173)

---

**Verzió:** 1.0 | **Dátum:** 2026-05-07 | **Elemzés:** Termelői meeting + 46 MASTER MD aggregálás
