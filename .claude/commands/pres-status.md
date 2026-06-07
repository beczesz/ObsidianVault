---
description: Presto STATUS mode — cross-project marketing áttekintés. 6-stage kanban (Seed/Draft/Prepared/Approval/Scheduled/Published) + aktív seedek szekció. Kötelező "Most ajánlott következő lépés" + "Egyéb opciók" szekció.
id: 9d23d4d4-0572-467e-a4c4-03157ad0c896
index_schema_version: 1
bdos_index: true
---

A felhasználó marketing-státuszt kér a Presto-tól.

**$ARGUMENTS** — opcionális. Példák:
- (üres) → cross-project áttekintés minden Area-ról
- `--area=ExarLabs` → csak egy Area kampányai és publikációi
- `--stage=draft` → csak egy stage-ben lévő entitások

**Tennivaló:**

1. Parsold az opcionális paramétereket az $ARGUMENTS-ből (`--area=`, `--stage=`).
2. Hívd meg a Presto-t **`subagent_type: presto`** **status módban**:
   - Olvas: `_dashboards/00_MARKETING_INDEX.md` (ha nincs, jelzi és javasolja a `/pres-index`-et)
   - Aggregálja minden Area `Marketing/Publications/*.md` fájljait (`presto.publication.v2` schema) stage szerint
   - Aggregálja a `presto/_inbox/seeds/*.md` aktív seed-eket (`status` != `exhausted`)
   - Fallback: régi `Marketing/Pipeline.md` + `CAMPAIGN.md` fájlokat is beolvassa (visszafelé kompatibilis)

3. Output (kötelező szekciók):

   **a) 6-stage kanban tábla** (csak nem-üres stage-ek):
   ```
   | Stage      | Area       | Entitás          | Due        | Next action            |
   |------------|------------|------------------|------------|------------------------|
   | Approval   | DH         | pub-linkedin-001 | 2026-05-26 | /pres-approve --pub .. |
   | Prepared   | ExarLabs   | pub-blog-001     | 2026-05-28 | /pres-approve --pub .. |
   | Draft      | DH         | pub-x-001        | 2026-05-30 | /pres-prepare --pub .. |
   ```

   **b) Aktív seedek** (ha van `presto/_inbox/seeds/` tartalom `status != exhausted`):
   ```
   | Seed-id                    | Area | Source       | Napok | Javaslat    |
   |----------------------------|------|--------------|-------|-------------|
   | seed-20260520-nyari-akció  | DH   | user         | 5     | draft/exhaust|
   ```

   **c) "Most ajánlott következő lépés"** — EGYETLEN konkrét slash-command
   **d) "Egyéb opciók"** — 2-3 alternatív akció bullet-ben

4. Confirmation NEM kell (info-mód).

**Kontextus-védelem:** a tábla az output — ne ismételd prózában. Csak rövid bevezető és a szekciók.
