---
title: Mit tanulhat a BDOS a marveen-től — prioritált döntési lista
date: 2026-05-30
author: Becze Szabolcs (Claude-elemzés)
status: active
description: Fontossági sorrendbe rakott, egyenként átnézhető lista a marveen-ből BDOS-ba átemelhető ötletekről. Minden tételhez: mi ez marveen-ben, miért számít a BDOS-nak, illeszkedés/effort, és egy DÖNTÉS mező (adopt / adapt / skip / later).
tags: [bdos, marveen, roadmap, decision-list, exarlabs]
id: d2911b90-f576-4cb5-b79c-d5d524328a4c
index_schema_version: 1
---

# Mit tanulhatunk a marveen-től — prioritált döntési lista

> Cél: végigmegyünk rajta egyenként, és minden tételnél döntünk: **adopt** (átvesszük), **adapt** (átszabva), **skip** (nem kell), **later** (későbbre). A "Döntés" mezőt a review során töltjük.
>
> Rangsorolás elve: **impact a BDOS-ra × illeszkedés a BDOS-filozófiához × megvalósíthatóság**. A marveen sok erőssége (daemon, csatorna, installer) tudatosan NEM BDOS-cél — ezek hátrébb kerülnek vagy kimaradnak. A lista azt rangsorolja, ami valódi BDOS-hiányt tölt, nem azt, ami marveen-ben menő.

## Áttekintő tábla

| # | Tétel | Tier | BDOS-hiány amit betölt | Effort | Filozófia-illeszkedés | Döntés |
|---|---|:---:|---|:---:|:---:|---|
| 1 | Persistent retry queue (at-least-once scheduler) | **P1** | reziliencia (4/10) | közepes | magas | ⬜ |
| 2 | Hibrid memória-keresés (vektor + FTS5 RRF) | **P1** | szemantikus retrieval | közepes | magas | ⬜ |
| 3 | Self-improving skill-factory (auto-gen + patch) | **P1** | gyakorlatlan tanulási hurok | nagy | magas | ⬜ |
| 4 | PreCompact hook — döntésmentés compact előtt | **P1** | kontextus-vesztés | kicsi | magas | ⬜ |
| 5 | Code-locked autonomy + server-side enforcement | **P2** | policy futásidejű kikényszerítés | közepes | magas | ⬜ |
| 6 | Trust-graph (trusted vs untrusted input wrapping) | **P2** | prompt-injection védelem | közepes | magas | ⬜ |
| 7 | Salience-decay + tiered memória (hot/warm/cold) | **P2** | memória-higiénia | közepes | közepes | ⬜ |
| 8 | Dream-engine — éjszakai konszolidáció (DREAM.md) | **P2** | proaktív szintézis | közepes | magas | ⬜ |
| 9 | MCP connector-katalógus + health/auto-reconnect | **P2** | eszköz-management | közepes | közepes | ⬜ |
| 10 | printing-press — CLI-gen OpenAPI/HAR-ból | **P2** | token-hatékony tool-integráció | nagy | közepes | ⬜ |
| 11 | Pure-logic / I/O szétválasztás + vitest tesztek | **P2** | érettség (Python capabilities) | közepes | magas | ⬜ |
| 12 | Token-usage tracker JSONL-transcript-parse | **P3** | meglévő telemetria gazdagítás | kicsi | közepes | ⬜ |
| 13 | Csatorna-réteg (Telegram/Slack/Discord provider) | **P3** | natív chat-interfész (nincs) | nagy | alacsony* | ⬜ |
| 14 | Watchdog / process-lock / pane-state reziliencia | **P3** | csak ha daemon-flotta lesz | nagy | alacsony* | ⬜ |
| 15 | Installer / reprodukálhatóság | **P3** | hordozhatóság | nagy | alacsony* | ⬜ |

\* alacsony illeszkedés = csak akkor releváns, ha a BDOS valaha "mindig futó, telepíthető termék" irányba mozdul. Ma nem az.

---

## P1 — Magas impact, erős illeszkedés (ezekkel kezdjünk)

### 1. Persistent retry queue (at-least-once delivery)
- **marveen-ben:** ha egy ütemezett, üzlet-kritikus task azért nem futott le, mert az agent épp foglalt volt, NEM vész el — bekerül egy `pending_task_retries` SQLite táblába, örökké újrapróbálja, és 1 óra után Telegram-alertet küld. Double-fire védelem + 30 perc catch-up window restart után.
- **Miért számít BDOS-nak:** a BDOS Phase 6 scheduler a leggyengébb reziliencia-pontunk (4/10). A telemetria szerint ~99% scheduler-zaj, és nincs garancia, hogy egy kihagyott job pótlódik. Ez közvetlen gyógyír.
- **BDOS-illeszkedés:** kiváló — már van `scheduled_jobs` + `job_runs` tábla az `agent_observability.db`-ben, ide egy `pending_retries` réteg natúrán illeszkedik.
- **Effort:** közepes (Python, a meglévő scheduler.py kiegészítése).
- **Kockázat:** alacsony.

### 2. Hibrid memória-keresés (vektor-embedding + FTS5, RRF-fúzió)
- **marveen-ben:** FTS5 full-text + local Ollama `nomic-embed-text` (768-dim) vektor-keresés, Reciprocal Rank Fusion-nal (k=60) összeolvasztva. Teljesen lokális, Ollama opcionális (ha nincs, FTS5-only fallback).
- **Miért számít BDOS-nak:** a vault-indexing ma FTS5-only (kulcsszó-alapú). A dokumentált bottleneck a description-coverage ÉS a szemantikus miss (releváns tartalom más Area-ban / más szóval). Egy opcionális local-embedding réteg pont ezt oldná, anélkül hogy felhőbe küldenénk bármit.
- **BDOS-illeszkedés:** erős — a markdown marad forrás-az-igazságra, a vektor csak egy újabb derived cache a `vault.db` mellé. Opcionális (degradál FTS5-re).
- **Effort:** közepes (Ollama dependency + embedding-tábla + RRF a query.py-ban).
- **Kockázat:** közepes (Ollama futtatás multi-device környezetben — per-machine, mint a bináris cache).

### 3. Self-improving skill-factory (auto-generálás + patch)
- **marveen-ben:** az agent nem-triviális munka után (5+ tool call, error→recovery, user-korrekció, multi-step workflow) automatikusan SKILL.md-t generál vagy meglévőt *patchel* (célzott edit + "Pitfalls" bejegyzés), nem újraír. Fleet-wide propagáció `seed-skills/`-ből idempotensen.
- **Miért számít BDOS-nak:** a BDOS learning-lifecycle ki van drótozva, de **gyakorlatlan** (0 active learning, 6 pending proposal). marveen mintája megmutatja, hogyan zárd be a hurkot a gyakorlatban — automatikus capture + human-review (ami a BDOS "visibly learns" elvét megőrzi).
- **BDOS-illeszkedés:** erős, de finomítandó — a BDOS szándékosan human-in-the-loop (proposed→active→retired). Az auto-generálás itt = auto-`proposal`, nem auto-`active`. Ez a kettő házasítása az igazi nyeremény.
- **Effort:** nagy (trigger-detektálás + proposal-generátor + a meglévő learning-lifecycle-be kötés).
- **Kockázat:** közepes (zaj-proposalok elkerülése).

### 4. PreCompact hook — döntésmentés context-compact előtt
- **marveen-ben:** egy Claude Code PreCompact hook automatikusan elmenti a fontos döntéseket a memóriába, mielőtt a context összenyomódik. Így a hosszú session-ök tudása nem vész el.
- **Miért számít BDOS-nak:** a BDOS-nak van SessionEnd hook-ja (activity-ledger), de PreCompact nincs. Hosszú agent-futások közben elveszhet a "miért döntöttünk így" kontextus. Olcsó, nagy hatású.
- **BDOS-illeszkedés:** kiváló — a `.claude/settings.json` hook-infra már megvan (SessionEnd ott él), egy PreCompact hozzáadása triviális. Output egy markdown decision-shard.
- **Effort:** kicsi.
- **Kockázat:** alacsony.

---

## P2 — Közepes impact / közepes effort (második kör)

### 5. Code-locked autonomy-kategóriák + server-side enforcement
- **marveen-ben:** `autonomy-config.json` per-kategória trust-szint (1=notify, 2=propose+approve, 3=autonomous). A hard-safety kategóriák (`publish_content`, `payment`, `data_delete`, `external_message`) **kódban lock-oltak** `maxLevel:1`-re, sosem emelhetők; `email_send` cap `maxLevel:2`. A backend kikényszeríti.
- **Miért számít BDOS-nak:** a BDOS-nak van CAPABILITY_MODEL policy-architektúrája (verb-osztályok), de az enforcement ma "az agent betartja a promptot" szinten van. marveen futásidejű, kód-szintű lock-ja erősebb garancia.
- **BDOS-illeszkedés:** jó — a policy már létezik, ehhez egy enforcement-réteg kell (pl. a scheduler `requires_approval` flag-jének kiterjesztése + egy kis guard-modul).
- **Effort:** közepes. **Kockázat:** alacsony.

### 6. Trust-graph — trusted vs untrusted input wrapping
- **marveen-ben:** inter-agent üzenetek és külső input `<trusted-peer>` vs `<untrusted>` tagbe csomagolva a `reportsTo`/`delegatesTo` reláció alapján, prompt-injection ellen; a security-tageket scrubbeli a payloadból.
- **Miért számít BDOS-nak:** a BDOS már kimondja "connector-adat = untrusted input (prompt-injection)", de nincs konkrét wrapping-mechanizmus. Ez operacionalizálja a meglévő elvet.
- **BDOS-illeszkedés:** jó (a flat orchestrációban kevésbé az inter-agent, inkább a connector/web-input wrapping releváns).
- **Effort:** közepes. **Kockázat:** alacsony.

### 7. Salience-decay + tiered memória (hot/warm/cold/shared)
- **marveen-ben:** memóriák salience-pontszáma idővel csökken (×0.995/nap 7 nap után), hozzáféréskor nő (+0.1), de SOSEM törlődik auto. Tier-ek mozgatása (hot→cold) éjszaka.
- **Miért számít BDOS-nak:** segítene priorizálni, mi releváns MA a vault-ban, a stale tartalom degradálásával (a Librarian tidy/deep-clean kézi ma).
- **BDOS-illeszkedés:** közepes (a markdown-forrás elvvel óvatosan — a decay egy derived score, nem törlés).
- **Effort:** közepes. **Kockázat:** közepes (ne degradáljon fontos, ritkán olvasott referenciát).

### 8. Dream-engine — éjszakai konszolidáció
- **marveen-ben:** ~02:00 csendes loop, `DREAM.md`-t termel 5 vödörrel (skill-javaslatok, memória-egészség, holnap top-3 prioritás, heti tool-scouting, skill-flotta health). A reggeli briefing ezt elé fűzi.
- **Miért számít BDOS-nak:** a BDOS-nak van reggeli rutin (`morning-v0.2`) + Maestro reflect, de nincs proaktív éjszakai szintézis. Alfred/Maestro reflect-tel kombinálható.
- **BDOS-illeszkedés:** jó (illik a Maestro reflect + Alfred today-hez).
- **Effort:** közepes. **Kockázat:** alacsony.

### 9. MCP connector-katalógus + health-monitor / auto-reconnect
- **marveen-ben:** `mcp-catalog.json` (15 connector + local overlay), dashboard-vezérelt agent-hozzárendelés, channel-health-monitor ami auto-reconnect-eli a leesett stdio pipe-okat.
- **Miért számít BDOS-nak:** a BDOS használ MCP-t (Chrome harvest, marketing pluginok), de nincs központi katalógus/management. Az auto-reconnect a harvest-jobok megbízhatóságát növelné.
- **BDOS-illeszkedés:** közepes. **Effort:** közepes. **Kockázat:** alacsony.

### 10. printing-press — token-hatékony CLI generálás
- **marveen-ben:** Mike Van Horn `cli-printing-press`-e OpenAPI-spec / docs-URL / **HAR-capture** alapján generál agent-natív, token-takarékos CLI-ket (API-khoz amiknek nincs MCP-je). 149+ kész CLI.
- **Miért számít BDOS-nak:** sok BDOS-integráció (Billingo, Wise, niche API-k) MCP nélkül. Egy HAR→CLI pipeline olcsóbb tokenben, mint egy teljes MCP.
- **BDOS-illeszkedés:** közepes. **Effort:** nagy (külső tool integ). **Kockázat:** közepes.

### 11. Pure-logic / I/O szétválasztás + unit-tesztek
- **marveen-ben:** a kódot tudatosan szétválasztják tiszta döntés-logikára és I/O-ra, hogy a kritikus modulok (prompt-safety, cron, retry, trust) vitest-tel tesztelhetők legyenek. 25 teszt-fájl.
- **Miért számít BDOS-nak:** a BDOS Python capabilities (vault-indexing, scheduler, observability ~6460 LOC) szinte teszteletlen. A kritikus részekre (query.py FTS, scheduler lock, migrate_uuid dry-run) pytest sokat dobna az érettségen (BDOS 5/10).
- **BDOS-illeszkedés:** erős (governance-szellem). **Effort:** közepes. **Kockázat:** alacsony.

---

## P3 — Opcionális / alacsony filozófia-illeszkedés (csak ha irányt váltunk)

### 12. Token-usage tracker JSONL-transcript-parse-ból
- **marveen-ben:** parse-olja a `~/.claude/projects/` JSONL transcript-eket, per-agent/session token-számlálás, kanban-korrelációval.
- **BDOS:** már van token-logging az `agent_logs`-ban (writer API). marveen módszere (transcript-parse) kiegészíthetné a nem-agent (main Claude) használat mérését. Kis nyeremény.
- **Effort:** kicsi.

### 13. Csatorna-réteg (Telegram/Slack/Discord provider-absztrakció)
- **marveen-ben:** provider-interfész, hang/kép, közvetlen notify-path. Ez marveen legnagyobb erőssége (10/10).
- **BDOS:** ma nincs natív chat-interfész (3/10) — de ez **tudatos**: a BDOS hívásra-futó kogníció, nem mindig-elérhető asszisztens. CSAK akkor releváns, ha a BDOS-t valaha "mindig elérhető" irányba visszük (pl. Alfred mint Telegram-bot). Akkor marveen a kész minta.
- **Effort:** nagy. **Döntés-kérdés:** akarunk-e egyáltalán chat-csatornát? Stratégiai, nem technikai.

### 14. Watchdog / process-lock / pane-state reziliencia
- **marveen-ben:** zombie-killer, pane-state detektor, watchdog grace. Ezek a tmux-flotta daemon-modell sebei.
- **BDOS:** csak akkor releváns, ha a BDOS daemon-flottát futtat (ma nem). Skip, hacsak nem #13 mellett döntünk.

### 15. Installer / reprodukálhatóság
- **marveen-ben:** OS-detect installer, VPS-support, LaunchAgent/systemd.
- **BDOS:** a vault MAGA a rendszer; "telepítés" = Google Drive sync. Egy reprodukálható setup-script (Python deps, hook-ok, cache-bootstrap) hasznos lehet új gépre, de nem prioritás. Adapt, ha új gépet állítunk be.

---

## Javasolt sorrend a review-hoz

1. **Először a P1 négyes** (retry queue, hibrid keresés, skill-factory, PreCompact hook) — ezek a legnagyobb BDOS-hiányt töltik, és illenek a filozófiához.
2. **Aztán P2** biztonsági kettős (5, 6) + a tesztelés (11), mert ezek governance-erősítők.
3. **P3 stratégiai döntés** (#13 csatorna) — ez nem technikai, hanem irány-kérdés: akar-e a BDOS valaha "kilépni" a Claude Code-ból egy chat-felületre.

> **Megjegyzés a párhuzamos index-fixhez:** a review során felszínre jött, hogy a **Presto canonical (v0.9.0) ≠ registration (v0.6.0)** — ez egy nyitott verzió-szinkron sérülés, amit külön kell lezárni (a registration-t v0.9.0-ra húzni). Az `00_AGENTS_INDEX.md` már flag-eli.
