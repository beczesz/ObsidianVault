---
description: Presto PLAN mode — új marketing kampány tervezése egy Area-ban. CAMPAIGN.md létrehozás + /marketing:campaign-plan skill futtatás. Confirmation kötelező.
id: a3ff7d8a-08ce-4e5f-970f-bb3e5f2d3493
index_schema_version: 1
---

A felhasználó új marketing kampányt tervez.

**$ARGUMENTS** — kötelező: az Area és a cél. Példák:
- `--area=ExarLabs --objective="Microsite Factory Q3 launch"` → új kampány Q3 launch-ra
- `--area=DH --objective="Húsvét akció" --tier=lite` → kisebb kampány light tier-ben
- `--area=CPS --objective="AWS co-marketing brief" --tier=premium` → komplex kampány

**Tennivaló:**

1. Parsold az $ARGUMENTS-ből: `--area=` (kötelező), `--objective=` (kötelező), `--tier=lite|standard|premium` (default: standard).
2. Ha bármelyik kötelező hiányzik, kérdezz vissza.
3. Hívd meg a Presto-t **`subagent_type: presto`** **plan módban**:
   - Új kampány-slug generálás (kebab-case az objective-ből)
   - Új fájlok: `02_Areas/<area>/Marketing/Campaigns/<slug>/CAMPAIGN.md` + `brief.md`
   - `Pipeline.md` `## Brief` szekciójába új sor
   - `/marketing:campaign-plan` skill futtatás az objective-vel → output a `brief.md`-be
4. **Confirmation gate KÖTELEZŐ** — Presto megmutatja a tervezett akciót (slug, lokáció, skill-hívás), és vár igen/yes válaszra mielőtt bármit írna.
5. Iteration history log a `CAMPAIGN.md`-ben.

**Hint:** ha az Area-nak még nincs `Marketing/` mappája, Presto javasolni fogja a bootstrap-et (engine-fájl + Pipeline + Dashboard létrehozása a `marketing-engine` capability sablonokból).
