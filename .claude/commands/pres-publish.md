---
description: Presto PUBLISH mode — approved publication execution through API→MCP→manual fallback chain. Confirmation kötelező.
id: c7e1a3b2-4d5f-6789-abcd-ef0123456789
index_schema_version: 1
---

A felhasználó Presto publish módot kér — egy jóváhagyott publikáció végrehajtása.

**$ARGUMENTS** — kötelező:
- `--pub <project>/<campaign>/<pub-id>` — a publication azonosítója

**Tennivaló:**

1. Parse $ARGUMENTS, validáld a pub paramétert (létezik-e a PUBLICATION.md)
2. Hívd `subagent_type: presto`
3. Paraméterek: `mode: publish`, `pub`
4. Presto:
   - Olvassa a PUBLICATION.md-t a pub paraméter alapján
   - Olvassa a vonatkozó CHANNEL_DNA.md-t — execution capabilities
   - Fallback chain: API → MCP → manual TODO
   - Logol minden próbálkozást
5. **Confirmation gate KÖTELEZŐ** — bemutatja: publication tartalom + target channel + execution method
6. Frissíti a publication_status-t: publish_pending → published (vagy failed → manual_required)

Lásd: `00_Prompts/BDOS/agents/presto.md` §6.13.
