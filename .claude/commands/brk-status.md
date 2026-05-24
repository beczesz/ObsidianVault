---
description: Broker STATUS mode — cross-project sales pipeline áttekintés. Megerősítés nélkül.
id: 938fdcf7-1b95-4e10-b700-6d9c634a91ac
index_schema_version: 1
---

A felhasználó Broker sales-status riportot kér.

**$ARGUMENTS** — opcionális `--area <name>` szűkítés.

**Tennivaló:**

1. Hívd `subagent_type: broker`, mode: `status`, opcionális area
2. Broker olvas: `_dashboards/00_SALES_INDEX.md` (ha nincs, jelez `index` mód javaslatot)
3. Output: tábla Area × Pipeline stage × Lead count × Stalled count × Next action

Lásd: `00_Prompts/BDOS/agents/broker.md` §4.1.
