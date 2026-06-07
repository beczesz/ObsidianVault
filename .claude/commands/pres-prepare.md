---
description: Presto PREPARE mode — draft Publication felkészítése jóváhagyásra. Brand-review futtatása, variációk generálása, schedule proposal, opcionális SEO audit (blog). publication_status: draft → prepared. Confirmation kötelező.
id: d5a3b9c4-1e6f-4a0b-c2d3-4e5f6a7b8c9d
index_schema_version: 1
bdos_index: true
---

A felhasználó egy draft publikációt készít elő jóváhagyásra.

**$ARGUMENTS** — kötelező:
- `--pub <pub-id>` — melyik Publication-t készítse elő
- opcionális `--variants=N` — N alternatív headline/hook variáció (default: 1)
- opcionális `--seo` — SEO audit futtatása (csak blog channel esetén releváns)

**Tennivaló:**

1. Parsold az $ARGUMENTS-ből: `--pub` (kötelező), `--variants`, `--seo`.
2. Ha `--pub` hiányzik, kérdezz vissza: "Melyik pub-id-t készítsem elő?"
3. Hívd `subagent_type: presto` **prepare módban**:
   - Olvasd a Publication fájlt (`02_Areas/<area>/Marketing/Publications/<pub-id>.md`)
   - Validáld: `publication_status: draft` (ha más, figyelmeztet — pl. ha `prepared`, javasol `/pres-approve`-t)
   - Futtasd `/marketing:brand-review`-t a publication body-ján
   - Ha `--seo` ÉS channel = blog/Newsletter: futtasd `/marketing:seo-audit`-ot
   - Ha `--variants=N` (N>0): generálj N alternatív headline + hook variációt (body megtartásával)
   - Javasolj `publish_date`-t (ha a seed-ben vagy area MARKETING_ENGINE.md-ben van cadence info)
4. **Confirmation gate KÖTELEZŐ** — mutasd: pub-id, brand-review összefoglaló (pass/fail/suggestions), variációk listája, javasolt publish_date. Vár igen/yes válaszra.
5. Igen után:
   - Frissítsd `publication_status: draft → prepared`
   - Append `## Review findings` szekcióba a brand-review outputját
   - Append `## Variants` szekcióba a variációkat (ha generált)
   - Set `publish_date` ha javasolt és user nem ellenezte

**Következő lépés prepare után:**
- `/pres-approve --pub <pub-id> --action approve` → jóváhagyás + ütemezés

**Soha:** ne ugord át a prepare lépést — az approval feltétele a `publication_status: prepared`.

Lásd: `00_Prompts/BDOS/agents/presto.md` §6.4c.
