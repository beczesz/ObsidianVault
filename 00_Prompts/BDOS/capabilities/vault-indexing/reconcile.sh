#!/bin/bash
# BDOS vault-indexing - scheduled reconciliation backstop.
#
# The growth guarantee. An incremental watcher (event or polling) can miss a
# filesystem event during a crash, sleep, or Drive sync lag, and an event-based
# watcher never re-checks, so a missed file stays invisible until the next full
# build. This job runs a full disk-vs-index reconciliation on a schedule
# (catches anything missed, removes ghosts) and refreshes the honest reach
# sidecar so the dashboard always shows the real number.
#
# Safe alongside the live watcher: both open the DB with WAL + busy_timeout.
# Idempotent: when nothing changed it does no writes.

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Prefer a PyYAML-equipped interpreter for full frontmatter fidelity on any
# markdown reindexed this pass; fall back to whatever python exists (the indexer
# degrades to its stdlib lenient parser without yaml).
pick_py() {
  for c in python3.11 /usr/local/bin/python3 python3 python; do
    if command -v "$c" >/dev/null 2>&1 && "$c" -c "import yaml" >/dev/null 2>&1; then
      echo "$c"; return
    fi
  done
  command -v python3 || command -v python
}
PY="$(pick_py)"

cd "$SCRIPT_DIR" || exit 1

# 1. Full reconciliation: index new/changed, purge ghosts (deleted files).
"$PY" watch.py --once   >/dev/null 2>&1

# 2. Refresh the honest reach sidecar (coverage_pct = real filesystem reach).
"$PY" emit_stats.py     >/dev/null 2>&1

exit 0
