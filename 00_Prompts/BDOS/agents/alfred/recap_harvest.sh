#!/bin/bash
# recap_harvest.sh — gather activity for /alf-recap from the markdown ledger shards.
# ===========================================================================
# Source of truth: 02_Areas/Personal Growth/Alfred/activity/YYYY-MM.<machine>.md
# Reads ALL machine shards, filters by date window, merges sorted by timestamp.
# Sync-safe: shards are per-machine (no two machines write the same file).
# NO git, NO database dependency (both are unreliable across multi-device sync).
#
# Usage:
#   recap_harvest.sh [--since YYYY-MM-DD] [--until YYYY-MM-DD]
#   Default: --since today, --until now.
# Output: plain text under ### headers, for Alfred to read + narrate. Read-only.
# ===========================================================================
set -euo pipefail

VAULT="$(cd "$(dirname "$0")/../../../.." && pwd)"
ACT_DIR="$VAULT/02_Areas/Personal Growth/Alfred/activity"

SINCE="$(date +%Y-%m-%d)"; UNTIL=""
while [ $# -gt 0 ]; do
  case "$1" in
    --since) SINCE="$2"; shift 2 ;;
    --until) UNTIL="$2"; shift 2 ;;
    *) shift ;;
  esac
done
UNTIL_EFF="${UNTIL:-9999-12-31}"

echo "### WINDOW"
echo "since=$SINCE until=${UNTIL:-now}"
echo

echo "### ACTIVITY (merged across all machines, sorted by time)"
# Entry lines look like:  - 2026-05-29T19:00 · curator · tend · summary
# $2 (whitespace-split) is the ISO timestamp; date = first 10 chars.
if ls "$ACT_DIR"/*.md >/dev/null 2>&1; then
  out="$(grep -hE '^- [0-9]{4}-[0-9]{2}-[0-9]{2}T' "$ACT_DIR"/*.md 2>/dev/null \
        | awk -v s="$SINCE" -v u="$UNTIL_EFF" '{ d=substr($2,1,10); if (d>=s && d<=u) print }' \
        | sort)"
  if [ -n "$out" ]; then printf '%s\n' "$out"; else echo "(no ledger entries in window)"; fi
else
  echo "(no ledger shards yet)"
fi
echo

echo "### MACHINES seen"
if ls "$ACT_DIR"/*.md >/dev/null 2>&1; then
  for f in "$ACT_DIR"/*.md; do basename "$f"; done | sed -E 's/^[0-9]{4}-[0-9]{2}\.//; s/\.md$//' | sort -u
else
  echo "(none)"
fi
echo

echo "### DAILY NOTES in window"
if [ -d "$VAULT/05_DailyNotes" ]; then
  ls "$VAULT/05_DailyNotes/" 2>/dev/null | grep -E '[0-9]{4}-[0-9]{2}-[0-9]{2}' \
    | awk -v s="$SINCE" -v u="$UNTIL_EFF" '{ d=substr($0,1,10); if (d>=s && d<=u) print }' || echo "(none)"
else
  echo "(no 05_DailyNotes dir)"
fi
