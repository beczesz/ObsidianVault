---
description: Presto AUDIENCE mode — audience intelligence analízis. Pattern-keresés, NEM csak KPI. Atomic-cross-link kötelező. Megerősítés nélkül.
id: 717d8865-2189-488f-9fcf-ad0cf0a25c0d
index_schema_version: 1
---

A felhasználó Presto audience módot kér — audience-pattern-analízis Sage atomic-cross-link-elve.

**$ARGUMENTS** — opcionális:
- `--area <name>`
- `--period <YYYY-MM|last90d|all-time>` (default: last90d)
- `--dimension narrative|format|tone|platform|timing` (default: all)

**Tennivaló:**

1. Hívd `subagent_type: presto`
2. Paraméterek: `mode: audience`, `area`, `period`, `dimension`
3. Presto:
   - Olvassa minden Results-*.md-t az időszakban
   - **Cross-link minden eredményt vissza a forrás atomic-okra** (kötelező — narratíva-koherencia)
   - Aggregálj atomic-szinten + formátum-szinten + tone-szinten
   - Detektálj drift-et az előző periódushoz képest
4. Output: pattern-tábla + drift-flag-ek

**Anti-pattern:** ne mutass engagement-számot atomic-link nélkül.

Megerősítés NEM kell.

Lásd: `00_Prompts/BDOS/agents/presto.md` §6.10.
