---
description: Sage STATUS mode — last_run.md emberi olvasású összefoglalása. Megerősítés nélkül.
id: 4b7318c5-daa8-4712-97ee-6125d1e1d9bc
index_schema_version: 1
---

A felhasználó Sage állapot-riportot kér.

**Tennivaló:**

1. Olvasd be: `00_Prompts/BDOS/agents/sage/state/last_run.md`
2. Olvasd be: `00_Prompts/BDOS/agents/sage/state/last_seen.md` (utolsó feldolgozott ChatGPT üzenet)
3. Olvasd be: `00_Prompts/BDOS/agents/sage/learnings/00_INDEX.md` (learning counts)
4. Glob: `02_Areas/Personal Growth/Ideas/_inbox/**/*.md` (mennyi user-review vár)
5. Glob: `02_Areas/Personal Growth/Ideas/thoughts/*.md` + `atomic/*.md` (totals)

Adj vissza egy emberi, rövid (max 15 sor) riportot:
- mikor futott utoljára daily / weekly
- hány új gondolat / atomic / inbox-tétel
- aktív learningek száma
- ha bármi piros (errors, várakozó user-review > 5, never_run > 24h) — emeld ki

Ne hívd Sage agentet — ez puszta read-only riport.
