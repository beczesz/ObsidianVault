---
title: 00_GAPS
generated_by: librarian v0.5
generated_at: 2026-05-11T00:00:00
scope: 00_Prompts/
mode: index
id: 80d89f06-6a67-4eeb-9680-346c3a620866
index_schema_version: 1
---

# 00_Prompts — Gaps, Inkonzisztenciák, Árvák

> Librarian által detektált strukturális problémák, duplikátumok, árva fájlok, hiányzó tartalmak.
> Ez a fájl csak jelöl — tényleges akciók tidy vagy deep-clean módban futnak (dry_run: true alapértelmezett).

---

## GAP-01: Duplikált `.plugin` zip fájlok — general-utils

**Típus:** duplikátum gyanú
**Érintett fájlok:**
- `/00_Prompts/general-utils.plugin` (gyökérben, 15.8 KB, 2026-04-23)
- `/00_Prompts/Claude/Plugins/general-utils.plugin` (14.1 KB, 2026-04-14)

**Probléma:** Két `general-utils.plugin` zip fájl él különböző helyeken, eltérő mérettel és dátummal. A gyökérben lévő (15.8 KB, újabb) valószínűleg az aktuális — de explicit döntés kell.

**Javasolt akció:** md5 összehasonlítás (deep-clean módban), a régebbi/kisebb archiválása vagy törlése. Maradjon csak a `Claude/Plugins/`-ban lévő.

**Referencia:** `00_INDEX.md` — Legacy / Utils szekció

---

## GAP-02: Duplikált `.plugin` zip fájlok — speed-reader

**Típus:** duplikátum gyanú
**Érintett fájlok:**
- `/00_Prompts/Claude/Plugins/speed-reader.plugin` (26.3 KB, 2026-02-15)
- `/00_Prompts/Claude/Plugins/speed-reader-plugin.plugin` (26.2 KB, 2026-02-24)

**Probléma:** Két közel azonos méretű speed-reader zip fájl, 9 napnyi különbséggel. Az újabb (`speed-reader-plugin.plugin`) valószínűleg a nevesebb verzió.

**Javasolt akció:** md5 összehasonlítás. Ha különböznek: `speed-reader.plugin` (régebbi) archiválható. Ha azonosak: törölje a régebbit.

---

## GAP-03: Árva `.bak.*` fájlok — navigátor.md

**Típus:** árva backup fájlok
**Érintett fájlok:**
- `Claude/Plugins/Personal Utils Plugin/navigátor.md.bak.1778124276` (2.6 KB, 2026-05-07 06:24)
- `Claude/Plugins/Personal Utils Plugin/navigátor.md.bak.1778124620` (3.6 KB, 2026-05-07 06:30)

**Probléma:** Két automatikusan generált backup fájl (Unix timestamp elnevezéssel) a 2026-05-07-es szerkesztésből. Az aktív `navigátor.md` (2026-05-07 06:30) létezik — a `.bak` fájlok feleslegesek.

**Javasolt akció:** deep-clean módban törlés (> 30 nap szabály még nem teljesül 2026-05-11-én — flag-elés most, törlés 2026-06-07 után).

---

## GAP-04: Duplikált Sonrisa CPS skill zip fájlok

**Típus:** duplikátum gyanú / legacy cleanup
**Érintett fájlok:**
- `Claude/Skills/cps-dashboard-update-v0.1.skill` (8.3 KB, 2026-04-20)
- `Claude/Skills/sonrisa-cps-dashboard-update-v0.1.skill` (8.4 KB, 2026-04-20)

**Probléma:** Két majdnem azonos nevű, azonos dátumú, közel azonos méretű `.skill` zip fájl. Az aktív verzió a `sonrisa-cps-dashboard-update-v1.0/` könyvtár — mindkét v0.1 zip legacy.

**Javasolt akció:** md5 összehasonlítás. Ha tartalmuk azonos: az egyik törölhető. Mindkettő archiválható ha `v1.0` könyvtár a kanonikus.

---

## GAP-05: Legacy Navigator Plugin verziók nem archivált

**Típus:** verziók torlódása
**Érintett fájlok:**
- `Claude/Plugins/navigator-plugin-v0.2/` (könyvtár, 2026-03-15 era)
- `Claude/Plugins/navigator-plugin-v0.2.plugin` (zip, 44.6 KB, 2026-03-15)
- `Claude/Plugins/navigator-podcast.plugin` (zip, 15.1 KB, 2026-02-15 — v0.1 era)

**Probléma:** Három legacy Navigator-tartalom aktív v0.3 mellett. Egyiknek sincs `status: archived` frontmattere (a könyvtár README-jában nincs jelzés).

**Javasolt akció:** Ha nem kell visszafelé kompatibilitás: `04_Archive/`-ba mozgatás (tidy mód).

---

## GAP-06: Hiányzó fájlok — BDOS/capabilities/web-publishing/ placeholder struktúra

**Típus:** hiányzó tartalom (placeholder)
**Érintett helyek:**
- `BDOS/capabilities/web-publishing/methodology.md` — nem létezik (TODO)
- `BDOS/capabilities/web-publishing/infrastructure.md` — nem létezik (TODO)
- `BDOS/capabilities/web-publishing/agents/` — nem létezik (TODO)
- `BDOS/capabilities/web-publishing/teaching/` — nem létezik (TODO)

**Probléma:** A `CLAUDE.md` definiálja a struktúrát de a fájlok/mappák hiányoznak.

**Javasolt akció:** Nem Librarian feladata tartalmát létrehozni — ezt a felhasználó / más agent végzi el. Flag-elve a nyitott munkára.

---

## GAP-07: Hiányzó fájl — BDOS/principles.md

**Típus:** hiányzó tartalom (dokumentált TODO)
**Érintett hely:** `BDOS/principles.md`

**Probléma:** A `BDOS/CLAUDE.md` struktúra-listájában szerepel `principles.md (TODO)` de a fájl nem létezik.

**Javasolt akció:** Felhasználói feladat — BDOS elvek dokumentálása. Librarian csak flag-el.

---

## GAP-08: Hiányzó frontmatter — Utils/Severity Addon.md

**Típus:** konvenció-megsértés
**Érintett fájl:** `Utils/Severity Addon.md`

**Probléma:** Nincs YAML frontmatter (title, date, status, description). Vault konvenció minden fájlnál kötelező.

**Javasolt akció:** tidy mód — frontmatter hozzáadása. Tartalom szerint: `status: active`, `description: System prompt addon — pontossági és precizitási alapelv injekció`.

---

## GAP-09: Verzió-mismatch ellenőrzendő — Librarian canonical vs. registration

**Típus:** szinkron-ellenőrzés szükséges
**Érintett fájlok:**
- `BDOS/agents/librarian.md` — frontmatter: `version: 0.5`
- `.claude/agents/librarian.md` — nem olvasott ebben a futásban (scope: 00_Prompts/ — a `.claude/` a vault gyökerében van)

**Probléma:** A `00_AGENTS_INDEX.md` v0.4-et jelöl aktívnak, a canonical fájl v0.5-öt tartalmaz. Az index kézileg frissítendő.

**Javasolt akció:** audit mód (globális futás) ellenőrzi a verzió-szinkront mindkét fájlban.

---

## GAP-10: 00_AGENTS_INDEX.md verzió mismatch

**Típus:** elavult meta-adat
**Érintett fájl:** `BDOS/00_AGENTS_INDEX.md`

**Probléma:** Az index `Librarian — v0.4`-ként listázza az agentet (`Last updated: 2026-05-11 (v0.4)`), de a canonical `librarian.md` frontmatterje `version: 0.5`-öt mutat a changelog szerint.

**Javasolt akció:** `00_AGENTS_INDEX.md`-ben a Librarian bejegyzés v0.5-re frissítendő, a changelog sort `v0.5 (2026-05-11): PDF olvasás integrate módhoz` hozzáadva.

---

## Librarian akció-log (ez a futás)

| Timestamp | Action | Fájl | Note |
|---|---|---|---|
| 2026-05-11 | WRITE | `00_Prompts/00_INDEX.md` | Új scoped index létrehozva |
| 2026-05-11 | WRITE | `00_Prompts/00_KNOWLEDGE_MAP.md` | Új knowledge map létrehozva |
| 2026-05-11 | WRITE | `00_Prompts/00_DECISIONS_INDEX.md` | Új döntés-index létrehozva |
| 2026-05-11 | WRITE | `00_Prompts/00_OPEN_QUESTIONS.md` | Új nyitott kérdések lista létrehozva |
| 2026-05-11 | WRITE | `00_Prompts/00_GAPS.md` | Ez a fájl — gap-lista létrehozva |
