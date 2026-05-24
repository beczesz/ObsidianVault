"""
seed_logs.py — 8 test scenarios for agent_observability.db (Phase B, 2026-05-24)

Scenarios:
  1. Librarian retrieve — success, multi-file read, 2.1K tokens
  2. Maestro observe — success, log aggregation across 6 agents
  3. Curator tend — success, dashboard version bump
  4. Sage harvest — success, RSS + cognitive processing
  5. Presto adapt — partial, one platform failed
  6. Broker pipeline-review — success, 4 leads processed
  7. Curator build — error (YAML parse failure mid-build)
  8. Librarian tidy — slow operation (large vault scan, 8.2s)

Each scenario writes: invocation_start + 2-4 tool_calls + invocation_end (or error).
Total: ~30 events (8 invocations × 3-5 events each).
"""

import sys
import time
from pathlib import Path

# Ensure we can import from same directory
sys.path.insert(0, str(Path(__file__).parent))

from agent_log import log_event, VALID_AGENTS

# We write events with explicit ts so they look historical and realistic
BASE_TS = '2026-05-24T08:00:00Z'

def ts(offset_minutes: int) -> str:
    """Generate ISO timestamp offset_minutes after base."""
    from datetime import datetime, timezone, timedelta
    base = datetime(2026, 5, 24, 8, 0, 0, tzinfo=timezone.utc)
    dt = base + timedelta(minutes=offset_minutes)
    return dt.strftime('%Y-%m-%dT%H:%M:%SZ')


def seed_all():
    import time as _time
    latencies = []

    # -----------------------------------------------------------------------
    # Scenario 1: Librarian retrieve — success
    # -----------------------------------------------------------------------
    session = 'seed-lib-retrieve-01'
    t0 = _time.perf_counter()
    s1 = log_event('librarian', 'retrieve', 'invocation_start',
                   'Retrieve started: Deák sprint state query',
                   ts=ts(0), session_id=session,
                   model='claude-sonnet-4-6', project='deak-husuzlet',
                   level='info', refresh_sidecar=False)
    log_event('librarian', 'retrieve', 'tool_call', 'Read 00_INDEX.md (tier-1)',
              ts=ts(1), session_id=session, model='claude-sonnet-4-6',
              tool_used='Read', duration_ms=18, level='debug',
              parent_event_id=s1, project='deak-husuzlet', refresh_sidecar=False)
    log_event('librarian', 'retrieve', 'tool_call', 'Read Deák/01_PROJECT_STATE.md (tier-2)',
              ts=ts(2), session_id=session, model='claude-sonnet-4-6',
              tool_used='Read', duration_ms=24, level='debug',
              parent_event_id=s1, project='deak-husuzlet', refresh_sidecar=False)
    log_event('librarian', 'retrieve', 'invocation_end',
              'Retrieve complete — 3 files, 2 relevant sections returned',
              ts=ts(3), session_id=session, model='claude-sonnet-4-6',
              tokens_in=2100, tokens_out=480, duration_ms=910,
              outcome='success', level='info',
              parent_event_id=s1, project='deak-husuzlet', refresh_sidecar=False)
    latencies.append((_time.perf_counter() - t0) * 1000)

    # -----------------------------------------------------------------------
    # Scenario 2: Maestro observe — success
    # -----------------------------------------------------------------------
    session = 'seed-maestro-observe-01'
    t0 = _time.perf_counter()
    s2 = log_event('maestro', 'observe', 'invocation_start',
                   'Observe: aggregating family log streams (6 agents)',
                   ts=ts(10), session_id=session,
                   model='claude-sonnet-4-6', level='info', refresh_sidecar=False)
    log_event('maestro', 'observe', 'tool_call', 'Glob agent log directories',
              ts=ts(11), session_id=session, tool_used='Bash',
              duration_ms=55, level='debug',
              parent_event_id=s2, refresh_sidecar=False)
    log_event('maestro', 'observe', 'info', '6 agents scanned, 0 active log files (Phase 2.B pending)',
              ts=ts(12), session_id=session, level='warn',
              parent_event_id=s2, refresh_sidecar=False)
    log_event('maestro', 'observe', 'invocation_end',
              'Observe complete — empty state graceful, Phase 2.B reminder emitted',
              ts=ts(13), session_id=session,
              tokens_in=1800, tokens_out=320, duration_ms=1240,
              outcome='success', level='info',
              parent_event_id=s2, refresh_sidecar=False)
    latencies.append((_time.perf_counter() - t0) * 1000)

    # -----------------------------------------------------------------------
    # Scenario 3: Curator tend — success
    # -----------------------------------------------------------------------
    session = 'seed-curator-tend-01'
    t0 = _time.perf_counter()
    s3 = log_event('curator', 'tend', 'invocation_start',
                   'Tend maestro/index.html — add Logcat tab',
                   ts=ts(20), session_id=session,
                   model='claude-sonnet-4-6', level='info',
                   project='dashboard-family', refresh_sidecar=False)
    log_event('curator', 'tend', 'tool_call', 'Read DESIGN_SYSTEM.md',
              ts=ts(21), session_id=session, tool_used='Read',
              duration_ms=12, level='debug',
              parent_event_id=s3, project='dashboard-family', refresh_sidecar=False)
    log_event('curator', 'tend', 'tool_call', 'Edit maestro/index.html — version bump + Logcat tab',
              ts=ts(22), session_id=session, tool_used='Edit',
              duration_ms=38, level='debug',
              parent_event_id=s3, project='dashboard-family', refresh_sidecar=False)
    log_event('curator', 'tend', 'tool_call', 'Write 00_DASHBOARD_INDEX.md — index updated',
              ts=ts(23), session_id=session, tool_used='Write',
              duration_ms=9, level='debug',
              parent_event_id=s3, project='dashboard-family', refresh_sidecar=False)
    log_event('curator', 'tend', 'invocation_end',
              'Tend complete — maestro 0.3.0→0.4.0, index updated, sidecar refreshed',
              ts=ts(24), session_id=session,
              tokens_in=4200, tokens_out=1100, duration_ms=2150,
              outcome='success', level='info',
              parent_event_id=s3, project='dashboard-family', refresh_sidecar=False)
    latencies.append((_time.perf_counter() - t0) * 1000)

    # -----------------------------------------------------------------------
    # Scenario 4: Sage harvest — success
    # -----------------------------------------------------------------------
    session = 'seed-sage-harvest-01'
    t0 = _time.perf_counter()
    s4 = log_event('sage', 'harvest', 'invocation_start',
                   'Daily harvest: 7 sources, scheduled 06:00',
                   ts=ts(30), session_id=session,
                   model='claude-sonnet-4-6', level='info',
                   project='personal-growth', refresh_sidecar=False)
    log_event('sage', 'harvest', 'tool_call', 'Bash: fetch RSS feeds (3 sources)',
              ts=ts(31), session_id=session, tool_used='Bash',
              duration_ms=1200, level='debug',
              parent_event_id=s4, project='personal-growth', refresh_sidecar=False)
    log_event('sage', 'harvest', 'tool_call', 'Write: 4 atomic thoughts to _inbox/',
              ts=ts(33), session_id=session, tool_used='Write',
              duration_ms=22, level='debug',
              parent_event_id=s4, project='personal-growth', refresh_sidecar=False)
    log_event('sage', 'harvest', 'invocation_end',
              'Harvest complete — 4 atomics written, 2 signals for Presto',
              ts=ts(34), session_id=session,
              tokens_in=3800, tokens_out=920, duration_ms=3450,
              outcome='success', level='info',
              parent_event_id=s4, project='personal-growth', refresh_sidecar=False)
    latencies.append((_time.perf_counter() - t0) * 1000)

    # -----------------------------------------------------------------------
    # Scenario 5: Presto adapt — partial (LinkedIn succeeded, Twitter failed)
    # -----------------------------------------------------------------------
    session = 'seed-presto-adapt-01'
    t0 = _time.perf_counter()
    s5 = log_event('presto', 'adapt', 'invocation_start',
                   'Adapt: Sage atomic "AI-native teams" → LinkedIn + Twitter variants',
                   ts=ts(40), session_id=session,
                   model='claude-sonnet-4-6', level='info',
                   project='marketing-dh', refresh_sidecar=False)
    log_event('presto', 'adapt', 'tool_call', 'Read atomic: personal-growth/Ideas/ai-native-teams.md',
              ts=ts(41), session_id=session, tool_used='Read',
              duration_ms=14, level='debug',
              parent_event_id=s5, project='marketing-dh', refresh_sidecar=False)
    log_event('presto', 'adapt', 'warning',
              'Twitter/X variant skipped — character limit conflicts with source atomic',
              ts=ts(42), session_id=session, level='warn',
              parent_event_id=s5, project='marketing-dh', refresh_sidecar=False)
    log_event('presto', 'adapt', 'invocation_end',
              'Adapt partial — LinkedIn OK (423 chars), Twitter skipped (char limit)',
              ts=ts(43), session_id=session,
              tokens_in=2900, tokens_out=680, duration_ms=1820,
              outcome='partial', level='warn',
              parent_event_id=s5, project='marketing-dh', refresh_sidecar=False)
    latencies.append((_time.perf_counter() - t0) * 1000)

    # -----------------------------------------------------------------------
    # Scenario 6: Broker pipeline-review — success
    # -----------------------------------------------------------------------
    session = 'seed-broker-pipeline-01'
    t0 = _time.perf_counter()
    s6 = log_event('broker', 'pipeline-review', 'invocation_start',
                   'Pipeline review: 4 active leads in CPS Sales',
                   ts=ts(50), session_id=session,
                   model='claude-sonnet-4-6', level='info',
                   project='cps-sales', refresh_sidecar=False)
    log_event('broker', 'pipeline-review', 'tool_call',
              'Read Pipeline.md — 4 leads in HOT/WARM/COLD lanes',
              ts=ts(51), session_id=session, tool_used='Read',
              duration_ms=21, level='debug',
              parent_event_id=s6, project='cps-sales', refresh_sidecar=False)
    log_event('broker', 'pipeline-review', 'decision',
              'Prioritize KBOSS follow-up — 14 days no response, stage=WARM',
              ts=ts(52), session_id=session, level='info',
              parent_event_id=s6, project='cps-sales', refresh_sidecar=False)
    log_event('broker', 'pipeline-review', 'invocation_end',
              'Pipeline review done — 1 follow-up queued, 3 leads on-track',
              ts=ts(53), session_id=session,
              tokens_in=3200, tokens_out=710, duration_ms=1560,
              outcome='success', level='info',
              parent_event_id=s6, project='cps-sales', refresh_sidecar=False)
    latencies.append((_time.perf_counter() - t0) * 1000)

    # -----------------------------------------------------------------------
    # Scenario 7: Curator build — error (YAML parse failure)
    # -----------------------------------------------------------------------
    session = 'seed-curator-build-err-01'
    t0 = _time.perf_counter()
    s7 = log_event('curator', 'build', 'invocation_start',
                   'Build new dashboard: ExarLabs migration from legacy',
                   ts=ts(60), session_id=session,
                   model='claude-sonnet-4-6', level='info',
                   project='exarlabs', refresh_sidecar=False)
    log_event('curator', 'build', 'tool_call', 'Read ExarLabs/dashboard.html (legacy)',
              ts=ts(61), session_id=session, tool_used='Read',
              duration_ms=17, level='debug',
              parent_event_id=s7, project='exarlabs', refresh_sidecar=False)
    log_event('curator', 'build', 'error',
              'YAML parse error: Hungarian typographic quotes in frontmatter (« »)',
              ts=ts(62), session_id=session, level='error',
              parent_event_id=s7, project='exarlabs',
              tags=['yaml-error', 'hungarian-quotes'],
              payload={'file': '02_Areas/ExarLabs/projects.md', 'line': 14},
              refresh_sidecar=False)
    log_event('curator', 'build', 'invocation_end',
              'Build aborted — YAML parse failure; recommend migrate_uuid.py lenient parser',
              ts=ts(63), session_id=session,
              tokens_in=1600, tokens_out=240, duration_ms=680,
              outcome='failure', level='error',
              parent_event_id=s7, project='exarlabs', refresh_sidecar=False)
    latencies.append((_time.perf_counter() - t0) * 1000)

    # -----------------------------------------------------------------------
    # Scenario 8: Librarian tidy — slow (large vault scan, 8.2s)
    # -----------------------------------------------------------------------
    session = 'seed-lib-tidy-slow-01'
    t0 = _time.perf_counter()
    s8 = log_event('librarian', 'tidy', 'invocation_start',
                   'Tidy: full vault scan for stale tier-2 indexes',
                   ts=ts(70), session_id=session,
                   model='claude-sonnet-4-6', level='info',
                   project=None, refresh_sidecar=False)
    log_event('librarian', 'tidy', 'tool_call', 'Bash: find 02_Areas -name "00_INDEX.md"',
              ts=ts(71), session_id=session, tool_used='Bash',
              duration_ms=3400, level='debug',
              parent_event_id=s8, refresh_sidecar=False)
    log_event('librarian', 'tidy', 'tool_call', 'Read: 11 tier-2 index files',
              ts=ts(73), session_id=session, tool_used='Read',
              duration_ms=2100, level='debug',
              parent_event_id=s8, refresh_sidecar=False)
    log_event('librarian', 'tidy', 'info',
              '3 tier-2 indexes stale (>14 days): navigátor, exarlabs, ignis-academy',
              ts=ts(74), session_id=session, level='warn',
              parent_event_id=s8, refresh_sidecar=False)
    # Final insert — refresh sidecar here (last write)
    log_event('librarian', 'tidy', 'invocation_end',
              'Tidy complete — 3 stale flagged, 8 fresh. Vault scan 8.2s (large tree)',
              ts=ts(75), session_id=session,
              tokens_in=5800, tokens_out=1240, duration_ms=8200,
              outcome='success', level='info',
              parent_event_id=s8, refresh_sidecar=True)  # sidecar refresh on last event
    latencies.append((_time.perf_counter() - t0) * 1000)

    return latencies


if __name__ == '__main__':
    import sqlite3
    from pathlib import Path

    db_path = Path(__file__).parent / 'cache' / 'agent_observability.db'
    sidecar_path = Path(__file__).parent.parent.parent.parent / '_dashboards' / '_design' / 'agent_logs.json'

    print('Seeding 8 test scenarios...')
    t_total = time.perf_counter()
    latencies = seed_all()
    total_ms = (time.perf_counter() - t_total) * 1000

    # Verify row counts
    con = sqlite3.connect(str(db_path))
    total_rows = con.execute('SELECT COUNT(*) FROM agent_events').fetchone()[0]
    per_agent = con.execute(
        'SELECT agent, COUNT(*) as cnt FROM agent_events GROUP BY agent ORDER BY agent'
    ).fetchall()
    con.close()

    print(f'\nTotal rows inserted: {total_rows}')
    print('Per-agent:')
    for agent, cnt in per_agent:
        print(f'  {agent:15} {cnt:3} events')

    import os
    sidecar_size = os.path.getsize(sidecar_path) if sidecar_path.exists() else 0
    print(f'\nSidecar JSON: {sidecar_path}')
    print(f'  Size: {sidecar_size:,} bytes ({sidecar_size/1024:.1f} KB)')

    write_times = latencies
    p50 = sorted(write_times)[len(write_times)//2]
    p95_idx = int(len(write_times) * 0.95)
    p95 = sorted(write_times)[min(p95_idx, len(write_times)-1)]
    print(f'\nWrite latency per scenario (each = 4-5 events):')
    print(f'  p50: {p50:.1f}ms   p95: {p95:.1f}ms')
    print(f'  Total wall time: {total_ms:.0f}ms')
    print('\nSeed complete.')
