---
title: CPS Outreach Templates Library
date: 2026-05-19
status: active
description: Reusable outreach templates extracted from real sent messages. Differs from outreach-batch-1-hot-leads.md (which holds campaign-specific drafts) by being template-shaped and reusable across campaigns.
id: 8ff0f2b7-d35d-4ff3-a80b-6db7dd78f8ad
index_schema_version: 1
---

# CPS Outreach Templates Library

This file collects the message patterns we have battle-tested and want to reuse. Each entry includes the **tokenized template**, a **filled example**, and **when to use** notes.

When a new outreach lands well or feels especially clean, lift it here as a template. Reuse over reinvent.

---

## T01. HU LinkedIn Connect note, 3rd-degree, stack-anchored, value-prop close

**When to use:**
- Recipient is 3rd-degree on LinkedIn (free Connect Request, no InMail credit needed)
- 300 character limit (Premium accounts) or 200 character limit (free accounts)
- Recipient's company has a **publicly verifiable stack signal** (job posting, careers page, conference exhibitor list, etc.) that overlaps with our service offering
- Recipient is an operational decision-maker (Head of IT, IT Operations, Engineering Manager, CTO at smaller orgs) — NOT a C-level executive (use T02 or InMail for C-level)
- Goal: secondary contact at an already-engaged account, OR initial touch on a stack-match prospect

**Anatomy** (in order):
1. Soft opener (HU formal, "Kedves" + first name)
2. Self-identifier ("Sonrisa Cloud Platform Services-t vezetem")
3. Stack-anchor (we run X on the same stack the recipient publicly advertised)
4. Value-prop one-liner (managed-service economics vs hiring)
5. Soft CTA (10-min call, low commitment)

**Tokenized template:**

```text
Kedves [FIRST_NAME], Sonrisa Cloud Platform Services-t vezetem, [SERVICE_NAME] pont a [COMPANY] hirdetett stack-en fut. Rendszerint olcsóbb egy ilyen szolgáltatás mint ha felvennél valakit. Szívesen elmondom a részleteket 10 percben hogy miért.
```

Token slots:
- `[FIRST_NAME]` — recipient's first name (HU informal where appropriate)
- `[SERVICE_NAME]` — the specific CPS service that matches the recipient's stack (e.g., "Azure DevOps managed service", "AWS managed service", "managed Kubernetes operations")
- `[COMPANY]` — the recipient's company short name

**Filled example, AS-SENT to László Pataki at CIG Pannónia 2026-05-19:**

```text
Kevves László, Sonrisa Cloud Platform Services-t vezetem, Azure DevOps managed service-ünk pont a CIG hirdetett stack-en fut. Rendszerint olcsóbb egy ilyen szolgáltatás mint ha felvennél valakit. Szívesen elmondom a részleteket 10 percben hogy miért.
```

(Character count: 252 / 300. Comfortable headroom for slightly longer COMPANY or SERVICE_NAME values.)

Note on the AS-SENT version: "Kevves" is a typo for "Kedves" that slipped through and went out. The template version above uses "Kedves" (the correct form). Worth being slightly more careful proofreading on future sends.

**Why this works:**
- Hungarian peer-level tone for HU operational decision-makers
- Stack-anchor proves we did our homework, not generic spam
- Value-prop one-liner is the SAME positioning we use in long-form pitches ("Rendszerint olcsóbb...") so the message is consistent if the recipient cross-references multiple touches
- 10-min CTA is half of 20-min — easier to commit to, lower friction

**Variations to consider for future iterations:**
- For non-Hungarian recipients in HU companies: switch to "Üdv László," then EN body
- For more senior recipients (CTO/VP): consider adding one extra credibility sentence (e.g., MVMI + OKFO reference)
- For ICP fit without a published posting: drop the stack-anchor, replace with industry-pain-anchor (e.g., "biztosító cégeknél jellemző DORA pressure-re fókuszálunk")

---

## T02. HU Sales Navigator InMail, longer-form, full pitch (placeholder)

**When to use:**
- Recipient is 2nd-degree+ but you want to bypass the Connect Request acceptance gate
- You have an SN InMail credit to spend
- The lead is HOT-priority (worth the credit) and the recipient is a senior/decision-maker contact
- Goal: deliver the full pitch in one shot, no acceptance-gate latency

(Template TBD. The SEON Option F draft, the CIG Pannonia Option G draft, and the ABRIS Option C draft are all examples of this category. Lift a generalized template here after 2-3 more sends to see the stable structure.)

Reference examples:
- SEON Adam Berkecz Option F (HU, 2026-05-18) — see `Accounts/Leads/SEON/NOTES.md`
- CIG Attila Zankai Option G (HU, 2026-05-18) — see `Accounts/Leads/CIG_Pannonia/NOTES.md`
- ABRIS Zsolt Godry Option C (HU, forward-blurb via Miklos warm intro, 2026-05-19) — see `Accounts/Leads/ABRIS/NOTES.md`

---

## T03. HU warm-intro request to internal Sonrisa colleague (placeholder)

**When to use:**
- Sales Navigator reveals an internal Sonrisa person as the 1-mutual-connection between you and the target
- Goal: ask the Sonrisa colleague to forward a prepared blurb to the target

(Template TBD. The Miklos Komjathi → Zsolt Godry @ ABRIS request 2026-05-19 is the first example. Lift the pattern here after the second use.)

Reference example:
- Miklos Komjathi (Sonrisa IT Project Manager) → Zsolt Godry (ABRIS Managing Director), Teams 2026-05-19 — see `Accounts/Leads/ABRIS/NOTES.md`

---

## Template usage cadence

| Template | First-touch latency | Typical reply rate | Credit cost |
|---|---|---|---|
| T01 (Connect note) | 0-7 days for accept, then full message flow | Industry benchmark: 20-40% acceptance, then 5-15% reply | $0 (free) |
| T02 (InMail) | 0 days, full message delivered directly | 5-15% reply | 1 SN credit (~$2 cost) |
| T03 (Warm intro request to colleague) | 1-3 days for colleague to act, then warm intro lands | 40-60% reply (if intro lands) | $0 (relationship cost only) |

T03 > T01 > T02 in conversion order. Use T03 when path exists, T01 for cost-effective scaling, T02 for high-priority HOT where the credit is justified.

---

## Future templates to add

- T04: EN LinkedIn Connect note for HU+international companies (CEOs based abroad)
- T05: HU email outreach (for when LinkedIn paths fail, with email pattern verification)
- T06: HU follow-up nudge after no response (Day-5, Day-10, Day-14 variants)
- T07: HU referral-ask to existing client (when an existing client could intro to a prospect)

Lift these from real sends as they happen.
