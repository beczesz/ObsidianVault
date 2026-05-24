---
description: Sage SUMMARY mode — N napos összefoglaló az elmúlt időszakról (új gondolatok, atomic-ok, mintázatok). Megerősítés nélkül.
id: a8f144dd-1fe6-4084-b44e-293f954e0950
index_schema_version: 1
---

A felhasználó Sage összefoglalót kér a közelmúltról.

**$ARGUMENTS** — opcionális:
- üres → utolsó 7 nap
- `--days N` → N nap
- `--week <YYYY-Www>` → konkrét hét

**Tennivaló:**

1. Olvasd: `02_Areas/Personal Growth/Ideas/_journal/<vonatkozó YYYY-MM>.md`
2. Olvasd: `thoughts/*.md` frontmatter-szinten az időablakra
3. Olvasd: `curate/*.md` ha az időablakban van
4. Olvasd: `learnings/active/*.md` ha confirmed_at az ablakban van

Adj vissza emberi riportot:
- "Az elmúlt N napban: X új thought (Y kategóriában), Z új atomic, W learning, A curate-pattern"
- Top 3 kategória említve
- Top 1-2 érdekes emergent pattern (curate-ből) ha volt
- Ha csendes idő volt — mondd ki: "Csendes időszak. Kevés új gondolat."

Olvasás-only, NEM hívja Sage agentet — közvetlen vault-olvasás.
