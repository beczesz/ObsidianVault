---
title: "In-House or Managed DevOps: Five Questions That Decide It"
date: 2026-03-25
author: Becze Szabolcs
status: active
description: "Framework for DevOps leaders and CTOs to decide between in-house and managed services based on company stage, expertise breadth, hiring timeline, staff availability, and whether infrastructure is core to the product. Includes decision matrices and honest cost comparisons."
description_source: auto
description_hash: e1a684fe72be9cc8
id: 914dfd89-8e72-416a-94f6-96df8b86ddc5
index_schema_version: 1
bdos_index: true
---
# In-House or Managed DevOps: Five Questions That Decide It

**Series:** Managed Service Series - Article 2 of 3
**Reading time:** ~5 minutes
**Target:** CTOs, VP Engineering, IT Directors (20-500 employees)

---

Most companies never actually decide between managed DevOps and in-house. They drift into one or the other.

A deployment breaks. Someone gets hired to fix it. A vendor gets called because no one is available. Six months later, leadership realises the infrastructure model was never a deliberate choice -- it just accumulated.

Drifting into an infrastructure strategy is not the same as having one. And the cost of discovering that difference during a crisis is always higher than the cost of thinking it through in advance.

This article gives you five questions that force a real decision. Not based on vendor preferences or received wisdom -- based on where your company actually is right now.

---

## First: Understand What You Are Really Choosing Between

This is not a technical decision. It is a strategic one about where infrastructure risk sits in your organisation.

**Hiring in-house** is a commitment to finding and retaining the right people over time. You get deep context, institutional alignment, and someone who knows every corner of your environment. What you are betting against: that those people stay, that you can hire replacements quickly when they do not, and that one or two people can sustainably cover the breadth of modern cloud operations.

**A managed service** is a commitment to operational continuity independent of individual headcount. You get a team, breadth of expertise, and resilience that does not depend on any single person's availability. What you are betting against: that an external team can develop enough context about your specific environment to be genuinely useful.

**Neither is universally better.** They are different bets. The question is which bet fits your current situation.

> If you want to understand the specific risks of the single-engineer model in detail, the first article in this series covers them directly: [Why One DevOps Engineer Is Never Enough](https://sonrisa.hu/en/our-impact/article/why-one-devops-engineer-is-never-enough/18)

---

## Five Questions That Tell You Where to Go

Answer each one honestly. Taken together, they will point you in a clear direction.

---

### Question 1: What stage is your company at?

| Company Stage | Typical Best Fit | Reason |
|---|---|---|
| **Startup / scale-up (<50 people)** | Managed service | You need breadth and resilience, not another headcount |
| **Growing fast (50-200 people)** | Managed or hybrid | You need capability now, not in 6 months |
| **Established (200-500 people)** | Hybrid | Internal context plus managed coverage and architecture review |
| **Large (500+ people)** | In-house team | Managed service as specialist backup for specific domains |

Your company stage matters more than most people admit. The right model at 30 people is often the wrong model at 300 -- and the mistake is usually not switching when the stage changes.

---

### Question 2: How many specialties do you actually need?

AWS, GCP, Kubernetes, Terraform, CI/CD tooling, observability, security, compliance, FinOps -- that is eight or nine different disciplines. One engineer covers two or three of them well. Two engineers cover perhaps five.

If your infrastructure spans more specialties than your headcount can realistically cover, you have a structural gap that more hiring alone does not close. A managed service team gives you access to the full spectrum under one contract.

---

### Question 3: How fast do you need this?

Time to hire a senior DevOps engineer: 3-6 months. Time to reach full productivity: add another 1-3 months on top of that.

Time to onboard with a managed service: 2-4 weeks.

If you are solving a problem that exists today -- an upcoming audit, a production instability, an engineer who just left -- hiring is not the solution to that problem. It is the solution to the problem after next.

---

### Question 4: What is your plan when your DevOps person is unavailable?

Holiday. Sick leave. Parental leave. Resignation. These are not edge cases -- they are scheduled certainties and statistical near-certainties over any two-year window.

If your honest answer to "what happens when our DevOps engineer is unavailable?" is some version of "we would figure something out" -- that is not a plan. A managed service provides team continuity by design. Someone else always knows your systems. Someone else is always available.

---

### Question 5: Is infrastructure a core part of your product, or does it support your product?

This is the most important question, and it gets skipped most often.

If infrastructure **is** your product -- you are a hosting provider, a cloud platform, an infrastructure-as-a-service business -- then build an internal team. Full stop. Your competitive advantage lives in the infrastructure itself, and you need ownership and depth that only in-house people can provide.

If infrastructure **supports** your product -- meaning it is the foundation your actual product runs on, but not the thing you sell -- then keeping it entirely in-house may not be the best use of your engineering budget or management attention. The companies with the best products in your category are probably not the ones with the biggest internal DevOps teams.

---

## When Each Option Wins: An Honest Assessment

| | In-House | Managed Service | Hybrid |
|---|---|---|---|
| **Best for** | 200+ employees, DevOps is core | 5-200 employees, scaling fast | 50-500 employees, 1-2 internal engineers |
| **Time to capability** | 4-9 months | 2-4 weeks | Immediate for managed scope |
| **Annual cost** | EUR 100,000-158,000 fully loaded | EUR 24,000-72,000 | Variable, typically lower than full in-house |
| **Breadth of expertise** | 2-3 specialties per hire | Full team coverage | Combined |
| **Continuity risk** | Single point of failure | Team by design | Shared and reduced |

### The Hybrid Model Is Underrated

The most common model among growing companies -- and often the most practical -- is one internal engineer plus managed service coverage for architecture, breadth, and after-hours support.

Your internal engineer owns the day-to-day context and developer relationships. The managed service covers the specialties your engineer does not, handles the on-call rotation, and provides a senior architecture layer that one person cannot credibly do alone.

The result is a function that is genuinely resilient without the cost of building a full internal team. For companies in the 50-500 employee range, this is often the most cost-effective model available.

---

## The Pattern We See Most Often

We have worked with over 50 companies across this decision. A few things come up consistently.

Most companies wait too long. They bring in a managed service after an incident, not before. The companies that operate best have planned for redundancy before they needed it.

The best partnerships are not vendor relationships. When a client's situation genuinely calls for in-house hiring, we say so. Winning for both sides is the only model that sustains over time.

And hybrid is more common than the either/or framing suggests. Most conversations that start as "should we hire or use a managed service?" end with "both, in the right proportion."

---

## Make the Decision Before It Gets Made for You

Every week you operate without a deliberate infrastructure strategy is a week the decision is being made by default. An engineer leaves. A pipeline breaks. A cloud bill arrives. These events will force a decision eventually -- the only question is whether you make it on your terms or under pressure.

If you have read this far, you probably already know which direction makes sense. The next step is understanding what it actually costs.

---

**Next in this series:** [The Hidden Costs of Hiring vs. Managed Services](https://sonrisa.hu/en/our-impact/article/the-hidden-costs-of-hiring-vs-managed-services/23) -- A full cost breakdown that puts real numbers behind both options, including the costs most companies never see until it is too late.
