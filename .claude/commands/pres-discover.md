---
description: Presto DISCOVER mode — új platform/community signal-detector. NEM trend-chaser. 4-feltétel-szűrő. Auto-hívhatja Thinking Engine-t. Megerősítés nélkül.
id: bfadbd2e-d4f7-40cb-b328-6f4eab4d0d61
index_schema_version: 1
---

A felhasználó Presto discover módot kér — új audience/platform scanning.

**$ARGUMENTS** — opcionális:
- `--area <name>`
- `--focus emerging-platforms|niche-communities|audience-migration|competitor-channels`

**Tennivaló:**

1. Hívd `subagent_type: presto`
2. Paraméterek: `mode: discover`, `area`, `focus`
3. Presto:
   - Olvas current state-et
   - **Auto-hívhatja a Thinking Engine Orchestrator-t** (Perplexity research, ChatGPT niche-elemzés) — logoltan
   - 4-feltétel-szűrő minden javaslatra:
     1. Audience overlap exists
     2. Strategic relevance
     3. Operational feasibility
     4. Long-term value plausibility
   - Max 3 javaslat — mind 4 feltételt teljesít vagy NINCS javaslat
4. Output mentés: `agents/presto/discovery/<YYYY-MM-DD>_<slug>.md`

**Anti-pattern:** SOHA "TikTok-ra menjünk mert mindenki ott". 4-szűrőnek hibátlanul át kell mennie.

Megerősítés NEM kell.

Lásd: `00_Prompts/BDOS/agents/presto.md` §6.11.
