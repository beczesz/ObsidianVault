-- scheduler_schema.sql — BDOS Job Scheduler DDL  (schema v1.4, Phase B-redux — 2026-05-24)
-- Appended to agent_observability.db alongside the existing agent_logs table.
--
-- Two tables:
--   scheduled_jobs   — job registry (what to run and when)
--   job_runs         — execution log (every dispatch attempt + outcome)
--
-- Schema history:
--   v1.3 (2026-05-24) — Phase B: scheduler tables added. Job lock via
--                        last_locked_at / lock_holder_id (atomic UPDATE pattern).
--                        Sage daily/weekly jobs seeded.
--   v1.4 (2026-05-24) — Phase B-redux: rebuilt to brief vocabulary.
--                        scheduled_jobs: label→job_name, agent→agent_name,
--                          removed last_locked_at/lock_holder_id (moved to job_runs),
--                          added description.
--                        job_runs: device_id→claimed_by_device, finished_at→completed_at,
--                          added failed_at, output_tail→result_summary,
--                          error_tail→error_message, added metadata_json,
--                          added job_name/agent_name/schedule_type/scheduled_for/
--                          last_run_at/next_run_at/claimed_at/lock_until,
--                          status CHECK expanded to 9 states.
--                          Lock fields now live on job_runs (a run is locked, not the def).

-- =========================================================================
-- scheduled_jobs  — job registry
-- =========================================================================
CREATE TABLE IF NOT EXISTS scheduled_jobs (
  id                  INTEGER PRIMARY KEY AUTOINCREMENT,
  job_id              TEXT    NOT NULL UNIQUE,        -- stable slug, e.g. 'sage-daily-harvest'
  job_name            TEXT    NOT NULL,               -- human label, e.g. 'Sage Daily Harvest'
  agent_name          TEXT    NOT NULL,               -- which agent owns this job
  description         TEXT,                           -- longer description (optional)
  schedule_type       TEXT    NOT NULL
                              CHECK(schedule_type IN ('daily','weekly','interval','manual')),
  schedule_hour       INTEGER,                        -- UTC hour for daily/weekly (NULL for interval/manual)
  schedule_minute     INTEGER DEFAULT 0,              -- UTC minute (default 0)
  schedule_weekday    INTEGER,                        -- 0=Mon…6=Sun for weekly (NULL otherwise)
  interval_seconds    INTEGER,                        -- for schedule_type='interval'
  command             TEXT    NOT NULL,               -- full shell command / script path
  requires_approval   INTEGER NOT NULL DEFAULT 0,     -- 0=auto-run, 1=human-approval gate
  lock_duration_s     INTEGER NOT NULL DEFAULT 600,   -- per-job lock duration override (default 10 min)
  enabled             INTEGER NOT NULL DEFAULT 1,     -- 0=disabled (soft-off without delete)
  last_run_at         TEXT,                           -- ISO-8601 UTC timestamp of last dispatch
  next_run_at         TEXT,                           -- ISO-8601 UTC timestamp of scheduled next run
  created_at          TEXT    NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%SZ','now')),
  updated_at          TEXT    NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%SZ','now'))
);

CREATE INDEX IF NOT EXISTS idx_sj_job_id      ON scheduled_jobs(job_id);
CREATE INDEX IF NOT EXISTS idx_sj_enabled     ON scheduled_jobs(enabled);
CREATE INDEX IF NOT EXISTS idx_sj_next_run_at ON scheduled_jobs(next_run_at);
CREATE INDEX IF NOT EXISTS idx_sj_agent_name  ON scheduled_jobs(agent_name);

-- =========================================================================
-- job_runs  — per-execution log
-- =========================================================================
CREATE TABLE IF NOT EXISTS job_runs (
  id                  INTEGER PRIMARY KEY AUTOINCREMENT,
  job_id              TEXT    NOT NULL
                              REFERENCES scheduled_jobs(job_id) ON DELETE CASCADE,
  run_id              TEXT    NOT NULL UNIQUE,        -- UUID for this run
  job_name            TEXT,                           -- denormalized for query convenience
  agent_name          TEXT,                           -- denormalized for query convenience
  schedule_type       TEXT,                           -- denormalized snapshot at dispatch time
  scheduled_for       TEXT,                           -- ISO-8601 UTC when this run was expected
  last_run_at         TEXT,                           -- ISO-8601 UTC of the previous run (snapshot)
  next_run_at         TEXT,                           -- ISO-8601 UTC next expected run after this one
  status              TEXT    NOT NULL DEFAULT 'pending'
                              CHECK(status IN (
                                'pending','due','running','completed','failed',
                                'skipped','locked','overdue','disabled'
                              )),
  claimed_by_device   TEXT,                           -- device_id that dispatched/locked this run
  claimed_at          TEXT,                           -- ISO-8601 UTC when the lock was acquired
  lock_until          TEXT,                           -- ISO-8601 UTC when the lock expires
  completed_at        TEXT,                           -- ISO-8601 UTC when run finished successfully
  failed_at           TEXT,                           -- ISO-8601 UTC when run failed
  duration_ms         INTEGER,                        -- wall-clock run duration in milliseconds
  result_summary      TEXT,                           -- last ~2000 chars of stdout
  error_message       TEXT,                           -- last ~2000 chars of stderr / error description
  metadata_json       TEXT,                           -- JSON blob for extra context (exit_code, etc.)
  created_at          TEXT    NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%SZ','now'))
);

CREATE INDEX IF NOT EXISTS idx_jr_job_id           ON job_runs(job_id);
CREATE INDEX IF NOT EXISTS idx_jr_run_id           ON job_runs(run_id);
CREATE INDEX IF NOT EXISTS idx_jr_status           ON job_runs(status);
CREATE INDEX IF NOT EXISTS idx_jr_claimed_by_device ON job_runs(claimed_by_device);
CREATE INDEX IF NOT EXISTS idx_jr_created_at       ON job_runs(created_at);
CREATE INDEX IF NOT EXISTS idx_jr_completed_at     ON job_runs(completed_at);

-- =========================================================================
-- Bump schema version in obs_build_meta
-- =========================================================================
INSERT OR REPLACE INTO obs_build_meta(key, value)
VALUES ('schema_version', '1.4');

INSERT OR REPLACE INTO obs_build_meta(key, value)
VALUES ('scheduler_rebuilt_at', datetime('now'));
