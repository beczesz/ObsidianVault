---
title: CCHBC Opportunity — Rövidítések és terminológia
date: 2026-05-19
author: Becze Szabolcs (Librarian-generált)
status: active
description: Minden rövidítés és szakkifejezés egy helyen, amit a CCHBC opportunity során használunk — bid call-hoz, ajánlatíráshoz, technikai prezentációhoz.
tags: [cchbc, glossary, reference]
id: 8a632413-88de-426e-aa1f-4c6b2bc7808c
index_schema_version: 1
---

# CCHBC Opportunity — Glossary

Gyors referencia minden rövidítéshez ami az emailben, az RFP-ben, és a CPS-belső munkában előjön.

---

## 🏢 Cégek és szervezetek

| Rövidítés | Teljes név | Mi ez |
|---|---|---|
| **CCHBC** | Coca-Cola Hellenic Bottling Company | A végfelhasználó. FTSE 100 Coca-Cola palackozó, 29 ország, Zug HQ. Az RFP forrása. |
| **CCH** | Coca-Cola Hellenic | Ugyanaz, rövidebb forma — a Berecz email "CCH"-t használ. |
| **MT** | Magyar Telekom NyRT. | A prime bidder. Magyarországi Deutsche Telekom leányvállalat. Minket sub-bid komponensre kérnek. |
| **DT** | Deutsche Telekom AG | Az MT anyavállalata. "DT szintű focus" = csoport-szintű figyelem a deal-en. |
| **OTE** | Hellenic Telecommunications Organization (Görögország) | Görög telekom, DT-csoporttag. Petropoulos innen küldte a RFP-t. |
| **Combis** | Combis d.o.o. | Horvát IT-szolgáltató, T-Hrvatski Telekom leányvállalat. Tatjana Peček innen. |
| **openminds** | openminds.hu | Magyar partner cég, Szurdi Miklós a kontakt. A mi belépési pontunk. |
| **Sonrisa** | Sonrisa Technologies | Mi vagyunk. |
| **CPS** | Cloud Platform Services | A Sonrisa-n belüli üzletág, amit Szabolcs vezet. |

---

## 👥 Szerepkörök, részlegek (CCHBC + MT oldali)

| Rövidítés | Teljes név | Mit jelent |
|---|---|---|
| **DTPS** | Digital Technology & Platform Services | CCHBC belső csapata, ami a cloud platformot tulajdonolja — a mi végfelhasználói "vevőnk". |
| **VP** | Vice President | Cégvezetés alatti vezető szint. Petric Anton DT VP = senior. |
| **AICCST** | (Telekom belső tag) | Molnár Attila tag-je. Telekom-csoporton belüli AI/CCST részleg, "ext." = külsős. |
| **B2B_SIT** | Business-to-Business / Sales-IT | MT belső tag, Bakos Balázs tag-je. |
| **B2B_MCT** | Business-to-Business / Marketing-Customer Team | MT belső tag, Tóth László tag-je. |
| **SRE** | Site Reliability Engineer | CCHBC oldalon operatív excellence felelős — incidenskezelés, observability. |

---

## 📄 RFP-folyamat és üzleti

| Rövidítés | Teljes név | Magyarázat |
|---|---|---|
| **RFP** | Request for Proposal | Pályázati felhívás — ez az amit megkaptunk. |
| **RFI** | Request for Information | Pályázat előtti tájékozódási kör (Bartók emaili itt használja "RFI" szóval). |
| **QBR** | Quarterly Business Review | Negyedéves stratégiai review meeting MT-OTE között — innen jött az "action plan" amiből CCHBC opportunity. |
| **PI Planning** | Program Increment Planning | SAFe agile keretrendszer 8-12 hetes tervezési ceremóniája. CCHBC ennek alapján vár negyedéves cadencet. |
| **OKR** | Objectives and Key Results | Cél + mérőszám módszer. RFP "Quarterly Innovation OKRs"-t emleget. |
| **PoC** | Proof of Concept | "Bizonyítsd, hogy működik" mini-projekt. CCHBC quarterly Agentic AI PoC-kat vár. |
| **ICP** | Ideal Customer Profile | Sonrisa CPS belső fogalom — 30-500 emp mid-market. CCHBC ezen kívül esik. |
| **MSP** | Managed Service Provider | Generikus üzemeltetési vendor. CCHBC pont **NEM** ilyet keres ("not ops-heavy"). |
| **BMC** | Business Model Canvas | Sonrisa-belső stratégiai dokumentum. |
| **BDOS** | Business Development Operation System | Sonrisa AI-native agent rendszer ([00_Prompts/BDOS/CLAUDE.md](../../../../../00_Prompts/BDOS/CLAUDE.md)). |
| **ACE** | AWS Customer Engagement | AWS Partner Central opportunity-regisztrációs rendszer. |
| **APN** | AWS Partner Network | AWS partner program. |

---

## 🛡️ Compliance és szabványok

| Rövidítés | Teljes név | Mit jelent |
|---|---|---|
| **SOC 2 Type 2** | Service Organization Control 2 (Type 2) | Üzemeltetési biztonság-audit, 6-12 hónapot lefedő bizonyítás. CCHBC **kötelezően** vár a vendortól. Sonrisának **nincs** meg. |
| **GDPR** | General Data Protection Regulation | EU adatvédelmi rendelet. |
| **ISO 27001** | Information Security Management standard | Nemzetközi infosec szabvány. |
| **NIS2** | Network and Information Security Directive 2 | EU új kiber-direktíva. Sonrisának **nincs** meg (CPS/CLAUDE.md figyelmeztet rá). |
| **DORA** | Digital Operational Resilience Act | EU fintech direktíva (más kontextusból, Loxon lead-nél jött elő). |
| **Zero Trust** | Zero Trust Architecture | "Sose bízz, mindig ellenőrizd" biztonsági modell. RFP elvárás. |
| **RBAC** | Role-Based Access Control | Szerepkör-alapú hozzáférés. |
| **MFA** | Multi-Factor Authentication | Többtényezős autentikáció. |
| **PKI** | Public Key Infrastructure | Tanúsítvány-infrastruktúra. |

---

## 📊 Service Levels és incidens

| Rövidítés | Teljes név | Magyarázat |
|---|---|---|
| **SLA** | Service Level Agreement | Kötelező szerződéses szolgáltatási szint. |
| **SLO** | Service Level Objective | Belső célszint, amit mérünk (rugalmasabb mint SLA). |
| **SLI** | Service Level Indicator | Maga a mérőszám (pl. availability %). |
| **MTTR** | Mean Time To Resolve / Recover | Átlagos incidens-feloldási idő. |
| **MTTD** | Mean Time To Detect | Átlagos incidens-észlelési idő. |
| **RCA** | Root Cause Analysis | Gyökérok-elemzés post-incident. |
| **P0 / P1 / P2 / P3** | Priority levels | Incidens-prioritások: Crisis / High / Medium / Low. |
| **IMCR** | Incident Management Crisis Response | CCHBC formális válságkezelési folyamata. Vendornek 24/7 részt kell venni. |
| **SDR** | Service Disruption Report | Post-crisis dokumentum, amit a vendornek kell írni. |
| **RPO** | Recovery Point Objective | Maximum adatvesztés ideje DR esetén ("max 1 órányi adatot veszíthetünk"). |
| **RTO** | Recovery Time Objective | Helyreállítási idő DR esetén ("4 órán belül vissza kell jönnünk"). |
| **DRP** | Disaster Recovery Plan | Katasztrófa-helyreállítási terv. |
| **BC/DR** | Business Continuity / Disaster Recovery | Üzletmenet-folytonosság és helyreállítás együtt. |
| **CAB** | Change Advisory Board | Változás-jóváhagyási bizottság (ITIL fogalom). |
| **CMDB** | Configuration Management Database | Konfigurációs leltár-adatbázis. |
| **ITSM** | IT Service Management | IT szolgáltatás-menedzsment (ITIL alapú). ServiceNow ennek a platformja. |

---

## ☁️ Cloud / Azure specifikus

| Rövidítés | Teljes név | Magyarázat |
|---|---|---|
| **IaaS** | Infrastructure as a Service | Virtual gépek, hálózat, storage. |
| **PaaS** | Platform as a Service | App Service, SQL Managed Instance, Functions. |
| **SaaS** | Software as a Service | Pl. Dynamics 365. |
| **AKS** | Azure Kubernetes Service | Azure managed K8s. |
| **ACI** | Azure Container Instances | Serverless container futtatás. |
| **APIM** | Azure API Management | API gateway. |
| **AVD** | Azure Virtual Desktop | Felhős desktop (out-of-scope a RFP-ben). |
| **AHUB** | Azure Hybrid Use Benefit | Microsoft licenc-előny on-prem → Azure transzferre. |
| **RI** | Reserved Instance | Lekötött (1-3 év) kapacitás kedvezménnyel. |
| **SP** | Savings Plan | Rugalmasabb költségvállalás kedvezménnyel. |
| **VPC** | Virtual Private Cloud | Privát virtuális hálózat (AWS terminológia, de általánosan használt). |
| **WAF** | Well-Architected Framework | Microsoft / AWS architektúra-keretrendszer (5 pillér). Az RFP mandatórikusan ezt kéri. |
| **GCP** | Google Cloud Platform | CCHBC "future-ready" elvárás GCP-re is. |
| **IaC** | Infrastructure as Code | Terraform, Bicep — minden infrát kódban tartani. |
| **GitOps** | Git-based operations | Git-alapú deploy + drift detection. |
| **CI/CD** | Continuous Integration / Continuous Deployment | Automatizált build és deploy pipeline. |
| **SDLC** | Software Development Life Cycle | Szoftverfejlesztési életciklus (dev → test → prod). |

---

## 🔐 Microsoft biztonsági stack

| Rövidítés | Teljes név | Magyarázat |
|---|---|---|
| **Entra ID** | Microsoft Entra ID | Korábban Azure AD. Identitás-platform. |
| **Defender** | Microsoft Defender for Cloud | Cloud security posture management. |
| **Sentinel** | Microsoft Sentinel | SIEM (security event monitoring). |
| **SIEM** | Security Information & Event Management | Központi biztonsági log + esemény elemzés. |
| **EDR** | Endpoint Detection and Response | Végponti fenyegetés-detektálás. |
| **SOC** | Security Operations Center | Biztonsági monitoring csapat (CCHBC oldalon belső). |

---

## 💰 FinOps

| Rövidítés | Teljes név | Magyarázat |
|---|---|---|
| **FinOps** | Financial Operations | Cloud-költségmenedzsment gyakorlat. |
| **GreenOps** | Green Operations | Karbonlábnyom-orientált cloud üzemeltetés. |
| **Showback** | (nem rövidítés) | Belső költség-allokáció üzleti egységenként (riportálás, de nem terhelés). |
| **Chargeback** | (nem rövidítés) | Belső költség-terhelés tényleges fizetéssel. |
| **Rightsizing** | (nem rövidítés) | Erőforrás-méretezés a tényleges használathoz. |
| **Drift detection** | (nem rövidítés) | Eltérés-detektálás az IaC szándékolt és az élő állapot között. |

---

## 🤖 AI / AIOps / Agentic AI

| Rövidítés | Teljes név | Magyarázat |
|---|---|---|
| **AIOps** | AI for IT Operations | ML/AI alkalmazása IT üzemeltetésre. Gartner-fogalom 2016. |
| **Agentic AI** | (nem rövidítés) | Autonóm AI ágensek, amik többlépcsős döntést hoznak és cselekednek (nem csak ajánlanak). |
| **LLM** | Large Language Model | Nagy nyelvi modell (GPT-4, Claude, Llama stb.). |
| **LLMaaS** | LLM as a Service | LLM mint szolgáltatás — a mi Inference Farm termékünk. |
| **ML** | Machine Learning | Gépi tanulás. |
| **RAG** | Retrieval Augmented Generation | LLM kombinálása belső dokumentum-kereséssel. |
| **LoRA / QLoRA** | (Quantized) Low-Rank Adaptation | LLM finomhangolási technikák (alacsony erőforrásigénnyel). |
| **vLLM** | (open-source LLM serving framework) | Nagy teljesítményű LLM kiszolgáló (PagedAttention). |
| **GPU** | Graphics Processing Unit | LLM futtatáshoz szükséges hardver (Sonrisa: G5.12XL AWS). |
| **MLOps** | ML Operations | Az ML modellek életciklusának üzemeltetése. |
| **Closed-loop automation** | (nem rövidítés) | Önjavító, ember nélkül futó automatizmus. |

---

## 🛠️ Eszközök (CCHBC stackben szereplő)

| Eszköz | Mit csinál | Státusz az RFP-ben |
|---|---|---|
| **Dynatrace** | Observability (APM + infra + logs) | Mandatórikus, CCHBC tulajdonú licenc |
| **ServiceNow** | ITSM (incident/problem/change) | Mandatórikus, CCHBC tulajdonú licenc |
| **Azure DevOps** | CI/CD + repo + boards | Use only (nem mi menedzseljük) |
| **GitHub Actions** | CI/CD alternatíva | "Ideal tool" — preferált |
| **Terraform** | IaC | Erősen ajánlott primary |
| **Ansible** | Konfiguráció-menedzsment | Másodlagos automation tool |
| **Aqua / Trivy** | Container image scanning | Container security |
| **SonarQube** | Static code analysis | Preferált |
| **Azure Advisor** | MS belső ajánlások (cost, security) | Use AI features |
| **Apptio / Flexera / Turbonomic** | FinOps platformok | Preferált 3rd-party |
| **Power BI** | Riportálás / dashboard | Integrálási pont |

---

## 📡 Communication / vegyes

| Rövidítés | Teljes név | Magyarázat |
|---|---|---|
| **API** | Application Programming Interface | Programozási interfész. |
| **TLS** | Transport Layer Security | Hálózati titkosítás (HTTPS alapja). |
| **AES-256** | Advanced Encryption Standard 256-bit | Adat-titkosítás nyugalmi állapotban. |
| **SSO** | Single Sign-On | Egyszeri bejelentkezés (pl. SAML-en keresztül). |
| **SAML** | Security Assertion Markup Language | SSO protokoll. |
| **KPI** | Key Performance Indicator | Kulcs mérőszám. |
| **ROI** | Return on Investment | Befektetés-megtérülés. |
| **TCO** | Total Cost of Ownership | Teljes birtoklási költség. |
| **FMCG** | Fast-Moving Consumer Goods | Napi fogyasztási cikkek (CCHBC iparága). |
| **FYI** | For Your Information | Informális továbbküldés (Bartók/Molnár emailjei). |

---

## 🗂️ Sonrisa belső

| Rövidítés | Teljes név | Magyarázat |
|---|---|---|
| **CPS** | Cloud Platform Services | Sonrisa üzletág. |
| **BDOS** | Business Development Operation System | Sonrisa AI-native agent system. |
| **Maestro** | (agent neve) | Brand-to-Site Conductor BDOS agent. |
| **Librarian** | (agent neve) | Knowledge Manager BDOS agent (én). |
| **Inference Farm** | (termék neve) | A CPS LLMaaS platformja AWS GPU-kon. |
| **DH** | Deák Húsüzlet | Másik aktív pilot (nem releváns CCHBC-re). |
