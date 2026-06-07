#!/usr/bin/env python3
"""
scan_marketing_board.py — Marketing Board sidecar generator
============================================================
Scans the vault for marketing seeds and publications, aggregates them
into a structured JSON sidecar consumed by the Presto Marketing Board panel.

Output: _dashboards/_design/marketing_board.json

Run manually:
    python3 scan_marketing_board.py [--vault-root /path/to/vault]

Filters:
  - Files with `example: true` OR `status: example` in frontmatter are SKIPPED
    (these are illustrative placeholders, not production content)
  - Only presto.seed.v1 and presto.publication.v2 schema files are included

Lanes (publication stage → kanban lane):
    seed         → seeds from _inbox/seeds/ (status != exhausted)
    draft        → publications with publication_status: draft OR generated
    prepared     → publications with publication_status: needs_review
    approval     → publications with publication_status: approved (waiting to schedule)
    scheduled    → publications with publication_status: scheduled OR publish_pending
    published    → publications with publication_status: published OR monitoring OR manual_required

Calendar:
    Only publications with planned_publish_date OR scheduled_time are included.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path


# ─── YAML frontmatter parser (minimal, robust) ───────────────────────────────

def parse_yaml_frontmatter(text: str) -> dict:
    """Extract and parse YAML frontmatter from a markdown string.

    Returns an empty dict on any parse error (graceful degradation).
    Supports: scalars (str/int/float/bool/null), inline arrays, block arrays,
    nested objects (indent-based). Quote-aware comment stripping (#-in-string safe).
    """
    try:
        m = re.match(r'^---\s*\n(.*?)\n---', text, re.DOTALL)
        if not m:
            return {}
        raw = m.group(1)
        return _parse_yaml_block(raw.splitlines(), 0)[0]
    except Exception as e:
        return {}


def _strip_comment(line: str) -> str:
    """Remove trailing YAML comment, but preserve # inside quoted strings."""
    result, in_single, in_double = [], False, False
    i = 0
    while i < len(line):
        c = line[i]
        if c == "'" and not in_double:
            in_single = not in_single
        elif c == '"' and not in_single:
            in_double = not in_double
        elif c == '#' and not in_single and not in_double:
            # Check it's not part of a color token like #abc123
            # Only strip if preceded by whitespace or is at start
            if i == 0 or line[i-1] in (' ', '\t'):
                break
        result.append(c)
        i += 1
    return ''.join(result).rstrip()


def _coerce_scalar(s: str):
    """Coerce a YAML scalar string to Python type."""
    s = s.strip()
    # Remove surrounding quotes
    if (s.startswith('"') and s.endswith('"')) or (s.startswith("'") and s.endswith("'")):
        return s[1:-1]
    if s.lower() in ('true', 'yes'):
        return True
    if s.lower() in ('false', 'no'):
        return False
    if s.lower() in ('null', '~', ''):
        return None
    try:
        return int(s)
    except ValueError:
        pass
    try:
        return float(s)
    except ValueError:
        pass
    return s


def _parse_yaml_block(lines: list[str], base_indent: int) -> tuple[dict, int]:
    """Parse a YAML mapping block. Returns (dict, lines_consumed)."""
    result = {}
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.lstrip()
        if not stripped or stripped.startswith('#'):
            i += 1
            continue
        indent = len(line) - len(stripped)
        if indent < base_indent:
            break
        if indent > base_indent:
            i += 1
            continue

        stripped = _strip_comment(stripped)
        if ':' not in stripped:
            i += 1
            continue

        colon_pos = stripped.index(':')
        key = stripped[:colon_pos].strip().strip('"\'')
        rest = stripped[colon_pos+1:].strip()

        if rest == '':
            # Could be block sequence or block mapping
            j = i + 1
            child_lines = []
            child_indent = None
            while j < len(lines):
                child_line = lines[j]
                child_stripped = child_line.lstrip()
                if not child_stripped:
                    j += 1
                    continue
                child_ind = len(child_line) - len(child_stripped)
                if child_indent is None:
                    child_indent = child_ind
                if child_ind < child_indent:
                    break
                child_lines.append(child_line)
                j += 1
            if child_lines:
                first = child_lines[0].lstrip()
                if first.startswith('- ') or first == '-':
                    result[key] = _parse_yaml_sequence(child_lines, child_indent)
                else:
                    child_dict, _ = _parse_yaml_block(child_lines, child_indent)
                    result[key] = child_dict
                i = j
            else:
                result[key] = None
                i += 1
        elif rest.startswith('['):
            # Inline array
            end = rest.find(']')
            if end >= 0:
                inner = rest[1:end]
                result[key] = [_coerce_scalar(x.strip()) for x in inner.split(',') if x.strip()]
            else:
                result[key] = []
            i += 1
        elif rest.startswith('|') or rest.startswith('>'):
            # Block scalar — collect indented lines
            j = i + 1
            scalar_lines = []
            scalar_indent = None
            while j < len(lines):
                sl = lines[j]
                sl_stripped = sl.lstrip()
                if not sl_stripped:
                    scalar_lines.append('')
                    j += 1
                    continue
                sl_ind = len(sl) - len(sl_stripped)
                if scalar_indent is None:
                    scalar_indent = sl_ind
                if sl_ind < scalar_indent:
                    break
                scalar_lines.append(sl[scalar_indent:])
                j += 1
            result[key] = '\n'.join(scalar_lines).strip()
            i = j
        else:
            result[key] = _coerce_scalar(rest)
            i += 1
    return result, i


def _parse_yaml_sequence(lines: list[str], base_indent: int) -> list:
    """Parse a YAML block sequence into a Python list."""
    result = []
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.lstrip()
        if not stripped:
            i += 1
            continue
        indent = len(line) - len(stripped)
        if indent < base_indent:
            break
        if stripped.startswith('- '):
            item_rest = stripped[2:].strip()
            if item_rest == '' or item_rest.startswith('#'):
                # Block mapping item
                j = i + 1
                child_lines = []
                child_indent = None
                while j < len(lines):
                    cl = lines[j]
                    cs = cl.lstrip()
                    if not cs:
                        j += 1
                        continue
                    ci = len(cl) - len(cs)
                    if child_indent is None:
                        child_indent = ci
                    if ci < child_indent:
                        break
                    child_lines.append(cl)
                    j += 1
                if child_lines:
                    child_dict, _ = _parse_yaml_block(child_lines, child_indent if child_indent else base_indent + 2)
                    result.append(child_dict)
                    i = j
                else:
                    result.append(None)
                    i += 1
            elif item_rest.startswith('{'):
                # Inline mapping — skip for simplicity
                result.append(item_rest)
                i += 1
            else:
                # Could be "- key: val" (inline mapping item)
                if ':' in item_rest:
                    # Parse as a single-line mapping, possibly followed by more keys
                    item_dict = {}
                    colon = item_rest.index(':')
                    k = item_rest[:colon].strip().strip('"\'')
                    v = item_rest[colon+1:].strip()
                    item_dict[k] = _coerce_scalar(v)
                    # Collect continuation lines at deeper indent
                    j = i + 1
                    cont_indent = None
                    while j < len(lines):
                        cl = lines[j]
                        cs = cl.lstrip()
                        if not cs:
                            j += 1
                            continue
                        ci = len(cl) - len(cs)
                        if cont_indent is None:
                            cont_indent = ci
                        if ci < cont_indent or cs.startswith('- '):
                            break
                        cont_stripped = _strip_comment(cs)
                        if ':' in cont_stripped:
                            cc = cont_stripped.index(':')
                            ck = cont_stripped[:cc].strip().strip('"\'')
                            cv = cont_stripped[cc+1:].strip()
                            item_dict[ck] = _coerce_scalar(cv)
                        j += 1
                    result.append(item_dict)
                    i = j
                else:
                    result.append(_coerce_scalar(item_rest))
                    i += 1
        else:
            i += 1
    return result


# ─── Publication title helpers ───────────────────────────────────────────────

PUB_TYPE_LABEL = {
    'episode_full': 'launch',
    'personal_post_with_thumbnail': 'post',
    'reel_intro_cut': 'reel',
    'shorts_intro_cut': 'short',
    'tiktok_intro_cut': 'short',
    'followup_activation': 'followup',
    'archive_upload': 'archive',
    'date_fix': 'date-fix',
    'audio_re_upload': 'audio',
    'next_episode_teaser': 'teaser',
}

CHANNEL_FRIENDLY = {
    'youtube': 'YT',
    'youtube-shorts': 'YT Shorts',
    'youtube-community': 'YT Community',
    'facebook': 'FB',
    'instagram': 'IG',
    'tiktok': 'TT',
    'patreon': 'Patreon',
    'spotify': 'Spotify',
}


def _nice_title(pub: dict) -> str:
    """Return a human-friendly display title for a publication card.

    Priority:
    1. ep_number field present in frontmatter
    2. Extract EP number from tags list (regex ep(\\d+))
    3. Extract EP number from seed_ref (regex ep(\\d+))
    4. channel_friendly + pub_type_friendly
    5. filename (id field)
    """
    ep_num = pub.get('ep_number')
    if ep_num is not None:
        try:
            ep_num = int(ep_num)
            pub_type_friendly = PUB_TYPE_LABEL.get(
                str(pub.get('pub_type', '')), str(pub.get('pub_type', ''))
            )
            return f"EP{ep_num} {pub_type_friendly}".strip()
        except (ValueError, TypeError):
            pass

    # Try tags
    tags = pub.get('tags', [])
    if isinstance(tags, list):
        for tag in tags:
            m = re.search(r'ep(\d+)', str(tag), re.IGNORECASE)
            if m:
                pub_type_friendly = PUB_TYPE_LABEL.get(
                    str(pub.get('pub_type', '')), str(pub.get('pub_type', ''))
                )
                return f"EP{m.group(1)} {pub_type_friendly}".strip()

    # Try seed_ref
    seed_ref = pub.get('seed_ref', '') or ''
    m = re.search(r'ep(\d+)', str(seed_ref), re.IGNORECASE)
    if m:
        pub_type_friendly = PUB_TYPE_LABEL.get(
            str(pub.get('pub_type', '')), str(pub.get('pub_type', ''))
        )
        return f"EP{m.group(1)} {pub_type_friendly}".strip()

    # Channel + type fallback
    channel_friendly = CHANNEL_FRIENDLY.get(
        str(pub.get('channel', '')).lower(), str(pub.get('channel', ''))
    )
    pub_type_friendly = PUB_TYPE_LABEL.get(
        str(pub.get('pub_type', '')), str(pub.get('pub_type', ''))
    )
    if channel_friendly or pub_type_friendly:
        return f"{channel_friendly} {pub_type_friendly}".strip()

    # Last fallback: id/filename
    return str(pub.get('id', pub.get('title', '')))


# ─── Helpers ─────────────────────────────────────────────────────────────────

def age_days(dt_str: str | None) -> int | None:
    """Return days since a datetime string (ISO 8601), or None if unparsable."""
    if not dt_str:
        return None
    try:
        # Strip timezone offset for simplicity
        clean = re.sub(r'[+-]\d{2}:\d{2}$', '', str(dt_str)).strip()
        clean = clean.replace('T', ' ').split('.')[0]
        dt = datetime.strptime(clean[:16], '%Y-%m-%d %H:%M')
        now = datetime.now()
        return max(0, (now - dt).days)
    except Exception:
        try:
            dt = datetime.strptime(str(dt_str)[:10], '%Y-%m-%d')
            return max(0, (datetime.now() - dt).days)
        except Exception:
            return None


def is_example(fm: dict) -> bool:
    """Return True if this file is a demo/example and should be skipped."""
    if fm.get('example') is True:
        return True
    status = str(fm.get('status', '')).lower()
    if status == 'example':
        return True
    return False


def pub_stage_to_lane(fm: dict) -> str:
    """Map a publication's publication_status to a kanban lane name."""
    ps = str(fm.get('publication_status', fm.get('stage', 'draft'))).lower()
    mapping = {
        'draft':           'draft',
        'generated':       'draft',
        'needs_review':    'prepared',
        'approved':        'approval',
        'scheduled':       'scheduled',
        'publish_pending': 'scheduled',
        'published':       'published',
        'monitoring':      'published',
        'manual_required': 'published',
        'failed':          'draft',
        'archived':        'published',
    }
    return mapping.get(ps, 'draft')


def extract_pub_card(fm: dict, file_path: str, today: datetime) -> dict:
    """Build a publication card dict from frontmatter."""
    pub_date = fm.get('planned_publish_date') or fm.get('publish_date')
    sched_time = fm.get('scheduled_time')
    created = fm.get('created_at') or fm.get('date')
    intent = fm.get('intent') or {}
    if isinstance(intent, dict):
        objective = intent.get('goal', '')
    else:
        objective = str(intent)
    # Build a minimal pub dict for _nice_title (needs ep_number, pub_type, tags, seed_ref, channel)
    _mini = {
        'ep_number': fm.get('ep_number'),
        'pub_type':  fm.get('pub_type', ''),
        'tags':      fm.get('tags', []),
        'seed_ref':  fm.get('seed_ref', ''),
        'channel':   fm.get('channel', ''),
        'id':        fm.get('publication_id', os.path.basename(file_path)),
        'title':     fm.get('title', os.path.basename(file_path)),
    }
    display_title = _nice_title(_mini)
    return {
        'id':            fm.get('publication_id', os.path.basename(file_path)),
        'title':         display_title,
        'channel':       fm.get('channel', ''),
        'area':          fm.get('area', ''),
        'intent':        objective,
        'seed_ref':      fm.get('seed_ref', ''),
        'campaign_id':   fm.get('campaign_id', ''),
        'stage':         pub_stage_to_lane(fm),
        'publish_date':  str(pub_date) if pub_date else None,
        'publish_time':  str(sched_time) if sched_time else None,
        'published_at':  fm.get('published_at', None),
        'days_since_publish': age_days(fm.get('published_at')),
        'stage_entered_at':   str(created) if created else None,
        'age_days':      age_days(str(created) if created else None),
        'file_path':     file_path,
    }


# ─── Scanners ────────────────────────────────────────────────────────────────

def compute_todos_count(prerequisites) -> dict:
    """Aggregate prerequisites[] status counts into a todos_count dict.

    Works for both presto.seed.v2 (populated prerequisites list) and v1 (empty list).
    Returns: {pending, in_progress, done, skipped, total}
    """
    counts = {'pending': 0, 'in_progress': 0, 'done': 0, 'skipped': 0, 'total': 0}
    if not isinstance(prerequisites, list):
        return counts
    for item in prerequisites:
        if not isinstance(item, dict):
            continue
        status = str(item.get('status', 'pending')).lower()
        if status in counts:
            counts[status] += 1
        counts['total'] += 1
    return counts


def extract_seed_v2_fields(fm: dict) -> dict:
    """Extract v2-specific seed fields, with v1 backward-compat defaults."""
    schema = str(fm.get('schema', '')).lower()
    is_v2 = 'presto.seed.v2' in schema

    prerequisites = fm.get('prerequisites', []) if is_v2 else []
    distribution_timeline = fm.get('distribution_timeline', []) if is_v2 else []

    return {
        'schema_version':        'v2' if is_v2 else 'v1',
        'short_description':     fm.get('short_description', '') if is_v2 else '',
        'runbook_ref':           fm.get('runbook_ref', None) if is_v2 else None,
        'campaign_ref':          fm.get('campaign_ref', None) if is_v2 else None,
        'prerequisites':         prerequisites if isinstance(prerequisites, list) else [],
        'distribution_timeline': distribution_timeline if isinstance(distribution_timeline, list) else [],
        'todos_count':           compute_todos_count(prerequisites),
    }


def scan_seeds(vault_root: Path) -> list[dict]:
    """Scan seed files from _inbox/seeds/."""
    seeds_dir = vault_root / '00_Prompts/BDOS/agents/presto/_inbox/seeds'
    results = []
    if not seeds_dir.is_dir():
        return results
    for md_file in sorted(seeds_dir.glob('*.md')):
        if md_file.name.startswith('_'):
            continue
        try:
            text = md_file.read_text(encoding='utf-8', errors='replace')
        except Exception as e:
            print(f'[SKIP] Cannot read {md_file}: {e}', file=sys.stderr)
            continue
        fm = parse_yaml_frontmatter(text)
        if not fm:
            print(f'[SKIP] No frontmatter: {md_file.name}', file=sys.stderr)
            continue
        if is_example(fm):
            print(f'[FILTER] example seed skipped: {md_file.name}', file=sys.stderr)
            continue
        schema = str(fm.get('schema', '')).lower()
        if 'presto.seed' not in schema:
            print(f'[SKIP] Not a seed schema ({schema}): {md_file.name}', file=sys.stderr)
            continue
        # Skip exhausted seeds
        if fm.get('exhausted_at') is not None:
            print(f'[SKIP] Exhausted seed: {md_file.name}', file=sys.stderr)
            continue
        spawned = fm.get('publications_spawned', [])
        if isinstance(spawned, list):
            pub_ids = [p.get('pub-id', p.get('pub_id', '')) if isinstance(p, dict) else str(p) for p in spawned]
        else:
            pub_ids = []
        rel_path = str(md_file.relative_to(vault_root))
        v2_fields = extract_seed_v2_fields(fm)
        results.append({
            'id':                   fm.get('seed_id', md_file.stem),
            'title':                fm.get('title', md_file.stem),
            'source_type':          fm.get('source_type', ''),
            'captured_at':          str(fm.get('captured_at', fm.get('date', ''))),
            'age_days':             age_days(str(fm.get('captured_at', fm.get('date', '')))),
            'publications_spawned': pub_ids,
            'file_path':            rel_path,
            # v2 fields (v1 seeds get defaults)
            'schema_version':        v2_fields['schema_version'],
            'short_description':     v2_fields['short_description'],
            'runbook_ref':           v2_fields['runbook_ref'],
            'campaign_ref':          v2_fields['campaign_ref'],
            'prerequisites':         v2_fields['prerequisites'],
            'distribution_timeline': v2_fields['distribution_timeline'],
            'todos_count':           v2_fields['todos_count'],
        })
    return results


def scan_publications(vault_root: Path) -> dict[str, list[dict]]:
    """Scan publications from 02_Areas/*/Marketing/Publications/ directories.

    Returns a dict of lane_name → list of card dicts.
    """
    lanes: dict[str, list] = {
        'draft': [], 'prepared': [], 'approval': [], 'scheduled': [], 'published': []
    }
    pub_pattern = vault_root / '02_Areas'
    today = datetime.now()

    for pub_file in sorted(pub_pattern.rglob('Marketing/Publications/*.md')):
        if pub_file.name.startswith('_'):
            continue
        rel = str(pub_file.relative_to(vault_root))
        try:
            text = pub_file.read_text(encoding='utf-8', errors='replace')
        except Exception as e:
            print(f'[SKIP] Cannot read {rel}: {e}', file=sys.stderr)
            continue
        fm = parse_yaml_frontmatter(text)
        if not fm:
            print(f'[SKIP] No frontmatter: {rel}', file=sys.stderr)
            continue
        if is_example(fm):
            print(f'[FILTER] example publication skipped: {rel}', file=sys.stderr)
            continue
        schema = str(fm.get('schema', '')).lower()
        if schema and 'presto.publication' not in schema:
            print(f'[SKIP] Not a publication schema ({schema}): {rel}', file=sys.stderr)
            continue
        lane = pub_stage_to_lane(fm)
        card = extract_pub_card(fm, rel, today)
        lanes[lane].append(card)

    return lanes


def scan_todos(vault_root: Path) -> list[dict]:
    """Scan Presto operational TODOs from _inbox/todos/.

    Returns open (non-closed, non-dismissed) presto.todo.v1 task cards.
    These surface on the board as `type: task` calendar entries (on due_date)
    so a TODO is always visible as a task — not just in the /pres-todo list.
    """
    todos_dir = vault_root / '00_Prompts/BDOS/agents/presto/_inbox/todos'
    results: list[dict] = []
    if not todos_dir.is_dir():
        return results
    for md_file in sorted(todos_dir.glob('*.md')):
        if md_file.name.startswith('_'):
            continue
        try:
            text = md_file.read_text(encoding='utf-8', errors='replace')
        except Exception as e:
            print(f'[SKIP] Cannot read {md_file}: {e}', file=sys.stderr)
            continue
        fm = parse_yaml_frontmatter(text)
        if not fm:
            continue
        if is_example(fm):
            continue
        schema = str(fm.get('schema', '')).lower()
        if 'presto.todo' not in schema:
            continue
        status = str(fm.get('status', 'open')).lower()
        if status in ('done', 'closed', 'dismissed'):
            continue
        rel_path = str(md_file.relative_to(vault_root))
        results.append({
            'id':           fm.get('todo_id', md_file.stem),
            'title':        fm.get('title') or fm.get('description', md_file.stem),
            'area':         fm.get('area', ''),
            'channel':      fm.get('channel', ''),
            'urgency':      str(fm.get('urgency', 'normal')),
            'status':       status,
            'due_date':     str(fm.get('due_date')) if fm.get('due_date') else None,
            'action_type':  fm.get('action_type', ''),
            'related_episode': fm.get('related_episode', ''),
            'requires_human':  fm.get('requires_human', True),
            'file_path':    rel_path,
        })
    return results


def build_calendar(all_pubs: list[dict]) -> dict[str, list]:
    """Build the calendar dict from publications that have a publish_date."""
    calendar: dict[str, list] = {}
    for pub in all_pubs:
        pd = pub.get('publish_date')
        if not pd:
            continue
        date_key = str(pd)[:10]  # YYYY-MM-DD
        if date_key not in calendar:
            calendar[date_key] = []
        calendar[date_key].append({
            'publication_id': pub['id'],
            'title':          pub['title'],
            'channel':        pub['channel'],
            'area':           pub['area'],
            'publish_time':   pub.get('publish_time'),
            'stage':          pub['stage'],
            'status':         pub.get('status'),       # for 3-tier approval class detection
            'type':           'publication',           # MB Detail Drawer router
            'file_path':      pub.get('file_path'),    # FIX: enable calendar pill click → drawer
        })
    return calendar


# ─── Main ────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description='Generate marketing_board.json sidecar')
    parser.add_argument('--vault-root', default=None,
                        help='Path to vault root (default: parent of this script\'s BDOS dir)')
    parser.add_argument('--output', default=None,
                        help='Output JSON path (default: <vault-root>/_dashboards/_design/marketing_board.json)')
    parser.add_argument('--dry-run', action='store_true',
                        help='Print summary without writing output file')
    args = parser.parse_args()

    # Resolve vault root
    if args.vault_root:
        vault_root = Path(args.vault_root).resolve()
    else:
        # This script lives at: <vault>/00_Prompts/BDOS/capabilities/vault-indexing/
        vault_root = Path(__file__).resolve().parent.parent.parent.parent.parent
        # Verify heuristically
        if not (vault_root / '_dashboards').is_dir():
            # Try two levels up
            vault_root = Path(__file__).resolve().parent.parent.parent.parent
        if not (vault_root / '_dashboards').is_dir():
            print(f'ERROR: Cannot locate vault root. Pass --vault-root explicitly.', file=sys.stderr)
            sys.exit(1)

    print(f'Vault root: {vault_root}', file=sys.stderr)

    # Scan
    print('Scanning seeds...', file=sys.stderr)
    seeds = scan_seeds(vault_root)
    print(f'  Found {len(seeds)} production seeds', file=sys.stderr)

    print('Scanning publications...', file=sys.stderr)
    pub_lanes = scan_publications(vault_root)
    total_pubs = sum(len(v) for v in pub_lanes.values())
    print(f'  Found {total_pubs} production publications', file=sys.stderr)
    for lane, items in pub_lanes.items():
        print(f'    {lane}: {len(items)}', file=sys.stderr)

    # Build calendar
    all_pubs = [p for lane_pubs in pub_lanes.values() for p in lane_pubs]
    calendar = build_calendar(all_pubs)
    print(f'  Calendar entries: {len(calendar)} days', file=sys.stderr)

    # Scan operational TODOs → surface as task cards on the calendar (due_date)
    print('Scanning todos...', file=sys.stderr)
    tasks = scan_todos(vault_root)
    print(f'  Found {len(tasks)} open todos', file=sys.stderr)
    for task in tasks:
        dd = task.get('due_date')
        if not dd:
            continue
        date_key = str(dd)[:10]
        calendar.setdefault(date_key, []).append({
            'publication_id': task['id'],
            'title':          task['title'],
            'channel':        task.get('channel') or 'task',
            'area':           task['area'],
            'publish_time':   None,
            'stage':          'task',
            'status':         task['status'],
            'type':           'task',            # MB Detail Drawer router + render branch
            'urgency':        task.get('urgency', 'normal'),
            'file_path':      task.get('file_path'),
        })

    # Assemble output
    output = {
        'generated_at':    datetime.now(timezone.utc).isoformat(),
        'schema_version':  '2',
        'lanes': {
            'seed':      seeds,
            'draft':     pub_lanes['draft'],
            'prepared':  pub_lanes['prepared'],
            'approval':  pub_lanes['approval'],
            'scheduled': pub_lanes['scheduled'],
            'published': pub_lanes['published'],
        },
        'tasks': tasks,
        'calendar': calendar,
    }

    if args.dry_run:
        print('\n--- DRY RUN --- Output (first 2KB):')
        preview = json.dumps(output, ensure_ascii=False, indent=2)[:2048]
        print(preview)
        return

    # Write output
    if args.output:
        out_path = Path(args.output)
    else:
        out_path = vault_root / '_dashboards/_design/marketing_board.json'

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f'\nWrote {out_path} ({out_path.stat().st_size} bytes)', file=sys.stderr)
    print(f'Summary: {len(seeds)} seeds, {total_pubs} publications, {len(tasks)} tasks, {len(calendar)} calendar days')


if __name__ == '__main__':
    main()
