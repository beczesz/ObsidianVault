#!/bin/bash
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
CACHE_DIR="$SCRIPT_DIR/cache"

echo "=== BDOS Vault Indexing — Status ==="

if [ -f "$CACHE_DIR/vault.db" ]; then
    SIZE=$(du -h "$CACHE_DIR/vault.db" | cut -f1)
    echo "  vault.db        : ✅ exists ($SIZE)"
else
    echo "  vault.db        : ❌ missing"
fi

check_pid() {
    local pidfile="$1"; local name="$2"; local port="$3"
    if [ -f "$pidfile" ]; then
        local pid=$(cat "$pidfile")
        if kill -0 "$pid" 2>/dev/null; then
            echo "  $name : ✅ running (PID $pid)${port:+, port $port}"
        else
            echo "  $name : ⚠️  stale PID file (PID $pid not alive)"
        fi
    else
        echo "  $name : ⏸  not running"
    fi
}

check_pid "$CACHE_DIR/watch.pid" "Watcher       " ""
check_pid "$CACHE_DIR/events.pid" "Events server " "4322"

if [ -f "$CACHE_DIR/watch.log" ]; then
    echo ""
    echo "  Latest watcher: $(tail -1 "$CACHE_DIR/watch.log" 2>/dev/null)"
fi
