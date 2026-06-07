---
description: Presto RUN mode — egy kampány aktuális open task-jának futtatása a megfelelő /marketing:* skill-lel. Skill-router a task type alapján. Confirmation kötelező. DEPRECATED v0.8.0 — új munkáknál /pres-seed → /pres-draft → /pres-prepare → /pres-approve pipeline kanonikus.
id: 44f0358d-6563-422a-b19e-dc6aaade5ae7
index_schema_version: 1
status: deprecated
---

> **DEPRECATED v0.8.0** — Ez a parancs visszafelé kompatibilis a meglévő `CAMPAIGN.md`-alapú kampányokkal. Új munkáknál a kanonikus út: `/pres-seed` → `/pres-draft` → `/pres-prepare` → `/pres-approve`. Presto lefuttatja `run` módban, de migrálási javaslatot tesz.

A felhasználó egy kampány-feladatot futtat.

**$ARGUMENTS** — kötelező: a kampány. Példák:
- `--campaign=ExarLabs/microsite-q3` → első open task futtatása
- `--campaign=ExarLabs/microsite-q3 --task=2` → konkrét task index
- `--campaign=DH/husvet-2 --skill=draft-content` → override a router-en

**Tennivaló:**

1. Parsold az $ARGUMENTS-ből: `--campaign=<area>/<slug>` (kötelező), opcionális `--task=<id>`, `--skill=<override>`.
2. Hívd meg a Presto-t **`subagent_type: presto`** **run módban**:
   - Olvas: `02_Areas/<area>/Marketing/Campaigns/<slug>/CAMPAIGN.md`
   - Megkeresi az első open `- [ ]` task-ot (vagy a megadott index-űt)
   - **Skill-router**: a task `type:` mezője alapján:
     - `content-draft` → `/marketing:draft-content`
     - `content-review` → `/marketing:brand-review`
     - `email-flow` → `/marketing:email-sequence`
     - `seo-task` → `/marketing:seo-audit`
     - `competitor-research` → `/marketing:competitive-brief`
     - egyéb / üres → kérdez vissza melyik skill kell
   - Ha `--skill=` override van, azt használja
3. **Confirmation gate KÖTELEZŐ** — Presto megmutatja: melyik task, melyik skill, milyen inputtal, melyik fájlokat érinti. Vár igen/yes válaszra.
4. Skill-futtatás után: task checkbox `[x]`, asset mentés `assets/`-be ha kell, Iteration history log.

**Soha:** Presto nem publishel közvetlenül semmit (social/blog/email). A draft `ready`-re kerül, az ember küldi/postaolja.
