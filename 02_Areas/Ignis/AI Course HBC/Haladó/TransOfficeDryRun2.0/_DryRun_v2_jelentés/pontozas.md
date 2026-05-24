# Dry-Run v2.0 Pontozás — Ignis Academy Haladó AI Workshop

> **Készítette:** Claude (dry-run v2.0 meta-evaluator)
> **Dátum:** 2026-05-13
> **Skála:** 1-10 (1 = csapnivaló, 5 = elfogadható, 7 = jó, 8-9 = kiváló, 10 = referencia-szintű)
> **Forrás:** A 6 fázis tényleges végrehajtása a TransOfficeDryRun2.0/ mappában (29 output) + az oktatói segédlet v2.0 értékelése
> **Modell:** instructor-led + stáció pedagógia
> **Új 8. kritérium:** **Stáció-tisztaság** — a stáció(k) izoláltak? Egy résztvevő meg tudja csinálni F1 után, függetlenül a páros előző tevékenységétől?

---

## v2.0 összesített pontozási tábla

| Fázis | Érth. | Új info | Haszn. | Narr. | WOW | Hands-on | Real. | **Stáció** | **Átlag** |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Bevezető (0:00-0:22)** | 8 | 6 | 7 | 9 | 7 | 5 | 8 | 7 | **7,1** |
| **F1 — Káoszból rendszer** | 9 | 9 | 10 | 9 | 9 | **9** | 9 | **10** | **9,3** |
| **F2 — TODO-k** | 8 | 10 | 9 | 9 | 9 | 8 | 8 | 9 | **8,8** |
| **F3 — Pályázat-elemzés** | 7 | 9 | 10 | 8 | 9 | 7 | 8 | 8 | **8,3** |
| **F4 — Multi-persona** | 7 | 10 | 9 | 10 | 10 | 7 | 7 | 8 | **8,5** |
| **F5 — Pályázat összeáll.** | 7 | 9 | 10 | 9 | **10** | **9** | 7 | **10** | **8,9** |
| **F6 — Web redesign** | 9 | 8 | 8 | 8 | 10 | **10** | 8 | 9 | **8,8** |
| **Zárás (3:37-3:50)** | 10 | 5 | 9 | 10 | 7 | 9 | 9 | 8 | **8,4** |
| **ÖSSZÁTLAG** | **8,1** | **8,3** | **9,0** | **9,0** | **8,9** | **8,0** | **8,0** | **8,6** | **8,5** |

---

## v1.0 vs v2.0 — ÖSSZEHASONLÍTÓ TÁBLA

### Fázisátlagok

| Fázis | v1.0 átlag | v2.0 átlag | **Különbség** |
|-------|:----------:|:----------:|:--------------:|
| Bevezető | 7,0 | 7,1 | +0,1 |
| F1 | 8,6 | **9,3** | **+0,7** |
| F2 | 8,4 | 8,8 | +0,4 |
| F3 | 8,1 | 8,3 | +0,2 |
| F4 | 8,1 | 8,5 | +0,4 |
| F5 | 7,7 | **8,9** | **+1,2** |
| F6 | 8,4 | 8,8 | +0,4 |
| Zárás | 8,3 | 8,4 | +0,1 |
| **Összátlag** | **8,1** | **8,5** | **+0,4** |

### Kritériumonkénti változás

| Kritérium | v1.0 átlag | v2.0 átlag | **Különbség** |
|-----------|:----------:|:----------:|:-------------:|
| Érthetőség | 7,9 | 8,1 | +0,2 |
| Új info (Cowork-spec) | 8,3 | 8,3 | 0,0 |
| Hasznosság | 8,5 | 9,0 | **+0,5** |
| Narratív illeszkedés | 9,0 | 9,0 | 0,0 |
| WOW-faktor | 8,6 | 8,9 | +0,3 |
| **Hands-on érték** | **6,5** | **8,0** | **+1,5** ⭐ |
| Realizmus | 7,9 | 8,0 | +0,1 |
| ÚJ: Stáció-tisztaság | — | 8,6 | (új) |

---

## Hol történtek a legnagyobb javulások?

### ⭐ 1. F5 — Pályázat összeállítás (+1,2)

**Ez a v2.0 legnagyobb fejlődése.** Az új **5.A (form-katalogizáló) + 5.B (manuális idő-becslés) stáció-pár** strukturálisan megváltoztatta a fázis dramaturgiáját. A v1.0-ban az F5 csak **DEMO-WOW** volt (Cowork tölti ki a formot), míg a v2.0-ban a résztvevők **maguk is hozzányúlnak a forráshoz** (55 mező katalogizálása + kb. 90 perces manuális idő becslése). Amikor a Cowork 90 mp alatt kitölti az egészet, **a 90 perc nem üres állítás, hanem a résztvevők saját számolása**. Pszichológiailag elképesztően hatékony.

**Pontváltozások:** Hands-on 6 → 9 (+3), WOW 9 → 10 (+1), Hasznosság 9 → 10 (+1), Stáció (új) = 10.

### ⭐ 2. Hands-on érték (+1,5)

A v1.0 legrosszabb pontja (6,5 átlag) **az új stáció-modellel egyértelműen javult** 8,0-ra. **Minden fázisban** van legalább 1-2 saját laptopon végzett stáció — az F1-ben mindenki egyszerre futtatja az A.1 promptot (parallel mode), F2-F5-ben 2-2 stáció, F6-ban 3 saját variáns. **A 70/20/10 arány a v2.0-ban valóban közelít a 65/30/5-höz.**

**Hol vannak még tartalékok?** Az F3 (Hands-on 7) és F4 (Hands-on 7) — itt a stációk **lényegileg rövid analízis-feladatok** (CR-08, M-11, Béla válasz, EBITDA margin), nem **kreatív** vagy **outputtermelő** akciók.

### ⭐ 3. F1 — Káoszból rendszer (+0,7)

A v1.0-ban az F1 egy 5 perces „MICRO HANDS-ON" volt (mindenki beolvas 3 fájlt + summary-t kér). A v2.0-ban viszont **a teljes 15 perc parallel-stáció** — minden résztvevő **maga futtatja az A.1 promptot a teljes mappára**, és **saját CLAUDE.md-vel távozik**. Ez **F2-F6-tól kezdve élesít minden további stációt** (mindenki a saját CLAUDE.md-jét használja).

**Pontváltozások:** Hands-on 6 → 9 (+3), Hasznosság 9 → 10 (+1), Stáció (új) = 10.

### Másodlagos nyertesek

- **F2 +0,4** — a Productivity plugin demó nem változott, de a 2.A stáció (follow-up email) **konkrét output**
- **F4 +0,4** — a 4.B EBITDA-stáció **számszerű azonnali eredmény**, ami minden résztvevőnél verifikálható
- **F6 +0,4** — a Hands-on 9 → 10 (a v2.0-ban **3 saját variáns** kötelező, nem opcionális)

---

## v2.0 stáció-tisztaság (új 8. kritérium) — részletes magyarázat

| Fázis | Stáció-tisztaság | Indok |
|-------|:----------------:|-------|
| Bevezető | 7 | „1 mondat amit várok" verbális, nem laptop-stáció — átmeneti |
| F1 | **10** | Mindenki egyszerre, ugyanaz a A.1 prompt, F1 után **minden résztvevőnek saját CLAUDE.md-je van** |
| F2 | 9 | 2.A önállóan futtatható, csak a saját CLAUDE.md kell — izolált |
| F3 | 8 | 3.A + 3.B önállóan futtatható, **de** kissé hasonlít egymásra (mindkettő analízis) |
| F4 | 8 | 4.A + 4.B önálló, de **a 4.A vételi opció része a látott Béla bácsi-válaszra épül** — nem 100% izolált |
| F5 | **10** | 5.A + 5.B kombinációja **dramaturgiai szempontból tökéletes**, és mindkettő önállóan futtatható |
| F6 | 9 | 3 saját variáns ugyanazon sablonprompttal, **csak [STÍLUS] szót cserél** — **akkor is működik ha valaki a modern referenciát nem látta** |
| Zárás | 8 | „1 mondat" saját Cowork-jén futtatható, de a stáció-output **emlékezet-függő** (a fázisokra kell visszanézni) |
| **Átlag** | **8,6** | A stáció-tisztaság **átlagosan kiváló** — a v2.0 fő pedagógiai célja teljesült |

---

## Top 3 v2.0-erősség

1. **A stáció-modell strukturálisan megoldotta a v1.0 hands-on gyenge pontját.** A 6,5-ről 8,0-ra emelkedés (+1,5) a **legnagyobb egyetlen javulás** — a workshop most **valódi 65/30/5 arányban** dolgozik, nem csak névlegesen.

2. **Az F5 stáció-pár (5.A + 5.B) a dramaturgia új csúcsa.** A „**90 perc saját becslés vs 90 mp Cowork**" kontraszt-pillanat **a saját számukból érkezik**, nem az oktató állításából. Ez **pszichológiai mestermű**.

3. **Az F1 párhuzamos stáció = univerzális indítópont.** Mindenki **saját** CLAUDE.md-jével távozik F1-ből, ami az összes további fázis (F2-F6) stáció-tisztaságát biztosítja — egy résztvevő **bármelyik fázisnál újra tud csatlakozni**, mert a CLAUDE.md a kontextust hordozza.

---

## Top 3 v2.0-fejlesztendő pont (v2.1 felé)

1. **F3 + F4 stációk túl analitikusak** (mindkét fázisnál Hands-on 7). A stációk kérdezz-felelek típusúak, **nem kreatívak vagy output-termelők**. A v2.1 ide **kreatívabb stáció-feladatokat** építhet (pl. F3: „*írj 5 mondatos riasztó-emailt egy AFM-felelősnek*"; F4: „*módosítsd a CEO PPT 4. slide-ját egy másik kockázattal*").

2. **Csendes Cowork-várás** F4.3 (PPT) és F5.1 (Plan de afaceri) közben — **az oktatónak csendben várnia kell 60-180 mp**. **Javaslat**: párhuzamos indítás (F4.3 PPT-t az 4.B stáció alatt elindítani), vagy „mesélj közben" instrukció a segédletben.

3. **A „1 dolog amit várok" bevezető stáció verbális** — a többi stációval ellentétben nem laptopon történik. **Javaslat**: kombináljuk: a résztvevő **a saját Cowork-jébe írja be** az 1 mondatot, ami **F1 nyitásakor automatikusan elérhető** (új context-item).

---

## ÖSSZÁTLAG: v1.0 = 8,1 → v2.0 = 8,5 (+0,4)

A v2.0 átlag-pontszám **0,4-del** magasabb mint a v1.0 — ami **átlag-szinten kis változás, de a Hands-on dimenzióban +1,5** (a 8 kritériumból a leggyengébb pont). A workshop **filmszerű erőssége és narratív íve megmaradt** (mindkét érték 9,0), miközben **a tényleges résztvevői aktivitás strukturálisan megemelkedett**.

---

## Egy mondatos overall vélemény

A v2.0-os átdolgozás **megérte**: a workshop **változatlan narratív erővel** és **mérhetően magasabb résztvevői aktivitással** működik — az F5 stáció-pár pedig **a workshop dramaturgiájának új csúcsa** lett, ami önmagában indokolja a v1.0 → v2.0 átdolgozás befektetését.
