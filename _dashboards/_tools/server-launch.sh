#!/usr/bin/env bash
# Launch wrapper for the dashboard server under launchd.
# Sources ~/.bdos/anthropic.env (if present) so the Alfred Sonnet tier has an
# ANTHROPIC_API_KEY in the launchd context (the login keychain is not reachable
# from a background agent). The key file is chmod 600 and NOT in the vault.
set -e
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ENV_FILE="$HOME/.bdos/anthropic.env"
if [ -f "$ENV_FILE" ]; then
  set -a
  . "$ENV_FILE"
  set +a
fi
NODE="$(command -v node || echo /opt/homebrew/bin/node)"
exec "$NODE" "$DIR/dash-server.mjs"
