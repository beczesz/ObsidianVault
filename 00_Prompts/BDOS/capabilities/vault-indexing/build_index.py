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
import hashlib
from pathlib import Path

# PyYAML is preferred for full-fidelity frontmatter parsing, but it must NOT be a
# hard dependency: the watcher can be launched by whichever python3 is first on
# PATH (homebrew/system), and a missing module would crash it silently. When yaml
# is absent we fall back to the lenient line parser below (stdlib only). Full
# rebuilds (run with a yaml-equipped python) restore full fidelity.
try:
    import yaml
except ImportError:
    yaml = None

# Vault root = 3 levels up from this script
SCRIPT_DIR = Path(__file__).resolve().parent
VAULT_ROOT = SCRIPT_DIR.parent.parent.parent.parent  # capabilities → BDOS → 00_Prompts → vault root
sys.path.insert(0, str(SCRIPT_DIR))
from runtime import DB_PATH  # per-machine local index (re-exported for watch*.py importers)
# Coverage policy is the single source of truth for what the index covers and
# how deep. EXCLUDE_DIRS is re-exported here because watch.py imports it from
# build_index (kept for back-compat with existing importers).
from policy import (
    EXCLUDE_DIRS, KNOWLEDGE_EXT, FULLTEXT_EXT, METADATA_EXT, ext_of, classify,
)
SCHEMA_PATH = SCRIPT_DIR / "schema.sql"

FRONTMATTER_PATTERN = re.compile(r'^---\s*\n(.*?)\n---\s*\n', re.DOTALL)
WIKILINK_PATTERN = re.compile(r'\[\[([^\]|\n]+)(?:\|([^\]\n]+))?\]\]')
SIMPLE_KEY_VAL = re.compile(r'^([a-zA-Z_][a-zA-Z0-9_-]*): *(.*?)\s*$')
SEP_PATTERN = re.compile(r'[_\-]+')


def humanize_filename(path):
    """Synthesize a readable title from a filename for files without frontmatter
    (transcripts, documents). 'EP03_benedek-dezso.srt' -> 'EP03 benedek dezso'."""
    return SEP_PATTERN.sub(' ', path.stem).strip()


def clean_transcript(content, ext):
    """Strip SRT/VTT timestamps and sequence numbers so the FTS body lane holds
    only spoken text, not '00:01:23,456 --> 00:01:25,789' noise."""
    if ext not in ('.srt', '.vtt'):
        return content
    out = []
    for line in content.splitlines():
        s = line.strip()
        if not s:
            continue
        if s.isdigit():            # SRT sequence number
            continue
        if '-->' in s:             # timestamp cue line
            continue
        if s.startswith('WEBVTT'): # VTT header
            continue
        out.append(s)
    return '\n'.join(out)


def body_sha(body):
    """Stable short hash of a note body. MUST match backfill_descriptions.body_sha."""
    return hashlib.sha256((body or '').strip().encode('utf-8')).hexdigest()[:16]


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
    if yaml is None:
        # No PyYAML on this interpreter: lenient stdlib parse (top-level keys).
        fm = lenient_yaml_parse(fm_text)
        return fm, body, ('lenient' if fm else 'failed')
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


_NOTE_COLUMNS = [
    'path', 'title', 'description', 'date', 'status',
    'id', 'index_schema_version', 'bdos_index',
    'schema_field', 'version', 'category', 'subcategory', 'tags', 'area', 'agent', 'source_chat_title',
    'health_state', 'indexed_at', 'mtime', 'size_bytes', 'has_frontmatter', 'body_word_count',
    'ext', 'content_class',
    'description_source', 'description_hash', 'body_hash',
]


def _base_record(rel, now, stat, ext, cls):
    """A note record with every column defaulted, so each ingestion branch only
    sets what it knows."""
    return {
        'path': rel,
        'title': None, 'description': None, 'date': None, 'status': None,
        'id': None, 'index_schema_version': None, 'bdos_index': 1,
        'schema_field': None, 'version': None, 'category': None, 'subcategory': None,
        'tags': None, 'area': None, 'agent': None, 'source_chat_title': None,
        'health_state': 'ok', 'indexed_at': now,
        'mtime': stat.st_mtime, 'size_bytes': stat.st_size,
        'has_frontmatter': 0, 'body_word_count': 0,
        'ext': ext, 'content_class': cls,
        'description_source': None, 'description_hash': None, 'body_hash': None,
    }


def _write_note(conn, record, body, title):
    """INSERT OR REPLACE the note row + refresh its FTS row."""
    cols = ', '.join(_NOTE_COLUMNS)
    placeholders = ', '.join(':' + c for c in _NOTE_COLUMNS)
    conn.execute(f'INSERT OR REPLACE INTO notes ({cols}) VALUES ({placeholders})', record)
    conn.execute('DELETE FROM notes_fts WHERE path = ?', (record['path'],))
    conn.execute(
        'INSERT INTO notes_fts (path, title, description, category, tags, body) VALUES (?, ?, ?, ?, ?, ?)',
        (record['path'], title or '', record.get('description') or '',
         record.get('category') or '', record.get('tags') or '', body or ''))


def _trunc(v, maxlen=2000):
    if v is None:
        return None
    v = str(v).strip()
    return v[:maxlen] if v else None


def index_file(path, vault_root, conn, now):
    """Index one knowledge file. Branches by content class:
      - metadata (pdf/docx/xlsx/...) : discoverable stub, title from filename, no body
      - fulltext markdown            : full frontmatter + body + wikilinks (unchanged)
      - fulltext transcript/txt      : whole (cleaned) body into FTS, title from filename
    """
    rel = path.relative_to(vault_root).as_posix()
    ext = ext_of(path.name)
    cls = classify(ext)

    try:
        stat = path.stat()
    except OSError as e:
        return None, f"stat_error: {e}"

    parts = rel.split('/')
    area = parts[1] if rel.startswith('02_Areas/') and len(parts) >= 2 else ''
    agent = ''
    if rel.startswith('00_Prompts/BDOS/agents/') and len(parts) >= 4:
        agent = parts[3].replace('.md', '')

    # --- Metadata class: discoverable stub, no body read (pdf/docx/xlsx/...) ---
    if cls == 'metadata':
        record = _base_record(rel, now, stat, ext, cls)
        record['title'] = _trunc(humanize_filename(path), 500)
        record['area'] = area or None
        _write_note(conn, record, body='', title=record['title'])
        conn.execute('DELETE FROM backlinks WHERE source_path = ?', (rel,))
        return record, None

    # --- Fulltext class: markdown (frontmatter) or transcript/txt (whole body) ---
    try:
        content = path.read_text(encoding='utf-8', errors='replace')
    except OSError as e:
        return None, f"read_error: {e}"

    if ext == '.md':
        fm, body, parse_method = extract_frontmatter(content)
    else:
        fm, body, parse_method = {}, clean_transcript(content, ext), 'none'

    tags = fm.get('tags', [])
    if isinstance(tags, str):
        tags = [tags]
    elif not isinstance(tags, list):
        tags = []

    bdos_index_raw = fm.get('bdos_index', True)
    if isinstance(bdos_index_raw, str):
        bdos_index_raw = bdos_index_raw.lower() not in ('false', 'no', '0')
    bdos_index_val = 1 if bdos_index_raw else 0

    isv = fm.get('index_schema_version')
    if isinstance(isv, str) and isv.isdigit():
        isv = int(isv)
    elif not isinstance(isv, int):
        isv = None

    # Derive health_state per FRONTMATTER_SCHEMA.md §2 (refined v0.8.1).
    health = 'ok'
    if '04_Archive' in rel or '_archive' in rel:
        health = 'archived'
    elif bdos_index_val == 0:
        health = 'excluded'
    elif ext != '.md':
        health = 'ok'   # transcript/txt: frontmatter not expected, fully indexed
    elif not fm:
        health = 'broken_frontmatter' if parse_method == 'failed' else 'no_frontmatter'
    elif not fm.get('description') and rel.startswith('00_Prompts/BDOS/'):
        health = 'missing_required_fields'
    elif fm.get('index_schema_version') is None and fm.get('id') is None:
        health = 'needs_reindex'

    # Markdown keeps its frontmatter title; non-md synthesizes one from filename.
    title = _trunc(fm.get('title') or fm.get('name'), 500)
    if not title and ext != '.md':
        title = _trunc(humanize_filename(path), 500)

    record = _base_record(rel, now, stat, ext, cls)
    record.update({
        'title': title,
        'description': _trunc(fm.get('description'), 2000),
        'date': _trunc(fm.get('date'), 50),
        'status': _trunc(fm.get('status'), 50),
        'id': _trunc(fm.get('id'), 40),
        'index_schema_version': isv,
        'bdos_index': bdos_index_val,
        'schema_field': _trunc(fm.get('schema'), 200),
        'version': _trunc(fm.get('version'), 50),
        'category': _trunc(fm.get('category'), 100),
        'subcategory': _trunc(fm.get('subcategory'), 100),
        'tags': json.dumps(tags) if tags else None,
        'area': area or None,
        'agent': agent or None,
        'source_chat_title': _trunc(fm.get('source_chat_title'), 200),
        'health_state': health,
        'has_frontmatter': 1 if fm else 0,
        'body_word_count': len(body.split()),
        'description_source': _trunc(fm.get('description_source'), 20),
        'description_hash': _trunc(fm.get('description_hash'), 40),
        'body_hash': body_sha(body),
    })
    _write_note(conn, record, body=body, title=title)

    conn.execute('DELETE FROM backlinks WHERE source_path = ?', (rel,))
    for target, text in extract_wikilinks(body):
        conn.execute(
            'INSERT INTO backlinks (source_path, target, link_text) VALUES (?, ?, ?)',
            (rel, target, text or None))

    return record, None


def walk_vault(vault_root):
    for root, dirs, files in os.walk(vault_root):
        # Prune excluded dirs in-place
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS and not d.startswith('.smart-env')]
        for fname in files:
            if ext_of(fname) in KNOWLEDGE_EXT:
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
        'fulltext_files': conn.execute("SELECT COUNT(*) FROM notes WHERE content_class='fulltext'").fetchone()[0],
        'metadata_stubs': conn.execute("SELECT COUNT(*) FROM notes WHERE content_class='metadata'").fetchone()[0],
        'transcripts_srt': conn.execute("SELECT COUNT(*) FROM notes WHERE ext='.srt'").fetchone()[0],
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
