#!/usr/bin/env python3
"""BDOS Vault Indexing — Phase 4.A UUID migration script.

Walks files per FRONTMATTER_SCHEMA.md §9 migration plan and adds:
- id: <uuid4>
- index_schema_version: 1

Default: dry-run. Use --apply to actually write.

Usage:
    python3 migrate_uuid.py               # dry-run (default — shows what would change)
    python3 migrate_uuid.py --apply       # apply changes
    python3 migrate_uuid.py --scope bdos  # only BDOS-system files (~50 files)
    python3 migrate_uuid.py --scope sage  # only Sage outputs
    python3 migrate_uuid.py --scope active-frontmatter  # active frontmatter-having files
"""

import argparse
import os
import re
import sys
import uuid
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
VAULT_ROOT = SCRIPT_DIR.parent.parent.parent.parent

# Scope definitions — per FRONTMATTER_SCHEMA.md §9
SCOPES = {
    'bdos': [
        '00_Prompts/BDOS/agents/*.md',
        '00_Prompts/BDOS/agents/**/*.md',
        '00_Prompts/BDOS/capabilities/**/CLAUDE.md',
        '00_Prompts/BDOS/CONSTITUTION*.md',
        '00_Prompts/BDOS/CLAUDE.md',
        '00_Prompts/BDOS/LOG_SCHEMAS.md',
        '00_Prompts/BDOS/AGENT_PROFILES.md',
        '00_Prompts/BDOS/TODO.md',
        '00_Prompts/BDOS/00_BDOS_PRIMER.md',
        '00_Prompts/BDOS/FRONTMATTER_SCHEMA.md',
        '00_Prompts/BDOS/00_AGENTS_INDEX.md',
    ],
    'sage': [
        '02_Areas/Personal Growth/Ideas/thoughts/*.md',
        '02_Areas/Personal Growth/Ideas/atomic/*.md',
        '02_Areas/Personal Growth/Ideas/_inbox/atomic_proposals/*.md',
    ],
    'active-frontmatter': [
        # Anything with existing frontmatter — Librarian will scan
    ],
}

FRONTMATTER_PATTERN = re.compile(r'^(---\s*\n)(.*?)(\n---\s*\n)', re.DOTALL)
ID_LINE_PATTERN = re.compile(r'^id:\s*', re.MULTILINE)
INDEX_SCHEMA_VERSION_PATTERN = re.compile(r'^index_schema_version:\s*', re.MULTILINE)


def has_frontmatter(content):
    return FRONTMATTER_PATTERN.match(content) is not None


def has_id_field(fm_text):
    return ID_LINE_PATTERN.search(fm_text) is not None


def has_isv_field(fm_text):
    return INDEX_SCHEMA_VERSION_PATTERN.search(fm_text) is not None


def add_fields_to_frontmatter(content, new_id, isv=1):
    """Return new content with id and index_schema_version added at the end of frontmatter."""
    m = FRONTMATTER_PATTERN.match(content)
    if not m:
        return content, False
    fm_text = m.group(2)

    additions = []
    if not has_id_field(fm_text):
        additions.append(f"id: {new_id}")
    if not has_isv_field(fm_text):
        additions.append(f"index_schema_version: {isv}")

    if not additions:
        return content, False

    new_fm = fm_text.rstrip() + '\n' + '\n'.join(additions)
    new_content = m.group(1) + new_fm + m.group(3) + content[m.end():]
    return new_content, True


def expand_globs(patterns):
    """Expand list of glob patterns to actual files."""
    out = set()
    for pattern in patterns:
        full = VAULT_ROOT / pattern
        out.update(VAULT_ROOT.glob(pattern))
    return sorted(p for p in out if p.is_file() and p.suffix == '.md')


def collect_files(scope):
    if scope == 'active-frontmatter':
        # Walk all files, filter by has_frontmatter
        files = []
        for root, dirs, fnames in os.walk(VAULT_ROOT):
            dirs[:] = [d for d in dirs if d not in {
                '.smart-env', '.obsidian', '04_Archive', 'node_modules', '.git', '.trash', '_archive_old'
            }]
            for fn in fnames:
                if fn.endswith('.md'):
                    p = Path(root) / fn
                    try:
                        head = p.read_text(encoding='utf-8', errors='replace')[:2000]
                    except OSError:
                        continue
                    if has_frontmatter(head):
                        files.append(p)
        return files
    elif scope in SCOPES:
        return expand_globs(SCOPES[scope])
    elif scope == 'all':
        bdos = expand_globs(SCOPES['bdos'])
        sage = expand_globs(SCOPES['sage'])
        return sorted(set(bdos + sage), key=str)
    else:
        raise ValueError(f"Unknown scope: {scope}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--apply', action='store_true', help='Actually write changes (default: dry-run)')
    ap.add_argument('--scope', choices=['bdos', 'sage', 'active-frontmatter', 'all'], default='bdos')
    args = ap.parse_args()

    files = collect_files(args.scope)
    print(f"Scope: {args.scope}")
    print(f"Files in scope: {len(files)}")
    print(f"Mode: {'APPLY' if args.apply else 'DRY-RUN'}")
    print()

    skipped_no_fm = 0
    skipped_already_has = 0
    would_modify = 0
    modified = 0
    errors = []

    for p in files:
        try:
            content = p.read_text(encoding='utf-8')
        except (OSError, UnicodeDecodeError) as e:
            errors.append((p, str(e)))
            continue

        if not has_frontmatter(content):
            skipped_no_fm += 1
            continue

        m = FRONTMATTER_PATTERN.match(content)
        fm_text = m.group(2)
        if has_id_field(fm_text) and has_isv_field(fm_text):
            skipped_already_has += 1
            continue

        new_uuid = str(uuid.uuid4())
        new_content, changed = add_fields_to_frontmatter(content, new_uuid, isv=1)
        if not changed:
            skipped_already_has += 1
            continue

        rel = p.relative_to(VAULT_ROOT).as_posix()
        if args.apply:
            try:
                p.write_text(new_content, encoding='utf-8')
                modified += 1
                if modified <= 10:
                    print(f"  ✅ {rel} ← id={new_uuid[:8]}...")
            except OSError as e:
                errors.append((p, str(e)))
        else:
            would_modify += 1
            if would_modify <= 10:
                print(f"  WOULD ADD: {rel} ← id={new_uuid[:8]}...")

    if would_modify > 10 or modified > 10:
        print(f"  ... ({(would_modify or modified) - 10} more)")
    print()

    if args.apply:
        print(f"✅ Applied: {modified} files modified")
    else:
        print(f"Dry-run: {would_modify} files WOULD be modified")
        print(f"To apply, re-run with --apply")
    print(f"Skipped (no frontmatter):   {skipped_no_fm}")
    print(f"Skipped (already has id):   {skipped_already_has}")
    if errors:
        print(f"Errors: {len(errors)}")
        for p, e in errors[:5]:
            print(f"  {p}: {e}")


if __name__ == '__main__':
    main()
