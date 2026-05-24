# 🎯 Unified Product Master — 2026-05-07

> **Single source of truth for the migration into `MASTER/products/*.md`.**
> Reconciled from 4 sources: pre-v1.0 archív, Google Sheet, meeting transcript, internal printout (Baczo Annamaria Sziget).
> Schema target: **v1.1** (with new `internal_code` field).

---

## 📋 Meta + döntések (Szabolcs visszajelzései 2026-05-07)

| Döntés | Szabolcs válasza | Hatás |
|--------|------------------|-------|
| **Q1 — Termékkör** | **A — Konzervatív** | 37 legacy + 7 Sheet új (Csirke 3, Lapocka, Sajtos cérna, Tepertő szalonna, Roppanós virsli) **+ a Sheet 2 sárga sora (Hasrész csontnélkül + Oldalas)** = **46 termék** ⚠️ Lásd lent. |
| **Q2 — Schema bump** | **Igen, v1.1 + új mező** | `internal_code` opcionális mező (pl. `014`, `ACS04`, `945.1`) hozzáadva |
| **Q3 — Új termék-bontások** | **Konzervatív, csak ha kell** | NEM hozzák létre: `0271` Csontos karaj szalonnás, `0211` Munkahús lapocka, `0201` Has császárhús, `944` Füstölt császárhús, `9531` Füstölt bordacsont egész, `9452` Grill csülök, stb. |

### ⚠️ Termékszám — pontosítás kell

A Q1-ben „37 + 7 = 44"-et mondtál. Azonban a **Sheet 2 sárga új sora** (Sertés Hasrész Csontnélkül + Sertés Oldalas, kódok `019` + `020`) **a meeting alapján rögzítve** lett — tehát ezeket is a pre-v1.0 evolúciójához tartozónak vettem.

**Tehát 46 termék** (37 legacy + 2 Sheet hasrész split + 7 Sheet új).

→ **Ha mégis 44-et akarsz** (a 2 hasrész split-et kihagyva), szólj és törlöm őket.

---

## 🔧 Schema v1.1 változások (ami ma került be)

```diff
+ "internal_code": {
+   "type": ["string", "null"],
+   "pattern": "^[A-Z0-9]{3,7}(\\.[0-9]+)?$",
+   "default": null,
+   "description": "Internal product code from Baczo Annamaria Sziget master list"
+ }
```

Példák: `"014"`, `"0221"`, `"ACS04"`, `"945.1"`, `"9904"` — mind illeszkedik a regex-re.
Opcionális (null megengedett, ha nincs kód).

---

## 📊 Master táblázat — minden termék egy pillantásra

> Sorrend: kategória → ABC. Az ár oszlop a printoutban szereplő ár (RON). „Hyb" = hybrid termék (méret-változatos).

### 🥩 Friss Sertéshús (14 termék)

| # | Kód | ID | HU (publikus) | RO | Ár | Típus | Opciók (DH-173) | Forrás |
|---|-----|----|---------------|-----|-----|-------|-----------------|--------|
| 1 | `014` | `nyakas_karaj` | Sertés nyakaskaraj | Ceafă porc | 33 | weight | **Forma** (sima/dupla) + **Pácolás** (3 érték) | legacy (renamed) |
| 2 | `026` | `sertes_belszin` | Sertés Bélszín | Mușchuleți porc | 40 | hybrid (~0.5 kg) | NINCS | legacy |
| 3 | `0221` | `sertes_borda_csont` | Sertés Bordacsont (kisebb) | Coaste porc | 12 | weight | NINCS | legacy |
| 4 | `010` | `sertes_comb` | Sertés comb csontnélkül | Pulpă porc | 25 | weight | NINCS | legacy (renamed) |
| 5 | `016` | `sertes_csontos_karaj` | Sertés csontos karaj | Cotlet porc cu os și slănină | 25.5 | hybrid (~1.5 kg) | **Pácolás** (3 érték) + szeletelve adják | legacy |
| 6 | `007` | `sertes_csulok` | Sertés Csülök | Ciolan porc | 19 | hybrid (~1.5 kg) | **Méret** (kisebb/közepes/nagyobb) | legacy |
| 7 | `0222` | `sertes_egesz_bordacsont` | Sertés Egész Bordacsont | Coaste porc întregi | 15 | weight | NINCS | legacy |
| 8 | `015` | `sertes_feher_karaj` | Sertés fehérkaraj csontnélkül | Cotlet porc fără os | 33 | weight | **Szeletelés** + **Pácolás** | legacy (renamed) |
| 9 | `018` | `sertes_hasresz` | Sertés Hasrész (csontos+bőrös) | Piept porc | 24.5 | weight | NINCS | legacy |
| 10 | `019` | `sertes_hasresz_csont_nelkul` | Sertés Hasrész Csontnélkül (bőrös) | Piept porc fără os | 26 | weight | **Szeletelés** + **Pácolás** | Sheet (új sárga sor) |
| 11 | `020` | `sertes_oldalas` | Sertés Oldalas (csontos, bőr nélkül) | Costiță | 26 | weight | **Szeletelés** + **Pácolás** | Sheet (új sárga sor) |
| 12 | `011` | `sertes_lapocka` | Sertés Lapocka (csontnélkül, szalonna nélkül) | Spata porc, fără os și fără slănină | 25 | weight | NINCS | Sheet Új |
| 13 | `021` | `sertes_munka_hus` | Sertés Apróhús | Carne porc lucru | 21 | weight | NINCS | legacy |
| 14 | `902` | `sertes_orolt_hus` | Sertés Őrölt Hús | Carne tocată porc | 21 | weight | **Alapanyag** (4 érték) + **Zsírosság** (3 érték) | legacy |
| 15 | `012` | `sertes_szalonnas_comb` | Sertés Szalonnás Comb | Pulpă porc cu slănină | 24.5 | weight | NINCS | legacy |
| 16 | `008` | `sertes_toka_szalonna` | Sertés Toka Szalonna | Slănină gușă | 20 | weight | NINCS | legacy |

### 🐄 Friss Növendékhús (1 termék)

| # | Kód | ID | HU | RO | Ár | Típus | Opciók | Forrás |
|---|-----|----|-----|-----|-----|-------|--------|--------|
| 17 | `114` | `velos_csont` | Növendék Velős Csont | Oase bovine cu măduvă | 22 | weight | NINCS | legacy |

### 🔥 Füstölt Áruk (12 termék)

| # | Kód | ID | HU | RO | Ár | Típus | Opciók | Forrás |
|---|-----|----|-----|-----|-----|-------|--------|--------|
| 18 | `949.3` | `fustolt_belszin` | Füstölt Bélszín | Mușchuleți porc afumat | 55 | hybrid (~0.4-0.5 kg) | NINCS | legacy |
| 19 | `953` | `fustolt_bordacsont` | Füstölt Bordacsont | Coaste porc afumat | 16 | weight | NINCS | legacy |
| 20 | `945` | `fustolt_csulok` | Füstölt Csülök | Ciolan porc afumat | 34 | hybrid (~1.5 kg) | **Méret** (kisebb/nagyobb) | legacy |
| 21 | `945.1` | `fustolt_csulok_csont_nelkul` | Füstölt Csülök Csont Nélkül *(belső név: Csemege Csülök)* | Ciolan porc afumat fără os | 44 | hybrid (~1.2 kg) | **Méret** (kisebb/nagyobb) | legacy |
| 22 | `934` | `fustolt_egybe_sonka` | Füstölt Egész Sonka 🌟 *(szezonális — húsvét/karácsony)* | Șuncă de porc întreg afumat | 55 | weight (5-6 kg/db) | NINCS, csak szeletelhetőség | legacy |
| 23 | `949` | `fustolt_feher_karaj` | Füstölt Fehér Karaj | Cotlet porc afumat | 49 | weight | **Vastagság** (vékony 2mm / közepes 4mm / vastag 6mm) | legacy |
| 24 | `946` | `fustolt_has` | Füstölt Has csont nélkül | Piept porc afumat | 47 | weight | **Vastagság** + **Pácolás** | legacy |
| 25 | (—) | `fustolt_kotozott_sonka` | Füstölt Kötözött Sonka 🌟 *(szezonális)* | Jambon de sărbătoare | 50 | hybrid (~1 kg) | fél darab is adható | legacy |
| 26 | `948` | `fustolt_nyakas_karaj` | Füstölt Nyakas Karaj | Ceafă porc afumat | 49 | weight | **Szeletelés** (vastagság NEM) | legacy |
| 27 | `952` | `fustolt_oldalas` | Füstölt Oldalas | Costiță afumată | 47 | weight | NINCS | legacy |
| 28 | `942` | `fustolt_szalonna` | Füstölt Szalonna | Slănină afumată | 42 | weight | NINCS | legacy |
| 29 | `933` | `fustolt_szalonnas_sonka` | Füstölt Szalonnás Sonka | Șuncă de porc afumat cu slănină | 48 | weight | NINCS | legacy |

### 🌭 Kolbász & Szalámi (8 termék)

| # | Kód | ID | HU | RO | Ár | Típus | Opciók | Forrás |
|---|-----|----|-----|-----|-----|-------|--------|--------|
| 30 | `920` | `cerna_kolbasz` | Cérna Kolbász | Cârnați Cabanos | 48 | weight | NINCS | legacy |
| 31 | `911` | `erdelyi_kolbasz` | Deák háziKolbász *(belső: Deák Házi Kolbász)* | Cârnați de casă Deák | 45 | weight | NINCS | legacy |
| 32 | `906` | `miccs` | Miccs | Mititei | 40 | weight | NINCS — **8 db = 0.5 kg, 16 db = 1 kg** | legacy |
| 33 | `991` | `novendek_szalami` | Házi Szalámi *(régi: Növendék Szalámi)* | Salam de casă | 46 | weight | **Vastagság** (3 érték) | legacy (renamed) |
| 34 | `917` | `sertes_szalami` | Sertés Szalámi | Salam de porc | 43 | weight | **Vastagság** (3 érték) | legacy |
| 35 | `921` | `szekely_kolbasz` | Székely Kolbász | Cârnați de casă Secuieni | 45 | weight | NINCS | legacy |
| 36 | `9904` | `teli_szalami` | Téli Szalámi | Salam de iarnă | 68 | weight | **Vastagság** (3 érték) | legacy |
| 37 | `9201` | `sajtos_cerna_kolbasz` | Sajtos Cérna Kolbász | Cârnați de cabanos cu cașcaval | 48 | weight | NINCS | Sheet Új |

### 🍖 Felvágott & Egyéb (5 termék)

| # | Kód | ID | HU | RO | Ár | Típus | Opciók | Forrás |
|---|-----|----|-----|-----|-----|-------|--------|--------|
| 38 | `941` | `abalt_szalonna` | Abált Szalonna | Slănină fiartă | 35 | weight | NINCS | legacy |
| 39 | `909` | `diszno_fosajt` | Disznó Fősajt | Tobă de porc | 35 | weight | NINCS | legacy |
| 40 | `9980` | `gongyolt_hus` | Göngyölt Hús | Rulada de porc | 47 | weight | NINCS (NEM szeletelhető — kipotyogna) | legacy |
| 41 | `982` | `pastetom` | Pástétom 330g | Pate porc de casă | 22 | piece | NINCS | legacy |
| 42 | `025` | `tepertonek_valo_szalonna` | Tepertőnek való Szalonna *(régi: Munka szalonna)* | Slănină lucru | 15 | weight | NINCS — **NYÁRI termék** | Sheet Új |

### 🐔 Csirke (3 termék — ÚJ KATEGÓRIA?)

| # | Kód | ID | HU | RO | Ár | Típus | Opciók | Forrás |
|---|-----|----|-----|-----|-----|-------|--------|--------|
| 43 | `ACS01` | `csirke_szarny` | Csirke Szárny | Aripi de pui | 16 | weight | NINCS | Sheet Új |
| 44 | `ACS02` | `csirke_egybe_comb` | Csirke Egybe Comb | Pulpă de pui întreagă | 17 | weight | NINCS | Sheet Új |
| 45 | `ACS04` | `csirke_mell_csont_borr_nelkul` | Csirke Mell Csont és Bőr Nélkül | Piept de pui fără os și piele | 34 | weight | NINCS | Sheet Új |

> **Kérdés:** új `friss_csirkehus` kategória, vagy a `friss_serteshus`-ba? *(felvetésem: új kategória — más állat)*

### 🌭 Egyéb új kolbász (1 termék)

| # | Kód | ID | HU | RO | Ár | Típus | Opciók | Forrás |
|---|-----|----|-----|-----|-----|-------|--------|--------|
| 46 | `960` | `roppanos_virsli` | Roppanós Virsli | Crenvuști "Roppanós" | 48 | weight | NINCS — disznócombból + szalonna, juhbélbe töltve, „ehető bél" | Sheet Új |

> **Kérdés:** ez melyik kategóriába? `kolbasz_szalami`-ba? Vagy új `virsli` kategória?

---

## 📌 Termék részletek — opciókkal és/vagy fontos megjegyzéssel

### #1 — `nyakas_karaj` (Sertés nyakaskaraj)

**Internal:** `014` · **Image:** `nyakas_karaj.webp` · **Ár:** 33 RON/kg · **Type:** weight

**Opciók:**

| Opció | Type | Default | Required | Értékek |
|-------|------|---------|----------|---------|
| `forma` | single_select | `sima` | false | sima (újnyi vastag minimum), dupla (két szelet középen egyben, kinyitva) |
| `pacolas` | single_select | `nem_pacolt` | false | nem_pacolt, hagyomanyos (só + bors + fokhagyma), barbecue (paradicsomos) |

**Termelői megjegyzés (2026-05-07 meeting):**
> A vékonyra szeletelt nyakaskaraj „cipőtalp érzet"-et ad — minimum újnyi vastagság kell. A „dupla" forma a férfias, nagyobb verzió: két szelet középen egyben hagyva, kinyitva, potyolva.

**Foto-stratégia:** szükséges fotók a `sima` és `dupla` formához + `pácolt` és `nem_pácolt`. Háttér: zöld + piros zöldség (saláta, paradicsom).

---

### #5 — `sertes_csontos_karaj`

**Internal:** `016` · **Image:** `sertes_csontos_karaj.webp` · **Ár:** 25.5 RON/kg · **Type:** hybrid (1.5 kg/db, 1.2-1.8 kg)

**Opciók:**

| Opció | Type | Default | Required | Értékek |
|-------|------|---------|----------|---------|
| `pacolas` | single_select | `nem_pacolt` | false | nem_pacolt, hagyomanyos, barbecue |

**Termelői megjegyzés:** Szeletelve adják alapból. Csontot grillhez hagyják. Vastagság-variáció NINCS.

---

### #6 — `sertes_csulok`

**Internal:** `007` · **Image:** `sertes_csulok.webp` · **Ár:** 19 RON/kg · **Type:** hybrid (1.5 kg/db, 1.2-1.8 kg)

**Opciók:**

| Opció | Type | Default | Required | Értékek |
|-------|------|---------|----------|---------|
| `meret` | single_select | `kozepes` | false | kisebb (1.2-1.4 kg), közepes (1.4-1.6 kg), nagyobb (1.6-1.8 kg) |

**Termelői megjegyzés:** „Egy 40-től egy 70-ig" méret-eltérés (~10-30 deka). Vásárlók kérik („mama a kisebbiket").

---

### #8 — `sertes_feher_karaj`

**Internal:** `015` · **Image:** `sertes_feher_karaj.webp` · **Ár:** 33 RON/kg · **Type:** weight

**Opciók:**

| Opció | Type | Default | Required | Értékek |
|-------|------|---------|----------|---------|
| `szeletes` | single_select | `egesz` | false | egesz, szeletelt |
| `pacolas` | single_select | `nem_pacolt` | false | nem_pacolt, hagyomanyos, barbecue |

**Termelői megjegyzés:** „Szeletnek való", Bécsi szelet, flekken (sovány szereti). Pörköltnek nem ideális.

---

### #10 — `sertes_hasresz_csont_nelkul`

**Internal:** `019` · **Image:** *(még kell)* · **Ár:** 26 RON/kg · **Type:** weight

**Opciók:**

| Opció | Type | Default | Required | Értékek |
|-------|------|---------|----------|---------|
| `szeletes` | single_select | `egesz` | false | egesz, szeletelt |
| `pacolas` | single_select | `nem_pacolt` | false | nem_pacolt, hagyomanyos, barbecue |

**Termelői megjegyzés:** Bőrös, csontnélküli. Felhasználás: grill, lerben kisütni, „hasonló mint a nyakas karaj". RO: Piept porc fără os.

---

### #11 — `sertes_oldalas`

**Internal:** `020` · **Image:** *(még kell)* · **Ár:** 26 RON/kg · **Type:** weight

**Opciók:**

| Opció | Type | Default | Required | Értékek |
|-------|------|---------|----------|---------|
| `szeletes` | single_select | `egesz` | false | egesz, szeletelt |
| `pacolas` | single_select | `nem_pacolt` | false | nem_pacolt, hagyomanyos, barbecue |

**Termelői megjegyzés:** „Csontos, de nincs rajta bőr." RO: Costiță (NINCS a Sheetben — kérdéses!).

---

### #14 — `sertes_orolt_hus` (Sertés Őrölt Hús) — ⚠️ legtöbb opció

**Internal:** `902` · **Image:** `sertes_orolt_hus.webp` · **Ár:** 21 RON/kg (fix, opciók nem módosítják) · **Type:** weight

**Opciók:**

| Opció | Type | Default | Required | Értékek |
|-------|------|---------|----------|---------|
| `alapanyag` | single_select | `lapocka` | false | comb (szárazabb), lapocka (alapért.), has (zsírosabb), vegyes (fele-fele) |
| `zsirossag` | single_select | `normal` | false | kevesbe_zsiros (bolognai, ragú), normal (alap, fele-fele), zsirosabb (fasírt, töltelékes káposzta) |

**Termelői megjegyzés:** Az ár fix 21 RON akármilyen alapanyag-választással. UX: opciók alá szöveges magyarázat („zsírosabból sütöd a fasírtot, kevésbé zsírosból a bolognait, ragút").

---

### #20 — `fustolt_csulok`

**Internal:** `945` · **Image:** `fustolt_csulok.webp` · **Ár:** 34 RON/kg · **Type:** hybrid (~1.5 kg)

**Opciók:**

| Opció | Type | Default | Required | Értékek |
|-------|------|---------|----------|---------|
| `meret` | single_select | `kozepes` | false | kisebb, közepes, nagyobb |

---

### #21 — `fustolt_csulok_csont_nelkul` (Csemege Csülök)

**Internal:** `945.1` · **Image:** `fustolt_csulok_csont_nelkul.webp` · **Ár:** 44 RON/kg · **Type:** hybrid (~1.2 kg)

**Opciók:**

| Opció | Type | Default | Required | Értékek |
|-------|------|---------|----------|---------|
| `meret` | single_select | `kozepes` | false | kisebb, közepes, nagyobb |

---

### #22 — `fustolt_egybe_sonka` 🌟 (Szezonális)

**Internal:** `934` · **Ár:** 55 RON/kg · **Type:** weight (5-6 kg/db, csontos)

**Opció:** csak szeletelhetőség (5 cm karikára felvághatók fűrésszel).

**Termelői megjegyzés:** „Bükkfa fűrészporral füstölt" — fontos marketing megjegyzés. **Szezonális:** csak húsvét + karácsony.

---

### #23 — `fustolt_feher_karaj`

**Internal:** `949` · **Ár:** 49 RON/kg · **Type:** weight

**Opciók:**

| Opció | Type | Default | Required | Értékek |
|-------|------|---------|----------|---------|
| `vastagsag` | single_select | `kozepes` | false | vekony (2mm), kozepes (4mm), vastag (6mm) |

---

### #24 — `fustolt_has`

**Internal:** `946` · **Ár:** 47 RON/kg · **Type:** weight

**Opciók:**

| Opció | Type | Default | Required | Értékek |
|-------|------|---------|----------|---------|
| `vastagsag` | single_select | `kozepes` | false | vekony, kozepes, vastag |
| `pacolas` | single_select | `nem_pacolt` | false | nem_pacolt, hagyomanyos, barbecue |

**Termelői megjegyzés:** „Bükkfa fűrészporral füstölt". Felhasználás: leves, lerben sütés, káposztához (NEM grill).

---

### #25 — `fustolt_kotozott_sonka` 🌟 (Szezonális)

**Internal:** *(nincs külön kód a printouton)* · **Ár:** 50 RON/kg · **Type:** hybrid (~1 kg)

**Termelői megjegyzés:** Hálóban tartva. **Fél darab is adható.** Szezonális (mint az egész sonka).

---

### #26 — `fustolt_nyakas_karaj`

**Internal:** `948` · **Ár:** 49 RON/kg · **Type:** weight

**Opciók:**

| Opció | Type | Default | Required | Értékek |
|-------|------|---------|----------|---------|
| `szeletes` | single_select | `szeletelt` | false | egesz, szeletelt |

**Termelői megjegyzés:** Csak szeletelt/egész — vastagság-variáció NEM (nem éri meg).

---

### #33 — `novendek_szalami` (Házi Szalámi)

**Internal:** `991` · **Ár:** 46 RON/kg · **Type:** weight

**Opciók:**

| Opció | Type | Default | Required | Értékek |
|-------|------|---------|----------|---------|
| `vastagsag` | single_select | `kozepes` | false | vekony, kozepes, vastag |

**Termelői megjegyzés:** Szeleteléskor a bőrt automatikusan eltávolítják? — UX kérdés, nem schema. Belső név változás: „Növendék Szalámi" → **„Száraz Házi Szalámi"** (kód `991`).

---

### #34 — `sertes_szalami`

**Internal:** `917` · **Ár:** 43 RON/kg · **Type:** weight

**Opciók:** ugyanaz mint a `novendek_szalami` (Vastagság).

---

### #36 — `teli_szalami`

**Internal:** `9904` · **Ár:** 68 RON/kg · **Type:** weight

**Opciók:** ugyanaz mint a szalámik (Vastagság).

---

### #41 — `pastetom`

**Internal:** `982` · **Ár:** 22 RON/db · **Type:** piece (330g)

**Termelői megjegyzés:** A pontos kiszerelés rögzítve: **330g**.

---

### #46 — `roppanos_virsli`

**Internal:** `960` · **Ár:** 48 RON/kg · **Type:** weight

**Termelői megjegyzés:** Disznócombból + szalonna, juhbélbe töltve, „ehető bél". RO: `Crenvuști "Roppanós"`.

---

## ❓ Nyitott kérdések — Szabolcs validáció kell

### Kérdés 1 — Csirke kategória
- **Új `friss_csirkehus`** (külön kategória, magyar/RO névvel) vagy `friss_serteshus`-ba?
- **Javaslat:** új kategória, mert más állat. Más logika. (3 termék most, később bővülhet)

### Kérdés 2 — `roppanos_virsli` kategória
- `kolbasz_szalami`-ba vagy új `virsli` kategória?
- **Javaslat:** `kolbasz_szalami`-ba (csak 1 termék most, nem érdemes új kategória).

### Kérdés 3 — `tepertonek_valo_szalonna` kategória
- A pre-v1.0 archívban `felvagott_egyeb`-be raknám.  
- **Javaslat:** `felvagott_egyeb`. (Szezonális meta-flag: `seasonal: summer`).

### Kérdés 4 — Termékszám: 44 vs 46 ⚠️
- Q1-re „A" választoltad (= „37 + 7 = 44").
- A Sheet 2 sárga új sora (`sertes_hasresz_csont_nelkul`, `sertes_oldalas`) viszont a meeting alapján rögzítve van.  
- **Vagy 46 termék** (a Sheet 2 sárgát is bevesszük), **vagy 44 termék** (csak az eredeti `sertes_hasresz` marad, a 2 splitelt szerepel a backlogban).

### Kérdés 5 — Sertés Hasrész (`018`) Sheet description hiánya
- A Sheet leírása: „Zsíros, ízgazdag hasrész, pörköltnek, darálva vagy frissen sütve kiváló."
- A meeting és a printout szerint ez a **csontos+bőrös** verzió.
- A leírás OK marad, de **változik:** opció már nincs (csontos+bőrös = simán kilóra).

### Kérdés 6 — Sheet hibás row 7 (sertes_csulok)
- Sheet `Új Név` és `nume produs` a Csontos Karaj értékeit tartalmazza tévesen.
- **Javítás:** RO neve `Ciolan porc` (az unified master már így tartja).
- Szabolcs javítja a Sheet-ben?

---

## 🚦 Mit jelent ez a következő lépésben

Ha a 6 nyitott kérdésre válaszolsz + a 44 vs 46 számot megerősíted, akkor:

1. **Schema v1.1 deploy** (a `_schema-v1.1.json` már elkészült, csak deployolni kell)
2. **MASTER MD migráció** — 44 (vagy 46) MD fájlt generálunk a `MASTER/products/`-ba az unified master alapján
3. **Build → JSON v1.1** generálás
4. **Deploy** — új JSON kerül a Documents tabra (régi v1.0 product file leváltva v1.1-re)

A migráció **nagyrészt automatizálható** — minden termékhez alapsablonból generálódik az MD, az opciókkal és termelői megjegyzésekkel együtt.

---

## 📑 Forrás-leképezés (audit trail)

- **pre-v1.0 archív:** `Products/(archív legacy)` (legacy, deprecated)
- **Google Sheet:** https://docs.google.com/spreadsheets/d/15AJpMxf1Q6S-6o8DoiBvKMtTJ67AuJm7l6BmwItD084 + lokálisan `Products/meetings/Termékek - Termékek.csv`
- **Meeting transcript:** `Products/meetings/DH - Mikado - Termek variációk-transcript-full.srt` (43 perc)
- **Decisions extract:** `Products/meetings/2026-05-07_decisions.md`
- **Internal printout:** `Products/meetings/2026-05-07_internal-product-codes.md` (Baczo Annamaria Sziget, ~95 termék)
- **Schema v1.1:** `Products/MASTER/_schema-v1.1.json`

---

**Készítette:** Cowork session (Szabolccsal együttműködésben)
**Dátum:** 2026-05-07
**Státusz:** REVIEW — Szabolcs jóváhagyására vár, mielőtt MASTER/products/*.md generálás indul
