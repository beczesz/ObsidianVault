---
title: BDOS Architecture Boundaries — Source-of-Truth Map
date: 2026-05-29
author: Becze Szabolcs
status: active
description: A BDOS kanonikus forrás-az-igazságra térképe. Data-class-onként megmondja, melyik tároló a single source of truth, és mi a derived/disposable. A 2026-05-29 multi-AI study #1 javaslata (B1). Cél a "source-of-truth confusion" megszüntetése: minden új írásnak nevesítenie kell a data-class-át. Egyetlen nyitott döntés (agent logok markdown vs SQLite) a §3-ban, ratifikálásra vár.
tags: [bdos, architecture, source-of-truth, boundaries, governance]
version: 0.1.0
id: 3ce956ca-2b77-427a-8c47-583239487c49
index_schema_version: 1
bdos_index: true
---

# BDOS Architecture Boundaries

> **Az invariáns:** a markdown a tudás forrás-az-igazságra. Minden adatbázis és JSON sidecar **regenerálható derived réteg**, hacsak ez a doksi explicit ki nem mondja az ellenkezőjét. Ha egy írás nem talál data-class-t itt, az új írást meg kell állítani, amíg a class be nem kerül ide.

Forrás: [2026-05-29 architectural evolution study](brainstorm/2026-05-29_bdos-architectural-evolution-analysis.md), B1 javaslat.

## 1. Source-of-truth map

| Data class | Kanonikus store (truth) | Derived / disposable | Builder | Megjegyzés |
|---|---|---|---|---|
| Tudás és tartalom (notes, agent-defek, capability-docs) | Markdown vault (PARA) | `vault-indexing/cache/vault.db` (FTS5), backlink graph | `runtime.py` / indexer | A DB cache, bármikor újraépíthető a markdownból. |
| Taskok | `02_Areas/Personal Growth/Alfred/todos/<scope>.md` (Obsidian checkbox) | (egyelőre nincs) | Alfred | Explicit döntés: NINCS DB a taskokra (00_TODOS.md). |
| Marketing pipeline (seedek, publikációk) | Markdown frontmatter (`presto.seed.v1`, `presto.publication.v2`) | `_dashboards/_design/marketing_board.json` | `scan_marketing_board.py` | A board scan-eli a markdownt, nem fordítva. |
| Sales pipeline (Broker cohortok) | Markdown `COHORT.md` | sales board JSON (ha van) | Broker / scan | Presto-mintára. |
| Naptár / reminderek | Markdown task (`📅 due`) + külső naptár (forrás a külső rendszer) | dashboard nézet | Alfred | A külső naptár a truth a meeting-ekre; a vault csak tükröz. |
| Vault statisztika | (számolt) | `_dashboards/_design/vault_stats.json` | `emit_stats.py` | Tisztán derived. |
| Dashboardok (HTML + JSON sidecar) | (nincs saját truth) | `_dashboards/**` HTML + `_design/*.json` | Curator / build | Compiled artifact, derived. B7 inkrementálissá teszi. |
| Scheduler ütemezés-definíció | Markdown / config (`agents/*/cron/`) | run-logok | scheduler.py | A *definíció* kanonikus; a *futás-log* operational. |
| Indexek | (nincs) | `vault.db`, sidecar JSON-ok | indexer | Mindig eldobható, regenerálható. |
| Strukturált domain-adat (pl. DH screen-catalog `products-v1.x.json`) | **A JSON maga kanonikus** az adott Area-ban | belőle generált nézetek | domain tooling | Kivétel az invariáns alól: inherens-táblázatos adat JSON-canonical lehet, ha az Area-ban él (NEM az index-rétegben). |
| Agent logok — ember-jelentésű | Markdown `agents/<agent>/logs/{learning,version}/` + döntések/reflektciók | (nincs) | agent maga | Ezt olvassa Maestro reflect/observe. Lásd §3. |
| Agent logok — telemetria | `agent_observability.db` (SQLite) | `agent_logs.json` (sidecar) | `agent_log.py` | Tool-call, token, duration, query-stat. Lásd §3. |
| Inter-agent események (B2) | `agent_observability.db` → `events` tábla (SQLite-canonical) | (jövőbeli markdown cold-record) | `events.py` `emit_event()` | Append-only koordinációs/audit log. Kiváltja a "shared markdownba írok, hogy jelezzek" anti-patternt. Emit-only v0.1; reactor = B6. |

## 2. Szabályok

1. **Markdown-first írás:** ami emberi-jelentésű és git-diffelhető, az markdownba megy; a DB/JSON ezt tükrözi.
2. **A derived réteg sosem írásra-cél kézzel:** ha egy sidecart/DB-t szerkesztenél kézzel, rossz helyen állsz — a markdownt szerkeszd, és regeneráld.
3. **Új data-class = előbb ide bekerül, utána íródik:** ez a doksi a registry.
4. **Kivételek nevesítve:** a strukturált domain-adat (JSON-canonical) csak akkor megengedett, ha (a) inherens-táblázatos, (b) az Area-ban él, (c) itt fel van sorolva.

## 3. RATIFIKÁLT DÖNTÉS — Agent logok: komplementer split (2026-05-29)

**A probléma (a study fő találata):** ma KÉT párhuzamos log-rendszer fut.
- **Markdown narratív logok:** `agents/<agent>/logs/{operational,learning,version}/YYYY-MM.md` — a Constitution Phase 2.B "3 stream", ember-olvasható, git-verziózott.
- **SQLite strukturált telemetria:** `agent_observability.db`, `agent_log.py` writer API-val (28 oszlop: tool-call, token, duration, outcome…), + `agent_logs.json` sidecar a dashboardoknak.

Ezek **nem egymás tükrei** — átfedő, de eltérő granularitású adatot tartanak. Ettől homályos, hogy "hol az igazság".

**RATIFIKÁLVA (2026-05-29):** komplementer szerep, explicit határral:
- **Markdown = kanonikus** az ember-jelentésű, ritka, diffelendő eseményekre: `learning`, `version_change`, döntések, reflektciók. (Ezt olvassa Maestro reflect/observe.)
- **SQLite = kanonikus** a nagy-volumenű, gépi telemetriára: tool-call, token-usage, duration, query-stat. (Ez túl zajos markdownnak; a `agent_logs.json` ennek a derived sidecarja.)
- **Tilos a duplikáció:** egy esemény vagy az egyikbe, vagy a másikba megy, a fenti szabály szerint, soha mindkettőbe.

**Következmény a kódra:** `agent_log.py` továbbra is a telemetriát kezeli (DB + sidecar). Az ember-jelentésű eseményeket (learning, version_change, döntés, reflektció) az agentek a markdown stream-jeikbe írják, NEM a DB-be. Ahol ma egy esemény mindkét helyre megy, a telemetria-oldalon meg kell szüntetni a narratív duplikációt (külön cleanup-task, nem blokkolja ezt a doksit).

## 4. Verzió-napló
- **v0.1.0 (2026-05-29):** első térkép a B1 alapján. Minden class hozzárendelve. §3 agent-log döntés ratifikálva (komplementer split). status: active.
