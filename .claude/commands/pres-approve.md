---
description: Presto APPROVE mode — prepared publikáció jóváhagyása és ütemezése (approval → scheduled), vagy elutasítása (approval → draft). Interaktív publish_date bekérés ha nincs kitöltve. Confirmation kötelező.
id: d8f2b4c3-5e6a-7890-bcde-f01234567890
index_schema_version: 1
bdos_index: true
---

A felhasználó egy prepared/approval-stage publikációt hagy jóvá vagy utasít el.

**$ARGUMENTS** — kötelező:
- `--pub <pub-id>` — a publication azonosítója (pl. `pub-linkedin-20260525-dh-akció`)
- `--action approve|reject` — jóváhagyás vagy elutasítás
- opcionális `--publish-date="YYYY-MM-DD HH:MM"` (approve esetén; ha hiányzik, Presto interaktívan kérdezi)
- opcionális `--reason "<szöveg>"` (reject esetén; ha hiányzik, Presto kérdezi)

**Tennivaló:**

1. Parsold az $ARGUMENTS-ből: `--pub`, `--action`, opcionálisan `--publish-date`, `--reason`.
2. Ha `--action` hiányzik, kérdezz vissza: "approve vagy reject?"
3. Hívd `subagent_type: presto` **approve módban**:
   - Olvasd a Publication fájlt (`Marketing/Publications/<pub-id>.md`)
   - Validáld: `publication_status` legyen `prepared` vagy `approval` (ha `draft`, javasold `/pres-prepare`-t előbb)
4. **approve folyamat:**
   - Ha `publish_date` hiányzik a fájlból ÉS `--publish-date` nincs megadva: kérdezd interaktívan: "Mikor legyen ütemezve? (YYYY-MM-DD HH:MM, pl. 2026-05-27 10:00)"
   - Confirmation gate: publication tartalom összefoglaló + publish_date + "Ezzel ütemezem: publication_status → scheduled"
   - Igen után: frissítsd `publication_status: scheduled`, `publish_date` kitöltve, logolj
5. **reject folyamat:**
   - Ha `--reason` hiányzik, kérdezd: "Mi az elutasítás oka?"
   - Confirmation gate: publication összefoglaló + reason + "publication_status → draft"
   - Igen után: frissítsd `publication_status: draft`, `rejection_reason` kitöltve, logolj
6. **Confirmation gate KÖTELEZŐ** minden esetben — vár igen/yes válaszra.

**Következő lépés approve után:**
- Ha `scheduled` → a következő emberi akció: `/pres-publish --pub <pub-id>` a `publish_date`-kor.

**Soha:** ne approve-olj `publication_status: draft` (futtasd `/pres-prepare`-t előbb).

Lásd: `00_Prompts/BDOS/agents/presto.md` §6.4d.
