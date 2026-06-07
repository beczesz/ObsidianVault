---
id: ep_process
title: /api/alfred/process
layer: server
purpose: |
  Az Alfred "intelligens capture" végpontja. A beérkező szöveget átadja
  a Claude CLI (Tier-1) vagy Haiku API (Tier-2) feldolgozónak, amely
  scope-ot, prioritást és határidőt nyer ki, majd a megfelelő
  todos/<scope>.md fájlba írja taskként.
depends_on: [server, claude_cli]
status_endpoint: /health (component: ep_process)
index_schema_version: 1
---

## Miért létezik

A nyers capture szövegből automatikusan strukturált task-ot gyártani
megkönnyíti az Alfred workflow-t — a felhasználónak nem kell gondolkodnia
a formátumon, elég begépelni a gondolatot.

## Feldolgozási lépések

1. HTTP POST body JSON: `{"message": "Holnap reggel 9-re emlékezz a call-ra"}`
2. Az endpoint spawn-ol egy `claude` subprocess-t (Tier-1) vagy Haiku API hívást (Tier-2)
3. Az AI kinyeri: scope (personal/family/work/bdos), priority, due date
4. A task bekerül a `todos/<scope>.md` megfelelő szekciójába
5. Válasz: `{"ok": true, "task": {...}, "tier": "claude_cli"}`

## Hibamódok

- Claude CLI timeout (>30s) → Haiku fallback
- Haiku API fail → capture fallback (inbox.md append)
- Mindkettő fail → HTTP 503

## Kapcsolódó komponensek

- `claude_cli` — Tier-1 feldolgozó
- `haiku_fallback` — Tier-2 fallback
- `capture_fallback` — Tier-3 inbox append
