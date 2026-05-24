---
title: 00_DECISIONS_INDEX
generated_by: librarian v0.5
generated_at: 2026-05-11T00:00:00
scope: 00_Prompts/
mode: index
id: 1cb0266d-f8b9-4629-97a5-ba3a90c09001
index_schema_version: 1
---

# 00_Prompts — Döntések Index

> Stratégiai, taktikai és operacionális döntések a rendszer-szintű tartalmakban.
> Forrás-referenciák: fájl + kontextus.

---

## Stratégiai döntések

| # | Döntés | Dátum | Forrás |
|---|---|---|---|
| S-01 | **BDOS umbrella-struktúra bevezetése** — minden agent és capability `00_Prompts/BDOS/` alatt él, domain-mentes meta-réteg | 2026-05-11 | `BDOS/CLAUDE.md` |
| S-02 | **`agents/` mappa megszűnt** — áthelyezve `BDOS/agents/`-be; az eredeti `00_Prompts/agents/` path deprecated | 2026-05-11 | BDOS refaktor (context paraméter) |
| S-03 | **Librarian v0.5 aktív** — 6 mód (index, retrieve, tidy, audit, integrate, deep-clean); PDF olvasás (pdftotext) integrate módban | 2026-05-11 | `BDOS/agents/librarian.md` §9 Changelog |
| S-04 | **Két-fájlos agent elhelyezés** — canonical `BDOS/agents/<name>.md` + registration `.claude/agents/<name>.md`; verzió-szinkron kötelező | 2026-05-10 | `BDOS/agents/librarian.md` §11 |
| S-05 | **Agent-sprawl limit: 4-5 agent max** — nem 15-20; hierarchia akkor élesedik ha 3+ worker egy domain alatt | 2026-05-11 | `BDOS/CLAUDE.md` — Aktív agentek szekció |
| S-06 | **Microsite Factory brand-névként rögzítve** (canonical path: `web-publishing/`) | 2026-05-11 | `BDOS/capabilities/web-publishing/CLAUDE.md` — Open questions, [x] Név |
| S-07 | **Retrieval-based cognition** alapelv — agentek nem emlékeznek, visszakeresnek; Librarian a kulcs réteg | 2026-05-11 | `BDOS/CLAUDE.md` — Alapelvek |
| S-08 | **Kontextus-védelem alapelv** — retrieve módban te olvasol, hívó csak szűrt összegzést kap | 2026-05-11 | `BDOS/agents/librarian.md` §2 Mission |

---

## Taktikai döntések

| # | Döntés | Dátum | Forrás |
|---|---|---|---|
| T-01 | **Navigator Plugin v0.3 aktív** — „Intelligens Motor"; csatorna-intelligencia 52 epizód szintéziséből táplálva; v0.2 legacy (nem törölt) | 2026-04-06 | `Claude/Plugins/navigator-plugin-v0.3/CHANGELOG.md` |
| T-02 | **Verzió-suffix konvenció a Navigator Plugin-ban** — minden skill és command tartalmazza a verzió-suffixet (pl. `-v0.3`) a visszafelé-kompatibilitásért | 2026-04-06 | `Claude/Plugins/navigator-plugin-v0.3/CHANGELOG.md` — Verzió-suffix konvenció szekció |
| T-03 | **Pre-publish + post-publish workflow összekötve** Navigator v0.3-ban — `/csatorna-intelligencia` visszatáplál a metadata commandokba | 2026-04-06 | `Claude/Plugins/navigator-plugin-v0.3/CHANGELOG.md` |
| T-04 | **Sonrisa dashboard update kétfázisú architektúra** — Phase 1 (Cowork: Monthly Brief generálás) + Phase 2b (Claude for Excel: cellák közvetlen írása) | 2026-04-20 | `Claude/Plugins/Sonrisa Management Plugin/README.md` — cps-dashboard-update szekció |
| T-05 | **Speed Reader v0.7 multi-agent architektúra** — Speed-Reader (orchestrátor) + Context-Researcher + Chapter-Analyzer; párhuzamos futás ahol lehetséges | ~2026-02 | `Claude/Plugins/speed-reader-plugin/README.md` — Multi-Agent Benefits |
| T-06 | **Google Drive sync** a Speed Reader-ből — `/upload` command, PARA-struktúrát tartja a felhőben | ~2026-02 | `Claude/Plugins/speed-reader-plugin/README.md` |
| T-07 | **Yahoo cleanup state file alapú** — `yahoo-cleanup-state.md` persistent state, dátum-alapú visszafelé haladás | 2026-04-02 | `Claude/Plugins/Personal Utils Plugin/README.md` — State fájl szekció |
| T-08 | **Kettős hosting stratégia a Microsite Factory-ban** — Netlify (dev sandbox) + Cloudflare Pages (production edge); még nem végleges | 2026-05-11 | `BDOS/capabilities/web-publishing/CLAUDE.md` — Architektúra |

---

## Operacionális döntések

| # | Döntés | Dátum | Forrás |
|---|---|---|---|
| O-01 | **`04_Archive/` indexelhető** a Librarianban (v0.3 óta) — explicit scope-ban vagy `include_archive: true` flaggel; globális futásban default nem mélyen | 2026-05-11 | `BDOS/agents/librarian.md` §3 |
| O-02 | **Tidy mód dry_run default true** — Sprint 3 alatt visszakérdez minden mozgatásnál | 2026-05-11 | `BDOS/agents/librarian.md` §4.3 Safety |
| O-03 | **Egy hívás = egy mód** — Librarian soha nem kever módot egy futáson belül | 2026-05-11 | `BDOS/agents/librarian.md` §3 + §10 Anti-patterns |
| O-04 | **File collision handling** Speed Reader-ben — soha nem írja felül; `-v2`, `-v3` suffix | ~2026-02 | `Claude/Plugins/speed-reader-plugin/README.md` — Collision handling |
| O-05 | **DH pilot pointer** — `BDOS/pilots/deak-husuzlet.md` csak pointer, a valódi napló `02_Areas/Deák Húsüzlet/brainstorm/brainstorm_bdos.md`-ben él; ne duplikáld | 2026-05-11 | `BDOS/pilots/deak-husuzlet.md` |
