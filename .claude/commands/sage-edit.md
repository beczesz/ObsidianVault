---
description: Sage EDIT mode — egy konkrét thought/atomic note refine-olása. Confirmation kötelező.
id: caeef1de-31b5-4f7d-8969-22d27d56c24d
index_schema_version: 1
---

A felhasználó egy konkrét note editálását kéri.

**$ARGUMENTS** — kötelező: a note slug-ja vagy útvonala (pl. `thoughts/2026-05-24_cognition-distribution-wall` vagy `atomic/low-noise-high-signal`).

**Tennivaló:**

1. Értelmezd a path-ot — Ideas/ alatti relatív vagy slug
2. Ellenőrizd, hogy a fájl létezik (Glob)
3. Hívd `subagent_type: sage`
4. Paraméterek:
   - `mode: edit`
   - `note_path: 02_Areas/Personal Growth/Ideas/<resolved path>`
5. Sage először javasol változtatást (diff-szerűen, NEM ír)
6. **Várj user-confirm-ra** ("igen" / "yes" / "--confirm")
7. Csak akkor írj
8. Frissítsd `note_revision`-t a frontmatterben + append `_journal/<YYYY-MM>.md`
