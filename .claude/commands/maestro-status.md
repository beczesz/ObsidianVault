---
description: Maestro STATUS mode — Brand Spine projekt állapot-riport (megerősítés nélkül). Hol tartunk a 7 rétegből, mi blokkolt, mi készül.
id: 48b68e53-013d-48db-93b3-270949147997
index_schema_version: 1
---

A felhasználó a Maestro `status` módját hívja.

**$ARGUMENTS** — opcionális. Példák:
- (üres) → current working directory project
- `--project="02_Areas/Sonrisa"` → másik projekt

**Tennivaló:**

1. Parsold a `--project=` paramétert (default: current working directory).
2. Hívd meg a Maestro-t **`subagent_type: maestro`** **status módban**:
   - Olvas: `brand-spine-state.md` (ha létezik) + a recipe
   - Riport: jelenlegi réteg, befejezett rétegek, blokkok, next-up
3. Confirmation NEM kell (info-mód).

**Output:** strukturált riport-blokk + következő lépés tipp ha kell. Tömör — ne ismételd az állapotot prózában.
