---
title: Alfred TODO Store — konvenció + index
date: 2026-05-28
author: Becze Szabolcs
status: active
description: Alfred markdown-natív TODO-rendszerének belépője. Leírja a task-formátumot (sima Obsidian checkbox + dátum + prioritás + scope), a scope-onkénti fájlszervezést, és az archív-szabályt (semmi nem törlődik). A forrás-az-igazságra a markdown; gyorsindex/sidecar csak v0.2+ ha a skála megköveteli.
tags: [alfred, todos, convention, checkboxes]
id: 5d656478-107b-470d-8658-f1c19ab6bf68
index_schema_version: 1
bdos_index: true
agent: alfred
schema: alfred.todos-index.v1
---

# Alfred TODO Store

> **Markdown a forrás-az-igazságra.** Sima Obsidian checkbox — bárhol pipálható (mobil is), git-verziózott, sosem vész el. Nincs adatbázis a tárolásra; Alfred maga parse-ol és nyer ki. (Ha valaha több ezer rekordra nő → regenerálható sidecar a `marketing_board.json` mintára, de NEM most.)

## Task-formátum

Egy task egy checkbox-sor a scope-fájl `## Active` szekciójában:

```markdown
- [ ] <feladat szövege> <prioritás> 📅 <YYYY-MM-DD> #<scope>
```

- **Státusz:** `- [ ]` nyitott · `- [x]` kész
- **Prioritás (opcionális, Tasks-plugin-kompatibilis):** `⏫` magas · `🔼` közepes · `🔽` alacsony
- **Határidő (opcionális):** `📅 YYYY-MM-DD` (vagy `due:: YYYY-MM-DD` inline mező — Dataview-kompatibilis)
- **Scope tag:** `#<scope>` (redundáns a fájllal, de kereshetővé teszi)

**Archív:** a kész tételt Alfred a `## Archive` szekcióba mozgatja (vagy `archive/<scope>-YYYY.md`-be, ha sok lesz) — **sosem törli**.

## Scope-fájlok (élő)

| Scope | Fájl | Mit fed |
|---|---|---|
| personal | [`personal.md`](personal.md) | Személyes, projekt-független feladatok |
| family | [`family.md`](family.md) | Családi teendők, emlékeztetők |
| fokuszpont | [`fokuszpont.md`](fokuszpont.md) | Fókuszpont projekt feladatai |
| bdos | [`bdos.md`](bdos.md) | BDOS architektúra-fejlesztési backlog (2026-05-29 study) |
| exarlabs | [`exarlabs.md`](exarlabs.md) | ExarLabs feladatok (csapatépítő Szováta 2026-05-30 batch + folyamatos) |
| cps | [`cps.md`](cps.md) | Sonrisa CPS operatív feladatok (Atlassian billing, Oracle/MVMI/Euroleasing follow-ups, vault-gap teendők — inbox triage 2026-06-06) |

> Új scope = új `<scope>.md` fájl ezzel a fejléccel + bejegyzés ide. A dashboard a `TODO_SCOPES` listából olvas (v0.2-ben auto-discover ebből az indexből).

## Hogyan kerül ide feladat

Alfrednek mondod (bármilyen kontextusban) — ő triázsol és confirmation után ide írja:
- *„Alfréd, nézd át ezt a szöveget és nézd meg mit kell csinálnom"* → action item-eket nyer ki → ide
- *„Alfréd, emlékeztess erre [dátumra]"* → reminder-task due dátummal
- *„Alfréd, kész a [task]"* → kipipálás + Archive-ba mozgatás

Részletek: [`../../../../00_Prompts/BDOS/agents/alfred.md`](../../../../00_Prompts/BDOS/agents/alfred.md) §11 (Intent recognition).
