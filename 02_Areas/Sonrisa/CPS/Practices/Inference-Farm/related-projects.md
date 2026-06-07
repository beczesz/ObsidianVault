---
title: Inference Farm — Related Projects (cross-link to engagements)
date: 2026-05-27
description: Wikilink-tábla a kliens-engagementekhez, ahol a CPS Inference Farm practice area releváns vagy alkalmazva van. Broker karbantartja az engagement-oldali NOTES-okat, Forge frissíti ezt a fájlt amikor az engagement érintkezik a practice area-val. Bi-directional cross-reference: az engagement NOTES-ban is meg kell jelennie a practice-link-nek.
bdos_index: false
id: 88764623-a3a0-47b5-ad1f-61a60795b5ea
index_schema_version: 1
---

# Inference Farm — Related Projects

> Cross-link a kliens-engagementekhez. Frissíti: Forge `capture` / `handoff` módok confirmation után. **Forward-link kötelező:** az engagement-oldali NOTES.md-ben is jelölni kell a practice-kapcsolatot.

## Active engagements

| Engagement | Stage | Relevance | Folder |
|---|---|---|---|
| **Merkantil Bank Zrt.** | Backlog (AM) / Discovery Call (Sales) | **TRIGGERED THIS PRACTICE** — AID infra deployment sizing. First concrete sizing exercise. | [[Accounts/Leads/Merkantil/NOTES]] |

## Reference engagements (analog patterns)

Olyan engagementek, amik nem Inference Farm-ot szállítanak, de a deployment-pattern (one-time setup + havi managed) referencia-pontként szolgál:

| Engagement | Mit ad referenciaként | Folder |
|---|---|---|
| **MVMI — Azure DevOps Managed Service** | A "mirror Sonrisa-internal stack + managed overlay" packaging pattern referencia-pontja. Sizing- és árazás-szempontból analog. | [[Accounts/Active/MVMI/AzureDevOps Managed Service/NOTES]] |
| **MVMI — Omni Support (OpenShift)** | A "containerized platform managed service" pattern referencia-pontja. CPS itt is fut Kubernetes-szintű managed ops-szal. | [[Accounts/Active/MVMI/Omni Support/NOTES]] |

## Strategic-dependency engagements (indirect)

Olyan engagementek, amikben az Inference Farm **Pillar 2/3** (Agentic AIOps / FinOps) függőségként szerepel — nem direkt LLMaaS-t szállítunk, de a Pillar 1 substrate alatta van:

| Engagement | Kapcsolat | Folder |
|---|---|---|
| **CCHBC (Coca-Cola HBC) — AIOps Tender** | Magyar Telekom-os sub-bid az Agentic AIOps tier model alatt. Pillar 2 deliverable, ami **a Sonrisa LLMaaS-en (Pillar 1) fut**, mint inference substrate. CCHBC indirektül validálja az Inference Farm strategic positioningját. | [[Accounts/Leads/CCHBC/NOTES]] |

## Candidate engagements (where Inference Farm could apply if signal materializes)

- **Loxon Solutions** — banking, AWS, DORA. Ha Loxon AI use case-t fejleszt → potenciálisan releváns.
- **SEON** — fraud detection, AWS. ML/inference workload-jaik vannak, de saját stack-en. Ha váltani akarnak managed-re → releváns.
- **ABRIS Kft.** — banking IT vendor (Temenos). DORA pressure-re ML capability bővíthet.
- **CIG Pannonia** — insurance. DORA + insurance regulátor. Belső AI use case-ek várhatók.

## Cross-area links (related practices)

Most még üres. Várható csatlakozási pontok:
- **Cloud Cost Optimization** (ha létrejön külön practice) — GPU FinOps overlap
- **DevSecOps** (ha létrejön külön practice) — banking-compliance overlap
- **Managed Kubernetes** (ha létrejön külön practice) — K8s orchestration overlap

## Change log

| Date | Event |
|---|---|
| 2026-05-27 | Fájl létrehozva. Merkantil mint trigger-engagement rögzítve. MVMI Azure DevOps + Omni Support mint reference. Loxon/SEON/ABRIS/CIG mint candidate. |
