---
schema: sage.learning.v1
slug: capability-script-restart-and-smoke-test
type: failure-mode
status: proposed
confidence: high
proposed_at: 2026-05-26T00:00:00+02:00
confirmed_at: null
last_applied_at: null
applications_count: 0
evidence:
  - "2026-05-26 session: Curator beírta a MarketingBoardHook-ot watch_event.py-be, de a futó PID 88534 (Sun06PM óta aktív) nem vette fel — kill + restart kellett, user fedezte fel."
  - "2026-05-26 session: Curator beírta az SSE marketing_board broadcast-ot events_server.py-be, de a futó PID 96200 nem tudta — ismét kill + restart kellett, user fedezte fel."
  - "2026-05-26 session: Curator által írt kódban scoping-bug volt (UnboundLocalError: _clients) — egy minimális smoke-test elkapta volna, de nem futott le. Így néma fail jutott el a user-ig."
retired_at: null
retired_reason: null
id: 3eb6cc23-4a10-4494-861f-e9e708cf600b
index_schema_version: 1
description: Meta-learning a Python long-running daemon scriptek módosítása utáni kötelező restart + smoke-test mintáról. Három független eset alapján azonosított failure-mode, amelyet Curator és bármely más agent követ el, ha daemon-szerű .py fájlt módosít anélkül, hogy a futó folyamatot újraindítaná és az eredményt ellenőrizné.
bdos_index: true
---

## A tanulság

**Python long-running daemon-szerű scriptet (watchdog, events_server, scheduler, stb.) érintő bármely agent-módosítás után KÉT dolgot kell elvégezni — nem opcionálisan, hanem a deliverable részeként:**

### 1. szabály — Restart kötelező

Ha az agent módosít egy `.py` fájlt, ami daemon-ként, watchdog-ként vagy long-running server-ként fut a háttérben, a futó folyamat **nem tölti újra automatikusan a megváltozott kódot** (Python source-reload nincs implicit). A régi PID a memóriában lévő régi kóddal fut tovább.

Az agentnek autonóm módon kell:
1. Azonosítania a futó PID-et (`pgrep -f <script_name>` vagy systemd/launchd).
2. Leállítania a régi folyamatot (`kill <PID>` vagy `pkill -f <script_name>`).
3. Újraindítania a daemon-t (ugyanazzal a paranccsal, amivel eredetileg futott).
4. Verifikálnia, hogy az új PID él és a módosítás aktiválódott (legalább log-sor ellenőrzés vagy health-check endpoint).

**Ne hagyja a user-en hogy észrevegye, hogy a kód futott, de a viselkedés nem változott.**

### 2. szabály — Smoke-test kötelező

Az agentnek nem elég megírni a kódot — egy minimális end-to-end test a deliverable része:

- Trigger a várt esemény (pl. tesztüzenet küldése, fájlmódosítás, HTTP kérés).
- Ellenőrizni a várt output-ot (log-sor, broadcast, state-változás).
- Ha a test hibát jelez (pl. `UnboundLocalError`): a következő turn-ben javítani, nem elrejteni.

A smoke-test az **elfogadás feltétele** — nem opcionális polishing. Cél: néma fail helyett gyors, agent-oldali hibajelzés.

## Mire vonatkozik

Ez a learning elsősorban a **Curator** és **Presto** agentekre vonatkozik (capability-scriptek íróira), de általánosan érvényes bármely BDOS-agenten belül, amely daemon-szerű Python scriptet módosít.

## Hogyan vonom vissza

Ha 4 héten belül ugyanez a mintázat (user fedezi fel a néma daemon-hibát) ismét előfordul, ez a learning kevés — mélyebb eszköz kell (pl. reload-hook a scriptekbe, vagy pre-modifikáció daemon-detekció).

Ha 4 hét után 0 ilyen eset → confirmed.

## Kapcsolódó

- Sage learning `2026-05-24_theme-enumeration-before-selection` — hasonló struktúra: agent-oldali ellenőrzés a deliverable része, ne user-fedezze fel.
- BDOS Phase 2 operational log: `agent_observability.db` — a restart + smoke-test eseményeket érdemes loggolni `tool_call` event típussal.
