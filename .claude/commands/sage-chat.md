---
description: Sage CHAT mode — interaktív beszélgetés a tudásbázisról mély vault kontextussal (Librarian retrieve). Edit/refine confirmation kötelező.
id: 5b9611f3-8ab6-4217-8659-6f1b5db9262b
index_schema_version: 1
---

A felhasználó beszélgetni akar a Sage-vel.

**$ARGUMENTS** — opcionális első kérdés. Ha üres, üdvözlő mondat utan vár.

**Tennivaló:**

1. Hívd `subagent_type: sage` (fallback `general-purpose` + chat_persona.md)
2. Paraméterek:
   - `mode: chat`
   - `prompt_file: 00_Prompts/BDOS/agents/sage/prompts/chat_persona.md`
   - `initial_question: <$ARGUMENTS>` ha van
3. Mély kontextus engedélyezve: Sage Librarian-on át teljes vault retrieve-elhet
4. Interaktív session — több kör is lehet
5. **Edit confirmation:** ha Sage note-mutációt javasol, a felhasználó explicit `--confirm` után írhat csak
6. A session vége: rövid összefoglaló (max 5 sor) — mit beszéltetek meg, mi az actionable
