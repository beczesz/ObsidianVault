---
description: Presto PLAN mode — új marketing kampány tervezése egy Area-ban. Két use-case: A) kampány-slug alapján új CAMPAIGN.md + /marketing:campaign-plan skill, B) seed-redirect — meglévő seed-ből indul a kampány. Confirmation kötelező.
id: a3ff7d8a-08ce-4e5f-970f-bb3e5f2d3493
index_schema_version: 1
bdos_index: true
---

A felhasználó új marketing kampányt tervez.

**Két use-case:**

**A) Kampány-alapú tervezés (default)**
- `--area=ExarLabs --objective="Microsite Factory Q3 launch"` → új kampány az objective-ből
- `--area=DH --objective="Húsvét akció" --tier=lite` → kisebb kampány light tier-ben
- `--area=CPS --objective="AWS co-marketing brief" --tier=premium` → komplex kampány

**B) Seed-redirect (seed-ből indul)**
- `--area=DH --from-seed=seed-20260525-dh-barbeque` → a seed intent-jéből generálódik a kampány-brief

**$ARGUMENTS:**
- `--area=<name>` (kötelező mindig)
- `--objective="<szöveg>"` (kötelező A esetben; B esetben a seed intent-jéből jön)
- `--tier=lite|standard|premium` (default: standard)
- `--from-seed=<seed-id>` (B eset kapcsolója)

**Tennivaló:**

1. Parsold az $ARGUMENTS-ből a fenti paramétereket.
2. Ha `--area` hiányzik, kérdezz vissza.
3. **A eset** (nincs `--from-seed`):
   - Ha `--objective` hiányzik, kérdezz vissza.
   - Generálj campaign-slug-ot kebab-case-ben az objective-ből.
4. **B eset** (`--from-seed` megadva):
   - Olvasd `presto/_inbox/seeds/<seed-id>.md`-t.
   - Validáld: `status` nem `exhausted` (ha igen, figyelmeztet és megkérdezi folytatja-e).
   - A seed `intent.message` és `intent.audience` mezőiből generálj `objective` stringet.
   - Campaign-slug = seed slug-ból `camp-<seed-slug-suffix>`.
5. Hívd `subagent_type: presto` **plan módban** a kinyert paraméterekkel.
6. Presto:
   - Új fájlok: `02_Areas/<area>/Marketing/Campaigns/<slug>/CAMPAIGN.md` + `brief.md`
   - `Pipeline.md` `## Brief` szekciójába új sor
   - `/marketing:campaign-plan` skill futtatás → output `brief.md`-be
   - B esetben: seed `status: campaign-linked`, `linked_campaign: <slug>` mező kitöltve
7. **Confirmation gate KÖTELEZŐ** — Presto megmutatja: slug, lokáció, skill-hívás, seed-link (B esetben). Vár igen/yes válaszra.
8. Iteration history log a `CAMPAIGN.md`-ben.

**Hint:** ha az Area-nak még nincs `Marketing/` mappája, Presto javasolni fogja a bootstrap-et (engine-fájl + Pipeline + Dashboard létrehozása a `marketing-engine` capability sablonokból).

**Seed-redirect előtt javasolt:** futtasd `/pres-status`-t hogy lásd az aktív seed-eket — vagy `/pres-draft`-ot ha nem egész kampányt, csak egy publikációt akarsz a seed-ből.
