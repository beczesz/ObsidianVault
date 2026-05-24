"""
agent_log.py — Writer API for agent_observability.db  (Phase 5, schema v1.2, 2026-05-24)

Table: agent_logs (28 columns) — see agent_obs_schema.sql for the full DDL.

Usage (from any Python script or agent runner):

    from agent_log import AgentLogger, log_event

    log = AgentLogger(agent='librarian', model='claude-sonnet-4-6')
    log.start(mode='retrieve', project='deák-húsüzlet',
               message='Retrieve started')
    try:
        ...work...
        log.tool('Read', 'Read 3 files', duration_ms=42)
        log.query('FTS5 search on vault.db', query_duration_ms=18)
        log.end(outcome='success', tokens_in=2100, tokens_out=480, duration_ms=910)
    except Exception as e:
        log.error(str(e))

Sidecar JSON is refreshed automatically on every insert via _refresh_sidecar().
The sidecar lives at VAULT_ROOT/_dashboards/_design/agent_logs.json and is the
transport layer that the HTML dashboards read (no server-side Python required in
the browser context).

Log levels:  debug | info | notice | warning | error | critical
Event types: task_started | task_completed | tool_call | query | file_scan |
             index_update | token_usage | dashboard_update | approval_requested |
             publish_prepared | publish_completed | reflection | learning |
             version_change | error
"""

from __future__ import annotations
import json
import os
import sqlite3
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

# ---------------------------------------------------------------------------
# Paths (all relative to the vault root — adjust if moved)
# ---------------------------------------------------------------------------
_HERE = Path(__file__).parent                         # vault-indexing/
_CACHE = _HERE / 'cache'
DB_PATH = _CACHE / 'agent_observability.db'

# Walk up to vault root (vault-indexing -> capabilities -> BDOS -> 00_Prompts -> vault root)
_VAULT_ROOT = _HERE.parent.parent.parent.parent
SIDECAR_PATH = _VAULT_ROOT / '_dashboards' / '_design' / 'agent_logs.json'

# ---------------------------------------------------------------------------
# Model cost table (USD per 1K tokens; input / output)
# Updated 2026-05-24 — extend as new models are deployed
# ---------------------------------------------------------------------------
MODEL_COSTS: dict[str, tuple[float, float]] = {
    # claude-sonnet-4-6  (3 / 15 per 1M)
    'claude-sonnet-4-6':        (0.003,  0.015),
    'claude-sonnet-4-5':        (0.003,  0.015),
    # claude-opus-4-7 / 4-5  (15 / 75 per 1M)
    'claude-opus-4-7':          (0.015,  0.075),
    'claude-opus-4-5':          (0.015,  0.075),
    # claude-haiku-3-5  (0.8 / 4 per 1M)
    'claude-haiku-3-5':         (0.0008, 0.004),
    # generic fallback
    'unknown':                  (0.003,  0.015),
}

VALID_AGENTS = frozenset(['librarian','maestro','curator','sage','presto','broker'])
VALID_EVENT_TYPES = frozenset([
    'task_started', 'task_completed', 'tool_call', 'query',
    'file_scan', 'index_update', 'token_usage', 'dashboard_update',
    'approval_requested', 'publish_prepared', 'publish_completed',
    'reflection', 'learning', 'version_change', 'error',
])
VALID_LEVELS = frozenset(['debug', 'info', 'notice', 'warning', 'error', 'critical'])
VALID_STATUSES = frozenset(['success', 'partial', 'failure'])


def _compute_cost(
    model: Optional[str],
    tokens_in: Optional[int],
    tokens_out: Optional[int],
) -> Optional[float]:
    if tokens_in is None and tokens_out is None:
        return None
    key = (model or 'unknown').lower()
    in_rate, out_rate = MODEL_COSTS.get(key, MODEL_COSTS['unknown'])
    cost = (tokens_in or 0) * in_rate / 1000 + (tokens_out or 0) * out_rate / 1000
    return round(cost, 6)


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


def _get_connection() -> sqlite3.Connection:
    con = sqlite3.connect(str(DB_PATH), timeout=10)
    con.row_factory = sqlite3.Row
    con.execute('PRAGMA journal_mode=WAL')
    con.execute('PRAGMA foreign_keys=ON')
    return con


def _refresh_sidecar(con: sqlite3.Connection) -> None:
    """
    Export last 500 events to agent_logs.json for dashboard consumption.
    Schema: { generated_at, schema_version, total_rows, events: [...] }
    Each event: all DB columns as a plain dict (None -> null).
    """
    cur = con.execute("""
        SELECT id, timestamp, agent_name, agent_id, agent_version,
               task_id, operation_id, parent_operation_id, trace_id,
               log_level, event_type, project, title, message,
               status, model_name, tool_name,
               input_tokens, output_tokens, total_tokens, estimated_cost,
               duration_ms, query_duration_ms, affected_files,
               tags, metadata_json, error_message, created_at
        FROM agent_logs
        ORDER BY id DESC
        LIMIT 500
    """)
    rows = [dict(r) for r in cur]
    rows.reverse()  # chronological order

    total = con.execute('SELECT COUNT(*) FROM agent_logs').fetchone()[0]

    payload = {
        'generated_at':   _now_iso(),
        'schema_version': '1.2',
        'total_rows':     total,
        'events':         rows,
    }
    SIDECAR_PATH.parent.mkdir(parents=True, exist_ok=True)
    tmp = SIDECAR_PATH.with_suffix('.tmp')
    tmp.write_text(json.dumps(payload, ensure_ascii=False, indent=2, default=str))
    tmp.replace(SIDECAR_PATH)


# ---------------------------------------------------------------------------
# Low-level insert function (public — for use without AgentLogger class)
# ---------------------------------------------------------------------------
def log_event(
    agent_name: str,
    mode: str,
    event_type: str,
    message: str,
    *,
    title: Optional[str] = None,
    project: Optional[str] = None,
    log_level: str = 'info',
    model_name: Optional[str] = None,
    tool_name: Optional[str] = None,
    input_tokens: Optional[int] = None,
    output_tokens: Optional[int] = None,
    duration_ms: Optional[int] = None,
    query_duration_ms: Optional[int] = None,
    status: Optional[str] = None,
    task_id: Optional[str] = None,
    operation_id: Optional[str] = None,
    parent_operation_id: Optional[str] = None,
    trace_id: Optional[str] = None,
    agent_id: Optional[str] = None,
    agent_version: Optional[str] = None,
    affected_files: Optional[list] = None,
    tags: Optional[list] = None,
    metadata_json: Optional[dict] = None,
    error_message: Optional[str] = None,
    ts: Optional[str] = None,
    refresh_sidecar: bool = True,
) -> int:
    """
    Insert one event row into agent_logs and optionally refresh the sidecar JSON.
    Returns the new row id.
    """
    if agent_name not in VALID_AGENTS:
        raise ValueError(f'Unknown agent: {agent_name!r}. Must be one of {sorted(VALID_AGENTS)}')
    if event_type not in VALID_EVENT_TYPES:
        raise ValueError(f'Unknown event_type: {event_type!r}. Must be one of {sorted(VALID_EVENT_TYPES)}')
    if log_level not in VALID_LEVELS:
        raise ValueError(f'Unknown log_level: {log_level!r}. Must be one of {sorted(VALID_LEVELS)}')
    if status is not None and status not in VALID_STATUSES:
        raise ValueError(f'Unknown status: {status!r}. Must be one of {sorted(VALID_STATUSES)}')

    now = ts or _now_iso()
    total_tokens = (
        (input_tokens or 0) + (output_tokens or 0)
        if (input_tokens is not None or output_tokens is not None) else None
    )
    estimated_cost = _compute_cost(model_name, input_tokens, output_tokens)
    title_val = title or (message[:60].rstrip() if message else None)
    tags_json      = json.dumps(tags, ensure_ascii=False)          if tags is not None           else None
    payload_json   = json.dumps(metadata_json, ensure_ascii=False) if metadata_json is not None  else None
    files_json     = json.dumps(affected_files, ensure_ascii=False) if affected_files is not None else None

    con = _get_connection()
    try:
        cur = con.execute("""
            INSERT INTO agent_logs
              (timestamp, agent_name, agent_id, agent_version,
               task_id, operation_id, parent_operation_id, trace_id,
               log_level, event_type, project, title, message,
               status, model_name, tool_name,
               input_tokens, output_tokens, total_tokens, estimated_cost,
               duration_ms, query_duration_ms, affected_files,
               tags, metadata_json, error_message, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            now, agent_name, agent_id, agent_version,
            task_id, operation_id, parent_operation_id, trace_id,
            log_level, event_type, project, title_val, message,
            status, model_name, tool_name,
            input_tokens, output_tokens, total_tokens, estimated_cost,
            duration_ms, query_duration_ms, files_json,
            tags_json, payload_json, error_message, now,
        ))
        new_id = cur.lastrowid
        con.commit()
        if refresh_sidecar:
            _refresh_sidecar(con)
        return new_id
    finally:
        con.close()


# ---------------------------------------------------------------------------
# Stateful logger class (convenience wrapper)
# ---------------------------------------------------------------------------
class AgentLogger:
    """
    Context-aware logger for a single agent invocation session.

    Example:
        log = AgentLogger(agent='curator', model='claude-sonnet-4-6')
        start_id = log.start(mode='tend', project='cps-sales')
        tool_id  = log.tool('Edit', 'bumped version header', duration_ms=12)
        log.end(status='success', tokens_in=800, tokens_out=200, duration_ms=350)

    Log levels:  debug | info | notice | warning | error | critical
    Event types: task_started | task_completed | tool_call | query | file_scan |
                 index_update | token_usage | dashboard_update | approval_requested |
                 publish_prepared | publish_completed | reflection | learning |
                 version_change | error
    """

    def __init__(
        self,
        agent: str,
        task_id: Optional[str] = None,
        model: Optional[str] = 'claude-sonnet-4-6',
        agent_version: Optional[str] = None,
        auto_refresh: bool = True,
    ):
        if agent not in VALID_AGENTS:
            raise ValueError(f'Unknown agent: {agent!r}')
        self.agent = agent
        self.task_id = task_id or f'task-{uuid.uuid4().hex[:8]}'
        self.model = model
        self.agent_version = agent_version
        self.auto_refresh = auto_refresh
        self._start_id: Optional[int] = None
        self._start_wall: Optional[float] = None
        self._mode: str = 'unknown'

    def _emit(self, event_type: str, message: str, mode: Optional[str] = None, **kwargs) -> int:
        return log_event(
            agent_name=self.agent,
            mode=mode or self._mode,
            event_type=event_type,
            message=message,
            task_id=self.task_id,
            model_name=kwargs.pop('model_name', self.model),
            agent_version=kwargs.pop('agent_version', self.agent_version),
            refresh_sidecar=self.auto_refresh,
            **kwargs,
        )

    def start(
        self,
        mode: str,
        message: str = 'Task started',
        project: Optional[str] = None,
        **kwargs,
    ) -> int:
        """Log task_started. Returns row id. Starts wall-clock timer."""
        self._mode = mode
        self._start_wall = time.perf_counter()
        self._start_id = self._emit(
            'task_started', message, mode=mode,
            log_level='info', project=project, **kwargs,
        )
        return self._start_id

    def end(
        self,
        status: str = 'success',
        message: str = 'Task completed',
        **kwargs,
    ) -> int:
        """Log task_completed. Auto-computes duration if start() was called."""
        if self._start_wall is not None and 'duration_ms' not in kwargs:
            kwargs['duration_ms'] = int((time.perf_counter() - self._start_wall) * 1000)
        return self._emit(
            'task_completed', message,
            log_level='info', status=status,
            parent_operation_id=str(self._start_id) if self._start_id else None,
            **kwargs,
        )

    def tool(self, tool_name: str, message: str, **kwargs) -> int:
        """Log a tool_call event."""
        return self._emit(
            'tool_call', message,
            tool_name=tool_name,
            log_level='debug',
            parent_operation_id=str(self._start_id) if self._start_id else None,
            **kwargs,
        )

    def query(self, message: str, query_duration_ms: Optional[int] = None, **kwargs) -> int:
        """Log a query event (Librarian-specific: DB/index query with query_duration_ms)."""
        return self._emit(
            'query', message,
            log_level='debug',
            query_duration_ms=query_duration_ms,
            parent_operation_id=str(self._start_id) if self._start_id else None,
            **kwargs,
        )

    def file_scan(self, message: str, affected_files: Optional[list] = None, **kwargs) -> int:
        """Log a file_scan event."""
        return self._emit(
            'file_scan', message,
            log_level='debug',
            affected_files=affected_files,
            parent_operation_id=str(self._start_id) if self._start_id else None,
            **kwargs,
        )

    def index_update(self, message: str, affected_files: Optional[list] = None, **kwargs) -> int:
        """Log an index_update event."""
        return self._emit(
            'index_update', message,
            log_level='info',
            affected_files=affected_files,
            parent_operation_id=str(self._start_id) if self._start_id else None,
            **kwargs,
        )

    def token_usage(
        self,
        message: str,
        input_tokens: Optional[int] = None,
        output_tokens: Optional[int] = None,
        **kwargs,
    ) -> int:
        """Log a token_usage event (explicit token accounting)."""
        return self._emit(
            'token_usage', message,
            log_level='info',
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            parent_operation_id=str(self._start_id) if self._start_id else None,
            **kwargs,
        )

    def dashboard_update(self, message: str, **kwargs) -> int:
        """Log a dashboard_update event (Curator: version bump, index updated)."""
        return self._emit(
            'dashboard_update', message,
            log_level='info',
            parent_operation_id=str(self._start_id) if self._start_id else None,
            **kwargs,
        )

    def info(self, message: str, **kwargs) -> int:
        return self._emit(
            'task_completed', message,
            log_level='info',
            parent_operation_id=str(self._start_id) if self._start_id else None,
            **kwargs,
        )

    def notice(self, message: str, **kwargs) -> int:
        return self._emit(
            'task_completed', message,
            log_level='notice',
            parent_operation_id=str(self._start_id) if self._start_id else None,
            **kwargs,
        )

    def warn(self, message: str, **kwargs) -> int:
        return self._emit(
            'error', message,
            log_level='warning',
            parent_operation_id=str(self._start_id) if self._start_id else None,
            **kwargs,
        )

    def error(self, message: str, **kwargs) -> int:
        return self._emit(
            'error', message,
            log_level='error',
            status='failure',
            error_message=message,
            parent_operation_id=str(self._start_id) if self._start_id else None,
            **kwargs,
        )

    def critical(self, message: str, **kwargs) -> int:
        return self._emit(
            'error', message,
            log_level='critical',
            status='failure',
            error_message=message,
            parent_operation_id=str(self._start_id) if self._start_id else None,
            **kwargs,
        )

    def decision(self, message: str, **kwargs) -> int:
        """Log approval_requested (confirmation gate for destructive/family-wide actions)."""
        return self._emit(
            'approval_requested', message,
            log_level='notice',
            parent_operation_id=str(self._start_id) if self._start_id else None,
            **kwargs,
        )

    def reflection(self, message: str, **kwargs) -> int:
        return self._emit(
            'reflection', message,
            log_level='info',
            parent_operation_id=str(self._start_id) if self._start_id else None,
            **kwargs,
        )

    def learning(self, message: str, **kwargs) -> int:
        return self._emit(
            'learning', message,
            log_level='info',
            parent_operation_id=str(self._start_id) if self._start_id else None,
            **kwargs,
        )

    def version_change(self, message: str, **kwargs) -> int:
        return self._emit(
            'version_change', message,
            log_level='notice',
            parent_operation_id=str(self._start_id) if self._start_id else None,
            **kwargs,
        )

    def handoff(self, message: str, **kwargs) -> int:
        """Log task_completed as a handoff (agent-to-agent pass)."""
        return self._emit(
            'task_completed', message,
            log_level='info',
            parent_operation_id=str(self._start_id) if self._start_id else None,
            **kwargs,
        )

    def scheduler_event(
        self,
        event_type: str,
        message: str,
        *,
        job_id: Optional[str] = None,
        level: str = 'info',
        status: Optional[str] = None,
        duration_ms: Optional[int] = None,
        metadata: Optional[dict] = None,
    ) -> int:
        """
        Convenience helper for scheduler events.
        Automatically tags with ['scheduler'] and optionally 'job:<job_id>'.
        event_type should be one of: task_started, task_completed, error, index_update.
        """
        tags: list = ['scheduler']
        if job_id:
            tags.append(f'job:{job_id}')
        return self._emit(
            event_type, message,
            log_level=level,
            status=status,
            duration_ms=duration_ms,
            tags=tags,
            metadata_json=metadata,
            parent_operation_id=str(self._start_id) if self._start_id else None,
        )


if __name__ == '__main__':
    import sys
    print(f'DB: {DB_PATH}  (exists: {DB_PATH.exists()})')
    print(f'Sidecar: {SIDECAR_PATH}')
    if '--smoke' in sys.argv:
        log = AgentLogger(agent='maestro', model='claude-sonnet-4-6')
        sid = log.start(mode='observe', message='smoke test start')
        log.tool('Read', 'read AGENTS_INDEX.md', duration_ms=14)
        log.end(status='success', input_tokens=500, output_tokens=120, duration_ms=280)
        print(f'Smoke test OK — task {log.task_id}, start_id={sid}')
    if '--refresh-sidecar' in sys.argv:
        con = _get_connection()
        _refresh_sidecar(con)
        con.close()
        print(f'Sidecar refreshed: {SIDECAR_PATH}')
