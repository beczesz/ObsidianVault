---
title: BDOS Log Schemas — Operational, Learning, Version
date: 2026-05-24
author: Becze Szabolcs
status: active
version: 1.3
description: A Phase 2 family-szintű 3 log-stream invariáns kanonikus schema definíciója. Ez a fájl a forrás-az-igazságra arra, hogyan néznek ki az Operational, Learning, és Version log bejegyzések. Backward-compatible bővítés engedélyezett, törlés tilos. Maestro Dashboard és minden agent-prompt erre épül. Phase 5 (2026-05-24): az Operational markdown stream DEPRECATED; az agent_observability SQLite DB és a writer API (agent_log.py) az elsődleges operacionális megfigyelhetőségi réteg. Phase 6 (2026-05-24): scheduler tag-discriminator convention added (§0.S); scheduled_jobs + job_runs DDL cross-reference added.
tags: [BDOS, schemas, logging, telemetry, observability]
id: 15f43650-22ff-4d55-bee0-71ede67cb108
index_schema_version: 1
---

# BDOS Log Schemas

> **Phase 2 invariáns:** minden agent kötelezően vezet 3 független log-streamet:
> Operational, Learning, Version.
>
> Ez a fájl definiálja a strukturált formátumokat.

> **Phase 5 update (2026-05-24):** Az Operational markdown stream **DEPRECATED** új eseményekre. Az új kanonikus operacionális megfigyelhetőségi réteg az `agent_observability.db` SQLite adatbázis, amelybe az `agent_log.py` writer API-n keresztül kell írni. A Learning és Version log markdown streamek változatlanul aktívak. Lásd §0 az új infrastruktúráért.

> **Phase 6 update (2026-05-24 — schema v1.3):** Scheduler tag-discriminator convention added (§0.S). `scheduled_jobs` + `job_runs` DDL cross-reference added. See `CONSTITUTION_PHASE_6.md` for the full scheduler architecture.

---

## 0. Phase 5 Observability Infrastructure (2026-05-24)

### agent_observability.db — Primary Operational Store

**Location:** `00_Prompts/BDOS/capabilities/vault-indexing/cache/agent_observability.db`

This SQLite database is the canonical, machine-queryable operational observability layer for the BDOS family. All six agents write to it. Maestro reads across all agents; each agent reads only its own scope.

**Table:** `agent_logs` (28 columns) — see `capabilities/vault-indexing/agent_obs_schema.sql` for the full DDL.

**Table DDL** (from `capabilities/vault-indexing/agent_obs_schema.sql`):

```sql
CREATE TABLE IF NOT EXISTS agent_logs (
  id                    INTEGER PRIMARY KEY AUTOINCREMENT,
  timestamp             TEXT    NOT NULL,                   -- ISO-8601 UTC
  agent_name            TEXT    NOT NULL CHECK(agent_name IN ('librarian','maestro','curator','presto','broker','alfred','forge')),
  agent_id              TEXT,                               -- optional stable UUID for the agent instance
  agent_version         TEXT,                               -- e.g. 0.7.0
  task_id               TEXT,                               -- groups events within one task
  operation_id          TEXT,                               -- groups events within one sub-operation
  parent_operation_id   TEXT,                               -- for nested operation hierarchies
  trace_id              TEXT,                               -- cross-agent trace correlation ID
  log_level             TEXT    NOT NULL DEFAULT 'info'
                               CHECK(log_level IN ('debug','info','notice','warning','error','critical')),
  event_type            TEXT    NOT NULL
                               CHECK(event_type IN (
                                 'task_started','task_completed','tool_call','query',
                                 'file_scan','index_update','token_usage','dashboard_update',
                                 'approval_requested','publish_prepared','publish_completed',
                                 'reflection','learning','version_change','error'
                               )),
  project               TEXT,                               -- vault unit / area slug (nullable)
  title                 TEXT,                               -- short event title
  message               TEXT    NOT NULL,                   -- full event description
  status                TEXT    CHECK(status IN ('success','partial','failure',NULL)),
  model_name            TEXT,                               -- e.g. claude-sonnet-4-6
  tool_name             TEXT,                               -- Read, Write, Edit, Bash, Grep, etc.
  input_tokens          INTEGER,
  output_tokens         INTEGER,
  total_tokens          INTEGER,                            -- stored (input+output) for query speed
  estimated_cost        REAL,                               -- auto-computed from tokens + model cost table
  duration_ms           INTEGER,                            -- wall-clock duration
  query_duration_ms     INTEGER,                            -- Librarian: DB/index query time
  affected_files        TEXT,                               -- JSON array of file paths touched
  tags                  TEXT,                               -- JSON array of extra tags
  metadata_json         TEXT,                               -- JSON blob for extra context
  error_message         TEXT,                               -- extracted error string (for error events)
  created_at            TEXT    NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%SZ','now'))
);
```

28 columns total. Key indexes: `(agent_name, timestamp)`, `(agent_name, log_level)`, `task_id`, `status`.
FTS5 virtual table `agent_logs_fts` on `title` + `message`.

**Log levels (6):** `debug` | `info` | `notice` | `warning` | `error` | `critical`

**Event types (15):** `task_started` | `task_completed` | `tool_call` | `query` | `file_scan` | `index_update` | `token_usage` | `dashboard_update` | `approval_requested` | `publish_prepared` | `publish_completed` | `reflection` | `learning` | `version_change` | `error`

**Notable columns:**
- `query_duration_ms` — Librarian-specific: vault DB / index query latency; key for retrieve-mode performance optimization
- `total_tokens` — stored column (not computed) = `input_tokens + output_tokens`; kept for query speed
- `title` — short summary separate from full `message`; both indexed in FTS5
- `affected_files` — JSON array; populated by file_scan and index_update events
- `error_message` — extracted for error events; searchable separately from message

**Column name migration from v1.0/v1.1:**

| Old column (agent_events) | New column (agent_logs) |
|---|---|
| `ts` | `timestamp` |
| `agent` | `agent_name` |
| `level` | `log_level` |
| `model` | `model_name` |
| `tool_used` | `tool_name` |
| `tokens_in` | `input_tokens` |
| `tokens_out` | `output_tokens` |
| `outcome` | `status` |
| `session_id` | `task_id` |
| `parent_event_id` | `parent_operation_id` |
| `payload` | `metadata_json` |
| `invocation_start` event_type | `task_started` |
| `invocation_end` event_type | `task_completed` |
| `warn` level | `warning` |
| `fatal` level | `critical` |

**Sidecar JSON:** `_dashboards/_design/agent_logs.json` — auto-refreshed on every insert (last 500 events). This is the transport layer for HTML dashboards — no server-side Python required in the browser context.

### Writer API Contract

**Module:** `capabilities/vault-indexing/agent_log.py`

**Preferred usage — `AgentLogger` class:**

```python
from agent_log import AgentLogger

log = AgentLogger(agent='<agent_name>', model='claude-sonnet-4-6')

# 1. Log task_started (starts wall-clock timer)
start_id = log.start(mode='<mode>', project='<optional-slug>')

# 2. Log tool calls during work
log.tool('<ToolName>', '<description>', duration_ms=42)

# 3. Log decisions, info, warnings as needed
log.decision('<description>')          # -> approval_requested event
log.info('<description>')              # -> task_completed/info
log.warn('<description>')              # -> error/warning level
log.query('<description>', query_duration_ms=18)  # Librarian only

# 4. Log task_completed (auto-computes duration from start())
log.end(status='success', input_tokens=2100, output_tokens=480)
```

**Low-level usage — `log_event` function (single insert):**

```python
from agent_log import log_event

log_event(
    agent_name='<agent_name>',
    mode='<mode>',
    event_type='task_completed',  # one of the 15 brief event types
    message='<description>',
    log_level='info',             # debug | info | notice | warning | error | critical
    input_tokens=None,
    output_tokens=None,
    duration_ms=None,
    query_duration_ms=None,       # Librarian only
    status=None,                  # success | partial | failure (for task_completed)
    task_id=None,
    metadata_json={'key': 'value'},  # optional JSON context blob
)
```

**Invariants (Phase 5 constitutional rules — schema v1.2):**
1. `input_tokens` and `output_tokens` MUST be populated on every `task_completed` event.
2. `duration_ms` MUST be populated on every `task_completed` event.
3. The DB is append-only. Corrections are new rows, never updates to existing rows.
4. `estimated_cost` is auto-computed by `agent_log.py` from the `MODEL_COSTS` table — do not set manually.
5. `total_tokens` is auto-computed as `input_tokens + output_tokens` and stored for query speed.

### §0.S — Phase 6 Scheduler Tag-Discriminator Convention (schema v1.3)

All scheduler events written to `agent_logs` carry a structured `tags` JSON array that allows Logcat and analytics queries to discriminate scheduler traffic from agent-invocation traffic.

**Tag pattern:**

```python
tags = ['scheduler'] + (['job:' + job_id] if job_id else [])
# e.g. ['scheduler', 'job:sage-daily-harvest']
```

The `agent_name` field for scheduler infrastructure events is `'maestro'` (the scheduler is an infrastructure concern owned by the conductor). Individual agent job completions logged from within a job's subprocess use the owning agent's `agent_name`.

**11 scheduler tag values in use:**

| Tag value | When present |
|---|---|
| `scheduler` | All scheduler events — always present on every scheduler-emitted row |
| `job:alfred-daily-harvest` | Alfred daily harvest dispatch / completion / skip |
| `job:alfred-weekly-curate` | Alfred weekly curate dispatch / completion / skip |
| `job:maestro-daily-observe` | Maestro daily observe (not yet seeded — example) |
| `job:librarian-weekly-index` | Librarian weekly global re-index (not yet seeded — example) |
| `job:presto-daily-today` | Presto daily campaign-check (not yet seeded — example) |
| `job:curator-weekly-survey` | Curator weekly dashboard survey (not yet seeded — example) |
| `job:broker-daily-today` | Broker daily pipeline check (not yet seeded — example) |
| `job:<custom-job-id>` | Any other job inserted into `scheduled_jobs` — dynamic, follows slug |
| (lock expiry events) | `scheduler` only — no `job:*` tag; these are cross-job maintenance events |
| (scheduler loop start) | `scheduler` only — no `job:*` tag; emitted once on daemon start |

**Logcat filter usage:**

```sql
-- All scheduler traffic
SELECT * FROM agent_logs WHERE tags LIKE '%"scheduler"%' ORDER BY timestamp DESC;

-- Sage harvest runs only
SELECT * FROM agent_logs WHERE tags LIKE '%"job:alfred-daily-harvest"%' ORDER BY timestamp DESC;

-- All failed scheduler dispatches
SELECT * FROM agent_logs
WHERE tags LIKE '%"scheduler"%' AND status = 'failure' ORDER BY timestamp DESC;
```

### §0.J — Scheduler DDL Tables (`scheduled_jobs` + `job_runs`)

**Authoritative DDL:** `00_Prompts/BDOS/capabilities/vault-indexing/scheduler_schema.sql` (schema v1.4)

**Constitutional reference:** `CONSTITUTION_PHASE_6.md` — full architecture, lock protocol, 9 job states, `requires_approval` semantics.

**`scheduled_jobs` — job registry (17 columns):**

```
job_id TEXT UNIQUE           -- stable slug (e.g. 'alfred-daily-harvest')
job_name TEXT                -- human label
agent_name TEXT              -- owning agent
description TEXT             -- optional longer description
schedule_type TEXT           -- 'daily' | 'weekly' | 'interval' | 'manual'
schedule_hour INTEGER        -- UTC hour (daily/weekly)
schedule_minute INTEGER      -- UTC minute (default 0)
schedule_weekday INTEGER     -- 0=Mon…6=Sun (weekly only)
interval_seconds INTEGER     -- seconds between runs (interval only)
command TEXT                 -- full shell command / script path
requires_approval INTEGER    -- 0=auto-run, 1=human-approval gate
lock_duration_s INTEGER      -- per-job lock override (default 600s / 10 min)
enabled INTEGER              -- 0=soft-disabled
last_run_at TEXT             -- ISO-8601 UTC of last dispatch
next_run_at TEXT             -- ISO-8601 UTC of next expected run
created_at TEXT
updated_at TEXT
```

**`job_runs` — per-execution log (20 columns):**

```
job_id TEXT (FK)             -- references scheduled_jobs.job_id
run_id TEXT UNIQUE           -- UUID for this run
job_name TEXT                -- denormalized for query convenience
agent_name TEXT              -- denormalized for query convenience
schedule_type TEXT           -- snapshot at dispatch time
scheduled_for TEXT           -- ISO-8601 UTC when this run was expected
last_run_at TEXT             -- ISO-8601 UTC of previous run (snapshot)
next_run_at TEXT             -- ISO-8601 UTC next expected run after this one
status TEXT                  -- 9 states (see CONSTITUTION_PHASE_6 §6)
claimed_by_device TEXT       -- device_id (~/.bdos/device_id) that dispatched
claimed_at TEXT              -- ISO-8601 UTC when lock was acquired
lock_until TEXT              -- ISO-8601 UTC when lock expires
completed_at TEXT
failed_at TEXT
duration_ms INTEGER
result_summary TEXT          -- last ~2000 chars of stdout
error_message TEXT           -- last ~2000 chars of stderr
metadata_json TEXT           -- JSON blob (exit_code, command, etc.)
created_at TEXT
```

**9 job_runs status states:** `pending` | `due` | `running` | `completed` | `failed` | `skipped` | `locked` | `overdue` | `disabled`

---

### Operational Markdown Stream — DEPRECATED

**Status: DEPRECATED for new events as of 2026-05-24.**

The markdown stream at `agents/<name>/logs/operational/<YYYY-MM>.md` (schema `bdos.operational.log.v1`) is no longer the primary sink for operational events. Existing historical entries remain and are not to be backfilled or deleted. New agent invocations MUST write to `agent_observability.db` instead.

The `bdos.operational.log.v1` schema below (§1) is retained for reference and backward compatibility only.

---

## Folder konvenció

Minden agent home alatt:

```
00_Prompts/BDOS/agents/<agent-name>/
└── logs/
    ├── operational/
    │   └── <YYYY-MM>.md       ← havi, append-only
    ├── learning/
    │   └── <YYYY-MM>.md
    └── version/
        └── <YYYY-MM>.md
```

**Megjegyzés (Sage-Alfred migráció):** Sage legacy `_journal/` stream-je `02_Areas/Personal Growth/Ideas/_journal/<YYYY-MM>.md`-ben él, megmarad archívumként. Alfred az `agents/alfred/logs/` konvenciót követi Phase 2.B óta.

---

## Fájl struktúra — havi log fájl

Minden havi fájl frontmatterrel kezdődik, alatta egymás után YAML-blokkok jönnek:

```markdown
---
schema: bdos.<stream>.log.v1
agent: <agent-name>
month: 2026-05
---

# <Agent> <Stream> Log — 2026-05

Append-only audit trail. Minden bejegyzés egy ` ```yaml ``` ` blokk.

\`\`\`yaml
event: ...
ts: 2026-05-24T06:00:42+02:00
...
\`\`\`

\`\`\`yaml
event: ...
...
\`\`\`
```

A YAML blokk-konvenció:
- Minden bejegyzés egy ```` ```yaml ```` és ```` ``` ```` között
- Egy regex parser (`^```yaml$ ... ^```$`) ki tudja venni mindet
- Obsidianban olvasható marad

---

## 1. Operational Log *(markdown stream — DEPRECATED for new events; see §0 for the SQLite DB)*

**Mit logol:** meaningful work execution — egy slash command futása / agent invocation / scheduled task fire.

**Granularitás:** egy log entry per agent-invocation. NEM minden tool-call. Egy `/alf-harvest` futás = 1 bejegyzés, sub-statisztikákkal.

### Schema — `bdos.operational.log.v1`

```yaml
event: operation
ts: <ISO 8601 with timezone>
op_id: <unique slug, pl. "sage-harvest-2026-05-24-0600">
agent: <agent-name>
mode: <which mode was invoked, pl. "harvest" | "curate" | "team-status">
command: "<the slash command or invocation, pl. /alf-harvest>"
model: <claude-sonnet-4-6 | claude-opus-4-7 | etc.>
tokens:
  input: null              # Phase 2.C-ben feltöltődik
  output: null
  total: null
cost_estimate_usd: null    # Phase 2.C-ben feltöltődik
category: <scheduled-harvest | user-invoked | system-orchestrated | maintenance>
duration_ms: <integer | null>
trigger:
  type: <cron | manual | parent-agent | hook>
  source: <"cron daily 06:00" | "/sage-harvest from user" | "Maestro team-promote" | etc.>
inputs:
  - <key>: <value>          # mit kapott, pl. references_seen: 2
outputs:
  - <key>: <value>          # mit produkált, pl. thoughts_created: 1
downstream_effects:
  - "<plain description of side effects>"
  - "<file path that was created/modified>"
outcome: <success | partial | failure | aborted>
errors: []                  # ha outcome != success
notes: <optional one-line note>
```

### Példa

```yaml
event: operation
ts: 2026-05-24T06:00:42+02:00
op_id: alfred-harvest-2026-05-24-0600
agent: alfred
mode: harvest
command: "/alf-harvest"
model: claude-sonnet-4-6
tokens:
  input: null
  output: null
  total: null
cost_estimate_usd: null
category: scheduled-harvest
duration_ms: 412000
trigger:
  type: cron
  source: "launchd com.becze.alfred-daily-harvest 06:00 Europe/Bucharest"
inputs:
  - references_seen: 2
outputs:
  - thoughts_created: 1
  - atomic_proposals: 1
  - inbox_uncertain: 0
downstream_effects:
  - "thoughts/2026-05-24_cognition-distribution-wall.md created"
  - "_inbox/atomic_proposals/marketing-as-translation.md created"
  - "00_INDEX.md regenerated"
  - "state/last_run.md updated"
outcome: success
errors: []
notes: "First scheduled harvest after alfred-daily-harvest setup (migrated from Sage)"
```

---

## 2. Learning Log

**Mit logol:** reflection events — felfedezések, ismétlődő hibák, optimalizációs lehetőségek.

**Mikor írunk learning bejegyzést:** amikor egy agent (vagy Maestro reflektív analízis közben) észrevesz valami **mintát**, ami nem egyetlen futás eseménye.

**Granularitás:** ritka. Nem minden futáskor. Csak amikor van mit jegyzeni.

### Schema — `bdos.learning.log.v1`

```yaml
event: learning
ts: <ISO 8601>
learning_id: <unique slug>
agent: <agent-name that observed/produced>
type: <discovery | recurring-failure | optimization | workflow-insight | prompt-weakness | successful-pattern | improvement>
title: "<short human title>"
context: "<which scenario this came from>"
evidence:
  - "[[logs/operational/2026-05.md#op-...]]"
  - "[[logs/operational/2026-05.md#op-...]]"
proposed_action: "<what could be done about this>"
status: <open | actioned | retired>
actioned_in: null            # kitöltve ha actioned: link a Version Log bejegyzéshez
actioned_at: null            # ISO ts ha actioned
related_learnings: []        # opcionális cross-link más learningekhez
```

### Példa

```yaml
event: learning
ts: 2026-06-02T09:15:00+02:00
learning_id: sage-voice-fillers-not-instructions
agent: sage
type: prompt-weakness
title: "Voice fillers ('gyakorlatilag', 'tulajdonképpen') are parsed as instructions"
context: "Observed in 3 separate harvest runs in May. Sage tried to extract them as commands."
evidence:
  - "[[logs/operational/2026-05.md#sage-harvest-2026-05-15-0600]]"
  - "[[logs/operational/2026-05.md#sage-harvest-2026-05-22-0600]]"
  - "[[logs/operational/2026-05.md#sage-harvest-2026-06-01-0600]]"
proposed_action: "Add explicit filter to daily_harvest.md §3.c for known voice fillers"
status: open
actioned_in: null
actioned_at: null
related_learnings: []
```

### Megjegyzés az agent learnings-rendszerrol

Alfred (és Presto, Broker, Forge) rendelkezik egy `learnings/proposals|active|retired/` rendszerrel (Sage innovációja, Phase 2.B-ben kiterjesztve). Ezek **PROMOTE**-ot kapnak a Learning Log-ból (egy nyitott learning ami beigazolódik → active learning). Azaz:

- **Learning Log** = nyers reflection-stream (minden agent)
- **Agent learnings/** = kifejlesztett user-reviewed taste-modeling (Alfred örökli a Sage-tól, más agenteknél is elérheto)

---

## 3. Version Log

**Mit logol:** evolúciós eseményeket — prompt-, workflow-, viselkedés-, architektúra-változások.

**Mikor írunk version bejegyzést:** minden agent-szintű változtatáskor (canonical edit, registration version bump, slash command add/remove, prompt rewrite).

**Granularitás:** minden szignifikáns változás kap egyet. Tipográfiai fix nem.

### Schema — `bdos.version.log.v1`

```yaml
event: version-change
ts: <ISO 8601>
change_id: <unique slug>
agent: <agent-name>
type: <prompt-change | workflow-change | behavior-change | architecture-change | token-optimization | mode-add | mode-remove | rename>
from_version: <semver, pl. "0.2">
to_version: <semver, pl. "0.3">
description: "<short human description>"
expected_impact: "<what the user/Maestro expects to change as a result>"
actually_measured_impact: null    # töltsd ki később ha mérted
reversible: <true | false>
rollback_path: "<how to undo this change>"
related_learning: null            # ha ez a változás egy actioned learning, link ide
approved_by: <user | maestro-team-promote | autonomous>  # csak `autonomous` ha tényleg autonóm, Phase 2-ben legtöbbször `user`
files_touched:
  - <path>
```

### Példa

```yaml
event: version-change
ts: 2026-06-03T11:00:00+02:00
change_id: sage-voice-filler-filter-added
agent: sage
type: prompt-change
from_version: 0.2
to_version: 0.3
description: "Added voice-filler filter to daily_harvest.md §3.c — Sage now ignores 'gyakorlatilag', 'tulajdonképpen' etc. as non-instructional."
expected_impact: "~5% reduction in false-positive instruction parsing during harvest"
actually_measured_impact: null
reversible: true
rollback_path: "Remove the §3.c filter section from daily_harvest.md"
related_learning: "[[logs/learning/2026-06.md#sage-voice-fillers-not-instructions]]"
approved_by: user
files_touched:
  - "00_Prompts/BDOS/agents/sage/prompts/daily_harvest.md"
  - "00_Prompts/BDOS/agents/sage.md"
  - ".claude/agents/sage.md"
```

---

## 4. Maestro-aggregálás

Maestro a `observe` és `reflect` módokban ezeket a fájlokat olvassa:

```
00_Prompts/BDOS/agents/*/logs/operational/*.md
00_Prompts/BDOS/agents/*/logs/learning/*.md
00_Prompts/BDOS/agents/*/logs/version/*.md
```

Egy parseolható minta — YAML-blokkok-szám:
- Operational entries / hónap / agent → activity metrics
- Learning entries — open vs actioned → reflection health
- Version entries — changes / hónap / agent → evolution velocity

Lásd `agents/maestro.md` §4.C (Observability Domain).

---

## 5. Maestro Dashboard adatforrás

A Maestro Dashboard a `_dashboards/maestro/index.html` minden 8 másodpercben:

- Globbol minden `00_Prompts/BDOS/agents/*/logs/*/2026-*.md`-t
- Parse-olja a YAML blokkokat
- Aggregálja per agent / per stream / per időablak
- Render-eli a 6 fő panel valamelyikébe

Mivel **markdown-state driven**, a dashboardon semmilyen szám sem hardcode-olt — minden a fájlokból jön.

---

## 6. Backward compatibility

Schema-evolúció szabályok:

- **Új mező hozzáadása** engedélyezett, default `null`
- **Mező típus változtatása** TILOS
- **Mező törlés** TILOS — deprecated-jelölés szabad, de a mező marad
- **Schema major-bump** (pl. `v1 → v2`) csak constitution-level változásnál

---

## 7. Empty state

Egy újonnan létrejött havi log-fájl (még nincs benne bejegyzés) így néz ki:

```markdown
---
schema: bdos.<stream>.log.v1
agent: <name>
month: 2026-05
---

# <Agent> <Stream> Log — 2026-05

Append-only audit trail. **Üres** — még nincs bejegyzés ebben a hónapban.
```

A Maestro Dashboard üres-state-ben "Csendes hónap" / "Nincs adat" panel-rendert ad.

---

## 8. Hivatkozott dokumentumok

- Phase 2 alkotmány: [`CONSTITUTION_PHASE_2.md`](CONSTITUTION_PHASE_2.md)
- Maestro canonical (v0.3+): [`agents/maestro.md`](agents/maestro.md)
- Session-bootstrap primer: [`00_BDOS_PRIMER.md`](00_BDOS_PRIMER.md)
