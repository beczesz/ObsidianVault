---
description: CPS Statistics Processor (Phase 1) - feldolgozza a raw Sontime activity report xlsx-t és generálja a _base.xlsx, _tam.xlsx és MUB markdown fájlokat. Trigger: "process timesheets", "havi statisztika", "activity report", "raport", "cps stats".
id: cps-stats-0001-4c00-8b00-000000000001
index_schema_version: 1
---

CPS havi statisztika feldolgozás kérés érkezett.

**$ARGUMENTS** — opcionális: hónap (pl. `2026_05`) vagy fájl elérési útja.

**Tennivaló:**

1. Olvasd a teljes skill-instrukciót: `00_Prompts/Claude/Plugins/Sonrisa Management Plugin/skills/cps-statistics-v0.3/SKILL.md`
2. Olvasd a referencia fájlokat (mub-instructions.md, build-process.md) a plugin mappájából.
3. Raw input keresési helye a vault-ban: `02_Areas/Sonrisa/CPS/Administration/Reports/raw/`
4. Ha fájl nincs ott, kérdezd meg a felhasználót az elérési útról.
5. Kövesd a SKILL.md-ben leírt Phase A (parse + classify + user review) és Phase B (generate) lépéseket PONTOSAN.
6. MUB output helye: `02_Areas/Sonrisa/CPS/Administration/Reports/MUB/MUB_YYYY_MM.md`
7. xlsx outputok (\_base, \_tam) a SKILL.md szerinti SharePoint útvonalra kerülnek (nincs vault-ban tárolva).
8. Ha új task kerül "Other" kategóriába, frissítsd a `references/mub-instructions.md` fájlt a plugin mappájában.

**Vault plugin forrás:** `00_Prompts/Claude/Plugins/Sonrisa Management Plugin/`
