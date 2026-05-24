---
description: Broker RUN mode — egy konkrét sales-task futtatása (outreach draft / proposal-prep / objection-handling / follow-up). Confirmation kötelező. NEM küld semmit.
id: 5c0d6923-fbae-4491-974b-c5915d75570d
index_schema_version: 1
---

A felhasználó Broker sales-task futtatást kér.

**$ARGUMENTS** — kötelező: `--lead <area/cohort/lead-id>`, `--task outreach|follow-up|proposal-prep|objection-handling`.

**Tennivaló:**

1. Parse $ARGUMENTS
2. Hívd `subagent_type: broker`, mode: `run`
3. **Confirmation KÖTELEZŐ** — melyik lead, melyik task, milyen tone
4. Apply után: draft mentés `Cohorts/<slug>/drafts/<lead-id>/`-be
5. **NEM küld semmit** — drafts only, user küld

**Anti-pattern:** soha ne küldj outreach-et automatikusan.
