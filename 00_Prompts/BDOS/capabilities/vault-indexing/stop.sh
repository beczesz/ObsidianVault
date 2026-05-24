#!/bin/bash
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
CACHE_DIR="$SCRIPT_DIR/cache"

stop_pidfile() {
    local pidfile="$1"; local name="$2"
    if [ ! -f "$pidfile" ]; then
        echo "  $name : not running"
        return
    fi
    local pid=$(cat "$pidfile")
    if kill -0 "$pid" 2>/dev/null; then
        kill -TERM "$pid"
        sleep 1
        kill -0 "$pid" 2>/dev/null && kill -KILL "$pid"
        rm -f "$pidfile"
        echo "  $name : 🛑 stopped (PID $pid)"
    else
        rm -f "$pidfile"
        echo "  $name : stale PID file removed"
    fi
}

echo "Stopping BDOS Vault Indexing background processes..."
stop_pidfile "$CACHE_DIR/watch.pid" "Watcher"
stop_pidfile "$CACHE_DIR/events.pid" "Events server"
