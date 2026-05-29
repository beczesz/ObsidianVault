#!/bin/bash
# ledger_append.sh — append ONE big-event line to this machine's activity ledger shard.
# ===========================================================================
# Sync-safe by design: each machine writes ONLY its own shard file, named by a
# machine slug (hostname). Two machines therefore never touch the same file, so
# Obsidian / Drive sync can never conflict on the ledger. Markdown is the source
# of truth (BDOS law: the DB is a regenerable cache, not the ledger).
#
# Append-only. BIG events only (not granular). Read back by /alf-recap.
#
# Usage:
#   ledger_append.sh --source <who> --category <cat> --summary "text" [--ts <ISO>]
# Example:
#   ledger_append.sh --source curator --category tend --summary "Alfred dashboard v0.4.2"
#
# Categories (convention): build, tend, audit, publish, promote, fix, denoise,
#   spec, capture, session, decision, note.
# ===========================================================================
set -euo pipefail

VAULT="$(cd "$(dirname "$0")/../../../.." && pwd)"
ACT_DIR="$VAULT/02_Areas/Personal Growth/Alfred/activity"

# Machine slug: readable + stable (short hostname, .local stripped, slugified).
MACHINE="$(hostname -s 2>/dev/null || hostname || echo unknown)"
MACHINE="$(printf '%s' "$MACHINE" | tr '[:upper:]' '[:lower:]' \
           | sed 's/\.local$//; s/[^a-z0-9]/-/g; s/--*/-/g; s/^-//; s/-$//')"
[ -z "$MACHINE" ] && MACHINE="unknown"

SOURCE="manual"; CATEGORY="note"; SUMMARY=""; TS=""
while [ $# -gt 0 ]; do
  case "$1" in
    --source)   SOURCE="$2";   shift 2 ;;
    --category) CATEGORY="$2"; shift 2 ;;
    --summary)  SUMMARY="$2";  shift 2 ;;
    --ts)       TS="$2";       shift 2 ;;
    *) shift ;;
  esac
done
[ -z "$SUMMARY" ] && { echo "ledger_append: --summary required" >&2; exit 1; }
[ -z "$TS" ] && TS="$(date +%Y-%m-%dT%H:%M)"

MONTH="$(printf '%s' "$TS" | cut -c1-7)"   # YYYY-MM
SHARD="$ACT_DIR/${MONTH}.${MACHINE}.md"
mkdir -p "$ACT_DIR"

if [ ! -f "$SHARD" ]; then
  cat > "$SHARD" <<EOF
---
title: Activity ledger · ${MONTH} · ${MACHINE}
date: ${TS%%T*}
author: Becze Szabolcs
status: active
description: Alfred activity-ledger shard for machine '${MACHINE}', month ${MONTH}. Append-only big-event log. One shard per machine so multi-device Obsidian sync never conflicts. Read by /alf-recap.
tags: [alfred, activity-ledger, ${MACHINE}]
agent: alfred
schema: alfred.activity.v1
machine: ${MACHINE}
---

# Activity · ${MONTH} · ${MACHINE}

<!-- Append-only. One line per big event:  - <ISO> · <source> · <category> · <summary> -->

EOF
fi

# Single line, no pipe/newline breakage, no em dashes (vault §0).
CLEAN="$(printf '%s' "$SUMMARY" | tr '\n' ' ' | sed 's/—/,/g; s/--/,/g')"
printf '%s\n' "- ${TS} · ${SOURCE} · ${CATEGORY} · ${CLEAN}" >> "$SHARD"
echo "ledger += [${MACHINE}] ${TS} ${SOURCE}/${CATEGORY}: $(printf '%s' "$CLEAN" | cut -c1-60)"
