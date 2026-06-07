#!/bin/bash
# Alfred weekly curate — runs Monday 06:05 Europe/Budapest (04:05 UTC summer).
# Trend analysis, category revision, atomic promote candidates, meta-learning proposals.
# May take 15-20 minutes.
# NOTE: This replaces the former sage/cron/run_weekly_curate.sh (Sage-Alfred merge 2026-05-28).

set -euo pipefail

VAULT="/Users/becze-mac/My Drive (beczesz.szabolcs@gmail.com)/0. Ideas Vault"
CLAUDE="/opt/homebrew/bin/claude"
LOG_DIR="$VAULT/00_Prompts/BDOS/agents/alfred/cron/logs"
TS=$(date +%Y-%m-%dT%H-%M-%S)

mkdir -p "$LOG_DIR"

cd "$VAULT"
"$CLAUDE" -p "/alf-curate

Ez a futás az ütemezett heti curate (Monday 06:05 Europe/Budapest). A megerosités implicit \"yes\" — futtasd közvetlenül, ne kérdezz vissza." \
  --permission-mode acceptEdits \
  >"$LOG_DIR/weekly_${TS}.log" 2>&1

# Prune weekly logs older than 90 days
find "$LOG_DIR" -name 'weekly_*.log' -mtime +90 -delete 2>/dev/null || true
