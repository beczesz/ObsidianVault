---
description: Librarian AUDIT mode — vault egészségi riport. Stale fájlok, hiányzó frontmatter, struktúra-anomáliák, agent meta-állapot.
id: 55cb7e26-ca61-4f71-bbad-f942c955f675
index_schema_version: 1
---

A felhasználó vault-audit-ot kér a Librarian-tól.

**$ARGUMENTS** — scope + opcionális focus. Példák:
- üres → globális audit
- `--scope=deak` → Deák scope
- `--focus=frontmatter` → csak frontmatter-hiányok
- `--focus=agents` → csak agent meta-index frissítés (`00_AGENTS_INDEX.md`)
- `--focus=dates` → csak stale-detektálás

Lehetséges focus értékek: `frontmatter`, `dates`, `structure`, `agents`, `all` (default).

**Tennivaló:**

1. Parsold a scope-ot és focus-t
2. Hívd meg a Librariant **`subagent_type: librarian`**-nal audit módban:
   - `mode: audit`
   - `scope: <scope>`
   - `focus: <focus>`
3. A subagent **csak olvas + ír** (audit fájlt). Nem mozgat, nem töröl.
4. Output: `00_AUDIT.md` a scope gyökerében (új vagy felülírt fájl)
5. **Ha focus=agents vagy focus=all**: frissíti a `00_Prompts/BDOS/00_AGENTS_INDEX.md`-et is — verziók szinkronja, új agent felvétele, deprecated jelölés
6. Summary-ben emeld ki a top 3-5 leginkább cselekvésre okot adó találatot (pl. "47 fájlnak nincs frontmatter", "5 agent verzió-mismatch a canonical és registration között")

**Frekvencia ajánlás:** havi rutinos audit a vault egésze fölött + ad-hoc focus-specifikus auditok ha gyanú van valamire.
