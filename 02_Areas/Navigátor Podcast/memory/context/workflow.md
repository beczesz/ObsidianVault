---
title: "Navigátor Podcast Workflow"
date: 2026-03-09
author: Becze Szabolcs
status: active
description: "A Navigátor Podcast epizódok publikálásának teljes munkafolyamata: SRT felirat generálása után plugin parancsokkal YouTube metaadat (hook, cím, thumbnail, leírás, időkódok) előállítása, majd videó feltöltése és kereszt-promóció Spotify és közösségi médiában."
description_source: auto
description_hash: 38c965ec1e03b1a6
id: 647b1925-c5ce-4d43-9966-953d6253d642
index_schema_version: 1
bdos_index: true
---
# Navigátor Podcast Workflow

## Epizód publikálási folyamat

### 1. Felvétel után
- SRT felirat fájl generálása a beszélgetésből
- SRT fájl mentése az Episodes mappába

### 2. Metaadat generálás (Plugin használat)

Az SRT fájlból az összes YouTube metaadat előállítható a plugin parancsokkal:

```bash
/hook epizod.srt          # Cold open hook ötletek (5 db, virális pontszámmal)
/cim epizod.srt           # YouTube cím javaslatok (5 db)
/thumbnail epizod.srt     # Thumbnail szövegek (5 db, max 3-4 szó)
/leiras epizod.srt        # SEO-optimalizált leírás + hashtagek
/idokod epizod.srt        # Időkódok (10-12 kulcspillanat)
```

Vagy összevont parancs:
```bash
/navigator-metadata epizod.srt    # Minden metaadat egyszerre
```

### 3. Tartalmi elemek kiválasztása

- Hook kiválasztása (cold open a videó elejére)
- Cím finomítása
- Thumbnail szöveg kiválasztása
- Leírás testreszabása szükség szerint
- Időkódok ellenőrzése

### 4. YouTube publikálás

- Videó feltöltése
- Kiválasztott cím beillesztése
- Leírás + hashtagek hozzáadása
- Időkódok beillesztése a leírásba
- Thumbnail készítés a kiválasztott szöveggel

### 5. Kereszt-promóció

- Spotify publikálás
- Social media posztok
- Newsletter kiküldés (ha releváns)

## Eszközök

- **SRT generálás:** Whisper AI vagy professzionális feliratozó szoftver
- **Metaadat generálás:** Navigator Podcast plugin (Claude Cowork)
- **Thumbnail készítés:** Canva / Photoshop
- **Analytics:** YouTube Studio + Social Blade

## Folyamatban lévő feladatok

- AI-os epizód előkészítése (EP 42, deadline: 2026-03-10)
- Spotify publikálás: Hassan és Palkovics epizód ✓
- ~~Intro az örökbe fogadós részhez~~ → elengedve (lejárt: 2026-02-15)
