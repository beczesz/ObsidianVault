---
title: "Channels Index — Navigátor Podcast"
date: 2026-05-25
author: Becze Szabolcs
status: active
description: "Központi index minden Navigátor Podcast-hoz kapcsolódó social media csatornáról és személyes profilról."
id: idx-channels-navigator-001
index_schema_version: 1
bdos_index: true
---

# Channels Index — Navigátor Podcast

> Presto channel-profile leltár. Minden csatorna külön fájlban, iteratív audit és stratégia-fejlesztésre.

## Navigátor Podcast csatornák

| # | Platform | Típus | Fájl | Státusz | Prioritás |
|---|----------|-------|------|---------|-----------|
| 1 | YouTube | Navigátor Podcast (primary) | [[youtube]] | ✅ Aktív, adatgazdag | **P0** |
| 2 | Instagram | Navigátor Podcast | [[instagram]] | 🔍 Fiók azonosítandó | P1 |
| 3 | Facebook | Navigátor + személyes | [[facebook]] | ⚠️ Aktív, alig dokumentált | P1 |
| 4 | TikTok | Navigátor Podcast | [[tiktok]] | 🔍 Audit szükséges | P2 |
| 5 | X (Twitter) | Személyes | [[x-twitter]] | 🔍 Audit szükséges | P2 |

## Más area-k csatornái (cross-reference)

| # | Platform | Area | Handle | Fájl | Státusz |
|---|----------|------|--------|------|---------|
| 6 | Instagram | Fókuszpont | @fokuszpont_ | `02_Areas/Fókuszpont/Channels/instagram.md` | ❌ Recovery szükséges |

## Megjegyzések

- **YouTube** a primary platform — minden más csatorna ebből derivál vagy ezt támogatja
- **Facebook** a 4. legnagyobb traffic forrás YouTube-hoz (7.9% external), de vault-ban alig dokumentált
- **@fokuszpont_** Instagram NEM Navigator — Fókuszpont imaesemény fiókja (recovery folyamatban)
- **TikTok** és **X** még nem auditált — handle-ek és stats szükségesek
- A felhasználónak további Facebook fiókjai is vannak — később külön dokumentálandók

## Presto channel-dna állapot

| Platform | DNA definiálva? | Lokáció |
|----------|-----------------|---------|
| YouTube | ✅ | `00_Prompts/BDOS/agents/presto/channel-dna/youtube.md` |
| Instagram | ✅ | `00_Prompts/BDOS/agents/presto/channel-dna/instagram.md` |
| X (Twitter) | ✅ | `00_Prompts/BDOS/agents/presto/channel-dna/x-twitter.md` |
| LinkedIn | ✅ | `00_Prompts/BDOS/agents/presto/channel-dna/linkedin.md` |
| TikTok | ❌ | — (létrehozandó) |
| Facebook | ❌ | — (létrehozandó) |

## Következő lépések

1. Iteratív channel review — minden csatorna stats feltöltése
2. Instagram telefonszám csere befejezése
3. Kommunikációs stratégia csatornánként
4. Dashboard készítés (végcél)
