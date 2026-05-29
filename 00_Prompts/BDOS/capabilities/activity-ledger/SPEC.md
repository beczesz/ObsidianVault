---
title: Activity Ledger — capability spec
date: 2026-05-29
author: Becze Szabolcs
status: draft
version: 0.1.0
description: Spec egy néma activity-ledger képességhez. A user passzívan rögzített "mit végeztem" naplót akar, amit később megkérdezhet ("mit csináltam a héten / szerdán?"). Ownership-split: Maestro gyűjt (chronicle mód), Alfred válaszol (recap mód). A git history a fő adatforrás, mert a logok hiányosak.
tags: [bdos, capability, activity-ledger, maestro, alfred, observability]
id: 7c3a1e94-2b5d-4f81-9a06-d4e8c1f2a3b7
index_schema_version: 1
bdos_index: true
---

# Activity Ledger — capability spec (draft v0.1.0)

## 1. Cél és motiváció

A user egy **néma asszisztenst** akar, ami passzívan rögzíti a munkája nagyobb eseményeit (dashboard-munka, videó-publikálás, megbeszélések), hogy később megkérdezhesse: "mit csináltam a héten / szerdán?". Részben azért, hogy ellensúlyozza a visszatérő "nem csinálok eleget" érzést: bizonyítékot adjon a tényleges output-ról.

Alapelv: **derive, ne kérj kézi naplózást.** A user nem logol, a rendszer származtat.

## 2. Architektúra — ownership split

| Szerep | Agent | Mit csinál |
|---|---|---|
| **Collector** | Maestro | A meglevő log-stream-eket + git history-t emberi-olvasható activity event-ekké rolloltja, és a ledgerbe írja. Új `chronicle` mód. |
| **Interface** | Alfred | A user kérdéseit ("mit csináltam szerdán") a ledgerből válaszolja meg, emberi hangon. Új `recap` mód. |

Indoklás: a "mit csináltam / eleget teszek-e" emberi, executive kérdés = Alfred. A log-aggregáció Maestro meglevő idegrendszere = ne duplikáljuk Alfredbe. Egy közös artefakt (a ledger), két szerep.

## 3. A kemény tanulság (Maestro grounded audit, 2026-05-29)

A jelenlegi log-infrastruktúra **NEM elég** önmagában:

- `agent_observability.db` (`capabilities/vault-indexing/cache/`): ~3632 sor, de **~99% scheduler-zaj** (5 perces cron-refresh). A `tags`-ban `scheduler` diszkriminálja.
- A tényleges emberi agent-invokáció ~30-40 sor 5 nap alatt. **Alfred és Forge 0 sort ír.**
- A main-Claude / user-direkt munka (fájl-szerkesztés, mint ez a session) **egyáltalán nincs a DB-ben** — részben a markdown Version log-okban él.

**Következmény:** a **vault git history a fő adatforrás**, nem opcionális kiegészítő. `git log --name-status --since=<date>` adja a user tényleges munkájának fájl-szintű, commit-üzenettel ellátott képét. A DB és a Version log gazdagít, de a git a gerinc.

## 4. Ledger — adatmodell

**Hol él (NYITOTT, lásd §7 D1):** javaslat `00_Prompts/BDOS/agents/maestro/logs/activity-ledger/<YYYY-MM>.md` (collector-tulajdon) VAGY `02_Areas/Personal Growth/Alfred/activity/<YYYY-Www>.md` (human-facing, Alfred-area).

Append-only, YAML-block per rollup. Maestro javasolt event-sémája:

```yaml
event: activity
ts: <ISO-8601>
period_start: <ISO-8601>
period_end: <ISO-8601>
entry_id: activity-YYYYMMDD
source: daily-rollup | session-end | git | manual
events_processed: <int>
git_commits_included: <bool>
items:
  - date: <YYYY-MM-DD>
    agent: curator | presto | librarian | maestro | alfred | broker | forge | user-git
    summary: "Curator tended alfred/index.html to v0.4.2 (capture box, process endpoint)"
    category: tend | build | audit | publish | promote | team-change | learn | git-commit
    files_touched: [<paths>]
    tokens: {in: <int|null>, out: <int|null>}
    db_task_id: <task_id|null>     # drill-down a DB-be
    git_ref: <short-hash|null>     # drill-down a git-be
    details: <string|null>
```

A `date` mező teszi olcsóvá Alfred dátum-szűrését (1 Read + string-match, nem raw-log túrás).

## 5. Capture pipeline — 4 forrás

1. **Vault git history** (gerinc, ingyen). `git log --name-status --since`. Lefedi a user kézi és Claude-asszisztált munkáját.
2. **agent_observability.db** (`scheduler` tag kiszűrve). Az emberi agent-invokációk, ahol vannak.
3. **Markdown Version log-ok** (`agents/*/logs/version/`). Gazdagítás: `files_touched`, `description`, `from/to_version`.
4. **Session-end hook** (a valódi néma rögzítő — NYITOTT, D3). Claude Code `Stop`/`SessionEnd` hook a settings.json-ben, ami session-záráskor Haiku 4.5-tel egy event-sort ír. Ez fogja meg a main-Claude munkát, amit a logok nem. Kiegészíti a git-et (a hook a "miért/mit", a git a "milyen fájlok").
5. **Manuális no-trace event** (videó kiment, megbeszélés): a user egy sort dob az Alfred capture boxba → activity-ként rögzül (nem task). A meglevő box dual-purpose lesz.

Dedup: egy `task_id` (started + N tool_call + completed) → EGY event. Git-commit és DB-event átfedés → a részletesebbet tartjuk, `git_ref`/`db_task_id` cross-ref.

## 6. Maestro `chronicle` mód + Alfred `recap` mód

- **`chronicle`** (Maestro, Observability domain 4. mód): WRITES → confirmation kell. Kadencia: napi roll-up (hajnali ~5:30, meglevő scheduler) + opcionális session-end. Eldobja a scheduler-forgalmat, bevonja a git-et (`git_commits_included: true`).
- **`recap`** (Alfred): read-only. Csak a ledger fájlt olvassa, dátumra szűr, emberi hangon összegez, és tudja gyengéden ellensúlyozni a "nem csinálok eleget" érzést a tényleges output felmutatásával. Mély kérdésnél a `db_task_id`/`git_ref` mentén drill-down.

## 7. Nyitott döntések (a user-re vár)

- **D1 — Ledger helye:** Maestro-stream (`agents/maestro/logs/activity-ledger/`) vagy Alfred-area (`02_Areas/Personal Growth/Alfred/activity/`)? A human-facing jelleg az Alfred-area mellett szól; a collector-tulajdon a Maestro-stream mellett.
- **D2 — Git mint gerinc:** elfogadjuk-e, hogy a git history a fő forrás (nem a DB)? Ez a grounded audit ajánlása.
- **D3 — Session-end hook:** megépítsük-e (settings.json + Haiku)? Ez a legnagyobb lever a néma rögzítéshez, de harness-configot érint és kis session-záró latenciát ad.
- **D4 — Alfred/Forge DB-írás gap:** javítsuk-e, hogy a ledger ne legyen vak az Alfred-munkára? (A user sokat dolgozik Alfreddel.)

## 8. Build-státusz (mit kell megépíteni)

| Elem | Státusz |
|---|---|
| SQLite DB + writer, scheduler | KÉSZ |
| Git-history harvest a rollupban | HIÁNYZIK (gerinc) |
| Maestro `chronicle` mód | HIÁNYZIK |
| `activity-ledger/` skeleton + séma | HIÁNYZIK |
| Alfred `recap` mód | HIÁNYZIK |
| Session-end hook (D3) | HIÁNYZIK / opcionális |
| Alfred + Forge DB-írás (D4) | HIÁNYZIK / opcionális |

## 9. Hivatkozások

- Maestro collector grounded audit: 2026-05-29 (e spec §3 és §4 forrása).
- `_dashboards/_design/agent-logs.js` — sidecar helper.
- `00_Prompts/BDOS/agents/maestro/` — collector agent.
- `02_Areas/Personal Growth/Alfred/` — interface agent state.
