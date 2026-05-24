---
title: Navigátor Podcast Dashboard — Adat-kontraktus
date: 2026-05-21
author: Becze Szabolcs
status: active
version: 0.1.0
description: >
  Formátum-kontraktus a navigator.html élő dashboard és a markdown forrásfájlok
  (EPISODES.md, TODO.md, Synthesis/Podcast/EP*.md) között. Olvasd el, mielőtt
  bármelyik fájl szerkezetét módosítod, vagy új mezőt veszel fel.
id: 079b2f06-c94b-4fc5-86f5-2309de282625
index_schema_version: 1
---

# Navigátor Podcast Dashboard — Adat-kontraktus

> A [`_dashboards/navigator.html`](/_dashboards/navigator.html) egy **élő, read-only
> renderer**. 8 másodpercenként (SSE push-ra azonnal) újraolvassa az alábbi markdown
> fájlokat és újrarajzolja magát. **Nincs build lépés, nincs adatbázis.** A markdown
> a single source of truth. **Edit a markdownt Obsidianban, ne a HTML-t.**
> Általános konvenciók: `02_Areas/Sonrisa/CPS/Sales/DASHBOARD_CONTRACT.md`.

## Forrásfájlok

| Fájl | Szerep |
|------|--------|
| `02_Areas/Navigátor Podcast/EPISODES.md` | Az **Epizódok** tab forrása — `episodes` frontmatter tömb. |
| `02_Areas/Navigátor Podcast/TODO.md` | A **Kanban** tab forrása — Obsidian Kanban board. |
| `02_Areas/Navigátor Podcast/Synthesis/Podcast/<synthesis>.md` | A **drawer** gazdagítása — kattintásra betöltve. |

A dashboard mindkét fő fájlt minden poll ciklusban lekéri; a synthesis fájlt csak
a drawer megnyitásakor (és cache-eli).

## EPISODES.md — `episodes` tömb

Minden epizód egy objektum a frontmatter `episodes:` tömbjében. Mezők:

| Mező | Típus | Hajtja |
|------|-------|--------|
| `ep` | int (1–42) | EP badge, alap rendezés |
| `guest` | string | Vendég oszlop, drawer cím |
| `topic` | string | Téma oszlop, drawer alcím |
| `duration` | string `H:MM:SS` | Hossz oszlop |
| `youtube_id` | string | ▶ YouTube CTA |
| `youtube_date` | `YYYY-MM-DD` | YouTube oszlop dátum (= a helyes Spotify dátum) |
| `spotify` | enum: `ok` \| `date_fix` \| `missing` \| `unverified` | Spotify státusz badge + szűrő |
| `spotify_current` | `YYYY-MM-DD` | `date_fix`-nél a hibás dátum |
| `spotify_correct` | `YYYY-MM-DD` | a javítandó / feltöltési dátum |
| `views` | int (0 = nincs adat) | Nézések oszlop, rendezés, „Összes nézés" widget |
| `cluster` | string | Klaszter chip + szűrő |
| `synthesis` | string | A `Synthesis/Podcast/<…>.md` neve **kiterjesztés nélkül**; üres = nincs drawer-tartalom |
| `priority` | bool | „prio" badge |
| `top` | bool | ★ TOP performer kiemelés + szűrő |

**Gyakori hibák:** rossz `spotify` enum érték → a badge „unverified"-ként esik vissza.
Hibás `synthesis` fájlnév → a drawer „nincs szintézis" üzenetet mutat (nem hibázik).

## TODO.md — Obsidian Kanban

- A frontmatterben **kötelező** a `kanban-plugin: board`, hogy Obsidianban is board legyen.
- `## Oszlopnév` → kanban lane. A lane színe a névből származik (kész/folyamat/dátum/feltölt/youtube kulcsszavak).
- Kártya sor: `- [ ] **Cím** #tag #tag2 @{YYYY-MM-DD} szabad teaser szöveg`
  - `**...**` = kártya címe (kötelező a felismeréshez).
  - `#tag` = chip (az `#epNN` tagek el vannak rejtve a chipek közül, de kereshetők).
  - `#priority` tag → kiemelt chip.
  - `@{YYYY-MM-DD}` = határidő pill (lejárt = piros).
  - `- [x]` = kész (áthúzott, halványított).
- A `%% kanban:settings ... %%` blokk a parser számára lezárja a feldolgozást — alatta ne legyen kártya.

## Drawer

Kattints egy epizód sorára → jobb oldali drawer. Fejléc: meta + CTA gombok
(▶ YouTube, Szintézis Obsidianban, EPISODES.md). A törzs a `synthesis` fájl
**body** részét (frontmatter nélkül) rendereli könnyű markdown→HTML motorral
(címsorok, **bold**, listák, táblázatok).

## Szervezés

```
node _dashboards/_tools/dash-server.mjs     # majd http://localhost:4321/
```
A szerver `WATCH_DIRS`-je tartalmazza a `02_Areas/Navigátor Podcast` mappát, így
a fenti fájlok bármelyikének mentése sub-second push-t küld a dashboardnak.
</content>
