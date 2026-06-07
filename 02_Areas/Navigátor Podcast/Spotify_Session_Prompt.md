---
title: "Navigátor Podcast — Spotify + Dashboard Session Prompt"
date: 2026-05-21
author: Becze Szabolcs
status: active
description: "Spotify integrációs prompt a Navigátor Podcast dashboard fejlesztéséhez, amely három feladatot tartalmaz: meglévő epizódok dátumainak korrigálása, hiányzó epizódok feltöltése és egy interaktív HTML dashboard létrehozása az összes epizód adatainak megjelenítéshez, valamint YouTube Analytics és Spotify státusz nyomon követéshez."
description_source: auto
description_hash: 856653e5539aa45b
id: 9458cc5d-2b64-492e-b9f4-796ccc0cd2ed
index_schema_version: 1
bdos_index: true
---
# Navigátor Podcast — Spotify + Dashboard Session Prompt

> Ez a prompt egy új Claude Code / Cowork sessionbe másolandó.
> Előfeltétel: a `Spotify_Master_Plan.md` fájl a Navigátor Podcast mappában.

---

## Prompt (másolni)

```
Szia! A Navigátor Podcast Spotify integrációján és dashboard-ján dolgozunk.

### Kontextus

Olvasd be a `Spotify_Master_Plan.md` fájlt a Navigátor Podcast mappából — ez tartalmazza az összes tervet, metadatát és instrukciót.

Továbbá olvasd be a `CLAUDE.md`-t is a kontextusért (YouTube API státusz, epizód lista, plugin commands stb.).

### Feladatok

#### 1. Spotify dátumjavítás (Chrome MCP)
- 18 meglévő Spotify epizód publish date-je HIBÁS
- A Master Plan tartalmazza a pontos YouTube dátumokat
- Spotify for Creators URL: https://creators.spotify.com/pod/show/navigatorpodcast/episodes
- Fiók: navigator.podc@gmail.com
- Lépések: Epizód → Edit → Publish date átírás → Save
- Prioritás: EP38, EP39, EP41, EP42 először (2026-05-20 dátumúak), aztán a többi

#### 2. Hiányzó epizódok feltöltése (ha van audio)
- 17 epizód hiányzik Spotify-ról
- A Master Plan tartalmazza az összes metadatát (cím, leírás, YouTube ID, dátum)
- Feltöltés: https://creators.spotify.com/pod/show/navigatorpodcast/episodes/new
- Audio: MP3 fájl szükséges (a felhasználó biztosítja)
- Publish date = YouTube eredeti dátum (backdating, NEM küld notifikációt)

#### 3. Epizód Dashboard generálás
- Készíts egy interaktív HTML dashboard-ot az ÖSSZES Navigátor Podcast epizódról (EP01-EP42)
- Adatforrás: a `Synthesis/Podcast/` mappában lévő .md fájlok + a Master Plan
- A dashboard mutassa:
  - Epizód lista (szűrhető, rendezhető)
  - Platform státusz: ✅ YouTube | ✅/❌ Spotify | Dátumok
  - YouTube analytics: views, watch hours, AVD, subscribers gained
  - Vendég neve, téma, hossz
  - Klaszter/kategória ha van
  - TOP performers kiemelve
  - Spotify feltöltési státusz (feltöltve / hiányzik / dátum javítva)
- Formátum: egyetlen .html fájl (React artifact vagy vanilla HTML+JS)
- Legyen reszponzív, sötét/világos mód, kereshető, rendezhető oszlopok

### Technikai megjegyzések
- YouTube Data API v3 NEM működik (kvóta 0) — NE próbáld használni
- YouTube Analytics API működik (youtube_analytics_* tools)
- Spotify-hoz Chrome MCP kell (creators.spotify.com böngészőautomatizálás)
- A Synthesis/ .md fájlokból kinyerhető: views, watch_hours, avg_view_duration, subscribers_gained, youtube_id, published date, guest info
```

---

## Megjegyzések

- A dashboard-hoz a legjobb ha a `Synthesis/Podcast/` mappát beolvassa és a frontmatter-ből kinyeri az adatokat
- Az EP01-EP07 YouTube dátumait még ellenőrizni kell (YouTube Studio page 3)
- EP40 nincs szintézis fájl → CLAUDE.md-ből kell az alapadatokat venni
- EP41, EP42: szintén nincs szintézis (EP42-nek van SRT, EP41-nek van metadata a CLAUDE.md-ben)
