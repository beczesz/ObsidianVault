---
id: haiku_fallback
title: Haiku fallback
layer: processing
purpose: |
  Tier-2 feldolgozó: Anthropic Haiku 4.5 REST API hívás, amelyet az
  ep_process végpont akkor aktivál, ha a Tier-1 (claude_cli) OAuth
  tokenje érvénytelen, lejárt vagy a subprocess timeout-olt.
  Gyorsabb mint a CLI spawn, de API key-t igényel.
depends_on: [capture_fallback]
fallback_to: capture_fallback
status_endpoint: /health (component: haiku_fallback)
index_schema_version: 1
---

## Miért létezik

A két-rétegű fallback (Tier-1 → Tier-2 → Tier-3) robusztussá teszi
az Alfred capture flow-t: még ha a primary Claude CLI nem elérhető
(OAuth lejárt, hálózati hiba), a Haiku API átveszi a feladatot és
elvégzi a task parse-t.

## Konfiguráció

```bash
# ~/.bdos/anthropic.env
ANTHROPIC_API_KEY=sk-ant-...
```

A dash-server betölti ezt az env fájlt induláskor. Ha hiányzik vagy üres,
a haiku_fallback `idle` státuszba kerül (nem hiba, csak nem konfigurált).

## Mikor aktiválódik

- claude_cli → 401 (OAuth expired)
- claude_cli → rate limit / quota
- claude_cli → timeout (>30s)

## Teljesítmény

A Haiku API ~500ms-1s latenciával válaszol, szemben a Claude CLI
3-10s spawn overhead-jével. A minőség alacsonyabb (Haiku vs Sonnet),
de task parse-ra elegendő.
