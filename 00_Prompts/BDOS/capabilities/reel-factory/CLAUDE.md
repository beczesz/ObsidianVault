---
title: Reel Factory — Short-form Video Production Capability
version: 0.1-draft
date: 2026-05-27
author: Becze Szabolcs
status: design
description: BDOS capability — YouTube hosszú-formátumból rövid reel (9:16, square, vertical) gyártás Claude Code orchestrációval. yt-dlp + ffmpeg + Whisper alapokon. Eredeti minőségben (nem HD-re csonkított), magyar felirattal, brand-konzisztens template-tel. Első pilot: Navigátor Podcast reelek.
id: 7a3d12e4-9c5f-4b8a-b2e1-8f4d6a9c3e72
index_schema_version: 1
bdos_index: true
---

# Reel Factory

> **Mappanév (canonical):** `reel-factory` · **Brand-név (user-facing):** Reel Factory

> **Státusz:** v0.1-draft, kidolgozás alatt. A pipeline és a template-paletta még tanulási fázisban.

## Cél

Replikálható munkamódszer + Python pipeline, ami YouTube hosszú-formátumból rövid reel-eket gyárt:
- Eredeti minőségű forrás (yt-dlp, nem HD-limit)
- Tetszőleges szegmens kivágás timestamp-tel
- Reframe 9:16-ra (Reels/Shorts/TikTok) vagy 1:1-re (Instagram feed) blurred background-gel
- Magyar felirat Whisper-rel (`medium` model default — Navigátorhoz elég pontos)
- Háttérzene mixelés ducking-gel
- Brand-konzisztens felirat-stílus, intro/outro template

**Első pilot:** Navigátor Podcast reel-ek (Sprint cél: epizódonként 2-3 reel kimegy Instagram + TikTok + YouTube Shorts-ra).

## Trade-off ami miatt épül

| Opus Clip | Reel Factory |
|---|---|
| Vizuális, drag-and-drop | CLI / scripted |
| AI viral-momentum detektálás | User választja a timestamp-eket (later: LLM segíthet) |
| **HD limit** | **Eredeti 4K megőrizve** |
| Magyar felirat: gyengébb | Whisper magyar: jó |
| $$$ subscription | $0 (open source stack) |
| Nem reprodukálható | Egy parancs → reel — template-elve |

A két eszköz nem zárja ki egymást: Opus-szal lehet *megtalálni* a klip-momentumokat, de a renderelést a Factory végzi eredeti minőségben.

## Toolchain

| Tool | Mire | Status (2026-05-27) |
|---|---|---|
| `yt-dlp` | YT letöltés best quality | ✅ installed |
| `ffmpeg` / `ffprobe` | vágás, reframe, mix, burn-in | ✅ installed (C:\Program Files\ffmpeg) |
| `whisper` (OpenAI) | magyar ASR → SRT | ✅ installed |
| `python` 3.12 | orchestrator | ✅ installed |

Lásd [README.md](README.md) install + verify lépésekért.

## Pipeline (v0.1)

```
YT URL + timestamps
        │
        ▼
   1. download    (yt-dlp, best mp4)
        │
        ▼
   2. clip        (ffmpeg -ss/-to)
        │
        ▼
   3. reframe     (ffmpeg crop+scale, blurred bg)
        │
        ▼
   4. transcribe  (whisper → .srt)   ←─── opcionálisan kézzel javítható
        │
        ▼
   5. compose     (ffmpeg: burn subs + music mix + fade)
        │
        ▼
   reel-<slug>.mp4  (1080x1920, ~30-90s)
```

Minden lépés külön subcommand-ként is futtatható (`reel.py download`, `reel.py clip`, …) — iteráláshoz alapvető. A `reel.py full` egyben végigfut.

## Munkamódszer (workflow rules)

Ezek a szabályok minden reel-factory futás során aktívak. Az AI (Claude) MAGÁTÓL kérdez rá / végrehajtja.

### 0. A TELJES EPIZÓD SRT-je MINDIG required input

Mielőtt bármilyen reel-en dolgozunk, az AI **a teljes epizód SRT-jét** olvassa fel forrásként. Ez:
- A **felirat ground truth-ja** — a saját Whisper-futásunk hallucinálhat / félrehallhat. A teljes SRT (manuálisan verifikált vagy professzionális tool-lal készített) felülírja a saját generálást.
- A **cím-generálás kontextusa** — a klip önmagában csonka. A teljes történet (előzmény, szereplők, kulcsszavak) nélkül félrevezető címet írhatnánk (lásd Iter 2: Opus rosszul azonosította a szereplőt — férj helyett valójában édesanya).
- A **leírás forrása** — a vendég neve, az epizód témája, a kulcsfogalmak (pl. „ambiguous loss") onnan derülnek ki.
- A **burned-in subtitle forrása** — a klip-szegmens megfelelő SRT-sorait átemeljük, nem újra-generáljuk. Az időzítést a klip-start offset-tel toljuk.

**Hol keressük az SRT-t:** `02_Areas/Navigátor Podcast/Episodes/EP<NN> - <Téma> - <Vendég>/*.srt`. Ha az AI nem találja → KÉRJ a felhasználótól: "hol van a teljes epizód SRT-je?".

**Bizonyíték hogy ez a szabály miért életbevágó (Iter 2 incident):**
- Iter 1 Whisper: `"...annyi nézd magadra, hát kivel beszéljek, és ennek **korláttam** utoljára"`
- Teljes SRT: `"...anyu nézd magadra, hát kivel beszéljek. **És én ekkor láttam utoljára.**"`
- A két állítás *teljesen más jelentésű*. A beégetett felirat hibás üzenetet közvetített.

### 1. Felirat-helyesség ellenőrzés a `compose` ELŐTT

A Whisper `medium` model magyarul ~95%-os pontosság — a maradék 5% rendre a *kontextus-érzékeny* hibák (eszközterem→tehetetlen, korláttam→korholtam, tulajdonnevek). A burn-in irreverzibilis, ezért:

- A `transcribe` lefutása után az AI **átolvassa a teljes `subs.srt`-t**, és a gyanús szavakat (értelmetlen összetételek, hangzásbeli közeli alternatívák, tulajdonnevek) listázza a felhasználónak javaslattal.
- A felhasználó dönti el: javítja (kézzel a srt-ben vagy diktálja), vagy hagyja.
- Csak ezután futtatja az AI a `compose` lépést.

### 2. Source törlés-prompt a reel(ek) befejezésekor

Egy YT epizódból gyakran több reel készül. A `source.mp4` 1+ GB-os, a vault-on belül van — nem szabad ott felejteni.

- Amikor a felhasználó jelzi, hogy **kész a reel(ek) előkészítésével** egy adott epizódra (jellemzően: "ez jó lesz", "ennyi reel kell", "tegyük közzé"), az AI **megkérdezi**: "Töröljem a `source.mp4`-et? (X.X GB)".
- Default ajánlás: igen, törlés — szegmens-letöltéssel bármikor újra-megszerezhető.
- A `clip.mp4`, `reframed.mp4`, `subs.srt`, `reel-*.mp4` **maradnak** ebben a fázisban.

### 3. Reel-törlés a publikálás után

A publikált verzió Instagram / TikTok / YouTube-on él, a deliverable-mappa csak előkészítő.

- Amikor a felhasználó jelzi, hogy **minden reel fel van töltve / közzétéve** az adott epizódból (jellemzően: "kész vagyok", "ki van rakva", "feltöltöttem"), az AI **megkérdezi**: "Töröljem a deliverable reel-mappát (`<area>/Reels/<slug>/`)? VAGY archiváljam `04_Archive`-ba?".
- Default ajánlás: archiválás (a PUBLISH.md meta-adata érték lehet később), de törlés is OK.
- A capability `output/<slug>/` scratch-mappa szintén törölhető ekkor.

### 4. Iteráció után LEARNINGS frissítés

Minden nem-triviális iteráció (új hiba, új optimalizáció, új default-jelölt) végén az AI bejegyzi a [LEARNINGS.md](LEARNINGS.md)-be. Lásd ott a sablont.

### 5. Tárolási konvenció — HOL él mi

> **Kulcs-elv:** a capability `reel-factory/` mappa **template + script + scratch**. A kész deliverable-ek az **adott terület saját mappájába** kerülnek — soha nem az agent folderbe.

| Mi | Hol | Commit? |
|---|---|---|
| Pipeline script, templatek, doksi | `capabilities/reel-factory/` | igen (a capability része) |
| Reusable template (outro, intro, zene) | `capabilities/reel-factory/assets/templates/`, `assets/music/` | igen |
| Munka-intermediates (source, clip, reframed, subs) | `capabilities/reel-factory/output/<slug>/` | **nem** (gitignore, scratch) |
| **Kész deliverable (reel + PUBLISH.md)** | **`02_Areas/<terület>/.../<EpisodeOrUnit>/Reels/<reel-slug>/`** | a terület dönt |

**Példa (Navigátor):** `02_Areas/Navigátor Podcast/Episodes/EP43 - Gyász - Farkas Kinga/Reels/reel-01-anyu-nezd-magadra/` → `reel-01-anyu-nezd-magadra.mp4` + `PUBLISH.md`.

**Más terület** (DH, Sonrisa, ExarLabs) ugyanígy: a saját mappájában, a saját egység-struktúrája szerint. A `reel.py publish --dest <area_reels_dir> --slug <slug>` automatizálja: létrehozza a per-reel mappát, bemásolja a videót, scaffold-ol egy `PUBLISH.md`-t.

Részletes módszertan: [METHODOLOGY.md](METHODOLOGY.md).

---

## Struktúra

```
capabilities/reel-factory/              ← AGENT (template + script + scratch)
├── CLAUDE.md         ← ITT — meta, belépő, workflow rules
├── METHODOLOGY.md    — kanonikus reprodukálható módszertan (ezt olvasd reel előtt)
├── README.md         — install + quick start + parancsok
├── LEARNINGS.md      — iteratív tanulási napló (minden próba után írjuk)
├── scripts/
│   └── reel.py       — fő pipeline (download/clip/reframe/extract-subs/compose/full/publish)
├── assets/
│   ├── music/        — háttérzene library (royalty-free, brand-jóváhagyott)
│   ├── fonts/        — felirat font-ok
│   └── templates/    — reusable brand templatek (outro-v0.mp4 + TEMPLATES.md)
├── compare/          — referencia-elemzések (pl. Opus reel)
└── output/<slug>/    — SCRATCH intermediates (gitignore, törölhető)

02_Areas/<terület>/.../Reels/<reel-slug>/  ← DELIVERABLE (a terület mappája)
├── <reel-slug>.mp4   — a publikálandó videó
└── PUBLISH.md         — cím + platform-leírások + tagek + checklist
```

## Open questions / döntésre vár

- [x] **Reframe stratégia default:** ✅ blurred-bg (működik bárhol a beszélő). Dynamic-zoom/face-tracking később (v0.3+).
- [x] **Felirat stílus:** ✅ Arial Bold 18, white + outline, MarginV 70, **word-fragment 3 szó** (Opus-stílusú karaoke). Finomítás: Segoe UI Black (libass nem találta), BorderStyle=4 box — nyitva.
- [x] **Aspect ratio default:** ✅ 9:16. 1:1 variáns külön kérésre (`--aspect 1:1`).
- [x] **Outro:** ✅ `assets/templates/outro-v0.mp4` auto-concat minden reel végén.
- [ ] **Háttérzene forrás:** YouTube Audio Library? Pixabay? Saját collection? *(nincs default, user adja meg)*
- [ ] **LLM-segített klip-választás:** transcript alapján LLM jelöli a momentumokat? *(v0.4 kísérlet)*
- [ ] **Fragment-időzítés** szótag-hossz szerint (most szó-szám-arányos).
- [ ] **Intro / brand-bumper** a reel ELEJÉN? (jelenleg csak outro)
- [ ] **Dynamic zoom / face-tracking** reframe (Opus-szerű vizuális változatosság).

## Hivatkozott

- BDOS belépő: [`../../CLAUDE.md`](../../CLAUDE.md)
- Navigátor pilot: [`../../../../02_Areas/Navigátor Podcast/`](../../../../02_Areas/Navigátor%20Podcast/)
- Presto agent (distribution): [`../../agents/presto.md`](../../agents/presto.md) — a kész reel-eket Presto adapt-eli platformra
