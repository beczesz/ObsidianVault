#!/usr/bin/env python3
"""BDOS Vault Indexing — Integrity Audit (Phase 4.B).

Scans the index, produces a structured integrity report:
- health-state distribution
- duplicate IDs
- orphan files (no backlinks in either direction)
- missing required fields (BDOS files without description)
- broken-frontmatter files
- schema version mismatch
- stale entries (DB mtime older than file mtime)

Usage:
    python3 audit.py                  # human readable
    python3 audit.py --json           # machine readable
    python3 audit.py --health stale   # filter by health state
"""

import argparse
import json
import sqlite3
import time
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
from runtime import db_read_path
VAULT_ROOT = SCRIPT_DIR.parent.parent.parent.parent


def get_conn():
    DB_PATH = db_read_path()
    if not DB_PATH.exists():
        raise FileNotFoundError(f"No index — run: python3 {SCRIPT_DIR}/build_index.py")
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def health_distribution(conn):
    rows = conn.execute("SELECT health_state, COUNT(*) as n FROM notes GROUP BY health_state ORDER BY n DESC").fetchall()
    return [{"state": r[0], "count": r[1]} for r in rows]


def duplicate_ids(conn):
    rows = conn.execute("""
        SELECT id, GROUP_CONCAT(path, '|') as paths, COUNT(*) as n
        FROM notes
        WHERE id IS NOT NULL
        GROUP BY id HAVING n > 1
    """).fetchall()
    return [{"id": r[0], "paths": r[1].split("|"), "count": r[2]} for r in rows]


def orphans(conn, limit=50):
    rows = conn.execute("""
        SELECT path FROM notes
        WHERE bdos_index = 1
        AND path NOT IN (SELECT DISTINCT resolved_path FROM backlinks WHERE resolved_path IS NOT NULL)
        AND path NOT IN (SELECT DISTINCT source_path FROM backlinks WHERE source_path IS NOT NULL)
        AND has_frontmatter = 1
        ORDER BY mtime DESC LIMIT ?
    """, (limit,)).fetchall()
    return [r[0] for r in rows]


def missing_required_fields(conn, limit=100):
    rows = conn.execute("""
        SELECT path FROM notes WHERE health_state = 'missing_required_fields' LIMIT ?
    """, (limit,)).fetchall()
    return [r[0] for r in rows]


def needs_reindex(conn, limit=100):
    rows = conn.execute("""
        SELECT path FROM notes WHERE health_state = 'needs_reindex' LIMIT ?
    """, (limit,)).fetchall()
    return [r[0] for r in rows]


def stale_entries(conn, limit=50):
    """Files where file mtime > indexed_at."""
    rows = conn.execute("""
        SELECT path, mtime, indexed_at FROM notes
        WHERE mtime > indexed_at + 1.0
        ORDER BY mtime DESC LIMIT ?
    """, (limit,)).fetchall()
    return [{"path": r[0], "mtime": r[1], "indexed_at": r[2], "lag_sec": round(r[1]-r[2], 1)} for r in rows]


def broken_frontmatter(conn, limit=50):
    rows = conn.execute("""
        SELECT path FROM notes WHERE health_state = 'broken_frontmatter' LIMIT ?
    """, (limit,)).fetchall()
    return [r[0] for r in rows]


def full_audit(conn):
    """Return complete audit report."""
    n_total = conn.execute("SELECT COUNT(*) FROM notes").fetchone()[0]
    n_with_id = conn.execute("SELECT COUNT(*) FROM notes WHERE id IS NOT NULL").fetchone()[0]
    n_with_fm = conn.execute("SELECT COUNT(*) FROM notes WHERE has_frontmatter=1").fetchone()[0]
    n_with_desc = conn.execute("SELECT COUNT(*) FROM notes WHERE description IS NOT NULL").fetchone()[0]
    n_backlinks = conn.execute("SELECT COUNT(*) FROM backlinks").fetchone()[0]
    n_resolved = conn.execute("SELECT COUNT(*) FROM backlinks WHERE resolved_path IS NOT NULL").fetchone()[0]

    return {
        "totals": {
            "files_indexed": n_total,
            "files_with_id": n_with_id,
            "files_with_frontmatter": n_with_fm,
            "files_with_description": n_with_desc,
            "backlinks_total": n_backlinks,
            "backlinks_resolved": n_resolved,
        },
        "health_distribution": health_distribution(conn),
        "duplicate_ids": duplicate_ids(conn),
        "orphans_sample": orphans(conn, limit=20),
        "missing_required_fields_sample": missing_required_fields(conn, limit=20),
        "needs_reindex_sample": needs_reindex(conn, limit=20),
        "stale_entries_sample": stale_entries(conn, limit=20),
        "broken_frontmatter_sample": broken_frontmatter(conn, limit=20),
        "audit_ts": time.time(),
    }


def print_audit(report):
    print("=== BDOS Vault Audit Report ===\n")
    print("Totals:")
    for k, v in report["totals"].items():
        print(f"  {k:30s} : {v}")
    print("\nHealth distribution:")
    for h in report["health_distribution"]:
        print(f"  {h['state']:30s} : {h['count']}")
    print(f"\nDuplicate IDs: {len(report['duplicate_ids'])}")
    for d in report["duplicate_ids"][:5]:
        print(f"  {d['id']} → {d['count']} files")
    print(f"\nOrphans (sample, top 5):")
    for o in report["orphans_sample"][:5]:
        print(f"  {o}")
    print(f"\nMissing required fields (sample, top 5):")
    for m in report["missing_required_fields_sample"][:5]:
        print(f"  {m}")
    print(f"\nNeeds reindex (sample, top 5):")
    for n in report["needs_reindex_sample"][:5]:
        print(f"  {n}")
    print(f"\nStale entries (sample, top 5):")
    for s in report["stale_entries_sample"][:5]:
        print(f"  {s['path']} (lag {s['lag_sec']}s)")
    print(f"\nBroken frontmatter (sample, top 5):")
    for b in report["broken_frontmatter_sample"][:5]:
        print(f"  {b}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--health", help="Filter by health state")
    args = ap.parse_args()

    conn = get_conn()
    report = full_audit(conn)

    if args.health:
        rows = conn.execute("SELECT path FROM notes WHERE health_state = ?", (args.health,)).fetchall()
        if args.json:
            print(json.dumps([r[0] for r in rows], indent=2))
        else:
            print(f"Files with health = {args.health}: {len(rows)}")
            for r in rows[:50]:
                print(f"  {r[0]}")
        return

    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print_audit(report)


if __name__ == "__main__":
    main()
