#!/bin/bash
# BDOS Vault Indexing — start the watcher + events server (idempotent).
# Both required for full live-dashboard experience.

set -e

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
CACHE_DIR="$SCRIPT_DIR/cache"
PID_WATCHER="$CACHE_DIR/watch.pid"
PID_EVENTS="$CACHE_DIR/events.pid"
LOG_WATCH="$CACHE_DIR/watch.log"
LOG_EVENTS="$CACHE_DIR/events.log"
DB_FILE="$CACHE_DIR/vault.db"

mkdir -p "$CACHE_DIR"

# ----- WATCHER -----
WATCHER_NEEDED=true
if [ -f "$PID_WATCHER" ]; then
    OLD_PID=$(cat "$PID_WATCHER")
    if kill -0 "$OLD_PID" 2>/dev/null; then
        echo "✅ Watcher already running (PID $OLD_PID)"
        WATCHER_NEEDED=false
    else
        rm -f "$PID_WATCHER"
    fi
fi

if [ "$WATCHER_NEEDED" = "true" ]; then
    if [ ! -f "$DB_FILE" ]; then
        echo "🔨 No vault.db — initial build..."
        python3 "$SCRIPT_DIR/build_index.py"
    fi

    ENGINE="polling"
    WATCHER="$SCRIPT_DIR/watch.py"
    if python3 -c "from watchdog.observers import Observer" 2>/dev/null; then
        ENGINE="event-based (watchdog)"
        WATCHER="$SCRIPT_DIR/watch_event.py"
    fi

    echo "🚀 Starting watcher ($ENGINE)..."
    nohup python3 "$WATCHER" >> "$LOG_WATCH" 2>&1 &
    WP=$!
    sleep 1
    if kill -0 "$WP" 2>/dev/null; then
        echo "   ✅ Watcher PID $WP — $ENGINE"
    else
        echo "   ❌ Watcher failed to start. See $LOG_WATCH"
        exit 1
    fi
fi

# ----- EVENTS SERVER -----
EVENTS_NEEDED=true
if [ -f "$PID_EVENTS" ]; then
    OLD_PID=$(cat "$PID_EVENTS")
    if kill -0 "$OLD_PID" 2>/dev/null; then
        echo "✅ Events server already running (PID $OLD_PID)"
        EVENTS_NEEDED=false
    else
        rm -f "$PID_EVENTS"
    fi
fi

if [ "$EVENTS_NEEDED" = "true" ]; then
    echo "🚀 Starting events server (SSE on port 4322)..."
    nohup python3 "$SCRIPT_DIR/events_server.py" >> "$LOG_EVENTS" 2>&1 &
    EP=$!
    echo $EP > "$PID_EVENTS"
    sleep 1
    if kill -0 "$EP" 2>/dev/null; then
        echo "   ✅ Events server PID $EP — http://localhost:4322/events"
    else
        echo "   ❌ Events server failed to start. See $LOG_EVENTS"
        rm -f "$PID_EVENTS"
        exit 1
    fi
fi

echo ""
echo "✅ Both processes running. Dashboards will get live updates."
echo "   Stop: ./stop.sh"
echo "   Status: ./status.sh"
