/**
 * _design/markdown-parser.js — Canonical YAML frontmatter parser for the
 * dashboard family.
 *
 * Sprint 3 engine-extraction of the inline `parseYamlFrontmatter()` previously
 * duplicated VERBATIM across the partnerships / team / navigator dashboards
 * (the "canonical 87-line" cluster, normalized hash 41edbbd902e5).
 *
 * Other dashboards (sales, aiops, broker, librarian, presto, sage) have
 * FUNCTIONALLY DIFFERENT inline parsers tuned to their own needs — they are
 * NOT migrated by Sprint 3. Curator /dash-promote workflow will eventually
 * decide on a unified successor.
 *
 * Public API
 * ----------
 *   window.parseYamlFrontmatter(md)
 *     Returns { frontmatter, body } if md starts with `---\n...\n---`,
 *     otherwise null. Frontmatter supports:
 *       - scalars: string, int, float, true, false, null, ~
 *       - quoted strings (single or double)
 *       - inline arrays: [a, b, c]
 *       - block arrays: list of `- item`
 *       - nested objects via indentation
 *       - inline comments stripped (quote-aware)
 *
 * Integration (per-dashboard)
 * ---------------------------
 *   <!-- Before </body>, alongside theme.js / clipboard.js / etc.: -->
 *   <script src="/_dashboards/_design/markdown-parser.js"></script>
 *
 * Audit trail
 * -----------
 *   1.0.0 (2026-05-25) initial extraction from canonical inline block
 *         (partnerships.html / team.html / navigator.html — all 3 verbatim
 *         identical modulo whitespace). Sprint 3 rollout. Behavior-equivalent.
 */
(function () {
  'use strict';

  function parseYamlFrontmatter(md) {
    const m = md.match(/^---\r?\n([\s\S]*?)\r?\n---\r?\n?/);
    if (!m) return null;
    const lines = m[1].split('\n');
    const root = {};
    const stack = [{ indent: -1, container: root, key: null }];

    const stripComment = (line) => {
      let q = null;
      for (let i = 0; i < line.length; i++) {
        const c = line[i];
        if (q) { if (c === q && line[i - 1] !== '\\') q = null; }
        else if (c === '"' || c === "'") q = c;
        else if (c === '#' && (i === 0 || /\s/.test(line[i - 1]))) return line.slice(0, i).replace(/\s+$/, '');
      }
      return line.replace(/\s+$/, '');
    };
    const sv = (raw) => {
      let v = raw.trim();
      if (v === '') return '';
      if (v === 'null' || v === '~') return null;
      if (v === 'true') return true;
      if (v === 'false') return false;
      if ((v.startsWith('"') && v.endsWith('"')) || (v.startsWith("'") && v.endsWith("'"))) return v.slice(1, -1);
      if (v.startsWith('[') && v.endsWith(']')) {
        const inner = v.slice(1, -1).trim();
        return inner ? inner.split(',').map(s => sv(s)) : [];
      }
      if (/^-?\d+$/.test(v)) return parseInt(v, 10);
      if (/^-?\d+\.\d+$/.test(v)) return parseFloat(v);
      return v;
    };

    for (let i = 0; i < lines.length; i++) {
      const raw = lines[i];
      if (!raw || /^\s*$/.test(raw)) continue;
      const nc = stripComment(raw);
      if (!nc.trim()) continue;
      const indent = nc.match(/^(\s*)/)[1].length;
      const trimmed = nc.trim();
      while (stack.length > 1 && indent <= stack[stack.length - 1].indent) stack.pop();
      const top = stack[stack.length - 1];

      if (trimmed.startsWith('- ')) {
        const item = trimmed.slice(2).trim();
        if (!Array.isArray(top.container)) continue;
        if (item.includes(':')) {
          const obj = {};
          top.container.push(obj);
          const ci = item.indexOf(':');
          const k = item.slice(0, ci).trim();
          const val = item.slice(ci + 1).trim();
          if (val !== '') obj[k] = sv(val);
          stack.push({ indent, container: obj, key: null });
        } else {
          top.container.push(sv(item));
        }
        continue;
      }

      const ci = trimmed.indexOf(':');
      if (ci === -1) continue;
      const key = trimmed.slice(0, ci).trim();
      const val = trimmed.slice(ci + 1).trim();
      const parent = top.container;
      if (val === '') {
        let ni = i + 1;
        while (ni < lines.length && /^\s*(#.*)?$/.test(lines[ni])) ni++;
        const nl = lines[ni] || '';
        const nIndent = nl.match(/^(\s*)/)[1].length;
        const nTrim = nl.trim();
        if (nTrim.startsWith('- ') && nIndent > indent) {
          const arr = []; if (Array.isArray(parent)) parent.push(arr); else parent[key] = arr;
          stack.push({ indent, container: arr, key });
        } else if (nIndent > indent && nTrim.includes(':')) {
          const obj = {}; if (Array.isArray(parent)) parent.push(obj); else parent[key] = obj;
          stack.push({ indent, container: obj, key });
        } else {
          if (Array.isArray(parent)) parent.push(null); else parent[key] = null;
        }
      } else {
        const value = sv(val);
        if (Array.isArray(parent)) parent.push({ [key]: value }); else parent[key] = value;
      }
    }
    return { frontmatter: root, body: md.slice(m[0].length) };
  }

  // Expose global (parity with theme.js / clipboard.js / admin-bar.js pattern)
  window.parseYamlFrontmatter = parseYamlFrontmatter;
})();
