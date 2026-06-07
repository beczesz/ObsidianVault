---
description: Alfred CAPTURE — nyers dump az inbox.md-be, strukturálás nélkül. Megerősítés nélkül fut (append-only).
id: a1f10001-0000-4c00-8000-000000000001
index_schema_version: 1
---

A felhasználó gyors raw capture-t kér — valamit be akar dobni az Alfred inbox-ba.

**$ARGUMENTS** — kötelező: szabad szöveges dump (idézőjelben vagy anélkül).

**Tennivaló:**

1. Vedd az `$ARGUMENTS` teljes szövegét mint nyers dump.
2. Timestamp-et generálj (`YYYY-MM-DD HH:MM`) a jelenlegi helyi időből.
3. Fűzd hozzá az `02_Areas/Personal Growth/Alfred/inbox.md` végéhez ebben a formátumban:
   ```
   - [YYYY-MM-DD HH:MM] <dump szövege>
   ```
4. Semmi strukturálás, semmi routing, semmi kérdés. Csak rögzítés.
5. Rövid visszaigazolás: "Rögzítve." + idézd vissza az első ~60 karaktert.

**Confirmation nem kell** — ez append-only, nem-destruktív írás.

Lásd: `00_Prompts/BDOS/agents/alfred.md` §4 `capture` mód.
