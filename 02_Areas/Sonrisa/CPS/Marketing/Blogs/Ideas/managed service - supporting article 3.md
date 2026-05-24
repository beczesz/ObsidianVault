# Availability Is an Engineering Problem, Not an HR Problem

> ⚠️ **STATUS: PARKED — Do not publish yet**
> **Reason:** CPS is still defining its 24/7 on-call operational model and SLA commitments. This article should only be published once service levels are clearly defined and deliverable. Keep for future use.
> **Revisit when:** On-call rotation model is established, SLAs are agreed internally, pricing for 24/7 is confirmed.

---

> **Series:** Managed Service Blog Series (Future — Supporting Article 3)
> **Primary Keyword:** devops on-call coverage
> **Secondary Keywords:** 24/7 infrastructure monitoring, devops availability, on-call burnout
> **Target Audience:** Engineering managers, CTOs dealing with on-call pain, companies after their first serious outage
> **Funnel Stage:** Middle-of-funnel (Consideration)
> **Estimated Word Count:** 1,200-1,500 words
> **CTA:** Learn about CPS 24/7 On-Call / Book a consultation
> **Links back to:** [Main Article](./managed%20service%20-%20main%20article.md)

---

## Meta Description

_(Under 160 characters)_

24/7 infrastructure coverage isn't about hiring more people — it's an engineering problem. Here's how managed on-call actually works.

---

## Outline

### Hook / Introduction (120 words)

- **Opening scenario:** "It's 3:17 AM. Your monitoring fires an alert — database connection pool exhausted, API response times spiking. Your one DevOps engineer is asleep. So is everyone else who might know what to do."
- **The uncomfortable truth:** Availability isn't about effort or dedication. It's about math. One person physically cannot provide 24/7 coverage sustainably.
- **Thesis:** Treating availability as a hiring problem leads to burnout, turnover, and ultimately worse availability. Treating it as an engineering problem — with proper systems, runbooks, and team rotation — leads to reliability.

---

### Section 1: The Math of On-Call (300 words)

**Key points:**
- **168 hours in a week.** One person working 40 hours covers 24% of the week. Where's the other 76%?
- Sustainable on-call rotation requires minimum 3 people (1 week on, 2 weeks off)
- With one engineer: they're either always on-call (unsustainable) or there are gaps (risky)
- **The burnout equation:**
  - Week 1-4: Engineer is alert and responsive
  - Month 2-3: Fatigue sets in, response times increase
  - Month 4-6: Engineer starts job hunting
  - Month 7+: You're back to hiring
- **BMC Connection — Customer Pain Points:**
  - "Our engineer is burning out from on-call"
  - "We had an outage at 2 AM and nobody responded for 4 hours"
  - "We can't retain DevOps people because of the on-call load"

**Supporting data/examples:**
- Industry data: on-call burnout is the #1 reason DevOps engineers leave (cite relevant studies)
- The cost of turnover (tie back to Supporting Article 2)

---

### Section 2: What Good Availability Actually Requires (300 words)

**Key points — the engineering approach:**

1. **Monitoring & Alerting Architecture**
   - Proactive alerts that catch issues before users do
   - Meaningful alerts (not alert fatigue with 200 notifications/day)
   - Escalation paths: who gets paged, when, and what's the backup

2. **Runbooks & Documentation**
   - Every critical system has a documented response procedure
   - New team members can handle incidents from day one
   - **CPS approach:** We build and maintain runbooks as part of every engagement

3. **Rotation & Redundancy**
   - Minimum 3-person rotation for sustainable 24/7
   - Cross-training so multiple people can handle any incident
   - **BMC Connection — Key Resources:** CPS team structure provides built-in rotation

4. **Incident Response Process**
   - Clear severity definitions
   - Defined SLAs per severity level
   - Post-incident reviews that prevent recurrence
   - **BMC Connection — Key Activities:** Proactive monitoring, incident response, infrastructure reviews

- **CPS Value — Tervezés (Planning):** "Kétlépcsős teremtés" — first design the system, then implement it. Availability is designed, not hoped for.

---

### Section 3: How CPS Solves the On-Call Problem (250 words)

**Key points:**
- **24/7 On-Call add-on (€2,000/month):**
  - Team-based rotation (no single point of failure)
  - Trained on YOUR infrastructure (runbooks, architecture, access)
  - Defined response SLAs
  - Escalation to senior engineers and architects when needed
  - Monthly on-call reports: what happened, what was prevented, what should change

- **Why this works vs. hiring:**
  - 3 engineers for 24/7 rotation = €180,000+/year in salaries alone
  - CPS 24/7 On-Call = €24,000/year with a full team behind it
  - Plus: the CPS team brings collective experience from managing dozens of infrastructures

- **BMC Connection — Value Propositions:**
  - Reliability without burnout
  - Breadth of experience (patterns seen across multiple clients)
  - Continuous improvement (we don't just respond — we prevent)

- **CPS Value — Alázat (Humility):** "Nem tudunk mindent, szükség van egymásra" — We need each other. Your knowledge of your business + our operational expertise = real reliability.

---

### Section 4: The Proactive vs. Reactive Spectrum (200 words)

**Key points:**

| Maturity Level | Description | On-Call Impact |
|---|---|---|
| **Level 0: No coverage** | Hope nothing breaks at night | High risk of extended outages |
| **Level 1: Hero culture** | One person handles everything | Burnout, turnover, single point of failure |
| **Level 2: Reactive rotation** | Team takes turns, responds when alerted | Better, but still reactive |
| **Level 3: Proactive monitoring** | Systems catch issues before they escalate | Fewer incidents, faster resolution |
| **Level 4: Preventive engineering** | Architecture designed to self-heal, auto-scale, degrade gracefully | Minimal human intervention needed |

- **CPS takes you from wherever you are toward Level 4**
- Most companies CPS works with start at Level 1 or 2
- The goal: reduce the need for on-call by making systems more resilient
- **CPS Value — Proaktivitás:** The best on-call incident is the one that never happens.

---

### Section 5: Signs You Need to Rethink Your On-Call Strategy (150 words)

**Quick checklist format:**
- ☐ One person handles all infrastructure alerts
- ☐ You've had after-hours incidents with no response for >1 hour
- ☐ Your DevOps engineer mentions burnout or on-call fatigue
- ☐ You don't have documented runbooks for critical systems
- ☐ You've lost a DevOps hire partly due to on-call load
- ☐ Your monitoring produces more noise than actionable alerts
- ☐ You don't have defined SLAs for incident response

**If 3+ boxes are checked:** Your availability is at risk, and it's not a hiring problem — it's a systems problem.

---

### Conclusion & CTA (100 words)

- The takeaway: Availability is built through engineering discipline — monitoring, runbooks, rotation, and proactive architecture. Throwing bodies at the problem doesn't scale.
- **CPS positioning:** We've built the systems and team structure to provide reliability as a service. You focus on building your product; we'll make sure it stays up.
- **CTA:** "Want to stop worrying about 3 AM alerts? Let's talk about how CPS 24/7 On-Call works for your infrastructure."
- Secondary CTA: "Read the full comparison: [Managed DevOps vs. Hiring In-House →](./managed%20service%20-%20main%20article.md)"

---

## Notes for Writing

- **Tone:** Technical but accessible. This article speaks to engineering leaders who feel the on-call pain personally.
- **Voice:** Empathetic and solutions-oriented. Many readers are living this problem right now.
- **Key CPS values to weave in:** Proaktivitás (prevention over reaction), Alázat (humility — one person can't do it all), Tervezés (systematic planning)
- **Avoid:** Making readers feel guilty about their current on-call setup. Instead, show the path from where they are to where they could be.
- **Include:** The maturity model (gives readers a framework to assess themselves), the math (168 hours argument is powerful), the cost comparison (€24k/year vs. €180k+)
