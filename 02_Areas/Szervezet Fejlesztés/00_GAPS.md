---
title: 00_GAPS
generated_by: librarian v0.3
generated_at: 2026-05-11T00:00:00
scope: 02_Areas/Szervezet fejlesztés/
mode: index
file_count: 62
id: 379a833a-f347-4108-b1c8-7263a60dad39
index_schema_version: 1
---

# 00_GAPS — Inkonzisztenciák, hiányok, Librarian akciók

## 1. Naming inkonzisztencia (tidy kandidátus)

- **`Szervezet fejlesztés`** — kisbetűs "f", míg a vault konvenció többnyire Title Case. Jelölve **tidy** futásra. Megjelenik mind `02_Areas/`, mind `01_Projects/` alatt — átnevezésnél mindkét helyen szinkronban kell.
- **Vezetők Imája alkalom-fájlok számozási csúszása (Sheet vs Obsidian, #41-től):** `41. Betenbough Könyvek.md` valójában Sheet #42. → 6 fájl átnevezése szükséges (`41. → 42.`, `42. → 43.`, `44. → 44.` stb.). Lásd `Vezetők Imája/CLAUDE.md` 108–127. sor. Tidy-ban **NEM** automatizálható (semantic döntés szükséges), Szabolcs hagyja jóvá.

## 2. Hiányzó fájlok / üres állapotú fájlok

| Fájl | Hiány | Forrás |
|------|-------|--------|
| Sheet #41 OrtoProfil/Buzogány Ágnes (2025-06-02) Obsidian-fájl | Teljesen hiányzik | `Vezetők Imája/CLAUDE.md` 162 |
| `45. Atalantic.md` | Üres / hiányos | `Vezetők Imája/CLAUDE.md` 118 |
| `23. Ismeretlen alkalom.md` | Üres | `Vezetők Imája/alkalmak.md` 41 |
| `28., 29., 30., 33., 36. Ismeretlen alkalom.md` | Csak placeholder, adatok nincsenek | folder listázás |

## 3. Frontmatter hiányok / inkonzisztenciák

- `42. Mikado - Rendcsinálás.md`: `date:` üres
- `30., 33. Ismeretlen alkalom.md`: `date: ""` (üres string)
- Az **area root** két md-jén (`KAW - Vezetői Kézikönyv.md`, `7 Szokás képzés.md`) csak `significance:` van, de nincs `type`, `status`, `created` mező.
- `Mentor program 2026/Projektek.md` — semmilyen frontmatter
- `Vezetők Imája/Hasznos.md` — csak egy link, frontmatter nincs
- `Kingdom At Work/TASKS.md` és `Kingdom At Work/program.md` — frontmatter nélkül

## 4. Cross-PARA referencia (scope-on kívül, de releváns)

`01_Projects/Szervezet fejlesztés/` tartalom (nem indexeltük itt, csak megjelölés):
- `Gergely István - Pályázat/Anexa 6 - Plan de afaceri.pdf` (üzleti terv, román)
- `Veszprém - Kecskemét körút/Kecskemét előadás 2025.09.26.md`
- `Veszprém - Kecskemét körút/Utiterv.md`
- `Veszprém - Kecskemét körút/25_ERME_ELVONULAS_prog_reg.pdf`

Kapcsolódás: vezetőfejlesztési körút + pályázat-támogatás a területhez, projekt-PARA bucket-ben, így onnan releváns.

## 5. Lehetséges duplikációk / téma-átfedés

- `KAW - Vezetői Kézikönyv.md` (area root) vs `Kingdom At Work/` unit — két különböző workstream (könyv vs konferencia), de a "KAW" prefix összemoshatja. Megfontolandó: prefix-egyértelműsítés vagy egy `book/` almappa.
- `Kingdom At Work/CLAUDE.md` (rövid memória) + `Kingdom At Work/memory/projects/kingdom-at-work-event.md` (részletes) — kicsi duplikáció (Casey, Manfred, Hungarian preferred). Nem byte-azonos, tidy nem javítja.
- `Kingdom At Work/memory/glossary.md` — csak 1 sort tartalmaz (Kingdom At Work definíció). Stub.

## 6. Stub-szerű / minimal fájlok

- `Kingdom At Work/TASKS.md` (9 sor, 1 In Progress)
- `Kingdom At Work/memory/glossary.md` (1 term)
- `Vezetők Imája/Hasznos.md` (1 link)
- `Mentor program 2026/Projektek.md` (6 sor)

## 7. PDF assets (nem md, csak listázva)

- `Kingdom At Work/KAWActionGroupsWorkbook-compressed.pdf`
- `Kingdom At Work/KAW_Program.pdf`

## 8. Broken / külső linkek

- Több Google Drive / Sheet / Canva / Doc link a `Vezetők Imája/CLAUDE.md`-ben és `alkalmak.md`-ben — működés nem ellenőrizve (out of scope).

## 9. Librarian akciók logja

| Időpont | Mód | Akció |
|---------|-----|-------|
| 2026-05-11 | index | 5 tier-2 index fájl létrehozása scope gyökerében (`00_INDEX.md`, `00_KNOWLEDGE_MAP.md`, `00_DECISIONS_INDEX.md`, `00_OPEN_QUESTIONS.md`, `00_GAPS.md`) |

## 10. Javaslatok következő librarian-futásra

- **`tidy` dry-run** az area-n: árva fájlok ellenőrzése, broken md-link szkennelés (különösen `alkalmak.md` táblában a `42. Mikado` stb. wikilink-ek).
- **`audit`** futás `focus: frontmatter` — alkalom-fájlok frontmatter-normalizálása.
- A számozási csúszás (#41+) — Szabolcs döntése után dedikált rename batch (kézi vagy célzott tidy).
