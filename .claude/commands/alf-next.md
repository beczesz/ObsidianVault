---
description: Alfred NEXT — "van valamilyen feladatom?" A legmagasabb prioritású előkészített dossziét riportként mutatja: mi volt a feladat, hogyan próbálta megoldani (agent-timeline + draft), hol tartunk + mihez kell döntés. Read-only, megerősítés nélkül fut.
id: 37b319ef-c79c-4a82-86e5-578a5fa33f11
index_schema_version: 1
---

A felhasználó azt kérdezi: "Alfréd, van valamilyen feladatom?" / "mi a következő?" (Alfred `next` mód, v0.4).

**$ARGUMENTS** — opcionális: `[scope]` — szűrés adott scope-ra.

**Tennivaló:**

1. Olvasd `02_Areas/Personal Growth/Alfred/tasks/00_TASKS.md` (queue) + `state/triage_queue.md` (pending).
2. Válaszd a legmagasabb prioritású **`prepared`** (vagy `in-review`) dossziét: rendezés `priority` (high→med→low) → `due` (közelebbi előrébb) → `received` (régebbi előrébb). Scope-szűrő ha van.
3. Olvasd be a dosszié-fájlt (`tasks/<…>.md`).
4. **Riport (kötelező 3 blokk):**
   - **Mi volt a feladat** — a `## A feladat` szekcióból: feladó, tárgy, mit kérnek, miért kell rá reagálni.
   - **Hogyan próbáltam megoldani** — a `## Agent-hozzájárulások (timeline)` (ki, mit, milyen sorrendben) + a `## Előkészített válasz` draft.
   - **Hol tartunk most** — a `## Státusz` szekcióból: aktuális státusz + javasolt következő lépés + pontosan **mihez kell a döntésed** (pl. "jóváhagyod a draftot? · átírjam X-et? · promote-oljam az actionable-öket todo-ba?").
5. Ha több dosszié van: jelezd, hogy "még N feladat vár" — a következőt a `next` ismételt hívása hozza.
6. Ha nincs `prepared` dosszié: mondd el, mikor futott utoljára a triage (`triage_queue.md` last_triage_at), és ajánld fel a `/alf-triage` futtatását.

**Read-only** — nem módosít semmit. A státusz-váltást a `done`/`todo` módok végzik (a `next` csak felszolgál).

Lásd: `00_Prompts/BDOS/agents/alfred.md` §4 `next` mód + §5b dossier-séma.
