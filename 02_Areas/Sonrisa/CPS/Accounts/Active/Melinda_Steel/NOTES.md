---
type: account
id: melinda-steel
company: "Melinda Impex Steel SA"
project: "WhatsApp-based Quoting Chatbot (Ügyfélfelé Ajánlatkérő)"
stage: delivery
status: active
unit_display: "Cloud Platform Services"
unit_short: "CPS"
description: "Separate CPS engagement with MELINDA IMPEX STEEL SA (sister company to Melinda Impex Instal SA, also Odorheiu Secuiesc / Harghita, RO). Project: a WhatsApp-based automated quoting chatbot for Melinda Steel's steel-industry customers, who currently request quotes by phone/email. Built by Sonrisa CPS / CloudGuild on n8n + Azure Communication Services + LLM. PoC Aug 2025, framework + order signed 2025-11-20 (MELS-SON-K2025), Part 2 WhatsApp integration Apr 2026. T&M billing. NOT the Melinda Instal mobile-app project."
tags: [melinda-steel, romania, whatsapp, chatbot, quoting, automation, n8n, azure-communication-services, llm, cps, cloudguild, t-and-m, lang-hu, lang-ro]
geo: RO
language: [hu, ro]

# At-a-glance (AM board card)
strategic_directions:
  - "WhatsApp-based automated quoting chatbot for steel-industry B2B customers"
  - "CPS / CloudGuild delivery on n8n + Azure Communication Services + LLM"
  - "Phased: Part 1 client-quoting automation → Part 2 WhatsApp integration"
next_step: "Confirm current phase status (Part 2 WhatsApp integration, proposal v1.0 Apr 2026) + sign the Nov 2025 Teljesítés Igazolás (TIG awaiting signature)"
deadline: null
blocker: "Melinda_Steels_TIG_2025.11 awaiting signature (as of 2025-12-02)"
top_todos:
  - "Get the 2025-11 Teljesítés Igazolás signed (MELS-SON-K2025)"
  - "Confirm Part 2 (WhatsApp integration) scope + status — proposal v1.0 dated 2026-04-13"
  - "Clarify billing entity (invoices issued to Melinda Impex INSTAL SA, not Steel)"

# Commercial
contract: "MELS-SON-K2025"
contract_signed: 2025-11-20
contract_type: "T&M (Cloud Platform Services)"
sharepoint_folder: "https://sonrisakft.sharepoint.com/sites/sales/Megosztott dokumentumok/General/Accounts/Melinda Steel"
created: 2026-05-28
last_signal: 2026-04-23
last_synced_from_sharepoint: 2026-05-28
---

# Melinda Impex Steel SA — WhatsApp Quoting Chatbot

> **Status 2026-05-28:** Separate CPS/CloudGuild engagement, introduced to the board today. Distinct from the Melinda Instal mobile-app project (different company, different contract). Signed 2025-11-20, T&M, currently in the WhatsApp-integration phase (Part 2).

## Quick Info

| Field | Value |
|-------|-------|
| **Client** | MELINDA IMPEX STEEL SA (RO, Str. Beclean Nr. 316, Odorheiu Secuiesc, Harghita) — sister of Melinda Impex Instal SA |
| **Contractor** | Sonrisa Informatikai Kft. |
| **Project** | WhatsApp-based automated quoting chatbot (Ügyfélfelé Ajánlatkérő) |
| **Unit** | CPS / CloudGuild |
| **Contract** | MELS-SON-K2025 (framework + order, signed 2025-11-20) |
| **Type** | T&M (Cloud Platform Services) |
| **Contact** | Becze Szabolcs (becze.szabolcs@sonrisa.hu, +40 740 507 135) |
| **Developer** | Szabó Andor (per Skillmatrix profile) |
| **Tech** | n8n + Azure Communication Services + LLM |

## What Is This Account

**Melinda Impex Steel SA** is a Romanian steel-industry distributor (sister company to Melinda Impex Instal SA). Their customers currently request quotes for steel products by phone or email — a manual, slow process.

The project automates this: a **WhatsApp-based quoting chatbot** that receives customer quote requests via WhatsApp, processes them (LLM + n8n workflow), and generates/returns quotes. Built and operated by Sonrisa CPS / CloudGuild.

## The Project (phases)

- **Part 1 — Client quoting automation** (`action_plan_client_quoting.md`, cloudguild site): automate processing of incoming price-quote requests. Azure Communication Services for the WhatsApp channel.
- **Part 2 — WhatsApp integration** (`Technikai_Ajanlat_MelindaSteel_WhatsApp_v1.0.docx`, 2026-04-13 + `n8n - integration part 2.xlsx`): the WhatsApp integration build, task breakdown via n8n.

Input examples (real customer WhatsApp messages / images) collected for training/testing (`Melinda examples.zip`, cloudguild site).

## Tech / Integrations

- **n8n** — workflow automation orchestrating the quote pipeline
- **Azure Communication Services** — WhatsApp channel integration
- **LLM** — parse incoming quote requests, generate responses
- Likely connects to Melinda Steel's product/pricing data (export/API — flagged as a question in the action plan)

## Commercial / Billing

- Contract: **MELS-SON-K2025**, signed 2025-11-20, T&M.
- Invoices (Nov 2025, ~5,320 EUR net): **E-2025-559** (+5,320), **E-2025-562** (-5,320 storno), **E-2025-563** (+5,320). Net ~5,320 EUR for the period.
- **NOTE:** invoices were issued to **MELINDA IMPEX INSTAL SA** (the billing entity), even though the project is for Melinda Steel. Confirm the billing-entity arrangement.
- **Teljesítés Igazolás** `Melinda_Steels_TIG_2025.11_ aláírásra.pdf` (2025-12-02) — completion cert for the Nov 2025 period, **awaiting signature** (note: filed under the Melinda Instal/Számlák folder, slightly misfiled).

## People

| Name | Role |
|------|------|
| Becze Szabolcs | Sonrisa CPS contact / owner |
| Szabó Andor | Developer (quote-processing automation) |
| Pap Dávid | Involved in PoC discussion (Aug 2025) |

## Key History

- 2025-08-29: PoC discussion (`melinda steel poc atbeszelles.loop`, Pap Dávid)
- 2025-10-03: early CPS offer (`Book.xlsx`, Planning/CPS/offers/Melinda)
- 2025-11-13: framework agreement + order form drafted
- 2025-11-20: contract signed (`Contr. Sonrisa-Melinda Steel_signed.pdf`)
- 2025-11-24/25: invoices E-2025-559/562/563 (~5,320 EUR net t&m)
- 2025-12-02: Teljesítés Igazolás for Nov 2025 (awaiting signature)
- 2026-04: Part 2 WhatsApp integration (technical proposal v1.0 + n8n task breakdown, input examples collected)

## Open Items

- [ ] **Sign the Nov 2025 TIG** (Teljesítés Igazolás, MELS-SON-K2025). 📅 2026-05-28 #status
- [ ] **Part 2 (WhatsApp integration) status** — proposal v1.0 from 2026-04-13; confirm where it stands. 📅 2026-05-28 #status
- [ ] **Billing entity** — invoices to MELINDA IMPEX INSTAL SA, project for Steel; clarify the arrangement. 📅 2026-05-29 #finance
- [ ] **TIG misfiled** — `Melinda_Steels_TIG_2025.11` is in the Melinda Instal/Számlák folder; should move to Melinda Steel/Számlák. 📅 #hygiene

## Related Documents (SharePoint — re-sync source)

> Folder: `sites/sales/.../General/Accounts/Melinda Steel`. Also: `sites/cloudguild/.../Melinda Steel` (technical workspace).

| Document | SharePoint |
|---|---|
| Signed contract | `Accounts/Melinda Steel/signed/Contr. Sonrisa-Melinda Steel_signed.pdf` |
| Framework agreement + order form | `Accounts/Melinda Steel/` |
| WhatsApp technical proposal v1.0 | `Accounts/Melinda Steel/Part 2 WhatsApp integration/` |
| n8n task breakdown (Part 2) | `Accounts/Melinda Steel/n8n - integration part 2.xlsx` |
| Action plan (client quoting) | `sites/cloudguild/.../Melinda Steel/action_plan_client_quoting.md` |
| Input examples (WhatsApp) | `sites/cloudguild/.../Melinda Steel/Input examples/` |
| Invoice E-2025-559 | `Accounts/Melinda Steel/Számlák/E-2025-559 MELINDA IMPEX INSTAL SA.pdf` |

## Next Step

Confirm the current Part 2 (WhatsApp integration) status and get the Nov 2025 Teljesítés Igazolás signed. Clarify the billing-entity arrangement (invoices to Instal SA for a Steel project).
