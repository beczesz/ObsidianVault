---
title: AWS Cost Health Check
version: 0.2
date: 2026-01-23
author: Sonrisa - Cloud Platform Services (CPS)
description: Internal service documentation defining the intent, strategy, scope, and execution model of the AWS Cost Health Check service
---

# AWS Cost Health Check

**Internal Service Documentation – v0.2**

---

## 1. Purpose of This Document

This document defines the **intent, strategy, scope, and execution model** of the **AWS Cost Health Check** service.

Its primary goal is **alignment**:

- alignment between sales and delivery,
- alignment between strategy and execution,
- alignment between what we _offer_ and what we _actually deliver_.

This service is **not** a goodwill exercise.  
It is a **strategic wedge** into long-term, high-quality CPS engagements.

---

## 2. Why We Are Doing This

### 2.1 Strategic Motivation

The AWS Cost Health Check exists to solve three internal problems simultaneously:

1. **Cold entry into accounts is inefficient**
    - Managed services are hard to sell without context.
    - Buyers resist long-term commitments without proof.

2. **Cost pain is universal and urgent**
    - Cloud cost is one of the few problems that:
        - affects Finance, Engineering, and Leadership at once,
        - has visible monthly impact,
        - creates immediate executive attention.

3. **We need a low-risk way to qualify clients**
    - Not every company is a good CPS customer.
    - We need a controlled mechanism to:
        - assess technical maturity,
        - assess collaboration quality,
        - assess long-term fit.

The Cost Health Check addresses all three.

---

### 2.2 What This Service Is _Not_

Internally, it is critical to understand what this service is **not**:

- It is **not** a full FinOps audit.
- It is **not** a consulting engagement.
- It is **not** a cost optimization project.
- It is **not** free engineering work.
- It is **not** a replacement for paid discovery.

It is a **signal extraction exercise**.

---

## 3. Strategic Intent

### 3.1 Primary Intent

The primary intent of the AWS Cost Health Check is to:

> Create a credible, low-friction technical entry point that naturally leads into CPS Growth or Scale engagements.

Everything else is secondary.

---

### 3.2 Secondary Intents

Second-order objectives include:

- **Sales qualification**
    - Identify whether the client:
        - has real production workloads,
        - has decision-making clarity,
        - can act on findings.

- **Learning loop**
    - Capture anonymized patterns:
        - recurring waste types,
        - industry-specific anti-patterns,
        - maturity indicators.
    - Feed these back into:
        - CPS playbooks,
        - automation opportunities,
        - future offerings.

- **Brand positioning**
    - Position Sonrisa as:
        - pragmatic,
        - technically deep,
        - aligned with both Finance and Engineering.

---

## 4. Sales Strategy Behind the Service

### 4.1 Role in the Sales Funnel

The AWS Cost Health Check sits **between marketing and CPS Growth**.

It is not top-of-funnel content.  
It is **mid-funnel qualification**.

Typical flow:

1. Awareness (content, referrals, outbound)
2. Cost Health Check (this service)
3. Decision fork:
    - DIY → no resentment
    - CPS Growth / Scale → ideal outcome

---

### 4.2 What Sales Is Actually Selling

Sales is **not** selling cost savings.

Sales is selling:

- clarity,
- reduced uncertainty,
- a safe first step.

Savings are the _vehicle_, not the product.

---

### 4.3 Qualification Criteria (Implicit but Real)

Sales should only offer this service if **at least most** of the following are true:

- AWS production environment exists
- Monthly AWS spend is non-trivial
- There is some internal confusion or frustration around cost
- A technical contact can grant read-only access
- A business or finance stakeholder is at least aware

If these are missing, conversion probability is low.

---

### 4.4 Disqualification Is a Feature

If, after the Health Check:

- the client is disorganized,
- unresponsive,
- unwilling to act,
- or purely price-shopping,

**we still win**:

- no long-term commitment,
- minimal sunk cost,
- valuable learning captured.

---

## 5. Overall Service Strategy

### 5.1 Core Principle: Tight Scope

This service **must remain tightly scoped**.

Scope creep destroys:

- margins,
- engineer focus,
- sales leverage.

The correct internal mindset:

> "Enough insight to create urgency — not enough to solve the problem."

---

### 5.2 Output Philosophy

Outputs must be:

- concise,
- defensible,
- non-prescriptive.

We surface:

- _where_ money leaks,
- _why_ it likely happens,
- _what kind_ of action is required.

We do **not** deliver:

- implementation steps,
- Terraform,
- architectural diagrams,
- effort estimates.

---

## 6. Technical Strategy

The AWS Cost Health Check is implemented through a **layered technical pipeline** that combines read-only data extraction, AI-assisted analysis on private infrastructure, and mandatory human validation.  
The strategy is intentionally designed to maximize insight quality while minimizing operational risk, scope creep, and client disruption.

At no stage does the service modify client infrastructure, apply optimizations, or require production-level access.

---

### 6.1 Access Model and Data Extraction

The service operates exclusively on **read-only access** to the client's AWS environment, limited to billing, cost, and optimization metadata.

**Access principles:**

- Read-only IAM role
- No write permissions
- No application, workload, or traffic-level access
- No persistent integrations beyond the assessment period
- Optional NDA or contractual agreement prior to access

**Primary AWS data sources:**

- AWS Cost Explorer (historical spend and aggregation)
- Cost & Usage Report (CUR), if available
- AWS Trusted Advisor (cost-related signals only)
- AWS Compute Optimizer (utilization and rightsizing signals)

Data is collected via **dedicated AWS data extraction components** (scripts, collectors, or jobs) that:

- retrieve historical cost and usage data
- normalize currency, time range, and service categorization
- aggregate data at service, account, and usage-pattern level

The output of this stage is a **raw technical cost dataset** describing:

- where costs originate
- how they evolve over time
- which services, accounts, or usage types dominate spend

No interpretation, recommendations, or business conclusions are made at this stage.

---

### 6.2 MCP-Based AI Analysis on Private Infrastructure

All AI-assisted processing is performed using a **self-hosted Minimax 2.1 open-source large language model**, running entirely on Sonrisa-controlled hardware.

This ensures:

- client data never leaves Sonrisa infrastructure
- no third-party AI providers are involved
- enterprise-grade data confidentiality and sovereignty

#### Model Context Protocol (MCP)

A **Model Context Protocol (MCP)** layer is used as the formal interface between:

- AWS-derived cost data
- and the AI analysis layer

MCP provides:

- structured, scoped context delivery
- clear separation between data extraction and reasoning
- controlled exposure of client data to AI agents

#### Technical Insight Generation (Raw Analysis Layer)

The first AI pass consumes MCP-exposed cost data and produces a **technical analysis draft**.

Its purpose is to:

- detect recurring cost patterns
- identify structural FinOps and engineering anti-patterns
- surface candidate optimization signals (e.g. commitment gaps, over-provisioning tendencies, governance issues)

Important constraints:

- AI output is exploratory, not authoritative
- Findings are framed as signals and hypotheses
- No guarantees, savings claims, or implementation steps are generated

The result is a **raw, technical AI-generated report**, suitable only for internal review.

---

### 6.3 Human Validation, Executive Synthesis, and Final Output

Human review is a **mandatory control gate** and cannot be skipped.

A senior technical reviewer:

- validates AI-generated observations
- removes false positives and low-signal findings
- ensures conclusions align with real-world AWS and FinOps behavior
- verifies that no prescriptive or contractual language is introduced

Only validated findings proceed to the executive synthesis stage.

#### Executive Report Generation

A second AI agent is then applied using a **strictly customized prompt** that defines:

- company branding
- document structure and section hierarchy
- executive-level tone and vocabulary
- explicit rules against promises or implementation guidance

This agent transforms validated technical findings into an **executive-readable narrative**, including:

- cost landscape overview
- dominant structural signals
- explanation of why costs persist
- high-level decision options (e.g. leave as-is, address internally, engage CPS)

The generated executive report is reviewed once more by a technical owner to ensure:

- technical accuracy is preserved
- messaging remains non-prescriptive
- scope boundaries are respected

---

### 6.4 Deliverables and Time Constraints

The final deliverable is a **PDF-based executive report** designed to be:

- concise and defensible
- understandable by Finance, Engineering, and Leadership
- actionable at a decision level, not an implementation level

Total end-to-end effort per client is intentionally capped at **3–4 hours**, including:

- client coordination and access setup
- contractual or NDA formalities
- data extraction
- AI-assisted analysis
- human validation
- report generation
- delivery discussion

This strict time and scope limitation is essential to:

- preserve scalability
- prevent unpaid consulting
- maintain the service's role as a qualification and trust-building mechanism

---

## 7. Delivery Guardrails

### 7.1 What We Explicitly Do Not Say

During delivery, we must avoid:

- "This is easy to fix"
- "We can save you exactly X euros"
- "You should definitely do Y"
- "This will pay for itself in Z months"

We deal in **signals and options**, not guarantees.

---

### 7.2 Step 3 Conversation Framing

The final conversation must always end with:

- "Here is what we found"
- "Here is why it matters"
- "Here are your options"

Options must always include:

- acting internally,
- continuing with Sonrisa.

No pressure. No manipulation.

---

## 8. Relationship to CPS Packages

### 8.1 Why CPS Growth Is the Natural Next Step

CPS Growth works well because:

- cost optimization is ongoing, not one-off,
- savings decay without enforcement,
- governance matters more than fixes.

The Health Check creates the **problem awareness**;  
CPS provides the **ongoing protection**.

---

### 8.2 "Self-Funding" Narrative (Internal Alignment)

Internally, we understand this clearly:

- Savings are not guaranteed.
- "Self-funding" is a **pattern**, not a promise.

Sales may explain this conceptually, but must never present it as a guarantee.

---

## 9. Success Criteria (Internal)

The AWS Cost Health Check is successful if:

- It leads to a CPS Growth or Scale engagement  
    **OR**
- It cleanly disqualifies a poor-fit client  
    **OR**
- It produces a reusable insight for CPS improvement

If none of these happen, the execution failed.

---

## 10. Risks and Mitigations

### 10.1 Scope Creep

**Risk:** Engineers over-deliver.  
**Mitigation:** Clear internal time cap and output template.

### 10.2 Sales Overpromising

**Risk:** "Free audit" becomes "free consulting."  
**Mitigation:** Sales playbook + consistent language.

### 10.3 Perceived Value Dilution

**Risk:** Free feels cheap.  
**Mitigation:** Tight eligibility, professional delivery, clear boundaries.

---

## 11. Versioning & Evolution

This is **v0.2**.

Expected future iterations:

- v0.3: inclusion of sample anonymized outputs
- v1.0: standardized internal report template
- v1.x: automation support and pattern library

Changes must always preserve:

- tight scope,
- strategic intent,
- CPS upsell integrity.

---

## Final Internal Summary

The AWS Cost Health Check is:

- a **strategic wedge**, not a giveaway,
- a **qualification tool**, not a service substitute,
- a **learning engine**, not just a sales tactic.

If executed with discipline, it will:

- shorten sales cycles,
- improve client quality,
- and strengthen CPS positioning long-term.

This document exists to ensure that discipline.