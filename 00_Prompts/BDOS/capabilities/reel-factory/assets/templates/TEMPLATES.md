---
title: Reel Factory — assets/templates index
date: 2026-05-27
author: Becze Szabolcs
status: living
description: A Reel Factory assets/templates mappa indexe. Brand-konzisztens, reusable templatek (outro, intro, bumper). Minden template a végleges 1080×1920 / 25 fps / h264 / aac specifikációban él, hogy közvetlenül concat-olható legyen a reel output-okkal.
id: 2a098eed-fedb-4c9f-9d20-550502d9d776
index_schema_version: 1
---

# Templates index

## Output spec

Minden template megfelel az alábbi spec-nek (ami a Reel Factory output is):
- **Felbontás:** 1080 × 1920 (9:16)
- **FPS:** 25
- **Video codec:** H.264 (libx264)
- **Audio codec:** AAC

Így a `compose` lépés után közvetlenül concat-olhatóak.

## Templates

### `outro-v0.mp4` — Navigátor Podcast outro logo animation

| | |
|---|---|
| Forrás | YouTube Shorts [XJXbaFW0HJ0](https://www.youtube.com/shorts/XJXbaFW0HJ0), 36.72-39.62 sec |
| Hossz | 2.89 sec |
| Méret | 184 KB |
| Tartalom | Fehér háttér + Navigátor Podcast logo zoom-in animáció (kis iránytű → teljes logo headphones-szal) |
| Mikor használjuk | Minden Navigátor reel végén |

**Beágyazási mód (manuálisan, amíg nincs `compose --outro` flag):**

```powershell
# 1. Hozd létre a concat listfile-t:
@"
file 'reel-mainpart.mp4'
file '..\..\assets\templates\outro-v0.mp4'
"@ | Out-File -Encoding ASCII concat.txt

# 2. Concat (re-encode, mert a két fájl encoder-paraméterei eltérhetnek):
ffmpeg -y -f concat -safe 0 -i concat.txt -c:v libx264 -crf 18 -c:a aac reel-with-outro.mp4
```

**Iter 4 javaslat:** új `compose --outro <path>` flag, ami a kompozit végén concat-olja az outro-t. Vagy új subcommand `append-outro`.

## Forrás-fájlok

A letöltött outro-source.mp4 törölve (2026-05-27, user-jóváhagyással). Újra-letöltés szükség esetén:

```powershell
python scripts/reel.py download "https://www.youtube.com/shorts/XJXbaFW0HJ0" `
    --out assets/templates/outro-source.mp4
```

majd:

```powershell
python scripts/reel.py clip assets/templates/outro-source.mp4 `
    --start "00:00:36.72" --end "00:00:39.62" `
    --out assets/templates/outro-v0.mp4
```
