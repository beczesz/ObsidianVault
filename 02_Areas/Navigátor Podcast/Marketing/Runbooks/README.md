---
title: Navigátor Podcast — Runbooks
status: active
description: Per-Area runbookok — ismétlődő publikálási folyamatok strukturált receptjei. Egy runbook egy intent-típushoz tartozik (pl. új epizód launch), és előírja milyen csatornákon, milyen időzítéssel, milyen tartalom-formátummal jelennek meg a publikációk. Folyamatosan iterálódik a teljesítmény-feedback alapján.
id: f2f56ad4-2ece-41a9-809d-838227b84b85
index_schema_version: 1
bdos_index: true
tags: [navigator-podcast, runbooks, marketing, playbooks]
---

# Navigátor Podcast — Runbooks

## Mi a runbook?

Egy runbook **egy ismétlődő publikálási intent strukturált receptje**. Megmondja:
- Mit publikálunk (channel-mix)
- Milyen időzítéssel (T+0, T+1, T+7, stb.)
- Milyen tartalom-formátumban (post, reel, follow-up, teaser)
- Milyen prerekvizitumokkal (mit kell előkészíteni az epizódhoz)
- Ki cselekszik (user vs. Presto)

A runbook **template** — amikor egy epizód publikálásra kész, ez generálja az N db Publication-t (Seed → /pres-plan --runbook <name> → N db Publication a `Publications/` mappában).

## Mi NEM a runbook?

- **NEM** egy konkrét epizód state-tracker — azt a CAMPAIGN.md csinálja
- **NEM** Channel DNA — azt a `ChannelDNA/` mappa fájljai csinálják
- **NEM** brand voice / tone — az a MARKETING_ENGINE.md
- **NEM** öröksátén — folyamatosan iterálódik

## Folyamatos finomítás

Minden runbook tartalmaz egy `## Iteration history` szekciót, ahol:
- Mikor módosult
- Mi változott
- Miért (mely metrikára optimalizáltunk)
- Mi volt az eredmény (a következő iteráció előtt)

A runbook **élő dokumentum** — minden epizód-launch után review (mit tanultunk, mit változtatunk).

## Aktív runbookok

| Runbook | Verzió | Státusz | Trigger | Output |
|---|---|---|---|---|
| [episode-launch.md](episode-launch.md) | 0.1.0 | active | Új epizód publikálásra kész | 8 publikáció T+0…T+14 |

## Tervezett runbookok

- `seasonal-recap.md` — évszakos/féléves visszatekintő (terv)
- `guest-anniversary.md` — egy vendég visszahozása (terv)
- `community-question.md` — kérdés-válasz workflow Patreon→YT (terv)

## Schema

A runbook frontmatter `schema: presto.runbook.v1` mezőt használ. Schema-spec inline minden runbook tetején; majd kanonizáljuk a `MARKETING_OS_SCHEMAS_v2.md`-be amikor 2+ runbook él.

## Hivatkozott dokumentumok

- [MARKETING_ENGINE.md](../MARKETING_ENGINE.md) — Navigátor brand-pozíció, voice, KPI, kadencia
- [Pipeline.md](../Pipeline.md) — kanban state
- [ChannelDNA/Navigator-YT.md](../ChannelDNA/Navigator-YT.md) — YouTube channel DNA
- Plugin: `navigator-context-v0.3` skill (metadata-generálás)
- Synthesis: `../../Synthesis/new_video_checklist.md` (operatív 5-fázisos checklist)
- Synthesis: `../../Synthesis/channel.md` (channel intelligence)
- Synthesis: `../../patterns.md` (popularity score modell)
