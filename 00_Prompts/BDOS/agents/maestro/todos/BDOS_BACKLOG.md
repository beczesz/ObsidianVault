---
title: BDOS Backlog, Maestro-managed cross-family TODO list
date: 2026-05-27
author: Becze Szabolcs
status: active
description: A BDOS rendszer egészét érintő future ideas és nem-sürgős fejlesztések. Maestro kezeli (ő a családi karmester). NEM per-agent TODO — minden olyan ami egynél több agentet érint, vagy infrastrukturális, vagy stratégiai. Per-agent TODO-k a saját agent mappájukban élnek.
tags: [bdos, backlog, todo, maestro, future]
id: 4e8c9f1a-7b3d-4a52-9e1f-6c8b2d5a3f47
index_schema_version: 1
bdos_index: true
---

# BDOS Backlog, Maestro-managed

> **Cél:** rögzíteni mindent ami a BDOS családot érinti, de még nem futtatható feladat. Maestro `team-status` / `team-audit` mód-ban átolvassa ezt, és releváns lépéseknél javaslatot tesz.
>
> **NEM ide tartozik:** per-agent TODO (`agents/<name>/todos/`), aktív sprint-feladat, egyszeri tisztogatás.

## Schema

Minden item:

```yaml
- id: <kebab-case-slug>
  title: <egy mondat>
  created: <YYYY-MM-DD>
  triggers: [<which-agent-or-capability>]
  priority: <low|medium|high>
  effort: <small|medium|large>
  status: <idea|spec-needed|spec-ready|in-progress|done|wontfix>
  notes: |
    Részletek, miért fontos, mi a következő konkrét lépés.
```

---

## Active backlog

### 1. Video upload pipeline a Presto számára (hybrid API + Playwright)

- **id:** `presto-video-upload`
- **created:** 2026-05-27
- **triggers:** Presto, Think Engine v0.10, Reel Factory capability
- **priority:** medium
- **effort:** medium (egy délutáni munka az alapra, platform-onként 200-400 sor)
- **status:** spec-ready
- **notes:** |
  Presto jelenlegi `/pres-publish` csak manual-fallback TODO-t generál. A valódi automatizáció hibrid uploader-pattern-t igényel:
  
  - **Elsődleges útvonal: hivatalos API-k** (YouTube `videos.insert`, Facebook Graph, Instagram Content Publishing, LinkedIn UGC). Cost: pl. YouTube 1,600 quota-unit/upload, 10K default napi quotán = ~6 upload/nap, Navigátor cadence-nek elég.
  - **Fallback: Playwright** (Think Engine v0.10 runtime alatti `uploaders/`). Csak akkor, ha API nem elérhető, ÉS a user explicit engedélyezte (kockázatos platformokon — YouTube/TikTok — dupla confirmation).
  - **Riziko:** YouTube/TikTok aktívan detektálja a Studio/web upload automatizmust → channel suspension. Ezért API-first.
  
  Konkrét next step a v0.10 cool-down után:
  1. `uploaders/youtube-api.mjs` — `videos.insert` wrapper, OAuth + quota validation, dry-run mód
  2. `uploaders/_template.mjs` — generic interface (transport, capabilities, riskLevel, upload(), schedule())
  3. `/pres-publish` slash command refactor — uploader-router, API-first, Playwright fallback engedélylevéllel
  4. Smoke test: Navigátor unlisted teszt-video felmegy a YouTube-ra API-n keresztül, metadata helyes
  
  Részletek: lásd a Think Engine v0.10 SKILL.md "out of scope" szekciójának kibővítését.

### 2. Maestro skill: agent portrait prompt generator

- **id:** `maestro-agent-portrait-skill`
- **created:** 2026-05-27
- **triggers:** Maestro, agent family
- **priority:** low
- **effort:** small (kész)
- **status:** done — 2026-05-27
- **notes:** |
  Pixar-stílusú robot profil-kép prompt-okat generál minden agentre. Reusable style template + per-agent prompt fájlok.
  
  Hely: `00_Prompts/BDOS/agents/maestro/skills/agent-portrait/`

---

## How to add a new item

1. Másold a schema sablont fent
2. Adj egy kebab-case `id`-t (unique vault-szinten)
3. Töltsd ki, status: `idea` vagy `spec-needed`
4. Maestro `team-status` mód-ban újra elolvassa, és releváns lépésnél felhozza

## How Maestro should use this

`team-status` / `team-audit` / `next` módokban Maestro **olvashatja** ezt a fájlt, és:
- Felhozhatja a relevant backlog item-eket ("még él a Presto video-upload TODO")
- Promote-olhat item-eket `idea` → `spec-needed` → `in-progress`-re user-confirmation-nel
- Új item-eket adhat hozzá (csak confirmation után)

Soha nem törli automatikusan a `done` item-eket — a historyt megőrizzük itt.
