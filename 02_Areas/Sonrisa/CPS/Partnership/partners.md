---
# ===========================================================================
# CPS Partnerships board, dashboard source. Read by Partnership/dashboard.html
# every 8 seconds. Edit here in Obsidian; the dashboard reflects changes live.
# Deep reference material stays in AWS/, Oracle/, Azure/ subfolders.
# ===========================================================================
type: partner-board
title: CPS Technology Partnerships
updated: 2026-05-20
partners:
  - vendor: AWS
    status: active
    accent: "#FF9900"
    program: "AWS Partner Network (APN)"
    tier: "Select Tier Partner"
    renewal: ""
    annual_fee: ""
    certs_active: 3
    certs_target: 4
    accredited: 7
    summary: "APN Select Tier plus Ingram Micro Premier channel. 7 accredited individuals, 3 active certs."
    requirements:
      - label: "Accredited Individuals"
        current: 7
        required: 4
        met: true
      - label: "Technical accreditations"
        current: 5
        required: 2
        met: true
      - label: "Business accreditations"
        current: 4
        required: 2
        met: true
      - label: "Foundational Certified"
        current: 12
        required: 2
        met: true
      - label: "Technical Certified"
        current: 1
        required: 2
        met: false
    gaps:
      - "Need 1 more AWS Technical Certified individual"
    contacts:
      - name: "Ingram Micro"
        role: "Channel Partner, Premier. 8% discount, 60-day terms, shared opportunities"
    next_actions:
      - "Torok Balint, AWS Security Specialty (planned, fills the Technical Certified gap and adds first Specialty)"
    source_files:
      - "AWS/certifications.md"
      - "AWS/Ingram Micro.md"
  - vendor: Oracle
    status: active
    accent: "#C74634"
    program: "Oracle Partner Network (OPN)"
    tier: "Level 1 Principal Partner"
    renewal: 2027-04-28
    annual_fee: "USD 5,000 / year"
    certs_active: 0
    certs_target: 0
    accredited: 0
    summary: "OPN Level 1 Principal Partner, approved 2026-05-08. 5 training seats, Marketplace listing access."
    requirements:
      - label: "Membership active"
        current: 1
        required: 1
        met: true
      - label: "Training seats used"
        current: 0
        required: 5
        met: false
    gaps:
      - "Use the 5 Oracle University training seats (sales and delivery readiness)"
      - "Submit target accounts to the CCE system for Oracle territory matching"
    contacts:
      - name: "Csitneki Attila"
        role: "Alliances and Channel PSAM, Oracle Hungary"
      - name: "Kiss Orsi"
        role: "Oracle specialist, Arrow ECS Kft. (distributor), can assist with enabler/tenancy"
      - name: "Szabolcs"
        role: "Sonrisa Partner Administrator (becze.szabolcs@sonrisa.hu)"
    next_actions:
      - "[NEXT WEEK / strategic] File 'Test and Dev order' Partner Help ticket (Category: Go-to-Market > Partner Programs) to buy Universal Credits at 55% discount for dev/test/demo + internal dev/test. First clarify: can existing tenancy cps_admin@sonrisa.hu be used, or is a NEW OPN environment required (no mixing production/non-production)? Complete the UC Request Template. Contacts: Csitneki Attila + Kiss Orsi (Arrow ECS). Ref guide a_id 1020948."
      - "Extract Oracle case studies + create Rozs Robert DB-expert profile (see Strategy/Oracle tudas.md)"
      - "Scope the Oracle capabilities landing page"
      - "Display Oracle Partner logo on sonrisa.hu (pending)"
      - "Earn Partner Credits so year-2 renewal can be paid with credits instead of USD 5,000"
    source_files:
      - "Oracle/Oracle Partnership.md"
  - vendor: Azure
    status: in_progress
    accent: "#0078D4"
    program: "Microsoft Cloud Partner Program"
    tier: "Solutions Partner designation in progress"
    renewal: ""
    annual_fee: ""
    certs_active: 0
    certs_target: 2
    accredited: 0
    summary: "No formal partnership yet. Solutions Partner designation in progress, zero certs on file."
    requirements:
      - label: "Azure Certified Individuals"
        current: 0
        required: 2
        met: false
    gaps:
      - "No Azure / Microsoft certifications on file"
      - "Solutions Partner designation not yet earned"
    contacts: []
    next_actions:
      - "Decide whether to formalize the Microsoft partnership and assign cert owners"
    source_files: []
---

# CPS Technology Partnerships

Live data for the partner-health board lives in the frontmatter above. Edit it in Obsidian and `Partnership/dashboard.html` reflects the change within 8 seconds.

Deep reference material:
- **AWS**: `AWS/certifications.md`, `AWS/Ingram Micro.md`
- **Oracle**: `Oracle/Oracle Partnership.md`, `Oracle/eOPN Program Pitch_2025_October.pptx`
- **Azure**: no folder yet, create `Azure/` when the Microsoft partnership is formalized.

## Editing notes

- `status`: `active`, `in_progress`, or `none`.
- `certs_active` / `certs_target`: drives the certification coverage bar.
- `requirements[]`: each row renders in the requirements list with a met / gap marker. Set `met: true` or `met: false`.
- `renewal`: a `YYYY-MM-DD` date drives the renewal countdown. Leave `""` if not applicable.
- `accent`: the vendor brand color used for the card's top stripe.
