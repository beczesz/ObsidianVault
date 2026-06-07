/**
 * _design/clipboard.js — Canonical clipboard helpers for the dashboard family.
 *
 * Sprint 1 engine-extraction of the inline DS §4a clipboard block previously
 * duplicated across 15 of 16 dashboards. Behavior-equivalent to the original;
 * this file is the single source of truth from DS 0.7.0 onward.
 *
 * What this file provides
 * -----------------------
 *   • window.copyText(text, el)
 *       Copy `text` to clipboard via navigator.clipboard.writeText; on failure
 *       falls back to the textarea + document.execCommand('copy') trick.
 *       Adds `.copied` class to `el` for 1.6 s as visual feedback.
 *
 *   • window.wireCopyRef(containerEl)
 *       Find all `.card-copy-ref` buttons inside containerEl, attach click
 *       handler that stops propagation (critical — never trigger the card's
 *       own navigation) and copies `DASH_STEM + ':' + card.dataset.cardId`.
 *
 *   • window.wirePanelAnchors()   [DS 0.8.10]
 *       Attach copy-on-click behavior to every `.panel-anchor` element on
 *       the page. On primary click (no modifier): copies the relative deep-
 *       link path (pathname + hash, NO origin) to the clipboard and shows
 *       "✓" for 1.5 s then restores the original "#N" text. Does NOT update
 *       the browser hash and does NOT scroll — purely a clipboard write.
 *       Example copied value: /_dashboards/presto/index.html#panel-4-campaigns
 *       Middle-click / Cmd+click / Ctrl+click / Shift+click pass through
 *       untouched so the browser's native "open in new tab" behavior is
 *       preserved.
 *       Auto-mounted on DOMContentLoaded — no per-dashboard call needed.
 *       A11y: aria-label="Másolás vágólapra" and title="Másolás vágólapra"
 *       are set on every anchor at wire time.
 *
 * Requirements per-dashboard
 * --------------------------
 *   const DASH_STEM = '<stem>';   // must be defined before wireCopyRef runs;
 *                                 // typically the HTML filename without
 *                                 // extension (e.g. 'partnerships', 'team').
 *                                 // window.DASH_STEM also accepted.
 *
 *   wirePanelAnchors() — NO per-dashboard call required. Auto-mounts on
 *                        DOMContentLoaded. The inline wirePanelAnchors()
 *                        definition and boot call should be removed from
 *                        dashboard HTML.
 *
 * Integration
 * -----------
 *   <!-- Before </body>, alongside theme.js + live-updates.js + admin-bar.js: -->
 *   <script src="/_dashboards/_design/clipboard.js"></script>
 *
 *   // After dynamic render (e.g. building card grid from fetched data):
 *   wireCopyRef(gridEl);
 *
 * No auto-wiring of wireCopyRef on DOMContentLoaded — cards are usually
 * rendered after fetch, so dashboards must call `wireCopyRef(...)` explicitly
 * after each render. This is consistent with the existing pattern and avoids
 * surprising double-wires. (`wireCopyRef` uses `.onclick = ...` assignment,
 * so manual re-wires are safe.)
 *
 * wirePanelAnchors() IS auto-wired on DOMContentLoaded because panel anchors
 * are static markup (not dynamically rendered after fetch).
 *
 * Audit trail
 * -----------
 *   1.1.1 (2026-05-25) TEND DS 0.8.10: wirePanelAnchors() copy formula changed
 *         to relative path+hash only (pathname + href, no origin) — avoids
 *         port-dependent dead links when pasted in a different context. Primary
 *         click now ONLY writes to clipboard — no hash update, no scrollIntoView,
 *         no navigation. A11y: title + aria-label updated to "Másolás vágólapra".
 *   1.1.0 (2026-05-25) PROMOTE DS 0.8.9: wirePanelAnchors() extracted from 8
 *         inline dashboard definitions. Adds modifier-key pass-through (middle/
 *         Cmd/Ctrl/Shift+click open natively), a11y attributes, and auto-mount
 *         on DOMContentLoaded. Removes ~30 LOC × 8 dashboards (~240 LOC saved).
 *   1.0.0 (2026-05-25) initial extraction from inline DS §4a block. Sprint 1
 *         engine rollout. Replaces ~26 LOC of inline duplicate code in each
 *         of 15 dashboards (~405 LOC saved family-wide).
 */
(function () {
  'use strict';

  function copyText(text, el) {
    function flash() {
      if (!el || !el.classList) return;
      el.classList.add('copied');
      setTimeout(function () { el.classList.remove('copied'); }, 1600);
    }

    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(flash).catch(fallback);
    } else {
      fallback();
    }

    function fallback() {
      var ta = document.createElement('textarea');
      ta.value = text;
      ta.style.position = 'fixed';
      ta.style.opacity = '0';
      document.body.appendChild(ta);
      ta.select();
      try { document.execCommand('copy'); } catch (e) { /* ignore */ }
      document.body.removeChild(ta);
      flash();
    }
  }

  function wireCopyRef(containerEl) {
    if (!containerEl || !containerEl.querySelectorAll) return;
    var stem = (typeof DASH_STEM !== 'undefined') ? DASH_STEM : window.DASH_STEM;
    if (!stem) {
      console.warn('[clipboard.js] DASH_STEM is not defined — copy-ref buttons will not work.');
      return;
    }
    containerEl.querySelectorAll('.card-copy-ref').forEach(function (btn) {
      btn.onclick = function (e) {
        e.stopPropagation(); // never trigger card navigation
        var card = btn.closest('[data-card-id]');
        if (!card) return;
        copyText(stem + ':' + card.dataset.cardId, btn);
      };
    });
  }

  /* ===== Panel Anchor Clipboard (DS 0.8.10) ===== */
  /* Intercepts primary clicks on every .panel-anchor element.
   * Primary click (no modifier): ONLY copies the relative path+hash to the
   * clipboard — no hash update, no scroll, no navigation.
   * Middle-click / Cmd+click / Ctrl+click / Shift+click pass through so the
   * browser's native "open in new tab" / "open in new window" behavior works. */
  function wirePanelAnchors() {
    document.querySelectorAll('.panel-anchor').forEach(function (anchor) {
      // Set a11y attributes at wire time
      anchor.setAttribute('aria-label', 'Másolás vágólapra');
      anchor.setAttribute('title', 'Másolás vágólapra');

      anchor.addEventListener('click', function (e) {
        // Pass through modifier clicks (Cmd/Ctrl/Meta/Shift) and middle-button
        if (e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) {
          return; // let the browser handle it natively
        }
        e.preventDefault();

        // Copy relative path + hash only — no origin (avoids port-dependent dead links)
        var href = this.getAttribute('href') || '';
        var url  = location.pathname + href;

        // Clipboard + visual feedback only — no hash update, no scroll
        var original = this.textContent;
        var btn = this;
        function showCheck() {
          btn.textContent = '✓';
          setTimeout(function () { btn.textContent = original; }, 1500);
        }

        if (navigator.clipboard && navigator.clipboard.writeText) {
          navigator.clipboard.writeText(url).then(showCheck).catch(function () {
            clipboardFallback(url);
            showCheck();
          });
        } else {
          clipboardFallback(url);
          showCheck();
        }
      });
    });
  }

  function clipboardFallback(text) {
    var ta = document.createElement('textarea');
    ta.value = text;
    ta.style.position = 'fixed';
    ta.style.opacity  = '0';
    document.body.appendChild(ta);
    ta.select();
    try { document.execCommand('copy'); } catch (e) { /* ignore */ }
    document.body.removeChild(ta);
  }

  // Auto-mount panel anchors on DOMContentLoaded (static markup — safe to wire early)
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', wirePanelAnchors);
  } else {
    wirePanelAnchors(); // already parsed
  }

  // Expose globals (parity with admin-bar.js / live-updates.js / theme.js)
  window.copyText         = copyText;
  window.wireCopyRef      = wireCopyRef;
  window.wirePanelAnchors = wirePanelAnchors;
})();
