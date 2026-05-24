---
description: Maestro START mode — új Brand Spine projekt indítása tier-választással. brand-spine-state.md létrehozás. Confirmation kötelező.
id: 3dc07541-0b21-4666-97d2-4335d0c2442d
index_schema_version: 1
---

A felhasználó új brand→site projektet indít.

**$ARGUMENTS** — kötelező a projekt-név. Példák:
- `"Sonrisa CPS"` → standard tier (default)
- `"Deák Húsüzlet" --tier=lean` → lean tier
- `"Premium kliens" --tier=premium` → premium tier
- `"Új projekt" --project="02_Areas/Új projekt"` → explicit lokáció

**Tennivaló:**

1. Parsold az $ARGUMENTS-ből: projekt-név (idézőjelek között), `--tier=lean|standard|premium` (default: standard), opcionális `--project=`.
2. Hívd meg a Maestro-t **`subagent_type: maestro`** **start módban**:
   - Új `brand-spine-state.md` létrehozás a célmappában
   - Tier-specifikus recipe alapján Layer 1 induló paraméterek
3. **Confirmation gate KÖTELEZŐ** — Maestro megmutatja: hová kerül a state, melyik tier, melyik recipe, mi az induló lépés. Vár igen/yes-re.
4. A user OK-jára létrehozza a fájlt + Iteration history első bejegyzés.

**Tier-gyors-útmutató:**
- `lean` — minimal-viable site, 1-2 hét, kevés tool
- `standard` — teljes 7 réteg, 3-4 hét, közepes tool-stack
- `premium` — multi-AI brainstorm + minden tool, 6+ hét, full stack
