---
title: "YouTube — Navigátor Podcast"
date: 2026-05-25
author: Becze Szabolcs
status: active
description: "Navigátor Podcast YouTube csatorna operatív profil — elsődleges platform, 354K+ view, 5.7K+ sub, Analytics API aktív."
id: chan-yt-navigator-001
index_schema_version: 1
bdos_index: true
schema: presto.channel-profile.v1
channel: youtube
---

# YouTube — Navigátor Podcast

## Account info

| Mező | Érték |
|------|-------|
| Platform | YouTube |
| Csatorna neve | Navigátor Podcast |
| Handle | `@NavigatorPodcast` |
| URL | https://www.youtube.com/@NavigatorPodcast |
| Brand Account | beczesz.szabolcs@gmail.com |
| Podcast email | navigator.podc@gmail.com |
| Létrehozva | — |
| Státusz | **ACTIVE — PRIMARY PLATFORM** |

## Stats snapshot (2026-04-08 baseline)

| Metrika | Érték |
|---------|-------|
| Összes megtekintés | 354,213 |
| Feliratkozók | ~5,780 |
| Watch minutes (lifetime) | 5,714,247 (95,237 óra) |
| 28 napos views | 8,872 |
| 28 napos net subs | +89 |
| Avg view duration (28d) | 20:19 |
| Avg view duration (lifetime) | 17:05 |
| Publikált epizódok | 41+ |

## Demographics

| Dimenzió | Érték |
|----------|-------|
| Kor 35+ | 89.6% |
| Nő | 53.1% |
| Legnagyobb szegmens | 45-54 (33.3%) |
| Magyarország | 61.7% |
| Románia (Erdély) | 15.8% |
| SK + RS + AT | többi |

## Traffic sources

| Forrás | Arány |
|--------|-------|
| Feliratkozók | 29.8% |
| Suggested/related | 23.7% |
| Shorts | 17.8% |
| External (Facebook stb.) | 7.9% |
| YouTube search | 5.1% |

## Content pattern

- **Top performer téma:** pszichológia / egészség / belső világ (7/10 top videó)
- **Top 6 videó = 56% összes view**
- **Formátum:** 60-120+ perces mélyinterjúk
- **Shorts:** discovery funnel, nem standalone

## API & tooling

| Tool | Státusz |
|------|---------|
| YouTube Data API v3 | ❌ 0 kvóta (audit szükséges) |
| YouTube Analytics API | ✅ teljes hozzáférés |
| YouTube Reporting API | ✅ bulk CSV |
| Chrome MCP workaround | ✅ YouTube Studio |
| navigator-podcast:* skillek | ✅ 9 skill LIVE |

## Presto channel-dna

→ Kanonikus DNA: `00_Prompts/BDOS/agents/presto/channel-dna/youtube.md`
- Tone: `podcast-host-authoritative`
- Language: `hu`

## Kockázatok

- Voice drift (promóciós hang elidegenítheti a 5.7K feliratkozót)
- Format drift (rövid tartalom gyengíti a brandot)
- API constraint (Data API 0-kvóta → Chrome MCP függőség)

## TODO

- [ ] Friss snapshot (utolsó: 2026-04-08)
- [ ] EP42 MMA publikálás
- [ ] Cards audit befejezése (TOP 10 → összes)
- [ ] Spotify cross-link stratégia
