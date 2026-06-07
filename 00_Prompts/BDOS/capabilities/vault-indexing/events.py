#!/usr/bin/env python3
"""
events.py — BDOS append-only event log writer (B2 v0.1, 2026-05-29)
===================================================================
The structured inter-agent coordination/audit log the 2026-05-29 architectural
study called the "missing primitive". Replaces the anti-pattern of agents
signalling state by editing shared markdown files.

EMIT-ONLY for now. A future reactor (B6) may consume unprocessed events and
dispatch; nothing does today, so emitting an event has no side effects beyond
the append.

Lives in agent_observability.db (synced, shared) next to agent_logs. Per
ARCHITECTURE_BOUNDARIES.md §3, events are the telemetry class -> SQLite-canonical.

Usage (from any agent runner / script):

    from events import emit_event
    emit_event('publication.approved', source_agent='presto',
               scope='deak-husuzlet', payload={'publication_id': 'pub-123'})

CLI:
    python3 events.py --emit publication.approved --agent presto \
        --scope deak-husuzlet --payload '{"publication_id":"pub-123"}'
    python3 events.py --recent 20
    python3 events.py --recent 20 --type publication.approved
"""
from __future__ import annotations

import argparse
import json
import sys
import uuid
from pathlib import Path

_SCRIPT_DIR = Path(__file__).resolve().parent
if str(_SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_DIR))

import runtime  # connect() helper with busy_timeout + WAL
import agent_log  # DB_PATH = agent_observability.db (synced, shared)

DB_PATH = agent_log.DB_PATH
SCHEMA_PATH = _SCRIPT_DIR / "events_schema.sql"

_initialized = False


def _device_id() -> str:
    try:
        import scheduler
        return scheduler.get_device_id()
    except Exception:
        return "unknown"


def _connect():
    con = runtime.connect(DB_PATH, wal=True, busy_timeout_ms=5000, timeout=10)
    global _initialized
    if not _initialized:
        con.executescript(SCHEMA_PATH.read_text())
        _initialized = True
    return con


def emit_event(event_type: str, *, source_agent: str | None = None,
               scope: str | None = None, payload: dict | None = None,
               device_id: str | None = None) -> str:
    """Append one event. Returns the generated event_id. Emit-only (no dispatch)."""
    if not event_type or "." not in event_type:
        raise ValueError("event_type must be a dotted string, e.g. 'seed.created'")
    event_id = str(uuid.uuid4())
    con = _connect()
    try:
        con.execute(
            "INSERT INTO events (event_id, event_type, source_agent, scope, payload_json, device_id) "
            "VALUES (?, ?, ?, ?, ?, ?)",
            (
                event_id,
                event_type,
                source_agent,
                scope,
                json.dumps(payload, ensure_ascii=False) if payload is not None else None,
                device_id or _device_id(),
            ),
        )
        con.commit()
    finally:
        con.close()
    return event_id


def recent(limit: int = 20, event_type: str | None = None, scope: str | None = None):
    """Return the most recent events (list of dicts). Read helper for agents/CLI."""
    con = _connect()
    try:
        q = "SELECT event_id, event_type, source_agent, scope, payload_json, device_id, occurred_at, processed FROM events"
        clauses, params = [], []
        if event_type:
            clauses.append("event_type = ?"); params.append(event_type)
        if scope:
            clauses.append("scope = ?"); params.append(scope)
        if clauses:
            q += " WHERE " + " AND ".join(clauses)
        q += " ORDER BY id DESC LIMIT ?"; params.append(int(limit))
        cols = ["event_id", "event_type", "source_agent", "scope", "payload_json", "device_id", "occurred_at", "processed"]
        return [dict(zip(cols, row)) for row in con.execute(q, params).fetchall()]
    finally:
        con.close()


def _main(argv=None):
    ap = argparse.ArgumentParser(description="BDOS event log (emit-only v0.1)")
    ap.add_argument("--emit", metavar="EVENT_TYPE", help="emit an event of this dotted type")
    ap.add_argument("--agent", help="source agent name")
    ap.add_argument("--scope", help="project/area scope slug")
    ap.add_argument("--payload", help="JSON payload string")
    ap.add_argument("--recent", type=int, metavar="N", help="print the N most recent events")
    ap.add_argument("--type", help="filter --recent by event_type")
    args = ap.parse_args(argv)

    if args.emit:
        payload = json.loads(args.payload) if args.payload else None
        eid = emit_event(args.emit, source_agent=args.agent, scope=args.scope, payload=payload)
        print(json.dumps({"ok": True, "event_id": eid, "event_type": args.emit}))
        return 0
    if args.recent is not None:
        rows = recent(limit=args.recent, event_type=args.type)
        print(json.dumps(rows, indent=2, ensure_ascii=False))
        return 0
    ap.print_help()
    return 2


if __name__ == "__main__":
    raise SystemExit(_main())
