---
topic: AI Platform Comparison - Strengths & Capabilities
created: 2026-04-24
last_updated: 2026-04-24
status: active
id: 552f2d87-6d71-447d-856c-c6d21cda634f
index_schema_version: 1
---

# Brainstorm: AI Platform Comparison

## Team
| AI | Role | URL |
|----|------|-----|
| Claude (Cowork) | Orchestrator & Researcher | local session |

## Sessions
| Date | Team | Key Outcome |
|------|------|-------------|
| 2026-04-24 | Claude solo (web research) | Initial comparison of 5 platforms + latest models |

## Key Insights

### ChatGPT (GPT-5.5, released 2026-04-23)
- Codename "Spud", first fully retrained base model since GPT-4.5
- Strongest in: agentic coding, computer use, knowledge work, multi-step tasks
- 512K-1M context with 74% MRCR v2 score (up from 36.6%)
- "Smartest and most intuitive" -- excels at figuring out next steps with less guidance
- Matches GPT-5.4 latency despite intelligence boost
- API price doubled vs previous generation

### Claude (Opus 4.7, released 2026-04)
- 13% coding benchmark lift, 3x more production tasks resolved vs 4.6
- SWE-bench Pro: 64.3% (up from 53.4%), SWE-bench Verified: 87.6%
- First Claude with high-res image support (2576px / 3.75MP)
- Task budgets for agentic work -- running token countdown
- 1M context window, 128K max output
- Same pricing as Opus 4.6 ($5/$25 per M tokens)
- Strongest in: long-horizon agentic work, knowledge work, vision, memory tasks

### Gemini 2.5 Pro
- ~90% MMLU, 78% SWE-bench Verified
- Native multimodal: video, image, audio processing built-in
- 1M token context with 99% needle-in-haystack accuracy
- Significantly cheaper than competitors
- Strong math/science reasoning
- Leading model for learning/education (LearnLM)
- Strongest in: multimodal processing, long context, cost efficiency

### Perplexity
- 1B+ queries/month, 45M+ users
- Real-time web search with inline citations
- Multi-model: can run GPT-5.2, Claude 4.6, and others simultaneously (Model Council)
- Deep Research for multi-step investigation
- Strongest in: sourced research, fact verification, current events, academic questions

### Microsoft Copilot (M365)
- Agentic capabilities in Word/Excel/PowerPoint now GA
- Work IQ: knows you, your job, your company data
- Access to SharePoint, Teams, Outlook, OneDrive
- Project Manager Agent for task tracking
- Enterprise-grade security, inherits M365 permissions
- Strongest in: enterprise data integration, document workflow, meeting intelligence

## Decisions Made
- Research done via web search rather than external AI team (factual task)

## Open Questions
- [ ] How do these platforms compare on Hungarian language support? (for: Human)
- [ ] Which combination is optimal for CPS workflows? (for: Human)
