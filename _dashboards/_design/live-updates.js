/**
 * live-updates.js — DS 0.4.0
 * ============================================================
 * Shared event-driven live-update helper for the _dashboards/ family.
 * Imported by every dashboard via <script src="/_dashboards/_design/live-updates.js"></script>
 *
 * Usage:
 *   LiveUpdates.subscribe(refetchAndRender);   // call your data-load function
 *
 * Architecture:
 *   Primary:  SSE EventSource → http://localhost:4322/events  (vault.db mtime watcher)
 *   Fallback: setInterval(8000) polling — activates automatically if SSE fails to
 *             connect within 3 seconds (e.g. events_server.py not running, or
 *             opened via file:// without dash-server).
 *
 * Status indicator:
 *   Call LiveUpdates.mountStatusIndicator(containerEl) to inject the pill into
 *   any element. The indicator auto-updates its visual state as SSE connects/drops.
 *   Colors: green (active), amber (polling fallback), red (error/disconnected).
 *
 * Exports (via window.LiveUpdates):
 *   subscribe(callback)                — register a refetch callback
 *   mountStatusIndicator(el)           — inject status pill into el
 *   getState()                         → 'connecting'|'active'|'polling'|'error'
 *
 * Version history:
 *   0.4.0 (2026-05-24) initial — promote: event-driven SSE family-wide.
 * ============================================================
 */
(function(global) {
  'use strict';

  const SSE_URL    = 'http://localhost:4322/events';
  const FALLBACK_INTERVAL = 8000;   // ms — polling fallback interval
  const SSE_TIMEOUT_MS    = 3000;   // ms — wait for SSE before activating fallback
  const HEARTBEAT_STALE_MS = 60000; // ms — >60s since last event → show stale

  let _callbacks = [];
  let _state = 'connecting'; // 'connecting'|'active'|'polling'|'error'
  let _lastEventTs = 0;
  let _pollTimer = null;
  let _evtSrc = null;
  let _sseTimeout = null;
  let _statusEls = []; // mounted indicator elements

  // ---- internal helpers ----

  function _setState(s) {
    if (_state === s) return;
    _state = s;
    _updateAllIndicators();
  }

  function _trigger() {
    _lastEventTs = Date.now();
    _setState('active');
    _callbacks.forEach(function(cb) {
      try { cb(); } catch(e) { console.warn('[live-updates] callback error', e); }
    });
  }

  function _startFallbackPolling() {
    if (_pollTimer) return; // already polling
    _setState('polling');
    _pollTimer = setInterval(function() {
      _lastEventTs = Date.now();
      _callbacks.forEach(function(cb) {
        try { cb(); } catch(e) {}
      });
    }, FALLBACK_INTERVAL);
  }

  function _stopFallbackPolling() {
    if (_pollTimer) { clearInterval(_pollTimer); _pollTimer = null; }
  }

  function _connectSSE() {
    if (typeof EventSource === 'undefined') {
      _startFallbackPolling();
      return;
    }
    _setState('connecting');

    // If SSE hasn't opened in SSE_TIMEOUT_MS, activate fallback polling
    _sseTimeout = setTimeout(function() {
      if (_state === 'connecting') {
        _startFallbackPolling();
      }
    }, SSE_TIMEOUT_MS);

    try {
      _evtSrc = new EventSource(SSE_URL);

      _evtSrc.addEventListener('message', function(ev) {
        clearTimeout(_sseTimeout);
        _stopFallbackPolling();
        try {
          var data = JSON.parse(ev.data);
          if (data.type === 'vault-update') {
            _trigger();
          }
        } catch(e) {}
      });

      _evtSrc.onopen = function() {
        clearTimeout(_sseTimeout);
        _stopFallbackPolling();
        _setState('active');
        _lastEventTs = Date.now();
      };

      _evtSrc.onerror = function() {
        _setState('error');
        // EventSource will auto-retry via the retry: 3000 directive
        // Give it one cycle before activating fallback
        clearTimeout(_sseTimeout);
        _sseTimeout = setTimeout(function() {
          if (_state === 'error' || _state === 'connecting') {
            _startFallbackPolling();
          }
        }, SSE_TIMEOUT_MS);
      };
    } catch(e) {
      clearTimeout(_sseTimeout);
      _startFallbackPolling();
    }
  }

  // ---- Status indicator ----

  var _css = [
    '.lu-pill{display:inline-flex;align-items:center;gap:5px;font-size:11px;font-weight:500;',
    'padding:3px 9px;border-radius:999px;border:1px solid var(--line,#e5e4df);',
    'background:var(--bg-elev,#fff);color:var(--ink-3,#6d6d6a);',
    'font-family:"JetBrains Mono",monospace;white-space:nowrap;cursor:default;',
    'transition:background 120ms,color 120ms,border-color 120ms;}',
    '.lu-pill:hover{border-color:var(--accent,#D97757);}',
    '.lu-dot{width:7px;height:7px;border-radius:50%;flex-shrink:0;transition:background 120ms;}',
    '.lu-pill[data-state="active"] .lu-dot{background:#1f7a4d;}',
    '.lu-pill[data-state="active"]{color:var(--ok,#1f7a4d);border-color:rgba(31,122,77,.25);background:var(--ok-tint,#e6f3ec);}',
    '.lu-pill[data-state="polling"] .lu-dot{background:#b07a18;}',
    '.lu-pill[data-state="polling"]{color:var(--warn,#b07a18);border-color:rgba(176,122,24,.25);background:var(--warn-tint,#fbf2dc);}',
    '.lu-pill[data-state="connecting"] .lu-dot{background:#9c9c98;animation:lu-blink 1.2s ease-in-out infinite;}',
    '.lu-pill[data-state="error"] .lu-dot{background:#c0392b;}',
    '.lu-pill[data-state="error"]{color:var(--gap,#c0392b);border-color:rgba(192,57,43,.25);background:var(--gap-tint,#fbeae6);}',
    '@keyframes lu-blink{0%,100%{opacity:1}50%{opacity:.35}}',
    /* modal */
    '.lu-modal-scrim{position:fixed;inset:0;background:rgba(20,20,19,.45);z-index:9998;display:flex;align-items:center;justify-content:center;}',
    '.lu-modal{background:var(--bg-elev,#fff);border:1px solid var(--line,#e5e4df);border-radius:12px;padding:24px 28px;max-width:400px;width:90%;box-shadow:0 8px 32px rgba(20,20,19,.14);z-index:9999;position:relative;}',
    '.lu-modal h3{font-size:15px;font-weight:600;margin-bottom:10px;color:var(--ink-1,#141413);}',
    '.lu-modal p{font-size:13px;color:var(--ink-2,#3a3a37);line-height:1.55;margin-bottom:8px;}',
    '.lu-modal code{font-family:"JetBrains Mono",monospace;font-size:11.5px;background:var(--bg-sunken,#f3f1ea);padding:2px 6px;border-radius:4px;}',
    '.lu-modal-close{position:absolute;top:12px;right:14px;font-size:18px;cursor:pointer;color:var(--ink-4,#9c9c98);background:none;border:none;line-height:1;}',
  ].join('');

  var _styleInjected = false;
  function _injectStyle() {
    if (_styleInjected) return;
    _styleInjected = true;
    var s = document.createElement('style');
    s.textContent = _css;
    document.head.appendChild(s);
  }

  function _stateLabel(s) {
    if (s === 'active')     return 'live';
    if (s === 'polling')    return 'polling';
    if (s === 'connecting') return 'connecting';
    return 'offline';
  }

  function _tooltipText(s) {
    var ago = _lastEventTs ? Math.round((Date.now() - _lastEventTs) / 1000) + 's ago' : 'never';
    var engine = s === 'active' ? 'SSE (event-driven)' :
                 s === 'polling' ? '8s poll (fallback — events_server.py not running)' :
                 s === 'connecting' ? 'connecting to events_server.py…' :
                 'disconnected';
    return 'Engine: ' + engine + ' · Last update: ' + ago + ' · State: ' + s;
  }

  function _updateAllIndicators() {
    _statusEls.forEach(function(el) { _updateIndicator(el); });
  }

  function _updateIndicator(pill) {
    if (!pill) return;
    pill.setAttribute('data-state', _state);
    pill.title = _tooltipText(_state);
    var lbl = pill.querySelector('.lu-label');
    if (lbl) lbl.textContent = _stateLabel(_state);
    var dot = pill.querySelector('.lu-dot');
    // dot color is CSS-driven via data-state
  }

  function _showModal() {
    _injectStyle();
    var scrim = document.createElement('div');
    scrim.className = 'lu-modal-scrim';
    scrim.innerHTML = [
      '<div class="lu-modal" role="dialog" aria-modal="true" aria-label="Live updates info">',
      '<button class="lu-modal-close" aria-label="Close">&times;</button>',
      '<h3>Live Update Engine</h3>',
      '<p>The dashboard family uses <strong>event-driven live updates</strong> via <code>events_server.py</code> — a tiny SSE server that watches the vault SQLite index (<code>vault.db</code>) for changes.</p>',
      '<p>When the vault watcher (<code>watch_event.py</code>, powered by watchdog 6.x) indexes new markdown, <code>vault.db</code> is updated, and the events server pushes a <code>vault-update</code> event to all connected dashboards — sub-second latency.</p>',
      '<p>To start the watcher + events server:</p>',
      '<p><code>cd 00_Prompts/BDOS/capabilities/vault-indexing &amp;&amp; ./start.sh</code></p>',
      '<p>If the events server is not running, dashboards fall back to <strong>8-second polling</strong> automatically. The status pill in the header shows the current mode.</p>',
      '<p><strong>Status colors:</strong> green = event-stream active &nbsp;·&nbsp; amber = polling fallback &nbsp;·&nbsp; red = error/offline</p>',
      '</div>'
    ].join('');
    document.body.appendChild(scrim);
    scrim.querySelector('.lu-modal-close').onclick = function() { document.body.removeChild(scrim); };
    scrim.onclick = function(e) { if (e.target === scrim) document.body.removeChild(scrim); };
    document.addEventListener('keydown', function esc(e) {
      if (e.key === 'Escape') { document.body.removeChild(scrim); document.removeEventListener('keydown', esc); }
    });
  }

  // ---- Public API ----

  function subscribe(callback) {
    if (typeof callback === 'function') _callbacks.push(callback);
  }

  function mountStatusIndicator(containerEl) {
    if (!containerEl) return;
    _injectStyle();
    var pill = document.createElement('button');
    pill.className = 'lu-pill';
    pill.setAttribute('data-state', _state);
    pill.title = _tooltipText(_state);
    pill.setAttribute('aria-label', 'Live update status — click for details');
    pill.innerHTML = '<span class="lu-dot"></span><span class="lu-label">' + _stateLabel(_state) + '</span>';
    pill.onclick = _showModal;
    containerEl.appendChild(pill);
    _statusEls.push(pill);
    return pill;
  }

  function getState() { return _state; }

  // ---- Boot ----
  _connectSSE();

  // Expose
  global.LiveUpdates = { subscribe: subscribe, mountStatusIndicator: mountStatusIndicator, getState: getState };

}(window));
