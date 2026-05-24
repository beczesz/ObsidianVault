#!/usr/bin/env python3
"""BDOS Vault Indexing — full rebuild.

Walks the vault, extracts frontmatter + wikilinks from every .md file,
populates SQLite cache. Idempotent — safe to re-run anytime.

Markdown is source of truth. This cache is regenerable.
"""

import os
import sys
import sqlite3
import re
import json
import time
import yaml
from pathlib import Path

# Vault root = 3 levels up from this script
SCRIPT_DIR = Path(__file__).resolve().parent
VAULT_ROOT = SCRIPT_DIR.parent.parent.parent.parent  # capabilities → BDOS → 00_Prompts → vault root
DB_PATH = SCRIPT_DIR / "cache" / "vault.db"
SCHEMA_PATH = SCRIPT_DIR / "schema.sql"

EXCLUDE_DIRS = {
    ".smart-env", ".obsidian", "04_Archive", "node_modules", ".git",
    ".trash", "_archive_old"  # known archive locations
}

FRONTMATTER_PATTERN = re.compile(r'^---\s*\n(.*?)\n---\s*\n', re.DOTALL)
WIKILINK_PATTERN = re.compile(r'\[\[([^\]|\n]+)(?:\|([^\]\n]+))?\]\]')
SIMPLE_KEY_VAL = re.compile(r'^([a-zA-Z_][a-zA-Z0-9_-]*): *(.*?)\s*$')


def lenient_yaml_parse(text):
    """Line-based fallback for when PyYAML fails (e.g. Hungarian typographic quotes
    inside double-quoted strings cause YAML parse errors). Extracts top-level
    key:value pairs only; ignores nested/multiline structures.
    """
    out = {}
    for line in text.splitlines():
        if not line or line.startswith('#') or line.startswith(' ') or line.startswith('\t'):
            continue
        m = SIMPLE_KEY_VAL.match(line)
        if not m:
            continue
        k, v = m.group(1), m.group(2).strip()
        # Strip outer ASCII quotes
        if len(v) >= 2 and v[0] == v[-1] and v[0] in ('"', "'"):
            v = v[1:-1]
        if v in ('', '[', '{', '|', '>'):
            continue
        out[k] = v
    return out


def extract_frontmatter(content):
    """Returns (frontmatter_dict, body_text, parse_method)."""
    m = FRONTMATTER_PATTERN.match(content)
    if not m:
        return {}, content, 'none'
    fm_text = m.group(1)
    body = content[m.end():]
    try:
        fm = yaml.safe_load(fm_text)
        if isinstance(fm, dict):
            return fm, body, 'yaml'
        # Result isn't a dict — fall back
        fm2 = lenient_yaml_parse(fm_text)
        return fm2, body, ('lenient' if fm2 else 'failed')
    except yaml.YAMLError:
        fm = lenient_yaml_parse(fm_text)
        return fm, body, ('lenient' if fm else 'failed')


def extract_wikilinks(body):
    """Returns list of (target, link_text)."""
    out = []
    for m in WIKILINK_PATTERN.finditer(body):
        target = m.group(1).strip()
        text = (m.group(2) or '').strip()
        out.append((target, text))
    return out


def index_file(path, vault_root, conn, now):
    try:
        content = path.read_text(encoding='utf-8', errors='replace')
    except OSError as e:
        return None, f"read_error: {e}"

    fm, body, parse_method = extract_frontmatter(content)
    rel = path.relative_to(vault_root).as_posix()

    # Area extraction
    area = ''
    parts = rel.split('/')
    if rel.startswith('02_Areas/') and len(parts) >= 2:
        area = parts[1]

    # Agent extraction (for logs/agent files)
    agent = ''
    if rel.startswith('00_Prompts/BDOS/agents/'):
        if len(parts) >= 4:
            agent_name = parts[3].replace('.md', '')
            agent = agent_name

    # Tags normalize
    tags = fm.get('tags', [])
    if isinstance(tags, str):
        tags = [tags]
    elif not isinstance(tags, list):
        tags = []

    word_count = len(body.split())
    stat = path.stat()

    def s(v, maxlen=2000):
        if v is None:
            return None
        s = str(v).strip()
        return s[:maxlen] if s else None

    # Phase 4 field extraction
    bdos_index_raw = fm.get('bdos_index', True)
    if isinstance(bdos_index_raw, str):
        bdos_index_raw = bdos_index_raw.lower() not in ('false', 'no', '0')
    bdos_index_val = 1 if bdos_index_raw else 0

    isv = fm.get('index_schema_version')
    if isinstance(isv, str) and isv.isdigit():
        isv = int(isv)
    elif not isinstance(isv, int):
        isv = None

    # Derive health_state per FRONTMATTER_SCHEMA.md §2 (refined v0.8.1)
    health = 'ok'
    if '04_Archive' in rel or '_archive' in rel:
        health = 'archived'
    elif bdos_index_val == 0:
        health = 'excluded'
    elif not fm:
        # No frontmatter present — distinguish parse failure from absence
        if parse_method == 'failed':
            health = 'broken_frontmatter'
        else:
            health = 'no_frontmatter'   # NEW v0.8.1 — not all files need frontmatter
    elif not fm.get('description') and rel.startswith('00_Prompts/BDOS/'):
        health = 'missing_required_fields'
    elif fm.get('index_schema_version') is None and fm.get('id') is None:
        health = 'needs_reindex'   # has frontmatter but missing Phase 4 fields

    record = {
        'path': rel,
        # Tier 0
        'title': s(fm.get('title') or fm.get('name'), 500),
        'description': s(fm.get('description'), 2000),
        'date': s(fm.get('date'), 50),
        'status': s(fm.get('status'), 50),
        # Tier 1 (Phase 4)
        'id': s(fm.get('id'), 40),
        'index_schema_version': isv,
        'bdos_index': bdos_index_val,
        # Tier 2
        'schema_field': s(fm.get('schema'), 200),
        'version': s(fm.get('version'), 50),
        'category': s(fm.get('category'), 100),
        'subcategory': s(fm.get('subcategory'), 100),
        'tags': json.dumps(tags) if tags else None,
        'area': area or None,
        'agent': agent or None,
        'source_chat_title': s(fm.get('source_chat_title'), 200),
        # Tier 3 (Librarian-managed)
        'health_state': health,
        'indexed_at': now,
        # Filesystem
        'mtime': stat.st_mtime,
        'size_bytes': stat.st_size,
        'has_frontmatter': 1 if fm else 0,
        'body_word_count': word_count,
    }

    conn.execute('''
        INSERT OR REPLACE INTO notes (
            path, title, description, date, status,
            id, index_schema_version, bdos_index,
            schema_field, version, category, subcategory, tags, area, agent, source_chat_title,
            health_state, indexed_at, mtime, size_bytes, has_frontmatter, body_word_count
        ) VALUES (
            :path, :title, :description, :date, :status,
            :id, :index_schema_version, :bdos_index,
            :schema_field, :version, :category, :subcategory, :tags, :area, :agent, :source_chat_title,
            :health_state, :indexed_at, :mtime, :size_bytes, :has_frontmatter, :body_word_count
        )
    ''', record)

    conn.execute('DELETE FROM notes_fts WHERE path = ?', (rel,))
    conn.execute('''
        INSERT INTO notes_fts (path, title, description, category, tags)
        VALUES (?, ?, ?, ?, ?)
    ''', (rel, record['title'] or '', record['description'] or '',
          record['category'] or '', record['tags'] or ''))

    conn.execute('DELETE FROM backlinks WHERE source_path = ?', (rel,))
    for target, text in extract_wikilinks(body):
        conn.execute('''
            INSERT INTO backlinks (source_path, target, link_text)
            VALUES (?, ?, ?)
        ''', (rel, target, text or None))

    return record, None


def walk_vault(vault_root):
    for root, dirs, files in os.walk(vault_root):
        # Prune excluded dirs in-place
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS and not d.startswith('.smart-env')]
        for fname in files:
            if fname.endswith('.md'):
                yield Path(root) / fname


def main():
    if not SCHEMA_PATH.exists():
        print(f"ERROR: schema.sql not found at {SCHEMA_PATH}", file=sys.stderr)
        sys.exit(1)

    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    
    # Fresh rebuild — delete old db if present
    if DB_PATH.exists():
        DB_PATH.unlink()

    conn = sqlite3.connect(DB_PATH)
    conn.executescript(SCHEMA_PATH.read_text())
    
    now = time.time()
    total = 0
    errors = []
    start = time.time()

    # Resolve backlinks after all notes inserted
    for path in walk_vault(VAULT_ROOT):
        record, err = index_file(path, VAULT_ROOT, conn, now)
        if err:
            errors.append((str(path), err))
        else:
            total += 1
        if total % 500 == 0 and total > 0:
            elapsed = time.time() - start
            print(f"  ...indexed {total} files in {elapsed:.1f}s", flush=True)
            conn.commit()

    conn.commit()

    # Resolve backlinks: 2-pass
    # Pass 1: exact path-ends-with match
    conn.execute('''
        UPDATE backlinks SET resolved_path = (
            SELECT path FROM notes WHERE notes.path LIKE '%' || backlinks.target || '.md'
            ORDER BY length(notes.path) ASC LIMIT 1
        )
        WHERE resolved_path IS NULL
    ''')
    # Pass 2: basename-only match (for slug-only wikilinks)
    # Target = "cognition-replaces-middle-management" should match
    # any file whose basename matches: */cognition-replaces-middle-management.md
    conn.execute('''
        UPDATE backlinks SET resolved_path = (
            SELECT path FROM notes
            WHERE notes.path LIKE '%/' || backlinks.target || '.md'
               OR notes.path = backlinks.target || '.md'
            ORDER BY length(notes.path) ASC LIMIT 1
        )
        WHERE resolved_path IS NULL
          AND backlinks.target NOT LIKE '%/%'
    ''')
    conn.commit()

    elapsed = time.time() - start

    # Build meta
    conn.execute('INSERT OR REPLACE INTO build_meta (key, value) VALUES (?, ?)',
                 ('last_build_at', str(now)))
    conn.execute('INSERT OR REPLACE INTO build_meta (key, value) VALUES (?, ?)',
                 ('total_notes', str(total)))
    conn.execute('INSERT OR REPLACE INTO build_meta (key, value) VALUES (?, ?)',
                 ('build_duration_sec', f"{elapsed:.2f}"))
    conn.commit()

    # Stats
    stats = {
        'total_notes': total,
        'errors': len(errors),
        'duration_sec': round(elapsed, 2),
        'with_frontmatter': conn.execute('SELECT COUNT(*) FROM notes WHERE has_frontmatter=1').fetchone()[0],
        'with_description': conn.execute('SELECT COUNT(*) FROM notes WHERE description IS NOT NULL').fetchone()[0],
        'with_category': conn.execute('SELECT COUNT(*) FROM notes WHERE category IS NOT NULL').fetchone()[0],
        'with_status': conn.execute('SELECT COUNT(*) FROM notes WHERE status IS NOT NULL').fetchone()[0],
        'total_backlinks': conn.execute('SELECT COUNT(*) FROM backlinks').fetchone()[0],
        'resolved_backlinks': conn.execute('SELECT COUNT(*) FROM backlinks WHERE resolved_path IS NOT NULL').fetchone()[0],
        'unique_areas': conn.execute('SELECT COUNT(DISTINCT area) FROM notes WHERE area IS NOT NULL').fetchone()[0],
        'unique_categories': conn.execute('SELECT COUNT(DISTINCT category) FROM notes WHERE category IS NOT NULL').fetchone()[0],
    }

    print()
    print("=" * 60)
    print("VAULT INDEX BUILD COMPLETE")
    print("=" * 60)
    for k, v in stats.items():
        print(f"  {k:25s} : {v}")
    print()
    print(f"  Database: {DB_PATH}")
    print(f"  DB size:  {DB_PATH.stat().st_size / 1024:.1f} KB")
    if errors:
        print()
        print(f"  First 5 errors:")
        for p, e in errors[:5]:
            print(f"    {p}: {e}")

    conn.close()


if __name__ == '__main__':
    main()
