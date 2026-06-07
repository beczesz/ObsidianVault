/**
 * alfred-tasks.js  —  Alfred Tasks Sidebar  (DS 0.9.0)
 * =============================================================================
 * Shared helper that mounts a persistent sidebar listing ALL open tasks from
 * Alfred's todos/<scope>.md files. Loaded by every dashboard in the family
 * so the user always sees their live task list alongside each dashboard's own
 * content.
 *
 * Usage (two lines per dashboard):
 *   <aside id="alfred-tasks-sidebar"></aside>   <!-- mount point -->
 *   <script src="/_dashboards/_design/alfred-tasks.js"></script>
 *
 * The host dashboard MUST also wrap its existing content in a .app-main element
 * inside a .app-shell flex wrapper (the outer .app container is replaced by
 * .app-shell, which contains .app-main and the sidebar).
 *
 * The sidebar auto-bootstraps on DOMContentLoaded. It re-fetches every 30 s
 * (relaxes to SSE-push if live-updates.js is loaded: listens for the
 * 'alfred-tasks:refresh' custom event that live-updates.js dispatches when
 * a vault-update event arrives).
 *
 * Dependencies (already present in every dashboard):
 *   - /_dashboards/_design/tokens.css  (CSS custom props)
 *   - /_dashboards/_design/dom-utils.js  (escapeHtml, toSlug)
 *   - /_dashboards/_design/clipboard.js  (wireCopyRef — called after render)
 *   No dependency on markdown-parser.js (tasks use a dedicated parser below).
 *
 * Version: 1.0.0
 * =============================================================================
 */
(function () {
  'use strict';

  /* ------------------------------------------------------------------
   * Config — Alfred data sources (canonical, matches alfred/index.html)
   * ------------------------------------------------------------------ */
  var TODOS_BASE = '/02_Areas/Personal Growth/Alfred/todos/';
  var TODO_SCOPES = [
    { scope: 'personal',   label: 'Személyes',   file: TODOS_BASE + 'personal.md'   },
    { scope: 'family',     label: 'Családi',      file: TODOS_BASE + 'family.md'     },
    { scope: 'cps',        label: 'CPS',          file: TODOS_BASE + 'cps.md'        },
    { scope: 'navigator',  label: 'Navigátor',    file: TODOS_BASE + 'navigator.md'  },
    { scope: 'exarlabs',   label: 'ExarLabs',     file: TODOS_BASE + 'exarlabs.md'   },
    { scope: 'fokuszpont', label: 'Fókuszpont',   file: TODOS_BASE + 'fokuszpont.md' },
  ];

  /* ------------------------------------------------------------------
   * Internals
   * ------------------------------------------------------------------ */
  var _pollTimer = null;
  var _POLL_INTERVAL_MS = 30000;

  function _fetchSoft(url) {
    return fetch(url, { cache: 'no-store' })
      .then(function (r) { return r.ok ? r.text() : ''; })
      .catch(function () { return ''; });
  }

  function _stripFrontmatter(md) {
    if (!md) return '';
    var m = md.match(/^---\n[\s\S]*?\n---\n?/);
    return m ? md.slice(m[0].length) : md;
  }

  function _getSection(body, heading) {
    if (!body) return '';
    var lines = body.split('\n'), out = [], capturing = false;
    for (var i = 0; i < lines.length; i++) {
      var h = lines[i].match(/^##\s+(.*)$/);
      if (h) {
        if (capturing) break;
        if (h[1].trim().toLowerCase().indexOf(heading.toLowerCase()) === 0) capturing = true;
        continue;
      }
      if (capturing) out.push(lines[i]);
    }
    return out.join('\n').trim();
  }

  function _parseTasks(body) {
    var parseLines = function (text) {
      return (text || '').split('\n').map(function (l) { return l.trim(); })
        .map(function (l) { return l.match(/^- \[([ xX])\]\s+(.*)$/); })
        .filter(Boolean)
        .map(function (m) {
          var done = m[1].toLowerCase() === 'x';
          var raw = m[2];
          var dueM = raw.match(/(?:📅\s*|due::\s*)(\d{4}-\d{2}-\d{2})/);
          var due = dueM ? dueM[1] : null;
          var prio = null;
          if (raw.indexOf('⏫') !== -1) prio = 'high';
          else if (raw.indexOf('🔼') !== -1) prio = 'med';
          else if (raw.indexOf('🔽') !== -1 || raw.indexOf('⏬') !== -1) prio = 'low';
          var text = raw
            .replace(/📅\s*\d{4}-\d{2}-\d{2}/g, '')
            .replace(/\(?due::\s*\d{4}-\d{2}-\d{2}\)?/g, '')
            .replace(/[⏫🔼🔽⏬]/g, '')
            .replace(/#[^\s#]+/g, '')
            .replace(/\s{2,}/g, ' ').trim();
          return { done: done, text: text, due: due, prio: prio };
        });
    };
    return {
      active: parseLines(_getSection(body, 'Active')),
      archiveCount: parseLines(_getSection(body, 'Archive')).length
    };
  }

  function _dueState(dateStr) {
    if (!dateStr) return { cls: 'none', label: '' };
    var today = new Date(); today.setHours(0, 0, 0, 0);
    var d = new Date(dateStr + 'T00:00:00');
    if (isNaN(d.getTime())) return { cls: 'none', label: dateStr };
    var days = Math.round((d - today) / 86400000);
    if (days < 0) return { cls: 'overdue', label: '' + (-days) + 'n lejárt' };
    if (days === 0) return { cls: 'today', label: 'ma' };
    if (days <= 7) return { cls: 'soon', label: days + 'n' };
    return { cls: 'planned', label: dateStr.slice(5) }; // MM-DD
  }

  /* ------------------------------------------------------------------
   * Render
   * ------------------------------------------------------------------ */
  function _render(scopeResults) {
    var el = document.getElementById('alfred-tasks-sidebar');
    if (!el) return;

    // Flatten all open tasks
    var allOpen = [];
    scopeResults.forEach(function (s) {
      if (!s.tasks) return;
      s.tasks.active.forEach(function (t) {
        if (!t.done) allOpen.push({ scope: s.scope, label: s.label, task: t });
      });
    });

    // Sort: overdue first, then today, then soon, then planned, then none
    var order = { overdue: 0, today: 1, soon: 2, planned: 3, none: 4 };
    allOpen.sort(function (a, b) {
      var da = _dueState(a.task.due), db = _dueState(b.task.due);
      return (order[da.cls] || 4) - (order[db.cls] || 4);
    });

    var total = allOpen.length;
    var esc = typeof escapeHtml === 'function' ? escapeHtml : function (s) {
      return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
    };
    var slug = typeof toSlug === 'function' ? toSlug : function (s) {
      return String(s).toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
    };

    var prioLabel = { high: '⬆', med: '↑', low: '↓' };

    var rows = allOpen.map(function (item) {
      var ds = _dueState(item.task.due);
      var dueHtml = ds.cls !== 'none' && ds.label
        ? '<span class="ats-due ats-due--' + ds.cls + '">' + esc(ds.label) + '</span>'
        : '';
      var prioHtml = item.task.prio
        ? '<span class="ats-prio ats-prio--' + item.task.prio + '">' + prioLabel[item.task.prio] + '</span>'
        : '';
      var cardId = 'ats/' + item.scope + '/' + slug(item.task.text.slice(0, 40) || 'task');
      return '<div class="ats-row" data-card-id="' + cardId + '" tabindex="0">'
        + '<button class="card-copy-ref" aria-label="Kártya-azonosító másolása" data-for-card onclick="event.stopPropagation()">'
        + '<svg width="9" height="9" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>'
        + 'ref</button>'
        + '<div class="ats-row-body">'
        + '<div class="ats-scope-badge">' + esc(item.label) + '</div>'
        + '<div class="ats-text">' + esc(item.task.text) + '</div>'
        + (dueHtml || prioHtml ? '<div class="ats-chips">' + dueHtml + prioHtml + '</div>' : '')
        + '</div>'
        + '</div>';
    }).join('');

    var emptyHtml = '<div class="ats-empty">Minden feladat kész. Remek!</div>';

    el.innerHTML =
      '<div class="ats-header">'
      + '<span class="ats-title">Feladatok</span>'
      + '<span class="ats-count">' + total + '</span>'
      + '<a class="ats-link" href="/_dashboards/alfred/index.html" title="Megnyit Alfred dashboardon">Alfred →</a>'
      + '</div>'
      + '<div class="ats-body">'
      + (total > 0 ? rows : emptyHtml)
      + '</div>';

    if (typeof wireCopyRef === 'function') wireCopyRef(el);
  }

  /* ------------------------------------------------------------------
   * Fetch + refresh
   * ------------------------------------------------------------------ */
  function _refresh() {
    Promise.all(
      TODO_SCOPES.map(function (s) {
        return _fetchSoft(s.file).then(function (md) {
          return {
            scope: s.scope,
            label: s.label,
            tasks: md ? _parseTasks(_stripFrontmatter(md)) : null
          };
        });
      })
    ).then(_render).catch(function (e) {
      var el = document.getElementById('alfred-tasks-sidebar');
      if (el) el.innerHTML = '<div class="ats-empty">Nem sikerült betölteni a feladatokat.</div>';
    });
  }

  /* ------------------------------------------------------------------
   * CSS injection — sidebar layout + component styles
   * Uses DS tokens; no hardcoded hex values outside :root scope.
   * ------------------------------------------------------------------ */
  function _injectStyles() {
    if (document.getElementById('alfred-tasks-sidebar-styles')) return;
    var style = document.createElement('style');
    style.id = 'alfred-tasks-sidebar-styles';
    style.textContent = [
      '/* ===== Alfred Tasks Sidebar — DS 0.9.0 ===== */',

      /* Two-column shell */
      '.app-shell {',
      '  display: flex; align-items: flex-start; gap: 0;',
      '  max-width: 1440px; margin: 0 auto;',
      '}',
      '.app-main {',
      '  flex: 1; min-width: 0;',
      '  max-width: 1200px; padding: 28px 36px 96px;',
      '}',

      /* Sidebar column */
      '#alfred-tasks-sidebar {',
      '  width: 240px; flex-shrink: 0;',
      '  position: sticky; top: calc(34px + 16px);', /* 34px admin-bar + breathing room */
      '  max-height: calc(100vh - 34px - 32px);',
      '  overflow-y: auto;',
      '  padding: 20px 14px 32px;',
      '  border-left: 1px solid var(--line);',
      '  background: var(--bg-page);',
      '  align-self: flex-start;',
      '  scrollbar-width: thin;',
      '  scrollbar-color: var(--line) transparent;',
      '}',

      /* Header row */
      '.ats-header {',
      '  display: flex; align-items: center; gap: 6px;',
      '  margin-bottom: 14px; padding-bottom: 10px;',
      '  border-bottom: 1px solid var(--line);',
      '}',
      '.ats-title {',
      '  font-size: 11px; font-weight: 600; text-transform: uppercase;',
      '  letter-spacing: .08em; color: var(--ink-3);',
      '  flex: 1;',
      '}',
      '.ats-count {',
      '  font-family: "JetBrains Mono", monospace; font-size: 10px; font-weight: 500;',
      '  color: var(--ink-4); background: var(--bg-sunken); border: 1px solid var(--line);',
      '  border-radius: 999px; padding: 1px 7px;',
      '}',
      '.ats-link {',
      '  font-size: 10px; color: var(--accent-deep); font-weight: 500;',
      '  text-decoration: none;',
      '}',
      '.ats-link:hover { text-decoration: underline; }',

      /* Body scroll area */
      '.ats-body { display: flex; flex-direction: column; gap: 6px; }',

      /* Task row */
      '.ats-row {',
      '  position: relative;',
      '  background: var(--bg-elev); border: 1px solid var(--line-soft);',
      '  border-radius: var(--radius-m); padding: 8px 10px;',
      '  cursor: default;',
      '  transition: border-color var(--t-fast), box-shadow var(--t-fast);',
      '}',
      '.ats-row:hover { border-color: var(--line); box-shadow: var(--shadow-1); }',
      '.ats-row:hover .card-copy-ref, .ats-row:focus-within .card-copy-ref { opacity: 1; }',

      '.ats-row-body { display: flex; flex-direction: column; gap: 3px; }',

      '.ats-scope-badge {',
      '  font-size: 9px; font-weight: 600; text-transform: uppercase; letter-spacing: .06em;',
      '  color: var(--ink-4);',
      '}',
      '.ats-text {',
      '  font-size: 12px; color: var(--ink-2); line-height: 1.4;',
      '  word-break: break-word;',
      '}',
      '.ats-chips { display: flex; gap: 4px; flex-wrap: wrap; margin-top: 3px; }',

      /* Due chips */
      '.ats-due {',
      '  font-family: "JetBrains Mono", monospace; font-size: 9px;',
      '  padding: 1px 5px; border-radius: 999px; border: 1px solid var(--line);',
      '  color: var(--ink-3); background: var(--bg-sunken);',
      '}',
      '.ats-due--overdue { color: var(--gap); border-color: rgba(192,57,43,.3); background: var(--gap-tint); }',
      '.ats-due--today { color: var(--accent-deep); border-color: var(--accent); background: var(--accent-tint); }',
      '.ats-due--soon { color: #3d4a63; border-color: #5b6b8c; background: rgba(91,107,140,.1); }',

      /* Prio chips */
      '.ats-prio {',
      '  font-family: "JetBrains Mono", monospace; font-size: 9px; font-weight: 700;',
      '  padding: 1px 5px; border-radius: 999px;',
      '}',
      '.ats-prio--high { color: var(--gap); background: var(--gap-tint); }',
      '.ats-prio--med { color: #3d4a63; background: rgba(91,107,140,.1); }',
      '.ats-prio--low { color: var(--ink-4); background: var(--bg-sunken); }',

      /* Empty state */
      '.ats-empty { font-size: 12px; color: var(--ink-4); text-align: center; padding: 20px 0; }',

      /* ===== Responsive: narrow viewport — sidebar stacks below main ===== */
      '@media (max-width: 900px) {',
      '  .app-shell { flex-direction: column; }',
      '  .app-main { max-width: 100%; padding: 20px 18px 60px; }',
      '  #alfred-tasks-sidebar {',
      '    width: 100%; max-height: none; position: static;',
      '    border-left: none; border-top: 1px solid var(--line);',
      '    padding: 18px 18px 24px;',
      '  }',
      '}',
    ].join('\n');
    document.head.appendChild(style);
  }

  /* ------------------------------------------------------------------
   * Public API
   * ------------------------------------------------------------------ */
  var AlfredTasks = {
    /** Force an immediate re-fetch and re-render. */
    refresh: function () { _refresh(); },

    /** Start the 30 s poll timer (called automatically on boot). */
    startPolling: function () {
      if (_pollTimer) clearInterval(_pollTimer);
      _pollTimer = setInterval(_refresh, _POLL_INTERVAL_MS);
    },

    /** Stop the poll timer. */
    stopPolling: function () {
      if (_pollTimer) { clearInterval(_pollTimer); _pollTimer = null; }
    },

    /** Mount: inject styles, do first fetch, start polling.
     *  Called automatically on DOMContentLoaded. */
    mount: function () {
      _injectStyles();
      _refresh();
      AlfredTasks.startPolling();
      // Relax polling when live-updates.js is running (subscribe to vault-update events)
      document.addEventListener('alfred-tasks:refresh', function () { _refresh(); });
    }
  };

  // Integrate with live-updates.js if present: trigger refresh on vault-update
  // by broadcasting the custom event from within the LiveUpdates callback.
  // Each dashboard's boot code can call:
  //   LiveUpdates.subscribe(function() { document.dispatchEvent(new CustomEvent('alfred-tasks:refresh')); refetchAndRender(); });
  // OR the sidebar simply polls independently (30 s is acceptable for a sidebar).

  document.addEventListener('DOMContentLoaded', function () {
    if (document.getElementById('alfred-tasks-sidebar')) {
      AlfredTasks.mount();
    }
  });

  window.AlfredTasks = AlfredTasks;
})();
