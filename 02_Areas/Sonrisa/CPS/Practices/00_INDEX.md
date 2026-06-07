---
schema: cps.practices.index.v1
generated_at: 2026-05-27
description: CPS Practice Areas élő indexe — cross-client kapacitás- és kutatási területek a CPS unit alatt. Forge agent karbantartja. Minden practice area saját mappa NOTES.md-vel, struktúrált subfolderekkel (_inbox, research, patterns, decisions, experiments, proposals, learnings). NEM ügyfél-engagement (az Accounts/), hanem stabil szakterület több projekten átívelően.
maintained_by: Forge agent (v0.1)
unit: "Sonrisa/CPS"
practice_count: 1
id: c5e8d24f-91a7-4b63-8f5c-3d7a9b2e1f48
index_schema_version: 1
bdos_index: false
---

# CPS Practice Areas — Index

> Élő index, Forge agent tartja karban. Generálás: `/forge-index` (v0.2-ben). Manuálisan most v0.1 boot-állapotban.

## Mi a practice area

**Practice area = stabil szakterület**, amit a CPS team folyamatosan fejleszt, ami **több ügyfél-engagementen ível át**, és ami **research, design patterns, deliverables-mix-ként** él. NEM ügyfél-engagement (azt `Accounts/Active/` tartja). NEM ad-hoc projekt (azt `01_Projects/` tartja).

A practice area-k a CPS **kapacitás-rétege**. Innen merít Broker amikor proposalt készít új ügyfélnek, és innen merít Presto amikor case study / marketing publikációt épít.

## Active practice areas (1)

| Practice | Maturity | Status | Owner | Triggered by | Last signal |
|---|---|---|---|---|---|
| [Inference Farm](Inference-Farm/NOTES.md) | research | forming | Becze Szabolcs + Ceclan Sanyi | Merkantil Discovery 2026-05-27 | 2026-05-27 |

## Maturity stages

| Stage | Mit jelent | Practice areas a stage-ben |
|---|---|---|
| `research` | exploratory, nincs még stable pattern | Inference Farm |
| `patterns-emerging` | 1-2 pattern már kikristályosodott, evidence < 3 | — |
| `service-ready` | reusable proposalok van, 3+ ügyfél evidence egy patternre | — |
| `mature` | több service-tier, jól árazott, ismétlődő engagement | — |
| `retired` | nincs aktív kereslet, archive státusz | — |

## Candidates / Backlog (more practice areas to consider)

Olyan területek, amik a CPS működésében felmerülnek, de még NEM kaptak practice area dedikációt. Ha 2-3 kliens-szignál jön ugyanarra, érdemes practice area-vá emelni (Forge `/forge-capture` confirm után):

- **Cloud Cost Optimization (FinOps)** — már létezik `Services/Cost optimization/` alatt, esetleg ide promote-olható
- **Managed Kubernetes / OpenShift** — MVMI Omni Support, OKFO Azure DevOps releváns
- **DevSecOps add-on** — Loxon, ABRIS, Cardinal Software releváns
- **AWS Migration playbook** — Observer (cs-002), Onriva (cs-003) releváns
- **Azure DevOps Managed Service** — MVMI flagship, OKFO releváns, CIG Pannonia outreach
- **Banking-grade On-Prem Inference** — Inference Farm szűkebb fókuszú változata, esetleg sub-practice
- **Agentic Workflow Operations (n8n / Camunda)** — Merkantil email router triggered

A backlog-ot Forge `reflect` mód havonta felülvizsgálja.

## Konvenciók

Lásd Forge canonical: [`00_Prompts/BDOS/agents/forge.md`](../../../../00_Prompts/BDOS/agents/forge.md) §5 Storage Convention.

Kötelező subfolderek minden practice area-ban: `_inbox/`, `research/`, `patterns/`, `decisions/`, `experiments/`, `proposals/`, `learnings/`. Kötelező fájlok: `NOTES.md`, `learnings/00_INDEX.md`, `related-projects.md`, `open-questions.md`.

## Maintenance log

| Date | Action | Note |
|---|---|---|
| 2026-05-27 | Bootstrap | Forge v0.1 létrehozva. Első practice area: Inference Farm (Merkantil-triggered). Index első iteráció. |
