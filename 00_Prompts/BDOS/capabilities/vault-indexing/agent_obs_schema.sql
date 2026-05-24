-- agent_observability.db Schema v1.4 (Phase B-redux — 2026-05-24)
-- v1.4 rebuilds scheduler tables to brief vocabulary (see scheduler_schema.sql).
--
-- agent_observability.db Schema v1.3 (Phase B — 2026-05-24)
-- v1.3 adds scheduler tables: scheduled_jobs + job_runs (see scheduler_schema.sql).
--
-- agent_observability.db Schema v1.2 (Phase 5 — 2026-05-24)
-- Sibling to vault.db in cache/. Read-write by agent_log.py; read-only by dashboards
-- via sidecar JSON (_dashboards/_design/agent_logs.json).
-- Markdown operational logs are DEPRECATED as primary stream; this DB is the
-- canonical observability source. Learning + Version log markdown stays active.
--
-- Schema history:
--   v1.0 (2026-05-24) — initial release with agent_events (8 event types, 5 levels)
--   v1.1 (2026-05-24) — Phase B observability stack built
--   v1.2 (2026-05-24) — Realigned to brief: agent_events -> agent_logs, 28 columns,
--                        15 event types, 6 log levels, query_duration_ms added,
--                        title/total_tokens/affected_files/error_message added.
--   v1.3 (2026-05-24) — Scheduler tables added (Phase B).
--   v1.4 (2026-05-24) — Scheduler tables rebuilt to brief vocabulary (Phase B-redux).
--                        scheduled_jobs: label→job_name, agent→agent_name,
--                          lock fields removed (moved to job_runs), description added.
--                        job_runs: device_id→claimed_by_device, finished_at→completed_at,
--                          failed_at added, output_tail→result_summary,
--                          error_tail→error_message, metadata_json added,
--                          status CHECK expanded to 9 states, lock fields added.

-- =========================================================================
-- Core event log  (28 columns)
-- =========================================================================
CREATE TABLE IF NOT EXISTS agent_logs (
  id                    INTEGER PRIMARY KEY AUTOINCREMENT,
  timestamp             TEXT    NOT NULL,                   -- ISO-8601 UTC e.g. 2026-05-24T10:30:00Z
  agent_name            TEXT    NOT NULL CHECK(agent_name IN ('librarian','maestro','curator','sage','presto','broker')),
  agent_id              TEXT,                               -- optional stable UUID for the agent instance
  agent_version         TEXT,                               -- e.g. 0.7.0
  task_id               TEXT,                               -- groups events within one task (replaces session_id)
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
  title                 TEXT,                               -- short event title (separate from message)
  message               TEXT    NOT NULL,                   -- full event description
  status                TEXT    CHECK(status IN ('success','partial','failure',NULL)),
  model_name            TEXT,                               -- claude-sonnet-4-6, claude-opus-4-7, etc.
  tool_name             TEXT,                               -- Read, Write, Edit, Bash, Grep, etc.
  input_tokens          INTEGER,
  output_tokens         INTEGER,
  total_tokens          INTEGER,                            -- stored (input+output) for query speed
  estimated_cost        REAL,                               -- auto-computed by agent_log.py from MODEL_COSTS
  duration_ms           INTEGER,                            -- wall-clock duration
  query_duration_ms     INTEGER,                            -- Librarian: DB/index query time (perf optimization)
  affected_files        TEXT,                               -- JSON array of file paths touched
  tags                  TEXT,                               -- JSON array of extra tags
  metadata_json         TEXT,                               -- JSON blob for extra context
  error_message         TEXT,                               -- extracted error string (for error events)
  created_at            TEXT    NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%SZ','now'))
);

-- Single-column indexes
CREATE INDEX IF NOT EXISTS idx_al_timestamp        ON agent_logs(timestamp);
CREATE INDEX IF NOT EXISTS idx_al_agent_name       ON agent_logs(agent_name);
CREATE INDEX IF NOT EXISTS idx_al_task_id          ON agent_logs(task_id);
CREATE INDEX IF NOT EXISTS idx_al_trace_id         ON agent_logs(trace_id);
CREATE INDEX IF NOT EXISTS idx_al_project          ON agent_logs(project);
CREATE INDEX IF NOT EXISTS idx_al_event_type       ON agent_logs(event_type);
CREATE INDEX IF NOT EXISTS idx_al_log_level        ON agent_logs(log_level);
CREATE INDEX IF NOT EXISTS idx_al_model_name       ON agent_logs(model_name);
CREATE INDEX IF NOT EXISTS idx_al_tool_name        ON agent_logs(tool_name);
CREATE INDEX IF NOT EXISTS idx_al_status           ON agent_logs(status);

-- Composite for "give me all errors for this agent in this month" query pattern
CREATE INDEX IF NOT EXISTS idx_al_agent_ts         ON agent_logs(agent_name, timestamp);
CREATE INDEX IF NOT EXISTS idx_al_agent_level      ON agent_logs(agent_name, log_level);

-- FTS5 on title + message for text-search filter in Logcat
CREATE VIRTUAL TABLE IF NOT EXISTS agent_logs_fts USING fts5(
  title, message,
  agent_name UNINDEXED,
  content='agent_logs',
  content_rowid='id'
);

-- Triggers to keep FTS in sync
CREATE TRIGGER IF NOT EXISTS al_fts_insert AFTER INSERT ON agent_logs BEGIN
  INSERT INTO agent_logs_fts(rowid, title, message, agent_name)
  VALUES (new.id, COALESCE(new.title,''), new.message, new.agent_name);
END;

CREATE TRIGGER IF NOT EXISTS al_fts_delete AFTER DELETE ON agent_logs BEGIN
  INSERT INTO agent_logs_fts(agent_logs_fts, rowid, title, message, agent_name)
  VALUES ('delete', old.id, COALESCE(old.title,''), old.message, old.agent_name);
END;

CREATE TRIGGER IF NOT EXISTS al_fts_update AFTER UPDATE ON agent_logs BEGIN
  INSERT INTO agent_logs_fts(agent_logs_fts, rowid, title, message, agent_name)
  VALUES ('delete', old.id, COALESCE(old.title,''), old.message, old.agent_name);
  INSERT INTO agent_logs_fts(rowid, title, message, agent_name)
  VALUES (new.id, COALESCE(new.title,''), new.message, new.agent_name);
END;

-- =========================================================================
-- Build / sidecar metadata
-- =========================================================================
CREATE TABLE IF NOT EXISTS obs_build_meta (
  key   TEXT PRIMARY KEY,
  value TEXT
);

-- Seed meta
INSERT OR REPLACE INTO obs_build_meta(key, value)
VALUES
  ('schema_version', '1.4'),
  ('created_at',     datetime('now')),
  ('sidecar_path',   '_dashboards/_design/agent_logs.json');

-- =========================================================================
-- Scheduler tables (v1.4 rebuild — see scheduler_schema.sql for full DDL)
-- =========================================================================

CREATE TABLE IF NOT EXISTS scheduled_jobs (
  id                  INTEGER PRIMARY KEY AUTOINCREMENT,
  job_id              TEXT    NOT NULL UNIQUE,        -- stable slug
  job_name            TEXT    NOT NULL,               -- human label
  agent_name          TEXT    NOT NULL,               -- which agent owns this job
  description         TEXT,                           -- longer description (optional)
  schedule_type       TEXT    NOT NULL
                              CHECK(schedule_type IN ('daily','weekly','interval','manual')),
  schedule_hour       INTEGER,
  schedule_minute     INTEGER DEFAULT 0,
  schedule_weekday    INTEGER,
  interval_seconds    INTEGER,
  command             TEXT    NOT NULL,
  requires_approval   INTEGER NOT NULL DEFAULT 0,
  lock_duration_s     INTEGER NOT NULL DEFAULT 600,
  enabled             INTEGER NOT NULL DEFAULT 1,
  last_run_at         TEXT,
  next_run_at         TEXT,
  created_at          TEXT    NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%SZ','now')),
  updated_at          TEXT    NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%SZ','now'))
);

CREATE INDEX IF NOT EXISTS idx_sj_job_id      ON scheduled_jobs(job_id);
CREATE INDEX IF NOT EXISTS idx_sj_enabled     ON scheduled_jobs(enabled);
CREATE INDEX IF NOT EXISTS idx_sj_next_run_at ON scheduled_jobs(next_run_at);
CREATE INDEX IF NOT EXISTS idx_sj_agent_name  ON scheduled_jobs(agent_name);

CREATE TABLE IF NOT EXISTS job_runs (
  id                  INTEGER PRIMARY KEY AUTOINCREMENT,
  job_id              TEXT    NOT NULL
                              REFERENCES scheduled_jobs(job_id) ON DELETE CASCADE,
  run_id              TEXT    NOT NULL UNIQUE,
  job_name            TEXT,
  agent_name          TEXT,
  schedule_type       TEXT,
  scheduled_for       TEXT,
  last_run_at         TEXT,
  next_run_at         TEXT,
  status              TEXT    NOT NULL DEFAULT 'pending'
                              CHECK(status IN (
                                'pending','due','running','completed','failed',
                                'skipped','locked','overdue','disabled'
                              )),
  claimed_by_device   TEXT,
  claimed_at          TEXT,
  lock_until          TEXT,
  completed_at        TEXT,
  failed_at           TEXT,
  duration_ms         INTEGER,
  result_summary      TEXT,
  error_message       TEXT,
  metadata_json       TEXT,
  created_at          TEXT    NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%SZ','now'))
);

CREATE INDEX IF NOT EXISTS idx_jr_job_id            ON job_runs(job_id);
CREATE INDEX IF NOT EXISTS idx_jr_run_id            ON job_runs(run_id);
CREATE INDEX IF NOT EXISTS idx_jr_status            ON job_runs(status);
CREATE INDEX IF NOT EXISTS idx_jr_claimed_by_device ON job_runs(claimed_by_device);
CREATE INDEX IF NOT EXISTS idx_jr_created_at        ON job_runs(created_at);
CREATE INDEX IF NOT EXISTS idx_jr_completed_at      ON job_runs(completed_at);
