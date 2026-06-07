#!/usr/bin/env node
// =============================================================================
// _dashboards/_design/lint.mjs — Dashboard convention checker
// =============================================================================
// Zero-dependency Node script. Validates dashboards against ARCHITECTURE.md +
// DESIGN_SYSTEM.md rules. Output: human-readable (default) or JSON (--json).
//
// Usage:
//   node _dashboards/_design/lint.mjs                  # lint all dashboards
//   node _dashboards/_design/lint.mjs team.html         # lint one file
//   node _dashboards/_design/lint.mjs broker/index.html # lint one (subdir)
//   node _dashboards/_design/lint.mjs --strict          # warnings become errors
//   node _dashboards/_design/lint.mjs --json            # JSON output
//   node _dashboards/_design/lint.mjs --quiet           # only show problems
//
// Exit codes:
//   0 = all green (or only warnings without --strict)
//   1 = errors found (or warnings with --strict)
//   2 = invalid invocation
//
// Sprint 0 baseline (2026-05-25). Update rules as Sprint 1-5 land.
// =============================================================================

import { readFile, readdir, stat } from 'node:fs/promises';
import { join, dirname, basename, relative } from 'node:path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const DASHBOARDS_DIR = dirname(__dirname); // _design/.. = _dashboards/

// ── arg parsing ──────────────────────────────────────────────────────────────
const args = process.argv.slice(2);
const flags = new Set(args.filter(a => a.startsWith('--')));
const positional = args.filter(a => !a.startsWith('--'));
const STRICT = flags.has('--strict');
const JSON_OUT = flags.has('--json');
const QUIET = flags.has('--quiet');

// ── helpers ──────────────────────────────────────────────────────────────────
const ANSI = {
  reset: '\x1b[0m', dim: '\x1b[2m', bold: '\x1b[1m',
  red: '\x1b[31m', yellow: '\x1b[33m', green: '\x1b[32m', cyan: '\x1b[36m',
};
const c = (color, s) => JSON_OUT ? s : `${ANSI[color]}${s}${ANSI.reset}`;

/** Find all dashboard HTML files: top-level *.html + <subdir>/index.html */
async function findDashboards() {
  const out = [];
  const entries = await readdir(DASHBOARDS_DIR, { withFileTypes: true });
  for (const e of entries) {
    if (e.name.startsWith('_') || e.name.startsWith('.')) continue;
    if (e.isFile() && e.name.endsWith('.html')) {
      out.push(e.name);
    } else if (e.isDirectory()) {
      try {
        const sub = join(DASHBOARDS_DIR, e.name, 'index.html');
        await stat(sub);
        out.push(`${e.name}/index.html`);
      } catch { /* no index.html in this subdir */ }
    }
  }
  return out.sort();
}

// ── rule definitions ─────────────────────────────────────────────────────────
// Each rule: { id, severity: 'error'|'warning'|'info', desc, check(html, ctx) }
// check returns null (pass) or { msg, line? }

const RULES = [
  // ── A. HTML SHELL ───────────────────────────────────────────────────────
  {
    id: 'A1-doctype',
    severity: 'error',
    desc: '<!DOCTYPE html> must be first line',
    check: (html) => html.trimStart().startsWith('<!DOCTYPE html>') ? null
      : { msg: '<!DOCTYPE html> missing or not at top' },
  },
  {
    id: 'A2-audit-trail-comment',
    severity: 'error',
    desc: 'HTML header comment with "Version: x.y.z" and "Audit trail:" present',
    check: (html) => {
      // Find the first HTML comment (typically the file header); no size limit
      const headerMatch = html.match(/<!--[\s\S]*?-->/);
      if (!headerMatch) return { msg: 'no HTML comment header found' };
      const h = headerMatch[0];
      if (!/Version:\s*\d+\.\d+\.\d+/.test(h)) return { msg: 'header missing "Version: x.y.z"' };
      if (!/Audit trail:/i.test(h)) return { msg: 'header missing "Audit trail:" section' };
      return null;
    },
  },
  {
    id: 'A3-lang-attr',
    severity: 'warning',
    desc: '<html lang="..."> attribute set',
    check: (html) => /<html\s+lang=["'][a-z-]+["']/i.test(html) ? null
      : { msg: '<html> missing lang attribute' },
  },
  {
    id: 'A4-charset',
    severity: 'error',
    desc: '<meta charset="UTF-8"> in <head>',
    check: (html) => /<meta\s+charset=["']?utf-?8["']?/i.test(html) ? null
      : { msg: 'meta charset UTF-8 missing' },
  },
  {
    id: 'A5-viewport',
    severity: 'warning',
    desc: '<meta name="viewport"> in <head>',
    check: (html) => /<meta\s+name=["']viewport["']/i.test(html) ? null
      : { msg: 'meta viewport missing' },
  },
  {
    id: 'A6-title',
    severity: 'error',
    desc: '<title> non-empty',
    check: (html) => {
      const m = html.match(/<title>\s*([^<]+?)\s*<\/title>/i);
      return (m && m[1].trim().length > 0) ? null : { msg: '<title> missing or empty' };
    },
  },
  {
    id: 'A7-fouc-init',
    severity: 'error',
    desc: 'FOUC-preventing theme-init <script> in <head> (DS §1b)',
    check: (html) => {
      // Look for the canonical pattern inside <head>
      const headMatch = html.match(/<head[^>]*>([\s\S]*?)<\/head>/i);
      if (!headMatch) return { msg: '<head> not found' };
      const head = headMatch[1];
      const hasIIFE = /localStorage\.getItem\(['"]dash-theme['"]\)/.test(head)
                   && /document\.documentElement\.dataset\.theme\s*=/.test(head);
      return hasIIFE ? null : { msg: 'FOUC-init script missing in <head> (must read dash-theme + set documentElement.dataset.theme before paint)' };
    },
  },

  // ── B. TOKENS ───────────────────────────────────────────────────────────
  {
    id: 'B1-tokens-present',
    severity: 'error',
    desc: ':root design tokens present (inline OR via /_design/tokens.css)',
    check: (html) => {
      const hasInline = /:root\s*{[^}]*--bg-page\s*:/.test(html);
      const hasLink = /<link[^>]+href=["'][^"']*_design\/tokens\.css/.test(html);
      return (hasInline || hasLink) ? null
        : { msg: 'no :root --bg-page token block AND no tokens.css link — at least one required' };
    },
  },
  {
    id: 'B2-dark-tokens-present',
    severity: 'error',
    desc: ':root[data-theme="dark"] override present (inline OR via tokens.css)',
    check: (html) => {
      const hasInline = /:root\[data-theme=["']dark["']\]/.test(html);
      const hasLink = /<link[^>]+href=["'][^"']*_design\/tokens\.css/.test(html);
      return (hasInline || hasLink) ? null
        : { msg: 'no dark-theme override AND no tokens.css link' };
    },
  },
  {
    id: 'B3-no-custom-hex-in-css',
    severity: 'warning',
    desc: 'no custom hex colors outside :root token blocks',
    check: (html) => {
      // Extract <style> blocks
      const styles = [...html.matchAll(/<style[^>]*>([\s\S]*?)<\/style>/gi)].map(m => m[1]);
      if (!styles.length) return null;
      // Strip :root { ... } blocks and @media blocks containing :root
      const stripped = styles.map(s => {
        return s
          .replace(/:root[^{]*{[^}]*}/g, '')
          .replace(/@media[^{]*{\s*:root[^{]*{[^}]*}\s*}/g, '');
      }).join('\n');
      // Find non-token hex usage (3, 6, or 8 digit hex)
      const hexes = [...stripped.matchAll(/#[0-9a-fA-F]{3,8}\b/g)]
        .map(m => m[0])
        .filter(h => h.length === 4 || h.length === 7 || h.length === 9);
      // Allow some grey/black/white-ish defaults that may appear in rgba() animations etc
      const suspicious = hexes.filter(h => !/^#(fff|000|FFF|000000|ffffff)$/.test(h));
      if (suspicious.length === 0) return null;
      const unique = [...new Set(suspicious)].slice(0, 6);
      return { msg: `${suspicious.length} custom hex(es) outside :root: ${unique.join(', ')}${suspicious.length > 6 ? ', ...' : ''}` };
    },
  },

  // ── C. SHELL COMPONENTS ─────────────────────────────────────────────────
  {
    id: 'C1-home-link',
    severity: 'error',
    desc: 'home-link with href="/_dashboards/index.html" (absolute)',
    check: (html, ctx) => {
      // Launcher itself (index.html) is exempt
      if (ctx.relpath === 'index.html') return null;
      const hasLink = /<a[^>]+class=["'][^"']*\bhome-link\b[^"']*["'][^>]+href=["']\/_dashboards\/index\.html["']/i.test(html)
                   || /<a[^>]+href=["']\/_dashboards\/index\.html["'][^>]+class=["'][^"']*\bhome-link\b/i.test(html);
      return hasLink ? null
        : { msg: 'home-link missing or href is not absolute /_dashboards/index.html' };
    },
  },
  {
    id: 'C2-theme-toggle',
    severity: 'error',
    desc: '.theme-toggle button with id="themeToggle" present',
    check: (html) => /<button[^>]+id=["']themeToggle["']/.test(html) ? null
      : { msg: '<button id="themeToggle"> missing' },
  },
  {
    id: 'C3-version-pill',
    severity: 'warning',
    desc: '.version-pill present',
    check: (html) => /class=["'][^"']*\bversion-pill\b/.test(html) ? null
      : { msg: '.version-pill not found in markup' },
  },
  {
    id: 'C4-admin-bar-mount',
    severity: 'error',
    desc: 'admin-bar mount point: #bdos-admin-bar (or legacy #bdos-ops-header)',
    check: (html) => {
      const hasNew = /id=["']bdos-admin-bar["']/.test(html);
      const hasLegacy = /id=["']bdos-ops-header["']/.test(html);
      if (hasNew) return null;
      if (hasLegacy) return { msg: 'using legacy #bdos-ops-header — migrate to #bdos-admin-bar (DS 0.6.0)' };
      return { msg: '#bdos-admin-bar div missing (admin-bar.js needs mount point)' };
    },
  },
  {
    id: 'C5-admin-bar-script',
    severity: 'error',
    desc: '<script src="...admin-bar.js"> included',
    check: (html) => /<script\s+src=["'][^"']*_design\/admin-bar\.js["']/.test(html) ? null
      : { msg: 'admin-bar.js script tag missing' },
  },

  // ── D. THEME / CLIPBOARD HELPERS ────────────────────────────────────────
  {
    id: 'D1-setTheme-defined',
    severity: 'error',
    desc: 'setTheme available: inline definition OR <script src="...theme.js"> OR ESM import',
    check: (html) => {
      const hasInline = /function\s+setTheme\s*\(/.test(html);
      const hasScript = /<script\s+src=["'][^"']*_design\/theme\.js["']/.test(html);
      const hasImport = /from\s+["'][^"']*_design\/theme\.js["']/.test(html);
      return (hasInline || hasScript || hasImport) ? null
        : { msg: 'setTheme not defined inline AND theme.js not loaded (no <script src> or import)' };
    },
  },
  {
    id: 'D2-copyText-defined',
    severity: 'warning',
    desc: 'copyText available if any copy-ref/copyable in markup (inline OR clipboard.js)',
    check: (html) => {
      const needsCopy = /class=["'][^"']*\b(card-copy-ref|chip-copyable|invocation-row)\b/.test(html);
      if (!needsCopy) return null;
      const hasInline = /function\s+copyText\s*\(/.test(html);
      const hasScript = /<script\s+src=["'][^"']*_design\/clipboard\.js["']/.test(html);
      const hasImport = /from\s+["'][^"']*_design\/clipboard\.js["']/.test(html);
      return (hasInline || hasScript || hasImport) ? null
        : { msg: 'copyable element present but copyText not defined inline AND clipboard.js not loaded' };
    },
  },
  {
    id: 'D3-DASH_STEM',
    severity: 'warning',
    desc: 'const DASH_STEM defined (required for card-copy-ref)',
    check: (html) => {
      const needs = /class=["'][^"']*\bcard-copy-ref\b/.test(html);
      if (!needs) return null;
      return /\bDASH_STEM\s*=\s*['"`]/.test(html) ? null
        : { msg: 'card-copy-ref present but const DASH_STEM not defined' };
    },
  },

  // ── E. LIVE UPDATES ─────────────────────────────────────────────────────
  {
    id: 'E1-no-direct-eventsource',
    severity: 'warning',
    desc: 'no direct new EventSource(...) — use LiveUpdates.subscribe()',
    check: (html, ctx) => {
      // live-updates.js itself is the shared lib — skip
      if (ctx.relpath === '_design/live-updates.js') return null;
      const matches = [...html.matchAll(/new\s+EventSource\s*\(/g)];
      return matches.length === 0 ? null
        : { msg: `${matches.length} direct EventSource(...) — should use LiveUpdates.subscribe() from /_design/live-updates.js` };
    },
  },
  {
    id: 'E2-no-bare-setInterval-polling',
    severity: 'info',
    desc: 'no bare setInterval(fn, 8000)-style data polling',
    check: (html) => {
      // Match setInterval with intervals 5000-30000 (likely poll loops); allow live-updates.js patterns
      const matches = [...html.matchAll(/setInterval\s*\([^,]+,\s*(\d{4,5})\s*\)/g)]
        .filter(m => {
          const ms = parseInt(m[1], 10);
          return ms >= 5000 && ms <= 30000;
        });
      return matches.length === 0 ? null
        : { msg: `${matches.length} setInterval(${matches.map(m => m[1]).join(', ')}ms) call(s) — should use LiveUpdates.subscribe() (poll is now fallback-only)` };
    },
  },

  // ── F. CARD-COPY-REF ────────────────────────────────────────────────────
  {
    id: 'F1-card-copy-ref-has-data-card-id',
    severity: 'info',
    desc: 'if .card-copy-ref present, data-card-id referenced somewhere',
    check: (html) => {
      const hasCopyRef = /class=["'][^"']*\bcard-copy-ref\b/.test(html);
      if (!hasCopyRef) return null;
      return /data-card-id/.test(html) ? null
        : { msg: '.card-copy-ref present but no data-card-id attribute found — copy refs will silently fail' };
    },
  },
  {
    id: 'F2-card-classes-have-data-card-id',
    severity: 'warning',
    desc: 'every CSS .x-card class that is RENDERED (in HTML or JS) carries data-card-id (DS §4a)',
    check: (html) => {
      // 1. Find all CSS class definitions ending in -card or matching a card-like pattern.
      //    e.g. `.agent-node-card {`, `.stat-card {`, `.detail-card {`, `.vendor {` (skip non-card-named)
      //    We focus on `.[name]-card { ... }` declarations to avoid noise.
      const cssDecls = [...html.matchAll(/\.([\w-]+-card)\b\s*[,{:]/g)].map(m => m[1]);
      const cardClasses = [...new Set(cssDecls)];
      if (cardClasses.length === 0) return null;

      const problems = [];
      for (const cls of cardClasses) {
        // Skip the shared helper class itself
        if (cls === 'card-copy-ref' || cls === 'card-link' || cls === 'card-num' || cls === 'card-date' ||
            cls === 'card-head' || cls === 'card-host' || cls === 'card-host-label' || cls === 'card-scripture' ||
            cls === 'card-speaker' || cls === 'card-links') continue;

        // Find each USE-SITE: either `class="...<cls>..."` in HTML or `className = '...<cls>...'` in JS or
        // `className: ... <cls>` in template strings.
        const useRe = new RegExp(
          '(?:class=["\'][^"\']*\\b' + cls + '\\b[^"\']*["\']|' +
          'className\\s*=\\s*["\'][^"\']*\\b' + cls + '\\b|' +
          'className\\s*[=+]\\s*["\'][^"\']*\\b' + cls + '\\b|' +
          '\\.className\\s*=\\s*[\'"][^\'"]*\\b' + cls + '\\b)', 'g'
        );
        const uses = [...html.matchAll(useRe)];
        if (uses.length === 0) continue; // CSS defined but never used → not our concern here

        // For each use-site, check whether `data-card-id` appears within ±400 chars OR on the SAME
        // element creation block. Use a wider window since JS may set the attribute on a later line
        // (e.g. card.className = X; card.setAttribute('data-card-id', ...)).
        let missing = 0;
        for (const u of uses) {
          const window_ = html.slice(Math.max(0, u.index - 200), u.index + 600);
          if (!/data-card-id|setAttribute\(\s*['"]data-card-id/.test(window_)) {
            missing++;
          }
        }
        if (missing > 0) problems.push(`.${cls} (${missing}/${uses.length} use-sites)`);
      }
      return problems.length === 0 ? null
        : { msg: `${problems.length} card-class(es) used without nearby data-card-id: ${problems.join(', ')}` };
    },
  },

  // ── G. SIDECAR / AGENT_NAME ─────────────────────────────────────────────
  {
    id: 'G1-agent-name-field',
    severity: 'warning',
    desc: 'sidecar filter uses e.agent_name (not e.agent) — DS §7',
    check: (html) => {
      // Look for agent filter expressions
      if (!/agent_logs\.json/.test(html)) return null; // not an agent dashboard
      // Bad pattern: e.agent === or .agent === without _name
      const badMatches = [...html.matchAll(/\.\s*agent\s*===/g)];
      // Filter out e.agent_name === matches
      const trulyBad = badMatches.filter(m => {
        const before = html.slice(Math.max(0, m.index - 40), m.index);
        return !/agent_name/.test(before + html.slice(m.index, m.index + 20));
      });
      if (trulyBad.length === 0) return null;
      return { msg: `${trulyBad.length} use(s) of e.agent === (legacy field) — must be e.agent_name === (DS §7, schema v1.2+)` };
    },
  },

  // ── H. ANTI-PATTERNS ────────────────────────────────────────────────────
  {
    id: 'H1-no-build-step',
    severity: 'error',
    desc: 'no build-step markers (webpack, vite, tsx, etc.)',
    check: (html) => {
      const bad = [];
      if (/<script[^>]+type=["']text\/jsx["']/.test(html)) bad.push('JSX script type');
      if (/<script[^>]+src=["'][^"']*\.tsx?["']/.test(html)) bad.push('TS/TSX script src');
      if (/<script[^>]+src=["'][^"']*\/node_modules\//.test(html)) bad.push('node_modules/ script src');
      return bad.length === 0 ? null : { msg: `build-step marker(s): ${bad.join(', ')}` };
    },
  },
  {
    id: 'H2-no-cdn-frameworks',
    severity: 'warning',
    desc: 'no React/Vue/etc CDN script tags (zero-build rule)',
    check: (html) => {
      const bad = [...html.matchAll(/<script[^>]+src=["']([^"']*(react|vue|angular|jquery|svelte|lodash|moment)[^"']*)["']/gi)]
        .map(m => m[1]);
      return bad.length === 0 ? null
        : { msg: `framework CDN script(s) — vault is zero-build: ${bad.slice(0, 3).join(', ')}${bad.length > 3 ? ', ...' : ''}` };
    },
  },
  {
    id: 'H3-no-fetch-POST',
    severity: 'warning',
    desc: 'no fetch(..., {method: "POST"|"PUT"|"DELETE"}) — dashboards are read-only',
    check: (html) => {
      const matches = [...html.matchAll(/method\s*:\s*['"](POST|PUT|DELETE|PATCH)['"]/gi)];
      return matches.length === 0 ? null
        : { msg: `${matches.length} write-method fetch call(s) — dashboards are read-only (edit markdown directly)` };
    },
  },

  // ── I. VERSION CONSISTENCY ──────────────────────────────────────────────
  {
    id: 'I1-version-pill-matches-comment',
    severity: 'warning',
    desc: 'version-pill text matches HTML comment "Version: x.y.z"',
    check: (html) => {
      const commentMatch = html.match(/Version:\s*(\d+\.\d+\.\d+)/);
      if (!commentMatch) return null; // already caught by A2
      const commentVersion = commentMatch[1];
      // Find .version-pill content
      const pillMatch = html.match(/class=["'][^"']*\bversion-pill\b[^"']*["'][^>]*>([^<]+)</);
      if (!pillMatch) return null; // already caught by C3
      const pillText = pillMatch[1].replace(/[^\d.]/g, '');
      // Pill might have multiple x.y.z patterns; check if comment version present
      return pillText.includes(commentVersion) ? null
        : { msg: `version-pill shows "${pillMatch[1].trim()}" but HTML comment says Version ${commentVersion}` };
    },
  },
];

// ── runner ───────────────────────────────────────────────────────────────────
async function lintFile(relpath) {
  const fullpath = join(DASHBOARDS_DIR, relpath);
  let html;
  try {
    html = await readFile(fullpath, 'utf8');
  } catch (e) {
    return { relpath, error: `cannot read: ${e.message}`, results: [] };
  }
  const ctx = { relpath, fullpath };
  const results = [];
  for (const rule of RULES) {
    try {
      const r = rule.check(html, ctx);
      if (r) {
        results.push({
          id: rule.id,
          severity: rule.severity,
          desc: rule.desc,
          ...r,
        });
      }
    } catch (e) {
      results.push({ id: rule.id, severity: 'error', desc: rule.desc, msg: `rule crashed: ${e.message}` });
    }
  }
  return { relpath, results };
}

function summarize(fileResults) {
  let errors = 0, warnings = 0, infos = 0;
  for (const fr of fileResults) {
    for (const r of fr.results) {
      if (r.severity === 'error') errors++;
      else if (r.severity === 'warning') warnings++;
      else infos++;
    }
  }
  return { errors, warnings, infos, files: fileResults.length };
}

function printHumanReport(fileResults, summary) {
  for (const fr of fileResults) {
    if (fr.error) {
      console.log(`${c('red', '✗')} ${c('bold', fr.relpath)} — ${fr.error}`);
      continue;
    }
    if (fr.results.length === 0) {
      if (!QUIET) console.log(`${c('green', '✓')} ${fr.relpath}`);
      continue;
    }
    console.log(`${c('red', '✗')} ${c('bold', fr.relpath)} — ${fr.results.length} issue(s)`);
    for (const r of fr.results) {
      const icon = r.severity === 'error' ? c('red', '  ✗')
                 : r.severity === 'warning' ? c('yellow', '  ⚠')
                 : c('cyan', '  ℹ');
      console.log(`${icon} [${r.id}] ${r.msg}`);
      if (!QUIET) console.log(`    ${c('dim', r.desc)}`);
    }
  }
  console.log();
  const verdict = summary.errors > 0 ? c('red', '✗ FAIL')
                : (STRICT && summary.warnings > 0) ? c('red', '✗ FAIL (strict)')
                : c('green', '✓ PASS');
  console.log(`${verdict} — ${summary.files} file(s) · ${c('red', summary.errors + ' error')} · ${c('yellow', summary.warnings + ' warning')} · ${c('cyan', summary.infos + ' info')}`);
}

// ── main ─────────────────────────────────────────────────────────────────────
async function main() {
  let targets;
  if (positional.length > 0) {
    targets = positional;
  } else {
    targets = await findDashboards();
  }

  if (targets.length === 0) {
    console.error('No dashboards found.');
    process.exit(2);
  }

  const fileResults = [];
  for (const t of targets) {
    fileResults.push(await lintFile(t));
  }

  const summary = summarize(fileResults);

  if (JSON_OUT) {
    console.log(JSON.stringify({ summary, files: fileResults }, null, 2));
  } else {
    printHumanReport(fileResults, summary);
  }

  const fail = summary.errors > 0 || (STRICT && summary.warnings > 0);
  process.exit(fail ? 1 : 0);
}

main().catch(e => {
  console.error('lint.mjs crashed:', e);
  process.exit(2);
});
