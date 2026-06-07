---
title: Dashboard lint — pre-commit gates
date: 2026-05-25
author: Becze Szabolcs
status: active
description: Két opcionális pre-commit gate a dashboard linthez. (1) Git pre-commit hook — univerzális, CLI + Obsidian git plugin + bárhol fut. (2) Claude Code stop-hook — csak CC-ben, instant feedback Edit/Write után. Mindkettő opcionális; manuális futtatás (`node lint.mjs`) mindig elérhető marad.
tags: [dashboards, hooks, lint]
id: 32beeea3-ff0e-416b-bed5-9932fe068888
index_schema_version: 1
---

# Pre-commit gates a dashboard lintre

Két opció. **Egyik sem kötelező** — manuális `node _dashboards/_design/lint.mjs` mindig elérhető. De ha automatizálni szeretnéd, válassz:

## A) Git pre-commit hook (ajánlott — univerzális)

Akkor fut, amikor `git commit`-elsz, akár CLI-ből, akár Obsidian git plugin-ból, akár bármi más git-frontend-ből.

**Telepítés:**

```bash
cd "/Users/becze-mac/My Drive (beczesz.szabolcs@gmail.com)/0. Ideas Vault"
ln -s ../../_dashboards/_design/_hooks/pre-commit .git/hooks/pre-commit
```

Vagy ha symlink nem opció (pl. shared repo):

```bash
cp _dashboards/_design/_hooks/pre-commit .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

**Mit csinál:**
- Minden staged `_dashboards/*.html` fájlon lefuttatja a lint-et
- Ha **error** van → commit blokkolva
- **Warning** nem blokkol (default) — `DASH_LINT_STRICT=1 git commit ...` kapcsolja be a strict-et

**Egy commitra kikapcsolni:**
```bash
git commit --no-verify -m "..."
```

## B) Claude Code stop-hook (instant feedback CC-ben)

Akkor fut, amikor a Claude Code Edit/Write-ol egy dashboardot. Real-time visszajelzés sessziónon belül.

**Telepítés:** szerkeszd `.claude/settings.json`-t vagy `.claude/settings.local.json`-t a vault gyökerében. Add hozzá:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "case \"$CLAUDE_TOOL_INPUT_file_path\" in *_dashboards/*.html) cd \"$CLAUDE_PROJECT_DIR\" && node _dashboards/_design/lint.mjs \"${CLAUDE_TOOL_INPUT_file_path#*_dashboards/}\" ;; esac"
          }
        ]
      }
    ]
  }
}
```

(Vagy ennél egyszerűbb: csak `node _dashboards/_design/lint.mjs` ami minden fájlon lint-eli.)

**Mit csinál:** Edit / Write után a dashboard-érintő változtatást azonnal lintoli. Eredmény bekerül a Claude kontextusába (vissza tudja olvasni a warninget és proaktívan reagálni).

## C) Csak manuális (a default)

Egyetlen parancs commit előtt:

```bash
node _dashboards/_design/lint.mjs
```

Bármely opciónál: ha új szabályt kell hozzáadni, edit `_design/lint.mjs` `RULES` array-t.

## Kapcsolódó

- [`../lint.mjs`](../lint.mjs) — a lint engine
- [`../ARCHITECTURE.md`](../ARCHITECTURE.md) §9 — lint szabályok dokumentációja
- [`../../CLAUDE.md`](../../CLAUDE.md) — discovery layer (lintet emlegeti)
