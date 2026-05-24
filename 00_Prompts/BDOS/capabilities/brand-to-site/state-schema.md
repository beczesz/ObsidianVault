---
title: brand-spine-state.md — séma
version: 0.1
date: 2026-05-14
author: Becze Szabolcs
status: active
description: A Maestro agent által olvasott és írt per-projekt state-fájl kanonikus formátuma. Minden Brand Spine projekt (DH, Sonrisa, Ignis, stb.) egy `brand-spine-state.md` fájllal rendelkezik az Area gyökerében. Ez a single source of truth a projekt haladásáról.
id: 64300f69-a141-41f4-aded-f86c0cfe9eb6
index_schema_version: 1
---

# brand-spine-state.md — séma

> A Maestro **olvas és ír** ezen a fájlon. Minden Brand Spine projekt egyetlen ilyet birtokol. Hely: `<project-area>/brand-spine-state.md`.

## Helyzet a vault-ban

```
02_Areas/Deák Húsüzlet/brand-spine-state.md       ← DH state
02_Areas/Sonrisa/brand-spine-state.md             ← Sonrisa state
02_Areas/Ignis Academy/brand-spine-state.md       ← Ignis state
... stb.
```

## Teljes séma — YAML frontmatter

```yaml
---
# === Projekt identitás ===
project: <Project Name>                # ember-olvasható név, pl. "Deák Húsüzlet"
project_slug: <slug>                   # snake_case azonosító, pl. "deak-husuzlet"

# === Tier & status ===
tier: lean | standard | premium        # méret-tier (lásd recipes/)
status: planning | in_progress | paused | shipped | iterating
started: <ISO date>                    # YYYY-MM-DD
last_updated: <ISO timestamp>          # YYYY-MM-DDTHH:MM (a Maestro frissíti minden írásnál)

# === Haladás ===
overall_progress: <0-100>              # %, auto-számolt a rétegek progress-ei alapján
current_layer: <1-9>                   # éppen aktív réteg száma (vagy "pulse" ha iterating)

# === Tulajdonjog ===
maestro_owner: true                    # jelzi, hogy a Maestro frissítheti

# === Anti-references — divergencia-védelem (lásd Brand Spine v0.3 capability) ===
anti_references:
  vault_projects:                      # más aktív projektek a vault-ban
    - DH (warm brick + cream + serif — már foglalt)
    - Sonrisa CPS (TBD)
  category_first_reflex: ""             # mi az első kategória-reflex amit el kell kerülni
  category_second_reflex: ""            # mi a második (mélyebb) reflex
  forbidden_palettes: []                # konkrét tilalmas színkombinációk
  physical_world_references: []         # fizikai-világ referencia-fotók path-jai
  artistic_constraints: []              # szándékos korlátok (pl. "csak monospace")
---
```

## Body — réteg-szekciók

A frontmatter után minden rétegnek külön szekció, egységes mini-séma:

```markdown
## Layers

### 1. Brand Core
- **status:** not_started | in_progress | complete | needs_revision
- **progress:** <0-100>%
- **artifact:** <relative path az output fájlhoz, vagy "—" ha nincs még>
- **tool_used:** <tool · skill> | "—"
- **last_touched:** <ISO timestamp> | "—"
- **next_action:** <egy mondat, mi a következő ezen a rétegen>
- **blockers:** [] | [<lista a fennakadásokról>]
- **decisions:**
  - <ISO date>: <döntés rövid leírása>

### 2. Market & Audience Reality
- ... (ugyanaz a séma)

### 3. Positioning & Offer
- ...

### 4. Messaging & Proof Architecture
- ...

### 5. Narrative UX + IA
- ...

### 6. Creative Direction → Design System
- ...

### 7. Build + Polish + Quality Gate
- ...

### ↻ Pulse (loop, csak shipping után)
- **status:** not_applicable_yet | active | paused
- **progress:** N/A
- **active_experiments:** []
- **insights_fed_back_to:** [layer 2, 4]
```

## Body — egyéb szekciók

```markdown
## Iteration history (append-only)
A Maestro minden írásnál ide tesz egy sort. Sose töröld a régieket.

- 2026-05-13 18:00 — INIT (Lean tier, Maestro v0.1)
- 2026-05-13 18:30 — Layer 1 (Brand Core) → complete, artifact: ./brand-brief.md
- 2026-05-13 22:00 — Layer 2 (Audience) → complete
- 2026-05-14 09:15 — Layer 3 (Positioning + Offer) → complete
- 2026-05-14 11:30 — Layer 5 started (Lean összevonta L3+L4), paused at 40%

## Tool readiness (snapshot)
Frissül `next` és `status` módban — gyors emlékeztető a recommend-elt toolok telepítettségéről.

| Tool | Telepítve | Megjegyzés |
|------|-----------|------------|
| brand-toolkit | ❌ | Layer 1-4 default — telepítendő |
| impeccable | ✅ | Layer 5, 7 default |
| ui-ux-pro-max | ✅ | Layer 6 katalógus |
| marketingskills | ❌ | Layer 7, Pulse — Lean tier opcionális |

## Open questions
Maestro nem oldja meg ezeket — csak felsorolja, hogy a user lássa.

- [ ] /pricing vagy /products legyen az URL?
- [ ] Final brand-név (Brand Spine working)?

## Notes
Free-form szekció — a user is írhat ide, a Maestro is.

- Megfigyelés: a Lean tier-ben a L3 és L4 természetesen összeolvad ennél a projektnél.
```

## Minimum kötelező mezők (a Maestro elvárja)

- frontmatter: `project`, `tier`, `status`, `current_layer`, `overall_progress`
- Body: `## Layers` szekció minden rétegre (a tier szerint — Lean=5, Standard=7, Premium=9)
- Body: `## Iteration history` szekció (akár üresen induljon)

## Auto-számolási szabály

`overall_progress` = `Σ(layer_progress) / N` ahol N a tier rétegszáma.

- Lean: N = 5
- Standard: N = 7
- Premium: N = 9

(Pulse loop NEM számít a százalékba — az iterációs réteg, post-ship.)

## Kapcsolódó

- Maestro agent: [`../../agents/maestro.md`](../../agents/maestro.md)
- Tier-receptek: [`recipes/`](recipes/)
- Layer-templates: [`templates/`](templates/)
- Initial state template: [`templates/brand-spine-state.md.template`](templates/brand-spine-state.md.template)
