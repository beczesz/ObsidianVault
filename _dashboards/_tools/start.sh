#!/usr/bin/env bash
# Start the Ideas Vault dashboard server (macOS / Linux).
# Usage:  ./start.sh    (chmod +x once if needed)
set -e
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
echo "Starting Ideas Vault dashboard server..."
node "$DIR/dash-server.mjs"
