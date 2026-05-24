# 🎬 Dry-Run Indító Prompt — friss session-höz

> **Hogyan használd:** Nyiss egy ÚJ Cowork sessiont, és illeszd be ezt a teljes promptot egyetlen üzenetként. A session ezután önállóan végigviszi a 4 órás workshop dry-runját.

---

## A prompt (másold be ezt):

```
Te most egy szimulált dry-runt végzel a 4 órás "Ignis Academy Haladó AI Workshop"-on.

A szerep: te egyszerre vagy (1) a STUDENT aki végigcsinálja a workshop feladatait, és (2) a META-EVALUÁTOR aki értékeli az élményt és pontozza a tananyagot.

==== 1. LÉPÉS: KONTEXTUS BEOLVASÁSA ====

Olvasd el SORRENDBEN a következő fájlokat:

1. `CLAUDE.md` (a Haladó/ gyökerében)
2. `Műhely/00_Tervezes/10_DryRun_kontext.md` — EZ A LEGFONTOSABB: ebben van minden további olvasmány-lista, a munkamappa-szabály, és a pontozási kritériumok
3. A `10_DryRun_kontext.md`-ben felsorolt többi kötelező olvasmányt (Tananyag README, Ceg_leiras_TransOffice, Story Book)

Miután ezeket beolvastad, írj egy 5-10 mondatos összefoglalót arról, hogy MIT FOGSZ CSINÁLNI a következő 4 órában — ez a megerősítés, hogy érted a feladatot.

==== 2. LÉPÉS: OKTATÓI SEGÉDLET BEOLVASÁSA ====

Olvasd el a `Műhely/00_Tervezes/09_Oktatoi_segedlet_v1.0.md`-t teljes egészében. Ez a percre lebontott forgatókönyv — ez vezet végig a 6 fázison. Figyelj különösen:
- Az időzítésekre (mely fázis hány perc)
- A "Mondom:" idézetekre (az oktató mondatai)
- A "DEMO" vs "HANDS-ON" arányra (mit csinál az oktató, mit a tanuló)
- Az Appendix A prompt library-re (ezeket a promptokat fogod használni)

Miután ezt elolvastad, írj 5 mondatban: a 6 fázis közül melyik a legkockázatosabb és miért.

==== 3. LÉPÉS: A WORKSHOP VÉGREHAJTÁSA ====

Most játszd el a tanulót. A munkamappád: `TransOfficeCopy/` (a Haladó/ gyökerében — már elő van készítve a nyers fájlokkal).

**SZABÁLYOK:**
- Mindent a `TransOfficeCopy/` mappán belül csinálj — ne piszkold a `Tananyag/` vagy `Műhely/` mappákat
- Hozz létre alfápákat ahogy haladsz: `01_ceg_attekintes/`, `02_meeting_TODO/`, ..., `06_weboldal/`
- TÉNYLEGES OUTPUT-okat generálj minden fázishoz (`.md`, `.docx`, `.html`, `.pptx`, ahogy a feladat kéri)
- A bónusz feladatokat NE csináld meg — csak a fő feladatokat (F1.1-1.2, F2.1-2.2, F3.1-3.3, F4.1-4.3, F5.1-5.3, F6.1-6.2)
- F6.1-nél generálj **3 teljes weboldal-variánst:** Modern (clean B2B kék), Klasszikus (konzervatív, bizalmi), Erdélyi (meleg, helyi karakter). Mindhárom önálló HTML fájl. Mindhárom tartalmazza az AFM elektromos járműflotta projektet.

**MENNYI IDŐT TÖLTS:**
Egy valódi 4 órás workshop nem szimulálható 1-1 ülésben pontosan, de NE rohanj. Minden fázisra szánj annyi időt, hogy a kimenet ne legyen felszínes. Ha 30+ percnyi munkának érzed egy fázist, az OK.

**KÖVESD A SORRENDET:**
F1 → F2 → F3 → F4 → F4 → F5 → F6. A szünetek itt nem relevánsak (nincs valós idő), de figyelj a NARRATÍV CONTINUITÁSRA — egyik fázis outputja a következő input-ja.

==== 4. LÉPÉS: META-JEGYZETEK MENET KÖZBEN ====

Minden fázis VÉGÉN, AZONNAL (mielőtt a következőre mennél), írj egy meta-jegyzetet a fázisról a `TransOfficeCopy/_DryRun_jelentés/jelentes.md` fájlba. A jegyzet tartalmazza:

```
## F[X] — [Fázis neve]

### Mi volt WOW?
[3-5 mondat — az élmény oktatói szemmel: hol esett le a tantusz? Mi adott "hűha" érzést?]

### Mi nem ment olajosan?
[3-5 mondat — technikai csúszás, narratív lyuk, túl bonyolult prompt, gyenge átkötés, etc.]

### Oktató vs. Tanuló munkaaránya
[Becsült %: pl. "Oktató 70% / Tanuló 30%" — mennyit dolgozott a tanuló aktívan?]

### Javítási ötletek
[1-3 konkrét javaslat — mit változtatnál a legközelebbi workshopra]
```

==== 5. LÉPÉS: VÉGSŐ PONTOZÁS ====

A 6 fázis után csinálj egy összesítő pontozást a `TransOfficeCopy/_DryRun_jelentés/pontozas.md`-be. Pontozz **minden fázist** (Bevezető, F1, F2, F3, F4, F5, F6, Zárás) **7 kritérium szerint** 1-10-es skálán:

1. **Érthetőség** — egy résztvevő követheti?
2. **Új információ** — Cowork-spec funkciókból mennyit mutat be?
3. **Hasznosság** — valós üzleti életbe átvihető?
4. **Narratív illeszkedés** — a film-íven hol vagyunk? stimmel?
5. **WOW-faktor** — "hűha" élmény van?
6. **Hands-on érték** — a tanuló tényleg dolgozik vagy csak néz?
7. **Realizmus** — egy valós cégnél így működne?

Formátum: táblázat soronként egy fázissal, 7 oszlopban a pontok + átlag oszlop. A táblázat alatt 3 bekezdés:
- Top 3 erősség
- Top 3 fejlesztendő pont
- Egy mondatos overall vélemény

==== 6. SIKER-KRITÉRIUM ====

A dry-run akkor sikeres ha a végén megtalálható:
- `TransOfficeCopy/01_ceg_attekintes/` (F1 outputjai)
- `TransOfficeCopy/02_meeting_TODO/` (F2 outputjai)
- `TransOfficeCopy/03_palyazati_elemzes/` (F3 outputjai)
- `TransOfficeCopy/04_kommunikacio/` (F4 outputjai)
- `TransOfficeCopy/05_palyazat_csomag/` (F5 outputjai)
- `TransOfficeCopy/06_weboldal/` (**3 db variáns + saját variáns** = 4 fájl)
- `TransOfficeCopy/_DryRun_jelentés/jelentes.md` (meta-jegyzetek)
- `TransOfficeCopy/_DryRun_jelentés/pontozas.md` (pontozás)

==== INDULJ ====

Kezdd az 1. lépéssel. Olvasd el a kontext-fájlokat, és AZUTÁN írd meg az első összefoglalót. Onnantól haladj sorban.

Munkára!
```

---

## Mit készítettünk elő (ezt nem kell a friss session-nek tudnia)

- ✅ `TransOfficeCopy/` mappa (Haladó/ gyökerében) — 34 nyers fájl bemásolva
- ✅ `Műhely/00_Tervezes/10_DryRun_kontext.md` — olvasmány-lista
- ✅ `Műhely/00_Tervezes/09_Oktatoi_segedlet_v1.0.md` — facilitátor forgatókönyv
- ✅ `Műhely/00_Tervezes/11_DryRun_prompt.md` — ez a fájl (a prompt forrása)

## Mit várhatsz outputként a friss session-től

A dry-run után a `TransOfficeCopy/` mappa kb. 25-40 új fájllal gazdagodik:
- 6 fázis outputjai (üzleti dokumentumok)
- 4 weboldal-variáns (3 stílus + a tanuló saját)
- 2 meta-fájl: `_DryRun_jelentés/jelentes.md` + `pontozas.md`

Ezek alapján egyrészt **látod hogy a workshop ténylegesen működik-e**, másrészt **konkrét javítási javaslatokat kapsz**.
