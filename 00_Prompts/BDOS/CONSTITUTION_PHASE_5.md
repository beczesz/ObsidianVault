---
title: BDOS Constitution — Phase 5
date: 2026-05-24
author: Becze Szabolcs
status: active
version: 1.0
description: Phase 5 constitution for the BDOS agent family. Codifies the Observability v2 invariant: operational events are first-class structured data written to agent_observability.db via agent_log.py; the markdown operational stream is deprecated for new events; learning and version markdown streams remain the human-readable narrative layer; token and duration logging are mandatory on every LLM call; the DB is append-only; Maestro is the global reader; all other agents read only their own scope.
tags: [BDOS, constitution, observability, phase5, sqlite]
id: f3a2c8e1-4b77-4d9e-8c1f-9d0e7b5a2c34
index_schema_version: 1
---

# BDOS Constitution — Phase 5

> **Effective date:** 2026-05-24
> **Scope:** All 7 active agents — Librarian, Maestro, Curator, Presto, Broker, Alfred, Forge.
> **Supersedes:** Phase 2 operational log-stream requirement (operational markdown DEPRECATED for new events).
> **Extends:** Phase 2 (3-stream invariant), Phase 3.1 (description mandate), Phase 4 (Memory OS / UUID).

---

## 1. The Phase 5 Invariant — Structured Observability

**Operational events are first-class structured data, not prose.**

Every meaningful agent invocation MUST produce at minimum two structured rows in the `agent_events` table:

1. An `invocation_start` row at mode entry.
2. An `invocation_end` row at mode exit, with `tokens_in`, `tokens_out`, and `duration_ms` populated.

Tool calls, decisions, warnings, errors, and handoffs MAY be logged as additional rows within the same `session_id`.

This is not optional. An agent invocation that produces no DB rows is an observability gap.

---

## 2. The Canonical Observability Store

```
00_Prompts/BDOS/capabilities/vault-indexing/cache/agent_observability.db
```

Table: `agent_logs` (DDL in `capabilities/vault-indexing/agent_obs_schema.sql`).

The sidecar JSON at `_dashboards/_design/agent_logs.json` is the transport layer for HTML dashboards. It is refreshed automatically on every DB insert by `agent_log.py`. Do not write to it directly.

---

## 3. The Writer API

All writes to `agent_observability.db` MUST go through the writer API:

```
capabilities/vault-indexing/agent_log.py
```

Exported surface:
- `AgentLogger(agent, session_id, model, auto_refresh)` — stateful class, preferred
- `log_event(agent, mode, event_type, message, ...)` — low-level single-row insert

The writer API is the single point of schema enforcement. Direct SQLite writes bypassing `agent_log.py` are prohibited — they may violate CHECK constraints, skip cost estimation, or miss the sidecar refresh.

---

## 4. Token Usage is Mandatory

**Token counts MUST be logged on every LLM call.**

`tokens_in` and `tokens_out` are REQUIRED fields on every `invocation_end` event. A `null` value is acceptable only when the agent runs in a context where token counts are genuinely unavailable (e.g., a tool-only subprocess with no LLM call in that span). In all other cases, `null` tokens = a logging defect.

Rationale: token economics drive every architectural decision in the BDOS. Invisible cost = invisible waste. The `estimated_cost` field is auto-populated from the `MODEL_COSTS` table in `agent_log.py` — agents do not compute it manually.

---

## 5. Duration is Mandatory

**Duration MUST be logged on every meaningful operation.**

`duration_ms` is REQUIRED on every `invocation_end` event. `AgentLogger.start()` starts the wall-clock timer automatically; `AgentLogger.end()` auto-computes and sets `duration_ms`. For agents not using the class wrapper, `duration_ms` must be measured and passed explicitly.

Rationale: latency is a first-class observable. Hidden latency = hidden user experience cost.

---

## 6. The DB is Append-Only

**`agent_logs` rows are never updated or deleted.**

Corrections, retries, and revised interpretations are expressed as new rows, not as modifications to existing ones. The `parent_operation_id` foreign key allows a correction row to reference the row it supersedes — use this convention rather than silent overwrites.

The `obs_build_meta` table's `created_at` and `schema_version` keys are the only rows that may be upserted (schema initialization).

---

## 7. The Two-Layer Model

Phase 5 maintains a strict separation between two layers:

| Layer | What it is | Deprecated? |
|---|---|---|
| **SQLite `agent_logs`** | Machine-queryable operational events. Fine-grained, row-per-event. | No — this is the new primary layer |
| **Markdown Operational** (`logs/operational/*.md`) | Prose append-only per-invocation summaries in YAML-block format. | **Yes — DEPRECATED for new events** |
| **Markdown Learning** (`logs/learning/*.md`) | Human-readable reflection stream. Pattern observations. | No — remains active |
| **Markdown Version** (`logs/version/*.md`) | Human-readable evolution stream. Prompt and workflow changes. | No — remains active |

The learning and version markdown streams are the **human-readable narrative layer**. They answer "what did we learn?" and "what changed and why?". The SQLite DB answers "what happened, when, how long, at what cost?".

Neither layer is a substitute for the other. Both must be maintained for the system to be fully observable.

---

## 8. Reader Scope

**All 7 agents are log-writers. Maestro is the global reader. Each other agent reads only its own scope.**

| Agent | Write scope | Read scope |
|---|---|---|
| Librarian | `agent='librarian'` | `agent='librarian'` only |
| Maestro | `agent='maestro'` | ALL agents (no filter) |
| Curator | `agent='curator'` | `agent='curator'` only |
| Presto | `agent='presto'` | `agent='presto'` only |
| Alfred | `agent='alfred'` | `agent='alfred'` only |
| Broker | `agent='broker'` | `agent='broker'` only |
| Forge | `agent='forge'` | `agent='forge'` only |

Maestro's `observe`, `reflect`, and `optimize` modes query the full `agent_logs` table. Every Maestro observation run MUST itself be logged — so it is visible in future observation cycles (self-referential invariant).

Query tooling: `capabilities/vault-indexing/agent_log_query.py` provides a Python API and CLI for reading events. Maestro uses this in its observability modes.

---

## 9. Relationship to Prior Constitutions

| Constitution | Status | What it defined |
|---|---|---|
| Phase 2 | Active (partially superseded) | 3-stream logging invariant (Operational + Learning + Version), Maestro as reflective nervous system |
| Phase 3.1 | Active | `description:` field mandatory in all new files |
| Phase 4 | Active | UUID per indexed file, Memory OS, vault-indexing SQLite cache |
| **Phase 5 (this)** | **Active** | Observability v2 — SQLite as primary operational store, writer API contract, token + duration mandatory, append-only, reader scope |

Phase 2's 3-stream invariant is partially superseded: the Operational markdown stream is deprecated for new events. The Learning and Version streams remain fully active under Phase 2 rules.

---

## 10. Enforcement

The Maestro `team-audit` mode checks Phase 5 compliance as part of its per-agent checklist:

- Does the agent's canonical spec contain `## Observability v2`?
- Does it reference `agent_log.py` and `AgentLogger`?
- Is the operational markdown stream correctly marked as deprecated?
- Is the learning log and version log noted as active?

Librarian `audit` mode detects the absence of `## Observability v2` in agent canonicals as a compliance gap.

---

## 11. Hivatkozott dokumentumok

- Writer API: `capabilities/vault-indexing/agent_log.py`
- Query API: `capabilities/vault-indexing/agent_log_query.py`
- DB DDL: `capabilities/vault-indexing/agent_obs_schema.sql`
- Log schemas (markdown streams): `LOG_SCHEMAS.md`
- Phase 2 constitution: `CONSTITUTION_PHASE_2.md`
- Phase 4 constitution: `CONSTITUTION_PHASE_4.md`
- Agent canonicals: `agents/librarian.md`, `agents/maestro.md`, `agents/curator.md`, `agents/presto.md`, `agents/alfred.md`, `agents/broker.md`, `agents/forge.md`
- Agent index: `00_AGENTS_INDEX.md`
