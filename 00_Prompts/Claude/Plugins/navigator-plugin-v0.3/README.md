# Navigátor Podcast Plugin v0.3 — „Intelligens Motor"

A Navigátor Podcast teljes asszisztense: YouTube metadata generálás, epizód szintézis,
csatorna audit és epizód előkészítés — minden csatorna-intelligenciával alátámasztva.

## Mi újdonság a v0.3-ban?

A korábbi verzió „vakon" generálta a metadatát — az SRT-ből és a brand-kontextusból
dolgozott, de nem tudta, mi működött korábban a csatornán. A v0.3 összeköti a
pre-publish (metadata) és post-publish (szintézis/analytics) világot:

- **52 epizód szintéziséből kinyert csatorna-intelligencia** táplálja az összes commandot
- **ENGINE.md → Skill** átalakulás: a kézi audit-protokoll automatizált skill lett
- **Cross-referencia**: ha a vendég/téma korábban szerepelt, a plugin tudja és használja

## Skillek (3 db)

| Skill | Leírás |
|-------|--------|
| `navigator-context-v0.3` | Brand kontextus + YouTube stratégia + csatorna-intelligencia |
| `episode-prep-v0.3` | Epizód előkészítés (meghívó + kérdések) cross-referenciával |
| `episode-synthesis-v0.3` | Az ENGINE.md skill-változata — szintézis motor |

## Commandok (9 db)

### YouTube metadata (pre-publish)
| Command | Leírás |
|---------|--------|
| `/cim-v0.3` | YouTube címek + hatékonyság-pontszám (csatorna-adatok alapján) |
| `/hook-v0.3` | Cold Open hook-ok + retention-típus + 30mp teszt |
| `/thumbnail-v0.3` | Thumbnail szöveg + mobiloptimalizálás |
| `/leiras-v0.3` | SEO leírás + cross-referencia blokk + hashtagek |
| `/idokod-v0.3` | Időkódok + hook jelölés (★) |

### Szintézis (post-publish)
| Command | Leírás |
|---------|--------|
| `/szintezis-v0.3` | Egyetlen epizód teljes szintézise (SRT → Analytics → Szintézis) |
| `/audit-batch-v0.3` | Batch feldolgozás (N hiányzó epizód szekvenciálisan) |
| `/csatorna-intelligencia-v0.3` | Szintézis-minták visszatáplálása a metadata commandokba |

### Epizód előkészítés
| Command | Leírás |
|---------|--------|
| `/meghivo-v0.3` | Meghívólevél + felkészülési kérdések (cross-referenciával) |

## Használat

```
# Új epizód metadatájának generálása
/cim-v0.3 /path/to/srt
/hook-v0.3 /path/to/srt
/thumbnail-v0.3 /path/to/srt

# Epizód szintézis elkészítése
/szintezis-v0.3 EP45

# Batch audit (következő 3 hiányzó epizód)
/audit-batch-v0.3 3

# Csatorna-intelligencia frissítése (5-10 új szintézis után)
/csatorna-intelligencia-v0.3
```

## Fájlstruktúra

```
navigator-plugin-v0.3/
├── .claude-plugin/plugin.json
├── README.md
├── CHANGELOG.md
├── alkotmany.md
├── commands/
│   ├── cim-v0.3.md
│   ├── hook-v0.3.md
│   ├── thumbnail-v0.3.md
│   ├── leiras-v0.3.md
│   ├── idokod-v0.3.md
│   ├── meghivo-v0.3.md
│   ├── szintezis-v0.3.md
│   ├── audit-batch-v0.3.md
│   └── csatorna-intelligencia-v0.3.md
├── skills/
│   ├── navigator-context-v0.3/
│   │   ├── SKILL.md
│   │   └── references/
│   │       ├── podcast-alkotmany.md
│   │       └── csatorna-intelligencia.md
│   ├── episode-prep-v0.3/
│   │   └── SKILL.md
│   └── episode-synthesis-v0.3/
│       ├── SKILL.md
│       └── references/
│           ├── srt-mapping.md
│           └── quality-criteria.md
└── scripts/
    ├── create_meghivo.js
    ├── create_kerdesek2.js
    ├── create_meghivo_template.js
    └── Navigátor Podcast – Meghívó TEMPLATE.docx
```

## Szerkesztés

- **Brand változás:** `skills/navigator-context-v0.3/SKILL.md` és `references/podcast-alkotmany.md`
- **Csatorna-intelligencia:** `references/csatorna-intelligencia.md` (vagy futtasd a `/csatorna-intelligencia-v0.3` commandot)
- **Szintézis sablon:** `skills/episode-synthesis-v0.3/references/quality-criteria.md`
- **SRT mapping:** `skills/episode-synthesis-v0.3/references/srt-mapping.md`
- **Meghívó template:** `scripts/` mappában a .js és .docx fájlok
