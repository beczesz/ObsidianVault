#!/usr/bin/env python3
"""BDOS Vault Indexing — description backfill (Layer B).

Generates a 1-2 sentence `description:` for notes that lack one, using the
Anthropic API (Haiku), and writes it INTO the markdown frontmatter (markdown
stays the source of truth; the SQLite cache is downstream).

Two target sets (see the 2026-05-28 triage):
  SET 1 — note already has a frontmatter block, just no `description`.
          -> insert a `description:` line into the existing block (safe edit).
  SET 2 — note has no frontmatter at all.
          -> prepend a fresh frontmatter block (title/date/author/status/
             description/id/index_schema_version/bdos_index), per CLAUDE.md §4.

Transient notes are excluded (05_DailyNotes, Templates, */logs/*, <20-word stubs).

Safety:
  * DRY-RUN by default. Pass --apply to write files.
  * Idempotent: never overwrites an existing description; safe to re-run.
  * --sample N generates N previews (no writes) so you can judge quality.
  * Every write logged to cache/backfill_descriptions.log.

Usage:
  python3 backfill_descriptions.py --set 1 --sample 8          # preview quality
  python3 backfill_descriptions.py --set 1 --apply             # commit SET 1
  python3 backfill_descriptions.py --set 2 --apply             # commit SET 2
  python3 backfill_descriptions.py --set all --apply --workers 6
"""

import argparse
import json
import os
import re
import sys
import time
import uuid
import hashlib
import sqlite3
import datetime
import ssl
import urllib.request
import urllib.error
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

# macOS system Python often lacks root certs; prefer certifi's bundle if present.
try:
    import certifi
    SSL_CTX = ssl.create_default_context(cafile=certifi.where())
except Exception:
    SSL_CTX = ssl.create_default_context()

SCRIPT_DIR = Path(__file__).resolve().parent
VAULT_ROOT = SCRIPT_DIR.parent.parent.parent.parent
sys.path.insert(0, str(SCRIPT_DIR))
from runtime import db_read_path, CACHE_DIR  # noqa

API_URL = "https://api.anthropic.com/v1/messages"
MODEL = "claude-haiku-4-5-20251001"
LOG_PATH = CACHE_DIR / "backfill_descriptions.log"
BODY_CHAR_CAP = 6000          # cap note body sent to the model
MAX_DESC_WORDS = 45           # safety net; we prefer to cut at a sentence boundary

FM_PATTERN = re.compile(r'^---\s*\n(.*?)\n---\s*\n', re.DOTALL)
H1_PATTERN = re.compile(r'^#\s+(.+?)\s*$', re.MULTILINE)
HAS_DESC = re.compile(r'^\s*description\s*:', re.MULTILINE)
HAS_SOURCE = re.compile(r'^\s*description_source\s*:', re.MULTILINE)


def body_sha(body):
    """Stable short hash of a note body. MUST match build_index.body_sha."""
    return hashlib.sha256((body or '').strip().encode('utf-8')).hexdigest()[:16]

# Triage exclusion: transient / not worth describing.
EXCLUDE_SQL = (
    "path LIKE '05_DailyNotes/%' OR path LIKE 'Templates/%' "
    "OR path LIKE '%/logs/%' OR body_word_count < 20"
)

SYSTEM_PROMPT = (
    "You write one concise description for a note in a personal knowledge vault. "
    "Output ONLY the description text, nothing else: no quotes, no label, no preamble. "
    "1 to 2 sentences, at most 32 words. Write in the SAME language as the note "
    "(Hungarian or English). Be content-bearing: say what the note actually contains "
    "and who would read it, not a generic restatement of the title. "
    "Do NOT use em dashes or double hyphens; use commas, colons, semicolons or periods. "
    "Do NOT use the double-quote character anywhere in your output."
)


def log(msg):
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    ts = datetime.datetime.now().isoformat(timespec='seconds')
    with open(LOG_PATH, 'a', encoding='utf-8') as f:
        f.write(f"{ts}  {msg}\n")


def get_targets(which):
    conn = sqlite3.connect(db_read_path())
    conn.row_factory = sqlite3.Row
    base = ("SELECT path, title, has_frontmatter, mtime FROM notes "
            "WHERE (description IS NULL OR description='') "
            f"AND NOT ({EXCLUDE_SQL}) ")
    if which == '1':
        base += "AND has_frontmatter=1 "
    elif which == '2':
        base += "AND has_frontmatter=0 "
    base += "ORDER BY body_word_count DESC"
    return [dict(r) for r in conn.execute(base).fetchall()]


def call_api(api_key, title, body):
    body = body[:BODY_CHAR_CAP]
    payload = {
        "model": MODEL,
        "max_tokens": 120,
        "system": SYSTEM_PROMPT,
        "messages": [{
            "role": "user",
            "content": f"Note title: {title or '(none)'}\n\nNote content:\n{body}"
        }],
    }
    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(API_URL, data=data, method='POST', headers={
        "x-api-key": api_key,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json",
    })
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=60, context=SSL_CTX) as resp:
                out = json.loads(resp.read())
            return "".join(b.get("text", "") for b in out.get("content", [])).strip()
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503, 529) and attempt < 3:
                time.sleep(2 ** attempt)
                continue
            raise
        except (urllib.error.URLError, TimeoutError):
            if attempt < 3:
                time.sleep(2 ** attempt)
                continue
            raise
    raise RuntimeError("unreachable")


def clean_desc(text):
    """One line, no stray quotes, collapse whitespace, no em dash, length-capped
    at a sentence boundary so we never leave a dangling fragment."""
    text = (text or "").strip().strip('"“”').strip()
    text = re.sub(r'\s+', ' ', text)
    text = text.replace('—', ', ').replace('--', ', ').replace('"', '')
    if len(text.split()) <= MAX_DESC_WORDS:
        return text
    # Over the cap: keep as many whole sentences as fit; else hard-cut.
    sentences = re.split(r'(?<=[.!?])\s+', text)
    out = ''
    for s in sentences:
        cand = (out + ' ' + s).strip() if out else s
        if len(cand.split()) > MAX_DESC_WORDS and out:
            break
        out = cand
        if len(out.split()) >= MAX_DESC_WORDS:
            break
    if not out:  # a single very long sentence
        out = ' '.join(text.split()[:MAX_DESC_WORDS]).rstrip(',.;:') + '.'
    return out.strip()


def yaml_quote(s):
    # Double-quoted YAML scalar; description is guaranteed quote-free by clean_desc.
    return '"' + s.replace('\\', '\\\\') + '"'


def derive_title(path, content):
    m = H1_PATTERN.search(content)
    if m:
        return m.group(1).strip()
    return Path(path).stem.replace('-', ' ').replace('_', ' ').strip()


def set_fm_line(fm_lines, key, full_line, anchor=None):
    """Replace key's line in place if present; else insert right after `anchor`'s
    line if given; else append. Operates on a list of frontmatter lines."""
    kpat = re.compile(rf'^\s*{re.escape(key)}\s*:')
    for i, ln in enumerate(fm_lines):
        if kpat.match(ln):
            fm_lines[i] = full_line
            return
    if anchor:
        apat = re.compile(rf'^\s*{re.escape(anchor)}\s*:')
        for i, ln in enumerate(fm_lines):
            if apat.match(ln):
                fm_lines.insert(i + 1, full_line)
                return
    fm_lines.append(full_line)


def write_fields_into_fm(content, desc, body):
    """Set description + provenance (source=auto, hash=body) in an EXISTING
    frontmatter block. Used for SET 1 generation AND for refresh (replace-in-place)."""
    m = FM_PATTERN.match(content)
    if not m:
        return None
    fm_lines = m.group(1).split('\n')
    h = body_sha(body)
    set_fm_line(fm_lines, 'description', f"description: {yaml_quote(desc)}", anchor='title')
    set_fm_line(fm_lines, 'description_source', "description_source: auto", anchor='description')
    set_fm_line(fm_lines, 'description_hash', f"description_hash: {h}", anchor='description_source')
    return f"---\n" + '\n'.join(fm_lines) + "\n---\n" + content[m.end():]


def prepend_block(content, desc, path, mtime):
    """SET 2: prepend a fresh frontmatter block, with provenance."""
    title = derive_title(path, content)
    date = datetime.date.fromtimestamp(mtime).isoformat()
    h = body_sha(content)   # no frontmatter yet, so body == whole content
    block = (
        "---\n"
        f"title: {yaml_quote(title)}\n"
        f"date: {date}\n"
        "author: Becze Szabolcs\n"
        "status: active\n"
        f"description: {yaml_quote(desc)}\n"
        "description_source: auto\n"
        f"description_hash: {h}\n"
        f"id: {uuid.uuid4()}\n"
        "index_schema_version: 1\n"
        "bdos_index: true\n"
        "---\n\n"
    )
    return block + content


def process_one(api_key, rec, apply, refresh=False):
    """Generate (refresh=False) or regenerate (refresh=True) a description.
    Refresh replaces an existing auto description in place and re-stamps the hash."""
    path = rec['path']
    fpath = VAULT_ROOT / path
    try:
        content = fpath.read_text(encoding='utf-8', errors='replace')
    except OSError as e:
        return path, None, f"read_error: {e}"

    m = FM_PATTERN.match(content)
    body = content[m.end():] if m else content

    if not refresh:
        # Generate mode: skip notes that already carry a description (idempotent).
        if m and HAS_DESC.search(m.group(1)):
            return path, None, "skip: already has description"
        if len(body.split()) < 20:
            return path, None, "skip: too short"
    else:
        # Refresh mode: only touch auto-generated descriptions, and only if the
        # body actually moved on (double-check the live file, not just the index).
        if not m or not HAS_SOURCE.search(m.group(1)):
            return path, None, "skip: not auto-generated"
        if rec.get('description_hash') == body_sha(body):
            return path, None, "skip: body unchanged"

    try:
        raw = call_api(api_key, rec.get('title') or derive_title(path, content), body)
    except Exception as e:
        return path, None, f"api_error: {e}"
    desc = clean_desc(raw)
    if not desc:
        return path, None, "skip: empty generation"

    if m:
        new_content = write_fields_into_fm(content, desc, body)
    else:
        new_content = prepend_block(content, desc, path, rec['mtime'])
    if new_content is None:
        return path, desc, "skip: idempotent"

    if apply:
        fpath.write_text(new_content, encoding='utf-8')
        tag = 'refresh' if refresh else ('set1' if m else 'set2')
        log(f"WROTE [{tag}] {path} :: {desc}")
    return path, desc, "written" if apply else "dry-run"


def process_stamp(rec, apply):
    """Retro-stamp provenance (source=auto + hash) onto a tool-written description
    that predates the provenance feature. Does NOT call the API or change the text."""
    path = rec['path']
    fpath = VAULT_ROOT / path
    try:
        content = fpath.read_text(encoding='utf-8', errors='replace')
    except OSError as e:
        return path, None, f"read_error: {e}"
    m = FM_PATTERN.match(content)
    if not m or not HAS_DESC.search(m.group(1)):
        return path, None, "skip: no frontmatter description"
    if HAS_SOURCE.search(m.group(1)):
        return path, None, "skip: already stamped"
    body = content[m.end():]
    fm_lines = m.group(1).split('\n')
    set_fm_line(fm_lines, 'description_source', "description_source: auto", anchor='description')
    set_fm_line(fm_lines, 'description_hash', f"description_hash: {body_sha(body)}", anchor='description_source')
    new_content = f"---\n" + '\n'.join(fm_lines) + "\n---\n" + content[m.end():]
    if apply:
        fpath.write_text(new_content, encoding='utf-8')
        log(f"STAMPED {path}")
    return path, "(stamped auto)", "written" if apply else "dry-run"


def stale_targets():
    """Notes whose auto description no longer matches the current body."""
    conn = sqlite3.connect(db_read_path())
    conn.row_factory = sqlite3.Row
    rows = conn.execute(
        "SELECT path, title, has_frontmatter, mtime, description_hash FROM notes "
        "WHERE description_source='auto' AND description_hash IS NOT NULL "
        "AND body_hash IS NOT NULL AND description_hash != body_hash "
        f"AND NOT ({EXCLUDE_SQL})"
    ).fetchall()
    return [dict(r) for r in rows]


def log_written_paths():
    """Parse the backfill log for paths the tool has written (for --stamp-auto)."""
    if not LOG_PATH.exists():
        return []
    pat = re.compile(r'WROTE \[(?:set1|set2)\] (.*?) :: ')
    seen = []
    for line in LOG_PATH.read_text(encoding='utf-8').splitlines():
        mm = pat.search(line)
        if mm:
            seen.append(mm.group(1))
    # de-dupe, preserve order
    return list(dict.fromkeys(seen))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--set', choices=['1', '2', 'all'], default='1')
    ap.add_argument('--refresh-stale', action='store_true',
                    help='regenerate descriptions whose body changed since last generation (auto only)')
    ap.add_argument('--stamp-auto', action='store_true',
                    help='retro-stamp provenance onto previously tool-written descriptions (no API calls)')
    ap.add_argument('--apply', action='store_true', help='actually write files (default: dry-run)')
    ap.add_argument('--sample', type=int, default=0, help='generate N previews only, no writes')
    ap.add_argument('--limit', type=int, default=0, help='cap number processed (0 = no cap)')
    ap.add_argument('--workers', type=int, default=6)
    args = ap.parse_args()

    # --- stamp-auto: no API, just provenance ---
    if args.stamp_auto:
        paths = log_written_paths()
        if args.limit:
            paths = paths[:args.limit]
        apply = args.apply
        print(f"{'APPLY' if apply else 'DRY-RUN'}: stamping provenance on {len(paths)} log-written notes\n")
        done = skipped = errors = 0
        for p in paths:
            path, _, status = process_stamp({'path': p}, apply)
            if status.startswith('skip'):
                skipped += 1
            elif status.startswith(('read_error',)):
                errors += 1
                print(f"  ! {status}  {path}")
            else:
                done += 1
        print(f"\n{'='*60}\n  stamped: {done}   skipped: {skipped}   errors: {errors}")
        if apply:
            print("  NEXT: rebuild the index ->  python3 build_index.py")
        return

    api_key = os.environ.get('ANTHROPIC_API_KEY')
    if not api_key:
        print("ERROR: ANTHROPIC_API_KEY not set in environment.", file=sys.stderr)
        sys.exit(1)

    refresh = args.refresh_stale
    if refresh:
        targets = stale_targets()
    else:
        targets = []
        if args.set in ('1', 'all'):
            targets += get_targets('1')
        if args.set in ('2', 'all'):
            targets += get_targets('2')

    if args.sample:
        targets = targets[:args.sample]
        apply = False
        print(f"SAMPLE mode: generating {len(targets)} previews (no writes)\n")
    else:
        if args.limit:
            targets = targets[:args.limit]
        apply = args.apply
        mode = "APPLY (writing files)" if apply else "DRY-RUN (no writes)"
        scope = "refresh-stale" if refresh else f"set={args.set}"
        print(f"{mode}: {len(targets)} target notes ({scope})\n")

    done = errors = skipped = 0
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        futs = {ex.submit(process_one, api_key, r, apply, refresh): r for r in targets}
        for fut in as_completed(futs):
            path, desc, status = fut.result()
            if status.startswith(('skip', 'read_error', 'api_error')):
                if status.startswith('skip'):
                    skipped += 1
                else:
                    errors += 1
                    print(f"  ! {status}  {path}")
                continue
            done += 1
            short = path if len(path) < 70 else '...' + path[-67:]
            print(f"  [{done}] {short}\n        {desc}")

    print(f"\n{'='*60}\n  generated/written: {done}   skipped: {skipped}   errors: {errors}")
    if apply:
        print(f"  log: {LOG_PATH}")
        print("  NEXT: rebuild the index ->  python3 build_index.py")


if __name__ == '__main__':
    main()
