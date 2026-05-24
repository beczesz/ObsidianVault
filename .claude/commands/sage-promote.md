---
description: Sage PROMOTE mode — thought → atomic note promote, vagy _inbox/atomic_proposals/ → atomic/. Confirmation kötelező.
id: c36d72d4-3dd7-40de-b88a-5332dd527bf6
index_schema_version: 1
---

A felhasználó egy gondolat promote-ját kéri atomic-ká.

**$ARGUMENTS** — kötelező:
- vagy thought slug (pl. `thoughts/2026-05-24_cognition-distribution-wall`)
- vagy _inbox/atomic_proposals/ slug

**Tennivaló:**

1. Resolve a path
2. Hívd `subagent_type: sage`
3. Paraméterek:
   - `mode: promote`
   - `source_path: <resolved>`
   - `target_dir: 02_Areas/Personal Growth/Ideas/atomic/`
4. Sage:
   - Generál egy `sage.atomic.v1` schema-jú új note-ot (vagy bővít meglévőt)
   - Kötelezően kitölti a history szekciót (legalább 1 source_thought wikilink)
   - Cross-linkek mindkét irányba (source thought-ban is bevezet `atomic_links` mezőt)
5. **Confirmation kötelező** mielőtt write
6. Audit: append `_journal/<YYYY-MM>.md`
