---
description: Alfred STATUS — read-only rendszer-áttekintés: inbox backlog, utolsó sync, nyitott task-szám scope-onként, figyelmeztetések.
id: a1f10004-0000-4c00-8000-000000000004
index_schema_version: 1
---

A felhasználó Alfred státusz-riportot kér.

**$ARGUMENTS** — nincs.

**Tennivaló:**

1. Olvasd `02_Areas/Personal Growth/Alfred/inbox.md` — sorold meg a feldolgozatlan (timestamp utáni, még nem routolt) tételeket.
2. Olvasd `agents/alfred/state/last_run.md` — utolsó sync + harvest időpontja.
3. Olvasd az összes `02_Areas/Personal Growth/Alfred/todos/<scope>.md` — scope-onként nyitott checkbox szám.
4. Output:
   - **Inbox backlog:** X tétel feldolgozatlan (legrégebbi: dátum)
   - **Utolsó sync:** dátum + tétel-szám (vagy "soha" warning)
   - **Utolsó harvest:** dátum (vagy "soha" warning)
   - **Nyitott taskok scope szerint:** tábla (scope | nyitott | lejárt)
   - **Figyelmeztető jelzések:** inbox > 10 tétel, last_run > 48 óra, lejárt task van

**Read-only** — nem módosít semmit. Confirmation nem kell.

Lásd: `00_Prompts/BDOS/agents/alfred.md` §4 `status` mód.
