---
description: Maestro NEXT mode — következő konkrét lépés javaslata (réteg + tool + skill + másolható parancs). Megerősítés nélkül.
id: c4da1278-8393-462d-81fc-b479a7b69eec
index_schema_version: 1
---

A felhasználó a Maestro `next` módját hívja.

**$ARGUMENTS** — opcionális. Példák:
- (üres) → current project
- `--project="02_Areas/Deák Húsüzlet"` → másik projekt

**Tennivaló:**

1. Parsold a `--project=` paramétert.
2. Hívd meg a Maestro-t **`subagent_type: maestro`** **next módban**:
   - Olvas: `brand-spine-state.md`, `recipes/<tier>.md`, `tools/INVENTORY.md`
   - Javaslat: réteg + tool + skill + **másolható parancs** + (ha tool hiányzik) install-path és kompromisszum alternatíva
3. Confirmation NEM kell (csak javaslat, nem futtatás).

**Output:** strukturált blokk a következő konkrét akcióval, code-block-ban a parancs, hogy egy mozdulattal indulhasson.
