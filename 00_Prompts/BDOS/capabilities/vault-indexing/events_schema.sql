-- events_schema.sql — BDOS append-only event log DDL (B2 v0.1, 2026-05-29)
-- Lives in agent_observability.db (synced, shared) alongside agent_logs +
-- scheduled_jobs. This is the structured inter-agent coordination/audit log
-- the 2026-05-29 study (B2) called the "missing primitive".
--
-- v0.1 is EMIT-ONLY: agents write events instead of signalling each other by
-- editing shared markdown. The `processed` column is reserved for a future
-- reactor (B6) that would dispatch on events; nothing consumes it yet.
--
-- Source-of-truth: per ARCHITECTURE_BOUNDARIES.md §3, machine events are the
-- telemetry class -> SQLite-canonical. A human-readable markdown cold-record
-- can be batched later if needed; the DB is the truth for events.

CREATE TABLE IF NOT EXISTS events (
  id            INTEGER PRIMARY KEY AUTOINCREMENT,
  event_id      TEXT    NOT NULL UNIQUE,                 -- UUID for this event
  event_type    TEXT    NOT NULL,                        -- dotted: seed.created, publication.approved, task.created, file.indexed, comment.detected, job.due
  source_agent  TEXT,                                    -- emitter: agent name, 'human', or 'system'
  scope         TEXT,                                    -- project/area slug (e.g. 'deak-husuzlet')
  payload_json  TEXT,                                    -- JSON blob with event-specific data
  device_id     TEXT,                                    -- machine that emitted (single-owner clarity)
  occurred_at   TEXT    NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%SZ','now')),  -- ISO-8601 UTC
  processed     INTEGER NOT NULL DEFAULT 0               -- RESERVED for future reactor (B6); emit-only today
);

CREATE INDEX IF NOT EXISTS idx_events_type        ON events(event_type);
CREATE INDEX IF NOT EXISTS idx_events_occurred_at ON events(occurred_at);
CREATE INDEX IF NOT EXISTS idx_events_scope       ON events(scope);
CREATE INDEX IF NOT EXISTS idx_events_processed   ON events(processed);
