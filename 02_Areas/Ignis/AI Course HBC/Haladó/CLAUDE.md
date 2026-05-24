# Ignis Academy — Haladó AI Workshop (HBC)

## Mi ez?
Egy 4 órás, haladó szintű AI workshop tananyaga. A célközönség: 10-15 fős HBC csoport, akik már hallottak az AI-ról, de nem használják rendszeresen. A workshop célja: megtapasztalják, milyen az, amikor az AI ténylegesen együtt dolgozik velük.

## Módszer
**„Narrated Live Experience"** — nem tool training, hanem guided future experience.
- 70% élő demo (az oktató narrálva mutatja)
- 20% guided micro hands-on (résztvevők kis módosításokat csinálnak)
- 10% szabad próbálkozás

**Eszközök:** Claude Cowork (Pro, $20/hó) + Obsidian + Markdown
**Szimuláció:** Fiktív cég (TransOffice Trade SRL), a résztvevők Operations Manager szerepben

---

## 📁 Mappastruktúra — a 2 fő mappa szétválasztva

A projekt két, azonos struktúrájú gyökér-mappára van bontva:

```
Haladó/
├── CLAUDE.md                              ← TE ITT VAGY (struktúra-magyarázat)
│
├── Tananyag/                              ← 🎓 ZIP-ELHETŐ TANULÓI CSOMAG
│   │                                        (a résztvevő ezt kapja meg)
│   ├── README.md                          ← Verzió + bemutató + használat
│   ├── 00_Bevezetes/
│   ├── TransOffice/                       ← A fiktív cég kaotikus assetjei (kiindulópont)
│   ├── 01_Ceg_megertes/                   ← Feladatleírások (F1)
│   ├── 02_Meeting_Productivity/           ← F2 feladatok + assetek
│   ├── 03_Dontes_Elemzes/                 ← F3: pályázati kiírás + minta-outputok
│   ├── 04_Legal_Szerzodes/                ← F4: emailek, Excel-melléklet
│   ├── 05_Kommunikacio_Email/             ← F5: üzleti terv, csomag, form
│   └── 06_Marketing_Honlap/               ← F6: TransOffice „régi" weboldal
│
└── Műhely/                                ← 🛠 FEJLESZTŐI BACKSTAGE
    │                                        (a tanulónak NEM kell)
    ├── README.md                          ← Mit hol találsz
    ├── 00_Tervezes/                       ← Narratíva, master plan, kompetitor-elemzés
    │   └── 00_STORY_BOOK.md               ← 🌟 ELŐSZÖR EZT olvasd minden új session-kor!
    ├── 01_Ceg_megertes/                   ← (üres / jegyzetek)
    ├── 02_Meeting_Productivity/           ← (üres / jegyzetek)
    ├── 03_Dontes_Elemzes/                 ← Pályázati PDF build-szkriptek + archív
    ├── 04_Legal_Szerzodes/                ← Bérleti szerződés docx build
    ├── 05_Kommunikacio_Email/             ← (üres / jegyzetek)
    └── 06_Marketing_Honlap/               ← ANAF design-system forrás + archív
```

### Miért két mappa?

**Tananyag/** = a *tanulói csomag*. Itt csak az van, ami a résztvevőnek kell a workshop futtatásához:
- Cégleírás, feladatleírások, kész assetek (PDF, docx, html, xlsx).
- README.md a verzióval + bemutatóval.
- Ez a mappa zip-elhető és átadható.

**Műhely/** = a *fejlesztői backstage*. Itt minden, ami a Tananyag előállításához és karbantartásához kell:
- Tervezési doksik, narratíva, Story Book.
- Build-szkriptek (Python a pályázati PDF-hez, JS a szerződés-docx-hez).
- Design-system forrás-fájlok (eredeti ANAF CSS bundle).
- Korábbi verziók archívumai (`_archive/`, `_LEGACY_*`).
- **Ez a mappa NEM kerül a zip-be.**

A két mappa **azonos fázis-számozást használ** (`01_` → `06_`), hogy egy fázis fejlesztői anyagát könnyen kapcsolni lehessen a tanulói anyaghoz.

---

## A 6 feladat (narratív ív)

A workshop egy történet: a TransOffice pályázni akar elektromos autó flottára (70-80% EU támogatás), de a cég teljes káoszban van. A résztvevők végigviszik az utat a káosztól a kész pályázatig.

| # | Feladat | Lényeg | Idő |
|---|---------|--------|-----|
| F1 | Rend a fájlok között | Kaotikus TransOffice → rendezett mappastruktúra + CLAUDE.md | 20-25p |
| F2 | Rend a TODO-k között | Pályázat-meeting transcript → TODO-k (Productivity plugin) | 20-25p |
| F3 | Adatvadászat + eligibility | Pályázati kiírás → mi kell, mi van meg, mi hiányzik | 25-30p |
| F4 | Kommunikáció + feldolgozás | Emailek, Excel elemzés, szerződés jogi check, CEO prezentáció | 30-35p |
| F5 | Pályázat összeállítás | Submission package + form kitöltés (WOW blokk) | 30-35p |
| F6 | Web redesign | Régi oldal elemzés → új HTML + pályázati info | 25-30p |

---

## Kidolgozási státusz

| Elem | Státusz |
|------|---------|
| Master terv (00_Tervezes/02_ChatGPT szintézis) | ✅ kész |
| Bevezető script | ✅ kész |
| Zárás script | ✅ kész |
| Tananyag/TransOffice/ asseteket (27+ fájl) | ✅ kész |
| F1 feladatleírások | ✅ kész |
| F2 feladatleírások + transcript | ✅ kész |
| F3 feladatleírások + 94 oldalas pályázati kiírás MD+PDF | ✅ kész |
| F3→F4 átmenet — 3 minta-output (Pelda_outputok/) | ✅ kész |
| F4 README + 3 feladatleírás + emails (Béla bácsi, Mihaela) | ✅ kész |
| F5 README + 3 feladatleírás + üzleti terv + csomag + form HTML | ✅ kész |
| F6 weboldal (4 oldal: Acasă, Despre noi, Produse, Servicii + ANAF design) | ✅ kész |
| Prompt library | ❌ nem kezdődött |
| Próba-futtatás (dry run) | ❌ |
| **MELLÉKLET:** Versenytárs-elemzés (ThriveNexus) + PDF | ✅ kész |

---

## Hogyan dolgozz ezen a projekten

1. **🌟 OLVASD BE ELŐSZÖR:** `Műhely/00_Tervezes/00_STORY_BOOK.md` — **a workshop teljes narratívája egy helyen**.
2. **Master plan (technikai):** `Műhely/00_Tervezes/02_ChatGPT szintézis - Workshop struktúra.md`
3. **Kontextus a cégről:** `Tananyag/00_Bevezetes/Ceg_leiras_TransOffice.md`
4. **Filozófia:** `Műhely/00_Tervezes/05_ChatGPT szintézis v0.3 - Filozófia és delivery.md`
5. **F4 Legal sub-flow narratíva:** `Műhely/00_Tervezes/06_F4_narrativa_legal_plugin.md` — a Béla bácsi sztori részletesen
6. **Session log:** `Műhely/00_Tervezes/03_Jelen beszélgetés összefoglaló.md`
7. **Szerkesztés:** Google Drive mount, `Edit` tool nem működik — használj bash + sed/cat
8. **🔄 FRISSÍTÉS:** ha új narratíva-elem, asset, vagy fázis-finomítás van — **frissítsd a Story Book-ot** (`Műhely/00_Tervezes/00_STORY_BOOK.md`) is!

---

## Fontos szabályok

- A **Tananyag/** mappa tartalma az, amit a résztvevők látnak — legyen tiszta és önálló.
- A **Műhely/** mappa a mi munkaanyagunk — itt lehet messy, archív és köztes verziókat tárolni.
- A **TransOffice/** fájlok SZÁNDÉKOSAN kaotikusak — ez a kiindulópont F1-hez.
- Minden feladatnak van: kontextus, feladat, prompt javaslat, tanulási pont, checkpoint (WOW + MICRO).
- A pályázat (elektromos autó flotta) a fő narratív szál F2-től F6-ig.
- A két mappa **azonos fázis-számozást használ** (`01_` → `06_`) a könnyű kapcsolhatóság érdekében.
