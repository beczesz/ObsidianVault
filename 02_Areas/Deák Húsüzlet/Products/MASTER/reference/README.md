---
title: "Reference Files — DO NOT EDIT"
date: 2026-05-07
author: Becze Szabolcs
status: active
description: "Canonical reference documentation for Deák Húsmíves product schema and Frappe backend doctypes, including production-compliant JSON schema and sample data structures that serve as source of truth for local development and build validation."
description_source: auto
description_hash: 4bb7c0d109e3eddf
id: 3ef1f3a0-67ba-4c6b-8e51-c4abcc25abed
index_schema_version: 1
bdos_index: true
---
# Reference Files — DO NOT EDIT

These files are the **canonical source of truth** for the Deák Húsmíves product schema and data structure. They reflect the production Frappe backend doctypes:
- `Deak Product`
- `Deak Product Category`
- `Deak Product Settings`
- `Deak Product Quantity Override`
- `Deak Unit Option`

## Files

| File | Purpose |
|------|---------|
| `_schema-v1.0.json` | Authoritative JSON Schema — production-compliant |
| `products-v1.0.json` | Dummy/sample data (3 products) showing the structure |

## Rules

1. **Read-only:** these files are NEVER edited locally. They come from the production backend.
2. **Source of truth:** if there's a conflict between our MASTER MD format and this reference, the reference wins.
3. **Version bump:** when the production team updates these (e.g. new field for Sprint 4 options), they re-export and we update reference + bump our master schema.
4. **Build target:** `MASTER/scripts/build.py` must produce JSON that validates against `_schema-v1.0.json`.

## Synced from
- Frappe ERPNext / Deak App backend
- Date received: 2026-05-07
