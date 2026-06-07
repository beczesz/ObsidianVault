---
title: Intelligent Email Routing — Executive Summary (for Merkantil)
date: 2026-05-11
author: Bán József
status: sent
description: EN executive summary of the proposed n8n + on-prem LLM agentic email router for Merkantil customer-email triage. Sent to Merkantil 2026-05-13 (linked from the AI enablement commercial proposal). Source: exec_summary_merkantil_intelligent_email_rounting.docx.
tags: [merkantil, email-router, exec-summary, sent]
source_file: "C:\\Users\\EvoComputers\\Downloads\\exec_summary_merkantil_intelligent_email_rounting.docx"
extracted: 2026-05-27
id: ad1f260f-f78a-4b8f-a6e7-7965dce22ff8
index_schema_version: 1
---

# Intelligent Email Routing

**Agentic AI for Customer Communication Triage**
**for Merkantil**
**2026.05.11.**

## 1. Intelligent Email Routing

### 1.1 Scope

Merkantil receives a large volume of customer emails daily covering a broad range of topics — card issues, loan inquiries, KYC compliance, investment advice, insurance, complaints, and more. Today, dedicated staff read each incoming email, determine which department should handle it, and forward it manually. This manual triage process is the focus of this initiative.

### 1.2 From Manual to Intelligent

Manual email triage is slow, expensive, and error prone. Emails sent to the wrong department require correction, adding hours or days to resolution time and directly impacting customer satisfaction. The work itself is largely mechanical — skilled staff spend significant time on routing decisions that deliver little value relative to their expertise. Because manual decisions are rarely logged in a structured way, quality control and compliance review are difficult.

### 1.3 Proposed Solution

An agentic AI email router that reads incoming emails, classifies them against a structured ruleset, and routes them to the correct department automatically or escalates to a human operator when the decision is uncertain.

When an email arrives, the agent reads the full message and scores it against a declarative, keyword-based ruleset. Each department is represented by a set of weighted terms and contextual rules; the agent tallies scores, applies multipliers for urgency or customer type, and checks for priority override conditions such as fraud signals or legal escalation language. If the top-scoring department is clearly ahead and the overall confidence exceeds the configured threshold, the email is routed automatically. If the result is ambiguous — two departments scoring closely, or overall confidence too low — the agent escalates to a human operator rather than guessing.

Every decision produces a structured output containing the routing target, confidence score, matched keywords, priority level, and a one-line summary of the customer's request. This makes every routing action fully traceable and auditable.

The ruleset itself is a plain-text, declarative configuration. Departments, keywords, scores, and thresholds can be updated by business users without IT involvement — no model retraining, no code deployment. This means the system adapts as Merkantil's department structure and product portfolio evolve.

#### Design Principles

- **Transparency**: every routing decision is explained — not just where an email went, but why, with scores and evidence.
- **Safe degradation**: the agent is designed to recognize its own uncertainty and hand off to a human rather than route incorrectly.
- **Adaptability**: the classification configuration is fully editable by the business, making the system as flexible as Merkantil needs it to be.

### 1.4 Expected Outcomes

The primary goal is a significant reduction in misrouted emails, with the residual ambiguous cases caught by the human-in-the-loop mechanism rather than silently misclassified. Beyond accuracy, the solution frees triage staff from mechanical routing work and produces a complete audit log of every decision — something manual triage does not provide. Baseline metrics will be established before go-live to allow direct before/after comparison.

### 1.5 Delivery

The solution will be built on **n8n**, an open-source workflow automation platform that allows rapid assembly of integrations without heavy development overhead. n8n is well-suited here because it natively connects to email systems, supports AI agent nodes out of the box, and exposes each step of the workflow visually — making it easy to inspect, adjust, and hand over to Merkantil's team.

Integration points are kept minimal by design. On the input side, n8n connects to Merkantil's existing email infrastructure via an Outlook trigger, picking up incoming messages as they arrive. For inference, the agent calls Merkantil's on-premises LLM server — no external API, no data leaving the bank's network. On the output side, the routing decision is written as a structured record that can feed into a ticketing system, a shared inbox, or any downstream process Merkantil already operates. The timeline for delivery is to be defined.

### 1.6 Work Items

| # | Task | Description |
|---|------|-------------|
| 1 | Discovery & Baseline | Current-process documentation, baseline metrics, historical email collection, and KPI definition. |
| 2 | Infrastructure & Installation | Set up n8n, connect to KodeSage LLM endpoint, configure Outlook/Exchange access, and provision output channels and Human in the Loop (HITL) queue. |
| 3 | Department Configuration | Finalize department list with IDs, descriptions, and queues; validate with department leads; assign ongoing ownership. |
| 4 | Ruleset Definition | Analyze historical emails for keyword patterns, draft scoring rules and multipliers, define priority overrides, and review with SMEs. |
| 5 | Agent Configuration | Adapt the system prompt, define language and attachment policies, design email chain handling, build the end-to-end n8n workflow. |
| 6 | Testing | Benchmark against historical routing decisions, test edge cases and failure modes, run UAT with the triage team. |
| 7 | Fine-Tuning | Adjust keyword scores, thresholds, and override rules based on test results; iterate until acceptance criteria are met. |
| 8 | Integration & Go-Live Preparation | Connect live email trigger, set up logging and alerting, brief departments, train the triage team, agree on rollback plan. |
| 9 | Monitoring & Continuous Improvement | Track routing accuracy and HITL rates post-launch, collect operator overrides as feedback, report on value delivered vs. baseline. |

### Scope Remarks

Attachment handling is not in scope for the initial delivery and planned for a second phase, once the core routing solution is live and validated. In the initial phase, emails where the critical context is in an attachment are routed based on body text alone.
