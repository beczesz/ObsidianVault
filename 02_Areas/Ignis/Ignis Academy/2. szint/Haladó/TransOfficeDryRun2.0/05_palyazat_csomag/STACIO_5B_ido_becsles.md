---
title: "STÁCIÓ 5.B — Manuális idő-becslés (A.19 prompt) ← **KONTRASZT-PILLANAT**"
date: 2026-05-13
author: Becze Szabolcs
status: active
description: "A.19 prompt szerinti manuális formkitöltés időbecslése: 60 perc feldolgozás, közvetlenül azonban 90 perc reális idő, tekintettel az ellenőrzésre, hibajavításra és szóródási tényezőkre. Részletezett szakaszonkénti időallokáció 13 melléklettel és hosszú szöveges mezőkkel."
description_source: auto
description_hash: ec638abb1843951b
id: a87e50da-ad2b-4e92-bc40-df418526f568
index_schema_version: 1
bdos_index: true
---
# STÁCIÓ 5.B — Manuális idő-becslés (A.19 prompt) ← **KONTRASZT-PILLANAT**

> **Prompt:** A.19 — Ha minden info kéznél van, mennyi idő a form **manuális** kitöltése?
> **Idő:** 5 perc
> **Cowork-futás:** ~30 mp

---

## Idő-számítás kategóriánként

### 1. Egyszerű szöveg/szám mezők (kb. 30 sec/mező átlag)

| Kategória | Mező db | Becsült idő |
|-----------|---------|-------------|
| Cégadatok (10 mező — 8 egyszerű + 2 dropdown) | 10 | 10 × 30 sec = **5 perc** |
| Reprezentant legal (5 mező) | 5 | 5 × 30 sec = **2,5 perc** |
| Pénzügyi adatok (8 mező — figyelmesen másolni!) | 8 | 8 × 45 sec = **6 perc** |
| Impact (5 mező — 1 dropdown + 4 szám) | 5 | 5 × 30 sec = **2,5 perc** |

**Részösszeg:** **16 perc**

### 2. Hosszú szöveges mezők (3-5 perc/mező)

| Mező | Becsült idő |
|------|-------------|
| Titlu proiect | 1 perc |
| Descriere proiect (rezumat, 2000 char) | 5 perc |
| Obiective specifice (1500 char) | 4 perc |
| Egyéb projektleírás-mezők (6) | 6 × 45 sec = **4,5 perc** |

**Részösszeg:** **14,5 perc**

### 3. Mellékletek feltöltése (1 perc/fájl: tallózás + feltöltés + várás + ellenőrzés)

| Mellékletek | Idő |
|-------------|-----|
| 13 fájl × 1 perc | **13 perc** |

### 4. Declarații (checkbox) + ellenőrzés

| Tevékenység | Idő |
|-------------|-----|
| 5 checkbox + linkek olvasása | **3 perc** |

### 5. Teljes form végigellenőrzése (kötelező a véglegesítés előtt)

| Tevékenység | Idő |
|-------------|-----|
| Visszascrollolás, mezőnként újraellenőrzés | **8 perc** |
| 1-2 hiba javítása (átlag) | **2 perc** |

### 6. Beadás (Submit + várás + visszaigazolás letöltés)

| Tevékenység | Idő |
|-------------|-----|
| Final submit + szerver-feldolgozás | **3 perc** |

---

## Összesítés

| Szakasz | Idő |
|---------|-----|
| Cégadatok + Reprezentant + Pénzügy + Impact | 16 perc |
| Hosszú szöveges (Projekt) | 14,5 perc |
| Mellékletek (13 fájl) | 13 perc |
| Declarații | 3 perc |
| Ellenőrzés + hibajavítás | 10 perc |
| Submit + visszaigazolás | 3 perc |
| **TELJES MANUÁLIS IDŐ** | **~ 60 perc** |
| **+ Reális puffer** (figyelem-vesztés, telefon, kávé) | **+ 30 perc** |
| **REÁLIS BECSLÉS** | **≈ 90 perc (1,5 óra)** |

---

## Mit gondolok közben (Cowork-self-talk)

- A „**MINDEN információ kéznél van**" feltétel **nem realisztikus** — a valóságban 15-20 percet rászánok ide-oda lapozgatásra
- A „**gondolkodás nélkül beírom**" sem realisztikus a 2000 char-os mezőknél — ott **fogalmazni kell**
- A **kötelező 55 mező mind hibátlanul kitöltése** = magas mentális teher → fáradtság-eszkaláció a 60. percre
- A **hibajavítás** kötelezően a végén jön, mert a hibákat (pl. dropdown rossz választás) **nem észleli azonnal** a felhasználó

---

## A reális becslésem: **~ 90 perc**

(Ha az adatokat azokat keresgéltem volna közben is, 2,5-3 órás lett volna.)
