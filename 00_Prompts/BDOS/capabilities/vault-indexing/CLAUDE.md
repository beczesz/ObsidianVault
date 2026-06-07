---
title: Vault Indexing — SQLite-backed metadata read-cache for BDOS
date: 2026-05-24
author: Becze Szabolcs + Librarian research
status: active
version: 0.2
description: Lightweight SQLite read-cache a vault markdown frontmatterjeire és wikilinkjeire. A markdown a forrás-az-igazságra — az SQLite egy REGENERÁLHATÓ cache, NEM write-target. Agentek (különösen Librarian retrieve módja és Maestro observe) ezen át queryelnek metadata-szintű találatokat ~10-100x token-takarékossággal a full-context scan helyett.
tags: [BDOS, capability, indexing, sqlite, metadata, librarian]
id: b853bfe0-b23a-4146-9f5a-a881800afb39
index_schema_version: 1
---

# Vault Indexing (v0.1)

> **A markdown a forrás-az-igazságra.** Az SQLite egy READ-CACHE, mindig regenerálható a vault-ból. Az agentek a markdown fájlokba írnak — az indexerre nincs write-flow.

## Mit ad

- Frontmatter mezők lekérdezése `<50ms`-ben (3304 fájl → 1-2 sec)
- Wikilink-graph + backlinks + orphan detection
- FTS5 full-text keresés a `title` + `description` + `body` lane-eken (body alacsony súlyú fallback, 2026-05-28 óta)
- Token-takarékos retrieve: 80% relevance assessment a body-olvasás nélkül
- **Reach layer (2026-06-07):** nem csak `.md`, hanem `.srt`/`.txt`/`.vtt` (full-text) és `.pdf`/`.docx`/`.xlsx`/`.pptx`/`.epub` (metadata stub) is indexelve. Coverage-policy: [`policy.py`](policy.py) a forrás-az-igazságra arra, mi számít tudásnak és milyen mélyen.

## Reach: coverage reconciliation (2026-06-07)

> **Trust = falsifikálható szám a filesystem ground-truth ellen, nem hit a folyamatban.**

A régi `coverage_pct` (`emit_stats.py`) önreferenciális volt: `indexed / total_md_files`, ahol mindkét szám a `notes` táblából jött, így sosem tudott miss-t jelezni (mindig ~100%). A [`reach.py`](reach.py) ezt javítja: a filesystemet hasonlítja az indexhez + a coverage-policyhez, és három falsifikálható hibamódot jelent:

- **Format gap**: nem-md tudásfájl amit a walker sosem járt be
- **Completeness gap**: `.md` ami a lemezen van de az indexből hiányzik
- **Drift**: ghost (indexben, lemezről törölve), pollution (kizárt mappából indexelt), stale

```bash
python3 reach.py            # 00_REACH_REPORT.md a vault gyökerébe + summary
python3 reach.py --json     # gépi
```

### Growth guarantee: reconcile backstop

Egy inkrementális watcher elszalaszthat eseményt (crash, sleep, Drive-lag); az event-alapú sosem ellenőriz újra. Ezért a [`reconcile.sh`](reconcile.sh) (scheduler job `vault-index-reconcile`, interval 30 perc) teljes disk-vs-index reconciliationt futtat a watcher-engine-től függetlenül, és frissíti a reach sidecart. Seed: `python3 scheduler.py --seed-reach`. **Ez garantálja, hogy bármit beviszel, elérhetővé válik a Librarian számára akkor is, ha a watcher kihagyott.**

### yaml opcionális

A `build_index.py` PyYAML nélkül is fut (stdlib lenient parser fallback), így a watcher bármely python3-mal indítható crash nélkül. Teljes fidelity yaml-os pythonnal (full rebuild + reconcile azt preferálja).

## Fájlok

| Fájl | Mit ad |
|---|---|
| `policy.py` | **Coverage-policy single-source-of-truth**: mit indexelünk (EXCLUDE_DIRS, FULLTEXT_EXT, METADATA_EXT, classify). build_index + watch + reach + emit_stats ezt importálja. |
| `schema.sql` | SQLite DDL: `notes` (+`ext`,`content_class`) + `backlinks` + `notes_fts` (title+desc+body) |
| `build_index.py` | Full-rebuild. Walk + parse + insert, md/transcript/doc branch-ekkel. yaml opcionális. Idempotens. |
| `query.py` | Python query API + CLI (`--ext`, `--content-class`, NFC/NFD-robusztus area match) |
| `reach.py` | **Coverage reconciliation**: filesystem vs index, falsifikálható reach-szám. Read-only. |
| `reconcile.sh` | Scheduled backstop wrapper (watch.py --once + emit_stats). A growth guarantee. |
| `emit_stats.py` | Sidecar generátor: `coverage_pct` most a valódi reach (reach.py-ból) |
| `cache/vault.db` | A generált SQLite database (per-machine, gitignore-olt) |
| `README.md` | Setup + usage |

## Anti-pattern (Librarian research §architectural recommendations)

**NE használd write-targetnek.** A markdown fájlok soha nem válhatnak stub-bé. Ha a cache törlődik, a vault-nak állnia kell — emberileg olvasható maradnia.

## Használat

```bash
# Full rebuild (futtass amikor sok változás van vagy schema változik)
python3 build_index.py

# Query CLI
python3 query.py --category philosophy --status maturing
python3 query.py --area "Personal Growth" --tag ai-native
python3 query.py --orphans  # fájlok, ahova semmi nem mutat
python3 query.py --fts "middle management"  # FTS5 a description-on
```

## Marketing board sidecar auto-refresh (v0.2, 2026-05-25)

A `_dashboards/_design/marketing_board.json` sidecar automatikusan frissül, ha seed vagy publikáció fájl változik — a user-nek nem kell manuálisan futtatni `scan_marketing_board.py`-t.

### Két útvonal

| Útvonal | Trigger | Latencia | Fájl |
|---|---|---|---|
| **Watchdog hook (elsődleges)** | Fájlrendszer-esemény: `_inbox/seeds/*.md` vagy `Marketing/Publications/*.md` megváltozik | 5s debounce után azonnali | `watch_event.py` — `schedule_marketing_board_regen()` |
| **Scheduler safety net** | BDOS scheduler 5 perces interval job | ≤5 perc | `scheduler.py` — job_id: `marketing-board-sidecar-refresh` |

### Debounce

Mindkét útvonal a `marketing_board_refresh.py` wrapperen keresztül hívja a `scan_marketing_board.py`-t. A wrapper egy fájl-alapú debounce lockkal (`cache/mktboard_refresh.lock`) gondoskodik arról, hogy burst eseményeknél (pl. egy seed mentésekor 3-5 FS-esemény keletkezik) csak egyetlen regen fusson le.

- Debounce ablak: **5 másodperc** az utolsó befejezett regen után
- In-progress lock: ha már fut egy regen, a következő hívás azonnal kilép (exit 2)
- Stale lock timeout: 120 másodpercnél régebbi in-progress lock automatikusan érvénytelen (holt folyamat)

### Fájlok

| Fájl | Szerepe |
|---|---|
| `marketing_board_refresh.py` | Debounced wrapper — `--force` megkerüli a debounce-t, `--dry-run` átad a scan-nek |
| `watch_event.py` | Watchdog hook: `_is_marketing_board_relevant()` + `schedule_marketing_board_regen()` |
| `scheduler.py` | `seed_marketing_jobs()` helper + `--seed-marketing` CLI flag |
| `cache/mktboard_refresh.log` | Refresh log minden futáshoz |

### Kézi trigger

```bash
# Azonnali, debounce nélkül:
python3 marketing_board_refresh.py --force

# Dry-run (nem ír fájlt):
python3 marketing_board_refresh.py --force --dry-run

# Scheduler job egyszeri újra-regisztrálása (idempotens):
python3 scheduler.py --seed-marketing
```

### Amit NEM módosít

`scan_marketing_board.py` változatlan marad — self-contained, manuálisan is futtatható.

---

## Cross-platform futás (v0.3, 2026-05-28)

A vault Google Drive-on **két gép között szinkronizálódik** (macOS `becze-mac` + Windows). Mivel a `vault.db` egy szinkronizált bináris SQLite, **két watcher egyszerre írva konfliktus-másolatokat / korrupciót okozna**. Ezért a runtime-state gépenként, a synced vault-fán KÍVÜL él.

### `runtime.py` — single source of truth a path-okra
Per-machine cache dir (auto-detektált OS szerint), felülírható `BDOS_CACHE_DIR`-rel:
- Windows: `%LOCALAPPDATA%\bdos-vault-index\`
- macOS: `~/Library/Application Support/bdos-vault-index/`
- Linux: `$XDG_CACHE_HOME/bdos-vault-index/`

Ide kerül: `vault.db`, `watch.pid`, `events.pid`, `watch.log`, `events.log`. **Mindkét gép a saját lokális indexét írja** → nincs Drive-ütközés. Readerek (`query.py`, `audit.py`) a `db_read_path()`-en át a lokálist preferálják, de visszaesnek a legacy synced `cache/vault.db`-re amíg a lokális nem épült fel (migrációs grace).

**Synced marad** (szándékosan): `cache/agent_observability.db` (egységes agent-logok + scheduler jobok), `_dashboards/_design/marketing_board.json` sidecar, `mktboard_refresh.lock/.log`.

### `launch.py` — cross-platform indító (start/stop/restart/status)
Auto-detektálja az OS-t és a watchdog meglétét (event-based vs polling fallback). Gépenkénti PID-fájlok → egyik gép sosem nyúl a másik folyamataihoz. Wrapperek: `start.ps1`/`stop.ps1`/`status.ps1` (Windows), `start.sh`/`stop.sh`/`status.sh` (Mac) — mind a `launch.py`-t hívják.

### Scheduler single-owner szabály
A scheduler **pontosan egy gépen** futhat (különben a jobok duplán tüzelnek a synced `agent_observability.db`-n). **A Mac a tulajdonos** (`start.sh` scheduler ON). Windows: `start.ps1` `--no-scheduler` (vagy `BDOS_DISABLE_SCHEDULER=1`). Tulajdonos-váltás = a flag áthelyezése.

### Single-server (port 4321) — `events_server.py` headless daemon (2026-05-29)
Korábban **két** böngésző-felé néző szerver futott: `dash-server.mjs` (Node, 4321, statikus fájlok + `/__events` SSE) és `events_server.py` (Python, 4322, vault-update SSE + `/health` + scheduler). Ez fölösleges törékenység volt: két folyamat = két életben tartandó dolog, és a "Watchdog" health-pill kizárólag azért létezett, hogy a második szervert figyelje.

**Mostantól egyetlen böngésző-felé néző szerver van: `dash-server.mjs` (4321).** Ez szolgálja ki a `vault-update` SSE-t (a `vault.db` mtime-ot maga pollozza a per-machine cache-ben) **és** a `/health` végpontot (a daemon + watcher életjelét a PID-fájlokból olvassa). Az `events_server.py` **port nélküli headless daemon** lett: nincs socket, csak a háttérmunka (scheduler az owner gépen, sidecar self-refresh a secondary gépen). A fájlnév + `events.pid`/`events.log` nevek megmaradtak (PID/log migráció elkerülése), de fogalmilag ez az "indexing daemon".

Következmény: a 4322 port megszűnt, a dashboardok **csak a 4321-et** hívják. A "Watchdog" pill mostantól a `/health` `daemon_alive` mezőjéből a tényleges indexing daemon életjelét mutatja, nem egy külön HTTP-szerver elérhetőségét.

### Sidecar self-refresh a secondary gépen (2026-05-29)
Az `agent_logs.json` sidecart (amit a System Status dashboard a DB és Scheduler health-pillekhez olvas) csak a tulajdonos gép (Mac) állítja elő agent/scheduler aktivitásból. A secondary géphez (Windows) ez **csak Google Drive sync-en át jut el, több perces késéssel**, így a dashboard 5 perces frissesség-küszöbét rendszeresen túllépi → DB és Scheduler pill "stale/off", noha a synced `agent_observability.db` friss. Megoldás: ha `BDOS_DISABLE_SCHEDULER=1` (azaz a secondary gépen), a headless daemon (`events_server.py`) egy `sidecar-refresh` szállal **lokálisan regenerálja** a sidecart a synced DB-ből `BDOS_SIDECAR_REFRESH_S` (alapért. 60) másodpercenként. Csak a secondary gép self-refresh-el gyors ütemben (a tulajdonos agent-aktivitásból frissít) → a synced JSON-nek gép-szerepenként egy aktív írója marad.

A `launch.py` minden spawn-olt processznek `PYTHONUNBUFFERED=1`-et ad → a `print()` kimenet azonnal a `watch.log`/`events.log`-ba kerül (korábban a block-buffering miatt egy futó events_server üres logot hagyott, ami crash-nek látszott).

### Crash-recovery (recurring "watchdog red")
A logon-auto-start csak bejelentkezéskor fut; ha a folyamatok menet közben elhalnak (sleep, Drive-hiccup), semmi nem indítja újra őket a következő logonig. ÖnGyógyító megoldás: egy 5 perces Windows Scheduled Task, ami az idempotens `launch.py start --no-scheduler`-t futtatja (már-fut esetén no-op). Regisztráció (user-jóváhagyással):
```powershell
$pyw = "$env:LOCALAPPDATA\Programs\Python\Python312\pythonw.exe"
$launch = "C:\Users\EvoComputers\Obsidian\ideas-vault\00_Prompts\BDOS\capabilities\vault-indexing\launch.py"
$action  = New-ScheduledTaskAction -Execute $pyw -Argument "`"$launch`" start --no-scheduler"
$trigger = New-ScheduledTaskTrigger -Once -At (Get-Date) -RepetitionInterval (New-TimeSpan -Minutes 5)
$settings = New-ScheduledTaskSettingsSet -StartWhenAvailable -MultipleInstances IgnoreNew -ExecutionTimeLimit (New-TimeSpan -Minutes 4)
Register-ScheduledTask -TaskName "BDOS Vault Indexing Supervisor" -Action $action -Trigger $trigger -Settings $settings -Principal (New-ScheduledTaskPrincipal -UserId $env:USERNAME -LogonType Interactive) -Force
```

### Auto-start logonkor
- Windows: `%LOCALAPPDATA%\bdos-vault-index\autostart.ps1` + rejtett indító a Startup mappában (`bdos-vault-indexing.vbs`). Drive-mountra vár, majd `launch.py start --no-scheduler`.
- macOS: `com.bdos.vault-indexing.plist` LaunchAgent (telepítés a fájl fejlécében).

## Event log — `events.py` (B2 v0.1, 2026-05-29)

A 2026-05-29 architektúra-study #2 javaslata (B2): strukturált inter-agent **event log**, ami kiváltja azt az anti-patternt, hogy az agentek shared markdown fájl írásával jeleznek egymásnak állapotot.

- **Hol:** `events` tábla az `agent_observability.db`-ben (synced, shared), az `agent_logs` + `scheduled_jobs` mellett. Séma: `events_schema.sql`.
- **Forrás-az-igazságra:** [`../../ARCHITECTURE_BOUNDARIES.md`](../../ARCHITECTURE_BOUNDARIES.md) §3 szerint az események a telemetria-osztály → SQLite-canonical.
- **EMIT-ONLY v0.1:** az `emit_event()` csak hozzáfűz; semmi nem konzumálja. A `processed` oszlop a jövőbeli reactornak (B6) van fenntartva.
- **Concurrency-hardening (B2):** `runtime.connect()` helper `busy_timeout=5000` + WAL defaulttal. A per-machine `vault.db` mostantól WAL (a synced legacy copy szándékosan DELETE marad, hogy ne kerüljön `-wal`/`-shm` a Drive-ra).

```bash
python3 events.py --emit publication.approved --agent presto --scope deak-husuzlet --payload '{"publication_id":"pub-123"}'
python3 events.py --recent 20 --type publication.approved
```
```python
from events import emit_event
emit_event('seed.created', source_agent='alfred', scope='bdos', payload={'seed_id': 's-1'})
```

| Fájl | Szerepe |
|---|---|
| `events_schema.sql` | `events` tábla DDL (append-only, indexelve type/occurred_at/scope/processed-en) |
| `events.py` | `emit_event()` + `recent()` + CLI; self-initializing séma |
| `runtime.py` `connect()` | Megosztott connection helper: busy_timeout + WAL default |

## Roadmap

- **v0.1:** full-rebuild + query CLI + Python API
- **v0.2 (2026-05-25):** marketing board sidecar auto-refresh — watchdog hook + scheduler safety net + debounced wrapper
- **v0.3 (2026-05-28):** cross-platform runtime — per-machine cache (`runtime.py`), OS-detektáló `launch.py`, scheduler single-owner, logon auto-start (Win + Mac)
- **v0.3.1 (2026-05-29):** Windows health-pill fix — `events_server.py` sidecar self-refresh a secondary gépen (`BDOS_SIDECAR_REFRESH_S`), `launch.py` `PYTHONUNBUFFERED=1` a spawn-okhoz, dokumentált 5-perces crash-recovery supervisor task
- **v0.3.2 (2026-05-29):** single-server consolidation — `events_server.py` headless daemonná vált (nincs 4322 port); a `vault-update` SSE + `/health` átkerült `dash-server.mjs`-be (4321). Kliensek (`live-updates.js`, `admin-bar.js`, `ops-header.js`, scheduler dashboard) csak a 4321-et hívják. A Watchdog pill a `/health` `daemon_alive`-ot mutatja.
- **v0.3.3 (2026-05-29):** B2 event layer v0.1 — append-only `events` tábla + `emit_event()` API (emit-only), `runtime.connect()` busy_timeout+WAL helper, per-machine `vault.db` WAL-re állítva. Reactor (event→dispatch) elhalasztva B6-ra.
- **v0.4, Reach layer (2026-06-07):** coverage policy (`policy.py`) single-source-of-truth; non-md ingestion (srt/txt/vtt full-text + pdf/docx/xlsx/pptx/epub metadata stub, `ext`+`content_class` oszlopok); `reach.py` filesystem-vs-index reconciliation (falsifikálható reach-szám); `reconcile.sh` + `vault-index-reconcile` scheduler job (30 perc growth-guarantee backstop); `emit_stats` honest `coverage_pct`; yaml opcionális (stdlib fallback); query.py NFC/NFD-robusztus area match + `--ext`/`--content-class`. Reach: md 100%, full-text 100%, total-knowledge 100% (2185 md + 408 transcript/txt + 428 doc = 3021).
- **v0.5 (later):** Librarian retrieve módba integrálva — automatikus cache-first lookup
- **v0.6 (later):** Maestro observe módba integrálva — log-aggregálás cache-en át
- **v0.7 (later):** networkx PageRank a backlink graph-on retrieve scoring-hoz; pdf/docx text-extraction (metadata stub → full-text)
