/**
 * _design/dom-utils.js — Small shared string/DOM helpers.
 *
 * Sprint 5 lib. Provides two helpers that are widely re-implemented inline
 * across the dashboard family. New dashboards should load this file and use
 * the shared globals instead of redefining; existing dashboards keep their
 * inline versions until next touch (mass-migration not warranted for 3-line
 * functions — risk-vs-reward unfavorable, per Sprint 2b/3 lesson).
 *
 * Public API
 * ----------
 *   window.escapeHtml(s) → string
 *     Escapes &, <, >, ", '  for safe interpolation into innerHTML / template
 *     literals. NULL/undefined yield empty string.
 *
 *   window.toSlug(s) → string
 *     Lowercases + replaces non-alphanumeric runs with '-' + trims leading/
 *     trailing dashes. Used for stable card-id values (DS §4a).
 *
 * Integration
 * -----------
 *   <script src="/_dashboards/_design/dom-utils.js"></script>
 *
 * Audit trail
 * -----------
 *   1.0.0 (2026-05-25) initial. Sprint 5 lib for new dashboards + template
 *         scaffold. No family-wide migration (per Sprint 2b/3 risk lesson).
 */
(function () {
  'use strict';

  const ESC = { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' };

  function escapeHtml(s) {
    if (s === null || s === undefined) return '';
    return String(s).replace(/[&<>"']/g, (c) => ESC[c]);
  }

  function toSlug(s) {
    return String(s || '').toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
  }

  window.escapeHtml = escapeHtml;
  window.toSlug = toSlug;
})();
