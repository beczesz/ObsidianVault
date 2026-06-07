---
schema: forge.practice-learnings.area.v1
generated_at: null
practice_area: "exarlabs-microsites"
counts:
  active: 0
  proposed: 0
  retired: 0
description: Forge structured learnings élő indexe az ExarLabs Microsites practice area-hoz. Per-area tanulságok (NEM cross-area meta — az `agents/forge/practice-learnings/` mappában él). Tanulságok ahogy a practice area érlelődik: design patterns, AI-plugin combo recipes, deploy gotchas, performance trade-offs.
id: 3e8b6c14-9a25-4d78-bf02-7c1a5e9d4f63
index_schema_version: 1
bdos_index: false
---

# Microsites — Structured Learnings Index

Per-area tanulságok. **Forge `learn` mód karbantartja.** Lifecycle: `proposed → active → retired`.

## Active (0)
*Üres — practice area most jött létre (2026-05-27 bootstrap), nincsenek confirmed learnings.*

## Proposed (0)
## Retired (0)

---

## Cap

- Max **15 active learning**, max **2000 token** preamble
- Sorrend: `confidence DESC, last_applied_at DESC`

## Tanulság-típus jelölt-vocabulary

Microsites-specifikus tanulság-típusok (v0.2-ben Forge `learn` mód véglegesíti). Induló jelöltek:

| Típus | Mit rögzít |
|---|---|
| `archetype-pattern` | microsite-archetypes (landing / one-pager / event / brand intro), milyen layout/structure illik melyikhez |
| `plugin-combo-recipe` | mely AI-plugin kombináció ad jó eredményt mely deliverable-típusra |
| `design-token-pattern` | reusable design token recipek (warm-neutral, monochrome, vibrant, etc.) |
| `content-prompt-pattern` | content-first prompting receptek brand spine + StoryBrand + JTBD integrálásával |
| `performance-recipe` | Core Web Vitals tuning patterns |
| `deploy-quirk` | Cloudflare Pages / Netlify / Vercel specifikus gotcha-k |
| `accessibility-default` | WCAG AA achievement patterns default-tal |
| `tier-pricing-anchor` | Lean / Standard / Premium tier konkrét deliverable-scope és árazás-referencia |

(Ezek a jelöltek — Forge `learn` mód a végén v0.2-ben pinneli a stable type-vocabularyt.)
