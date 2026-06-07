---
title: "Contract Review: MSA & SOW — ProSharp / Sonrisa"
date: 2026-03-31
author: Becze Szabolcs
status: active
description: "Technical analysis of Pro-Sharp/Sonrisa MSA and SOW contracts covering master service agreement terms, statement of work pricing changes, IP transfer risks, and non-compete restrictions affecting developer hiring for three years post-engagement."
description_source: auto
description_hash: 4f1a1c1e2d685cc3
id: 8c313948-d595-4d22-be9c-bb508dfd615e
index_schema_version: 1
bdos_index: true
---
# Contract Review: MSA & SOW — ProSharp / Sonrisa

**Reviewer:** Claude (on behalf of Szabolcs Becze)
**Date:** March 5, 2026
**Documents reviewed:**
- MSA: `MSA_HUN_EN_SON_prosharp.docx` (Contract No. PROS-SON-K2026, bilingual HU/EN)
- SOW v1: `SOW_ProSharp_Sonrisa Technologies.docx` (original, 10,250 EUR)
- SOW v2: `SOW_ProSharp_Sonrisa Technologies v2.docx` (updated, 11,900 EUR, dated 04.03.2026)

---

## 1. MSA — Key Observations

### 1.1 Structure & Completeness

The MSA is a well-structured bilingual Hungarian/English master framework. It covers subject matter (§1), rights and obligations (§2), fees (§3), IP (§4), payment (§5), business protection (§6), confidentiality (§7), breach (§8), term and termination (§9), contacts (§10), and miscellaneous provisions (§11).

### 1.2 Risks and Concerns for Sonrisa

**Non-solicitation / Business Protection (§6):**
- The non-compete clause (§6.1) prohibits contacting each other's clients for work during the term. This is narrowly scoped (only clients met through the MSA/SOW) — reasonable.
- The **non-hire clause (§6.2)** is aggressive: 36 months post-termination, neither party may hire or contract with the other's current or former employees, advisors, subcontractors, or even people they *negotiated with* about prospective cooperation. This could restrict Sonrisa from hiring any .NET developer who works on this project for 3 years after the engagement ends.
- **Penalty: HUF 25,000,000 (~EUR 63,000)** per breach — very high relative to the contract value of EUR 11,900. This is the same penalty for both non-solicitation and confidentiality breaches.

**Late Performance Penalty (§8.1):**
- 0.5% per day of the contract value, capped at 10% of the net fee. On the SOW v2 price (11,900 EUR), that's a max penalty of 1,190 EUR. Moderate but manageable.
- Pro-Sharp can offset penalty amounts directly from invoices (§8.1) — meaning they can unilaterally deduct.

**Acceptance / Deemed Acceptance (§5.3):**
- If Pro-Sharp does not sign the acceptance certificate within 8 days without "good reason," performance is deemed accepted and Sonrisa can invoice. This is protective for Sonrisa.
- "Good reason" is defined as defects affecting usability in content or functionality attributable to Sonrisa. Minor defects cannot block acceptance.
- However, the determination of what constitutes "good reason" vs "minor defect" is not arbitrated — potential dispute vector.

**Liability Cap (§8.6):**
- Sonrisa's liability is capped at the fee actually paid under the SOW, except for intentional damage. This is a standard and favorable cap for Sonrisa.

**IP Transfer (§4):**
- Full IP transfer for software (§4.2): all proprietary rights transfer to Pro-Sharp, exclusive, unlimited in time and territory. Sonrisa cannot reuse the work.
- For non-software services (§4.3): exclusive transferable license, also unlimited.
- **Risk:** The OTel instrumentation code (spans, annotations) written for Pro-Sharp's codebase becomes their exclusive property. Sonrisa must ensure it does not reuse any project-specific instrumentation patterns in other engagements.
- **Open source disclosure (§4.5):** If any open source is used, Sonrisa must disclose licenses and separately notify if any restrict commercial use. OpenTelemetry itself is Apache 2.0 — no issue, but this obligation should be documented.

**Termination (§9):**
- Either party can terminate with 30 days written notice, no reason required (§9.5). This is important — Pro-Sharp could terminate mid-delivery.
- For cause termination requires written notice + 10 days cure period (§9.7). Reasonable.
- **On client serious breach (§9.8/9.1):** All outstanding invoices become immediately due, and Sonrisa can invoice for ordered-but-not-yet-invoiced work. This is protective for Sonrisa.

**Payment (§5.2):**
- 30 calendar days from invoice receipt. Standard.
- The MSA says invoicing follows acceptance certificate signing. The SOW v2 introduces a 50/50 split (upfront + on completion) — SOW prevails per §1.2.

**Governing Law (§11.6):**
- Hungarian law, Hungarian courts exclusive jurisdiction. As both parties are Hungarian entities, this is expected and appropriate.

### 1.3 Gaps / Missing Items

- **Client contacts in MSA are blank** — the Client-side contact person section has no name, email, or phone filled in. Sonrisa's side shows Szabolcs Becze. This should be completed before signing.
- **Invoice email address is blank** — §5.2 references ".....@...." as the email for invoices. Must be filled in.
- **MSA effective date is blank** — The execution section says "[date]". Needs to be filled before signing.
- **No force majeure clause** — The MSA does not include force majeure provisions. If performance becomes impossible for reasons beyond both parties' control (server outages, pandemic, etc.), the only recourse is §9.6 (impossibility terminates the SOW).
- **No limitation period for warranty claims** — The MSA doesn't specify a warranty/defect notification period post-acceptance.
- **No Data Processing Agreement (DPA)** — §11.2 requires a DPA as a SOW annex if personal data processing is involved. If the OTel instrumentation could capture any personal data in traces (user IDs, IP addresses in spans), a DPA may be required.

---

## 2. SOW v1 vs SOW v2 — Key Differences

| Aspect | SOW v1 (Original) | SOW v2 (Updated) |
|--------|-------------------|-------------------|
| Date | DD.MM.YYYY (unfilled) | 04.03.2026 |
| Client name | "Company Details" (placeholder) | Pro-Sharp Hungary Kft. |
| Client address | "Company Address" (placeholder) | Bácskai utca 29/A, Budapest 1145 |
| MSA date | DD.MM.YYYY (unfilled) | 10.02.2026 |
| Term end | May 31, 2026 | **March 31, 2026** |
| Price | 10,250 EUR | **11,900 EUR (net)** |
| Payment schedule | Not specified (refers to MSA) | **50% upfront (5,950 EUR), 50% on completion** |
| Objectives | Infra + tracing/telemetry only | **Added: structured trace annotations for Item Editor** |
| Scope | Generic OTel instrumentation | **Added: ~10 end-to-end flows, .NET dev collaboration, knowledge transfer** |
| Milestones | "TBA" | **Week 1: Development, Week 2: Refinement** |
| Deadlines | "TBA" | **March 31, 2026** |
| Contacts (Pro-Sharp) | Blank placeholders | Ádám Kovács, Gergely Mátyás |
| Contacts (Sonrisa) | Szabolcs Becze, Gergely Baján | Szabolcs Becze, **Szántó Zoltán** (replaced Gergely B.) |
| Place of performance | Not specified | **Remote** |

---

## 3. SOW v2 — Detailed Review

### 3.1 Strengths

- **Clear scope definition:** The expanded scope paragraph explicitly lists ~10 end-to-end flows, names specific operations (draft creation, publishing, GPC change, attribute management), and describes what annotations should capture (validation, data loading, business logic, DB calls, response generation). This directly addresses the scope ambiguity that caused the dispute.
- **Knowledge transfer obligation:** Explicitly stated — Pro-Sharp will be able to extend annotations independently.
- **Milestones are concrete:** Week 1 (dev) and Week 2 (refinement) give clear expectations.
- **Payment schedule:** 50/50 split protects Sonrisa with upfront payment.
- **Place of performance:** Explicitly stated as remote — avoids travel cost ambiguity.

### 3.2 Risks and Concerns

**Tight timeline (March 31 deadline):**
- SOW effective date is March 4, 2026. Deadline is March 31. That's 27 calendar days, but the work plan describes 2 weeks of active work.
- Today is March 5 — if not yet signed, the clock is ticking. Late performance penalty (0.5%/day, max 1,190 EUR) starts after March 31.
- **If the .NET developer is not yet onboarded**, the 2-week implementation window is at risk.

**"Approximately 10 end-to-end flows":**
- The word "approximately" introduces ambiguity. Pro-Sharp could argue for 12-15 flows. Consider whether to cap this or list the specific flows in an appendix.

**Deliverables section (§5) is unchanged and generic:**
- The "Key Project Deliverables" section still uses the same 3 bullet points from SOW v1 (infra setup, architecture design, documentation). It does **not** reflect the expanded scope (trace annotations, knowledge transfer).
- The scope section (§3) describes annotations, but the deliverables section doesn't list them as a formal deliverable. This mismatch could cause acceptance disputes — Pro-Sharp could argue annotations are a deliverable that must meet specific criteria, while Sonrisa could argue the deliverables are only what's listed in §5.

**"Examples of Services... include, but are not limited to":**
- The phrase "include, but are not limited to" in the deliverables section is open-ended and risky. Pro-Sharp could claim additional work was implied.

**Acceptance criteria are undefined:**
- The SOW describes what annotations should show (validation, data loading, business logic, DB calls, response generation) but doesn't define acceptance criteria. What constitutes "sufficient" trace clarity? Who decides if annotation granularity is adequate?
- The refinement milestone mentions "adjusting annotation granularity" and "verifying traces remain readable and useful" — but no objective standard is provided.

**Price discrepancy with negotiated terms:**
- Your notes indicate the agreed price was 11,900 EUR net (original 10,750 + ~1,150 from the 50/50 cost split of ~60h extra work at ~2,500 EUR). The SOW v2 reflects 11,900 EUR — this is consistent.
- However, the SOW does not acknowledge this as a revised price or reference the scope change that motivated it. If Pro-Sharp later disputes, there's no contractual record of *why* the price changed.

**Sentence fragment in deliverables:**
- "launching tracing and telemetry Develop unit testing cooperating with Pro-Sharp's Technology team" — this appears to be a run-on sentence from v1. It should be cleaned up.

---

## 4. Cross-Reference: SOW v2 vs MSA Consistency

| Check | Status | Notes |
|-------|--------|-------|
| SOW references MSA | ✅ | References Section 2 of MSA dated 10.02.2026 |
| SOW contains mandatory elements per MSA §1.2 | ⚠️ | Missing: explicit "term" as a separate field (it's embedded in the Term section but not called out per the MSA format) |
| Fixed fee designation per MSA §4(a) | ✅ | "fixed fee work stream" stated |
| Payment terms compatible | ✅ | 50/50 split in SOW overrides MSA's post-acceptance invoicing (SOW prevails per MSA §1.2) |
| Contact persons filled | ✅ | Both sides named |
| Place of performance specified | ✅ | Remote |
| Invoice email address | ❌ | Not specified in SOW; MSA also has it blank |
| Acceptance criteria defined | ❌ | No formal criteria; relies on §5.3 of MSA (8-day deemed acceptance) |
| Signatures section | ✅ | Present, unsigned |
| DPA annex needed? | ⚠️ | If OTel traces capture any PII, a DPA is required per MSA §11.2 |

---

## 5. Action Items

### Must Fix Before Signing

1. **Fill in invoice email address** in both MSA and SOW
2. **Fill in Pro-Sharp contact details in MSA** (currently blank)
3. **Fill in MSA execution date** (currently "[date]")
4. **Fix the run-on sentence** in SOW v2 §5 deliverables ("launching tracing and telemetry Develop unit testing...")
5. **Align deliverables section with scope** — the deliverables list should explicitly include trace annotations and knowledge transfer as formal deliverables

### Strongly Recommended

6. **Define acceptance criteria** for trace annotations (e.g., "each annotated flow must show distinct spans for: request entry, validation, business logic, data access, and response" — or similar objective standard)
7. **List the specific ~10 operations** to be annotated (remove "approximately" ambiguity), or cap at a number
8. **Remove "include, but are not limited to"** from the deliverables section — or add "as mutually agreed"
9. **Assess DPA requirement** — will OTel instrumentation capture any personal data (user IDs, session IDs, IP addresses)? If yes, attach a DPA per MSA §11.2

### Good to Consider

10. **Add a change log or recital** in the SOW noting this is a revised scope and price following the Feb 25 resolution, for contractual traceability
11. **Confirm the .NET developer is onboarded** before signing — the March 31 deadline is tight
12. **Verify the non-hire clause (MSA §6.2) implications** — the .NET subcontractor working on this project would fall under the 36-month restriction

---

*Disclaimer: This review is provided for informational purposes and does not constitute legal advice. For binding legal interpretation of these contracts, consult a qualified lawyer.*
