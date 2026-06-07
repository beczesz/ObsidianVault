---
title: "Product Options Matrix v1.0 — per-termék opció bontás"
date: 2026-05-09
author: Becze Szabolcs
status: active
description: "Detailed breakdown of 15 pork products with customizable options from a 46-product catalog, including 59 variation values for size, slicing, marinating, and thickness preferences used by production and sales teams."
description_source: auto
description_hash: a84c921847356991
id: 2630a396-2525-413d-ac41-ddccbba9d70f
index_schema_version: 1
bdos_index: true
---
# Product Options Matrix v1.0 — per-termék opció bontás

> **Generálva:** 2026-05-07 (a `Products/MASTER/products/*.md` fájlokból)
> **Spec:** [`product-variations-spec-v1.0.md`](./product-variations-spec-v1.0.md)
> **Forrás:** Termelői meeting (Mikado, 2026-05-07, 43 perc) + Sheet review

A 46 termékből **15 rendelkezik DH-173 opciókkal** (a maradék 31 csak simán kilóra/db).
**59 összes variation érték** rögzítve.

## Tartalomjegyzék

| Termék | Kód | Kategória | Opciók |
|--------|-----|-----------|--------|
| [Sertés Csülök](#sertes-csulok) | `007` | Friss Sertéshús | Méret |
| [Sertés Hasrész Csontnélkül](#sertes-hasresz-csont-nelkul) | `019` | Friss Sertéshús | Szeletelés + Pácolás |
| [Sertés Oldalas](#sertes-oldalas) | `020` | Friss Sertéshús | Szeletelés + Pácolás |
| [Sertés fehérkaraj csontnélkül](#sertes-feher-karaj) | `015` | Friss Sertéshús | Szeletelés + Pácolás |
| [Sertés fehérkaraj csontos szalonnás](#sertes-csontos-karaj) | `016` | Friss Sertéshús | Pácolás |
| [Sertés nyakaskaraj](#nyakas-karaj) | `014` | Friss Sertéshús | Forma + Pácolás |
| [Sertés Őrölt Hús](#sertes-orolt-hus) | `902` | Friss Sertéshús | Zsírosság |
| [Füstölt Csülök](#fustolt-csulok) | `945` | Füstölt Áruk | Méret |
| [Füstölt Csülök Csont Nélkül](#fustolt-csulok-csont-nelkul) | `945.1` | Füstölt Áruk | Méret |
| [Füstölt Fehér Karaj](#fustolt-feher-karaj) | `949` | Füstölt Áruk | Vastagság |
| [Füstölt Has](#fustolt-has) | `946` | Füstölt Áruk | Vastagság + Pácolás |
| [Füstölt Nyakas Karaj](#fustolt-nyakas-karaj) | `948` | Füstölt Áruk | Szeletelés |
| [Házi szalámi](#novendek-szalami) | `991` | Kolbász & Szalámi | Vastagság |
| [Sertés Szalámi](#sertes-szalami) | `917` | Kolbász & Szalámi | Vastagság |
| [Téli Szalámi](#teli-szalami) | `9904` | Kolbász & Szalámi | Vastagság |

---

## <a name="sertes-csulok"></a>Sertés Csülök

**Kód:** `007` · **Kategória:** Friss Sertéshús · **Típus:** `hybrid` · **Ár:** 19.0 RON · **RO:** Ciolan porc
**Becsült súly:** ~1.5 kg (1.2–1.8 kg)

### Opció — Méret

`option_id`: `meret` · `type`: `single_select` · required: `false` · default: `kozepes` · RO label: `Mărime`

| ✓/• | `value_id` | HU | RO | Megjegyzés |
|-----|-----------|-----|-----|------------|
| • | `kisebb` | Kisebb | Mai mic | 1.2-1.4 kg |
| ✓ | `kozepes` | Közepes | Mediu | 1.4-1.6 kg |
| • | `nagyobb` | Nagyobb | Mai mare | 1.6-1.8 kg |

---

## <a name="sertes-hasresz-csont-nelkul"></a>Sertés Hasrész Csontnélkül

**Kód:** `019` · **Kategória:** Friss Sertéshús · **Típus:** `weight` · **Ár:** 26.0 RON · **RO:** Piept porc fără os

### Opció — Szeletelés

`option_id`: `szeletes` · `type`: `single_select` · required: `false` · default: `egesz` · RO label: `Tăiere`

| ✓/• | `value_id` | HU | RO | Megjegyzés |
|-----|-----------|-----|-----|------------|
| ✓ | `egesz` | Egész | Întreg | — |
| • | `szeletelt` | Szeletelt | Feliat | — |

### Opció — Pácolás

`option_id`: `pacolas` · `type`: `single_select` · required: `false` · default: `nem_pacolt` · RO label: `Marinare`

| ✓/• | `value_id` | HU | RO | Megjegyzés |
|-----|-----------|-----|-----|------------|
| ✓ | `nem_pacolt` | Pácolatlan | Nemarinate | — |
| • | `hagyomanyos` | Pácolt — Hagyományos | Marinat — Tradițional | Só, bors, fokhagyma |
| • | `barbecue` | Pácolt — Barbecue | Marinat — Barbecue | Paradicsomos, BBQ-szerű |

---

## <a name="sertes-oldalas"></a>Sertés Oldalas

**Kód:** `020` · **Kategória:** Friss Sertéshús · **Típus:** `weight` · **Ár:** 26.0 RON · **RO:** Costiță

### Opció — Szeletelés

`option_id`: `szeletes` · `type`: `single_select` · required: `false` · default: `egesz` · RO label: `Tăiere`

| ✓/• | `value_id` | HU | RO | Megjegyzés |
|-----|-----------|-----|-----|------------|
| ✓ | `egesz` | Egész | Întreg | — |
| • | `szeletelt` | Szeletelt | Feliat | — |

### Opció — Pácolás

`option_id`: `pacolas` · `type`: `single_select` · required: `false` · default: `nem_pacolt` · RO label: `Marinare`

| ✓/• | `value_id` | HU | RO | Megjegyzés |
|-----|-----------|-----|-----|------------|
| ✓ | `nem_pacolt` | Pácolatlan | Nemarinate | — |
| • | `hagyomanyos` | Pácolt — Hagyományos | Marinat — Tradițional | Só, bors, fokhagyma |
| • | `barbecue` | Pácolt — Barbecue | Marinat — Barbecue | Paradicsomos, BBQ-szerű |

---

## <a name="sertes-feher-karaj"></a>Sertés fehérkaraj csontnélkül

**Kód:** `015` · **Kategória:** Friss Sertéshús · **Típus:** `weight` · **Ár:** 33.0 RON · **RO:** Cotlet porc fără os

### Opció — Szeletelés

`option_id`: `szeletes` · `type`: `single_select` · required: `false` · default: `egesz` · RO label: `Tăiere`

| ✓/• | `value_id` | HU | RO | Megjegyzés |
|-----|-----------|-----|-----|------------|
| ✓ | `egesz` | Egész | Întreg | — |
| • | `szeletelt` | Szeletelt | Feliat | — |

### Opció — Pácolás

`option_id`: `pacolas` · `type`: `single_select` · required: `false` · default: `nem_pacolt` · RO label: `Marinare`

| ✓/• | `value_id` | HU | RO | Megjegyzés |
|-----|-----------|-----|-----|------------|
| ✓ | `nem_pacolt` | Pácolatlan | Nemarinate | — |
| • | `hagyomanyos` | Pácolt — Hagyományos | Marinat — Tradițional | Só, bors, fokhagyma |
| • | `barbecue` | Pácolt — Barbecue | Marinat — Barbecue | Paradicsomos, BBQ-szerű |

---

## <a name="sertes-csontos-karaj"></a>Sertés fehérkaraj csontos szalonnás

**Kód:** `016` · **Kategória:** Friss Sertéshús · **Típus:** `hybrid` · **Ár:** 25.5 RON · **RO:** Cotlet porc cu os și slănină
**Becsült súly:** ~1.5 kg (1.2–1.8 kg)

### Opció — Pácolás

`option_id`: `pacolas` · `type`: `single_select` · required: `false` · default: `nem_pacolt` · RO label: `Marinare`

| ✓/• | `value_id` | HU | RO | Megjegyzés |
|-----|-----------|-----|-----|------------|
| ✓ | `nem_pacolt` | Pácolatlan | Nemarinate | — |
| • | `hagyomanyos` | Pácolt — Hagyományos | Marinat — Tradițional | Só, bors, fokhagyma |
| • | `barbecue` | Pácolt — Barbecue | Marinat — Barbecue | Paradicsomos, BBQ-szerű |

---

## <a name="nyakas-karaj"></a>Sertés nyakaskaraj

**Kód:** `014` · **Kategória:** Friss Sertéshús · **Típus:** `weight` · **Ár:** 33.0 RON · **RO:** Ceafă porc

### Opció — Forma

`option_id`: `forma` · `type`: `single_select` · required: `false` · default: `sima` · RO label: `Formă`

| ✓/• | `value_id` | HU | RO | Megjegyzés |
|-----|-----------|-----|-----|------------|
| ✓ | `sima` | Sima | Simplă | Vékony szelet, minimum újnyi vastag (vékonyabb cipőtalp érzet) |
| • | `dupla` | Dupla | Dublă | Két szelet középen egyben, kinyitva, potyolva — férfias, nagyobb |

### Opció — Pácolás

`option_id`: `pacolas` · `type`: `single_select` · required: `false` · default: `nem_pacolt` · RO label: `Marinare`

| ✓/• | `value_id` | HU | RO | Megjegyzés |
|-----|-----------|-----|-----|------------|
| ✓ | `nem_pacolt` | Pácolatlan | Nemarinate | — |
| • | `hagyomanyos` | Pácolt — Hagyományos | Marinat — Tradițional | Só, bors, fokhagyma |
| • | `barbecue` | Pácolt — Barbecue | Marinat — Barbecue | Paradicsomos, BBQ-szerű |

---

## <a name="sertes-orolt-hus"></a>Sertés Őrölt Hús

**Kód:** `902` · **Kategória:** Friss Sertéshús · **Típus:** `weight` · **Ár:** 21.0 RON · **RO:** Carne tocată porc

### Opció — Zsírosság

`option_id`: `zsirossag` · `type`: `single_select` · required: `false` · default: `normal` · RO label: `Conținut de grăsime`

| ✓/• | `value_id` | HU | RO | Megjegyzés |
|-----|-----------|-----|-----|------------|
| • | `kevesbe_zsiros` | Kevésbé zsíros | Mai slab | Bolognai, ragú |
| ✓ | `normal` | Normál | Normal | Alapértelmezett, fele-fele |
| • | `zsirosabb` | Zsírosabb | Mai gras | Fasírt, töltelékes káposzta |

---

## <a name="fustolt-csulok"></a>Füstölt Csülök

**Kód:** `945` · **Kategória:** Füstölt Áruk · **Típus:** `hybrid` · **Ár:** 34.0 RON · **RO:** Ciolan porc afumat
**Becsült súly:** ~1.5 kg (1.2–1.8 kg)

### Opció — Méret

`option_id`: `meret` · `type`: `single_select` · required: `false` · default: `kozepes` · RO label: `Mărime`

| ✓/• | `value_id` | HU | RO | Megjegyzés |
|-----|-----------|-----|-----|------------|
| • | `kisebb` | Kisebb | Mai mic | — |
| ✓ | `kozepes` | Közepes | Mediu | — |
| • | `nagyobb` | Nagyobb | Mai mare | — |

---

## <a name="fustolt-csulok-csont-nelkul"></a>Füstölt Csülök Csont Nélkül

**Kód:** `945.1` · **Kategória:** Füstölt Áruk · **Típus:** `hybrid` · **Ár:** 44.0 RON · **RO:** Ciolan porc afumat fără os
**Becsült súly:** ~1.2 kg (1.0–1.5 kg)

### Opció — Méret

`option_id`: `meret` · `type`: `single_select` · required: `false` · default: `kozepes` · RO label: `Mărime`

| ✓/• | `value_id` | HU | RO | Megjegyzés |
|-----|-----------|-----|-----|------------|
| • | `kisebb` | Kisebb | Mai mic | — |
| ✓ | `kozepes` | Közepes | Mediu | — |
| • | `nagyobb` | Nagyobb | Mai mare | — |

---

## <a name="fustolt-feher-karaj"></a>Füstölt Fehér Karaj

**Kód:** `949` · **Kategória:** Füstölt Áruk · **Típus:** `weight` · **Ár:** 49.0 RON · **RO:** Cotlet porc afumat

### Opció — Vastagság

`option_id`: `vastagsag` · `type`: `single_select` · required: `false` · default: `kozepes` · RO label: `Grosime`

| ✓/• | `value_id` | HU | RO | Megjegyzés |
|-----|-----------|-----|-----|------------|
| • | `vekony` | Vékony | Subțire | 2 mm |
| ✓ | `kozepes` | Közepes | Mediu | 4 mm |
| • | `vastag` | Vastag | Gros | 6 mm |

---

## <a name="fustolt-has"></a>Füstölt Has

**Kód:** `946` · **Kategória:** Füstölt Áruk · **Típus:** `weight` · **Ár:** 47.0 RON · **RO:** Piept porc afumat

### Opció — Vastagság

`option_id`: `vastagsag` · `type`: `single_select` · required: `false` · default: `kozepes` · RO label: `Grosime`

| ✓/• | `value_id` | HU | RO | Megjegyzés |
|-----|-----------|-----|-----|------------|
| • | `vekony` | Vékony | Subțire | 2 mm |
| ✓ | `kozepes` | Közepes | Mediu | 4 mm |
| • | `vastag` | Vastag | Gros | 6 mm |

### Opció — Pácolás

`option_id`: `pacolas` · `type`: `single_select` · required: `false` · default: `nem_pacolt` · RO label: `Marinare`

| ✓/• | `value_id` | HU | RO | Megjegyzés |
|-----|-----------|-----|-----|------------|
| ✓ | `nem_pacolt` | Pácolatlan | Nemarinate | — |
| • | `hagyomanyos` | Pácolt — Hagyományos | Marinat — Tradițional | Só, bors, fokhagyma |
| • | `barbecue` | Pácolt — Barbecue | Marinat — Barbecue | Paradicsomos, BBQ-szerű |

---

## <a name="fustolt-nyakas-karaj"></a>Füstölt Nyakas Karaj

**Kód:** `948` · **Kategória:** Füstölt Áruk · **Típus:** `weight` · **Ár:** 49.0 RON · **RO:** Ceafă porc afumat

### Opció — Szeletelés

`option_id`: `szeletes` · `type`: `single_select` · required: `false` · default: `szeletelt` · RO label: `Tăiere`

| ✓/• | `value_id` | HU | RO | Megjegyzés |
|-----|-----------|-----|-----|------------|
| • | `egesz` | Egész | Întreg | — |
| ✓ | `szeletelt` | Szeletelt | Feliat | — |

---

## <a name="novendek-szalami"></a>Házi szalámi

**Kód:** `991` · **Kategória:** Kolbász & Szalámi · **Típus:** `weight` · **Ár:** 46.0 RON · **RO:** Salam de casă

### Opció — Vastagság

`option_id`: `vastagsag` · `type`: `single_select` · required: `false` · default: `kozepes` · RO label: `Grosime`

| ✓/• | `value_id` | HU | RO | Megjegyzés |
|-----|-----------|-----|-----|------------|
| • | `vekony` | Vékony | Subțire | 2 mm |
| ✓ | `kozepes` | Közepes | Mediu | 4 mm |
| • | `vastag` | Vastag | Gros | 6 mm |

---

## <a name="sertes-szalami"></a>Sertés Szalámi

**Kód:** `917` · **Kategória:** Kolbász & Szalámi · **Típus:** `weight` · **Ár:** 43.0 RON · **RO:** Salam de porc

### Opció — Vastagság

`option_id`: `vastagsag` · `type`: `single_select` · required: `false` · default: `kozepes` · RO label: `Grosime`

| ✓/• | `value_id` | HU | RO | Megjegyzés |
|-----|-----------|-----|-----|------------|
| • | `vekony` | Vékony | Subțire | 2 mm |
| ✓ | `kozepes` | Közepes | Mediu | 4 mm |
| • | `vastag` | Vastag | Gros | 6 mm |

---

## <a name="teli-szalami"></a>Téli Szalámi

**Kód:** `9904` · **Kategória:** Kolbász & Szalámi · **Típus:** `weight` · **Ár:** 68.0 RON · **RO:** Salam de iarnă

### Opció — Vastagság

`option_id`: `vastagsag` · `type`: `single_select` · required: `false` · default: `kozepes` · RO label: `Grosime`

| ✓/• | `value_id` | HU | RO | Megjegyzés |
|-----|-----------|-----|-----|------------|
| • | `vekony` | Vékony | Subțire | 2 mm |
| ✓ | `kozepes` | Közepes | Mediu | 4 mm |
| • | `vastag` | Vastag | Gros | 6 mm |

---

## 📊 Statisztika

- **Termékek opcióval:** 15 / 46 (32%)
- **Összes opció definíció:** 20
- **Összes variation érték:** 55
- **Opció-típusok használatban:** `single_select` (20×)

## ⚠️ Megjegyzések

- **Csak `single_select`** van használva Phase 1-ben — a `multi_level` és `text` típusok deklarálva vannak a sémában de még nincs aktív termék velük.
- **Sertés Őrölt Hús (`902`)** — eredetileg 2 opció volt (Alapanyag + Zsírosság), de a termelő tisztázása alapján (2026-05-07) az Alapanyag KIVÉVE — egyelőre nem lehet választani miből legyen őrölve. Csak Zsírosság marad.
- A **Forma** opció a Sertés nyakaskarajnál a meeting-en kifejtett „sima vs dupla" döntés (két szelet középen egyben kinyitva, potyolva).
- A **Pácolás 3 érték** (`nem_pacolt` / `hagyomanyos` / `barbecue`) megerősítve a meeting-en — a hagyományos só+bors+fokhagyma, a barbecue paradicsomos.
- A **Méret opció** csak hybrid termékeknél (csülök, füstölt csülök, csemege csülök) — kisebb/közepes/nagyobb. Sertés Bélszínnél és más termékeknél NINCS méret-választás (max 5-10 deka eltérés).
- **Vastagság (`vekony`/`kozepes`/`vastag`)** szeletelt termékeknél — alaphelyzet `kozepes` (4 mm). A vékony 2 mm, a vastag 6 mm.

---

**Verzió:** 1.0 | **Dátum:** 2026-05-07 | **Forrás:** automatikusan generálva a MASTER MD-kből