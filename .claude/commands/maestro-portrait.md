---
description: Maestro PORTRAIT mode — Pixar-stílusú robot profil-prompt egy BDOS agenthez. `list` mód a kész portrékhoz, `propose --agent <name>` új agent prompt-jához. Skill: maestro-agent-portrait.
id: f9e2c4a7-3b8d-4516-bc92-1a7e6f8c3d4b
index_schema_version: 1
bdos_index: true
---

A felhasználó Pixar-stílusú robot profil-képet szeretne generálni egy BDOS agenthez (egy létezőnek vagy újnak).

**$ARGUMENTS** — opcionális:
- `list` — összes meglevő portré-prompt listázása
- `<agent-name>` — adott agent prompt-jának kiadása (pl. `librarian`, `maestro`, `presto`)
- `propose --agent <name>` — új agent prompt-jának generálása a kanonikus agent-definíció alapján

**Tennivaló:**

1. Olvasd be a skill specifikációt: `00_Prompts/BDOS/agents/maestro/skills/agent-portrait/SKILL.md`
2. Olvasd be az universal style template-et: `00_Prompts/BDOS/agents/maestro/skills/agent-portrait/style-template.md`

3. **Ha `$ARGUMENTS == "list"`:**
   - Listázd ki a `portraits/` mappa fájljait
   - Minden fájl frontmatter `agent` + `description` mezőjéből építs egy 1-soros összegzést
   - Output: táblázat, fájl-link kattintható

4. **Ha `$ARGUMENTS == <existing-agent-name>` (pl. `librarian`):**
   - Nyisd meg `portraits/<name>.md`-t
   - Output: a Final Prompt block (a copy-paste szöveg) + identity-mapping táblázat
   - Mondd, hogy paste-elheti ChatGPT / DALL-E / Midjourney-be

5. **Ha `$ARGUMENTS startswith "propose"`:**
   - Parse-old: `--agent <name>` kötelező
   - Olvasd be a kanonikus agent-definíciót: `00_Prompts/BDOS/agents/<name>.md`
   - Extract:
     - `description` field (one-line identity)
     - "Identity" / "Mission" szekciók (mit csinál)
     - Bármilyen vizuális hint (pl. "magus", "scholar", "blacksmith")
   - Töltsd ki a 7 per-agent variable-t (`agent_role`, `color_signature`, `prop`, `pose`, `ambient_motif`, `eye_expression`, `material_note`)
   - Generálj egy Final Prompt block-ot a `_template.md` sablon szerint
   - **Confirmation gate KÖTELEZŐ** — mutasd a javaslatot, kérdezd: "Mentem `portraits/<name>.md`-be?"
   - Igen után: írd a fájlt, frissítsd a SKILL.md "Files" listáját

6. **Ha `$ARGUMENTS` üres:**
   - Mutasd a használat helpet (a fenti 4 lehetőséget) + a `list` output-ot

**Constraints:**
- Soha NE töröld a meglevő portré-promptokat — csak új-et hozz létre vagy meglevőt módosíts confirmation-nel
- A family-coherence checklist-et (style-template.md végén) mindig add a propose-output-hoz
- Ne találj ki agentet — ha nincs `00_Prompts/BDOS/agents/<name>.md`, jelezd: "Ehhez az agenthez nincs kanonikus definíció, először scaffold-old `/maestro-team-introduce`-mal"

Lásd: `00_Prompts/BDOS/agents/maestro/skills/agent-portrait/SKILL.md`.
