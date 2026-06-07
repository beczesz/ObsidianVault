---
title: Curator promote backlog
date: 2026-05-25
author: Becze Szabolcs
status: active
description: Curator `/dash-promote` mód várólistája. Itt élnek a promote-tervek (egy fájl per pattern-család), amelyek a Sprint 0–6 refactor során kiderültek de mechanikus migrációval nem megoldhatók. Minden terv: divergencia-felmérés, kanonikus döntés-javaslat, rollout-lépések, kockázat. Curator `/dash-promote <fájl>` futtatja végig őket.
tags: [dashboards, curator, promote, backlog]
id: 518ec564-2c7d-4080-bf42-162865705631
index_schema_version: 1
---

# Curator promote backlog

A Sprint 0–6 refactor során kiderült, hogy két pattern-család **nem mechanikusan migrálható** — humán + Curator döntésre van szükség:

| Backlog item | Becsült LOC nyereség | Komplexitás | Fájl |
|---|---|---|---|
| Components CSS alignment | ~500 | közepes (vizuális regressziós kockázat) | [`components-css.md`](components-css.md) |
| parseYamlFrontmatter unification | ~500 | magas (funkcionális szuperset tervezés) | [`parse-yaml.md`](parse-yaml.md) |

## Folyamat (minden tételhez)

1. **Curator `survey`** — friss állapot ellenőrzése (lehet, hogy időközben változott)
2. **Olvasd el a terv-fájlt** ebben a mappában
3. **`/dash-promote <name>`** — Curator confirmation-flow:
   - Megerősíti a divergencia-mátrixot (élő mintán)
   - Kanonikus formát javasol
   - Rollout terv (mely fájlok, milyen edit)
   - Dry-run először
4. **Humán jóváhagyás** kötelező a rollout előtt
5. **Rollout** — fájlonkénti edit + verzió-bump + audit-trail
6. **DS-bump** (minor) — új audit-trail entry a DESIGN_SYSTEM.md-ben
7. **Lint** — `node _dashboards/_design/lint.mjs` zöld kell legyen
8. **Backlog cleanup** — a tételt mark-done a fájlban (NE töröld; történet)

## Új tétel hozzáadása

Új `.md` fájl ebben a mappában. Minimum mezők:

```yaml
---
title: <Promote terv neve>
date: <YYYY-MM-DD>
status: pending | analyzing | rolled-out | abandoned
priority: low | medium | high
estimated_loc_savings: ~N
risk: low | medium | high
---
```

Tartalom: divergencia-mátrix · javasolt kanonikus · alternatívák · rollout-lépések · kockázatok · rollback terv.
