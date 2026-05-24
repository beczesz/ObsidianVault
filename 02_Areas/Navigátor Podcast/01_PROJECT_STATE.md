---
version: 0.5
date: 2026-04-09
project: Navigátor Podcast
author: Szabolcs (exarlabs@gmail.com)
id: f860e2de-ec35-485b-922f-bdf1f734ab58
index_schema_version: 1
---

# 01_PROJECT_STATE — Navigátor Podcast

## Objective

Magyar vállalkozói podcast mélyreható beszélgetésekkel. Cél: térképet és alapelveket találni egy változó világban vendégekkel együtt. YouTube-központú tartalomstratégia, Patreon közösségépítés, és az epizód-pipeline folyamatos működtetése.

## Current Status

- **Utolsó kiadott epizód:** EP41 – Eberlein Éva (szexuális nevelés), megjelent 2026-03-18
- **Csatorna méret:** 5,780 YouTube feliratkozó, 353,693 összesen nézettség
- **Utolsó 28 nap (Analytics API):** 8,931 views, 2,959 óra watch time (177,511 perc), +87 nettó feliratkozó (+98/-11)
- **Átlagos nézési idő:** 20:06 (1,206 mp) — javulás az előző méréshez képest
- **Engagement:** 167 like, 25 komment, 291 megosztás (utolsó 28 nap)
- **Patreon:** 65 ingyenes tag, ~4 fizető tag (cél: 25 fizető tag)
- **YouTube API státusz:** Analytics API ✅ működik (~200 req/day) | Data API v3 ❌ 0 kvóta (audit pending) | Reporting API ✅
- **Plugin rendszer:** Navigátor Podcast plugin (6 parancs) + YouTube MCP (40 tool)
- **Csatorna audit:** Fázis 4a folyamatban — End Screen ✅, Pinned Comments 62/62 ✅, Cards/SEO következik
- **Új videó checklist:** Elkészült () — 5 fázisú publikálási workflow

## Key Metrics

| Metrika | Jelenlegi | Előző | Cél |
|---|---|---|---|
| YouTube feliratkozók | 5,780 | 5,786 | Növekedés |
| Napi átlag views | 319/nap | 380/nap | 500+/nap |
| Átl. nézési idő (csatorna) | 20:06 | 14:51 | 20:00+ |
| Megosztások (28d) | 291 | — | — |
| Patreon fizető tagok | ~4 | ~4 | 25 |

## Active Problems

1. **Alacsony Impressions CTR:** Az EP41 csak 5.8% CTR-t ért el — a thumbnail/cím vonzó de a retention 12.8% — optimalizálni kell
2. **Shorts stratégia hiányzik:** Csak 3.1% a Shorts-ból jön — kihasználatlan csatorna
3. **Mappa rendetlenség:** Non-md fájlok az Obsidian vault-ban, duplikátumok — takarítási útmutató elkészült
4. **Lejárt feladatok:** Farkas Kinga (EP45 gyász, 2026-02-24 lejárt), Webinar (2026-03-24)
5. **Üres epizód fájlok:** EP45, EP46 üresek — nincs felkészülés
6. **Patreon kampány:** 4 hetes kampány lezárult — eredmények ismeretlenek
7. **Felirat archívum hiányzik:** Csak ~13 SRT van, a többi ~180+ videóhoz le kell tölteni

## Current Focus

- **Fázis 4a: YouTube metadata re-optimalizálás** — aktívan folyamatban
  - ✅ End Screen audit kész (TOP 10 mind megvan, de alacsony hatékonyság hosszú videóknál: 10-15% retention a végén)
  - 🔴 **Cards beállítása** — TOP 10 → fokozatosan összes videó (a terv tematikus klasztereket tartalmaz)
  - ✅ **Pinned Comment** — 62/62 videón cross-promote CTA kitűzve (2026-04-09)
  - 🔴 **Description SEO** — kulcsszavak frissítése, hook az első 2 sorba
  - 🔴 **Channel layout** — 3 hiányzó playlist hozzáadása a főoldalhoz
  - ✅ **Címcsere** — 15/15 videó hook-alapú cím + SEO leírás kész (2026-04-09)
- **Snapshot rendszer létrehozva:**
  - `Synthesis/Snapshot/SNAPSHOT_RULES.md` — szabályrendszer
  - `Synthesis/Snapshot/SNAPSHOT_2026-04-09.md` — baseline snapshot
  - 15/15 cím+leírás re-optimalizáció kész (2026-04-09)
  - Heti mérés, Szabolcs triggereli
- Mappa takarítás (non-md fájlok eltávolítása az Obsidian vault-ból)
- SRT feliratok letöltése yt-dlp-vel az összes videóhoz
- Patreon kampány eredményeinek kiértékelése

## Next Actions

- [ ] Mappa takarítás — temp fájlok, duplikátumok törlése, non-md fájlok áthelyezése (ld. Csatorna Audit Terv.md 1. fejezet)
- [ ] SRT feliratok letöltése: `yt-dlp --write-auto-subs --sub-langs hu --sub-format srt --skip-download -o "%(upload_date)s - %(title)s.%(ext)s" "https://www.youtube.com/@NavigatorPodcast"`
- [ ] Epizódonkénti elemzés elkezdése a Synthesis mappában
- [ ] Patreon eredmények ellenőrzése
- [ ] EP45 (Farkas Kinga - gyász) — új dátum egyeztetése
- [ ] EP46 (Miklós Ervin) — dátum kitűzése

## Constraints

- **Idő:** Szabolcs egyedül csinálja a tartalmat (felvétel, vágás, publikálás)
- **Költség:** ~100 EUR/epizód → ~200 EUR/hó
- **Gyártó:** Szabó Sámuel / Samwork Studios
- **Támogatók:** Média Műhely, Eötvös-udvar, ExarLabs, Vekker Kávéközösség

## Last Updated

2026-04-09 (v0.5 — 15/15 cím+leírás kész, Snapshot rendszer létrehozva, baseline snapshot elkészült)

## Project Map

| Fájl / Mappa                           | Leírás                                                                                    |
| -------------------------------------- | ----------------------------------------------------------------------------------------- |
| `CLAUDE.md`                            | Projektszintű memória és AI instrukciók                                                   |
| `TASKS.md`                             | Aktív feladatlista                                                                        |
| `Csatorna Audit Terv.md`               | Teljes csatorna audit terv, analytics összefoglaló, takarítási útmutató                   |
| `Synthesis/new_video_checklist.md`     | **ÚJ** — Új videó publikálási checklist (5 fázis: Cards, End Screen, Pinned Comment, SEO) |
| `Synthesis/plan.md`                    | Master tracking — audit fázisok és haladás                                                |
| `Synthesis/end_screen_plan.md`         | End screen terv + tematikus klaszterek minden videóra                                     |
| `Synthesis/channel.md`                 | Csatorna-intelligencia, traffic source adatok                                             |
| `Synthesis/synthesis_map.md`           | Összes videó referencia térkép                                                            |
| `memory/projects/navigator-podcast.md` | Részletes projekt kontextus                                                               |
| `memory/context/workflow.md`           | Epizód publikálási workflow                                                               |
| `Episodes/`                            | Epizód-specifikus anyagok                                                                 |
| `Patreon/Patreon Kampányterv 2026.md`  | 4 hetes Patreon kampány terv                                                              |
| `prompts/`                             | YouTube metadata generáló promptok                                                        |
| `~/.youtube-mcp/`                      | YouTube MCP szerver config (client_secret.json, token.json)                               |

## Available Context

- [Google Drive mappa](https://drive.google.com/drive/u/0/folders/1Ou69cPqw3i8vfDp_Q_jvPjb8F5KjbFeI)
- [Social Blade](https://socialblade.com/youtube/channel/UCLGDnb7Zz-pSQ2ANeTiCN2w)
- [YouTube Studio Analytics](https://studio.youtube.com/channel/UCLGDnb7Zz-pSQ2ANeTiCN2w/analytics)
