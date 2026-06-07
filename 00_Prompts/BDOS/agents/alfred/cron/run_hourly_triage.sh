#!/bin/bash
# Alfred hourly triage — Cognitive Triage Engine (v0.4).
# Reads email (Gmail/Outlook/Yahoo MCP), filters threads needing a reply, and
# prepares multi-agent dossiers (Librarian + dynamic domain-routing) with a
# draft reply + actionable items. NEVER sends, never writes Gmail in --auto.
# Silent by default (Marveen heartbeat model). Degrade-safe: an unreachable
# source is logged + skipped, not fatal.
#
# Dispatched by the BDOS scheduler (scheduler.py) as job 'alfred-hourly-triage'
# (interval 3600s). Runs only while the BDOS daemon (events_server.py) is up.
# Headless LLM auth relies on CLAUDE_CODE_OAUTH_TOKEN (or ANTHROPIC_API_KEY),
# the same mechanism dash-server.mjs uses for /api/alfred/chat under launchd.

set -euo pipefail

VAULT="/Users/becze-mac/My Drive (beczesz.szabolcs@gmail.com)/0. Ideas Vault"
CLAUDE="/opt/homebrew/bin/claude"
LOG_DIR="$VAULT/00_Prompts/BDOS/agents/alfred/cron/logs"
TS=$(date +%Y-%m-%dT%H-%M-%S)

mkdir -p "$LOG_DIR"

cd "$VAULT"
"$CLAUDE" -p "/alf-triage --auto --source all" \
  --permission-mode acceptEdits \
  >"$LOG_DIR/triage_${TS}.log" 2>&1

# Prune logs older than 30 days
find "$LOG_DIR" -name 'triage_*.log' -mtime +30 -delete 2>/dev/null || true
