---
description: Maestro AUDIT mode — minőségi check a kész Brand Spine rétegekre. Megerősítés nélkül.
id: f6469173-6c33-413b-9ff1-6adb1c6aa2da
index_schema_version: 1
---

A felhasználó a Maestro `audit` módját hívja a már elkészült rétegekre.

**$ARGUMENTS** — opcionális. Példák:
- (üres) → minden befejezett réteg auditja
- `--layers=1,2,3` → csak megnevezett rétegek
- `--project="02_Areas/Sonrisa" --layers=4,5` → másik projekt, konkrét rétegek

**Tennivaló:**

1. Parsold az $ARGUMENTS-ből: `--layers=` (vesszős lista, default: all-completed), `--project=` (default: current).
2. Hívd meg a Maestro-t **`subagent_type: maestro`** **audit módban**:
   - Olvas: a réteg-specifikus deliverable-eket (worksheet-ek, designok, copy)
   - Méri: konzisztencia rétegek között, hiányzó döntések, minőségi gap-ek
3. Confirmation NEM kell (info-mód).

**Output:** réteg × pass/warn/fail tábla + konkrét hiányosság-lista + (ha van) javasolt follow-up parancs. Tömör — a tábla az output, ne ismételd prózában.
