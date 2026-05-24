---
title: 00_OPEN_QUESTIONS
generated_by: librarian v0.5
generated_at: 2026-05-11T00:00:00
scope: 00_Prompts/
mode: index
id: 57676396-7169-4414-bebf-6859b80769fd
index_schema_version: 1
---

# 00_Prompts — Nyitott Kérdések

> Nyitott kérdések, TODO-k és döntetlen pontok domain szerint.
> Forrás: `[ ]` checkbox-ok és explicit kérdőmondatok a fájlokban.

---

## BDOS — Rendszer-szintű

| # | Kérdés / TODO | Prioritás | Forrás |
|---|---|---|---|
| B-01 | **principles.md létrehozva?** — `BDOS/CLAUDE.md` struktúra-diagramjában szerepel `principles.md (TODO)`, de a fájl nem létezik | közepes | `BDOS/CLAUDE.md` — Struktúra szekció |
| B-02 | **Mikor élesednek a tervezett agentek?** — Product Strategist, Operations Steward, Exploration Agent, Validator mind tervezett; küszöb: 3+ worker egy domain alatt | alacsony | `BDOS/CLAUDE.md` — Aktív agentek tábla |
| B-03 | **Agent meta-index karbantartása** — `00_AGENTS_INDEX.md` jelenleg human-manual; audit mód fogja frissíteni (v0.2 óta definiált, de a jelenlegi meta-adat szerint még manual) | közepes | `BDOS/00_AGENTS_INDEX.md` — generated_by mező |

---

## Microsite Factory — Capability design

| # | Kérdés / TODO | Prioritás | Forrás |
|---|---|---|---|
| M-01 | **Cloudflare vs Netlify végleges választás?** — Kettős stratégia tervezett, de döntés szükséges | magas (blocking) | `BDOS/capabilities/web-publishing/CLAUDE.md` — Open questions |
| M-02 | **Hány agent szükséges?** — Deploy + Domain összevonható? Melyik lesz valódi BDOS-agent vs. skill/inline workflow? | magas | `BDOS/capabilities/web-publishing/CLAUDE.md` — Open questions |
| M-03 | **Repo-struktúra döntés** — monorepo (egy repo, sok site) vs. per-kliens repo? | közepes | `BDOS/capabilities/web-publishing/CLAUDE.md` — Open questions |
| M-04 | **Token-stratégia** — account-level vagy per-kliens tokenek? | közepes | `BDOS/capabilities/web-publishing/CLAUDE.md` — Open questions |
| M-05 | **Ignis Academy tananyag-export** — mikor és milyen formátumban? | alacsony | `BDOS/capabilities/web-publishing/CLAUDE.md` — Open questions |
| M-06 | **methodology.md** meg kell írni | közepes | `BDOS/capabilities/web-publishing/CLAUDE.md` — Struktúra (placeholder) |
| M-07 | **infrastructure.md** meg kell írni (Cloudflare/Netlify, tokenek, repo-konvenciók) | közepes | `BDOS/capabilities/web-publishing/CLAUDE.md` — Struktúra (placeholder) |
| M-08 | **agents/ alkönyvtár** a web-publishing alatt — empty, de a tervezett agentek (Deploy, Domain, Polish, SEO) be kell tölteni | alacsony | `BDOS/capabilities/web-publishing/CLAUDE.md` — Tervezett agentek |
| M-09 | **teaching/ alkönyvtár** a web-publishing alatt — Ignis Academy export placeholder, üres | alacsony | `BDOS/capabilities/web-publishing/CLAUDE.md` — Struktúra |

---

## Navigator Plugin

| # | Kérdés / TODO | Prioritás | Forrás |
|---|---|---|---|
| N-01 | **navigator-plugin-v0.2 törölhető?** — Legacy, v0.3 aktív; de explicit döntés kell archiváláshoz | alacsony | `Claude/Plugins/navigator-plugin-v0.2/` — nincs deprecation jelzés |
| N-02 | **navigator-podcast.plugin (v0.1) törölhető?** — 2026-02-15-ös legacy zip, v0.3 aktív | alacsony | `Claude/Plugins/navigator-podcast.plugin` |

---

## Sonrisa Plugin / Skills

| # | Kérdés / TODO | Prioritás | Forrás |
|---|---|---|---|
| So-01 | **cps-dashboard-update-v0.1.skill vs sonrisa-cps-dashboard-update-v0.1.skill** — Két szinte azonos nevű legacy zip fájl; azonosak-e? Mindkettő törölhető ha v1.0 könyvtár aktív | közepes | `Claude/Skills/` — két .skill fájl |

---

## Librarian backlog (definiált, de nem implementált)

| # | Jövőbeli képesség | Forrás |
|---|---|---|
| L-01 | Incremental refresh index módban (csak változott fájlok) | `BDOS/agents/librarian.md` §9 Backlog |
| L-02 | Frontmatter normalize (audit vagy tidy almód) | `BDOS/agents/librarian.md` §9 Backlog |
| L-03 | Broken link auto-fix (jelenleg csak flag-el) | `BDOS/agents/librarian.md` §9 Backlog |
| L-04 | Tag taxonomy + normalizálás | `BDOS/agents/librarian.md` §9 Backlog |
| L-05 | Cross-reference graph Mermaid-ben | `BDOS/agents/librarian.md` §9 Backlog |
| L-06 | Semantic retrieve (embeddings) | `BDOS/agents/librarian.md` §9 Backlog |
| L-07 | Multilingual aware (HU/EN kezelés) | `BDOS/agents/librarian.md` §9 Backlog |

---

## Utils / Egyéb

| # | Kérdés / TODO | Prioritás | Forrás |
|---|---|---|---|
| U-01 | **Severity Addon státusza** — nincs frontmatter, nincs verzió, nincs dátum; mi a jelenleg aktív felhasználása? | közepes | `Utils/Severity Addon.md` |
