---
title: "24 7 support"
date: 2025-09-09
author: Becze Szabolcs
status: active
description: "Planning document for launching a 24/7 support team covering team composition, shift scheduling, ticketing workflow, KPIs, client onboarding, staff training, documentation management, monitoring setup, and sales strategy for internal stakeholders and leadership."
description_source: auto
description_hash: 5c2377d4b3860b89
id: 5cf94c93-9caa-4b1d-95b2-f708bdf47ca2
index_schema_version: 1
bdos_index: true
---
### 1. Costs
Calculate the costs.
### 2. Team
We need a team of 6-8 people who is willing to be part of this team
We need a Support Lead, who will receive some extra, for keeping the team together.
##### Areas that we need to consider
- Incident handling: if they call us how the tickets would be reported. Ticket lifecycle.
- KPI-s, how to measure the teams performance
	- Zero ticketing system?
- How will we ramp up at clients
- How will we rampup new team members
	- How will they receive credentials
	- Training
	- Access the documentation
- How to maintain the cocumentation
- 24-7 monitoring
- Weekly schedule

### 3. Sales slides
Prepare a presentation. Marketing material. Etc
### 4. Sell to clients
Build on top of MVMI



## 🌐 24/7 Support Team — Readiness Mind Map

---
### 👥 Team Composition & People

- **Support Team Size & Roles**
    - 6–8 people for rotation
    - Clear shift-based scheduling (e.g., 3 shifts/day, 2 people/shift)
- **Support Lead**
    - Responsibility: team cohesion, first-line escalation
    - Compensation: additional allowance or bonus
- **Backup & Flex Pool**
    - On-call staff or rotation-ready alternates
- **HR/Legal**
    - Overtime, night shift, holiday compensation
    - Contracts & NDAs
    - Psychological support & burnout management
### 🧩 Operational Model
- **Shift Scheduling**
    - Rolling calendar (weekly/bi-weekly/monthly view)
    - Weekend/holiday rules
- **Communication & Handover**
    - Use of Microsoft Teams / Slack
    - Shift handover template (notes, pending tickets, risks)
- **Coverage Assurance**
    - Escalation tree (primary, secondary, manager)
    - Geo-distributed or time-zone spread, if applicable
---
### 🆘 Incident & Ticket Handling
- **Ticketing System**
    - Tool: Jira Service Desk, Freshdesk, Zendesk, etc.
    - Ticket lifecycle defined (Open → In Progress → Resolved → Closed)
- **Incident Categories & SLAs**
    - P1/P2/P3 classification
    - Resolution time expectations per level
- **Zero Ticketing?**
    - Define proactive resolution KPIs
    - Auto-resolution & bots
---

### 📊 KPIs & Performance Metrics
- Ticket Resolution Time
- First Response Time
- Escalation Rate
- Uptime % during support hours
- Customer Satisfaction (CSAT) / NPS
- Knowledge base usage & update frequency
---
### 🧪 Client Ramp-Up Process
- **Kickoff & Onboarding**
    - SLA agreement
    - Access provisioning
    - Client-specific tools and environment training
- **Shadowing & Dual Ops**
    - Initial shared responsibility
    - Gradual handover
---
### 👨‍💻 Team Member Onboarding
- **Access Management**
    - Role-based credentials via centralized IAM
    - Audit logs and expiration rules
- **Training Plan**
    - Shadowing → Test environment simulations → Live support
- **Documentation Access**
    - Internal Confluence / SharePoint
    - Bookmarking + internal search guide
---
### 📚 Documentation Lifecycle
- **Living Knowledge Base**
    - Ownership model (each team member owns a section)
    - Versioning and archiving policy
- **Change Management**
    - Integration with incident retrospectives
    - Templates for KB articles
- **AI-assisted documentation**
    - NLP-powered search or RAG-based internal assistants (future)
---
### 🔍 24/7 Monitoring & Observability
- **Tools**
    - Azure Monitor, Datadog, Prometheus/Grafana, New Relic
- **Integration with Alerting**
    - PagerDuty, OpsGenie, SMS, Email
- **Chaos Engineering (optional)**
    - Scheduled failure injection to test alert response
- **Proactive Dashboards**
    - Real-time system health visibility
    - Threshold-based alerts with escalation paths
---
### 🔒 Security & Compliance
- Access segregation (RBAC)
- DevSecOps checks for toolchain
- Logging and audit trail for compliance (ISO, SOC2, etc.)
- NDA, incident disclosure protocols
---
### 📦 Tooling & Platform Readiness
- Internal Developer Portal or Support Toolkit
- Auto-generated reports
- ChatOps (Teams bots, incident status broadcasts)
- Scripting and self-healing workflows
---
### 🧠 Culture, Feedback, and Growth
- **Retrospectives**
    - Weekly/monthly team reflection
- **1-on-1s & Peer Support**
    - Identify burnout, growth paths
- **Recognition**
    - Highlight great interventions, reward initiative
