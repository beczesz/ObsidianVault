#!/bin/bash
# BDOS vault-indexing — start (macOS/Linux wrapper around launch.py).
# Cross-platform logic lives in launch.py; this machine keeps the scheduler ON
# (it is the designated scheduler owner). To hand scheduler ownership to another
# machine, add --no-scheduler here and remove it on the new owner.
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PY="$(command -v python3 || command -v python)"
exec "$PY" "$SCRIPT_DIR/launch.py" start
