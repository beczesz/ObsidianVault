---
title: "deak-design Plugin"
date: 2026-04-18
author: Becze Szabolcs
status: active
description: "Technical reference for the Deák Húsmíves design system plugin, documenting wireframe generation skills, UI components, color tokens, and screen audit notes. Essential resource for wireframe creators requiring current design standards and component specifications."
description_source: auto
description_hash: 35a253ff906f992c
id: a979bf7e-b019-4125-9478-c274c667dfb9
index_schema_version: 1
bdos_index: true
---
# deak-design Plugin

```yaml
name: deak-design
version: 0.1.2
description: >
  Deák Húsmíves design system plugin — wireframe generálási skill és
  vizuális nyelv dokumentáció. Minden wireframe-hez kötelező betölteni.
skills:
  - wireframe-v0.1
context_files:
  - context/design-system.md   # design tokenek, komponensek
  - context/ui-strings.md      # UI szövegek, label-ek
  - context/ui-audit.md        # screen-level audit notes
changelog:
  - version: "0.1.3"
    date: "2026-04-18"
    changes:
      - "design-system.md: 12+1 Profil screen komponens (ProfileHero, MenuGroup, MenuRow, DocRow, CompanyCard, LangSeg, TocList, ExtRow, AppVersion)"
      - "design-system.md: 10 Savings Engine komponens (Nudge variánsok, BundleCard, EtaCard, Toast, ReturnBanner, Modal, UnavailableItem, LoadedMsg)"
      - "design-system.md: Wireframe CSS token referencia (szekció 12)"
  - version: "0.1.2"
    date: "2026-04-18"
    changes:
      - "design-system.md frissítve: Kosár screen audit (CartItemCard, SavingsProgressBar, InfoNotice, CartCTA, AvailabilityBadge)"
      - "secondary szín korrekció: #96724A → #D4A574"
      - "QuantitySelector: cart variáns (INPUT elem) dokumentálva"
      - "Navigáció: 3-tab (guest) vs 4-tab (logged in) tisztázva"
      - "Auditált screen-ek tábla hozzáadva (10. szekció)"
  - version: "0.1.0"
    date: "2026-04-17"
    changes:
      - "Első verzió — wireframe skill + design context"
```

## Verziókezelési szabályok

| Változás típusa | Bumpolás |
|-----------------|---------|
| context/ fájl frissítés | PATCH (0.1.0 → 0.1.1) |
| skill minor frissítés | MINOR (0.1.x → 0.2.0) |
| új skill hozzáadása | MINOR |
| breaking változás | MAJOR (0.x.y → 1.0.0) |

## Használat

Minden wireframe session elején:
1. Olvasd be: `plugins/deak-design/skills/wireframe-v0.1/SKILL.md`
2. Ez automatikusan hivatkozik a context fájlokra
3. SOHA ne kezdj wireframe-t a SKILL.md elolvasása nélkül
