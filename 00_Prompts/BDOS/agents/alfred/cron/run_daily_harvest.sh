#!/bin/bash
# Alfred daily harvest — runs at 06:00 Europe/Budapest (04:00 UTC summer).
# Reads the ChatGPT "Referencia chat", extracts new thoughts, generates
# structured notes in 02_Areas/Personal Growth/Ideas/.
# Silent by default unless 3+ new thoughts, uncertain inbox, or errors.
# NOTE: This replaces the former sage/cron/run_daily_harvest.sh (Sage-Alfred merge 2026-05-28).

set -euo pipefail

VAULT="/Users/becze-mac/My Drive (beczesz.szabolcs@gmail.com)/0. Ideas Vault"
CLAUDE="/opt/homebrew/bin/claude"
LOG_DIR="$VAULT/00_Prompts/BDOS/agents/alfred/cron/logs"
TS=$(date +%Y-%m-%dT%H-%M-%S)

mkdir -p "$LOG_DIR"

cd "$VAULT"
"$CLAUDE" -p "/alf-harvest" \
  --permission-mode acceptEdits \
  >"$LOG_DIR/daily_${TS}.log" 2>&1

# Prune logs older than 30 days
find "$LOG_DIR" -name 'daily_*.log' -mtime +30 -delete 2>/dev/null || true
