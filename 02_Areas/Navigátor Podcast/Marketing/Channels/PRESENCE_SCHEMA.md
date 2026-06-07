---
title: "Presto Presence Schema v1"
date: 2026-05-25
author: Becze Szabolcs
status: active
description: "Schema spec a presto.org-presence.v1 formátumhoz — minden szervezet/jelenlét egységes frontmatter struktúrája, vault-indexing kompatibilis."
id: schema-presence-v1-001
index_schema_version: 1
bdos_index: true
schema: bdos.schema-spec.v1
---

# Presto Presence Schema v1

> Minden szervezet/brand, amit Szabolcs kezel, kap egy `presence.md` fájlt az Area gyökerében.

## Frontmatter spec

```yaml
schema: presto.org-presence.v1
org_name: "Human-readable org name"
org_id: kebab-case-identifier        # stabil ID, query-khez
role: owner | admin | editor         # Szabolcs szerepe
access_via: szabolcs-becze-fb        # milyen fiókról érhető el
platforms: [facebook, instagram, youtube]  # flat list a gyors szűréshez
channels:                            # strukturált channel lista
  - platform: facebook
    type: page | profile | group
    name: "Page Name"
    handle: ""
    url: ""
    status: active | inactive | recovery-needed
    email: ""
    phone: ""
    access_via: "szabolcs-becze-fb"
  - platform: instagram
    # same fields...
```

## Query patterns (vault-indexing)

```bash
# Minden presence fájl
python3 query.py --fts "org-presence"

# Melyik szervezetnek van Instagram-ja
python3 query.py --fts "instagram"

# Recovery szükséges fiókok
python3 query.py --fts "recovery-needed"
```

## Graph edges

A presence fájlok `[[wikilink]]`-ekkel kapcsolódnak:
- `[[szabolcs-becze-personal]]` → személyes profil node
- `[[navigator-podcast-presence]]` → org node
- `[[mediamuhely-presence]]` → recovery chain
