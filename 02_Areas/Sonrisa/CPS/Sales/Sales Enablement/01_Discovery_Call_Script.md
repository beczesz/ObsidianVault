---
title: CPS Discovery Call Script
version: 0.1
date: 2026-03-16
author: Sonrisa - Cloud Platform Services (CPS)
description: Structured discovery call framework for qualifying and converting prospects into CPS managed service customers
id: 6a7e2499-0ef0-44fd-917e-8ca0338e4f36
index_schema_version: 1
---

# CPS Discovery Call Script

## Pre-Call Preparation (5 min)

Before every call, review:
- Company size (LinkedIn, Crunchbase)
- Tech stack hints (job postings, GitHub, blog)
- Estimated AWS spend if available
- Who you're talking to (CTO, VP Eng, Head of DevOps, CFO)
- How they found us (inbound, referral, outbound, AWS)

## Call Structure (30-45 min)

### 1. Opening (3 min)

**Goal:** Build rapport, set the frame.

> "Hi [Name], thanks for taking the time. I'm [Your Name] from Sonrisa's Cloud Platform Services team. We help companies run their AWS infrastructure reliably without building a full DevOps team internally.
>
> I'd love to learn about your current setup and see if there's a way we could help. Would it be alright if I asked a few questions first, and then I'll share what we do and we can see if it's a fit?"

**Key:** Always ask permission to lead the conversation. It signals respect.

---

### 2. Situation Discovery (10 min)

**Goal:** Understand their current state. Listen more than you talk.

**Infrastructure questions:**

- "Can you walk me through your current cloud setup? Which AWS services are you running?"
- "How many environments do you manage? (dev, staging, production)"
- "Roughly, what's your monthly AWS bill?"
- "Who's currently responsible for managing your infrastructure day-to-day?"

**Team questions:**

- "How big is your DevOps / platform team?"
- "Are your developers doing infrastructure work alongside feature development?"
- "If your main DevOps person left tomorrow, what would happen?"

**Process questions:**

- "How do deployments work today? How often do you deploy?"
- "What does your monitoring and alerting look like?"
- "When was the last time you had a production incident? How did it go?"

---

### 3. Pain Discovery (10 min)

**Goal:** Find the emotional trigger. Cost, risk, or speed.

**Cost pain:**

- "Do you feel like you have good visibility into your AWS costs?"
- "Have you ever been surprised by your monthly bill?"
- "Have you looked into reserved instances or savings plans?"

**Risk pain:**

- "What keeps you up at night about your infrastructure?"
- "Do you have a single point of failure in your DevOps team?"
- "How confident are you in your disaster recovery?"

**Speed pain:**

- "Are infrastructure bottlenecks slowing down your development team?"
- "How long does it take to spin up a new environment?"
- "Is your CI/CD pipeline where you want it to be?"

**The golden question:**

> "If you could fix one thing about your cloud operations tomorrow, what would it be?"

---

### 4. Implication & Urgency (5 min)

**Goal:** Help them quantify the cost of doing nothing.

- "What does that [problem they mentioned] cost you in terms of developer time?"
- "If you had an outage that lasted 4 hours, what's the business impact?"
- "How much engineering time goes into infrastructure instead of product features?"

**Frame the cost of inaction:**

> "So if I'm hearing this right, you're spending roughly [X hours/month] of senior engineering time on infrastructure, which at [Y rate] is about [Z EUR/month]. And you still have the risk of [their stated fear]. Is that a fair summary?"

---

### 5. Solution Presentation (7 min)

**Goal:** Map their pain to a specific CPS package. Do NOT pitch everything.

**Match to their situation:**

| Their Situation | Recommended Package | Monthly Price |
|----------------|---------------------|---------------|
| Have a DevOps person, want backup | Safety Net | EUR 990 |
| Small team, no dedicated DevOps | Essential | EUR 2,000 |
| Growing, need dedicated support | Growth | EUR 4,000 |
| Complex env, multiple teams | Scale | EUR 6,000 |

**Present only the relevant package:**

> "Based on what you've described, I think our [Package] tier would be the right fit. Here's what that looks like..."

**Explain the engagement model briefly:**

1. We start with a Cloud Maturity Review (what's working, what's risky)
2. Onboarding: dedicated team gets up to speed on your environment
3. Ongoing: [X] hours/month of proactive engineering, monitoring, incident response, and optimization
4. Monthly reporting so you see the value delivered

**Mention the Cost Health Check if appropriate:**

> "Actually, before we talk about packages, we offer a free AWS Cost Health Check. It gives you a clear picture of where you're overspending and what the quick wins are. No commitment. Would that be useful as a starting point?"

---

### 6. Objection Handling (5 min)

See the separate Objection Handling Guide for detailed responses to common pushbacks.

**Quick reference for the most common ones:**

**"We're thinking of hiring a DevOps person instead."**
> "That's a great option if you need someone full-time. A senior DevOps engineer in [their region] costs [X/year] plus benefits, recruiting, and ramp-up time. With CPS, you get a team of 2-3 engineers starting immediately, plus backup coverage. Many of our clients started with us while they were hiring, and some found they didn't need to hire after all."

**"Can we try it for a month first?"**
> "Absolutely. We don't require long-term contracts. Start with one month, see the value, and decide from there. Most clients stay because the ROI becomes obvious within the first 30 days."

**"Your pricing is higher than what I've seen."**
> "We're competitive for the EU market, and our pricing includes actual engineering work, not just monitoring dashboards. When you compare us to hiring even one full-time person, the economics are very favorable."

---

### 7. Next Steps & Close (5 min)

**Goal:** Never end without a concrete next step.

**If they're warm:**
> "Great, it sounds like there's a good fit here. What I'd suggest is [one of these]:"
> - "Let's start with the free Cost Health Check. I can get that set up this week."
> - "Let me send you a proposal for the [Package] tier. When can we review it together?"
> - "Can I schedule a technical deep-dive with one of our engineers and your team?"

**If they need time:**
> "I understand. Let me send you a summary of what we discussed and our one-pager. Can I follow up [specific day] to hear your thoughts?"

**If it's not a fit:**
> "I appreciate your time. It sounds like [reason] means we might not be the right fit right now. If things change, we'd love to help. And I'm happy to do the free Cost Health Check anytime, no strings attached."

**Always:**
- Confirm the next meeting date and time before hanging up
- Send a follow-up email within 2 hours
- Log the call in the pipeline tracker

---

## Qualification Scorecard (Fill during/after call)

| Criterion | Score (1-5) | Notes |
|-----------|-------------|-------|
| AWS spend >= $5K/month | | |
| No dedicated DevOps team (or overloaded) | | |
| Near-term trigger (migration, scaling, incident) | | |
| Decision-maker in the call | | |
| Budget authority confirmed | | |
| Timeline urgency (< 3 months) | | |
| **Total** | **/30** | |

**Scoring guide:**
- 24-30: Hot lead. Propose immediately.
- 18-23: Warm lead. Push for Cost Health Check.
- 12-17: Cool lead. Nurture with content.
- Below 12: Not qualified. Move on.

---

## Persona-Specific Adjustments

**CTO / VP Engineering:** Lead with strategic value (team leverage, risk reduction, speed). Skip cost details until they ask.

**Head of DevOps:** Lead with technical credibility (IaC, CI/CD, monitoring stack). Discuss how we complement rather than replace.

**CFO / Finance:** Lead with numbers (cost of hiring vs. CPS, savings from optimization, predictable spend). Bring the ROI comparison.

**Founder / CEO:** Lead with business impact (focus on product, reduce operational risk, scale without hiring). Keep it high-level.
