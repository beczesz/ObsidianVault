---
title: 00_DEEPCLEAN_LOG
generated_at: 2026-06-07
mode: deep-clean
dry_run: true
stale_days: 180
scope: global
generated_by: librarian v0.8.3
description: DRY-RUN nagytakarítás log. 3623 fájl szkennelve. Byte-azonos duplikátumok, üres fájlok, temp fájlok, stale flag-ek azonosítva. Semmilyen tényleges akció nem hajtódott végre.
id: 2d09c97a-f5a4-4835-9f3a-eecb35de3921
index_schema_version: 1
---

# Vault Deep-Clean Log — 2026-06-07 (DRY-RUN)

> Semmi nem lett törölve vagy mozgatva. Ez csak egy terv.
> Végrehajtáshoz: futtasd újra `dry_run: false` paraméterrel, minden szekciót explicit jóváhagyással.

---

## Summary

| Akció típus | Tervezett db | Becsült méret |
|---|---|---|
| Byte-azonos duplikátum törlés | 27 | ~3.6 MB |
| Üres fájl törlés | 14 | - |
| Temp fájl törlés | 12 | ~967 KB |
| Frontmatter-alapú archiválás | 0 | - |
| Stale flag (nem törlés) | 22 | - |
| Üres mappa törlés | 44 | - |
| **TOTAL** | **119** | **~4.6 MB** |

**Megjegyzés a nagy kizárásokról:**
- `02_Areas/ExarLabs/resources/ExarSharedBrain/` (163 MB) — önálló git repo (`ExarLabs/ExarSharedBrain`), tartalmaz sok vault-tükrözött fájlt. Kezelése git szinten szükséges, nem vault-szintű törlés.
- `02_Areas/ExarLabs/Practices/microsite-factory/node_modules/` (414 MB) — node_modules, gitignore-ba kellene. Nem érintett.
- `.trash/` (96 KB) — Obsidian trash, kihagyva (rendszer kezeli).

---

## Akciók

### TÖRLÉS JAVASOLT — Byte-azonos duplikátumok

#### DailyNotes — Másolat-fájlok (Obsidian szinkron-artifact, " (1)" suffix)

| Fájl (törlendő) | Megtartandó | md5 | Hivatkozás? | Visszacsinálás |
|---|---|---|---|---|
| `05_DailyNotes/2025/December/2025-12-10 (1).md` | `05_DailyNotes/2025/December/2025-12-10.md` | e59a3d8c | nem | `cp 2025-12-10.md "2025-12-10 (1).md"` |
| `05_DailyNotes/2025/December/2025-12-11 (1).md` | `05_DailyNotes/2025/December/2025-12-11.md` | 485c371f | nem | `cp 2025-12-11.md "2025-12-11 (1).md"` |
| `05_DailyNotes/2025/December/2025-12-12 (1).md` | `05_DailyNotes/2025/December/2025-12-12.md` | 4380fe25 | nem | `cp 2025-12-12.md "2025-12-12 (1).md"` |
| `05_DailyNotes/2025/December/2025-12-14 (1).md` | `05_DailyNotes/2025/December/2025-12-14.md` | f438a5df | nem | `cp 2025-12-14.md "2025-12-14 (1).md"` |
| `05_DailyNotes/2025/December/2025-12-15 (1).md` | `05_DailyNotes/2025/December/2025-12-15.md` | 288874d7 | nem | `cp 2025-12-15.md "2025-12-15 (1).md"` |
| `05_DailyNotes/2025/December/2025-12-18 (1).md` | `05_DailyNotes/2025/December/2025-12-18.md` | 795774f3 | nem | `cp 2025-12-18.md "2025-12-18 (1).md"` |
| `05_DailyNotes/2025/December/2025-12-19 (1).md` | `05_DailyNotes/2025/December/2025-12-19.md` | e25eda8e | nem | `cp 2025-12-19.md "2025-12-19 (1).md"` |
| `05_DailyNotes/2025/December/2025-12-22 (1).md` | `05_DailyNotes/2025/December/2025-12-22.md` | 060bb63b | nem | `cp 2025-12-22.md "2025-12-22 (1).md"` |
| `05_DailyNotes/2026/February/2026-02-15 (1).md` | `05_DailyNotes/2026/February/2026-02-15.md` | bd768bf2 | nem | `cp 2026-02-15.md "2026-02-15 (1).md"` |
| `05_DailyNotes/2026/February/2026-02-16 (1).md` | `05_DailyNotes/2026/February/2026-02-16.md` | 7fbf115b | nem | `cp 2026-02-16.md "2026-02-16 (1).md"` |

**Megjegyzés:** A `" (1)"` suffix Obsidian szinkron-ütközés artifact. Mind a 10 fájl byte-azonos az eredeti párjával. Nincs rájuk hivatkozás.

#### DailyNotes — Byte-azonos March páros (különböző dátum, azonos tartalom)

| Fájl (törlendő) | Megtartandó | md5 | Hivatkozás? | Visszacsinálás |
|---|---|---|---|---|
| `05_DailyNotes/2026/March/2026-03-15.md` | `05_DailyNotes/2026/March/2026-03-29.md` | be5c56ca | nem (csak frontmatter dátum-hivatkozás máshol) | `cp 2026-03-29.md 2026-03-15.md` |

> **Figyelem:** Ez a pár azonos tartalmú, de különböző dátumú napi note. Valószínűleg copy-paste artifact. A törlés javasolt, de a megtartandó fájl kiválasztása felhasználói döntés (mindkettő tartalom-üres napi rutin, azonos template).

#### `general-utils.plugin` duplikátum

| Fájl (törlendő) | Megtartandó | md5 | Hivatkozás? | Méret | Visszacsinálás |
|---|---|---|---|---|---|
| `02_Areas/Deák Húsüzlet/BIN/general-utils.plugin` | `00_Prompts/general-utils.plugin` | a628a699 | nem (BIN-re nem hivatkoznak) | 15.5 KB | `cp 00_Prompts/general-utils.plugin "02_Areas/Deák Húsüzlet/BIN/general-utils.plugin"` |

#### `BUSINESS_PLAN.md` duplikátum

| Fájl (törlendő) | Megtartandó | md5 | Hivatkozás? | Méret | Visszacsinálás |
|---|---|---|---|---|---|
| `00_Prompts/BDOS/capabilities/BUSINESS_PLAN.md` | `02_Areas/ExarLabs/BUSINESS_PLAN.md` | 5ff440ed | nincs hivatkozás a capabilities verzióra | 7.5 KB | `cp 02_Areas/ExarLabs/BUSINESS_PLAN.md 00_Prompts/BDOS/capabilities/BUSINESS_PLAN.md` |

> **Megjegyzés:** A capabilities/ példány nem hivatkozott sehonnan. Az ExarLabs/ példányra az `02_Areas/ExarLabs/Stratégia/Microsite Factory/` több dokumentuma hivatkozik.

#### `Ghidul-solicitantului-–-consultare-publica-1.pdf` duplikátum

| Fájl (törlendő) | Megtartandó | md5 | Hivatkozás? | Méret | Visszacsinálás |
|---|---|---|---|---|---|
| `01_Projects/Palyazat/Ghidul-solicitantului-–-consultare-publica-1.pdf` | `02_Areas/Személyes/admin/roman-admin/Ghidul-solicitantului-–-consultare-publica-1.pdf` | eb03a1f2 | igen (00_INTEGRATE_PROPOSALS.md a román-admin útvonalra mutat) | 2.5 MB | `cp "02_Areas/Személyes/admin/roman-admin/Ghidul-solicitantului-–-consultare-publica-1.pdf" "01_Projects/Palyazat/Ghidul-solicitantului-–-consultare-publica-1.pdf"` |

> **Megjegyzés:** A `01_Projects/Palyazat/` mappa nem más jelölt fájlt tartalmaz — ellenőrizd, hogy az egész Palyazat mappa archiválható-e a PDF törlése előtt.

#### `dashboard.html` tömeg-duplikátum (scatter copies)

| Fájl (törlendő) | Megtartandó | md5 | Hivatkozás? | Méret |
|---|---|---|---|---|
| `02_Areas/Média Műhely/dashboard.html` | `_dashboards/index.html` (vagy megfelelő dashboard) | 631423b4 | nem | 97 KB |
| `02_Areas/ExarLabs/dashboard.html` | (mint fent) | 631423b4 | nem | 97 KB |
| `02_Areas/Mikado/dashboard.html` | (mint fent) | 631423b4 | nem | 97 KB |
| `02_Areas/Ignis Academy/dashboard.html` | (mint fent) | 631423b4 | nem | 97 KB |
| `02_Areas/Sonrisa/Vision Corner/dashboard.html` | (mint fent) | 631423b4 | nem | 97 KB |
| `02_Areas/ExarLabs/Clients/dashboard.html` | (mint fent) | 631423b4 | nem | 97 KB |
| `02_Areas/Personal Growth/Movies/dashboard.html` | (mint fent) | 631423b4 | nem | 97 KB |
| `02_Areas/Deák Húsüzlet/BIN/dashboard.html` | (mint fent) | 631423b4 | BIN — nem | 97 KB |
| `02_Areas/Sonrisa/CPS/Strategy/dashboard.html` | (mint fent) | 631423b4 | nem | 97 KB |
| `02_Areas/Sonrisa/CPS/Projects/Onriva/dashboard.html` | (mint fent) | 631423b4 | nem | 97 KB |
| `02_Areas/Sonrisa/CPS/Services/Cost optimization/dashboard.html` | (mint fent) | 631423b4 | nem | 97 KB |
| `04_Archive/Ignis/AI Kurzus/dashboard.html` | (mint fent) | 631423b4 | nem | 97 KB |

> **Megjegyzés:** Ez az elavult `dashboard.html` scatter — régi generáció, szétszórva az Area-kba. Az `_dashboards/` mappában él az aktuális rendszer. Mind a 12 azonos bájt-tartalommal (md5: 631423b4). Törlés előtt **ellenőrizd:** van-e CLAUDE.md vagy 01_PROJECT_STATE.md az adott Area-ban ami erre hivatkozik.

---

### TÖRLÉS JAVASOLT — Üres fájlok (0 byte)

| Fájl | Méret | Hivatkozás? | Megjegyzés |
|---|---|---|---|
| `Untitled.md` | 0 B | nem | Névtelen véletlen fájl a vault gyökerében |
| `Navigator reggeli email osszefoglalas.md` | 0 B | nem | Placeholder, soha nem töltötték ki |
| `02_Areas/Main TODO.md` | 0 B | nem | Üres, felváltotta az Area-specifikus TASKS.md-ek |
| `Templates/Vezetők_Imája_alkalom_template.md` | 0 B | nem | Üres template |
| `Templates/Contrast_Note_Template.md` | 0 B | nem | Üres template |
| `05_DailyNotes/2026/2026-W07.md` | 0 B | nem | Üres heti note |
| `03_Resources/02_Books/Building_a_StoryBrand_Donald_Miller_2017.md` | 0 B | nem | Üres könyvjegyzet placeholder |
| `02_Areas/Média Műhely/Belső rendszerek.md` | 0 B | 5 refs | HIVATKOZOTT — nem törlés, csak flag |
| `02_Areas/Personal Growth/Habits 3.md` | 0 B | nem | Üres, duplikált fájl sorozat |
| `02_Areas/Personal Growth/Habits 2.md` | 0 B | nem | Üres |
| `02_Areas/Personal Growth/Habits.md` | 0 B | nem | Üres |
| `02_Areas/Personal Growth/Habits 1.md` | 0 B | nem | Üres |
| `02_Areas/Navigátor Podcast/Patreon/EP06 - Fegyelem = Szabadság.md` | 0 B | nem | Üres Patreon post |
| `02_Areas/Navigátor Podcast/Patreon/EP05 - Startupok.md` | 0 B | nem | Üres Patreon post |

> **Kivétel:** `02_Areas/Média Műhely/Belső rendszerek.md` üres de 5 helyen hivatkozott — NEM törlés, csak flag (tartalom hiánya probléma).

**Agent placeholder fájlok (üres listing fájlok — ne töröld, rendszer írja):**
- `00_Prompts/BDOS/agents/presto/insights/_listing.md`
- `00_Prompts/BDOS/agents/presto/templates/_listing.md`
- `00_Prompts/BDOS/agents/presto/todos/_listing.md`

> Ezek Presto agent infrastructure fájlok. Kihagyandók — szándékosan üresek.

---

### TÖRLÉS JAVASOLT — Temp fájlok

#### Navigátor Podcast EP39 — régi LumaFusion temp

| Fájl | Méret | Dátum | Hivatkozás? | Megjegyzés |
|---|---|---|---|---|
| `02_Areas/Navigátor Podcast/Episodes/Archive/EP39 - Szexuális nevelés - Eberlein Éva/lu1885dh57.tmp` | 108 KB | 2026-03-09 | nem | LumaFusion temp, 90+ nap, Archive mappában |
| `02_Areas/Navigátor Podcast/Episodes/Archive/EP39 - Szexuális nevelés - Eberlein Éva/lu2645dhx5.tmp` | 116 KB | 2026-03-09 | nem | LumaFusion temp, 90+ nap |

#### Ignis Academy TransOffice — Word temp fájlok

> **Kontextus:** Az `lu45pmb3.tmp` fájlok Word/LibreOffice temp fájlok, amik a különböző TransOffice practice mappákban szétszóródtak. Az `02_Areas/Ignis/Ignis Academy/2. szint/Haladó/TransOfficeCopy/_DryRun_jelentés/jelentes.md` maga is megjegyzi: "valószínűleg törölhető". Ezek szándékos "csali" fájlok az Ignis Academy tananyagban, de a tényleges törlés javasolt.

| Fájl | Méret | Dátum | Hivatkozás? | Megjegyzés |
|---|---|---|---|---|
| `02_Areas/Ignis/Ignis Academy/2. szint/Haladó/TransOfficeCopy/lu45pmb3.tmp` | 40 KB | 2026-05-12 | igen (tananyag-dokumentumok hivatkoznak, de mint "csali") | Ignis tananyag, óvatosan |
| `02_Areas/Ignis/Ignis Academy/2. szint/Haladó/TransOfficeDryRun2.0/lu45pmb3.tmp` | 40 KB | 2026-05-13 | igen | mint fent |
| `02_Areas/Ignis/Ignis Academy/2. szint/Haladó/TransOfficeCopy_v4/lu45pmb3.tmp` | 40 KB | 2026-05-14 | nem | |
| `02_Areas/Ignis/Ignis Academy/2. szint/Haladó/TransOfficeCopy_v3/lu45pmb3.tmp` | 40 KB | 2026-05-14 | nem | |
| `02_Areas/Ignis/Ignis Academy/2. szint/Haladó/TransOffice_LIVE/Kuka/lu45pmb3_DUPLIKACIO_szerzodes_PaperWorld_2021_pdf.tmp` | 40 KB | 2026-05-15 | nem | Kuka almappában |
| `02_Areas/Ignis/Ignis Academy/2. szint/Haladó/TransOffice_LIVE/_BACKUP_2026-05-15/lu45pmb3.tmp` | 40 KB | 2026-05-15 | nem | Backup |
| `02_Areas/Ignis/Ignis Academy/2. szint/Haladó/dryrun3/_TransOffice_eredeti_BACKUP_20260514/lu45pmb3.tmp` | 40 KB | 2026-05-14 | nem | Backup |
| `02_Areas/Ignis/Ignis Academy/2. szint/Haladó/Tananyag/TransOffice/lu45pmb3.tmp` | 40 KB | 2026-05-05 | igen (tananyag masterben) | Ignis tananyag, óvatosan |

> **Sprint-óvatossági flag:** Az Ignis Academy tmp fájlok törlése előtt konzultáld az Ignis tananyag aktuális fázisát — a TransOfficeCopy és Live verziók aktív tananyag-pilot részei lehetnek.

#### Archive tmp (> 30 nap)

| Fájl | Méret | Dátum | Hivatkozás? | Megjegyzés |
|---|---|---|---|---|
| `04_Archive/Ignis/AI Kurzus/presentation/lu44629dnh.tmp` | 444 KB | 2026-03-24 | nem (README megemlíti mint szemét) | 04_Archive-ban, biztonságosan törölhető |

#### DH BIN temp

| Fájl | Méret | Dátum | Hivatkozás? | Megjegyzés |
|---|---|---|---|---|
| `02_Areas/Deák Húsüzlet/BIN/design/test_write_check.tmp` | 5 B | 2026-04-21 | nem | Test fájl, BIN-ben |

---

### ARCHIVÁLÁS JAVASOLT — Frontmatter status: archived/stale/outdated

**Eredmény:** 0 akcionálható eset.

A scan (`status: archived | stale | outdated`) 4 fájlt talált, de:
- `00_Prompts/BDOS/agents/librarian.md` — agent definíció, NEM érinthető
- `00_Prompts/BDOS/agents/presto/MARKETING_OS_FLOW_v2.md` — `status: draft`, NEM archived. Aktívan hivatkozott (presto.md + episode-launch.md + MARKETING_OS_STRATEGIC_NORTH_STAR.md).
- `00_Prompts/BDOS/agents/presto/_inbox/seeds/README.md` — `status: active`, nem stale
- `.claude/commands/lib-deepclean.md` — command fájl, NEM érinthető

---

### FLAG ONLY — Stale fájlok (180+ nap, nem hivatkozott vagy kevéssé hivatkozott)

> Ezek NEM törlési javaslatok. A stale flag-elés csak azt jelzi: érdemes átnézni, van-e még aktivitás.

| Fájl | Utolsó módosítás | Hivatkozások | Megjegyzés |
|---|---|---|---|
| `02_Areas/Main TODO.md` | >180 nap | 0 | Üres + stale, törlési jelölt (lásd fent) |
| `02_Areas/Ignis Academy/Resources.md` | >180 nap | 52 (!) | Erősen hivatkozott, valószínűleg aktív — csak flag |
| `02_Areas/Média Műhely/Belső rendszerek.md` | >180 nap | 5 | Üres + hivatkozott — tartalom hiányzik |
| `02_Areas/Média Műhely/Kliensek/Clean Service.md` | >180 nap | 5 | Stale kliens-adat |
| `02_Areas/Média Műhely/Kliensek/Koffer.md` | >180 nap | 6 | Stale kliens-adat |
| `02_Areas/Média Műhely/Kliensek/RMÜE.md` | >180 nap | 6 | Stale kliens-adat |
| `02_Areas/Média Műhely/Timeline.md` | >180 nap | 32 | Hivatkozott — csak flag |
| `02_Areas/Sonrisa/Learning/AI Roadshow - Vibe coding.md` | >180 nap | - | Learning note, stale |
| `02_Areas/Sonrisa/Vision Corner/TODO.md` | >180 nap | 396 (!) | Nagyon hivatkozott, aktív — ez csak a dátum alapján stale, tartalom valószínűleg friss |
| `02_Areas/Szervezet Fejlesztés/Vezetők Imája/Hasznos.md` | >180 nap | 20 | Stale, de hivatkozott |
| `03_Resources/02_Books/Building_a_StoryBrand_Donald_Miller_2017.md` | >180 nap | 0 | Üres placeholder, törölhető (lásd fent) |
| `03_Resources/02_Books/TO READ.md` | >180 nap | 1 | Stale reading list |
| `05_DailyNotes/2025/September/2025-09-02.md` | >180 nap | nem | Régi napi note — normális, nem törlési javaslat |
| `05_DailyNotes/2025/September/2025-09-06.md` | >180 nap | nem | mint fent |
| `05_DailyNotes/2025/September/2025-09-07.md` | >180 nap | nem | mint fent |
| `Templates/48 Laws of Power Template.md` | >180 nap | nem | Stale template |
| `Templates/Admonition template.md` | >180 nap | nem | Stale template |
| `Templates/Atomic_Note_Template.md` | >180 nap | nem | Stale template |
| `Templates/Book_Summary_Template.md` | >180 nap | nem | Stale template |
| `Templates/Timeline Template.md` | >180 nap | nem | Stale template |
| `Templates/Contrast_Note_Template.md` | >180 nap | 0 | Üres + stale, törlési jelölt (lásd fent) |
| `Templates/Vezetők_Imája_alkalom_template.md` | >180 nap | 0 | Üres + stale, törlési jelölt (lásd fent) |

---

### FLAG ONLY — Üres mappák (44 db)

> Törölhetők, de néhány szándékosan üres (scaffold, placeholder). Listából kizárva: ExarSharedBrain + node_modules.

**Valóban üres, törölhető (scaffold nem jelölt):**

| Mappa | Megjegyzés |
|---|---|
| `02_Areas/Média Műhely/memory/projects` | Memory mappa, scaffold |
| `02_Areas/Média Műhely/memory/people` | Memory mappa, scaffold |
| `02_Areas/MédiaMűhely/Kliensek/RMÜE` | Üres kliens mappa |
| `02_Areas/Ignis/Ignis Academy/Palyazat` | Üres pályázat mappa |
| `02_Areas/ExarLabs/memory/projects` | Memory scaffold |
| `02_Areas/Personal Growth/Ideas/atomic` | Üres idea mappa |
| `02_Areas/Personal Growth/Ideas/curate` | Üres idea mappa |
| `02_Areas/Deák Húsüzlet/BIN/DH` | BIN almappa |
| `02_Areas/Deák Húsüzlet/BIN/.claude` | BIN almappa |
| `02_Areas/Ignis Academy/Pályázat/05_correspondence` | Üres pályázat almappa |
| `02_Areas/Ignis Academy/Pályázat/04_decisions` | Üres pályázat almappa |
| `03_Resources/03_Podcasts/Steven Bartlett - The Only 5 Jobs That Will Remain In 2030 - Roman Yampolskiy/Atomic_Ideas` | Üres |
| `03_Resources/03_Podcasts/Steven Bartlett - The Only 5 Jobs That Will Remain In 2030 - Roman Yampolskiy/Contrasts` | Üres |
| `02_Areas/Navigátor Podcast/Episodes/Archive/EP39 - Gál Ildikó - Fegyelmezés` | Üres epizód-mappa |
| `02_Areas/Navigátor Podcast/Episodes/Navigátor Podcast Plugin/scripts` | Üres |
| `04_Archive/Ignis/AI Kurzus/memory/context` | Archive scaffold |
| `02_Areas/Sonrisa/Vision Corner/memory/projects` | Scaffold |
| `02_Areas/Sonrisa/Vision Corner/memory/people` | Scaffold |
| `02_Areas/Sonrisa/CPS/Partnership/Azure` | Üres partner mappa |
| `02_Areas/ExarLabs/Practices/EU-Digitalizare-Grants/patterns` | Üres practice mappa |
| `02_Areas/ExarLabs/Practices/EU-Digitalizare-Grants/_inbox` | Üres practice inbox |
| `02_Areas/ExarLabs/Practices/EU-Digitalizare-Grants/experiments` | Üres |
| `02_Areas/ExarLabs/Practices/EU-Digitalizare-Grants/decisions` | Üres |
| `02_Areas/Personal Growth/Movies/memory/context` | Scaffold |
| `02_Areas/Personal Growth/Ideas/_inbox/thoughts` | Üres |
| `02_Areas/Deák Húsüzlet/Business Development/strategy/Features` | Üres |
| `00_Prompts/Claude/Plugins/navigator-plugin-v0.3/scripts` | Plugin scripts üres |
| `00_Prompts/Claude/Plugins/navigator-plugin-v0.2/scripts` | Plugin scripts üres |
| `00_Prompts/BDOS/capabilities/web-publishing/agents` | Capability scaffold |
| `00_Prompts/BDOS/capabilities/web-publishing/teaching` | Capability scaffold |
| `00_Prompts/BDOS/agents/presto/reflections` | Agent scaffold |
| `00_Prompts/BDOS/agents/presto/discovery` | Agent scaffold |
| `00_Prompts/BDOS/agents/broker/reflections` | Agent scaffold |
| `02_Areas/Sonrisa/CPS/Sales/Case Studies/raw` | Üres |
| `02_Areas/Sonrisa/CPS/Services/Cost optimization/clients` | Üres |
| `00_Prompts/BDOS/agents/broker/sales-learnings/retired` | Agent scaffold |
| `00_Prompts/BDOS/agents/broker/sales-learnings/active` | Agent scaffold |
| `00_Prompts/BDOS/agents/broker/sales-learnings/proposals` | Agent scaffold |
| `00_Prompts/BDOS/agents/presto/audience-learnings/retired` | Agent scaffold |
| `00_Prompts/BDOS/agents/presto/audience-learnings/proposals` | Agent scaffold |
| `00_Prompts/BDOS/agents/presto/_inbox/approval-actions` | Agent scaffold |
| `00_Prompts/BDOS/agents/forge/logs/learning` | Agent scaffold |
| `00_Prompts/BDOS/agents/forge/logs/operational` | Agent scaffold |
| `02_Areas/Sonrisa/CPS/Accounts/Active/Colosseum_Dental/Reports_Invoices` | Üres |

---

### MEGJEGYEZVE — Hivatkozott, de potenciálisan elavult

| Fájl | Probléma | Ajánlás |
|---|---|---|
| `02_Areas/Média Műhely/Belső rendszerek.md` | 0 byte, de 5 helyen hivatkozott | Tartalom kitöltendő vagy hivatkozások frissítendők |
| `02_Areas/Sonrisa/Vision Corner/TODO.md` | >180 nap módosítatlan, de 396 hivatkozás | Valószínűleg `mtime` nem frissül Obsidian-ban — vizsgáld meg manuálisan |
| `02_Areas/Ignis Academy/Resources.md` | >180 nap, de 52 hivatkozás | Mint fent |
| `00_Prompts/BDOS/capabilities/BUSINESS_PLAN.md` | Byte-azonos az ExarLabs verzióval, de a capabilities/ helye logikátlan | Törlés javasolt (duplikátum szekció) |

---

### MEGJEGYEZVE — Nagyszabású kizárások (külön kezelendők)

| Terület | Méret | Probléma | Ajánlott akció |
|---|---|---|---|
| `02_Areas/ExarLabs/resources/ExarSharedBrain/` | 163 MB | Önálló git repo (ExarLabs/ExarSharedBrain) — a vault-tükrözött fájlok (dashboardok, plugins, BDOS docs) byte-azonos duplikátumait tartalmazza | Git submodule-ként kezelni VAGY gitignore-ba venni a vault `.gitignore`-jában. Nem vault-szintű törlés. |
| `02_Areas/ExarLabs/Practices/microsite-factory/node_modules/` | 414 MB | node_modules a vault-ban | `.gitignore`-ba venni (ha még nincs), lokálisan NE szinkronizálni Google Drive-ra |
| `02_Areas/Deák Húsüzlet/BIN/` | 21 MB | BIN mappa aktív sprint-területen | Sprint-óvatosság: ne érintsd amíg Sprint 3 aktív |

---

### RENDSZER — Gyökér index fájlok státusza

A git status alapján az alábbi root-szintű index fájlok **törölt (Deleted) státuszban** vannak a working tree-ben:

| Fájl | Git státusz | Következtetés |
|---|---|---|
| `00_INDEX.md` | nem létezik (nincs staged delete) | Soha nem lett létrehozva (Librarian index mód nem futott) |
| `00_KNOWLEDGE_MAP.md` | `D` (deleted, staged) | Korábban létezett, törölve lett — helyesen |
| `00_GAPS.md` | `D` (deleted, staged) | Korábban létezett, törölve lett — helyesen |
| `00_OPEN_QUESTIONS.md` | `D` (deleted, staged) | Korábban létezett, törölve lett — helyesen |
| `00_DECISIONS_INDEX.md` | `D` (deleted, staged) | Korábban létezett, törölve lett — helyesen |

**Következtetés:** A root-szintű index fájlok (kivéve `00_INDEX.md` és `00_INTEGRATE_PROPOSALS.md`) megfelelően eltávolítva. Az `00_INDEX.md` újragyártásához futtasd a Librarian `index` módot.

---

## Végrehajtás — 2026-06-07

**Állapot: APPLY futtatva**

| Kategória | Tervezett | Végrehajtott | Megjegyzés |
|---|---|---|---|
| DailyNotes "(1)" duplikátumok | 10 | 10 | Törölve |
| Egyéb byte-azonos duplikátumok | 4 | 4 | general-utils.plugin (BIN), BUSINESS_PLAN.md (capabilities/), Ghidul PDF (01_Projects/), összes dashboard.html scatter |
| Dashboard.html scatter | 12 | 12 | Törölve |
| Üres fájlok | 13 | 13 | Törölve (Belső rendszerek.md kihagyva, hivatkozott) |
| Temp fájlok | 4 | 4 | LumaFusion (EP39), Archive tmp, DH BIN test |
| Ignis TransOffice tmps | 8 | 0 | KIHAGYVA (sprint-óvatosság, tananyag) |
| Üres mappák | 44 | 43 | 1 nem létezett (MédiaMűhely névkülönbség) |
| .gitignore frissítés | - | KÉSZ | node_modules/** + ExarSharedBrain/ hozzáadva |

## Nyitott tennivalók

- **Ignis TransOffice tmp fájlok (8 db, ~320 KB):** Ellenőrizd a tananyag-pilot státuszát, majd töröld manuálisan ha már nem aktív
- **ExarSharedBrain (163 MB):** gitignore-ba felvéve; ha Google Drive szinkronból is ki kell venni, az Obsidian Sync kivétellistájában kell kezelni
- **microsite-factory/node_modules (414 MB):** gitignore-ba felvéve; lokálisan maradt, Google Drive szinkronból érdemes kizárni
- **2026-03-15.md vs 2026-03-29.md:** Azonos tartalmú napi note-ok, felhasználói döntés szükséges
- **Librarian index mód:** `00_INDEX.md` regenerálás javasolt a következő session-ben
