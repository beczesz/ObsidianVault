---
description: "Analysis comparing Copilot Studio and n8n for building a WhatsApp client quoting bot for MelindaSteel, including pricing, API integrations, multi-turn conversation handling, and architectural recommendations from AI domain experts and strategists."
description_source: auto
description_hash: a213e0afe15bfb72
topic: Copilot Studio vs n8n -- Client Quoting Automation
created: 2026-04-23
last_updated: 2026-04-23T13:15
status: active
id: 91a65a1a-35c7-4858-a832-6b5f05a04e25
index_schema_version: 1
---
# Brainstorm: Copilot Studio vs n8n -- MelindaSteel Client Quoting

## Team
| AI | Role | URL |
|----|------|-----|
| Perplexity | Researcher | [link](https://www.perplexity.ai/search/microsoft-copilot-studio-2025-Y0pLldmMS2CqngfafTFfKQ) |
| ChatGPT | Strategist | [link](https://chatgpt.com/c/69e9e50b-9e00-8395-84e3-2ff527668f5d) |
| Copilot (M365) | Domain Expert (Microsoft) | [link](https://m365.cloud.microsoft/chat/conversation/23ad3c15-3463-4e35-8e42-501072480c1e) |

## Sessions
| Date | Team | Key Outcome |
|------|------|-------------|
| 2026-04-23 | Perplexity (Researcher) + ChatGPT (Strategist) + Claude WebSearch | Teljes kutatás Copilot Studio képességekről, árról, limitációkról vs n8n |
| 2026-04-23 | Copilot M365 (Domain Expert) | Copilot Studio validáció -- NEM elég önmagában, csak conversation layer-nek jó |

## AI Session Links
- Perplexity: https://www.perplexity.ai/search/microsoft-copilot-studio-2025-Y0pLldmMS2CqngfafTFfKQ
- ChatGPT: https://chatgpt.com/c/69e9e50b-9e00-8395-84e3-2ff527668f5d
- Copilot (M365): https://m365.cloud.microsoft/chat/conversation/23ad3c15-3463-4e35-8e42-501072480c1e

## Key Insights

### 1. Copilot Studio lényege (source: Perplexity + WebSearch)
- Low-code agent platform -- conversational AI agentek építésére
- Erősségei: Knowledge, Topics, Actions, Channels, Orchestration
- Generative orchestration: LLM-driven planning, ami intent alapján választ tool-t/knowledge-t
- **NEM** general-purpose integration runtime -- az n8n az

### 2. WhatsApp integráció (source: Perplexity + MS Learn)
- GA: 2025 július 31 (Azure Communication Services-en keresztül)
- Copilot Studio-ból natívan publisholható WhatsApp csatornára
- Multi-agent orchestration is működik WhatsApp-on
- **FONTOS:** Meta 2025 januártól tiltja a consumer LLM chatbotokat WhatsApp-on, DE ez a Copilot consumer szolgáltatásra vonatkozott, NEM a business API-ra

### 3. API / ERP integráció (source: Perplexity + MS Learn)
- 1000+ prebuilt connector (Power Platform)
- Custom connector: bármilyen REST API-t becsomagolhatsz (OpenAPI spec JSON v2)
- Power Automate flow-k hívhatók action-ként a chatbotból
- SAP ERP connector dokumentálva (BAPI hívások, OData)
- A fuzzy matching API custom connectorként bekötehető

### 4. Multi-turn / State management (source: Perplexity)
- Topics, Questions, Conditions, Entities, Variables (topic-scoped + global)
- System variable: Conversation.Id (stateful context)
- Generative orchestration: dinamikus tool/knowledge választás
- **Korlát:** Nem minden variable type adható át topic-ok között (Date, Duration, Multiple choice, custom entity)

### 5. Pricing (source: WebSearch -- MS Learn, msadvance.com)
- **Capacity pack:** 25,000 Copilot Credit = $200/hó/pack
- **PAYG:** $0.01 / Copilot Credit
- Egy "grounded query" ~12 credit (nem 1!)
- 500 session/hó = 3,000-10,000+ credit (függ a komplexitástól)
- **Becslés 100 conv/nap esetén:** ~3,000 conv/hó x ~12 credit = ~36,000 credit/hó = ~$360/hó PAYG vagy 2 pack ($400/hó)

### 6. Külső AI modellek (source: Perplexity + WebSearch)
- Azure AI Foundry-n keresztül: OpenAI GPT-4.5, Llama, DeepSeek stb.
- **Gemini NEM érhető el natívan** -- csak custom connectoron keresztül (API hívás)
- "Bring your own model for prompts" = Azure AI Foundry modelleket használhatsz
- Tehát a legacy Gemini-alapú extraction/matching NEM portolható közvetlenül

### 7. n8n előnyök a use case-hez (source: WebSearch összehasonlítások)
- Teljes rugalmasság: bármilyen API, bármilyen model, bármilyen logika
- Self-hosting: adatszuverenitás, nincs vendor lock-in
- Meglévő expertise + reusable workflow-k
- Olcsóbb: self-hosted n8n ~$20-50/hó (Cloud) vs Copilot Studio $200+/hó
- Gemini közvetlen használata (nincs Azure AI Foundry közvetítő)

### 8. Copilot Studio előnyök (source: Perplexity)
- Natív WhatsApp channel (nincs saját webhook/API kezelés)
- Beépített multi-turn conversation design (drag & drop topics)
- Enterprise governance, security, compliance
- Power Platform ökoszisztéma (ha Dynamics/SharePoint már van)
- Gyorsabb prototyping conversational UX-re (ha nincs n8n tapasztalat)

### 9. Copilot M365 Chat validáció (source: Copilot Domain Expert)
- **Copilot Studio NEM elég önmagában** -- conversation layer-nek jó, de NEM integrációs hub, NEM pricing engine, NEM source of truth
- **WhatsApp NEM natív** a Copilot Studio-ban a Copilot szerint -- Azure Bot Service kell közé (Twilio / Meta WhatsApp -> Azure Bot Service -> Copilot Studio)
- **Ajánlott architektúra:** WhatsApp (Twilio/Meta) -> Azure Bot Service -> Copilot Studio (NLP + dialogue) -> Power Automate -> Azure Functions -> ERP + Fuzzy API -> Dataverse/SharePoint
- **Fuzzy matching API integráció:** egyszerű, Power Automate HTTP action-nel hívható
- **ERP integráció:** a legnagyobb kockázat -- Copilot NEM hívja közvetlenül, Azure Function szükséges (pricing logic, margin, VAT)
- **Timeline:** MVP 4-6 hét, production-ready 8-10 hét (1 technikai ember)
- **Legnagyobb kockázatok:** WhatsApp session limitek, Copilot Studio korlátozott debugging, ERP unpredictability
- **Fontos megjegyzés a Copilot-tól:** Ha a quoting magas volumenű és business-critical, a Bot Framework SDK (C#/Node) + Azure OpenAI robusztusabb -- Copilot Studio inkább prototyping-ra

## Decisions Made
- (pending -- Szabolcs döntése szükséges)
- **FONTOS INSIGHT:** A Copilot saját maga mondja, hogy a Copilot Studio NEM elégséges egyedül. Ez jelentősen módosítja a korábbi értékelésünket.

## Open Questions
- [ ] Van-e Melinda Steel-nek Microsoft 365 / Dynamics előfizetése? (ha igen, Copilot Studio olcsóbb lehet)
- [ ] Melyik ERP rendszert használja Melinda Steel? (ha Dynamics 365 -> Copilot Studio előny)
- [ ] A Sonrisa csapat milyen szinten ismeri a Power Platform-ot? (learning curve)
- [ ] A legacy n8n Gemini prompt-ok mennyire portolhatók Azure AI Foundry-ba?

## Context References
- Melinda steel n8n project documentation.md (Section 7 -- Client Quoting Automation)
- Egyedi megrendelőlap_Megrendelo_Sonrisa_MelindaSteel v2.docx
