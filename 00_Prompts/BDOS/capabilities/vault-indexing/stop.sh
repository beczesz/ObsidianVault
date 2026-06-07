#!/bin/bash
# BDOS vault-indexing — stop (macOS/Linux wrapper around launch.py).
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PY="$(command -v python3 || command -v python)"
exec "$PY" "$SCRIPT_DIR/launch.py" stop
