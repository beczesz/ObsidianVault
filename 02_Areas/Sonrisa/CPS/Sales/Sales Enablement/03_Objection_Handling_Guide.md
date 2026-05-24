---
title: CPS Objection Handling Guide
version: 0.1
date: 2026-03-16
author: Sonrisa - Cloud Platform Services (CPS)
description: Comprehensive guide for handling the most common sales objections when selling CPS managed services
id: 01599f9e-759b-420e-9023-e252ef9c18da
index_schema_version: 1
---

# CPS Objection Handling Guide

## How to Use This Guide

Every objection is a buying signal. The prospect is engaged enough to push back. Your job is not to "win" the argument but to understand the concern behind the objection and address it honestly.

**Framework for every objection:**
1. **Acknowledge** -- validate their concern
2. **Reframe** -- shift the perspective
3. **Evidence** -- provide proof or logic
4. **Bridge** -- move toward next step

---

## Objection #1: "We'll just hire a DevOps person"

**What they're really saying:** "I think a full-time person gives me more control and availability."

**Response:**

"That's a solid option, and many of our clients considered it too. Let me share what we've seen in practice.

A senior DevOps engineer in the EU costs EUR 60,000-90,000/year in salary alone. Add benefits, recruiting fees (typically 2-3 months to find the right person), onboarding time (1-2 months before they're productive), and the risk of them leaving -- you're looking at EUR 80,000-120,000 all-in for your first year, for a single person.

With CPS Growth at EUR 4,000/month (EUR 48,000/year), you get a team of 2-3 engineers who start working immediately, plus backup coverage if someone is sick or on vacation. No single point of failure.

Some of our clients actually started with us while they were recruiting. And a few decided they didn't need to hire after all because the team model worked better for them."

**If they push back further:** "Would it help to start with our Essential package at EUR 2,000/month while you're hiring? That way you're covered now, and when your person starts, you can either downgrade to Safety Net for backup or transition off entirely. No lock-in."

---

## Objection #2: "Your pricing is too high" / "I found cheaper options"

**What they're really saying:** "I don't see enough value to justify this price yet."

**Response:**

"I appreciate you being upfront about that. Can I ask what you're comparing us to?

[If offshore/Indian MSP at EUR 25-35/h:]
You'll find lower hourly rates from offshore providers. The difference is in what you actually get. Our team is EU-based, same timezone, same work culture. We deliver actual engineering -- IaC, CI/CD, architecture -- not just monitoring dashboards and ticket routing. And because we're backed by Sonrisa's 300-person engineering organization, you'll never hit a wall where your provider doesn't have the expertise.

[If comparing to tools like CloudZero, nOps:]
Those are excellent tools, and we use some of them ourselves. But tools give you dashboards and recommendations. We give you engineers who implement the recommendations. The typical 10-30% cost savings we deliver pays for the CPS subscription itself.

[If comparing to a larger MSP at EUR 15K+:]
That's actually a great validation of the market. The large MSPs charge EUR 15-20K minimum because they have heavy overhead. We deliver equivalent engineering depth at a fraction of the cost because our delivery model is lean."

**Key principle:** Never compete on price. Compete on value density -- what they get per euro spent.

---

## Objection #3: "We don't have the budget right now"

**What they're really saying:** Either genuinely no budget, or they haven't prioritized this.

**Response:**

"I understand. Budget is always tight. Let me ask this: if I could show you that you're overspending on AWS by EUR 2,000-5,000 per month, and that fixing it would essentially pay for our service, would that change the equation?

Our free Cost Health Check does exactly that. No commitment, no cost. We analyze your AWS environment and show you where the money is leaking. If the savings are there, the service pays for itself. If not, you'll still walk away with a useful report."

**If genuinely no budget:** "No problem at all. Let me send you our one-pager so you have it when budget planning comes around. And the Cost Health Check offer stands whenever you're ready. Can I check back in [appropriate timeframe]?"

---

## Objection #4: "We need to think about it" / "Let me discuss internally"

**What they're really saying:** Either they need buy-in from others, or they're not convinced yet.

**Response:**

"Of course. These decisions shouldn't be rushed. A couple of questions to help me help you:

Who else would need to be involved in this decision? I'm happy to join a call with your [CTO/CFO/team] to answer technical or financial questions directly.

Is there anything specific you'd want to see before making a decision? A reference call with a similar company, a deeper technical review, a pilot period?

And what's a good date for me to follow up so I'm not chasing you at a bad time?"

**Key:** Always leave with a specific date and a concrete deliverable you'll send them.

---

## Objection #5: "What if we want to cancel?"

**What they're really saying:** "I'm worried about getting locked in."

**Response:**

"Great question. We don't do long-term lock-ins. Our standard terms are month-to-month after an initial 3-month onboarding period. The 3 months are there because it takes that long to properly understand your environment, set up monitoring, and start delivering real value.

After that, you can adjust your package level or end the engagement with 30 days notice. We're confident enough in the value we deliver that we don't need contracts to keep clients.

That said, clients who commit to 12 months get a 10% discount. But that's entirely optional."

---

## Objection #6: "How do we know you'll understand our system?"

**What they're really saying:** "I'm worried about the learning curve and quality."

**Response:**

"That's the most important question, and honestly it's the right concern to have. Here's how we handle it:

First, we start every engagement with a structured onboarding. Our team does a deep-dive into your architecture, your deployment processes, your monitoring, and your team's way of working. We document everything.

Second, you get a dedicated team, not a rotating pool of strangers. The same 2-3 engineers work on your environment consistently, so they build real context over time.

Third, we're backed by 300+ engineers at Sonrisa. If your environment has a specific technology -- Kubernetes, legacy Java, data pipelines -- we can pull in specialists without you having to explain your whole setup to a new person.

And if it helps, we can start with a smaller scope -- say, just monitoring and incident response -- and expand as we earn your trust."

---

## Objection #7: "We already have monitoring tools, why do we need you?"

**What they're really saying:** "We have Datadog/CloudWatch/Grafana, isn't that enough?"

**Response:**

"Monitoring tools are essential, and we work with whatever you already have. But there's a big difference between having alerts and having someone who acts on them intelligently at 2 AM.

Tools tell you something is wrong. We figure out why it's wrong, fix it, document the root cause, and make sure it doesn't happen again. That's the difference between monitoring and managed operations.

We've seen companies with excellent monitoring setups that still have frequent incidents because nobody is proactively tuning thresholds, responding to alerts before they escalate, or doing the unglamorous work of infrastructure hygiene."

---

## Objection #8: "Can you guarantee uptime / SLA numbers?"

**What they're really saying:** "I need to justify this to my boss with concrete promises."

**Response:**

"We provide SLA-backed response times: 12-hour response for standard issues, and optional 24/7 coverage with priority escalation for production-critical environments.

But I want to be honest with you: no managed service provider can guarantee uptime, because uptime depends on many factors including your application code, AWS itself, and architectural decisions. What we can guarantee is our response time, our engineering quality, and our commitment to proactive prevention.

What we do guarantee is that we'll monitor proactively, respond within SLA, and work to continuously improve your infrastructure's reliability. Our goal is to prevent incidents, not just respond to them."

---

## Objection #9: "We're too small / too early for this"

**What they're really saying:** "I'm not sure we need managed services at our scale."

**Response:**

"Actually, smaller companies often get the most value from us, because the alternative is either having your developers do DevOps (which slows product development) or hiring a dedicated person (which is expensive for a small team).

Our Essential package at EUR 2,000/month gives you 40 hours of engineering time. That's less than the cost of a part-time contractor, and you get a full team with diverse expertise.

And here's the thing: the earlier you set up your infrastructure properly, the less technical debt you accumulate. We've seen companies that waited too long and ended up paying 3-5x more to fix problems that could have been prevented."

---

## Objection #10: "We're a regulated industry, can you handle compliance?"

**What they're really saying:** "I need to know you won't create compliance risks."

**Response:**

"Absolutely. Sonrisa has been working with regulated enterprises for 19 years. We have experience with SOC2, ISO 27001, and PCI DSS environments. We worked with Lufthansa and Oracle, both heavily audited organizations.

For compliance-sensitive environments, we offer our DevSecOps add-on (EUR 700/month) which includes continuous security monitoring, vulnerability scanning, and compliance tracking.

We also follow AWS Well-Architected Framework principles, which aligns well with most compliance frameworks. And we can work within your existing security policies rather than imposing our own."

---

## Meta-Objection: "I just don't see why we need external help"

**What they're really saying:** "I'm not aware of the problem, or I'm not feeling it yet."

**Response:**

This is the hardest objection because it means you haven't found their pain point yet. Go back to discovery:

"Fair enough. Let me ask: in the last 6 months, how many hours has your team spent on infrastructure tasks instead of product features? Any production incidents that disrupted your business? Any surprise cloud bills?"

If they genuinely have no pain, they're not a prospect right now. Offer the free Cost Health Check as a no-risk value add and move on. Not everyone is a customer today.

---

## Tone Guidelines

Throughout all objection handling, remember CPS values:

- **Alazat (Humility):** We don't know everything. We don't claim to be the only option. We acknowledge when a prospect might be better served by hiring.
- **Win-win:** If it's not a fit, say so. A honest "no" today builds trust for a "yes" later.
- **No pressure:** Our job is to help them make the right decision, not to close a deal. If CPS isn't right for them, guide them honestly.
