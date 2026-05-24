# Strategist (Claude Opus 4.7) — Round 1 findings

## Summary

Az "Implementációs fázisok" doksi **megváltoztatja a tier-modell legjobb framing-jét**. Korábban "advisory vs production" tengelyen gondolkodtam, de a belső roadmap egy **agent-maturity tengelyt** rajzol ki, ami konceptuálisan tisztább és eladhatóbb. A 3 tier átkeretezve: **Agent Architect → Agent Builder → Agent Operator**. Ez (a) közvetlenül kapcsolódik a már megkezdett Sonrisa belső gondolkodáshoz, (b) konkrét agent-egységekkel mérhető deliverable-eket ad (Alert Agent, Operator Agent, FinOps Agent, Test Agent, Deploy Agent), (c) elkerüli a "consulting vs delivery" csapdát, ahol egy sub-bid vendor általában lefelé csúszik.

## Strategist answers

### Q1 — Pricing realism check (saját anchoring)

FTSE 100 FMCG, €5-20M/év cloud spend → prime managed services bid kb. €5-15M/év → MT 10-25% markup → **AIOps+Agentic AI+FinOps innovation szelet kb. €1-3M/év** a teljes deal-ből.

| Tier | Mennyi a teljes innovation szeletből | Megjegyzés |
|---|---|---|
| A: €32-60k/év | 2-5% | **Túl kicsi.** Egy sub-vendor szerződéses mass-ot kéne mutasson, különben MT-nek bid-bookkeeping zaj. |
| B: €100-160k/év | 5-15% | **Reálisabb sávközép.** Hihető "specialist sub-vendor" tarifa. |
| C: €240-400k/év | 15-30% | **Felső sáv.** Magas, de védhető, ha 3-4 FTE dedikáltan. |

**Javaslat**: Tier A árazás emelkedjen €15-25k/Q-ra (€60-100k/év), különben MT bid-bookkeeping szemszögből feleslegesnek tűnik a sub-vendor menedzselése.

### Q2 — Tier framing átalakítás

Új framing **agent-maturity tengelyen**:

| Tier | Új név | Központi értékajánlat |
|---|---|---|
| A | **Agent Architect** | Mi tervezzük, ők építik. Blueprint + Dynatrace tuning + agent-architecture review. |
| B | **Agent Builder** | Mi építünk 1 production agentet quarter-enként, MT operálja. |
| C | **Agent Operator** | Mi építünk ÉS operálunk 3-5 agent-et 24/7-ben. |

Ez összhangban a belső "Implementációs fázisok" Phase 2-vel: Alert Agent + Operator Agent + FinOps Agent + Test/Deploy Agent — ezek **konkrét, megnevezett agent-egységek**, amik kvártlis delivery cycle-be tehetők.

### Q3 — Implementációs fázisok roadmap → CCHBC stack mapping

A belső roadmap **konceptuálisan teljesen átvihető**, csak a stack komponenseket kell cserélni:

| Sonrisa internal | CCHBC mandatórikus |
|---|---|
| Oracle Cloud | Azure (mandatórikus) |
| Victoria Metrics / Logs / Traces + Grafana | Dynatrace (mandatórikus) — Davis AI + custom Grail queries |
| Teleport | Entra ID + Privileged Access (CCHBC kezeli) |
| Jira Cloud + Keep + Grafana Alertmanager | ServiceNow (mandatórikus) — Event Mgmt + IH |
| Gitlab pipeline | Azure DevOps / GitHub Actions |
| Hermes/OpenClaw + MiniMax LLM | Inference Farm (Azure-portolt) + Llama/DeepSeek |
| Opencost | Azure Cost Management + Apptio/Flexera + custom FinOps agent |

**Insight:** A belső csapat **már gondolkodik agent-tipusokban** (Alert Agent, Operator Agent, FinOps Agent, Test Agent, Deploy Agent). Ezek **pontosan azok**, amiket CCHBC kér. Az architekt-szintű egyezés erős, csak a tooling kicsi.

### Q4 — Tier B sweet spot (refined version)

**Tier B "Agent Builder"** rétegezett deliverable:

**Negyedévente 1 named production agent**, kiválasztva ebből a katalógusból (MT/CCHBC választ):
1. **Alert Triage Agent** — Dynatrace alertekből incidens-konszolidáció, ServiceNow ticket creation
2. **FinOps Optimizer Agent** — Azure Cost Management adatokból rightsizing + RI/SP recommendations + auto-execute kis erőforrásokra
3. **Operator Remediation Agent** — ismert pattern-ekre autonóm helyreállítás (autoscale, restart, failover)
4. **RCA Drafter Agent** — incidens-log + telemetria → első RCA draft ServiceNow-ban
5. **Deploy Verifier Agent** — pre/post-deploy health checks + rollback trigger
6. **Capacity Forecaster Agent** — predikció CPU/memory/storage budget overshoot-okra

**Évente 4 agent, ~16 agent 4 év alatt.** Ez egy "agent portfolio" amit CCHBC felépít velünk.

Plusz: minden agent egy **Hermes/OpenClaw-szerű orchestration framework**-en fut, amit egyszer felépítünk Q1-ben (= a "Phase 2 Intelligence" infrastruktúra a belső roadmap szerint).

### Q5 — Pre-engagement Tier 0 javaslat

**IGEN, érdemes** Tier 0-t hozzáadni: 4-6 hetes pre-engagement assessment **2026 Q4-ben** (az engagement előtt fél évvel), **€40-60k fixed fee** áron.

Tartalom:
- CCHBC Azure estate audit (resource inventory, tag coverage, cost baseline)
- Dynatrace tenant deep-dive (Davis AI használati audit)
- ServiceNow workflow mapping
- Agent portfolio prioritization workshop CCHBC-vel
- Tier B/C scoping fine-tune

**Indok**: 12 nap alatt nem tudunk megalapozott árajánlatot adni. Tier 0 fixed-fee assessment-ként **megkockáztatva** szólhat a bid-be, hogy 2026 H2-ben a tényleges scope kalibrálható legyen. MT-nek is jó (less risk a bid-ben), CCHBC-nek is jó (transparent, structured onboarding).

### Q6 — Pricing model recommendation

**Hybrid** model:
- **Retainer** (recurring havi fix): minimum capacity garantálás MT-nek + CCHBC-nek
  - Tier A: €3k/hó retainer (=€9k/Q) + €5k per quarterly demo PoC
  - Tier B: €8k/hó retainer (=€24k/Q) + €12k per production agent (1/Q)
  - Tier C: €15k/hó retainer (=€45k/Q) + €15k per agent + €5k/hó 24x7 fee
- **PoC fee** per delivered agent (acceptance criteria-vel)
- **Outcome bonus** (Tier C only): ha mért FinOps savings vagy MTTR reduction elér target-et → +10-20% quarterly bonus

Indok: pure FTE-billing **rosszul néz ki sub-bid-ben** (MT-nek extra menedzsment). Pure fixed-fee **kockázatos nekünk** (CCHBC bonyolultabb mint gondoljuk). Hybrid = stabilitás + delivery accountability.

### Q7 — Missing elements (kritikus hiányok)

1. **References & case study bundle** — MVMI Azure DevOps (cs-004), MVMI OpenShift (cs-001) közvetlenül relevánsak. Minden tier-hez 2-3 named reference + 1 page case study attachment.
2. **Named team commitment** — 4 éves engagement-nél MT/CCHBC tudni akarja, ki van rajta. Min. architect-lead + ML engineer-lead **named, retention commitment**-tel.
3. **MT-commitment lista** — mit kell az MT-nek tennie, hogy Sonrisa szállíthasson (introductions, Dynatrace access, ServiceNow read-permissions stb.). **Bid attachment-ként**.
4. **IP & exit clauses** — minden agent kódja CCHBC IP, de Sonrisa megőriz egy "reusable Hermes framework" alap-jogot. Ez **explicit** legyen.
5. **PR / joint go-to-market right** — sub-vendor CCHBC win esetén legalább **belső jelölés joga** ("Sonrisa is the AIOps partner in the MT-CCHBC delivery"). 

### Q8 — Sub-bid trap & mitigation

**A klasszikus sub-bid trap**: MT az ajánlatunkat **változatlanul** beilleszti az ő bid-jébe → CCHBC tárgyalás során MT árszintje összenyomódik → MT a sub-vendor (Sonrisa) árát **arányosan lenyomja**, miközben MT prime margin-ja sértetlen marad. **Sonrisa végül az eredeti ajánlat 60-70%-án dolgozik**, de még mindig kötelezett 100%-ban a deliverable-re.

**Mitigáció**:
- **Sticky pricing clause**: a Sonrisa ár-tartomány csak addig érvényes, amíg a CCHBC final scope ±10%-on belül van. Bármi nagyobb scope-csere = új tárgyalás.
- **Sonrisa fix retainer + variable PoC fee** kombinációja: a retainer védve, a variable rész scope-kötött.
- **Termination protection**: ha MT abbahagyja a deal-t Q1 után, minimum 6 hónapnyi retainer kifizetése (Sonrisa kapacitást lekötött).

### Q9 — Engagement timeline (új)

Javasolt szakaszolás CCHBC felé:

```
2026-05-31  Financial proposal to MT (3-tier menu + Tier 0 option)
2026-06-15  Technical presentation to MT (architecture + reference cases)
2026-06-30  MT submits to CCHBC (with Sonrisa as named sub-vendor)
2026 Q3-Q4  CCHBC shortlist + technical deep-dive (Sonrisa participates)
2026 Q4     Tier 0 pre-engagement (if won): assessment + scope fine-tune
2027 Q1     Engagement start: Tier B (default) or Tier C (if CCHBC requests)
            - Q1: Hermes/OpenClaw orchestration framework setup
            - Q2: Agent #1 (Alert Triage Agent — quick win)
            - Q3: Agent #2 (FinOps Optimizer Agent)
            - Q4: Agent #3 (Operator Remediation Agent) + first annual review
2028-2030   Year 2-4 cadence: 4 agents/year, retention check Q1 each year
```

## Open questions for follow-up

- **MT's commercial model**: do they pass-through Sonrisa pricing or markup? Need to know before final number.
- **Compliance umbrella**: is MT's SOC 2 / NIS2 enough for CCHBC, or does Sonrisa need its own?
- **Inference Farm Azure port effort**: 2-4 weeks engineering — but does MT budget for this as one-off setup fee, or hide in retainer?
- **Multi-country deployment**: CCHBC operates in 29 countries. Is the AI agent layer **centralized** (one Hermes deployment) or **distributed** (per-region)? Affects 5-10x in pricing.

## Flags for Szabolcs

- ⚠️ The internal team's Phase 1 (Operations Foundation) is **NOT** in scope for CCHBC — they have Dynatrace + ServiceNow + Azure DevOps. **Don't accidentally offer to rebuild their foundation.**
- ⚠️ "Oracle Cloud" mentioned internally **must NOT appear** in CCHBC-facing materials. They are Azure-only.
- ⚠️ MiniMax LLM is Chinese-owned — **strict no-go** for FMCG enterprise with US/EU compliance. Stay with Llama / DeepSeek / Qwen (open source) on Inference Farm.
- ⚠️ The Sonrisa internal roadmap is "AI agent multi-tenant platform" — **NOT** offered as a turn-key product to CCHBC. We offer the OUTCOMES (built agents), not the underlying platform. Otherwise we tie ourselves to delivering a productized SaaS that we haven't built yet.
