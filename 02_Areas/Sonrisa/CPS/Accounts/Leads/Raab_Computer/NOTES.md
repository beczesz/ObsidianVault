---
description: "Active partner-channel opportunity: Raab Computer (Győr) bringing Patent Csoport (security firm) to Sonrisa CPS for Kubernetes cluster build on VMware and 7/24 managed ops; indicative quote urgent (due 2026-05-28 18:00), full proposal Friday 2026-05-29."
description_source: auto
description_hash: eccc0927fb992957
type: lead
id: raab-computer-k8s
company: "Raab Computer Kft. (partner channel); end client: Patent Csoport (securitypatent.hu)"
stage: discovery
score: 13
score_breakdown:
  maturity: 3
  posting: 3
  aws: 1
  team_gap: 3
  geo_fit: 3
tags: [partner-channel, kubernetes, hybrid-cloud, multi-datacenter, service-mesh, autoscaling, build-plus-ops, lang-hu, urgent-quote, raab-computer]
geo: HU
language: hu
due: 2026-05-29
next_action: "Indicative TÓL-IG SENT to Ács Gusztáv 2026-05-28 (build 20-45k EUR one-time + post-go-live 7/24 6-10k EUR/hó; dev-phase business-hours support NOT quoted). Next: Friday 2026-05-29 discussion + Szántó effort sizing + dev-team CICD meeting; fix-scope quote after."
status: in_conversation
location: "Győr, Hungary (Raab Computer + end client Patent Csoport, both Győr)"
industry: "IT services / systems integration (partner Raab); end client Patent Csoport = security / property protection"
icp: "Profile #1-adjacent, partner-channel Kubernetes build + managed ops"
source_url: "Email 'Igény felmérése' from Ács Gusztáv (acsg@raabcomputer.hu) to becze.szabolcs@sonrisa.hu, 2026-05-27 11:19 CEST"
package:
  tier: TBD
  monthly_eur: 0
  addons: []
  total_eur: 0
sources:
  email: "[[source-docs/01-igeny-felmerese-email-2026-05-27]]"
  meeting_transcript: "[[source-docs/02-meeting-transcript-2026-05-28]]"
channels: [email, partner-channel]
primary_channel: email
case_study_match: "cs-001 MVMI Energy OpenShift (Kubernetes platform build + managed ops) — closest analog"
created: 2026-05-28
last_signal: 2026-05-27
index_schema_version: 1
---
# Raab Computer Kft. — Kubernetes Cluster Opportunity

> **Status 2026-05-28 (post discovery call):** Active partner-channel opportunity. End client = **Patent Csoport / SP Vagyonkezelő Kft.** (securitypatent.hu), Győr security / property-protection holding; Raab Computer is the partner channel (Sonrisa delivers under Raab's trust umbrella). Discovery call held **today 09:28** (Ács Gusztáv + Szántó Zoltán + Becze Szabolcs). **URGENT: indicative TÓL-IG number due by 18:00 TODAY** for the end client's directors budget meeting; full quote at/before the **Friday 2026-05-29** meeting. Greenfield: on-prem DEV cluster first on existing VMware, production in parallel, hybrid-cloud is a future roadmap item. **Indicative tól-ig number SENT to Gusztáv 2026-05-28** (build 20-45k EUR one-time + post-go-live 7/24 6-10k EUR/hó; dev-phase business-hours support not quoted). Strong core-CPS fit (Kubernetes build + managed ops).

## Signal

Inbound email from **Ács Gusztáv (Raab Computer Kft., Győr)** 2026-05-27, CC **Horváth Mihály**. Raab Computer is acting as a **partner / intermediary** — Ács reached the end client's IT lead, who refined an earlier requirement brief. Raab wants Sonrisa CPS to (a) build a Kubernetes cluster for the end client and (b) operate it ongoing.

This builds on a prior conversation ("ahogy tegnap beszéltünk" in the original brief) — not a cold contact. The relationship is warm, partner-mediated.

**2026-05-28 09:28 discovery call** (Ács Gusztáv + Szántó Zoltán + Becze Szabolcs, 23 min) confirmed and deepened the picture. See [[source-docs/02-meeting-transcript-2026-05-28]]. Sonrisa delivers under Raab's "trust umbrella" (Raab has been the end client's IT partner for 15-16 years and recommends Sonrisa).

**The ask, sharpened (2026-05-27):**
- Phase 1 (development phase, ~1-2 years): build the Kubernetes cluster in the **company's own environment** + provide support — **NOT yet 7/24** in this phase
- 7/24 support needed **after go-live** (éles indulás)
- **NOW:** an **indicative quote** so the end client's leadership can review/approve it
- Deadline: **before Friday 2026-05-29** (marked important). This precedes the Friday meeting with us.

## What They Want

Technical requirements (from the end client's original brief, relayed via Raab):

1. **Kubernetes cluster** as the system core
2. **Node / pod management** — operate the nodes and pods in the cluster
3. **Load-based autoscaling** (automatic if possible) — spin up new pods on demand, register them on the network
4. **Service discovery** — know which microservice runs where, how to reach it
5. **Service mesh / policy** — control which services may communicate with which (authentication + authorization)
6. **Health monitoring** — health checks on nodes / pods / microservices
7. **Self-healing** — restart on failure; if restart fails → **alerting mechanism**
8. **Multi-datacenter / hybrid-cloud** — cluster spans multiple DCs (company network + e.g. Vultr or other cloud provider)
9. **Scale** — on the order of **~100 pods / microservices** running in the cluster
10. **Build + ongoing operation** — they want both the buildout AND the long-term ops

**Phasing clarified on the 2026-05-28 call (important, differs from the email reading):**
- **Phase 1 = on-prem DEV cluster first**, then the production cluster in parallel, hosted on the end client's **existing VMware (vSphere) environment**. Observability (logging/monitoring/health-check/alerting) from the start.
- **Hybrid / public cloud is a FUTURE roadmap item, NOT Phase 1.** Design must keep it possible. They already run some components at third-party providers (e.g. a customer portal) they want to migrate later. So the "multi-DC / Vultr" element is a later phase, not a day-1 cost driver.
- **Driver:** replacing an old mission-critical alarm-to-dispatch system called "Tell" (its support person died, so they are rebuilding in-house). Production must never miss a signal → HA now, 7/24 ops + availability SLA after go-live.
- **Why K8s:** elastic scale for unpredictable dispatch volume (they also resell dispatch service to other security firms), easy rollouts, self-healing.
- They expect Sonrisa to bring the package/recommendation (dev-phase structure, CICD pipelines) — a follow-up meeting with their dev team is the agreed next step.

## About the Company

**Raab Computer Kft.** — Győr-based Hungarian IT company / systems integrator (9024 Győr, Malomszéki u. 7). Acting here as a **delivery partner / reseller** bringing an end-client opportunity to Sonrisa CPS.

**End client: Patent Csoport** (securitypatent.hu), confirmed by user 2026-05-28. Győr-based security / property-protection company (same city as Raab, a local partner relationship). Describes itself as one of Hungary's largest and most digitalized property-protection firms: ~16,000 clients, 100,000+ alarms handled annually, 24h dispatch centers, regional offices across Western Hungary. Proprietary software: Patent Gate (in-house property-protection system), myPatent (mobile app + customer portal), plus SAP for ERP. ISO certified. A ~100-microservice platform fits a digitalizing security operator (real-time alarm processing, monitoring, mobile/portal backends). It is NOT a regulated bank, so the Vultr / public-cloud element is unproblematic.

**Existing infra (from the 2026-05-28 call):** Dell servers + Dell storage, VMware (vSphere) hypervisor, ~21-22 VMs, fast SSD storage with memory headroom. The K8s cluster can sit on this existing VMware environment, so **no new hardware is needed for the dev phase**. Still TBD: the IT lead's / IT director's name, exact app workload mix across the ~100 microservices, and which components eventually move to cloud.

## Why This Is Interesting

- **Core-CPS fit.** Kubernetes platform build + managed ops is exactly CPS's flagship competency (MVMI OpenShift cs-001, OKFO Azure DevOps cs-005).
- **Build + multi-year ops** — both a project (Phase 1 buildout) AND a recurring managed-service annuity (support, then 7/24). High lifetime value.
- **Warm partner channel** — Raab brings the deal, lowers acquisition cost, pre-qualified.
- **Clear, well-articulated requirements** — the end client's IT lead already knows what they want (service mesh, autoscaling, multi-DC, ~100 microservices). Not vague.

### Pain Hypotheses

- End client building a microservices platform (~100 services), needs production-grade orchestration but lacks in-house Kubernetes + platform-ops depth
- Multi-DC / hybrid requirement signals data-sovereignty or resilience concern — they don't want full public-cloud lock-in
- "Build + operate" ask = they want a partner to own the platform layer so their devs focus on the microservices

## Value Propositions

- Kubernetes platform build to production-grade (service mesh, autoscaling, observability, self-healing) — the exact stack CPS runs for MVMI
- Phased engagement matches their phasing: Build (Phase 1) → business-hours support → 7/24 post-go-live
- Multi-DC / hybrid-cloud expertise (CPS runs AWS + Azure + on-prem OpenShift)
- ISO/IEC 27001:2022 certified delivery
- Long-term managed-ops annuity, not a one-off build

## Key Contacts

| Name | Role | Email | Notes |
|------|------|-------|-------|
| **Ács Gusztáv** | Raab Computer — primary contact / partner | acsg@raabcomputer.hu · 30/2172779 · 96/526-860 | Sent the requirement email 2026-05-27. The one asking for the indicative quote. |
| **Horváth Mihály** | Raab Computer | horvathm@raabcomputer.hu | CC on the email |
| **Szántó Zoltán** | Sonrisa CPS, technical lead (cloud-native) | (internal) | Drove the technical discovery on the 2026-05-28 call. The likely technical owner for effort sizing + the dev-team CICD meeting. |
| Patent Csoport IT director | (name TBD) | (unknown) | The end client's IT director; asked (via Ács) for the indicative number for today's directors budget meeting. Refined the requirement brief. Confirm name + meet directly at the Friday meeting. |

## The Angle

CPS is the Kubernetes platform partner Raab can stand behind: we build the cluster to production grade (service mesh + autoscaling + observability + self-healing + multi-DC) and operate it long-term, so the end client's leadership gets a credible, phased, fixed-then-managed proposal. MVMI OpenShift is the proof point.

## Timing

- **Email received:** 2026-05-27 (Wed)
- **Discovery call:** 2026-05-28 09:28 (done) — Gusztáv + Szántó Zoltán + Becze
- **Indicative TÓL-IG number:** SENT to Gusztáv **2026-05-28** (for the end client's directors budget meeting). As sent: build **20 000 – 45 000 EUR** one-time + post-go-live 7/24 **6 000 – 10 000 EUR/hó**; the dev-phase business-hours support line was dropped (not quoted). See [[proposals/02-indikativ-email-tol-ig-2026-05-28]].
- **Friday 2026-05-29:** first real discussion meeting.
- **Next step:** meeting with the end client's dev team (CICD pipelines, dev-phase structure).
- **Strategic thread:** broader project potential, Sonrisa sales director to be brought in ~2 weeks out (after Becze's vacation).
- **Phase 1:** ~1-2 years (development phase) — on-prem dev + business-hours support
- **Go-live + 7/24:** after Phase 1; hybrid/cloud extension somewhere along the roadmap

## Red Flags

- **Same-day clock on the number.** The indicative TÓL-IG figure is due by 18:00 TODAY for a budget meeting. No time for deep scoping; deliver an explicit from-to range with a stated uncertainty (Becze flagged up to 50-100% spread), priced to safely cover scope, narrowed after the Friday meeting + dev-team session.
- **Multi-DC / hybrid is a LATER phase, not day 1.** The 2026-05-28 call clarified Phase 1 is a single-site on-prem dev cluster on existing VMware. Do not price a multi-cluster federation into the Phase-1 number; flag hybrid as a roadmap item with its own scoping. (Corrects the original "multi-DC is the big day-1 cost driver" reading.)
- **Production is mission-critical (no missed alarm signals).** The real value/cost driver is HA + eventual 7/24 ops + availability SLA, plus onboarding ~100 microservices. This is the annuity, not the build.
- **Partner-channel commercial model unsettled.** Sonrisa is under Raab's "trust umbrella" but the model (Raab markup? sub-contract? joint delivery?) is not yet agreed. Clarify with Ács before any binding numbers.
- **Budget is real but not unlimited.** Gusztáv: "not as unlimited as MVM." Value-aware, trust-driven buyer (SP Vagyonkezelő holding). Price on value, but expect them to check the figure.
- **CPS does NOT have NIS2 certification** — position as NIS2-aware, ISO 27001 certified only.

## Drafts

### Indicative quote — structure (to be built, see Next Step)

Two components (MVMI-pattern):
1. **Phase 1 — Build (project, fixed or T&M-capped)**: cluster design + buildout (K8s + service mesh + autoscaling + observability + multi-DC topology + self-healing/alerting). Engineer-days × CPS day rate.
2. **Support (recurring managed service)**: business-hours during Phase 1 → 7/24 after go-live. CPS tier (Essential/Growth/Scale) + 24/7 On-Call add-on post-go-live.

Numbers TBD with Ceclan effort sizing.

## Action Items

- [ ] **URGENT: Draft indicative quote** for K8s build (Phase 1) + support, deliver to Ács before Friday 2026-05-29. 📅 2026-05-28 #urgent #drafting
- [ ] **Effort sizing with Ceclan Sanyi** — cluster build engineer-days + support FTE estimate. 📅 2026-05-28 #sizing
- [ ] **Clarify commercial model with Ács** — sub-contract to Raab, joint delivery, or direct? Raab margin? 📅 2026-05-28 #decision
- [ ] **Confirm Friday meeting** date/time + who attends from end client. 📅 2026-05-28 #followup
- [ ] **Surface end-client details** — name, industry, size, current stack, DC locations — at/before Friday meeting. 📅 2026-05-29 #research

## Next Step

Draft the **indicative quote** for the Kubernetes cluster build (Phase 1) + phased support, with explicit assumptions, deliver to Ács Gusztáv before Friday 2026-05-29. Effort sizing needs Ceclan. Confirm the commercial model (partner sub-contract vs joint) with Ács.
