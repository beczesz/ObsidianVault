---
description: Broker MEASURE mode — sales KPI (conversion, deal velocity, win/loss, cycle time). Megerősítés nélkül.
id: 38b207a2-bada-4ccf-a48a-2276e569b7aa
index_schema_version: 1
---

A felhasználó sales KPI-riportot kér.

**$ARGUMENTS** — opcionális: `--scope cohort:<area/slug>|area:<name>|cross-project`, `--period <YYYY-MM|Q?|last30d>`.

**Tennivaló:**

1. Hívd `subagent_type: broker`, mode: `measure`
2. Broker olvas: `Cohorts/<slug>/Results-*.md`, `Pipeline.md`-ek
3. Output: conversion rate, deal velocity, win/loss analysis, cycle time
