---
title: BDOS vs marveen — részletes architekturális összehasonlítás
date: 2026-05-30
author: Becze Szabolcs (Claude-elemzés)
status: active
description: Dimenziónként pontozott (1-10) összehasonlítás a BDOS (markdown-native cognition OS Claude Code-on) és a marveen (önállóan hostolható, többcsatornás AI-csapat framework) között. Mindkettő Claude Code-ra épül, de eltérő kategória.
tags: [bdos, marveen, comparison, agent-architecture, exarlabs]
id: b2a98d05-ad4d-4a06-98c1-1ad0c2fa988d
index_schema_version: 1
---

# BDOS vs marveen — részletes összehasonlítás

> Forrás: marveen klónozva ide: `5. ExarLabs/marveen` (commit `4e143d4`, 2026-05-30, ~300 commit, 25 vitest fájl). BDOS forrás: `0. Ideas Vault/00_Prompts/BDOS/`. Elemzés dátuma: 2026-05-30.

---

## 0. Egymondatos esszencia

- **marveen**: Önállóan hostolható, **telepíthető szoftvertermék** (TypeScript/Node service), ami a Claude Code-ot egy folyamatosan futó, proaktív, **többcsatornás (Telegram/Slack/Discord) AI-csapattá** alakítja, ami "fut, amíg te alszol". Háttérszolgáltatás + webdashboard + tmux-ben futó agent-flotta.
- **BDOS**: **Markdown-native cognition operating system** egy Obsidian-vaulton belül, Claude Code subagentekkel. Nem szoftvertermék, hanem *externalizált gondolkodási infrastruktúra*: az AI megfigyel, strukturál, javasol; az ember dönt. Nincs daemon az agentekhez, nincs build, a markdown a forrás-az-igazságra.

**Kulcsfelismerés:** a kettő **nem ugyanaz a kategória**. marveen egy *deployment/runtime termék* (operations-heavy, mindig fut), BDOS egy *kogníció-architektúra* (knowledge-heavy, hívásra fut). Közös DNS: Claude Code-alap, többszereplős, perszonál-operátornak, Claude előfizetésre (nem metered API). Ezért a pontozásnál minden dimenziónál jelzem, hogy a dimenzió melyik rendszer "hazai pályája".

---

## 1. Dimenziónkénti pontozás (1-10)

Skála: 1 = nincs/kezdetleges, 5 = működik de korlátos, 8 = erős/érett, 10 = best-in-class az adott kontextusban.

| # | Dimenzió | BDOS | marveen | Nyertes |
|---|---|:---:|:---:|---|
| 1 | Filozófiai tisztaság / célfókusz | **10** | 8 | BDOS |
| 2 | Multi-agent orchestráció (valódi delegálás) | 5 | **9** | marveen |
| 3 | Runtime / process-modell (folyamatos futás) | 3 | **9** | marveen |
| 4 | Perszisztencia / memória-modell | **8** | **8** | döntetlen |
| 5 | Tudás-indexelés / retrieval | **9** | 7 | BDOS |
| 6 | Skill-rendszer | 7 | **9** | marveen |
| 7 | Ütemezés / automatizáció | 6 | **9** | marveen |
| 8 | Csatornák / felhasználói interfész | 3 | **10** | marveen |
| 9 | Dashboard / vizualizáció | **9** | 8 | BDOS (szorosan) |
| 10 | Biztonság / jogosultság / safety | **9** | **9** | döntetlen |
| 11 | Tanulási hurok / önfejlesztés | 7 | **8** | marveen (szorosan) |
| 12 | MCP / eszköz-integráció | 6 | **9** | marveen |
| 13 | Telepítés / deployment / hordozhatóság | 4 | **9** | marveen |
| 14 | Multi-device támogatás | **8** | 5 | BDOS |
| 15 | Naplózás / auditálhatóság | **9** | 7 | BDOS |
| 16 | Dokumentáció minősége | **9** | 8 | BDOS (szorosan) |
| 17 | Érettség / tesztlefedettség / kódminőség | 5 | **9** | marveen |
| 18 | Bővíthetőség | 7 | **8** | marveen (szorosan) |
| 19 | Token-hatékonyság | **9** | 8 | BDOS (szorosan) |
| 20 | Reziliencia / hibakezelés | 4 | **10** | marveen |
| 21 | Governance / "alkotmány" / önfegyelmezés | **10** | 7 | BDOS |
| 22 | Üzleti/kognitív domain-mélység (sales/marketing/knowledge) | **9** | 5 | BDOS |
| | **Átlag** | **6.9** | **8.1** | **marveen** |

> Az átlag félrevezető: marveen a *gépészeti/üzemeltetési* dimenziók többségében nyer (mert az a kategóriája), BDOS a *kognitív/governance* dimenziókban dominál. Ha csak az "AI mint gondolkodási partner egy tudás-korpuszon" feladatra súlyozunk, BDOS vezet; ha "mindig elérhető, proaktív, többcsatornás asszisztens-flotta", marveen vezet elsöprően.

---

## 2. Dimenziónkénti indoklás

### 1. Filozófiai tisztaság / célfókusz — BDOS 10 / marveen 8
- **BDOS** szándékosan szűk és mély: "build externalized cognition, not autonomous intelligence" (PRIMER §1, §15). A cognition↔distribution "fal" (Presto/Broker soha nem dönti el, *mit* gondoljunk) ritka tisztaságú architekturális invariáns. Az ember mindig a döntéshozó.
- **marveen** célja világos ("AI-csapat ami fut amíg alszol"), de szélesebb és termékközpontúbb. Erős, de kevésbé filozófiailag élezett.

### 2. Multi-agent orchestráció — BDOS 5 / marveen 9
- **marveen**: *valódi* többszereplős rendszer. Minden agent külön Claude Code process saját tmux session-ben, saját `CLAUDE.md`+`SOUL.md`+memória+MCP. Tényleges inter-agent üzenetsor (SQLite `agent_messages`, 5s-es router, `tmux send-keys` injektálás) + **trust-graph** (`team-trust.ts`: trusted-peer vs untrusted wrapping prompt-injection ellen). Marveen mint PM delegál.
- **BDOS**: szándékosan **flat** (PRIMER invariáns #4) — agentek nem hívják egymást, a main Claude relayel. Ez tudatos döntés (no agent sprawl, 5-7 cap), de mint orchestrációs *képesség* gyengébb. Maestro "team" módjai meta-szinten kezelik a családot, nem futásidejű delegálás.

### 3. Runtime / process-modell — BDOS 3 / marveen 9
- **marveen**: két long-lived OS service (`launchd`/systemd, KeepAlive), tmux-flotta, watchdog + grace period, process-lock zombie-killer, pane-state detektor. **Folyamatosan fut.** Ez a hazai pályája.
- **BDOS**: nincs agent-daemon — hívásra (slash command) ébred, summary-t ad vissza, elalszik. Van egy Python scheduler daemon (Phase 6), de az agentek maguk nem futnak folyamatosan. Egy "mindig elérhető asszisztens" use-case-re ez gyenge.

### 4. Perszisztencia / memória — BDOS 8 / marveen 8 (döntetlen)
- **marveen**: per-agent tiered memória (`hot/warm/cold/shared`) SQLite-ban, **hibrid keresés** (FTS5 + Ollama vektor-embedding, RRF fúzió k=60), salience-decay (sosem töröl auto), PreCompact hook menti a döntéseket compact előtt. Technikailag kifinomult.
- **BDOS**: **markdown a forrás-az-igazságra**, minden DB regenerálható cache (ARCHITECTURE_BOUNDARIES). UUID-alapú stabil horgonyok (rename-túlélő), schema-verziózott state-fájlok, frontmatter-vezérelt. Filozófiailag tisztább (human-readable, git-elhető), de nincs vektor-szemantika. Egyetlen ratifikált kivétel: telemetria SQLite-kanonikus.
- **Döntetlen**: marveen technikailag gazdagabb (vektor+decay), BDOS architekturálisan tisztább és átláthatóbb (plaintext, verziózott, auditálható).

### 5. Tudás-indexelés / retrieval — BDOS 9 / marveen 7
- **BDOS** hazai pálya: a `vault-indexing` capability (~6460 LOC Python) FTS5 weighted bm25 (title×10, description×8, body×4), két-tier index (globális + 11 Area-scoped), orphan-detektálás, backlink-gráf, watchdog incremental refresh, 1966 note indexelve. A description-vezérelt retrieval 10-100x token-megtakarítás. Roadmapen networkx PageRank.
- **marveen**: a memória-FTS5+vektor erős, de ez *agent-memóriára* van hangolva, nem egy nagy dokumentum-korpusz strukturált navigálására. Nincs két-tier scoped index, nincs backlink-gráf, nincs orphan/gap-detektálás.

### 6. Skill-rendszer — BDOS 7 / marveen 9
- **marveen**: **self-learning skill-factory** — agentek automatikusan generálnak skillt nem-triviális munka után (5+ tool call, error→recovery, user-korrekció), meglévőt *patchelnek* (nem újraírnak), 3-szintű progressive disclosure (L0 index ~100 szó mindig betöltve → L1 → L2), fleet-wide propagáció `seed-skills/`-ből idempotensen. Záródó tanulási hurok.
- **BDOS**: 83 slash command + Cowork marketing-plugin 8 skillje. Strukturált, jól nevezett, de a skillek többnyire *kézzel írt* spec-ek; nincs auto-skill-generálás futásidőben (a tanulás külön learning-lifecycle-ben él, lásd #11).

### 7. Ütemezés / automatizáció — BDOS 6 / marveen 9
- **marveen**: schedule-runner (60s poll, cron, 30 perc catch-up, double-fire védelem), **persistent retry queue** (busy-skipped kritikus task sosem vész el, 1h után Telegram-alert), heartbeat (óránként natív adatgyűjtés, csak fontosra notifikál), dream-engine (éjszakai konszolidáció → DREAM.md), kanban 4-óránkénti audit.
- **BDOS**: dashboard-rezidens Python scheduler (Phase 6), multi-device SQLite lock, `requires_approval` flag, seedelt jobok (alfred-daily-harvest 04:00, weekly-curate). Működik, de fiatalabb, kevesebb reziliencia-réteg, és a telemetria szerint ~99% scheduler-zaj.

### 8. Csatornák / UI — BDOS 3 / marveen 10
- **marveen** elsöprő: provider-absztrakció (Telegram/Slack/Discord), hangleirat, kép/fájl, közvetlen API-path notifikációkhoz (akkor is megy, ha az interaktív session nem fut), webdashboard. Bárhonnan, bármilyen chat-appból.
- **BDOS**: nincs natív chat-csatorna. A felhasználó Claude Code-on (terminál/IDE) keresztül beszél vele, plusz Chrome MCP harvest. A dashboard read-only. Ez nem hiányosság, hanem kategóriakülönbség, de mint "interfész" gyenge.

### 9. Dashboard / vizualizáció — BDOS 9 / marveen 8
- **BDOS**: a Curator-vezérelt `_dashboards/` család **7 sérthetetlen törvénnyel**, kanonikus design-system (~70KB DESIGN_SYSTEM.md), automatikus lint (`lint.mjs`), SSE live-update, d3 force-graph az agent-családról, card-copy-ref pattern. Governance-vezérelt, konzisztens.
- **marveen**: egyetlen SPA (app.js 332KB, no framework), kanban drag-drop, memória-gráf (Canvas), token-usage, autonomy, vault. Funkcionálisan gazdag és interaktív (írható, nem csak olvasható), de kevésbé governance-elt/design-system-elt.
- BDOS szorosan vezet a *fegyelem és konzisztencia* miatt; marveen interaktívabb (CRUD).

### 10. Biztonság / safety — BDOS 9 / marveen 9 (döntetlen)
- **marveen**: code-locked hard-safety kategóriák (`publish_content`, `payment`, `data_delete`, `external_message` = `locked, maxLevel:1`; `email_send` cap maxLevel:2), trusted/untrusted prompt-injection wrapping, AES-256-GCM vault + OS Keychain, per-agent permission-profilok (marketer/researcher strict), supply-chain scanner (Bumblebee).
- **BDOS**: CAPABILITY_MODEL.md verb-osztályok (read/write-own/write-derived/delete/publish/send/browser/mcp-write), "never autonomous publish/send/delete", "connector data = untrusted", confirmation-gating + dry-run default a destruktív módoknál.
- **Döntetlen**: marveen futásidejű enforcement-je (server-side lock) konkrétabb; BDOS policy-architektúrája tisztább. Mindkettő ritkán érett biztonsági tudatosságot mutat hobbi-léptékhez.

### 11. Tanulási hurok / önfejlesztés — BDOS 7 / marveen 8
- **marveen**: skill-factory + dream-engine záródó hurok, *automatikus*. Erős, de kevésbé human-in-the-loop.
- **BDOS**: learning-lifecycle (`proposed → active → retired`), cap 15 active, **user-reviewable** ("the agent visibly learns, no hidden weights"). Filozófiailag kiválóbb (átlátható), DE: a hurok ki van drótozva de **gyakorlatlan** (0 active learning, 6 pending proposal). marveen működő hurokja most többet ér a gyakorlatban.

### 12. MCP / eszköz-integráció — BDOS 6 / marveen 9
- **marveen**: `mcp-catalog.json` 15 connector + local overlay, dashboard-vezérelt connector-hozzárendelés agentekhez, channel-health-monitor + auto-reconnect, **printing-press** (149+ CLI generálás OpenAPI/HAR-ból), vault-resolved auth.
- **BDOS**: használ MCP-t (Chrome harvest, marketing pluginok), de nincs központi connector-katalógus/management-réteg, se auto-reconnect.

### 13. Telepítés / deployment / hordozhatóság — BDOS 4 / marveen 9
- **marveen**: `install.sh` OS-detect → macOS (919 sor) / Linux / Windows(WSL), 7-lépéses interaktív flow, LaunchAgent/systemd, VPS first-class (OAuth token, swap-prompt), `update.sh` preflight-tel. Egy idegen gépre telepíthető.
- **BDOS**: nem telepíthető termék — a vault *maga* a rendszer. Hordozhatóság = Google Drive sync. Reprodukálni nehéz, dokumentálva van de nincs installer.

### 14. Multi-device — BDOS 8 / marveen 5
- **BDOS** hazai pálya: a vault Mac↔Windows között szinkronizál Google Drive-on, runtime-split (per-machine bináris cache a synced fán kívül, `runtime.py` OS-rezolúció), multi-device SQLite lock protokoll (`~/.bdos/device_id`). Tervezett, működő.
- **marveen**: alapvetően egy-host (egy Mac mini/VPS) modell. Több gép = több külön telepítés, nincs közös synced state.

### 15. Naplózás / auditálhatóság — BDOS 9 / marveen 7
- **BDOS**: 3-stream logging (operational/learning/version), append-only, dedikált writer API (`agent_log.py`, 28 oszlop, 15 eventtípus), token+duration+cost minden eventnél, version-log `reversible`+`rollback_path`+`approved_by` mezőkkel. Constitution-szintű.
- **marveen**: pino strukturált log + SQLite token-usage tracking JSONL-transcript-parse-ból, de nincs ennyire formalizált, verziózott, reversible-jelölt audit-trail az agent-evolúcióra.

### 16. Dokumentáció — BDOS 9 / marveen 8
- **BDOS**: kivételesen magas, önreflektív (PRIMER, 4 fázis-alkotmány, ARCHITECTURE_BOUNDARIES, FRONTMATTER_SCHEMA, CAPABILITY_MODEL). DE: **doc-drift** (Presto canonical v0.9/24-mód, de AGENTS_INDEX v0.5/12-mód; 83 command vs dokumentált 71).
- **marveen**: 14 feature-doc (what/why + how-it-works split), ATTRIBUTIONS.md minden kölcsönzött ötletre. DE: REBUILD_PROMPT_V3 részben stale a refaktorált `src/web/`-hez képest. Mindkettőnél van drift, BDOS-é mélyebb és önkritikusabb.

### 17. Érettség / tesztek / kódminőség — BDOS 5 / marveen 9
- **marveen**: ~300 commit 7 hét alatt, valódi PR-workflow (#170-#213), 25 vitest fájl (pure-logic modulokra: pane-state, prompt-safety, team-trust, cron…), tudatosan szétválasztott I/O vs döntés-logika a tesztelhetőségért. Production-hardening fázisban.
- **BDOS**: egyfejlesztős kísérleti platform, semver+canonical/registration sync-fegyelem erős, de **placeholder agentek** (Broker/Forge módok TBD, Forge 0 command), gyakorlatlan tanulási hurok, partial dashboard-ok. Kevés automatizált teszt.

### 18. Bővíthetőség — BDOS 7 / marveen 8
- **marveen**: új csatorna = 1 provider-fájl, új CLI = printing-press, új skill = auto-factory, új agent = dashboard-gomb (AI-generált CLAUDE.md/SOUL.md). Plugin-szerű.
- **BDOS**: új agent = canonical+registration scaffold (Maestro `team-introduce`), új capability-csomag, új dashboard (Curator `build`). Strukturált de manuálisabb; soft-gate lassítja szándékosan.

### 19. Token-hatékonyság — BDOS 9 / marveen 8
- **BDOS**: description-vezérelt retrieval (full-body olvasás elkerülése), context-protected subagentek (csak summary jön vissza), két-tier index. Mély token-tudatosság.
- **marveen**: progressive skill disclosure (L0 ~100 szó), natív heartbeat adatgyűjtés (nincs LLM-hívás ha nem kell), local embedding. Szintén erős, de a folyamatos flotta-futás drágább.

### 20. Reziliencia / hibakezelés — BDOS 4 / marveen 10
- **marveen** elsöprő: persistent retry queue at-least-once delivery+alert, process-lock zombie-killer, pane-state detektor (nem ejt promptot render-gap alatt), catch-up window, watchdog grace, channel auto-reconnect, update-preflight (refuses dirty/non-main). Production-sebek hegei.
- **BDOS**: hívás-alapú, kevés futásidejű failure-mód, de a multi-device lock + dry-run a meglétező védelmek. Mint *folyamatosan futó rendszer* nem reziliens, mert nem az a modellje.

### 21. Governance / alkotmány — BDOS 10 / marveen 7
- **BDOS** páratlan: fázis-alkotmányok (Phase 2/4/5/6), source-of-truth registry (ARCHITECTURE_BOUNDARIES: új write-nak deklarálnia kell a data-class-át *előbb*), 7 dashboard-törvény, agent-cap soft-gate, confirmation/dry-run mátrix, cognition-fal. Önfegyelmező rendszer.
- **marveen**: van governance (autonomy-config locks, attribution), de inkább safety-fókuszú, nem egy átfogó "alkotmányos" önkorlátozó keret.

### 22. Üzleti/kognitív domain-mélység — BDOS 9 / marveen 5
- **BDOS**: dedikált kogníció-rétegek üzleti domainekre — Presto (marketing distribution, 24 mód, seed→draft→prepare→approve→publish pipeline), Broker (sales one-to-one), Librarian (knowledge), Alfred (executive). Mély domain-modellezés.
- **marveen**: domain-agnosztikus flotta (backend dev, marketer, researcher role-ok), de a szerepek könnyűsúlyúak — nincs ennyire kidolgozott marketing/sales/knowledge kogníció-modell.

---

## 3. Miben jobb a BDOS

1. **Filozófiai tisztaság és governance** — a cognition↔distribution fal, a source-of-truth registry, a fázis-alkotmányok, az agent-cap soft-gate. Ez egy *önfegyelmező* rendszer; marveen-nek nincs ilyen átfogó kerete.
2. **Tudás-indexelés és retrieval** — két-tier scoped index, FTS5 weighted bm25, backlink-gráf, orphan/gap-detektálás, description-vezérelt token-megtakarítás. marveen memóriája agent-hangolt, nem korpusz-navigáló.
3. **Markdown-native átláthatóság** — minden human-readable, git-elhető, verziózott, auditálható. A "visibly learns, no hidden weights" elv. marveen állapota nagyrészt SQLite-ban (kevésbé átlátható).
4. **3-stream audit-trail** — reversible/rollback_path/approved_by az agent-evolúcióra. Constitution-szintű naplózás.
5. **Multi-device by design** — Mac↔Windows sync runtime-splittel és lock-protokollal.
6. **Domain-mélység** — kidolgozott marketing/sales/knowledge kogníció-rétegek, nem könnyűsúlyú szerepek.
7. **Dashboard-governance** — 7 törvény + design-system + auto-lint = konzisztencia.

## 4. Miben jobb a marveen

1. **Valódi multi-agent runtime** — külön processek, inter-agent üzenetsor, trust-graph, futásidejű delegálás. BDOS szándékosan flat.
2. **Folyamatos futás + proaktivitás** — heartbeat, dream-engine, "fut amíg alszol". BDOS hívásra ébred.
3. **Többcsatornás interfész** — Telegram/Slack/Discord, hang, kép, közvetlen notifikáció. BDOS-nak nincs natív chat-csatorna.
4. **Reziliencia** — persistent retry queue, zombie-killer, pane-state detektor, auto-reconnect, update-preflight. Production-érett hibakezelés.
5. **Telepíthetőség** — egy installer idegen gépre/VPS-re visz, OS-detect, service-management.
6. **Önfejlesztő skill-factory** — automatikus skill-generálás + patch + fleet-propagáció. BDOS tanulása kézibb és gyakorlatlan.
7. **Érettség** — 25 teszt, PR-workflow, I/O↔logika szétválasztás, ~300 commit production-hardeninggel.
8. **MCP-management** — connector-katalógus, auto-reconnect, printing-press CLI-generálás.
9. **Hibrid memória-keresés** — FTS5 + vektor-embedding RRF-fúzióval, salience-decay.

## 5. Ami megegyezik (közös DNS)

1. **Claude Code-alap** — mindkettő a Claude Agent SDK / Claude Code CLI-re épül, nem saját LLM-loop.
2. **Claude előfizetés, nem metered API** — mindkettő a Max/Pro OAuth-tokent használja.
3. **Perszonál-operátor célközönség** — szóló üzletember/power-user több projekttel, nem fejlesztő-SDK.
4. **Markdown-vezérelt agent-definíció** — mindkettőnél az agent személyisége/utasítása markdown (`CLAUDE.md`/`SOUL.md` vs canonical agent.md).
5. **SQLite mint state-store** — mindkettő SQLite-ot használ (marveen kanonikusan, BDOS derived cache + telemetria).
6. **Skill mint újrahasználható recept** — `SKILL.md` YAML-frontmatter + body mindkettőben (progressive disclosure mindkettőnél).
7. **Cron/ütemezés + heartbeat-szerű csendes ellenőrzés** — mindkettőnél van scheduler és "csak fontosra notifikálj" logika.
8. **Safety-tudatosság** — confirmation-gate / locked-kategóriák / "never autonomous publish-send-delete" mindkettőben.
9. **Confirmation a destruktív akciók előtt** — mindkettő human-in-the-loop a kockázatos műveleteknél.
10. **Dashboard a megfigyeléshez** — mindkettőnek van web-dashboardja.
11. **Attribution/dokumentációs kultúra** — mindkettő explicit dokumentálja az ötleteit/forrásait.

---

## 6. Verdikt és tanulságok az ExarLabs számára

A két rendszer **nem versenytárs, hanem komplementer**:

- **marveen = a "test" (runtime/üzemeltetés)**: hogyan futtass egy Claude-agent-flottát folyamatosan, reziliensen, többcsatornán, telepíthetően.
- **BDOS = az "elme" (kogníció/governance)**: hogyan strukturáld, indexeld, kontrolláld és tanítsd a gondolkodást átláthatóan, üzleti domain-mélységgel.

**A legértékesebb átemelhető ötletek marveen-ből a BDOS-ba:**
1. **Persistent retry queue + at-least-once delivery** — a BDOS scheduler reziliencia-hiányára közvetlen gyógyír.
2. **Hibrid memória-keresés (vektor + FTS5 RRF-fúzió)** — a vault-indexing már FTS5; egy opcionális local-embedding réteg (Ollama) sokat dobna a szemantikus retrievalen.
3. **Önfejlesztő skill-factory minta** — a BDOS gyakorlatlan learning-hurokjának életre keltése automatikus skill-patcheléssel.
4. **Code-locked autonomy-kategóriák** — a CAPABILITY_MODEL policy-architektúráját kiegészíteni server-side enforcementtel.
5. **Channel-réteg** — ha a BDOS-t valaha "mindig elérhetővé" akarjuk tenni, marveen provider-absztrakciója a kész minta.

**A legértékesebb átemelhető ötletek BDOS-ból a marveen-be:**
1. **Source-of-truth registry + markdown-canonical / DB-derived elv** — marveen állapota átláthatóbb és git-elhetőbb lenne.
2. **Két-tier scoped knowledge-index** — nagy dokumentum-korpuszra marveen memóriája gyenge.
3. **3-stream reversible audit-trail** — az agent-evolúció követhetőségéhez.
4. **Governance-alkotmány + agent-cap soft-gate** — az "agent sprawl" ellen.
5. **Dashboard-design-system + auto-lint** — konzisztenciához.

> **Összegzés:** Ha egy *folyamatosan futó, többcsatornás, telepíthető asszisztens-flottát* akarsz → marveen a referencia. Ha egy *átlátható, governance-elt, üzleti-domain-mély kogníció-infrastruktúrát* akarsz egy tudás-korpusz fölött → BDOS a referencia. A BDOS-nak marveen runtime-rezilienciája és csatorna-rétege hiányzik; a marveen-nek a BDOS governance-mélysége és tudás-indexelése. A két rendszer egymás vakfoltjait tölti ki.
