---
title: Alfred — Personal Operations Home
date: 2026-05-28
author: Becze Szabolcs
status: active
description: Alfred agent (Executive Cognition Layer) személyes operations otthona. Itt él a cognitive inbox, a sync-rituálé state-je, a napi briefingek, a személyes + családi prioritások és TODO-k. Alfred a gazda és a BDOS közötti komornyik — itt rögzül minden, amit kiszolgál.
tags: [alfred, personal-ops, cognitive-inbox, executive]
id: 7c4ae5cc-3958-4dd1-b2e6-b78d5fb34bc8
index_schema_version: 1
bdos_index: true
agent: alfred
---

# Alfred — Personal Operations Home

> Alfred a BDOS **human interface rétege** — a gazda (Szabolcs) komornyikja / chief-of-staff-ja. Canonical spec: [`00_Prompts/BDOS/agents/alfred.md`](../../../00_Prompts/BDOS/agents/alfred.md). Dashboard: `_dashboards/alfred/index.html`.

## Mi van itt

| Fájl / mappa | Mit tartalmaz |
|---|---|
| [`inbox.md`](inbox.md) | **A cognitive inbox** — raw capture, append-only. Ide kerül minden nyers dump (ötlet, TODO, emlékeztető, családi dolog, hangulat, felismerés). Semmi strukturálás. |
| [`state/last_run.md`](state/last_run.md) | A sync-rituálé state-je — a dashboard egyetlen igazságforrása. |
| `today/` | Napi briefingek (`YYYY-MM-DD.md`). |
| [`priorities.md`](priorities.md) | Aktuális személyes + családi prioritások. |
| [`todos/`](todos/00_TODOS.md) | **TODO store** — scope-onkénti checkbox-listák (`00_TODOS.md` konvenció + `personal.md` + `family.md` + …). Markdown a forrás, NEM adatbázis. Alfred kezeli (todo/remind/done/tasks), kész → Archive, sosem törli. |
| `routes/` | Audit-trail: mit honnan hová routolt a sync (`YYYY-MM.md`). |
| `learnings/` | (v0.2) Alfred tanulságai a gazda mintáiról. |

## Capture-csatornák

- **Vault-side:** `inbox.md` — amikor a gazda a gép előtt ül.
- **On-the-go:** ChatGPT "Alfred Inbox" chat — telefonról bemondott voice-dump, amit Alfred sync-kor Chrome MCP-vel beolvas (Sage Referencia-chat mintára). *(Setup v0.2: a chat URL ide kerül.)*

## Sync-ritmus

Reggel (briefing) · délután (capture-feldolgozás) · este (lezárás) · dashboard-indításkor (opportunista). NEM realtime — semmi nem vész el, de a feldolgozás egészséges kadenciában történik.

## Hogyan adok Alfrednek feladatot

Bármilyen kontextusban megszólítom — ő felismeri a szándékot (canonical §11):
- *„Alfréd, nézd át ezt a szöveget és nézd meg mit kell csinálnom"* → action item-eket nyer ki → scope + due + prioritás javaslat → megerősítés → checkbox a `todos/<scope>.md`-be
- *„Alfréd, emlékeztess erre [dátum]"* → emlékeztető-task due dátummal
- *„Alfréd, mi van ma / a [projekt]-tel?"* → briefing / scope-szűrt lista
- *„Alfréd, kész a [task]"* → kipipálás + Archive

## Állapot

**v0.2.0 (2026-05-28).** Élő: cognitive inbox + markdown-natív TODO-rendszer (`todos/`, scope-onként) + intent-felismerés (§11). Mag-módok: `capture`/`sync`/`today`/`status`/`todo`/`remind`/`done`/`tasks`. Registration létrehozva (`.claude/agents/alfred.md`). Dashboard v0.2.0 („Feladatok scope szerint" panel). A `reflect`/`learn`/family-dashboard rétegek v0.3-ban jönnek.
