---
id: claude_cli
title: Claude CLI (Sonnet)
layer: processing
purpose: |
  Az Alfred /api/alfred/process végpont Tier-1 feldolgozó motorja.
  Spawn-ol egy `claude` subprocess-t Sonnet modellel, OAuth tokennel,
  read-only tool-okkal (Read, Glob, Grep) hogy biztonságosan
  válaszoljon vault-szintű kérdésekre vagy task-okat parse-oljon.
inputs:
  - prompt string (HTTP body-ból)
outputs:
  - assistant message (JSON wrap)
depends_on: [oauth_token, vault_md]
fallback_to: haiku_fallback
status_endpoint: /health (component: claude_cli)
index_schema_version: 1
---

## Miért létezik

A Claude CLI az egyetlen módja annak, hogy a felhasználó Claude Code
subscription-jét felhasználja API kulcs nélkül — OAuth token alapon.
A subprocess izolált kontextusban fut: csak read-only tool-ok engedélyezettek
(Read, Glob, Grep), nincs Write, nincs Bash, nincs hálózati hozzáférés.
Ez garantálja, hogy az /api/alfred/process nem tud véletlenül írni a vaultba.

## Tier-1/2/3 architektúra

A BDOS három-rétegű fallback logikával dolgozik:

- **Tier-1 (claude_cli):** Sonnet subprocess + OAuth token. Lassabb (3-10s
  spawn overhead), de a legerősebb modell és nincs API-kulcs kiadás.
- **Tier-2 (haiku_fallback):** Haiku 4.5 REST API + Anthropic API key.
  Gyorsabb, de az API key expozált a szerver env-ben.
- **Tier-3 (capture_fallback):** Nyers inbox append, nincs AI. Garantáltan
  működik, de nincs parse.

## Tipikus hibamódok

- OAuth token lejárt → 401, automatikus fallback Haiku-ra.
- Quota kimerült → rate limit error, ugyanaz a fallback path.
- Subprocess timeout (>30s) → capture-only mode.
- `claude` binary nem elérhető → gap state a /health-ben.

## Kapcsolódó

- [Alfred dashboard](/_dashboards/alfred/index.html)
- [Ad-hoc konzol](/_dashboards/system.html) — System dashboard CLI modal
