#!/usr/bin/env python3
"""BDOS Vault Indexing — query CLI + Python API.

Quick metadata queries against the SQLite read-cache. Token-efficient
alternative to full-text vault scans.

Usage:
    python3 query.py --category philosophy --status maturing
    python3 query.py --area Sonrisa --tag ai-ops
    python3 query.py --agent sage --schema sage.thought.v1
    python3 query.py --orphans
    python3 query.py --fts "middle management"
    python3 query.py --stats
"""

import argparse
import sqlite3
import json
import sys
import unicodedata
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
from runtime import db_read_path


def _norm_forms(value):
    """Both Unicode normalization forms of a string, deduped. The index stores
    path-derived fields (area, agent) in the filesystem's form (NFD on macOS),
    but a typed or pasted query is usually NFC, so an exact match on an accented
    Area name like 'Navigator' would silently miss. Matching both forms fixes it
    without a rebuild or any change to how paths are stored."""
    nfc = unicodedata.normalize("NFC", value)
    nfd = unicodedata.normalize("NFD", value)
    return [nfc] if nfc == nfd else [nfc, nfd]


def get_conn():
    DB_PATH = db_read_path()
    if not DB_PATH.exists():
        raise FileNotFoundError(f"Index not built. Run: python3 {SCRIPT_DIR}/build_index.py")
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def query_notes(category=None, status=None, area=None, agent=None, schema=None, tag=None,
                content_class=None, ext=None, limit=50):
    """Python API — return matching notes."""
    conn = get_conn()
    where, params = [], []
    if category:
        where.append("category = ?"); params.append(category)
    if status:
        where.append("status = ?"); params.append(status)
    if area:
        forms = _norm_forms(area)
        where.append("area IN (%s)" % ",".join("?" * len(forms))); params.extend(forms)
    if agent:
        forms = _norm_forms(agent)
        where.append("agent IN (%s)" % ",".join("?" * len(forms))); params.extend(forms)
    if schema:
        where.append("schema_field = ?"); params.append(schema)
    if tag:
        where.append("tags LIKE ?"); params.append(f'%"{tag}"%')
    if content_class:
        where.append("content_class = ?"); params.append(content_class)
    if ext:
        where.append("ext = ?"); params.append(ext if ext.startswith('.') else '.' + ext)

    sql = "SELECT * FROM notes"
    if where:
        sql += " WHERE " + " AND ".join(where)
    sql += " ORDER BY mtime DESC LIMIT ?"
    params.append(limit)
    return [dict(r) for r in conn.execute(sql, params).fetchall()]


def fts_search(query, limit=20):
    conn = get_conn()
    # Weighted bm25 over (path, title, description, category, tags, body).
    # UNINDEXED columns (path, category) take weight 0. Title + description are the
    # high-signal lanes; body is a low-weight fallback so a note with no description
    # is still findable via its content without drowning the metadata lanes.
    rows = conn.execute(
        "SELECT path, title, description, category, "
        "bm25(notes_fts, 0.0, 10.0, 8.0, 0.0, 4.0, 1.0) AS rank "
        "FROM notes_fts WHERE notes_fts MATCH ? "
        "ORDER BY rank LIMIT ?",
        (query, limit)
    ).fetchall()
    return [dict(r) for r in rows]


def find_orphans(limit=50):
    conn = get_conn()
    rows = conn.execute('''
        SELECT path, title FROM notes
        WHERE path NOT IN (SELECT DISTINCT resolved_path FROM backlinks WHERE resolved_path IS NOT NULL)
        AND path NOT IN (SELECT DISTINCT source_path FROM backlinks)
        ORDER BY mtime DESC LIMIT ?
    ''', (limit,)).fetchall()
    return [dict(r) for r in rows]


def get_backlinks(target_path):
    """Find backlinks. target_path can be a slug, basename, or full path."""
    conn = get_conn()
    stem = Path(target_path).stem
    rows = conn.execute("""
        SELECT source_path, target, link_text, resolved_path FROM backlinks
        WHERE resolved_path = ?
           OR resolved_path LIKE ?
           OR target = ?
           OR target LIKE ?
           OR target LIKE ?
    """, (
        target_path,
        f'%/{target_path}.md',
        stem,
        f'%/{stem}',
        f'%{stem}'
    )).fetchall()
    return [dict(r) for r in rows]


def stats():
    conn = get_conn()
    out = {}
    out['total_notes'] = conn.execute("SELECT COUNT(*) FROM notes").fetchone()[0]
    out['with_frontmatter'] = conn.execute("SELECT COUNT(*) FROM notes WHERE has_frontmatter=1").fetchone()[0]
    out['with_description'] = conn.execute("SELECT COUNT(*) FROM notes WHERE description IS NOT NULL").fetchone()[0]
    out['with_category'] = conn.execute("SELECT COUNT(*) FROM notes WHERE category IS NOT NULL").fetchone()[0]
    out['total_backlinks'] = conn.execute("SELECT COUNT(*) FROM backlinks").fetchone()[0]
    out['resolved_backlinks'] = conn.execute("SELECT COUNT(*) FROM backlinks WHERE resolved_path IS NOT NULL").fetchone()[0]
    out['unique_categories'] = conn.execute("SELECT COUNT(DISTINCT category) FROM notes WHERE category IS NOT NULL").fetchone()[0]
    out['unique_areas'] = conn.execute("SELECT COUNT(DISTINCT area) FROM notes WHERE area IS NOT NULL").fetchone()[0]
    out['unique_agents'] = conn.execute("SELECT COUNT(DISTINCT agent) FROM notes WHERE agent IS NOT NULL").fetchone()[0]
    out['top_areas'] = [dict(r) for r in conn.execute("SELECT area, COUNT(*) as n FROM notes WHERE area IS NOT NULL GROUP BY area ORDER BY n DESC LIMIT 10").fetchall()]
    out['top_categories'] = [dict(r) for r in conn.execute("SELECT category, COUNT(*) as n FROM notes WHERE category IS NOT NULL GROUP BY category ORDER BY n DESC LIMIT 10").fetchall()]
    out['top_agents'] = [dict(r) for r in conn.execute("SELECT agent, COUNT(*) as n FROM notes WHERE agent IS NOT NULL GROUP BY agent ORDER BY n DESC LIMIT 10").fetchall()]
    return out


def print_results(results, format='table'):
    if not results:
        print("(no results)")
        return
    if format == 'json':
        print(json.dumps(results, indent=2, ensure_ascii=False))
        return
    print(f"  {len(results)} results:\n")
    for r in results:
        p = r.get('path', '')
        t = r.get('title') or '(no title)'
        d = r.get('description') or ''
        if len(d) > 100:
            d = d[:97] + '...'
        cat = r.get('category') or ''
        print(f"  • {p}")
        print(f"    {t}" + (f"  [{cat}]" if cat else ''))
        if d:
            print(f"    {d}")
        print()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--category')
    ap.add_argument('--status')
    ap.add_argument('--area')
    ap.add_argument('--agent')
    ap.add_argument('--schema')
    ap.add_argument('--tag')
    ap.add_argument('--content-class', dest='content_class',
                    help='Filter by content class: fulltext | metadata')
    ap.add_argument('--ext', help='Filter by extension, e.g. .srt or .pdf')
    ap.add_argument('--fts', help='FTS5 search on title+description+body')
    ap.add_argument('--orphans', action='store_true')
    ap.add_argument('--backlinks', help='Find files linking to this path/slug')
    ap.add_argument('--stats', action='store_true')
    ap.add_argument('--limit', type=int, default=20)
    ap.add_argument('--json', action='store_true')
    args = ap.parse_args()

    fmt = 'json' if args.json else 'table'

    if args.stats:
        print(json.dumps(stats(), indent=2, ensure_ascii=False))
        return
    if args.orphans:
        print_results(find_orphans(args.limit), fmt); return
    if args.backlinks:
        print_results(get_backlinks(args.backlinks), fmt); return
    if args.fts:
        print_results(fts_search(args.fts, args.limit), fmt); return

    results = query_notes(
        category=args.category, status=args.status, area=args.area,
        agent=args.agent, schema=args.schema, tag=args.tag,
        content_class=args.content_class, ext=args.ext, limit=args.limit
    )
    print_results(results, fmt)


if __name__ == '__main__':
    main()
