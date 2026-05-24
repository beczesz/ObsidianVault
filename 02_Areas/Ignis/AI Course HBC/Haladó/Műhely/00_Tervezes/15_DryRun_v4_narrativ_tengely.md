# 🎬 Dry-Run v4.0 — F3-F4 narratív tengely teszt

> **Cél:** A workshop **veleje** annak vizsgálata — hogy F3-ban **organikusan** kibukik-e a 2 piros pont, és F4-ben a 2 felkérő email **logikai folytatás** legyen.
> **Mit NEM tesztelünk:** copy-paste foolproof (azt a v3.0 csinálta).
> **Mit tesztelünk:** narratív dramaturgia + súgás-mentesség.

---

## A WORKSHOP DRÁMAI TENGELYE (amit teszteljük)

```
F3 gap-analízis →  2 PIROS PONT organikusan kibukik
                   ├─ Telephely-stabilitás (5 év kell, jelen 2 év) → Béla bácsi-szál
                   └─ Pénzügyi adatok 2024+2025 (TransOffice-on csak 2022) → Mihaela-szál
                            │
                            ▼
F4 stáció emailek  ←  a 2 piros pontra reagálnak konkrétan
                   ├─ Felkérő email Béla bácsinak (act adițional + acord scris)
                   └─ Felkérő email Mihaelának (bilanc 2024+2025)
```

**Kérdés:** A Cowork ezt **organikusan** találja meg, vagy **súgnunk kell**?
Ha súgnunk kell → a tananyagot javítani kell.

---

## A prompt (másold egy ÚJ Cowork sessionbe):

```
Te most egy szigorú narratív-tengely tesztet végzel az "Ignis Academy
Haladó AI Workshop" tananyagán. A kérdés: tényleg kibukik-e F3-ban a 2
kritikus probléma, amit F4-ben megoldunk?

==== A TANULÁS-DRAMATURGIA ====

F3 gap-analízisében 2 piros pontnak kellene kibuknia:
  1. TELEPHELY-STABILITÁS: a pályázat 5 év stabilitást követel a beadás
     dátumától, de a TransOffice bérleti szerződése csak 2028-ig megy
     → 2026-ban beadva csak 2 év marad. Plusz: töltőpont-engedély
     (acord scris) is kell.
  2. PÉNZÜGYI ADATOK: a pályázat utolsó 2 lezárt évet kéri (2024+2025),
     de a TransOffice mappában csak 2022-es eves_jelentes található
     → Mihaela (külsős könyvelő) kell.

Ha NEM bukik ki organikusan, vagy SÚGNI kellene, az hiba.

==== HOZZÁFÉRÉSI MODELL ====

Cowork hozzáférés:
- TransOfficeCopy_v4/ mappa (a Haladó/ gyökerében — előre elkészítve)
  • benne van a TransOffice/ 38 fájlja a kaotikus káoszban
  • plusz: TransOfficeCopy_v4/_palyazat_kiiras_csatolt/ mappa, ami a
    pályázati kiírás PDF-jét tartalmazza (mintha az oktató most
    csatolta volna a meeting-en)

Read-only "Obsidian-szimuláció" (csak hogy a prompt-okat extraháld):
- Tananyag/01_Ceg_megertes/Feladat_1.1.md          (F1)
- Tananyag/02_Meeting_Productivity/Feladat_2.2_*.md (F2 stáció)
- Tananyag/03_Dontes_Elemzes/Feladat_3.1_*.md      (F3 stáció 3.A)
- Tananyag/03_Dontes_Elemzes/Feladat_3.2_*.md      (F3 stáció 3.B)
- Tananyag/04_Legal_Szerzodes/Feladat_4.1_*.md     (F4 stáció 4.A)
- Tananyag/04_Legal_Szerzodes/Feladat_4.2_*.md     (F4 stáció 4.B)

NEM nyúlhatsz:
- Műhely/ (oktatói segédlet, story book, pelda outputok — ezeket egy
  résztvevő nem látja)
- A Tananyag-ban a DEMO-fájlok (F3.3, F4.3) → ezek az oktatóé

==== A 6 LÉPÉSES TESZT ====

────────────────────────────────────────────────────────────────
1. LÉPÉS — F1 (Feladat_1.1.md alapján)
────────────────────────────────────────────────────────────────
Másold ki az F1 promptot a Feladat_1.1.md "## A stáció prompt"
szekciójából, és futtasd a saját Cowork-eden a TransOfficeCopy_v4
mappán.

Cél: kapj CLAUDE.md-t + rendezett mappát + kivonatot.

────────────────────────────────────────────────────────────────
2. LÉPÉS — F2 stáció (Feladat_2.2)
────────────────────────────────────────────────────────────────
Másold ki és futtasd. Eredmény: 1 follow-up email Enikőnek.

────────────────────────────────────────────────────────────────
3. LÉPÉS — F3.1 STÁCIÓ (Feladat_3.1)
────────────────────────────────────────────────────────────────
A pályázati PDF a TransOfficeCopy_v4/_palyazat_kiiras_csatolt/
mappában van — "az oktató csatolta".

Futtasd az F3.1 prompt-ot (a Feladat_3.1-ben). A Cowork:
- Át kell hogy másolja a PDF-et a TransOffice/Palyazat_kiiras/-ba
- Meg kell hogy találja a CR-08 kritériumot
- Ki kell, hogy értékelje teljesít-e

────────────────────────────────────────────────────────────────
4. LÉPÉS — F3.2 GAP ANALÍZIS *** A FŐ TESZT ***
────────────────────────────────────────────────────────────────
A workshop szerint F3.2-ben az oktató egy ÁLTALÁNOS prompt-ot ad.
NE súgj — adj egy szándékosan általános promptot:

"Olvasd át alaposan a TransOffice/Palyazat_kiiras/-ban lévő pályázati
kiírást. Listázd ki a 17 kötelező mellékletet. Minden mellékletre jelöld
a TransOffice cégadatok (CLAUDE.md + TransOffice/ mappa) alapján:
VAN / NINCS / RÉSZBEN. Ahol RÉSZBEN vagy NINCS, írd oda kitől kell
beszerezni és milyen formátumban."

⚠️ KRITIKUS ELLENŐRZÉSEK (saját rögzítendő megfigyelés):

   (a) Kibukik-e a "Bérleti szerződés stabilitás 5 év"
       PIROS/RÉSZBEN-ként?
       ▸ A Cowork azt mondja-e: "a meglévő szerződés 2028-ig megy,
         de a pályázat 5 év stabilitást követel 2026-08-31-től,
         tehát 2031-ig — nem teljesül"?
       ▸ Megemlíti-e külön az "acord scris a töltőpontra"
         követelményt?

   (b) Kibukik-e a "Pénzügyi adatok 2024+2025" PIROS-ként?
       ▸ A Cowork azt mondja-e: "a TransOffice/Kovacs_Ilona/-ban
         csak 2022-es eves_jelentes található, de a pályázat
         2024+2025-öt kér — nem teljesül, könyvelőhöz kell fordulni"?

   (c) Megemlít-e a Cowork **több piros pontot is**, vagy csak
       ezt a 2-t? Ha sokat → még jobb (több anyag F4-be).

────────────────────────────────────────────────────────────────
5. LÉPÉS — F4.1 STÁCIÓ (Feladat_4.1 — Béla bácsi felkérő email)
────────────────────────────────────────────────────────────────
Másold a prompt-ot és futtasd.

ELLENŐRZÉS: az email a két konkrét kérést tartalmazza?
  • act adițional a szerződés meghosszabbítására (2031-ig)
  • acord scris a töltőpont telepítésére

→ A két kérés logikailag KÖVETKEZIK a F3.2 piros pontjából?

────────────────────────────────────────────────────────────────
6. LÉPÉS — F4.2 STÁCIÓ (Feladat_4.2 — Mihaela felkérő email)
────────────────────────────────────────────────────────────────
Másold a prompt-ot és futtasd.

ELLENŐRZÉS: az email a konkrét adatokat kéri?
  • bilanț + cont P&L + EBITDA + alkalmazotti adatok
  • 2024 ÉS 2025 évre

→ Az email logikailag KÖVETKEZIK a F3.2 piros pontjából?

==== META-JELENTÉS ====

Készíts TransOfficeCopy_v4/_DryRun_v4_jelentes/narrativ_tengely.md fájlt:

## 1. A 2 piros pont organikus kibukása F3.2-ben

### TELEPHELY-STABILITÁS
- Kibukott-e? ✅ IGEN / ❌ NEM / ⚠️ RÉSZBEN
- Mikor (melyik lépésnél)?
- Pontos szöveg a Cowork outputjából (idézet):
  > "..."
- Súgnod kellett? (igen/nem — ha igen, mit?)

### PÉNZÜGYI ADATOK 2024+2025
- Kibukott-e?
- Mikor?
- Pontos szöveg:
- Súgnod kellett?

### EGYÉB potenciálisan piros pontok amiket talált:
- ...

## 2. A 2 felkérő email konzisztenciája

### F4.1 (Béla bácsi):
- Tartalmazta act adițional? ✅/❌
- Tartalmazta acord scris a töltőpontra? ✅/❌
- Konzisztens-e a F3.2-ben kibukott piros ponttal?

### F4.2 (Mihaela):
- Kérdezett bilance + cont P&L + EBITDA + alkalmazotti adatokat? ✅/❌
- 2024+2025 évre? ✅/❌
- Konzisztens-e a F3.2-ben kibukott piros ponttal?
- Románul írt-e?

## 3. Konzisztencia-ellenőrzés a 2026-os dátum-pivottal

- A Cowork "ma" dátuma érzékeli-e 2026-os időkeretet?
- A pályázat határidő (2026-08-31) konzisztens a meeting dátumával
  (2026-08-25)?
- Bárhol talál-e a Cowork 2025-ös ellentmondást?

## 4. v2.1 → v2.2 javítási javaslatok

[1-5 konkrét javaslat amit fixálni kell mielőtt élesedik]

## 5. Egy mondatos overall

A workshop F3 → F4 dramaturgiai tengelye **organikusan működik-e**?

==== INDULJ ====

Kezdj F1-gyel. Ne improvizálj — légy szigorú megfigyelő. A cél:
kiderüljön, hogy a workshop tényleg lát-e organikusan, vagy
súgni kell.

Munkára!
```

---

## Mi készült elő hozzá (előre, ehhez a sessionhez nem kell csinálni)

- ✅ `TransOfficeCopy_v4/` — tiszta kópia a 38 TransOffice-fájllal
- ✅ `TransOfficeCopy_v4/_palyazat_kiiras_csatolt/Ghidul-...-IMM-2026.pdf` — a pályázati PDF mintha az oktató most csatolta volna
- ✅ Tananyag fájlok v2.1 frissítve (F1 v2.1 prompt, F4.1+F4.2 felkérő emaileket írnak)
- ✅ Dátum-pivot 2026-ra konzisztens (kiírás IMM-2026, meeting 2026-08-25, bilanc 2024-2025)

## Mit várható eredmény (hipotézisek)

**Optimista (a workshop dramaturgia szilárd):**
- Mindkét piros pont organikusan kibukik a 4. lépésben
- A 2 stáció email logikai folytatás — pontos kérésekkel
- Realizmus +0,5 pont a v2.0-hoz képest

**Pesszimista (kritikus lyukak):**
- A pénzügyi piros pont kibukik (mert a 2022-es Excel régi)
- DE: a telephely-piros NEM bukik ki spontán (mert a Cowork lehet hogy nem hasonlítja össze a 2028-as lejáratot a 5-éves követelménnyel)
- → v2.2-ben az F3.2 prompt-ot pontosítani kell

**Reális (közbülső):**
- Mindkét piros kibukik, de **az acord scris a töltőpontra** nem külön ponthordozóként → e fontos részlet pontosítást igényel

---

**Készült:** 2026-05-14 · **Verzió:** 4.0 (narratív tengely teszt)
