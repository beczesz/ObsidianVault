---
title: 00_GAPS (Archive)
generated_by: librarian v0.3
generated_at: 2026-05-11
scope: /04_Archive/
mode: index
file_count: 32
---

# Gaps & Anomalies — Archive

Inkonzisztenciák, gyanúsan ottmaradt aktív anyagok, hiányzó metaadat, duplikáció-gyanúk. Read-only észrevételek — tidy mód külön hívásban tud rajtuk dolgozni.

---

## 1. Lehetséges duplikáció / verzió-zaj

### EPRIVO.md kétszer szerepel
- `01_Projects/Sonrisa/CPS/EPRIVO.md` (2025-12-08, tartalom: 1 sor — done Santosh meeting)
- `01_Projects/Sonrisa/CPS/Projects/EPRIVO.md` (2025-09-03, tartalom: ugyanaz az 1 sor + üres checkbox)
- **Gyanú:** byte-azonos vagy közel-azonos. Tidy módban md5-összehasonlítás javasolt.
- **Akció:** ha azonos → root változat törlése (Projects/ alatti a kanonikus hely).

### BMC verziók
- `business-model-canvas-v1.0.md` (2026-03-27)
- `business-model-canvas-v2.0.md` (2026-03-28)
- **Nem hiba**, történeti precedens-érték miatt mindkettő indokolt. De: érdemes lenne frontmatter `supersedes:` mezővel összekötni őket.

### Dev roadmap verziók
- `dev-roadmap.md` (v1.1, 2026-03-05)
- `dev-roadmap-v1.2.md` (2026-03-25)
- **Naming inkonzisztencia**: v1.1 fájl `v1.1` SUFFIX NÉLKÜL, v1.2 fájl `v1.2` suffixszel. Tidy módban érdemes egységesíteni (pl. mindkettő explicit verzió-suffixszal).

---

## 2. Hiányzó frontmatter

A 32 fájlból csak **9** rendelkezik YAML frontmatterrel (DHOP pilot 7 + Think Engine 2). A többi 23 fájl frontmatter nélkül:
- Minden Navigátor Podcast / Digitális Székelyföld fájl (11)
- Minden Sonrisa CPS fájl (5, projects + team)
- Szervezet fejlesztés körút (2)
- Pályázat (2)
- ExarLabs Jegyzetek
- Személyes Osztálytalálkozó

**Hatás:** retrieve módban a frontmatter-szűrés (status, date, version) nem alkalmazható ezekre. Archív kontextusban ez **nem kritikus** (passzív anyag), csak észrevétel.

---

## 3. Naming anomáliák

### "2." prefix kollízió a podcast vendég-fájlokban
- `Podcast/2. Dr. Charaf Hassan.md`
- `Podcast/2. Süket Csaba.md`
- Két különböző fájl ugyanazzal a sorszámmal. Ha sorrend-jelentésű, az egyiknek nem 2-nek kellene lennie. Történeti kontextusban (archív) nem kell javítani, de jelezve.

### Tördelt, hosszú útvonalak
- `01_Projects/Szervezet fejlesztés/Veszprém - Kecskemét körút/...` — több szóköz, ékezet, kötőjel. Bash-szintaxisban folyamatos quoting-problémát okoz, de Obsidian-szinten korrekt.

---

## 4. Lehetséges "élő" anyag az archívumban (misplaced)

### `02_Areas/Személyes/20 Éves Osztálytalálkozó.md` (mtime 2026-05-07)
- **Mai dátum:** 2026-05-11. A fájl csak 4 napja módosult.
- **Gyanú:** lehet, hogy ez egy aktív személyes reflexió, ami véletlenül a 04_Archive-ban landolt, vagy a 02_Areas/Személyes/ alatti élő fájlt tükrözi az archive-fa.
- **Javaslat:** felhasználói review — szándékos archiválás vagy elhelyezési hiba?

### Pályázat fájlok
- `2025.10.16 RegioConsult meeting.md` és `2025.11.28 Contestare - meeting v1.1.md` — ha a pályázati ciklus / contestare még aktív (2026 májusig még futhat a TRL 3 elbírálás), akkor ezek nem archív hanem aktív anyagok.
- **Javaslat:** felhasználói review a pályázat státuszáról.

### `02_Areas/ExarLabs/Jegyzetek.md` (2026-02-17)
- "2025 retrospektív" jellegű, de a 2026-os stratégiai kontextus része. Lehet, hogy aktív reference doc.
- **Javaslat:** mérlegelni az áthelyezést élő 02_Areas/ExarLabs/ alá.

### `02_Areas/Deák Húsüzlet/think engine/` (2026-03-31, 2 fájl)
- A Think Engine OS v0.3 és Project Engine v0.2 **kanonikus design dokumentumok**. A `general-utils:project-engine` skill és a multi-AI orchestrator skill aktívan használja a koncepciókat.
- **Gyanú:** ezek nem archívak, hanem aktív canonical specek. Lehet, hogy a "Deák Húsüzlet" név miatt kerültek ide, de mára cross-cutting concern.
- **Javaslat:** áthelyezés `00_Prompts/` vagy `02_Areas/_shared/think-engine/` alá.

### DHOP pilot 7 fájl
- Frontmatter dates: 2026-03-05 — 2026-03-28. **DH aktív munka** zajlik (current branch `claude/musing-cori-3f0e65`, memory utal "DH wireframe craft conventions"-re).
- **Gyanú:** ez a doku-csomag valószínűleg az aktív DH platform fejlesztés precedens-readme-je, nem igazi archív.
- **Javaslat:** felhasználói review — szándékos archív "snapshot" vagy active reference?

---

## 5. Hiányzó archive-metaadat (rendszerszintű)

**Egyetlen** fájl sem tartalmaz `archived_at:` vagy `archive_reason:` frontmatter mezőt. Mtime az egyetlen proxy.
- **Javaslat (jövőbeli tidy szabály):** archiválás során automatikusan `archived_at: <ISO date>` + `archive_reason: <string>` mező hozzáadása.

---

## 6. Librarian akció-log (ez a futás)

| time | action | file | reason |
|---|---|---|---|
| 2026-05-11 | created | `00_INDEX.md` | Archive scoped index v0.3 first run |
| 2026-05-11 | created | `00_KNOWLEDGE_MAP.md` | Domain térkép + live cross-refs |
| 2026-05-11 | created | `00_DECISIONS_INDEX.md` | Történeti döntés-precedensek |
| 2026-05-11 | created | `00_OPEN_QUESTIONS.md` | Archiválás-kori nyitott kérdések |
| 2026-05-11 | created | `00_GAPS.md` | Ez a fájl |

Semmilyen fájl **nem** lett módosítva, mozgatva, törölve. Tisztán read-only index futás.
