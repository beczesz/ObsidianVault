---
title: 00_KNOWLEDGE_MAP
generated_by: librarian v0.3
generated_at: 2026-05-11T00:00:00
scope: 02_Areas/Szervezet fejlesztés/
mode: index
file_count: 62
id: f1c87c79-5bdf-4787-aa73-b6ba1fd6008a
index_schema_version: 1
---

# 00_KNOWLEDGE_MAP — Domain-térkép

## Központi téma

**Keresztény vezetőfejlesztés és közösség-építés** Erdély/Magyarország régióban, Becze Szabolcs (Exar / Ignis) szervezésében.

## Domain-térkép

### A. Közösség / Ima-szolgálat
- **Unit:** `Vezetők Imája/`
- **Központi fájlok:** `Vezetők Imája.md`, `Statutum.md`, `alkalmak.md`
- **Karakter:** havi rendszeresség, 2021 óta, 48+ alkalom
- **Visszatérő szereplők:** Barni Atya, Ábel Tiszti, Bereczki Orbán Zsolt, Mezei Ödön, Ferkő Andor, Hubi Atya, Pitó Zsolt, Örs (zenész)
- **Adatforrások:** Google Sheet (master), Google Drive (#1–#35 mappa), Obsidian (#41–#47 fájl), Canva (kártyák)

### B. Esemény / Konferencia-szervezés
- **Unit:** `Kingdom At Work/`
- **Központi fájlok:** `program.md`, `memory/projects/kingdom-at-work-event.md`
- **Karakter:** egyszeri esemény, 2026-09-25/26 Budapest
- **Külső kapcsolatok:** KAW csapat (Casey, Manfred — Ausztria), Wieslaw, János Atya
- **Workstream-ek:** program, helyszín, fordítás, keynote-ok, table talks

### C. Képzés / Tananyag
- **Fájlok:** `7 Szokás képzés.md`, `KAW - Vezetői Kézikönyv.md`
- **Karakter:** retrospektív (7 szokás, ~150 fő) + jövőbeli (kézikönyv-koncepció)
- **Kulcs kapcsolat:** Fábri Kornál, Fábián Zsolt, Ács Zoli, Lez, Ferenczy Isti?

### D. Mentor program
- **Unit:** `Mentor program 2026/`
- **Fájl:** `Projektek.md` (idea-list)
- **Karakter:** korai stage, ötletek

## Cross-references

| Honnan | Hová | Reláció |
|--------|------|---------|
| `Vezetők Imája/CLAUDE.md` | Google Drive / Sheet | Külső master adatforrás |
| `Vezetők Imája/alkalmak.md` | `01. ... .md` – `47. ... .md` | Master tábla → részfájlok |
| `Vezetők Imája/Hasznos.md` | Google Drive | Egyetlen link |
| `Kingdom At Work/CLAUDE.md` | `memory/projects/kingdom-at-work-event.md` | Kontextus → részlet |
| `Kingdom At Work/program.md` | KAW PDF-ek | Program → forrás |
| `KAW - Vezetői Kézikönyv.md` | `Vezetők Imája` (csoport) | Hivatkozás |
| Cross-PARA | `01_Projects/Szervezet fejlesztés/Veszprém - Kecskemét körút/` | Magyar út, kapcsolódó vezetői körút |
| Cross-PARA | `01_Projects/Szervezet fejlesztés/Gergely István - Pályázat/` | Üzleti terv pdf |

## Mermaid (vázlat)

```mermaid
graph TD
  A[Szervezet fejlesztés Area] --> B[Vezetők Imája]
  A --> C[Kingdom At Work]
  A --> D[7 Szokás képzés]
  A --> E[KAW Kézikönyv]
  A --> F[Mentor program 2026]
  B --> B1[Statutum]
  B --> B2[alkalmak.md master]
  B2 --> B3[47 alkalom-fájl]
  C --> C1[program.md 2026-09]
  C --> C2[KAW PDF-ek]
  A -.cross-PARA.-> X[01_Projects/Veszprém-Kecskemét]
  A -.cross-PARA.-> Y[01_Projects/Gergely István Pályázat]
```

## Glossary (vault-specifikus)

| Term | Jelentés |
|------|---------|
| Vezetők Imája | Havi keresztény vezetői ima-közösség, 2021 óta |
| Kingdom At Work (KAW) | Budapest konferencia 2026-09 + nemzetközi mozgalom |
| Statutum | A Vezetők Imája alapszabálya |
| Ignis | Becze Szabolcs szervezete (vezetőfejlesztési ág) |
| Exar / ExarLabs | Becze Szabolcs cége |
| Boroinfo, Atalantic, Mikado, Agora Center, OrtoProfil | Visszatérő házigazda-cégek |
