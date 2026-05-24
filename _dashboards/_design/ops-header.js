/**
 * ops-header.js — BDOS Ops Header  (DS 0.5.0, Phase B, 2026-05-24)
 * =================================================================
 * Renders a slim ops-status strip ABOVE every dashboard masthead.
 * Five status pills (Watchdog · Server · DB · Scheduler · Index),
 * each independently checked every 30 s.
 * A "System" button opens the reusable system-status drawer
 * at /_dashboards/scheduler/index.html (injected as an iframe overlay).
 *
 * Usage (add to every dashboard — injected by promote mode):
 *   <script src="/_dashboards/_design/ops-header.js"></script>
 *   <!-- anywhere in <body>, before other content: -->
 *   <div id="bdos-ops-header"></div>
 *
 * The script mounts itself into #bdos-ops-header.
 * Call OpsHeader.refresh() to force a manual re-check.
 *
 * DS Component: .bdos-ops-header, .ops-pill
 * Design tokens: inherits from dashboard :root — no standalone tokens defined here.
 */

(function() {
  'use strict';

  // ---------------------------------------------------------------------------
  // Configuration
  // ---------------------------------------------------------------------------
  const EVENTS_SERVER = 'http://localhost:4322';
  const DASH_SERVER   = 'http://localhost:4321';
  const SIDECAR_PATH  = '/_dashboards/_design/agent_logs.json';
  const SCHEDULER_URL = '/_dashboards/scheduler/index.html';
  const REFRESH_MS    = 30_000;  // poll every 30 s

  // How old (ms) a scheduler task_started event may be to count as "alive"
  const SCHEDULER_STALE_MS = 5 * 60 * 1000;  // 5 min
  // How old (ms) obs_build_meta index update may be to count as "fresh"
  const INDEX_STALE_MS     = 24 * 60 * 60 * 1000;  // 24 h

  // ---------------------------------------------------------------------------
  // CSS (injected once)
  // ---------------------------------------------------------------------------
  const CSS = `
.bdos-ops-header {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 5px 18px 5px 14px;
  background: var(--bg-sunken, #f3f1ea);
  border-bottom: 1px solid var(--line, #e5e4df);
  font-family: 'JetBrains Mono', 'Fira Mono', monospace;
  font-size: 10.5px;
  font-weight: 500;
  position: sticky;
  top: 0;
  z-index: 900;
  flex-wrap: wrap;
}

.bdos-ops-header .ops-label {
  color: var(--ink-4, #9c9c98);
  font-size: 10px;
  letter-spacing: .08em;
  text-transform: uppercase;
  margin-right: 2px;
  flex-shrink: 0;
}

.ops-pill {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  padding: 2px 8px 2px 6px;
  border-radius: 999px;
  border: 1px solid transparent;
  font-size: 10.5px;
  font-family: inherit;
  font-weight: 500;
  cursor: default;
  transition: background 120ms, border-color 120ms, color 120ms;
  white-space: nowrap;
  user-select: none;
}

.ops-pill .ops-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  flex-shrink: 0;
  transition: background 120ms;
}

.ops-pill.ok    { color: var(--ok, #1f7a4d);   background: var(--ok-tint, #e6f3ec);   border-color: rgba(31,122,77,.2);  }
.ops-pill.ok    .ops-dot { background: var(--ok, #1f7a4d); }

.ops-pill.warn  { color: var(--warn, #b07a18);  background: var(--warn-tint, #fbf2dc); border-color: rgba(176,122,24,.2); }
.ops-pill.warn  .ops-dot { background: var(--warn, #b07a18); }

.ops-pill.gap   { color: var(--gap, #c0392b);   background: var(--gap-tint, #fbeae6);  border-color: rgba(192,57,43,.2);  }
.ops-pill.gap   .ops-dot { background: var(--gap, #c0392b); }

.ops-pill.idle  { color: var(--ink-3, #6d6d6a); background: var(--bg-tint, #f5f4ef);  border-color: var(--line, #e5e4df); }
.ops-pill.idle  .ops-dot { background: var(--ink-4, #9c9c98); }

.bdos-ops-header .ops-spacer {
  flex: 1;
}

.bdos-ops-header .ops-system-btn {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  padding: 3px 10px;
  font-size: 10.5px;
  font-family: inherit;
  font-weight: 500;
  color: var(--ink-3, #6d6d6a);
  background: var(--bg-elev, #fff);
  border: 1px solid var(--line, #e5e4df);
  border-radius: var(--radius-m, 6px);
  cursor: pointer;
  transition: color 120ms, border-color 120ms, background 120ms;
  flex-shrink: 0;
}
.bdos-ops-header .ops-system-btn:hover {
  color: var(--accent-deep, #b35a3f);
  border-color: var(--accent, #D97757);
  background: var(--bg-tint, #f5f4ef);
}

/* Drawer overlay */
#bdos-ops-drawer {
  position: fixed;
  inset: 0;
  z-index: 9000;
  display: none;
  align-items: flex-start;
  justify-content: center;
  padding-top: 40px;
  background: rgba(20,20,19,.45);
  backdrop-filter: blur(3px);
}
#bdos-ops-drawer.open {
  display: flex;
}
#bdos-ops-drawer .drawer-frame {
  width: min(96vw, 1100px);
  height: min(85vh, 860px);
  background: var(--bg-page, #faf9f5);
  border-radius: var(--radius-xl, 14px);
  border: 1px solid var(--line, #e5e4df);
  box-shadow: 0 24px 64px rgba(20,20,19,.22);
  overflow: hidden;
  position: relative;
  display: flex;
  flex-direction: column;
}
#bdos-ops-drawer .drawer-close {
  position: absolute;
  top: 12px; right: 14px;
  width: 28px; height: 28px;
  border-radius: 50%;
  border: 1px solid var(--line, #e5e4df);
  background: var(--bg-elev, #fff);
  cursor: pointer;
  font-size: 14px;
  color: var(--ink-3, #6d6d6a);
  display: flex; align-items: center; justify-content: center;
  z-index: 2;
  transition: background 120ms, border-color 120ms;
}
#bdos-ops-drawer .drawer-close:hover {
  background: var(--gap-tint, #fbeae6);
  border-color: var(--gap, #c0392b);
  color: var(--gap, #c0392b);
}
#bdos-ops-drawer iframe {
  flex: 1;
  border: none;
  width: 100%;
  height: 100%;
}
`;

  // ---------------------------------------------------------------------------
  // State
  // ---------------------------------------------------------------------------
  const state = {
    watchdog:  { status: 'idle', label: 'Watchdog', detail: '' },
    server:    { status: 'idle', label: 'Server',   detail: '' },
    db:        { status: 'idle', label: 'DB',        detail: '' },
    scheduler: { status: 'idle', label: 'Scheduler', detail: '' },
    index:     { status: 'idle', label: 'Index',     detail: '' },
  };

  // ---------------------------------------------------------------------------
  // Check functions
  // ---------------------------------------------------------------------------

  async function checkWatchdog() {
    // Watchdog = events_server /health endpoint (which knows about vault.db)
    try {
      const r = await fetch(EVENTS_SERVER + '/health', { signal: AbortSignal.timeout(4000) });
      const j = await r.json();
      if (j.ok) {
        state.watchdog = { status: 'ok', label: 'Watchdog', detail: `clients:${j.clients}` };
      } else {
        state.watchdog = { status: 'warn', label: 'Watchdog', detail: 'unhealthy' };
      }
    } catch (e) {
      state.watchdog = { status: 'gap', label: 'Watchdog', detail: 'offline' };
    }
  }

  async function checkServer() {
    // Dash-server = port 4321 HEAD /
    try {
      const r = await fetch(DASH_SERVER + '/', {
        method: 'HEAD',
        signal: AbortSignal.timeout(4000),
      });
      state.server = {
        status: r.ok || r.status === 301 || r.status === 302 ? 'ok' : 'warn',
        label: 'Server',
        detail: String(r.status),
      };
    } catch (e) {
      state.server = { status: 'gap', label: 'Server', detail: 'offline' };
    }
  }

  async function checkDB() {
    // DB = sidecar JSON present + generated_at recent
    try {
      const r = await fetch(SIDECAR_PATH + '?_=' + Date.now(), { signal: AbortSignal.timeout(4000) });
      const j = await r.json();
      const ageMs = Date.now() - new Date(j.generated_at).getTime();
      const rows = j.total_rows || 0;
      if (ageMs < 5 * 60 * 1000) {  // freshened within 5 min
        state.db = { status: 'ok', label: 'DB', detail: `${rows} rows` };
      } else {
        state.db = { status: 'warn', label: 'DB', detail: 'stale sidecar' };
      }
    } catch (e) {
      state.db = { status: 'gap', label: 'DB', detail: 'no sidecar' };
    }
  }

  async function checkScheduler() {
    // Scheduler = last agent_logs row with tags includes 'scheduler' within 5 min
    try {
      const r = await fetch(SIDECAR_PATH + '?_=' + Date.now(), { signal: AbortSignal.timeout(4000) });
      const j = await r.json();
      const events = (j.events || []).filter(e => {
        try {
          const tags = typeof e.tags === 'string' ? JSON.parse(e.tags) : (e.tags || []);
          return Array.isArray(tags) && tags.includes('scheduler');
        } catch (_) { return false; }
      });
      if (events.length === 0) {
        state.scheduler = { status: 'idle', label: 'Scheduler', detail: 'no events' };
        return;
      }
      const latest = events[events.length - 1];
      const ageMs  = Date.now() - new Date(latest.timestamp).getTime();
      if (ageMs < SCHEDULER_STALE_MS) {
        state.scheduler = { status: 'ok', label: 'Scheduler', detail: 'active' };
      } else {
        const mins = Math.round(ageMs / 60000);
        state.scheduler = { status: 'warn', label: 'Scheduler', detail: `${mins}m ago` };
      }
    } catch (e) {
      state.scheduler = { status: 'gap', label: 'Scheduler', detail: 'unknown' };
    }
  }

  async function checkIndex() {
    // Index = sidecar generated_at within 24h (proxy for build_meta updated_at)
    try {
      const r = await fetch(SIDECAR_PATH + '?_=' + Date.now(), { signal: AbortSignal.timeout(4000) });
      const j = await r.json();
      const ageMs = Date.now() - new Date(j.generated_at).getTime();
      if (ageMs < INDEX_STALE_MS) {
        state.index = { status: 'ok', label: 'Index', detail: 'fresh' };
      } else {
        const h = Math.round(ageMs / 3600000);
        state.index = { status: 'warn', label: 'Index', detail: `${h}h ago` };
      }
    } catch (e) {
      state.index = { status: 'gap', label: 'Index', detail: 'unknown' };
    }
  }

  // ---------------------------------------------------------------------------
  // Render helpers
  // ---------------------------------------------------------------------------
  function pillHTML(key) {
    const s = state[key];
    const title = s.detail ? `${s.label}: ${s.detail}` : s.label;
    return `<span class="ops-pill ${s.status}" title="${title}" data-pill="${key}">
      <span class="ops-dot"></span>${s.label}${s.detail ? ' <span style="opacity:.65">' + s.detail + '</span>' : ''}
    </span>`;
  }

  function render() {
    const host = document.getElementById('bdos-ops-header');
    if (!host) return;
    host.innerHTML = `
      <span class="ops-label">BDOS</span>
      ${Object.keys(state).map(k => pillHTML(k)).join('')}
      <span class="ops-spacer"></span>
      <button class="ops-system-btn" id="bdos-ops-system-btn" title="Open system status drawer">
        <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14M4.93 4.93a10 10 0 0 0 0 14.14"/></svg>
        System
      </button>
    `;
    // Re-wire system button (re-rendered on every refresh)
    document.getElementById('bdos-ops-system-btn')?.addEventListener('click', openDrawer);
  }

  // ---------------------------------------------------------------------------
  // Drawer
  // ---------------------------------------------------------------------------
  function ensureDrawer() {
    if (document.getElementById('bdos-ops-drawer')) return;
    const el = document.createElement('div');
    el.id = 'bdos-ops-drawer';
    el.innerHTML = `
      <div class="drawer-frame">
        <button class="drawer-close" id="bdos-ops-drawer-close" aria-label="Close system drawer">&#x2715;</button>
        <iframe id="bdos-ops-iframe" src="" title="BDOS System Status"></iframe>
      </div>
    `;
    document.body.appendChild(el);
    el.addEventListener('click', (e) => { if (e.target === el) closeDrawer(); });
    document.getElementById('bdos-ops-drawer-close').addEventListener('click', closeDrawer);
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') closeDrawer();
    });
  }

  function openDrawer() {
    ensureDrawer();
    const drawer = document.getElementById('bdos-ops-drawer');
    const iframe = document.getElementById('bdos-ops-iframe');
    // Load/reload iframe
    iframe.src = SCHEDULER_URL + '?embedded=1&_=' + Date.now();
    drawer.classList.add('open');
    document.body.style.overflow = 'hidden';
  }

  function closeDrawer() {
    const drawer = document.getElementById('bdos-ops-drawer');
    if (!drawer) return;
    drawer.classList.remove('open');
    document.body.style.overflow = '';
    // Unload iframe to stop background fetches
    const iframe = document.getElementById('bdos-ops-iframe');
    if (iframe) iframe.src = '';
  }

  // ---------------------------------------------------------------------------
  // Public refresh
  // ---------------------------------------------------------------------------
  async function refresh() {
    await Promise.allSettled([
      checkWatchdog(),
      checkServer(),
      checkDB(),
      checkScheduler(),
      checkIndex(),
    ]);
    render();
  }

  // ---------------------------------------------------------------------------
  // Mount
  // ---------------------------------------------------------------------------
  function injectCSS() {
    if (document.getElementById('bdos-ops-header-css')) return;
    const s = document.createElement('style');
    s.id = 'bdos-ops-header-css';
    s.textContent = CSS;
    document.head.appendChild(s);
  }

  function mount() {
    injectCSS();
    // Create host element if not present
    let host = document.getElementById('bdos-ops-header');
    if (!host) {
      host = document.createElement('div');
      host.id = 'bdos-ops-header';
      document.body.insertBefore(host, document.body.firstChild);
    }
    // Render placeholder pills immediately
    render();
    // Kick off first real check
    refresh();
    // Schedule periodic refresh
    setInterval(refresh, REFRESH_MS);
  }

  // ---------------------------------------------------------------------------
  // Public API
  // ---------------------------------------------------------------------------
  window.OpsHeader = { mount, refresh, openDrawer, closeDrawer };

  // Auto-mount when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', mount);
  } else {
    mount();
  }

})();
