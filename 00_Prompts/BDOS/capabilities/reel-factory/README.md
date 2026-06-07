---
title: Reel Factory — README
date: 2026-05-27
author: Becze Szabolcs
status: draft
description: Reel Factory capability quick start — install, parancsok, példák. Fő dokumentáció a CLAUDE.md, ez a használati gyorsindító.
id: 37019350-ad8b-49bb-90a5-af7f7b3d8992
index_schema_version: 1
---

# Reel Factory — Quick Start

## Install ellenőrzés

A toolchain ezeket igényli:

```powershell
ffmpeg -version    # ✅ várhatóan: C:\Program Files\ffmpeg\bin\ffmpeg.exe
ffprobe -version
whisper --help     # OpenAI Whisper
yt-dlp --version
python --version   # 3.10+
```

Hiányzó tool esetén:
- **yt-dlp:** `python -m pip install --upgrade yt-dlp`
- **whisper:** `python -m pip install --upgrade openai-whisper` (első indításkor letölti a modellt)
- **ffmpeg:** [ffmpeg.org/download](https://ffmpeg.org/download.html) → add to PATH

## Parancsok

### End-to-end (legtöbb esetben ezt akarod)

```powershell
python scripts/reel.py full `
    "https://www.youtube.com/watch?v=XXXX" `
    --slug navigator-ep40-fegyelem-01 `
    --start 12:34 `
    --end 13:22 `
    --aspect 9:16 `
    --music "assets/music/calm-loop.mp3"
```

Eredmény: `output/navigator-ep40-fegyelem-01/reel-navigator-ep40-fegyelem-01.mp4`

### Lépésenként (iteráláshoz)

```powershell
# 1. letöltés (csak egyszer / epizódonként)
python scripts/reel.py download "https://www.youtube.com/watch?v=XXXX" `
    --out output/ep40/source.mp4

# 2. klip kivágása
python scripts/reel.py clip output/ep40/source.mp4 `
    --start 12:34 --end 13:22 `
    --out output/ep40/clip.mp4

# 3. reframe 9:16-ra blurred bg-vel
python scripts/reel.py reframe output/ep40/clip.mp4 `
    --aspect 9:16 `
    --out output/ep40/reframed.mp4

# 4. felirat generálás (lehet kézzel javítani utána)
python scripts/reel.py transcribe output/ep40/reframed.mp4 `
    --lang Hungarian --model medium `
    --out output/ep40/subs.srt

# 5. compose — felirat beégetés + zene mixelés
python scripts/reel.py compose output/ep40/reframed.mp4 `
    --subs output/ep40/subs.srt `
    --music assets/music/calm-loop.mp3 `
    --music-vol 0.15 `
    --out output/ep40/reel-final.mp4
```

## Tippek

- **Felirat kézi javítás:** Whisper magyar `medium` model kb. 95%-os pontosság — érdemes a `subs.srt`-t átolvasni és tulajdonneveket / szakszavakat javítani **a `compose` előtt**. VS Code-ban nyitva trivi.
- **`--model large`** akkor, ha tudsz várni 5-10 percet egy 60mp-es klipre, és pontos felirat kell.
- **`--music-vol`** alapérték 0.15 = halk háttér. 0.08 = nagyon halk, 0.25 = jól hallható, 0.40+ = előtérben.
- **Aspect váltás:** `--aspect 1:1` ha Instagram feedhez kell, `--aspect 9:16` Reels/Shorts/TikTok.
- **Slug konvenció:** `<projekt>-ep<n>-<téma>-<sorszám>`. Pl.: `navigator-ep40-fegyelem-01`.

## Hibakeresés

| Hiba | Ok | Fix |
|---|---|---|
| `'yt-dlp' is not recognized` | pip install nem PATH-on | `python -m yt_dlp` vagy `Scripts/yt-dlp.exe` direkt |
| Subtitle filter `cannot find file` | Windows path-colon escape | a script már `cwd`-be másol → nem szabadna előjönnie. Ha mégis: ellenőrizd hogy a stage_subs.srt létrejött az output dir-ben |
| Whisper "out of memory" | `large` model + nincs GPU | használj `medium`-ot vagy kisebbet |
| Zene túl hangos / túl halk | `--music-vol` rossz | finomítsd, 0.10–0.20 jó tartomány |
| Reframe blurred bg túl sötét | `eq=brightness=-0.10` túl alacsony | scripts/reel.py-ban a `REFRAME_FILTERS`-ben módosítsd |
| `UnicodeEncodeError: charmap` | Windows console cp1252, non-ASCII karakter (→, ékezet) `print`-ben | a script már `sys.stdout.reconfigure("utf-8")`-cal indít. Ha mégis: `chcp 65001` előtte, vagy `PYTHONIOENCODING=utf-8` env var |
| Whisper `CUDA error: no kernel image is available` | Telepített PyTorch CUDA kernel inkompatibilis a GPU-val | A script default `--device cpu`-val indul. Explicit override: `--device cuda` (de itt nem fog menni). |
| Whisper `Skipping ... due to UnicodeEncodeError` magyar `ű`/`ő`-n | Whisper saját `print()` cp1252-ben, és emiatt nem ír SRT-t | A script már átadja `PYTHONIOENCODING=utf-8`-at a whisper subprocessnek — nem szabadna előjönnie. Ha mégis: kézzel `$env:PYTHONIOENCODING="utf-8"` előtte. |

## Output struktúra

```
output/<slug>/
├── source.mp4      ← teljes YT letöltés (újrahasznosítható ha több reel kell egy epizódból)
├── clip.mp4        ← trim eredménye
├── reframed.mp4    ← 9:16 / 1:1
├── subs.srt        ← Whisper output (kézzel javítható)
├── stage_subs.srt  ← compose-időben használt másolat
└── reel-<slug>.mp4 ← FINAL
```

`source.mp4` jelentősen nagyobb (akár 1+ GB) — ha kifogysz a helyből, törölhető, csak az újra-letöltés a költség.

## Tanulási napló

Minden nem-triviális iteráció után írd be a tanulságot ide:
[`LEARNINGS.md`](LEARNINGS.md)
