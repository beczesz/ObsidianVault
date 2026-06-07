---
title: Opus Clip reel — referencia-elemzés (z.mp4)
date: 2026-05-27
author: Becze Szabolcs
status: reference
description: Opus Clip által gyártott reel vizuális + szöveges elemzése. Forrás: C:/Users/EvoComputers/Downloads/z.mp4 (44.5s, 1080×1920, 8 Mbps). Cél: a Reel Factory default-jainak finomítása (felirat-stílus, title-card, dynamic zoom) a megfigyelt Opus-mintákra.
id: 1095c113-5505-4a8a-885a-78fc7b815417
index_schema_version: 1
---

# Opus Clip reel — referencia-elemzés

**Forrás:** `C:/Users/EvoComputers/Downloads/z.mp4`
**Tárolva:** `compare/opus-z-2026-05-27/frames/` — 12 referencia-frame (0.3s, 1, 2, 5, 10, 15, 20, 25, 30, 35, 40, 43s)
**Whisper transcript:** `z.srt` (background job)
**Dátum:** 2026-05-27

## Forrás-meta

| | |
|---|---|
| Hossz | 44.52 sec |
| Felbontás | 1080 × 1920 (9:16) |
| Codec | H.264 + AAC |
| Bitrate | **8.12 Mbps** (a mi 1.3 Mbps-ünk vs ez — kb. 6x magasabb) |
| FPS | 25 |
| Méret | 45 MB |

## 1. Title card (a "tetjén megjelenő cím")

**Példa-szöveg:** `Évekig kereste az eltűnt férjét`

### Vizuális paraméterek

| Tulajdonság | Megfigyelés |
|---|---|
| **Pozíció** | Felső sáv, kb. 8-10% margin a tetejétől |
| **Háttér** | Fehér, rounded rectangle (pill) |
| **Border-radius** | ~16-20px |
| **Padding** | ~20px horizontal, ~16px vertical |
| **Text-szín** | Sötét (fekete vagy nagyon sötét szürke) |
| **Font-család** | Bold sans-serif (Inter / SF Pro / Montserrat-szerű — modern, geometrikus) |
| **Font-weight** | Bold (~700) |
| **Font-méret** | ~36-40px (a vásznon a karakterek ~3-4% canvas height) |
| **Sortörés** | 2 sor, center-aligned |
| **Megjelenés** | Csak az **első 3-4 másodperc** alatt látható, utána eltűnik |
| **Animáció** | Nem egyértelmű (statikus a megfigyelt frame-ekben), de Opus szokott fade-in / pop-in-t használni |

### Megfigyelés

A title card a **horog / teaser** — a kontextust kommunikálja egy mondatban. A burned-in subtitle ettől függetlenül halad a beszélő tényleges szavaival. Külön réteg, külön funkció:
- **Title:** "miről szól ez a klip" (statikus, néző behúzás)
- **Subtitle:** "mit mond éppen most" (dinamikus, érthetőség)

## 2. Subtitle (az alsó beszéd-felirat)

**Megfigyelt fragmentumok időrendben:**
| Időpont | Fragment |
|---|---|
| 0.3s | "És én ekkor" |
| 1.0s | "láttam utoljára" |
| 2.0s | *(üres — szünet)* |
| 5.0s | "képzelni azt az" |
| 10.0s | "vagy az" |
| 15.0s | "fölakasztva" |
| 20.0s | "összeesve" |
| 25.0s | "százalékában" |
| 30.0s | "szembe" |
| 35.0s | "éltem az" |
| 40.0s | "azt pásztáztam" |
| 43.0s | "talán ő" |

### Vizuális paraméterek

| Tulajdonság | Opus (megfigyelve) | A mi v0.1-ünk |
|---|---|---|
| **Szín** | Fehér | Fehér ✓ |
| **Outline** | **NINCS heavy outline** — csak finom drop shadow | Heavy fekete outline (Outline=2) |
| **Font** | Bold geometrikus sans-serif (Inter / Montserrat-szerű) | Arial |
| **Font-weight** | Bold (700) | Default (~400) |
| **Font-méret** | ~14-16% canvas-hez képest (nagyon olvasható) | Fontsize=14 (kisebb) |
| **Pozíció** | Lower third, ~25-30% a fenékről | MarginV=180 (~17% a fenékről) |
| **Szótördelés** | **1-3 szó / pillanat** (karaoke-style) | Mondat-egységek (3-6 másodpercig 8-12 szó) |
| **Időzítés** | Frame-pontos a beszédhez | Whisper szegmensek (3-7 sec mondat-darabok) |

### A LEGNAGYOBB különbség: szótördelés

Opus **rövid fragmenseket** csinál (1-3 szó), amik **gyorsan haladnak** — minden szó nagyjából akkor jelenik meg, amikor elhangzik. Ez:
- **Olvashatóság:** könnyű egy pillantással elkapni
- **Tempó-érzet:** dinamikusabb, "feszesebb" reel
- **Figyelem-fenntartás:** a változó szöveg miatt a néző tovább néz

A mi v0.1-ünk teljes Whisper-szegmenseket vág 1 sorba (5-10 szó / 3-7 sec) — statikusabb, kevésbé olvasható szkrollozás közben.

### Technikai megvalósítás

Opus-szerűen kéne:
1. **Word-level timestamp**-eket kérni a Whisper-től (`--word_timestamps True`)
2. Saját logikával **N=1-3 szóra** tördelni a fragmenseket
3. Új `.ass` (Advanced SubStation Alpha) fájlt írni szóra pontos time-stamping-gel
4. ffmpeg `subtitles=` filter az ASS-t is támogatja, csak az `srt` helyett `.ass`-ot adunk be

## 3. Reframe — NEM blurred-bg

Ez fontos: **az Opus reel nem blurred-bg**-t használ, mint mi.

### Megfigyelés
- 0-30s: a beszélő **álló alakja** látható a vásznon teljes magasságban — a forrás vagy már 9:16, vagy Opus okos crop-ot csinál
- 5s: rövid B-roll / másik kamera-szög, kicsi letterbox-szel
- **35-43s: ZOOM IN** — a beszélő arca tölti ki a vászon nagy részét (close-up)

Tehát Opus **dynamic crop**-ol: alapból medium shot, kulcs-pillanatokban beapproximál close-up-ra. Ez:
- Vizuális változatosságot ad (35+ másodperc statikus shot unalmas lenne)
- Az érzelmi csúcsoknál (a 35-43s rész valószínűleg a klimax) közelebb visz

### A mi v0.1 blurred-bg-jével szemben

A blurred-bg "biztonsági megoldás" — működik bármilyen forrásra, és nem rossz, **de unalmasabb mint a dynamic zoom**.

**Trade-off:**
- Dynamic zoom **face-detection**-t igényel (pl. mediapipe / opencv haar cascade) — komplexebb pipeline
- Blurred-bg **deterministikus**, működik kameraszög-független

Lehetséges v0.2 hibrid: ha a forrás már 16:9 portrait-ban "jól keretezett" (a beszélő középen, álló alak), akkor **direct crop** (központ kivágás) — blurred-bg nélkül. Ha rosszul keretezett, akkor blurred-bg.

## 4. Audio / zene

A megfigyelt 11 frame-ből nem hallhatok zenét, de:
- A 8 Mbps bitrate mintegy fele valószínűleg vizuális adat → a hang AAC-ben kb. 128-192 kbps
- Az Opus klasszikus output-ja **discrete background music**-kal van keverve (gyakran sub-LUFS szinten)
- A `compose` lépésünk ehhez kész — csak a `--music-vol 0.10-0.15` környékre kell pontosítani

## 5. Összegzés — mit változtassunk a Reel Factory-ban

### Default-okat finomítani (Iter 2):

1. `SUBTITLE_STYLE`:
   - `Fontname=Arial` → ami modern bold sans-serif elérhető rendszeren (kísérlet: `Montserrat`, `Inter`, fallback `Segoe UI Black` Windows-on)
   - `BorderStyle=1, Outline=2` → `BorderStyle=4, Outline=0, BackColour=&H80000000` (semi-transparent box) VAGY `BorderStyle=1, Outline=1, Shadow=1` (finomabb)
   - `Fontsize=14` → `Fontsize=18-22` (Opus nagyobb)
   - `MarginV=180` → `MarginV=350-400` (Opus tovább letolja)

2. **Word-level subs** — új subcommand: `transcribe --word-level --max-words-per-frag 3` → `.ass` output. Ez a legnagyobb látható különbség, érdemes priorizálni.

3. **Title card support** — új subcommand vagy `compose` flag: `--title "Évekig kereste az eltűnt férjét" --title-duration 3.5` — overlay a top 8%-on, white pill bg, bold dark text.

4. **Dynamic crop opcionális mód** — v0.3+: face-detection alapú zoom. Egyelőre maradunk a blurred-bg-en, mert van face-tracking nélkül is működő alternatíva.

### NEM másoljuk:

- A specifikus 8 Mbps bitrate — overkill, 2-3 Mbps elég IG/TikTok-ra (azok úgyis re-kompresszálnak)
- Pixel-pontos border-radius / padding — "elég közel" szint elegendő

## 6. Teljes Whisper transcript (saját, medium model, CPU)

Az Opus reel hangsávjából a mi Whisper-ünkkel:

```
1  00:00:00,000 → 00:00:05,820   és ennek korlágtam utoljára. Nem tudom, hogy el tudod eképzelni azt az érzést,
2  00:00:05,920 → 00:00:11,020   amikor így mézsz a mezőkön, gumicsizmában vagy az erdőben,
3  00:00:11,120 → 00:00:17,820   és így azt várod, hogy hol lesz fölakasztva, vagy hol lesz a földön,
4  00:00:17,920 → 00:00:21,900   vagy hol lesz összeesve. Az egyetemi éveim alatt,
5  00:00:22,000 → 00:00:26,380   én Kolozsváron az időm 90 százalékában úgy jártam,
6  00:00:26,380 → 00:00:30,760   kéltem az utcákon, hogy azt figyeltem, hogy hát, ha szembe jön valahol,
7  00:00:30,860 → 00:00:35,800   egy ilyen homályos állapotban éltem az életemet,
8  00:00:35,900 → 00:00:40,360   hogy igazából nem tudtam jelen lenni soha. Tehát mindig azt pásztáztam,
9  00:00:40,460 → 00:00:44,360   azt figyeltem, hogy talán ő szembe jön az utcán.
```

### Whisper-hibák (saját átolvasás workflow alapján)

| Whisper kiadta | Helyesen | Megjegyzés |
|---|---|---|
| `korlágtam` | `korholtam` | iter 1-ben is így rontotta — visszatérő minta |
| `el tudod eképzelni` | `el tudod-e képzelni` | kötőjel-tagolás |
| `mézsz` | `mész` | accent-hiba |
| `kéltem` | `keltem` *(vagy: jártam-keltem)* | accent-hiba |

### Cross-reference — az iter 1 klipjével

**Ez ugyanaz az epizód.** A beszélő ott (iter 1, 00:00-00:37) elmeséli, hogy 18 évesen "korholt utoljára" valakit ("…és ennek korholtam utoljára"). Ez a klip pontosan **azzal a mondattal kezdődik**, és onnan folytatja: éveken át kereste az illetőt mezőkön, erdőkben — várva, hogy fölakasztva, vagy összeesve találja meg.

**Következtetés:** a téma egy **közeli családtag öngyilkosság-utáni hosszú gyász és keresés** — nem férj. Opus címe (`Évekig kereste az eltűnt férjét`) téves vagy félrevezető, mert:
- A klipben nem hangzik el a `férj` szó
- Az iter 1 kontextusból: 18 évesen történt → valószínűbb hogy szülő (apa)
- A `férjét` szó nem jelenik meg a Whisper-transcriptben (sem az iter 1, sem ennek a klipnek a teljes szövegében)

→ **Saját címet kell írni** — lásd: [TITLE_AND_DESCRIPTION_DRAFTS.md](TITLE_AND_DESCRIPTION_DRAFTS.md) frissítve.

## 7. Hivatkozott

- A frame-ek: `frames/{000.3,001.0,002.0,005.0,010.0,015.0,020.0,025.0,030.0,035.0,040.0,043.0}.png`
- Whisper transcript: `z.srt` (a clip teljes szövege)
- Forrás videó: `C:/Users/EvoComputers/Downloads/z.mp4` (44.5s)
