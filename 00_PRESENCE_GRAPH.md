---
title: "Presence Graph — Összes szervezeti jelenlét"
date: 2026-05-25
author: Becze Szabolcs
status: active
description: "Központi registry minden szervezetről és csatornáról, amit Becze Szabolcs kezel. Graph áttekintés: 9 szervezet, 14+ csatorna, 1 személyes profil hub."
id: idx-presence-graph-001
index_schema_version: 1
bdos_index: true
schema: presto.presence-registry.v1
total_orgs: 8
---

# Presence Graph

> Szabolcs Becze összes szervezeti és személyes közösségi média jelenléte.
> Minden szervezet `presence.md` fájlja az adott Area gyökerében él (`schema: presto.org-presence.v1`).

## Graph overview

```
                    ┌─────────────────────┐
                    │   Szabolcs Becze     │
                    │   (személyes profil) │
                    │   FB / IG / X / TT   │
                    └──────────┬──────────┘
                               │ manages (7 pages)
          ┌────────────────────┼────────────────────┐
          │                    │                     │
    ┌─────┴─────┐    ┌────────┴────────┐    ┌──────┴──────┐
    │ Navigátor  │    │   Fókuszpont    │    │  ExarLabs   │
    │ Podcast    │    │                 │    │             │
    │ YT/FB/SP   │    │   FB / IG ⚠️    │    │    FB       │
    └───────────┘    └────────┬────────┘    └─────────────┘
                              │ recovery chain
          ┌───────────────────┼───────────────────┐
          │                   │                    │
    ┌─────┴─────┐    ┌───────┴───────┐    ┌──────┴──────┐
    │ Média      │    │  Arhitectura  │    │  IgnisCafe  │
    │ Műhely     │    │  Mikado       │    │             │
    │ FB (22!)   │    │  FB           │    │    FB       │
    │ ⚠️ KEY     │    └───────────────┘    └─────────────┘
    └───────────┘
          │
    ┌─────┴─────┐
    │ Vezetők   │
    │ Imája     │
    │ FB        │
    └───────────┘
```

## Szervezeti leltár

| # | Szervezet | Area | Platforms | Presence fájl | Státusz |
|---|-----------|------|-----------|---------------|---------|
| 0 | **Szabolcs Becze** | `02_Areas/Személyes/` | FB, IG, X, TT | [[presence\|személyes]] | ✅ Hub |
| 1 | **Navigátor Podcast** | `02_Areas/Navigátor Podcast/` | YT, FB, SP, IG(?), Patreon | [[presence\|navigator]] | ✅ Legérettebb |
| 2 | **Fókuszpont** | `02_Areas/Fókuszpont/` | FB, IG | [[presence\|fokuszpont]] | ⚠️ IG recovery |
| 3 | **ExarLabs** | `02_Areas/ExarLabs/` | FB | [[presence\|exarlabs]] | 🔍 Audit |
| 4 | **Arhitectura Mikado** | `02_Areas/Mikado/` | FB | [[presence\|mikado]] | 🔍 Audit |
| 5 | **IgnisCafe** | `02_Areas/Ignis/` | FB | [[presence\|ignis]] | 🔍 Audit |
| 6 | **Média Műhely** | `02_Areas/Média Műhely/` | FB | [[presence\|mediamuhely]] | ⚠️ Key email |
| 7 | **Vezetők Imája** | `02_Areas/Személyes/` | FB | [[vezetok-imaja-presence\|vezetok]] | 🔍 Audit |

## Platform összesítő

| Platform | Aktív fiókok | Szervezetek |
|----------|-------------|-------------|
| **Facebook** | 1 profil + 8 page | Mind a 9 |
| **YouTube** | 1 csatorna | Navigátor Podcast |
| **Instagram** | 2 profil | Személyes (@beczesz) + Fókuszpont (@fokuszpont_) |
| **X (Twitter)** | 1 profil | Személyes |
| **TikTok** | 1 profil | Személyes |
| **Spotify** | 1 (?) | Navigátor Podcast (nem auditált) |
| **Patreon** | 0 (planned) | Navigátor Podcast |

## Recovery issues

| Fiók | Probléma | Blocker | Akció |
|------|----------|---------|-------|
| @fokuszpont_ (IG) | Asszisztens telefonszáma | mediamuhely11@gmail.com jelszó | Peter Maria-tól kérni |
| fokuszpont2024@gmail.com | Hozzáférés hiányzik | mediamuhely11@gmail.com | Recovery email lánc |

## Query patterns

```bash
# Összes presence fájl
python3 query.py --fts "org-presence"

# Facebook page-ek
python3 query.py --fts "Facebook page"

# Recovery problémás fiókok
python3 query.py --fts "recovery-needed"

# Adott szervezet
python3 query.py --fts "Fókuszpont jelenlét"
```
