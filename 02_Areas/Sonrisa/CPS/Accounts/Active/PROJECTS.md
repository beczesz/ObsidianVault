---
description: "Live kanban source tracking Account Management project lifecycle from backlog through closure, with embedded metadata: project names, stage tags, review dates, teaser summaries, and wiki links to detailed engagement notes. Primarily for internal AM dashboard automation and project tracking workflow."
description_source: auto
description_hash: bb3f63b4c37b9b84
kanban-plugin: board
id: 570be668-ae79-4b09-8635-1ba8b786223b
index_schema_version: 1
---
<!--
  ===========================================================================
  LIVE DATA SOURCE for the Account Management dashboard.
  ===========================================================================
  Analog to Sales/Pipeline.md. This file is the source of truth for the
  Account Management kanban (project-level, not account-level). Each card
  is ONE engagement / sub-engagement. Accounts with multiple engagements
  (e.g. MVMI) appear as multiple cards.

  CARD LINE FORMAT (required):
      - [ ] **Project Display Name** #tag1 #tag2 @{YYYY-MM-DD} teaser text [[wiki-link]]
  - Bold project name is REQUIRED (the first **...** pair on the line).
  - Date syntax in THIS file: @{YYYY-MM-DD}. Same convention as Pipeline.md.
    Semantics: next-review / next-milestone / renewal-trigger date for the project.
  - Tags starting with stage names (#backlog, #delivery, etc.) are dropped by
    the parser since stage comes from the column. Other tags become card chips.

  COLUMN HEADERS (10 stages, in order):
      ## Backlog
      ## Initial meeting
      ## Define project need
      ## RFP / RFI
      ## Won
      ## Contracted
      ## Delivery
      ## Renewal
      ## Closed
      ## Lost
  - Parser matches stage by case-insensitive prefix.
  - Lost is TERMINAL (a project can land here from ANY stage above).
  - Closed and Lost are both visible (no auto-collapse).

  HANDOFF FROM SALES PIPELINE:
  - Sales/Pipeline.md ends at "Won" (deal closed).
  - When a card hits Won in Sales, it ALSO appears in this file at "Won"
    (or wherever appropriate in the AM lifecycle). Same project, two lenses.
  - Sales focus: lead-to-won.
  - AM focus: backlog-to-closed (full project lifecycle).
  - Cards may exist in BOTH dashboards simultaneously during the transition.

  RELATIONSHIP TO ACCOUNTS/ACTIVE/ FOLDERS:
  - Accounts/Active/<Name>/NOTES.md = account-level overview
  - Accounts/Active/<Name>/<Engagement>/NOTES.md = per-engagement detail
    (sub-folders for multi-engagement accounts; MVMI is the canonical example)
  - Each kanban card links to ONE NOTES.md (account-level OR engagement-level
    depending on granularity).
  - Backlog cards may temporarily link to Accounts/Leads/<Name>/NOTES.md
    (e.g. Merkantil before its folder is promoted to Active on Won).

  FULL CONTRACT: see Sales/DASHBOARD_CONTRACT.md (will be extended for AM).
  Renaming or moving this file silently breaks the dashboard.
  ===========================================================================
-->

## Backlog

- [ ] **Merkantil Bank Zrt.** #merkantil #banking #fintech #otp-group #aid #email-routing #ai-enablement #lang-hu #multi-workstream @{2026-05-28} NEW 2026-05-27. Multi-workstream Sonrisa engagement (active since 2026-04-27). Email router + AI Enablement proposals SENT 2026-05-21 by non-CPS units; CPS scope (AID infra deployment) Discovery call held 2026-05-27 12:00. Post-call info pending from user. NOTE: folder still at Accounts/Leads/ — promote to Active when CPS scope graduates to Won. [[Accounts/Leads/Merkantil/NOTES]]


## Initial meeting



## Define project need

- [ ] **Raab Computer — K8s Cluster** #raab-computer #kubernetes #partner-channel #hybrid-cloud #multi-datacenter #service-mesh #build-plus-ops #lang-hu #urgent @{2026-05-29} NEW 2026-05-28 via partner email (Ács Gusztáv, Raab Computer Kft., Győr). Partner-channel deal: end client (unnamed) wants a production K8s cluster — node/pod mgmt, load-based autoscaling, service discovery, service mesh (auth/authz), health-check + self-healing + alerting, MULTI-DC/hybrid (company net + Vultr/other cloud), ~100 microservices. Phase 1 (1-2yr dev): build + business-hours support; 7/24 after go-live. **URGENT: indicative quote needed before Friday 2026-05-29** for end-client leadership review, precedes Friday meeting. Core-CPS fit (MVMI OpenShift analog). Needs Ceclan effort sizing. [[Accounts/Leads/Raab_Computer/NOTES]]



## RFP / RFI



## Won



## Contracted



## Delivery

- [ ] **Melinda Instal — Installator App** #melinda-instal #romania #mobile-app #storefactory #ecommerce #software-dev #loyalty #erp-integration #lang-hu #lang-ro #deadline-passed @{2025-12-31} INTRODUCED 2026-05-28 from SharePoint ("régi új projekt"). MELINDA IMPEX INSTAL SA (RO national distributor of installation/sanitary materials, ~90% of RO). Mobile app (Android+iOS) for installers on StoreFactory: customer mgmt, catalog/webshop, cart+orders, PDF quotes, loyalty points, ERP+ANAF sync, WhatsApp/Push. Fixed price **144,400 EUR** (invoiced to date 114,110 EUR; 40% advance + Alfa milestone settled + Beta advance out). Framework MEL-MVE-K2024 + order signed 2024-12-06. **FLAG: contract deadline 2025-12-31 PASSED — status NEEDS CONFIRMATION.** Signatory = Mountain View Engineering SRL (Miklós Nándor). Contact: Becze Szabolcs. [[Accounts/Active/Melinda_Instal/NOTES]]
- [ ] **Melinda Steel — WhatsApp Quoting Chatbot** #melinda-steel #romania #whatsapp #chatbot #quoting #automation #n8n #azure-communication-services #cps #cloudguild #t-and-m #lang-hu #lang-ro @{2026-05-29} INTRODUCED 2026-05-28 from SharePoint. SEPARATE engagement from Melinda Instal — MELINDA IMPEX STEEL SA (sister company, RO steel distributor). WhatsApp-based automated quoting chatbot for their steel-industry B2B customers (currently quote by phone/email). CPS/CloudGuild on n8n + Azure Communication Services + LLM. PoC Aug 2025, signed 2025-11-20 (MELS-SON-K2025), **T&M**. Currently Part 2 (WhatsApp integration, proposal v1.0 Apr 2026). Invoices E-2025-559/562/563 (~5,320 EUR net Nov 2025, billed to INSTAL SA entity — clarify). **Open: sign Nov-2025 TIG; confirm Part 2 status.** Dev: Szabó Andor. Contact: Becze Szabolcs. [[Accounts/Active/Melinda_Steel/NOTES]]
- [ ] **MVMI — Azure DevOps Managed Service** #mvmi #energy #azure-devops #managed-service #lang-hu @{2026-06-15} L3 SLA support, critical bugs in 8h, containerization consulting, developer enablement 5x11. Per MVMI top-level NOTES: "needs to start ASAP" flag — verify with Kardos Sanyi if Delivery is the right stage or this is still Contracted-pre-kickoff. [[Accounts/Active/MVMI/AzureDevOps Managed Service/NOTES]]
- [ ] **MVMI — Omni Support (OpenShift)** #mvmi #energy #openshift #omni-support #lang-hu @{2026-06-15} OpenShift platform support engagement (cs-001 published case study): moved quarterly → bi-weekly releases, zero downtime for 3M+ households. Long-standing. [[Accounts/Active/MVMI/Omni Support/NOTES]]
- [ ] **MVMI — Chaos Engineering Workshop** #mvmi #energy #chaos-engineering #workshop #lang-hu @{2026-06-15} Sub-engagement under Omni Support. Specific workshop deliverable (verify status — could be Delivery if ongoing or Closed if one-off completed). [[Accounts/Active/MVMI/Omni Support/Chaos Engineering Workshop/NOTES]]
- [ ] **Onriva** #onriva #travel #aws #managed-service @{2026-06-15} Travel-tech AWS operations (cs-003 published case study). Reference account. [[Accounts/Active/Onriva/NOTES]]
- [ ] **Observer** #observer #media #aws #migration @{2026-06-15} Media AWS migration (cs-002 published case study). [[Accounts/Active/Observer/NOTES]]
- [ ] **OKFO** #okfo #public-sector #azure-devops #managed-service #lang-hu @{2026-06-15} Azure DevOps install + managed service (cs-005 published case study). Reference account for Azure DevOps managed-service pitches (used in CIG Pannonia outreach Option G). [[Accounts/Active/OKFO/NOTES]]
- [ ] **Direct Travel** #direct-travel #travel #managed-service @{2026-06-15} Active engagement — see NOTES for current state, contacts, and package. [[Accounts/Active/Direct_Travel/NOTES]]
- [ ] **Diligentes** #diligentes #managed-service @{2026-06-15} Active engagement — see NOTES for current state, contacts, and package. [[Accounts/Active/Diligentes/NOTES]]
- [ ] **Colosseum Dental** #colosseum-dental #healthcare-tech #managed-service @{2026-06-15} Active engagement — see NOTES for current state, contacts, and package. [[Accounts/Active/Colosseum_Dental/NOTES]]
- [ ] **Green Hill SynLab** #green-hill-synlab #healthcare-tech #managed-service @{2026-06-15} Active engagement — see NOTES for current state, contacts, and package. [[Accounts/Active/Green_Hill_SynLab/NOTES]]
- [ ] **Jumeon** #jumeon #managed-service @{2026-06-15} Active engagement — see NOTES for current state, contacts, and package. [[Accounts/Active/Jumeon/NOTES]]
- [ ] **ProSharp** #prosharp #managed-service @{2026-06-15} Active engagement — see NOTES for current state, contacts, and package. [[Accounts/Active/ProSharp/NOTES]]
- [ ] **SocialBud** #socialbud #managed-service @{2026-06-15} Active engagement — see NOTES for current state, contacts, and package. [[Accounts/Active/SocialBud/NOTES]]


## Renewal



## Closed



## Lost




%% kanban:settings
```
{"kanban-plugin":"board","list-collapse":[false,false,false,false,false,false,false,false,false,false],"new-note-folder":"Accounts/Active","lane-width":280,"show-checkboxes":true}
```
%%
