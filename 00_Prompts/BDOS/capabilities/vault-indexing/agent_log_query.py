"""
agent_log_query.py — Reader API for agent_observability.db  (Phase 5, schema v1.2, 2026-05-24)

Table: agent_logs (28 columns). All queries are read-only SELECT statements.

Usage (Python API):
    from agent_log_query import AgentLogQuery

    q = AgentLogQuery()

    # Filter by agent
    rows = q.by_agent('librarian', limit=20)

    # Filter by project
    rows = q.by_project('deák-húsüzlet')

    # Errors only
    rows = q.errors(agent='curator')

    # Slow operations (duration > threshold ms)
    rows = q.slow_ops(threshold_ms=2000)

    # High-token operations
    rows = q.high_token(threshold=5000)

    # Full-text search on title + message
    rows = q.search('YAML parse error')

    # Librarian-specific: slow queries (query_duration_ms)
    rows = q.slow_queries(threshold_ms=50)

    # Per-agent summary cards (for per-agent Logs panel)
    summary = q.agent_summary('librarian')

    # All recent events (Logcat view — all agents)
    rows = q.recent(limit=200)

CLI usage:
    python3 agent_log_query.py --agent librarian --limit 20
    python3 agent_log_query.py --errors
    python3 agent_log_query.py --slow 1000
    python3 agent_log_query.py --slow-query 50
    python3 agent_log_query.py --search "parse error"
    python3 agent_log_query.py --summary librarian
    python3 agent_log_query.py --stats

Log levels:  debug | info | notice | warning | error | critical
Event types: task_started | task_completed | tool_call | query | file_scan |
             index_update | token_usage | dashboard_update | approval_requested |
             publish_prepared | publish_completed | reflection | learning |
             version_change | error
"""

from __future__ import annotations
import json
import sqlite3
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Any, Optional

_HERE = Path(__file__).parent
DB_PATH = _HERE / 'cache' / 'agent_observability.db'

VALID_AGENTS = frozenset(['librarian','maestro','curator','sage','presto','broker'])
VALID_LEVELS = frozenset(['debug', 'info', 'notice', 'warning', 'error', 'critical'])
LEVEL_ORDER  = ['debug', 'info', 'notice', 'warning', 'error', 'critical']


def _get_connection() -> sqlite3.Connection:
    con = sqlite3.connect(str(DB_PATH), timeout=10)
    con.row_factory = sqlite3.Row
    con.execute('PRAGMA query_only=ON')
    return con


def _rows_to_dicts(rows) -> list[dict]:
    return [dict(r) for r in rows]


def _iso_n_days_ago(n: int) -> str:
    dt = datetime.now(timezone.utc) - timedelta(days=n)
    return dt.strftime('%Y-%m-%dT%H:%M:%SZ')


class AgentLogQuery:
    """Read-only query interface for agent_observability.db (agent_logs table)."""

    # ------------------------------------------------------------------
    # Core filter primitives
    # ------------------------------------------------------------------

    def recent(self, limit: int = 200, offset: int = 0) -> list[dict]:
        """Last N events across all agents, chronological order."""
        con = _get_connection()
        try:
            rows = con.execute("""
                SELECT * FROM agent_logs
                ORDER BY id DESC LIMIT ? OFFSET ?
            """, (limit, offset)).fetchall()
            return list(reversed(_rows_to_dicts(rows)))
        finally:
            con.close()

    def by_agent(
        self,
        agent: str,
        limit: int = 100,
        offset: int = 0,
        since_days: Optional[int] = None,
    ) -> list[dict]:
        """All events for one agent (chronological)."""
        where = 'agent_name = ?'
        params: list[Any] = [agent]
        if since_days is not None:
            where += ' AND timestamp >= ?'
            params.append(_iso_n_days_ago(since_days))
        con = _get_connection()
        try:
            rows = con.execute(
                f'SELECT * FROM agent_logs WHERE {where} ORDER BY id DESC LIMIT ? OFFSET ?',
                params + [limit, offset]
            ).fetchall()
            return list(reversed(_rows_to_dicts(rows)))
        finally:
            con.close()

    def by_project(self, project: str, limit: int = 100) -> list[dict]:
        """Events filtered by project slug."""
        con = _get_connection()
        try:
            rows = con.execute(
                'SELECT * FROM agent_logs WHERE project = ? ORDER BY id DESC LIMIT ?',
                (project, limit)
            ).fetchall()
            return list(reversed(_rows_to_dicts(rows)))
        finally:
            con.close()

    def by_level(self, level: str, limit: int = 100) -> list[dict]:
        """Events at or above a given severity level."""
        if level not in VALID_LEVELS:
            raise ValueError(f'Unknown level: {level!r}')
        idx = LEVEL_ORDER.index(level)
        levels_to_match = LEVEL_ORDER[idx:]
        placeholders = ','.join('?' * len(levels_to_match))
        con = _get_connection()
        try:
            rows = con.execute(
                f'SELECT * FROM agent_logs WHERE log_level IN ({placeholders}) ORDER BY id DESC LIMIT ?',
                levels_to_match + [limit]
            ).fetchall()
            return list(reversed(_rows_to_dicts(rows)))
        finally:
            con.close()

    def by_event_type(self, event_type: str, limit: int = 100) -> list[dict]:
        con = _get_connection()
        try:
            rows = con.execute(
                'SELECT * FROM agent_logs WHERE event_type = ? ORDER BY id DESC LIMIT ?',
                (event_type, limit)
            ).fetchall()
            return list(reversed(_rows_to_dicts(rows)))
        finally:
            con.close()

    def by_model(self, model: str, limit: int = 100) -> list[dict]:
        con = _get_connection()
        try:
            rows = con.execute(
                'SELECT * FROM agent_logs WHERE model_name = ? ORDER BY id DESC LIMIT ?',
                (model, limit)
            ).fetchall()
            return list(reversed(_rows_to_dicts(rows)))
        finally:
            con.close()

    def by_tool(self, tool: str, limit: int = 100) -> list[dict]:
        con = _get_connection()
        try:
            rows = con.execute(
                'SELECT * FROM agent_logs WHERE tool_name = ? ORDER BY id DESC LIMIT ?',
                (tool, limit)
            ).fetchall()
            return list(reversed(_rows_to_dicts(rows)))
        finally:
            con.close()

    def by_time_range(
        self,
        since: str,
        until: Optional[str] = None,
        agent: Optional[str] = None,
        limit: int = 500,
    ) -> list[dict]:
        """Events in [since, until) ISO range."""
        where = 'timestamp >= ?'
        params: list[Any] = [since]
        if until:
            where += ' AND timestamp < ?'
            params.append(until)
        if agent:
            where += ' AND agent_name = ?'
            params.append(agent)
        con = _get_connection()
        try:
            rows = con.execute(
                f'SELECT * FROM agent_logs WHERE {where} ORDER BY timestamp ASC LIMIT ?',
                params + [limit]
            ).fetchall()
            return _rows_to_dicts(rows)
        finally:
            con.close()

    def errors(self, agent: Optional[str] = None, limit: int = 100) -> list[dict]:
        """Events at level error or critical."""
        where = "log_level IN ('error','critical')"
        params: list[Any] = []
        if agent:
            where += ' AND agent_name = ?'
            params.append(agent)
        con = _get_connection()
        try:
            rows = con.execute(
                f'SELECT * FROM agent_logs WHERE {where} ORDER BY id DESC LIMIT ?',
                params + [limit]
            ).fetchall()
            return list(reversed(_rows_to_dicts(rows)))
        finally:
            con.close()

    def slow_ops(
        self,
        threshold_ms: int = 3000,
        agent: Optional[str] = None,
        limit: int = 50,
    ) -> list[dict]:
        """Operations that took longer than threshold_ms milliseconds."""
        where = 'duration_ms >= ?'
        params: list[Any] = [threshold_ms]
        if agent:
            where += ' AND agent_name = ?'
            params.append(agent)
        con = _get_connection()
        try:
            rows = con.execute(
                f'SELECT * FROM agent_logs WHERE {where} ORDER BY duration_ms DESC LIMIT ?',
                params + [limit]
            ).fetchall()
            return _rows_to_dicts(rows)
        finally:
            con.close()

    def slow_queries(
        self,
        threshold_ms: int = 50,
        agent: Optional[str] = None,
        limit: int = 50,
    ) -> list[dict]:
        """
        Librarian-specific: events with query_duration_ms above threshold.
        Useful for identifying slow vault DB / index queries.
        """
        where = 'query_duration_ms >= ?'
        params: list[Any] = [threshold_ms]
        if agent:
            where += ' AND agent_name = ?'
            params.append(agent)
        con = _get_connection()
        try:
            rows = con.execute(
                f'SELECT * FROM agent_logs WHERE {where} ORDER BY query_duration_ms DESC LIMIT ?',
                params + [limit]
            ).fetchall()
            return _rows_to_dicts(rows)
        finally:
            con.close()

    def high_token(
        self,
        threshold: int = 5000,
        agent: Optional[str] = None,
        limit: int = 50,
    ) -> list[dict]:
        """Operations with total_tokens above threshold."""
        where = 'total_tokens >= ?'
        params: list[Any] = [threshold]
        if agent:
            where += ' AND agent_name = ?'
            params.append(agent)
        con = _get_connection()
        try:
            rows = con.execute(
                f'SELECT * FROM agent_logs WHERE {where} ORDER BY total_tokens DESC LIMIT ?',
                params + [limit]
            ).fetchall()
            return _rows_to_dicts(rows)
        finally:
            con.close()

    def search(self, query: str, agent: Optional[str] = None, limit: int = 100) -> list[dict]:
        """Full-text search on title + message via FTS5."""
        fts_where = 'agent_logs_fts MATCH ?'
        params: list[Any] = [query]
        agent_filter = ''
        if agent:
            agent_filter = f' AND al.agent_name = ?'
            params.append(agent)
        params.append(limit)
        con = _get_connection()
        try:
            rows = con.execute(
                f"""SELECT al.* FROM agent_logs al
                    JOIN agent_logs_fts fts ON al.id = fts.rowid
                    WHERE {fts_where}{agent_filter}
                    ORDER BY rank LIMIT ?""",
                params
            ).fetchall()
            return _rows_to_dicts(rows)
        finally:
            con.close()

    # ------------------------------------------------------------------
    # Aggregate / summary
    # ------------------------------------------------------------------

    def agent_summary(self, agent: str) -> dict:
        """
        Per-agent summary card data:
          total_events, error_count, total_input_tokens, total_output_tokens,
          total_tokens, total_cost, avg_duration_ms, slowest_event (row),
          highest_token_event (row), recent_events (last 10), last_ts
        """
        if agent not in VALID_AGENTS:
            raise ValueError(f'Unknown agent: {agent!r}')
        con = _get_connection()
        try:
            agg = con.execute("""
                SELECT
                  COUNT(*)                                                              AS total_events,
                  SUM(CASE WHEN log_level IN ('error','critical') THEN 1 ELSE 0 END)  AS error_count,
                  SUM(COALESCE(input_tokens, 0))                                       AS total_input_tokens,
                  SUM(COALESCE(output_tokens, 0))                                      AS total_output_tokens,
                  SUM(COALESCE(total_tokens, 0))                                       AS total_tokens,
                  SUM(COALESCE(estimated_cost, 0))                                     AS total_cost,
                  AVG(duration_ms)                                                      AS avg_duration_ms,
                  MAX(timestamp)                                                        AS last_ts
                FROM agent_logs WHERE agent_name = ?
            """, (agent,)).fetchone()

            slowest = con.execute("""
                SELECT * FROM agent_logs WHERE agent_name = ? AND duration_ms IS NOT NULL
                ORDER BY duration_ms DESC LIMIT 1
            """, (agent,)).fetchone()

            highest_tok = con.execute("""
                SELECT * FROM agent_logs
                WHERE agent_name = ? AND total_tokens IS NOT NULL
                ORDER BY total_tokens DESC LIMIT 1
            """, (agent,)).fetchone()

            slowest_q = con.execute("""
                SELECT * FROM agent_logs
                WHERE agent_name = ? AND query_duration_ms IS NOT NULL
                ORDER BY query_duration_ms DESC LIMIT 1
            """, (agent,)).fetchone()

            recent = con.execute("""
                SELECT * FROM agent_logs WHERE agent_name = ? ORDER BY id DESC LIMIT 10
            """, (agent,)).fetchall()

            return {
                'agent':                agent,
                'total_events':         agg['total_events'],
                'error_count':          agg['error_count'],
                'total_input_tokens':   agg['total_input_tokens'],
                'total_output_tokens':  agg['total_output_tokens'],
                'total_tokens':         agg['total_tokens'],
                'total_cost':           round(agg['total_cost'] or 0, 6),
                'avg_duration_ms':      round(agg['avg_duration_ms'] or 0, 1),
                'last_ts':              agg['last_ts'],
                'slowest_event':        dict(slowest) if slowest else None,
                'highest_token_event':  dict(highest_tok) if highest_tok else None,
                'slowest_query_event':  dict(slowest_q) if slowest_q else None,
                'recent_events':        list(reversed([dict(r) for r in recent])),
            }
        finally:
            con.close()

    def global_stats(self) -> dict:
        """Cross-agent aggregate statistics."""
        con = _get_connection()
        try:
            total = con.execute('SELECT COUNT(*) FROM agent_logs').fetchone()[0]
            errors = con.execute(
                "SELECT COUNT(*) FROM agent_logs WHERE log_level IN ('error','critical')"
            ).fetchone()[0]
            per_agent = con.execute("""
                SELECT agent_name, COUNT(*) AS cnt FROM agent_logs
                GROUP BY agent_name ORDER BY cnt DESC
            """).fetchall()
            cost = con.execute(
                'SELECT SUM(estimated_cost) FROM agent_logs'
            ).fetchone()[0]
            meta = con.execute(
                'SELECT key, value FROM obs_build_meta'
            ).fetchall()
            return {
                'total_events': total,
                'error_count':  errors,
                'per_agent':    [dict(r) for r in per_agent],
                'total_cost':   round(cost or 0, 6),
                'meta':         {r['key']: r['value'] for r in meta},
            }
        finally:
            con.close()


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
if __name__ == '__main__':
    import argparse, time

    parser = argparse.ArgumentParser(description='Agent observability DB query CLI (agent_logs table)')
    parser.add_argument('--agent',      help='Filter by agent slug')
    parser.add_argument('--project',    help='Filter by project slug')
    parser.add_argument('--level',      help='Minimum level (debug/info/notice/warning/error/critical)')
    parser.add_argument('--type',       help='Filter by event_type')
    parser.add_argument('--model',      help='Filter by model_name')
    parser.add_argument('--tool',       help='Filter by tool_name')
    parser.add_argument('--errors',     action='store_true', help='Only error/critical events')
    parser.add_argument('--slow',       type=int, metavar='MS', help='Slow ops above MS milliseconds (duration_ms)')
    parser.add_argument('--slow-query', type=int, metavar='MS', help='Slow queries above MS ms (query_duration_ms)')
    parser.add_argument('--high-tok',   type=int, metavar='TOK', help='High-token ops above TOK total tokens')
    parser.add_argument('--search',     metavar='QUERY', help='FTS5 full-text search on title+message')
    parser.add_argument('--summary',    metavar='AGENT', help='Per-agent summary card')
    parser.add_argument('--stats',      action='store_true', help='Global statistics')
    parser.add_argument('--limit',      type=int, default=20, help='Row limit (default 20)')
    parser.add_argument('--recent',     action='store_true', help='Most recent N events')
    args = parser.parse_args()

    q = AgentLogQuery()

    def _print_rows(rows, label=''):
        if label:
            print(f'\n=== {label} ({len(rows)} rows) ===')
        for r in rows:
            ts    = (r.get('timestamp') or '')[:19]
            agent = r.get('agent_name','?')
            lvl   = r.get('log_level','?')
            etype = r.get('event_type','?')
            msg   = (r.get('message') or '')[:80]
            dur   = r.get('duration_ms')
            qdur  = r.get('query_duration_ms')
            tok   = r.get('total_tokens') or 0
            extras = ''
            if dur:  extras += f'  {dur}ms'
            if qdur: extras += f'  q:{qdur}ms'
            if tok:  extras += f'  {tok}tok'
            print(f'  {ts}  [{agent:10}] [{lvl:8}] {etype:18} {msg}{extras}')

    t0 = time.perf_counter()

    if args.stats:
        stats = q.global_stats()
        print(json.dumps(stats, indent=2, default=str))
    elif args.summary:
        summary = q.agent_summary(args.summary)
        print(json.dumps(summary, indent=2, default=str))
    elif args.errors:
        _print_rows(q.errors(agent=args.agent, limit=args.limit), 'Errors')
    elif args.slow is not None:
        _print_rows(q.slow_ops(threshold_ms=args.slow, agent=args.agent, limit=args.limit), f'Slow ops >{args.slow}ms')
    elif getattr(args, 'slow_query', None) is not None:
        _print_rows(q.slow_queries(threshold_ms=args.slow_query, agent=args.agent, limit=args.limit), f'Slow queries >{args.slow_query}ms')
    elif args.high_tok is not None:
        _print_rows(q.high_token(threshold=args.high_tok, agent=args.agent, limit=args.limit), f'High-token >{args.high_tok}')
    elif args.search:
        _print_rows(q.search(args.search, agent=args.agent, limit=args.limit), f'Search: {args.search!r}')
    elif args.project:
        _print_rows(q.by_project(args.project, limit=args.limit), f'Project: {args.project}')
    elif args.level:
        _print_rows(q.by_level(args.level, limit=args.limit), f'Level >= {args.level}')
    elif args.type:
        _print_rows(q.by_event_type(args.type, limit=args.limit), f'Type: {args.type}')
    elif args.model:
        _print_rows(q.by_model(args.model, limit=args.limit), f'Model: {args.model}')
    elif args.tool:
        _print_rows(q.by_tool(args.tool, limit=args.limit), f'Tool: {args.tool}')
    elif args.agent:
        _print_rows(q.by_agent(args.agent, limit=args.limit), f'Agent: {args.agent}')
    elif args.recent:
        _print_rows(q.recent(limit=args.limit), f'Recent {args.limit}')
    else:
        _print_rows(q.recent(limit=args.limit), f'Recent {args.limit}')

    elapsed = (time.perf_counter() - t0) * 1000
    print(f'\nQuery latency: {elapsed:.1f}ms')
