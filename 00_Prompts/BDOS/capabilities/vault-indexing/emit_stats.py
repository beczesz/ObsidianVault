#!/usr/bin/env python3
"""BDOS Vault Indexing — Vault Stats Sidecar Generator.

Reads vault.db and writes _dashboards/_design/vault_stats.json with:
  - total_md_files, indexed_count, coverage_pct
  - tier2_units: Areas under 02_Areas/ that have a 00_INDEX.md (scoped index)
  - health_breakdown, top_areas, top_categories

Usage:
    python3 emit_stats.py                  # write to _dashboards/_design/vault_stats.json
    python3 emit_stats.py --dry-run        # print JSON to stdout, don't write file
    python3 emit_stats.py --out /path/to/custom.json
"""

import argparse
import json
import os
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
# vault-indexing -> capabilities -> BDOS -> 00_Prompts -> vault root
VAULT_ROOT = SCRIPT_DIR.parent.parent.parent.parent
sys.path.insert(0, str(SCRIPT_DIR))
from runtime import db_read_path

DEFAULT_OUT = VAULT_ROOT / '_dashboards' / '_design' / 'vault_stats.json'
FRESHNESS_DAYS = 30


def get_conn():
    db = db_read_path()
    if not db.exists():
        raise FileNotFoundError(f"Index not built. Run: python3 {SCRIPT_DIR}/build_index.py")
    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row
    return conn


def detect_tier2_units():
    """Detect Areas under 02_Areas/ that have a scoped index set.

    A unit qualifies if it has at least one of the 5 standard scoped index files
    (00_KNOWLEDGE_MAP.md, 00_INDEX.md, 00_DECISIONS_INDEX.md, 00_OPEN_QUESTIONS.md,
    00_GAPS.md). The presence of 00_KNOWLEDGE_MAP.md is the primary indicator
    (deployed areas have this even if 00_INDEX.md is at vault root).

    'fresh' = most recent index file mtime within FRESHNESS_DAYS days.
    'has_5_index' = all 5 index files present.
    """
    areas_root = VAULT_ROOT / '02_Areas'
    if not areas_root.exists():
        return []

    five_index_names = [
        '00_INDEX.md', '00_KNOWLEDGE_MAP.md', '00_DECISIONS_INDEX.md',
        '00_OPEN_QUESTIONS.md', '00_GAPS.md'
    ]
    now = datetime.now(timezone.utc)
    units = []

    for area_dir in sorted(areas_root.iterdir()):
        if not area_dir.is_dir():
            continue
        # Check for any scoped index files
        found_indexes = {}
        for idx_name in five_index_names:
            idx_path = area_dir / idx_name
            if idx_path.exists():
                found_indexes[idx_name] = idx_path

        # Must have at least one index file to qualify as tier-2
        if not found_indexes:
            continue

        # Freshness based on the most recently modified index file
        newest_mtime = max(p.stat().st_mtime for p in found_indexes.values())
        mtime_dt = datetime.fromtimestamp(newest_mtime, tz=timezone.utc)
        age_days = (now - mtime_dt).days
        fresh = age_days < FRESHNESS_DAYS

        units.append({
            'name': area_dir.name,
            'has_5_index': len(found_indexes) >= 5,
            'index_count': len(found_indexes),
            'index_files': list(found_indexes.keys()),
            'last_index_mtime': mtime_dt.strftime('%Y-%m-%dT%H:%M:%SZ'),
            'age_days': age_days,
            'fresh': fresh,
        })

    return units


def build_stats():
    conn = get_conn()

    total_md_files = conn.execute("SELECT COUNT(*) FROM notes").fetchone()[0]
    with_frontmatter = conn.execute("SELECT COUNT(*) FROM notes WHERE has_frontmatter=1").fetchone()[0]
    with_description = conn.execute("SELECT COUNT(*) FROM notes WHERE description IS NOT NULL AND description != ''").fetchone()[0]
    with_backlinks = conn.execute("SELECT COUNT(DISTINCT source_path) FROM backlinks").fetchone()[0]

    # Coverage: notes that have frontmatter OR are in the FTS index
    fts_count = conn.execute("SELECT COUNT(*) FROM notes_fts").fetchone()[0]
    indexed_count = fts_count  # notes_fts is our "indexed" surface

    # HONEST coverage (Reach layer, 2026-06-07). The old coverage_pct here was
    # indexed_count / total_md_files where both came from the notes table, so it
    # measured the index against itself and could never report a miss. We now
    # take the real number from reach.py, which compares the index against the
    # filesystem ground truth. Falls back to the old (self-referential) value
    # only if the reach walk fails for any reason.
    reach_block = None
    coverage_pct = round(indexed_count / total_md_files * 100, 1) if total_md_files else 0.0
    try:
        import reach
        rr = reach.build_report()
        reach_block = rr["reach"]
        # coverage_pct now means honest full-text knowledge reach (md+srt+txt+vtt
        # actually present in the index vs on disk), not index-vs-itself.
        coverage_pct = reach_block["fulltext"]["pct"]
    except Exception as exc:
        print(f"[emit_stats] reach unavailable, using self-referential coverage: {exc}",
              file=sys.stderr)

    # Health breakdown (simple heuristic)
    ok_count = with_description
    stale_count = with_frontmatter - with_description  # has frontmatter but no description
    orphaned_count = total_md_files - with_backlinks - ok_count
    broken_frontmatter = total_md_files - with_frontmatter

    top_areas = [
        dict(r) for r in conn.execute(
            "SELECT area, COUNT(*) as count FROM notes WHERE area IS NOT NULL AND area != '' "
            "GROUP BY area ORDER BY count DESC LIMIT 15"
        ).fetchall()
    ]

    top_categories = [
        dict(r) for r in conn.execute(
            "SELECT category, COUNT(*) as count FROM notes WHERE category IS NOT NULL AND category != '' "
            "GROUP BY category ORDER BY count DESC LIMIT 10"
        ).fetchall()
    ]

    tier2_units = detect_tier2_units()
    tier2_active_count = len(tier2_units)
    fresh_count = sum(1 for u in tier2_units if u['fresh'])

    return {
        'generated_at': datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'total_md_files': total_md_files,
        'indexed_count': indexed_count,
        'coverage_pct': coverage_pct,
        'reach': reach_block,   # honest filesystem-vs-index reach (md/fulltext/total); None if reach walk failed
        'with_frontmatter': with_frontmatter,
        'with_description': with_description,
        'tier2_units': tier2_units,
        'tier2_active_count': tier2_active_count,
        'fresh_count': fresh_count,
        'health_breakdown': {
            'ok': ok_count,
            'stale': max(0, stale_count),
            'orphaned': max(0, orphaned_count),
            'broken_frontmatter': max(0, broken_frontmatter),
        },
        'top_areas': top_areas,
        'top_categories': top_categories,
    }


def main():
    ap = argparse.ArgumentParser(description='Emit vault_stats.json sidecar from vault.db')
    ap.add_argument('--dry-run', action='store_true', help='Print JSON to stdout, do not write file')
    ap.add_argument('--out', default=str(DEFAULT_OUT), help='Output path (default: _dashboards/_design/vault_stats.json)')
    args = ap.parse_args()

    stats = build_stats()
    json_str = json.dumps(stats, indent=2, ensure_ascii=False)

    if args.dry_run:
        print(json_str)
        return

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json_str, encoding='utf-8')
    print(f"[emit_stats] wrote {out_path} ({stats['total_md_files']} total, {stats['indexed_count']} indexed, {stats['coverage_pct']}% coverage, {stats['tier2_active_count']} tier-2 units, {stats['fresh_count']} fresh)")


if __name__ == '__main__':
    main()
