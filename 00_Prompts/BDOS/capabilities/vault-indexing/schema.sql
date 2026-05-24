-- BDOS Vault Indexing Schema v2 (Phase 4 — Memory OS additions)
-- Read-cache only. Markdown is source of truth.

CREATE TABLE IF NOT EXISTS notes (
  path TEXT PRIMARY KEY,

  -- Tier 0 (required for any indexed file)
  title TEXT,
  description TEXT,
  date TEXT,
  status TEXT,

  -- Tier 1 (Phase 4 — mandatory for new files)
  id TEXT,                       -- UUID4, stable across path moves
  index_schema_version INTEGER,
  bdos_index INTEGER,            -- 0/1, default 1 (opt-out model)

  -- Tier 2 (optional content-type-specific)
  schema_field TEXT,
  version TEXT,
  category TEXT,
  subcategory TEXT,
  tags TEXT,                     -- JSON array
  area TEXT,
  agent TEXT,
  source_chat_title TEXT,

  -- Tier 3 (Librarian-managed)
  health_state TEXT,             -- enum: ok|stale|needs_reindex|broken_frontmatter|duplicate_id|orphaned|missing_required_fields|archived|excluded
  indexed_at REAL,

  -- Filesystem metadata
  mtime REAL,
  size_bytes INTEGER,
  has_frontmatter INTEGER,
  body_word_count INTEGER
);

CREATE INDEX IF NOT EXISTS idx_notes_id ON notes(id);
CREATE INDEX IF NOT EXISTS idx_notes_category ON notes(category);
CREATE INDEX IF NOT EXISTS idx_notes_status ON notes(status);
CREATE INDEX IF NOT EXISTS idx_notes_area ON notes(area);
CREATE INDEX IF NOT EXISTS idx_notes_agent ON notes(agent);
CREATE INDEX IF NOT EXISTS idx_notes_schema ON notes(schema_field);
CREATE INDEX IF NOT EXISTS idx_notes_health ON notes(health_state);
CREATE INDEX IF NOT EXISTS idx_notes_bdos_index ON notes(bdos_index);

CREATE TABLE IF NOT EXISTS backlinks (
  source_path TEXT,
  target TEXT,
  resolved_path TEXT,
  resolved_id TEXT,              -- Phase 4: UUID-based resolution
  link_text TEXT,
  FOREIGN KEY(source_path) REFERENCES notes(path)
);

CREATE INDEX IF NOT EXISTS idx_backlinks_target ON backlinks(target);
CREATE INDEX IF NOT EXISTS idx_backlinks_source ON backlinks(source_path);
CREATE INDEX IF NOT EXISTS idx_backlinks_resolved_id ON backlinks(resolved_id);

CREATE VIRTUAL TABLE IF NOT EXISTS notes_fts USING fts5(
  path UNINDEXED,
  title,
  description,
  category UNINDEXED,
  tags
);

-- Phase 4.C placeholder (keyword + entity extraction, populated in Phase 4.C)
CREATE TABLE IF NOT EXISTS file_keywords (
  path TEXT,
  keyword TEXT,
  score REAL,
  FOREIGN KEY(path) REFERENCES notes(path)
);

CREATE TABLE IF NOT EXISTS file_entities (
  path TEXT,
  entity TEXT,
  entity_type TEXT,              -- person | project | atomic | url | etc.
  FOREIGN KEY(path) REFERENCES notes(path)
);

CREATE INDEX IF NOT EXISTS idx_file_keywords_keyword ON file_keywords(keyword);
CREATE INDEX IF NOT EXISTS idx_file_entities_entity ON file_entities(entity);

CREATE TABLE IF NOT EXISTS build_meta (
  key TEXT PRIMARY KEY,
  value TEXT
);
