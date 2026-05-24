---
title: Erdélyi versenytársak — Ignis Academy / ExarLabs piackutatás
date: 2026-05-22
author: Becze Szabolcs
status: active
description: Think-engine demo-futás eredménye. Erdélyi (romániai, magyar nyelvű) versenytársak az AI/digitális oktatás és a szoftver/AI-fejlesztés piacán, az Ignis Academy brand pozicionálásához. Forrás: ChatGPT (EXL Site documentation chat) kontextus + Perplexity Pro sourced research.
tags: [ignis-academy, exarlabs, versenytars, piackutatas, think-engine]
id: 3ab7c360-ac38-4f32-9541-ad96d571e243
index_schema_version: 1
---

# Erdélyi versenytársak — Ignis Academy / ExarLabs

> Think Agent Orchestrator v0.9 demo-futás · 1 kör · 2026-05-22

## Cél

Erdélyi versenytársak feltérképezése két profilban: (1) AI-alapú / gyakorlati digitális oktatás, IT-képzés, coding bootcamp; (2) szoftver- és AI-fejlesztő cégek. Kontextus: az ExarLabs új, **Ignis Academy** nevű gyakorlati AI/digitális tanulási brandet indít (magyarul, később románul).

## Team

| AI | Szerep | Transport | Model / URL |
|----|--------|-----------|-------------|
| Claude | Karmester / szintézis | API (orchestrator) | claude-opus-4-7 |
| ChatGPT | Kontextus-import | Böngésző (Chrome MCP) | [EXL Site documentation chat](https://chatgpt.com/g/g-p-69107df0495c81918db395f6ace82cf0/c/6a0c6d8e-2dd0-8392-bb8b-5fbdc4423e2e) |
| Perplexity Pro | Kutató (sourced) | Böngésző (Chrome MCP) | [search 7997a644](https://www.perplexity.ai/search/7997a644-d565-4082-8983-8b7f3d0f530a) |

## Raw Notes — Round 1

### ChatGPT kontextus (drift-szinkron a böngésző-szálból)
- A chat az ExarLabs projektben él, de tartalma az **Ignis Academy** különválasztásáról szól.
- Ignis Academy = önálló brand, önálló domain, önálló oktatási szolgáltatás és pozicionálás. Az ExarLabs-ból csak a munkamódszert / gondolkodási mélységet / háttérkontextust viszi tovább, NEM ExarLabs-aloldalként.
- Pozicionálás: **ne tanfolyamlistaként, hanem gyakorlati digitális tanulási brandként**. Magyarul indul, később románul (és esetleg angolul).
- Vault-megerősítés (`02_Areas/ExarLabs/CLAUDE.md`): Ignis = pályázati finanszírozású AI-alapú enterprise learning platform (B2B SaaS) + akkreditált digitális kompetencia-képzés. ExarLabs = 10 fős erdélyi IT-cég, Frappe-alapú fejlesztés.

### Perplexity findings (sourced, városonként)
**Kolozsvár**
- **Softech / Codespring** — kolozsvári magyar tulajdonú szoftvercég, az egyik legnagyobb erdélyi magyar fejlesztő, több városban csapatokkal. *(edu.codespring)*
- **Codespring Mentorprogram** — hosszabb távú, full-stack fókuszú gyakorlati mentorprogram egyetemistáknak. *(edu.codespring)* → **közvetlen oktatási versenytárs**
- **Versenyelőny 4.0** — többnapos intenzív gyakorlati üzletfejlesztési képzéssorozat KKV-knak. *(transtelex)*
- **Fortech** — nagy szoftverszolgáltató, kolozsvári központtal, regionális irodákkal (Brassó, Nagyvárad). *(techbehemoths)*

**Marosvásárhely**
- **Codespring Mentorprogram MV** — full-stack képzés Sapientia-hallgatóknak, heti rendszerességgel. *(edu.codespring)*
- **Code Labs Academy** — online IT-bootcamp (webfejlesztés, data science & AI, kiberbiztonság, design), Marosvásárhelyről is elérhető. *(codelabsacademy)* → **közvetlen oktatási versenytárs**

**Csíkszereda**
- **Erdélyi Mesterséges Intelligencia Tudásközpont** (tervezett) — magyar támogatású AI-tudásközpont, térségi AI-stratégia + alkalmazási projektek (önkormányzat, egészségügy, oktatás, mezőgazdaság). *(maszol)* → stratégiai figyelni-való, AI-fókusz
- Kereskedelmi coding bootcamp / IT-akadémia nyilvános nyoma nincs → **piaci rés Ignis Academy számára**.

**Sepsiszentgyörgy**
- **Venture Stúdió / StartUp HUB** — Erdély első venture stúdiója, tech-startupokat segít indulástól nemzetközi piacig. *(maszol)*
- **Code Studio** — a venture stúdió fejlesztői labora, szoftveres megoldások a portfólió-startupoknak. *(maszol)*

**Nagyvárad**
- **Make IT in Oradea / Bright Labs** — önkormányzat + IT-cégek programja: inkubátor, gyorsító, képzések a helyi tech-ökoszisztémának. *(oradea)*
- **Fortech – nagyváradi iroda** — regionális fejlesztőiroda nemzetközi ügyfeleknek. *(techbehemoths)*
- **Zexsoft** — nagyváradi székhelyű, egyedi end-to-end szoftvermegoldások (web + üzleti app). *(techbehemoths)*
- **LiftUp** — nemzetközi IT-tanácsadó (US + RO jelenlét), szoftverfejlesztés Nagyváradról is. *(techbehemoths)*

**Brassó**
- **ZegaSoftware – Software Development Bootcamp** — 3 hónapos, napi 8 órás intenzív Java- + AI-bootcamp, belső projekt + álláslehetőség a végén. *(zegasoftware)* → **közvetlen oktatási versenytárs**
- **Fortech – brassói iroda** — regionális szoftverfejlesztő iroda. *(techbehemoths)*

## Key Insights (szintézis)

1. **A két profil élesen szétválik.** Az igazi *oktatási* versenytárs kevés: **Code Labs Academy** (online, AI-t is tanít), **ZegaSoftware bootcamp** (Java+AI, Brassó), **Codespring Mentorprogram** (de ez tehetség-pipeline, nem kereskedelmi brand). A többi (Fortech, Zexsoft, LiftUp, Softech) **szoftvercég**, nem oktatási brand — ExarLabs-szintű peer, nem Ignis-versenytárs.
2. **Piaci rés a magyar nyelvű, gyakorlati AI-oktatásban.** Egyik szereplő sem pozicionálja magát kifejezetten *magyar nyelvű, gyakorlati AI/digitális tanulási brandként* — pont az Ignis Academy célpozíciója. A Code Labs Academy angol/online és általános IT; a Csíkszeredai AI-központ stratégiai/közszféra, nem lakossági kurzus-brand.
3. **Csíkszereda fehér folt** kereskedelmi IT-oktatásban, viszont jön a tervezett AI-tudásközpont → potenciális partner VAGY versenytárs, érdemes korán kapcsolatba lépni.
4. **A Codespring a legkomolyabb erdélyi magyar referencia** (brand-erő, regionális lefedettség) — pozicionálási benchmark, nem közvetlen oktatási rivális.

## Nyitott kérdések (eszkaláció a döntési hatósághoz)

- Az Ignis Academy elsődleges célközönsége **lakossági/diák** (B2C bootcamp) vagy **vállalati** (B2B digitális kompetencia)? Ez dönti el, kik a valódi versenytársak (Code Labs Academy vs. Versenyelőny 4.0 típusú vállalati képzés).
- Versenytárs-e vagy partner a Csíkszeredai AI-tudásközpont?
- Kell-e mélyebb kutatás a románul futó (nem magyar) erdélyi bootcampekről (pl. kolozsvári román nyelvű akadémiák)? Ez a 2. nyelvi fázishoz releváns.

## Hivatkozott
- Skill: `think-agent-orchestrator-v09` · capability: [`00_Prompts/BDOS/capabilities/think-engine/CLAUDE.md`](../../../00_Prompts/BDOS/capabilities/think-engine/CLAUDE.md)
- ExarLabs kontextus: [`02_Areas/ExarLabs/CLAUDE.md`](../../ExarLabs/CLAUDE.md)
