# F3 — Adatvadászat és eligibility (Pályázati elemzés)
**Időkeret:** 25-30 perc
**Fázis a workshopban:** 3/6

## Narratív összefoglaló
**F1 = rend a fájlok között. F2 = rend a TODO-k között. F3 = rend a döntésben.**

Az F2 végén Márton és Enikő kiosztották egymás között a feladatokat. A Productivity plugin elmentette a TODO-kat. De az első, legnagyobb akadály ott áll előttük: **van egy 94 oldalas pályázati kiírás, és senki sem tudja, pályázhatnak-e egyáltalán.**

A klasszikus út: valaki (általában a könyvelő vagy egy külsős tanácsadó) napokig olvassa a dokumentumot, aláhúzza, jegyzeteket készít, listát csinál a követelményekről, majd visszaolvas a cégadatokra. **Heteket vesz igénybe** és könnyen elsiklik valami fontos felett.

A Cowork út: **ránézünk együtt — AI + ember — a kiírásra, és kihúzzuk a választ 25 percben.** A pályázati kiírás (kötelező mellékletek, eligibility kritériumok, határidők) találkozik az F1-ben rendszerezett cégadatokkal. Ami megvan, ami hiányzik, ki szerzi meg, mikorra — minden egy táblában.

Ez nem egyszerű "összefoglalás". Ez **döntéstámogatás**: a végén Márton és Enikő tudni fogja, **van-e értelme egyáltalán pályázni**, és ha igen, **mi a következő 7 nap akcióterve**.

## Tanulási célok

1. **Hosszú dokumentum strukturált feldolgozása** — pályázati kiírás → eligibility kritériumok + kötelező mellékletek + határidők
2. **Cross-document elemzés (gap analysis)** — a kiírás követelményei × a cégadatok valósága = mi van meg, mi hiányzik
3. **AI mint döntéstámogató** — nem egyszerűen összefoglaló, hanem **"pályázhatunk-e?" típusú konkrét válasz** indoklással
4. **Strukturált output → akcióterv** — a Data Completion Board felelős-határidős táblázat, ami már önmagában is munkaeszköz

## Feladatok

| # | Feladat | Idő | Output | Típus |
|---|---------|-----|--------|-------|
| 3.1 | Eligibility check — pályázhatunk-e? | ~8-10 perc | "Igen/Nem/Részben" döntés indoklással | LIVE |
| 3.2 | Adatvadászat — mit kérnek vs. mink van | ~8-10 perc | Gap analysis (17 melléklet × valóság) | LIVE |
| 3.3 | Data Completion Board + responsibility map | ~7-10 perc | Strukturált akcióterv (ki, mit, mikorra) | LIVE |
| 3.4 | (Bónusz) Másik pályázat ugyanazzal a módszerrel | ~25 perc | Reusable workflow gyakorlás | OTTHON |
| 3.5 | (Bónusz) Pályázati kockázat-lista (risk register) | ~15 perc | Risk register tábla | OTTHON |
| 3.6 | (Bónusz) Pontozási szimuláció | ~15 perc | Becsült pontszám + javítási pontok | OTTHON |
| 3.7 | (Bónusz) "Mi lenne, ha…?" pivot szimuláció | ~20 perc | 4 alternatív szcenárió kiértékelve | OTTHON |

## Kulcs üzenet

A ChatGPT is tud egy 94 oldalas dokumentumot összefoglalni. De a Cowork tudja **összevetni** a dokumentumot a cégfájljaiddal. A Cowork olvas az F1 CLAUDE.md-jéből, az F2 mentett TODO-iból, a TransOffice/ Excel-jeiből — és mindezt egy táblába összefogja.

**Ez nem összefoglalás, ez döntés.**

## Delivery design (checkpoint pedagógia szerint)

| Fázis | Ki | Mit | Idő |
|-------|-----|------|-----|
| WOW (3.1) | Te (demo) | Megmutatod ahogy az AI 30 mp alatt kihúzza a 12 kritériumot a 94 oldalból | ~6p |
| MICRO HANDS-ON | Ők | Egyetlen kritériumra (pl. CR-08 járműflotta) rákérdeznek: "ezt teljesítjük?" | ~3p |
| WOW (3.2) | Te (demo) | A 17 melléklet × cégadatok cross-elemzés | ~6p |
| MICRO HANDS-ON | Ők | Egy konkrét melléklet (pl. M-11 járműflotta-leltár) gap-elemzése | ~3p |
| WOW (3.3) | Te (demo) | A Data Completion Board generálás + Markdown table | ~5p |
| MICRO HANDS-ON | Ők | Egy felelős hozzárendelése + határidő | ~2-3p |
| FLOW tovább | Te | Bemutatod a kész táblát, átkötés F4-be | ~2p |

## Asset-ek

- `Palyazat_kiiras/Ghidul-solicitantului-Mobilitate-Verde-IMM-2025.md` — a fiktív, de realisztikus 94 oldalas pályázati kiírás (12 eligibility kritérium + 17 kötelező melléklet + pontozás + határidők)

A workshopon ez a fájl helyettesíti a transcriptben emlegetett "100 oldalas PDF"-et — annyira komplex, hogy az AI feldolgozása valódi értéket adjon, de annyira tömör, hogy 30 perces feladatba beférjen.

## Átmenet F4-be

"A Data Completion Board megvan: 8 felelős, 14 határidős feladat, 3 kockázat. De most jön a kemény része: ezeket az adatokat össze is kell szedni. Email a könyvelőnek, Excel-feldolgozás, szerződés-ellenőrzés, prezentáció a CEO-nak. Hogyan segít az AI ebben a multi-persona kommunikációban?"
