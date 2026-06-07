---
title: CLAUDE
description: Vault-szintű konvenciók — szervezeti elv, PARA értelmezés, agent rendszer, navigáció. Olvasd először, mielőtt bármit csinálsz a vault-ban.
date: 2026-05-11
author: Becze Szabolcs
status: active
id: 543df4c3-c9a1-4c47-8944-235841d14ad7
index_schema_version: 1
---

# Vault konvenciók

Ezt a fájlt olvassa minden AI / agent először, hogy megértse a vault szervezeti elvét.

## 0. Szövegezési alapszabály (MINDEN AI-generált szövegre)

> **Soha ne használj gondolatjelet (em dash, `—`) AI-generált szövegben.** Ez érvényes MINDEN generált tartalomra: marketing-poszt, leírás, teaser, dokumentum, commit-üzenet, dashboard-szöveg, bármi. Helyette: vessző, kettőspont, pontosvessző, pont vagy zárójel. A `--` (dupla kötőjel) szintén kerülendő. (User-preferencia, 2026-05-28.)

## 1. Szervezeti elv — Areas-dominant PARA

A vault **PARA-szerű** struktúrában él, **DE módosítva** a felhasználó munkaszervezéséhez:

| Mappa | Mit tartalmaz |
|---|---|
| `01_Projects/` | **Csak ténylegesen rövid távú, cross-cutting, deadline-os feladatok.** Általában üres vagy alig-tartalmazó. |
| `02_Areas/` | **A vault zöme.** Tartós felelősségi körök (Deák Húsüzlet, Navigátor Podcast, Sonrisa, Personal Growth, ExarLabs, stb.). Egy Area belül szabadon szervez domain szerint — **nem kell PARA-fraktál**. |
| `03_Resources/` | Külső input: könyvek, podcastok, transcript-ek, cikkek. Unit-független referencia anyag. |
| `04_Archive/` | Inaktív, lezárt anyag. Nem indexeljük automatikusan. |
| `05_DailyNotes/` | Napi jegyzetek (template-elve). |
| `00_Prompts/` | AI prompt-ok, agentek definíciói, plugin-ok, skill-ek. |
| `Templates/` | Új fájl sablonok. |

### Indoklás (miért nem orthodox PARA)

A felhasználó **manager/operátor** szerepkörben dolgozik. A "projektek" nála **éveken át tartó kapcsolatok** (egy üzletfejlesztés, egy podcast, egy elszámolási rendszer), amik **soha nem zárulnak le** — csak fázisai vannak. Ezért az Area-szintű csoportosítás logikusabb, mint a Project-átsorolás.

Egy Area belső szervezése **domain szerint** zajlik (pl. DH: `Business Development/`, `Marketing/`, `Products/`, `brainstorm/`, `design/`, `manual/`, `plugins/`). Nem PARA-fraktál.

## 2. Agent rendszer (BDOS — Business Development Operation System)

A vault egyúttal **AI-native cognition system** kísérleti terep. Az agentek **stabil gondolkodási szerepek**, nem chat-bot replikák.

A BDOS kanonikus belépője: [`00_Prompts/BDOS/CLAUDE.md`](00_Prompts/BDOS/CLAUDE.md). Itt él minden BDOS-tartalom (agents, capabilities, pilots).

### BDOS struktúra
- `00_Prompts/BDOS/CLAUDE.md` — BDOS belépő
- `00_Prompts/BDOS/agents/` — kanonikus agent definíciók (ember-olvasható)
- `00_Prompts/BDOS/00_AGENTS_INDEX.md` — meta-index minden agentről (verzió, státusz, hely)
- `00_Prompts/BDOS/ARCHITECTURE_BOUNDARIES.md` — **forrás-az-igazságra térkép.** Operacionális állapot (log/task/board/index/sidecar) írása ELŐTT ezt nézd: melyik tároló kanonikus, mi derived.
- `00_Prompts/BDOS/capabilities/` — projekt-független képesség-csomagok (pl. `web-publishing/` — AI microsite factory, kidolgozás alatt)
- `00_Prompts/BDOS/pilots/` — élő pilot-pointerek (DH)
- `.claude/agents/` — Claude Code runtime regisztráció (YAML config + thin pointer)

### Aktív agentek
Az aktuális lista mindig itt: `00_Prompts/BDOS/00_AGENTS_INDEX.md`.

Jelenleg (Phase 3.1 utáni verziók, 7 aktív agent):
- **Librarian** v0.8 — Knowledge Manager (6 mód + cache-first retrieve a vault-indexing capability-vel)
- **Maestro** v0.5 — Conductor + Reflective Nervous System (3 domain, 12 mód)
- **Curator** v0.5 — Representation layer (dashboard) kurátor (7 mód)
- **Presto** v0.5 — Marketing Cognition Layer + Distribution Engine (24 mód)
- **Broker** v0.3 — Sales Engine Executor (9 mód)
- **Forge** v0.1 — Practice Steward (capability-layer, módok v0.2-ben)
- **Alfred** v0.3 — Executive Cognition Layer + Cognition Curator (12 mód). Alfred v0.3 absorbeálta a korábbi Sage agentet (2026-05-28): harvest, curate, chat, learn módok + meta-learning loop.

Mind a 7 agent Phase 2.B (3 log-stream) + Phase 3.1 (description mandatory) compliant. Sage 2026-05-28-án deprecated, Alfred v0.3-ba merged.

### Slash command-ok
`.claude/commands/` — gyors agent-meghívás. Példák: `/lib-find`, `/dash-build`, `/pres-today`, `/maestro-status`, `/alf-harvest`, `/alf-chat`, `/alf-curate`.

## 3. Indexelési struktúra — két szint

A Librarian **két szinten** tartja a retrieval réteget:

### Tier 1 — Vault gyökér (globális)
A vault gyökerében:
- `00_INDEX.md` — PARA bontás + Scoped Units lista
- `00_KNOWLEDGE_MAP.md` — cross-domain térkép
- `00_DECISIONS_INDEX.md` — globális döntés-index
- `00_OPEN_QUESTIONS.md` — nyitott kérdések globálisan
- `00_GAPS.md` — vault-szintű inkonzisztenciák

### Tier 2 — Aktív unit-ok scoped indexe
Minden **substansiális aktív** Area saját 5 indexet kap a saját gyökerében. Kritérium:
- ≥ 30 fájl, VAGY
- saját `01_PROJECT_STATE.md`-vel rendelkezik, VAGY
- aktív sprint/munka folyik

**Most élő tier-2 unit-ok:**
- `02_Areas/Deák Húsüzlet/` (✅ scoped index v0.1)
- További aktívak indexelése folyamatban (Navigátor Podcast, Sonrisa, ExarLabs).

### Retrieval algoritmus
A Librarian retrieve módja **két szintet olvas**:
- Ha a query unit-specifikus → csak tier-2 (locality)
- Ha cross-domain vagy globális → tier-1 elsőként, drill down tier-2-be ha kell

## 4. Frontmatter konvenció

Minden új fájl frontmatter-rel kezdődik:
```yaml
---
title: <fájl neve>
date: <YYYY-MM-DD>
author: Becze Szabolcs
status: active | draft | done | archived
description: <egy-két mondat — KÖTELEZŐ, nem opcionális>
tags: [opcionális]
---
```

**`description:` kötelező minden új fájlban.** Ez az egyetlen legnagyobb hatású frontmatter mező: a vault-indexing capability (`capabilities/vault-indexing/`) FTS5 keresése ezen fut, és az agentek (Librarian, Maestro) 80%-ban ebből ítélik meg egy fájl relevanciáját a teljes body olvasása nélkül — 10-100x token megtakarítás retrieve módban. Tartalom-vezérelt legyen (1-2 mondat, mit tartalmaz a fájl, ki olvassa), nem generikus.

Verziózott fájlokhoz (agentek, project state, BMC, roadmap): `version: <semver>` mező.

**Phase 4 (2026-05-24 óta):** új fájloknak kötelező `id: <uuid4>` + `index_schema_version: 1` + `bdos_index: true|false` mezők is. Részletes spec: [`00_Prompts/BDOS/FRONTMATTER_SCHEMA.md`](00_Prompts/BDOS/FRONTMATTER_SCHEMA.md). Migration meglevő fájlokra: `python3 00_Prompts/BDOS/capabilities/vault-indexing/migrate_uuid.py --apply`.

## 5. Aktív üzleti munka

A vault zöme **élő, aktívan használt** munka, nem archivum. **Sprint 3** fut Deák-on (~2026-04 indult, beta launch 2026-05-15 célzott). Más unit-okban is folyamatos kadenciák.

**Következmény az AI-okra nézve:**
- Destruktív akció előtt **mindig** kérdezz vissza, kivéve ha explicit engedély van
- Sprint alatt aktív projektekben **fokozott óvatosság**
- Tidy / cleanup akciók: dry-run default, logoljon mindent

## 6. Reggeli rutinok és automatizációk

A `personal-utils:morning-v0.2`, `personal-utils:navigator-v0.1`, `personal-utils:yahoo-v0.2` skillek napi futnak. Output-juk a `05_DailyNotes/`-ba kerül.

## 7. Hierarchikus AI rendszer (jövőbeli)

A BDOS hosszú távon hierarchikus lesz: Domain Manager-ek (Knowledge Manager, Product Manager, Operations Manager, stb.) saját worker agent-ekkel. Egyelőre **flat** — main Claude orchestrál, agentek workerek. Hierarchia akkor élesedik, ha 3+ worker egy domain alatt.

## 8. Hivatkozott dokumentumok

- `02_Areas/Deák Húsüzlet/brainstorm/brainstorm_bdos.md` — BDOS aktív állapot-fájl
- `02_Areas/Deák Húsüzlet/CLAUDE.md` — Deák-specifikus konvenciók
- `00_INDEX.md` — vault-gyökér index (Librarian-generált, friss állapot)
