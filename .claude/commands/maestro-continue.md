---
description: Maestro CONTINUE mode — félbehagyott Brand Spine munka folytatása. Confirmation kötelező.
id: f4133641-ba91-46dd-b732-57ef2693f040
index_schema_version: 1
---

A felhasználó a Maestro `continue` módját hívja.

**$ARGUMENTS** — opcionális. Példák:
- (üres) → current project
- `--project="02_Areas/Sonrisa"` → másik projekt

**Tennivaló:**

1. Parsold a `--project=` paramétert.
2. Hívd meg a Maestro-t **`subagent_type: maestro`** **continue módban**:
   - Olvas: `brand-spine-state.md` Iteration history-jából a legutóbbi munkát
   - Megmutatja: hol tartottunk, mi a folytatás
3. **Confirmation gate KÖTELEZŐ** — Maestro a tervezett akciót strukturált formában (TERVEZETT AKCIÓ / INPUT / KIMENETEL / STATE-FRISSÍTÉS / Folytassam?) megmutatja, és vár igen/yes válaszra.
4. A user OK-jára folytatja a munkát + frissíti a state-fájlt + Iteration history log.

**Hint:** ha a state > 14 napja nem mozdult, Maestro jelzi és kérdez: re-prioritizáljuk, vagy folytassuk ahonnan abbahagytuk?
