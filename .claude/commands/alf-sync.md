---
description: Alfred SYNC — ops-harvest (ChatGPT "Alfred Inbox" Chrome MCP) + inbox triázs + routing-javaslat. Confirmation-gate kötelező minden mutáció előtt.
id: a1f10002-0000-4c00-8000-000000000002
index_schema_version: 1
---

A felhasználó Alfred sync-rituálét kér — az ops inbox feldolgozása, routing-javaslat, confirmation-gate.

**$ARGUMENTS** — opcionális: `--skip-mcp` (csak vault inbox.md, ne harvestelj Chrome MCP-vel).

**Tennivaló:**

1. Olvasd `02_Areas/Personal Growth/Alfred/inbox.md` (vault-side inbox).
2. Ha nincs `--skip-mcp` flag: Chrome MCP-vel olvasd a ChatGPT "Alfred Inbox" chat legújabb üzeneteit (lásd alfred.md §3 ops-harvest csatorna).
3. Gyűjtsd össze az utolsó-sync-óta beérkezett tételeket.
4. Minden tételre triázsolj: kategória (idea / todo / reminder / family / priority / mood / insight) + javasolt routing (personal TODO / Presto-signal / Broker-signal / archív / egyéb).
5. **Mutasd a routing-terveket** egy áttekintő listában. Kérd confirmation-t: "Ezekkel a routingokkal haladok — mehet?"
6. Confirmation után hajtsd végre: írj TODO-kat, signalokat, archivált tételeket (a megerősített routingok szerint).
7. Frissítsd `agents/alfred/state/last_run.md` sync-riporttal.
8. Logolj (`routes/YYYY-MM.md` audit-trail + Logging §8 szerint).

**Csend default** — csak akkor notify, ha döntést igényel vagy mintát észleltél.

Lásd: `00_Prompts/BDOS/agents/alfred.md` §3 + §4 `sync` mód.
