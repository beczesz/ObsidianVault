---
description: Broker PLAN mode — új sales cohort tervezése egy Area-ban. Confirmation kötelező.
id: cb85e22f-cbef-40fe-8917-0b3768e08e32
index_schema_version: 1
---

A felhasználó új sales-cohort tervezését kéri.

**$ARGUMENTS** — kötelező: `--area <name>`, `--cohort "<one-line>"`, opcionális `--tier lite|standard|premium`.

**Tennivaló:**

1. Parse $ARGUMENTS
2. Hívd `subagent_type: broker`, mode: `plan`
3. **Confirmation gate KÖTELEZŐ** — mutatja a tervezett cohort-slug + lokáció
4. Apply után: új `Sales/Cohorts/<slug>/COHORT.md` + `Sales/Pipeline.md` update
