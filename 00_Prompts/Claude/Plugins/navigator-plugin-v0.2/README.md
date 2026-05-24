# Navigator Podcast Plugin v0.2

Teljes körű Navigátor Podcast asszisztens. Két fő funkciót lát el:

1. **YouTube metaadat generálás** — SRT fájlokból készít hookokat, címeket, thumbnail szövegeket, SEO-optimalizált leírást és időkódokat.
2. **Epizód előkészítés** — Meghívóleveleket és felkészülési kérdéseket generál vendégeknek (.docx + .pdf).

---

## Commandok

| Command | Leírás |
|---------|--------|
| `/hook` | Cold Open / Hook javaslatok (5 db, virális pontszámmal) |
| `/cim` | YouTube cím generálás (5 High-CTR cím) |
| `/thumbnail` | Thumbnail szöveg javaslatok (5 db, max 3-4 szó) |
| `/leiras` | YouTube leírás és hashtagek (SEO-optimalizált) |
| `/idokod` | Pontos időkódok / timestamps (10-12 kulcspillanat) |
| `/meghivo` | Epizód előkészítés – meghívó és felkészülési kérdések |

---

## Használat

### YouTube metaadat commandok

Minden metaadat command elfogad egy SRT fájl útvonalat argumentumként:

```
/hook epizod.srt
/cim epizod.srt
/thumbnail epizod.srt
/leiras epizod.srt
/idokod epizod.srt
```

Ha nem adsz meg fájlt, a command megkérdezi.

### Epizód előkészítés

```
/meghivo EP45 "Kovács János"
```

Ha nem adsz meg adatokat, a command végigkérdezi az összes szükséges információt.

---

## Skills

| Neve | Leírás |
|------|--------|
| `navigator-context` | A podcast brand kontextusa és YouTube stratégiája |
| `episode-prep` | Epizód-előkészítési workflow, állandó adatok, script útmutató |

---

## Szerkesztés

**Brand / YouTube stratégia változása esetén:**
Szerkeszd a `skills/navigator-context/SKILL.md` és a `skills/navigator-context/references/podcast-alkotmany.md` fájlokat.

**Meghívó vagy kérdések sablon változása esetén:**
Szerkeszd a `scripts/create_meghivo.js` vagy `scripts/create_kerdesek2.js` fájlokat.

**Állandó adatok (helyszín, Drive ID stb.) változása esetén:**
Szerkeszd a `skills/episode-prep/SKILL.md` és a `commands/meghivo.md` fájlokat.
