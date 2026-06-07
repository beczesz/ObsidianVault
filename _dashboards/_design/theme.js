/**
 * _design/theme.js — Canonical day/night theme controller for the dashboard family.
 *
 * Sprint 1 engine-extraction of the inline DS §1c block previously duplicated
 * across all 16 dashboards. Behavior-equivalent to the original; this file
 * is the single source of truth from DS 0.7.0 onward.
 *
 * What this file does
 * -------------------
 *   1. Defines `window.setTheme(t)` — applies a theme, persists, updates the
 *      visible `#themeToggle` button (icon + label + aria-label).
 *   2. Defines `window.initTheme()` — reads persisted (`dash-theme` localStorage
 *      key) or system preference, calls setTheme.
 *   3. On DOMContentLoaded auto-wires:
 *        • initTheme() — boot the theme
 *        • click handler on `#themeToggle`
 *        • storage event for cross-tab/cross-dashboard live sync
 *
 * What this file does NOT do
 * --------------------------
 * The FOUC-preventing inline `<script>` in `<head>` (DS §1b) MUST stay inline
 * in every dashboard — it has to run before paint, before any external script
 * has had a chance to load. This file handles the post-paint state only:
 * button label/icon sync and interaction.
 *
 * Integration (per-dashboard)
 * ---------------------------
 *   <!-- Before </body>, alongside live-updates.js + admin-bar.js: -->
 *   <script src="/_dashboards/_design/theme.js"></script>
 *
 * Public API
 * ----------
 *   window.setTheme('light' | 'dark')      // apply + persist + sync UI
 *   window.initTheme()                      // boot from storage/system
 *
 * Audit trail
 * -----------
 *   1.0.0 (2026-05-25) initial extraction from inline DS §1c block. Sprint 1
 *         engine rollout. Replaces ~14 LOC of inline duplicate code in each
 *         of the 16 dashboards (~224 LOC saved family-wide).
 */
(function () {
  'use strict';

  var STORAGE_KEY = 'dash-theme';

  function setTheme(t) {
    document.documentElement.dataset.theme = t;
    try { localStorage.setItem(STORAGE_KEY, t); } catch (e) { /* private mode */ }
    var btn = document.getElementById('themeToggle');
    if (btn) {
      var icon = btn.querySelector('.theme-icon');
      var label = btn.querySelector('.theme-label');
      if (icon)  icon.textContent  = t === 'dark' ? '☀' : '☾';
      if (label) label.textContent = t === 'dark' ? 'Light' : 'Dark';
      btn.setAttribute('aria-label',
        t === 'dark' ? 'Switch to light theme' : 'Switch to dark theme');
    }
  }

  function initTheme() {
    var t;
    try { t = localStorage.getItem(STORAGE_KEY); } catch (e) { /* ignore */ }
    if (!t) {
      t = (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches)
        ? 'dark' : 'light';
    }
    setTheme(t);
  }

  function wire() {
    var btn = document.getElementById('themeToggle');
    if (btn) {
      btn.addEventListener('click', function () {
        setTheme(document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark');
      });
    }
    // Cross-dashboard live sync (storage events fire in OTHER tabs)
    window.addEventListener('storage', function (e) {
      if (e.key === STORAGE_KEY && e.newValue) setTheme(e.newValue);
    });
    initTheme();
  }

  // Expose globals (parity with admin-bar.js / live-updates.js pattern)
  window.setTheme  = setTheme;
  window.initTheme = initTheme;

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', wire);
  } else {
    wire();
  }
})();
