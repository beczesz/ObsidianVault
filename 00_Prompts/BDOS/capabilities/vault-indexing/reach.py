#!/usr/bin/env python3
"""BDOS Vault Indexing - Reach Audit (coverage reconciliation).

Answers the trust question: "Did the index actually cover everything it should?"

This is fundamentally different from the two existing health tools:

  - audit.py     inspects the index against ITSELF (health states, orphans,
                 duplicate ids). It cannot see a file that was never indexed.
  - emit_stats.py computes coverage_pct = indexed_count / total_md_files where
                 total_md_files = COUNT(*) FROM notes. Both numbers come from the
                 index, so the metric is self-referential and can never report a
                 miss.

reach.py compares the index against the FILESYSTEM (ground truth) plus an
explicit COVERAGE POLICY (what should be reachable, and how deep). It is built
to be falsifiable: it can and will report failure. That is what makes it a
trust instrument rather than a comfort metric.

Three reach failure modes it surfaces:
  1. FORMAT gap       knowledge files in formats the indexer never walks
                      (.srt, .pdf, .docx, .xlsx) because walk_vault yields .md only
  2. COMPLETENESS gap in-scope .md files on disk that are absent from the index
  3. DRIFT            ghosts (in index, gone from disk), pollution (indexed from a
                      policy-excluded dir), and stale rows (disk newer than index)

Read-only. Never writes the index or any vault file. Writes one report at the
vault root: 00_REACH_REPORT.md (and --json for machine consumption / dashboards).

Usage:
    python3 reach.py                 # write 00_REACH_REPORT.md + print summary
    python3 reach.py --json          # machine-readable to stdout, no file write
    python3 reach.py --quiet         # write report, minimal stdout
    python3 reach.py --out PATH      # custom report path
"""

import argparse
import json
import os
import sqlite3
import sys
import time
import unicodedata
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path


def nfc(s):
    """Normalize to NFC. macOS stores filenames as NFD, Windows/Drive as NFC, so
    the index accumulates a mix of both forms across machines. Comparing raw
    strings would falsely flag accented paths as missing or ghosts. All set
    comparisons in this tool run on NFC-normalized paths; original disk forms are
    kept only for display."""
    return unicodedata.normalize("NFC", s)

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
from runtime import db_read_path

VAULT_ROOT = SCRIPT_DIR.parent.parent.parent.parent

# Coverage policy is shared with the indexer (single source of truth) so the
# reach auditor and the indexer can never silently disagree about what counts.
from policy import EXCLUDE_DIRS, FULLTEXT_EXT, METADATA_EXT, classify, ext_of

ARCHIVE_DIRS = {"04_Archive", "_archive_old"}   # dark on purpose: counted, not a gap
# Descend into archive only to COUNT what is intentionally dark; prune everything
# else the policy excludes (node_modules, .git, ExarSharedBrain, vault metadata).
PRUNE_DIRS = EXCLUDE_DIRS - ARCHIVE_DIRS


def zone_of(rel):
    """Human-readable zone label for grouping (Area name, Resource bucket, etc.)."""
    parts = rel.split("/")
    if rel.startswith("02_Areas/") and len(parts) >= 2:
        return parts[1]
    if rel.startswith("03_Resources/") and len(parts) >= 2:
        return "03_Resources/" + parts[1]
    if rel.startswith("00_Prompts/"):
        return "00_Prompts"
    if rel.startswith("05_DailyNotes/"):
        return "05_DailyNotes"
    if rel.startswith("01_Projects/") and len(parts) >= 2:
        return "01_Projects/" + parts[1]
    return parts[0] if len(parts) > 1 else "(root)"


def policy_walk():
    """Walk the vault once under the coverage policy. Returns list of file dicts
    and a separate count of intentionally-archived knowledge files."""
    files = []
    archived_knowledge = 0
    for root, dirs, fnames in os.walk(VAULT_ROOT):
        # Count archive knowledge before pruning, then prune.
        rootrel = Path(root).relative_to(VAULT_ROOT).as_posix()
        in_archive = any(seg in ARCHIVE_DIRS for seg in rootrel.split("/"))
        dirs[:] = [d for d in dirs if d not in PRUNE_DIRS]
        for fn in fnames:
            if fn == ".DS_Store":
                continue
            ext = ext_of(fn)
            if in_archive:
                if ext in FULLTEXT_EXT or ext in METADATA_EXT:
                    archived_knowledge += 1
                continue
            p = Path(root) / fn
            try:
                rel = p.relative_to(VAULT_ROOT).as_posix()
                st = p.stat()
            except (OSError, ValueError):
                continue
            files.append({
                "rel": rel,
                "ext": ext,
                "cls": classify(ext),
                "zone": zone_of(rel),
                "mtime": st.st_mtime,
                "size": st.st_size,
            })
    return files, archived_knowledge


def pct(num, den):
    return round(num / den * 100, 1) if den else 0.0


def is_polluted(rel):
    """An indexed path that the policy says should never be indexed (a duplicate
    mirror or archive that leaked in)."""
    return bool(set(rel.split("/")) & EXCLUDE_DIRS)


def build_report():
    db = db_read_path()
    if not db.exists():
        raise FileNotFoundError(f"No index. Run: python3 {SCRIPT_DIR}/build_index.py")
    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row

    index_rows = conn.execute("SELECT path, mtime, indexed_at FROM notes").fetchall()
    index_paths = {r["path"] for r in index_rows}
    index_paths_nfc = {nfc(p) for p in index_paths}
    index_indexed_at = {nfc(r["path"]): (r["indexed_at"] or 0) for r in index_rows}

    # Internal health (from the index, for context).
    n_total = len(index_rows)
    n_desc = conn.execute(
        "SELECT COUNT(*) FROM notes WHERE description IS NOT NULL AND description != ''"
    ).fetchone()[0]
    health = {
        r[0]: r[1] for r in conn.execute(
            "SELECT health_state, COUNT(*) FROM notes GROUP BY health_state"
        ).fetchall()
    }
    last_build = conn.execute(
        "SELECT value FROM build_meta WHERE key='last_build_at'"
    ).fetchone()
    last_build = float(last_build[0]) if last_build else None
    conn.close()

    disk_files, archived_knowledge = policy_walk()

    # All comparisons run on NFC-normalized paths; display uses the disk form.
    md_disk = [f for f in disk_files if f["ext"] == ".md"]
    md_disk_nfc = {nfc(f["rel"]) for f in md_disk}
    all_disk_nfc = {nfc(f["rel"]) for f in disk_files}
    ft_nonmd = [f for f in disk_files if f["cls"] == "fulltext" and f["ext"] != ".md"]
    meta_disk = [f for f in disk_files if f["cls"] == "metadata"]

    md_indexed_n = md_disk_nfc & index_paths_nfc
    md_missing = sorted(f["rel"] for f in md_disk if nfc(f["rel"]) not in index_paths_nfc)
    ft_nonmd_indexed = {f["rel"] for f in ft_nonmd if nfc(f["rel"]) in index_paths_nfc}
    meta_indexed = {f["rel"] for f in meta_disk if nfc(f["rel"]) in index_paths_nfc}

    # Drift. A ghost is an index path whose NFC form matches no file on disk
    # (covers deleted files and cross-form duplicates that no longer resolve).
    ghosts = sorted(p for p in index_paths if nfc(p) not in all_disk_nfc and not is_polluted(p))
    pollution = sorted(p for p in index_paths if is_polluted(p))
    stale = []
    for f in md_disk:
        if nfc(f["rel"]) not in index_paths_nfc:
            continue
        im = index_indexed_at.get(nfc(f["rel"]), 0)
        if f["mtime"] > im + 2.0:
            stale.append({"path": f["rel"], "lag_sec": round(f["mtime"] - im, 1)})
    stale.sort(key=lambda x: -x["lag_sec"])

    # Reach tiers.
    md_total = len(md_disk)
    ft_total = md_total + len(ft_nonmd)
    all_total = ft_total + len(meta_disk)
    md_hits = len(md_indexed_n)
    ft_hits = md_hits + len(ft_nonmd_indexed)
    all_hits = ft_hits + len(meta_indexed)

    # Format-gap inventory: non-md knowledge files NOT in the index. With non-md
    # ingestion live this should be ~0; a non-zero value means those formats are
    # not being walked (a real reach gap), so the count must reflect the actual
    # unindexed set, not the total count of non-md files.
    fmt_gap_by_ext = defaultdict(int)
    fmt_gap_by_zone = defaultdict(lambda: defaultdict(int))
    for f in ft_nonmd + meta_disk:
        if nfc(f["rel"]) in index_paths_nfc:
            continue
        fmt_gap_by_ext[f["ext"]] += 1
        fmt_gap_by_zone[f["zone"]][f["ext"]] += 1
    fmt_gap_count = sum(fmt_gap_by_ext.values())

    # Unclassified extensions (policy gaps to grow into).
    unclassified = defaultdict(int)
    for f in disk_files:
        if f["cls"] == "unclassified":
            unclassified[f["ext"] or "(none)"] += 1

    # Per-zone knowledge reach.
    zone_stats = defaultdict(lambda: {"knowledge": 0, "indexed": 0})
    for f in disk_files:
        if f["cls"] in ("fulltext", "metadata"):
            zone_stats[f["zone"]]["knowledge"] += 1
            if nfc(f["rel"]) in index_paths_nfc:
                zone_stats[f["zone"]]["indexed"] += 1

    return {
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "db_path": str(db),
        "last_build_at": last_build,
        "reach": {
            "md_completeness": {"hits": md_hits, "total": md_total, "pct": pct(md_hits, md_total)},
            "fulltext": {"hits": ft_hits, "total": ft_total, "pct": pct(ft_hits, ft_total)},
            "total_knowledge": {"hits": all_hits, "total": all_total, "pct": pct(all_hits, all_total)},
        },
        "index_internal": {
            "notes_rows": n_total,
            "with_description": n_desc,
            "description_pct": pct(n_desc, n_total),
            "health_distribution": health,
        },
        "completeness_gap": {
            "md_missing_count": len(md_missing),
            "md_missing_sample": md_missing[:40],
        },
        "format_gap": {
            "gap_count": fmt_gap_count,                       # non-md knowledge NOT indexed (the real gap)
            "fulltext_nonmd_total": len(ft_nonmd),            # non-md plain-text on disk (now indexed)
            "fulltext_nonmd_indexed": len(ft_nonmd_indexed),
            "metadata_total": len(meta_disk),                 # documents on disk (now stubbed)
            "metadata_indexed": len(meta_indexed),
            "by_ext": dict(sorted(fmt_gap_by_ext.items(), key=lambda x: -x[1])),
            "by_zone": {z: dict(d) for z, d in sorted(
                fmt_gap_by_zone.items(),
                key=lambda x: -sum(x[1].values()))},
        },
        "drift": {
            "ghosts_count": len(ghosts),
            "ghosts_sample": ghosts[:40],
            "pollution_count": len(pollution),
            "pollution_sample": pollution[:20],
            "stale_count": len(stale),
            "stale_sample": stale[:20],
        },
        "archived_knowledge_excluded": archived_knowledge,
        "unclassified_ext": dict(sorted(unclassified.items(), key=lambda x: -x[1])),
        "zone_reach": {z: s for z, s in sorted(
            zone_stats.items(),
            key=lambda x: -(x[1]["knowledge"] - x[1]["indexed"]))},
    }


# ---------------------------------------------------------------------------
# Rendering. No em dashes anywhere in generated output (vault CLAUDE.md s0).
# ---------------------------------------------------------------------------

def _fmt_ts(epoch):
    if not epoch:
        return "unknown"
    return datetime.fromtimestamp(epoch, tz=timezone.utc).strftime("%Y-%m-%d %H:%M UTC")


def render_markdown(r):
    reach = r["reach"]
    md = reach["md_completeness"]
    ft = reach["fulltext"]
    tk = reach["total_knowledge"]
    gen = r["generated_at"]

    lines = []
    lines.append("---")
    lines.append("title: 00_REACH_REPORT")
    lines.append(f"date: {gen[:10]}")
    lines.append("author: reach.py")
    lines.append("status: active")
    lines.append("bdos_index: false")
    lines.append(
        "description: Vault index reach audit. Compares the live SQLite index against "
        "the filesystem ground truth plus an explicit coverage policy. Reports format "
        "gaps (non-md knowledge unindexed), completeness gaps (md on disk absent from "
        "index), and drift (ghosts, pollution, stale). The falsifiable trust metric the "
        "self-referential coverage_pct cannot provide."
    )
    lines.append("---")
    lines.append("")
    lines.append("# Vault Index Reach Report")
    lines.append("")
    lines.append(f"Generated: {gen}")
    lines.append(f"Index DB: `{r['db_path']}`")
    lines.append(f"Last full build: {_fmt_ts(r['last_build_at'])}")
    lines.append("")
    lines.append("> Read-only reconciliation. Nothing in the index or the vault was modified.")
    lines.append("> This measures the index against the filesystem, not against itself.")
    lines.append("")
    lines.append("## Headline reach")
    lines.append("")
    lines.append("| Tier | What it means | Indexed / On disk | Reach |")
    lines.append("|---|---|---|---|")
    lines.append(f"| Markdown completeness | The index's own promise (.md only). Should be ~100%. | {md['hits']} / {md['total']} | **{md['pct']}%** |")
    lines.append(f"| Full-text knowledge | md + srt + txt + vtt (plain-text, cheap to index) | {ft['hits']} / {ft['total']} | **{ft['pct']}%** |")
    lines.append(f"| Total knowledge | the above + pdf/docx/xlsx/pptx/epub | {tk['hits']} / {tk['total']} | **{tk['pct']}%** |")
    lines.append("")

    # Completeness gap.
    cg = r["completeness_gap"]
    lines.append("## 1. Completeness gap (markdown the index should have but does not)")
    lines.append("")
    if cg["md_missing_count"] == 0:
        lines.append("None. Every in-scope `.md` file on disk is present in the index.")
    else:
        lines.append(f"**{cg['md_missing_count']} markdown files on disk are missing from the index.**")
        lines.append("If the watcher is running these resolve within a few seconds; a persistent")
        lines.append("entry here is a real reach bug. Sample:")
        lines.append("")
        for p in cg["md_missing_sample"]:
            lines.append(f"- `{p}`")
        if cg["md_missing_count"] > len(cg["md_missing_sample"]):
            lines.append(f"- ... and {cg['md_missing_count'] - len(cg['md_missing_sample'])} more")
    lines.append("")

    # Format gap.
    fg = r["format_gap"]
    lines.append("## 2. Format gap (non-markdown knowledge not in the index)")
    lines.append("")
    lines.append(f"Non-md knowledge on disk: {fg['fulltext_nonmd_total']} plain-text "
                 f"(srt/txt/vtt), indexed full-text {fg['fulltext_nonmd_indexed']}; "
                 f"{fg['metadata_total']} documents (pdf/docx/xlsx/pptx/epub), "
                 f"indexed as stubs {fg['metadata_indexed']}.")
    lines.append("")
    if fg["gap_count"] == 0:
        lines.append("Gap: **0**. Every non-md knowledge file on disk is in the index "
                     "(transcripts full-text, documents as discoverable stubs).")
    else:
        lines.append(f"Gap: **{fg['gap_count']}** non-md knowledge files are not indexed. "
                     "A non-zero value means a format is not being walked.")
    lines.append("")
    if fg["by_ext"]:
        lines.append("Unindexed by format:")
        lines.append("")
        lines.append("| Extension | Unindexed files |")
        lines.append("|---|---|")
        for ext, n in fg["by_ext"].items():
            lines.append(f"| `{ext}` | {n} |")
        lines.append("")
    if fg["by_zone"]:
        lines.append("By zone (where the dark knowledge lives):")
        lines.append("")
        lines.append("| Zone | Unindexed knowledge files | Breakdown |")
        lines.append("|---|---|---|")
        for zone, d in list(fg["by_zone"].items())[:20]:
            total = sum(d.values())
            bd = ", ".join(f"{k} {v}" for k, v in sorted(d.items(), key=lambda x: -x[1]))
            lines.append(f"| {zone} | {total} | {bd} |")
        lines.append("")

    # Drift.
    dr = r["drift"]
    lines.append("## 3. Drift (index out of sync with disk)")
    lines.append("")
    lines.append(f"- **Ghosts** (in index, file gone from disk): {dr['ghosts_count']}")
    lines.append(f"- **Pollution** (indexed from a policy-excluded dir such as ExarSharedBrain): {dr['pollution_count']}")
    lines.append(f"- **Stale** (file on disk newer than its index row): {dr['stale_count']}")
    lines.append("")
    if dr["ghosts_sample"]:
        lines.append("Ghost sample:")
        for p in dr["ghosts_sample"]:
            lines.append(f"- `{p}`")
        lines.append("")
    if dr["pollution_sample"]:
        lines.append("Pollution sample (these inflate the index with duplicates):")
        for p in dr["pollution_sample"]:
            lines.append(f"- `{p}`")
        if dr["pollution_count"] > len(dr["pollution_sample"]):
            lines.append(f"- ... and {dr['pollution_count'] - len(dr['pollution_sample'])} more")
        lines.append("")

    # Index internals.
    ii = r["index_internal"]
    lines.append("## Index internal health (for context)")
    lines.append("")
    lines.append(f"- Rows in index: {ii['notes_rows']}")
    lines.append(f"- With description: {ii['with_description']} ({ii['description_pct']}%)")
    lines.append(f"- Archived knowledge intentionally excluded: {r['archived_knowledge_excluded']}")
    lines.append("- Health distribution:")
    for state, n in sorted(ii["health_distribution"].items(), key=lambda x: -x[1]):
        lines.append(f"  - {state}: {n}")
    lines.append("")
    if r["unclassified_ext"]:
        lines.append("Unclassified extensions (policy did not have a rule, review and assign):")
        for ext, n in r["unclassified_ext"].items():
            lines.append(f"- `{ext}`: {n}")
        lines.append("")

    # Recommendations (only for gaps actually present).
    recs = []
    if cg["md_missing_count"] > 0:
        recs.append("**Completeness gap**: ensure the watcher is running (`./status.sh`) "
                    "or run `python3 build_index.py`. The scheduled reconcile also heals this.")
    if fg["gap_count"] > 0:
        recs.append("**Format gap**: a non-md format is not being walked. Check `policy.py` "
                    "KNOWLEDGE_EXT and `walk_vault`.")
    if dr["pollution_count"] > 0:
        recs.append("**Pollution**: a policy-excluded dir leaked into the index. "
                    "Confirm `policy.EXCLUDE_DIRS` then rebuild.")
    if dr["ghosts_count"] > 0 or dr["stale_count"] > 0:
        recs.append("**Ghosts / stale**: a running watcher clears these on its next cycle; "
                    "otherwise run the reconcile or rebuild.")

    lines.append("## What to do about each gap")
    lines.append("")
    if recs:
        for i, rec in enumerate(recs, 1):
            lines.append(f"{i}. {rec}")
    else:
        lines.append("Nothing. Reach is complete (100% across all tiers), no drift, no pollution.")
    lines.append("")
    lines.append("Re-run anytime: `python3.11 reach.py`")
    lines.append("")
    return "\n".join(lines)


def print_summary(r):
    reach = r["reach"]
    print("=== Vault Index Reach ===")
    for key, label in [("md_completeness", "Markdown completeness"),
                       ("fulltext", "Full-text knowledge   "),
                       ("total_knowledge", "Total knowledge       ")]:
        t = reach[key]
        print(f"  {label}: {t['pct']:5.1f}%  ({t['hits']}/{t['total']})")
    print(f"  Completeness gap (md missing): {r['completeness_gap']['md_missing_count']}")
    fg = r["format_gap"]
    print(f"  Format gap (non-md not indexed): {fg['gap_count']} "
          f"(of {fg['fulltext_nonmd_total']} text + {fg['metadata_total']} docs on disk)")
    dr = r["drift"]
    print(f"  Drift: {dr['ghosts_count']} ghosts, {dr['pollution_count']} pollution, {dr['stale_count']} stale")


def main():
    ap = argparse.ArgumentParser(description="Vault index reach audit (coverage reconciliation)")
    ap.add_argument("--json", action="store_true", help="Emit JSON to stdout, do not write report")
    ap.add_argument("--quiet", action="store_true", help="Write report, minimal stdout")
    ap.add_argument("--out", default=str(VAULT_ROOT / "00_REACH_REPORT.md"),
                    help="Report path (default: vault root 00_REACH_REPORT.md)")
    args = ap.parse_args()

    r = build_report()

    if args.json:
        print(json.dumps(r, indent=2, ensure_ascii=False))
        return

    out = Path(args.out)
    out.write_text(render_markdown(r), encoding="utf-8")
    if not args.quiet:
        print_summary(r)
        print(f"\nReport: {out}")
    else:
        print(f"[reach] wrote {out}")


if __name__ == "__main__":
    main()
