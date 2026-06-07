/**
 * _design/agent-logs.js — Helpers for the agent_logs.json sidecar (DS §7).
 *
 * Sprint 5 lib. Used by per-agent dashboards (broker, curator, librarian,
 * maestro, presto, sage) and by the scheduler dashboard. Provides:
 *
 *   1. A consistent fetcher (correct path, cache-busted)
 *   2. The canonical agent-name filter (DS §7: e.agent_name, NOT e.agent)
 *   3. A relative-time formatter for log timestamps
 *
 * NOT a mandatory replacement for existing inline patterns — provided for new
 * dashboards and as the reference implementation. Existing dashboards may
 * adopt at their next major touch.
 *
 * Public API
 * ----------
 *   await window.AgentLogs.fetch()
 *     → { events: [...], scheduled_jobs: [...], schema_version: '2', generated_at: ... }
 *     Throws on network error; resolves with empty events on missing file.
 *
 *   window.AgentLogs.filterByAgent(events, agentName)
 *     Canonical filter: events.filter(e => e.agent_name === agentName)
 *     For Maestro's fallback chain (multi-source), use the inline pattern.
 *
 *   window.AgentLogs.filterByLevel(events, level)
 *     level is 'info' | 'warn' | 'error' | 'debug' or null (all).
 *
 *   window.AgentLogs.formatTimestamp(ts)
 *     Returns relative ("3 min ago") for <24h, else ISO date.
 *     ts may be unix-seconds, unix-millis, or ISO string.
 *
 *   window.AgentLogs.formatAbsolute(ts)
 *     Returns "2026-05-25 14:32:18" local time.
 *
 * Integration
 * -----------
 *   <script src="/_dashboards/_design/agent-logs.js"></script>
 *
 * Audit trail
 * -----------
 *   1.0.0 (2026-05-25) initial. Sprint 5 lib. DS §7 schema-v2-aware.
 */
(function () {
  'use strict';

  const SIDECAR_PATH = '/_dashboards/_design/agent_logs.json';

  async function fetchLogs() {
    const res = await fetch(SIDECAR_PATH + '?_=' + Date.now(), { cache: 'no-store' });
    if (!res.ok) {
      if (res.status === 404) return { events: [], scheduled_jobs: [], schema_version: '0' };
      throw new Error('agent_logs fetch failed: ' + res.status);
    }
    const data = await res.json();
    return {
      events: Array.isArray(data.events) ? data.events : [],
      scheduled_jobs: Array.isArray(data.scheduled_jobs) ? data.scheduled_jobs : [],
      schema_version: data.schema_version || '1',
      generated_at: data.generated_at || null,
    };
  }

  function filterByAgent(events, agentName) {
    if (!Array.isArray(events) || !agentName) return [];
    return events.filter((e) => e && e.agent_name === agentName);
  }

  function filterByLevel(events, level) {
    if (!Array.isArray(events)) return [];
    if (!level) return events;
    return events.filter((e) => e && e.level === level);
  }

  function toMillis(ts) {
    if (typeof ts === 'number') {
      // Heuristic: <1e12 → seconds, else millis
      return ts < 1e12 ? ts * 1000 : ts;
    }
    if (typeof ts === 'string') {
      const n = Date.parse(ts);
      return isNaN(n) ? Date.now() : n;
    }
    return Date.now();
  }

  function formatTimestamp(ts) {
    const ms = toMillis(ts);
    const diff = Date.now() - ms;
    if (diff < 0) return 'in the future';
    const s = Math.floor(diff / 1000);
    if (s < 60) return s + ' sec ago';
    const m = Math.floor(s / 60);
    if (m < 60) return m + ' min ago';
    const h = Math.floor(m / 60);
    if (h < 24) return h + ' hr ago';
    return formatAbsolute(ms);
  }

  function formatAbsolute(ts) {
    const ms = toMillis(ts);
    const d = new Date(ms);
    const pad = (n) => String(n).padStart(2, '0');
    return `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())} ${pad(d.getHours())}:${pad(d.getMinutes())}:${pad(d.getSeconds())}`;
  }

  window.AgentLogs = {
    fetch: fetchLogs,
    filterByAgent,
    filterByLevel,
    formatTimestamp,
    formatAbsolute,
  };
})();
