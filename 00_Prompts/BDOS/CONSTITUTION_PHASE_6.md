---
title: BDOS Constitution — Phase 6 (Scheduler)
date: 2026-05-24
author: Becze Szabolcs
status: active
version: 1.0
description: Phase 6 constitutional invariants for BDOS agent scheduling. The local dashboard IS the BDOS control plane. Scheduling is dashboard-resident, not OS-resident. Codifies the scheduler architecture, 9 job states, multi-device safety via SQLite locks, requires_approval flag semantics, and the deprecation of launchd/cron for BDOS agent jobs.
tags: [BDOS, constitution, scheduler, phase6]
id: f3a1c8e2-7d45-4b89-a2f0-9e1d6b3c5078
index_schema_version: 1
---

# BDOS Constitution — Phase 6: Scheduler

> **Rationale:** Phase 5 gave the family a machine-queryable observability layer (SQLite `agent_logs`). Phase 6 gives it a dashboard-resident job scheduler. The scheduler is not a cron daemon — it is a thread inside the dashboard server, visible and controllable from the browser. This constitution locks the decisions made in Phase B-redux (2026-05-24).

---

## 1. The Dashboard IS the Control Plane

The local dashboard server (`_dashboards/_tools/dash-server.mjs` + embedded `events_server.py`) is the canonical BDOS control plane. The scheduler runs as a daemon thread inside `events_server.py`. This means:

- **Jobs only run while the dashboard is active.** If the dashboard server is not running, no scheduled jobs fire. This is acceptable — BDOS scheduling is not mission-critical infrastructure; it is cognitive assistance that degrades gracefully to manual invocation.
- **The scheduler state is fully visible** in the browser at `_dashboards/scheduler/index.html` (Health tab / Jobs tab / Logcat tab). No separate CLI or OS tool is needed to see what the scheduler is doing.
- **Starting the dashboard = starting the scheduler.** No separate daemon management.

## 2. Scheduling Is Dashboard-Resident, Not OS-Resident

The scheduler reads its job registry from the `scheduled_jobs` table in `agent_observability.db` — the same SQLite database used for `agent_logs`. Job definitions, run history, and lock state all live in one file.

**Consequence:** adding, disabling, or modifying a scheduled job is a SQL operation against `agent_observability.db`, not an OS-level change (no `launchctl`, no `crontab -e`, no `.plist` files).

## 3. launchd and cron Deprecation (BDOS scope only)

**launchd and cron are deprecated for BDOS agent scheduling as of Phase 6.**

Rationale:
- OS-level daemons survive dashboard shutdown, making scheduler state split across two systems.
- Dashboard-resident scheduling is observable and controllable from one UI.
- Phase B initial prototype used launchd; Phase B-redux supersedes it.

**Scope note:** this deprecation applies ONLY to BDOS agent jobs (Alfred harvest/curate, Maestro observe, Librarian re-index, etc.). System maintenance jobs, backups, and anything outside BDOS scope are unaffected; use launchd or cron freely for those.

**Migration:** any existing launchd `.plist` for Sage jobs should be unloaded and replaced with a `scheduled_jobs` INSERT. The `seed_alfred_cognition_jobs()` function in `scheduler.py` handles the Alfred seed rows idempotently (migrated from `seed_sage_jobs()` as part of the Sage-Alfred merge, 2026-05-28).

## 4. Multi-Device Safety via SQLite Locks on `job_runs`

BDOS may run on multiple machines (desktop + laptop). The scheduler must not dispatch a job on device B if device A is already running it. Safety is enforced by the `job_runs` table, NOT by machine-level file locks or OS primitives.

### Lock protocol (atomic acquire)

1. Before dispatching, the scheduler queries `job_runs` for any row where `job_id = ?` AND `status = 'running'` AND `claimed_at + lock_duration_s >= now`.
2. If such a row exists: skip this dispatch (record a `skipped` run row instead).
3. If no active lock: INSERT a new `job_runs` row with `status='running'`, `claimed_by_device=<device_id>`, `claimed_at=now`, `lock_until=now+lock_duration_s`.
4. On completion: UPDATE the `job_runs` row to `status='completed'` or `status='failed'`.
5. On scheduler startup: expire any `status='running'` rows whose `lock_until < now` by setting them to `status='failed'` with an error note `[lock expired — presumed dead]`.

### Device identity

Each machine has a stable device ID stored at `~/.bdos/device_id` (UUID4, auto-created on first run). This is the `claimed_by_device` value in `job_runs`. The file is per-user, per-machine — never shared.

## 5. Default Lock Duration and Per-Job Override

**Default lock duration: 600 seconds (10 minutes)**

This is the `DEFAULT_LOCK_DURATION_S` in `scheduler.py`. Every job inherits this unless overridden by the `lock_duration_s` column in `scheduled_jobs`.

Per-job overrides currently seeded:
- `alfred-daily-harvest`: 600s (10 min) — fast Chrome MCP scan
- `alfred-weekly-curate`: 1800s (30 min) — expensive multi-file analysis

Override guideline: set `lock_duration_s` to roughly 2× the expected wall-clock duration of the job. This leaves margin for slow runs without prematurely expiring and allowing double-dispatch.

## 6. The 9 Job States

The `job_runs.status` column has exactly 9 valid states:

| State | Meaning |
|---|---|
| `pending` | Inserted but not yet evaluated by the scheduler |
| `due` | Evaluated as due but not yet dispatched (transient — typically not observed) |
| `running` | Dispatched; lock is active; subprocess is in flight |
| `completed` | Subprocess exited with code 0 |
| `failed` | Subprocess exited non-zero, or lock expired, or dispatch error |
| `skipped` | Due but skipped because an active lock was held by another device/run |
| `locked` | Reserved for future use (e.g. manual lock by user in dashboard) |
| `overdue` | Future: computed state for jobs that never fired on schedule |
| `disabled` | Parent `scheduled_jobs.enabled=0` — run not attempted |

The scheduler only writes `running`, `completed`, `failed`, `skipped`. The dashboard UI may surface `locked`, `overdue`, `disabled` as computed display states.

## 7. requires_approval Flag Semantics

The `requires_approval` column in `scheduled_jobs` is an integer flag (0 or 1):

- **`requires_approval=0`** — the scheduler may auto-dispatch without human intervention. The job is safe to run autonomously because its side-effects are additive-only (writing new files) or read-only (generating reports). Examples: Alfred harvest, Maestro daily observe, Librarian weekly index, Presto daily today.
- **`requires_approval=1`** — the scheduler MUST NOT auto-dispatch. The job is blocked until a human explicitly triggers it from the dashboard Jobs tab. Examples: Alfred learn (learning-ops), Presto run, Broker run, Curator promote, Maestro team-promote.

The dashboard Jobs tab surfaces `requires_approval=1` jobs as "Awaiting approval" with a manual trigger button. The scheduler daemon skips them silently during its scan cycle.

**Constitutional rule:** any mode that can delete files, mutate existing content, close deals, send outreach, or publish content MUST have `requires_approval=1`. This is not negotiable.

## 8. All Scheduler Decisions Logged to `agent_logs`

Every meaningful scheduler event is written to the `agent_logs` table with:

```python
tags = ['scheduler'] + (['job:' + job_id] if job_id else [])
```

The `agent_name` is `'maestro'` for scheduler infrastructure events (the scheduler is an infra concern owned by the conductor). Individual agent job completions are logged under the agent's own `agent_name`.

### Scheduler tag taxonomy (11 values)

| Tag | When used |
|---|---|
| `scheduler` | All scheduler events — always present |
| `job:<job_id>` | Per-job events (e.g. `job:alfred-daily-harvest`) |
| `job:alfred-daily-harvest` | Alfred daily harvest dispatch/completion |
| `job:alfred-weekly-curate` | Alfred weekly curate dispatch/completion |
| `job:maestro-daily-observe` | Maestro daily observe (example — not yet seeded) |
| `job:librarian-weekly-index` | Librarian weekly index (example — not yet seeded) |
| `job:presto-daily-today` | Presto daily campaign check (example — not yet seeded) |
| `job:curator-weekly-survey` | Curator weekly survey (example — not yet seeded) |
| `job:broker-daily-today` | Broker daily pipeline check (example — not yet seeded) |
| (future agent job tags) | Pattern: `job:<agent>-<cadence>-<mode>` |
| (lock expiry events) | `scheduler` only — no job tag (cross-job maintenance) |

The full `tags` JSON array is stored in `agent_logs.tags`. Logcat in `_dashboards/scheduler/index.html` filters by these tags in real-time.

## 9. `scheduled_jobs` and `job_runs` DDL

The authoritative DDL lives in:

```
00_Prompts/BDOS/capabilities/vault-indexing/scheduler_schema.sql
```

Schema version: **v1.4** (Phase B-redux, 2026-05-24).

Summary:
- `scheduled_jobs` — job registry (17 columns): `job_id` (stable slug), `job_name`, `agent_name`, `description`, `schedule_type` (daily/weekly/interval/manual), `schedule_hour`, `schedule_minute`, `schedule_weekday`, `interval_seconds`, `command`, `requires_approval`, `lock_duration_s`, `enabled`, `last_run_at`, `next_run_at`, `created_at`, `updated_at`.
- `job_runs` — per-execution log (20 columns): `job_id` (FK), `run_id` (UUID), `job_name`, `agent_name`, `schedule_type`, `scheduled_for`, `last_run_at`, `next_run_at`, `status` (9 states), `claimed_by_device`, `claimed_at`, `lock_until`, `completed_at`, `failed_at`, `duration_ms`, `result_summary`, `error_message`, `metadata_json`, `created_at`.

See `scheduler_schema.sql` for full DDL including indexes and `obs_build_meta` version bump.

## 10. What Runs, What Does Not

| Acceptable for scheduling | Not acceptable for scheduling |
|---|---|
| Read-only observability (observe, today, status, audit) | Any mode that sends emails, LinkedIn DMs, or publishes content |
| Additive file writes (harvest, curate, index, survey) | Any mode that deletes vault files |
| Report generation (reflect, measure, audience) | Any mode that modifies deal state or closes sales |
| Index regeneration (librarian index, presto index, curator survey) | Any mode that touches agent canonical files without human review |

---

## 11. Changelog

- **v1.0 (2026-05-24):** Initial constitution. Codifies Phase 6 scheduling architecture: dashboard-as-control-plane, launchd/cron deprecation (BDOS scope), multi-device SQLite lock protocol, 9 job states, 10-minute default lock, requires_approval semantics, scheduler tag taxonomy, DDL reference.
