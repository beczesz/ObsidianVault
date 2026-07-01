---
title: "Regio Consult — haladó képzés adaptációs stratégia v0.1"
date: 2026-06-29
author: Becze Szabolcs
status: draft
version: 0.1
description: "Gondolati keret arra, hogyan adaptáljuk az Ignis haladó (TransOffice) workshopot a Regio Consult EU pályázati tanácsadó cégre. A bevált pedagógiát megtartjuk, a narratív keretet eltoljuk (pályázó KKV helyett tanácsadó-portfólió), a 6 fázist a Regio 3 fő fájdalmára húzzuk rá (szkennelt PDF kiolvasás, Excel-templét + skill, CLAUDE.md szabálykönyv a strukturált rendszer fölé). Nyitott kérdések, függőségek, logisztikai kockázatok."
id: 38a6f349-8821-4564-a90f-d156423c181e
index_schema_version: 1
bdos_index: true
tags: [ignis-academy, kepzes, halado, regio-consult, adaptacio, strategia, draft]
---

# Regio Consult — haladó képzés adaptációs stratégia (v0.1)

> Input: [[00_meeting_alap_2026-06-29]] (igényfelmérő meeting) + az eredeti workshop (`../original/`, kiemelten a Story Book és a `17_Eles_visszajelzes_elemzes_2026-05.md`).
> Ez **gondolkodás, nem kész terv.** A konkrét tananyag a follow-up fájlok (2 PDF, internet sztandárd, templét-hármas) megérkezése után épül.

## 0. A kulcs-belátás: keret-eltolás

Az eredeti workshop narratívája: **„Te vagy egy kaotikus KKV (TransOffice) Operations Managere, aki pályázatot ad be."** A pályázó szerepében ülsz, a káoszt rendezed, a végén beadsz EGY pályázatot.

A Regio **nem pályázó** — ő a **tanácsadó**, aki **20+ ügyfél** pályázati életciklusát viszi egyszerre, **erősen sztenderdizált** mappastruktúrában, sok **ismétlődő** dokumentum-/Excel-/elszámolás-munkával. A fájdalmuk nem „rendet rakni a káoszban" (náluk épp hogy erős struktúra van), hanem **a strukturált rendszerükben végzett repetitív szakmunka felgyorsítása**.

Tehát: **a pedagógiát megtartjuk, a sztorit és a fájdalom-tengelyt kicseréljük.**

## 1. Amit MEGTARTUNK (bizonyított, ne nyúljunk hozzá)

Az első HBC-kohorsz (n=14) mérése: össz-elégedettség 4,71/5, **100% ajánlaná**, 11/14 „felülmúlta". Ami működött:

- **Narrated Live Experience** — történet-vezérelt, 70% élő demo / 20% micro hands-on / 10% szabad. A Regio kapcsolattartó is ezt erősítette: „ne csak ledaráld", legyen szabad kérdezz-felelek is.
- **Történet mint felfűző-fonál.** Szabolcs a meetingen is kimondta: a sztorira fűzöd fel az eszközöket, mert úgy könnyebb figyelni.
- **WOW + MICRO checkpoint** ritmus fázisonként.
- **Instruktor-vezetett + stáció-modell** (v2.5), copy-paste promptok kódblokkban.
- **Történelmi párhuzam-keret** (eszterga/gőzgép → Cowork) a nyitányban.

## 2. Amit MÓDOSÍTUNK — közönség-kalibráció

| Dimenzió | Eredeti (HBC) | Regio Consult |
|---|---|---|
| Kik | 10-15 fő, „hallottak az AI-ról, nem használják" | **21 fő**, pályázati szakértők, OneDrive-on, „cseppként" már használják AI-t |
| Domain-tudás | laikus | **magas** (deviz, anexa, elszámolás, SEAP) — ne tanítsuk a szakmájukat |
| AI-érettség | nulla | alap-prompt szint; a kapcsolattartó a **Mester** képzésen járt (a haladón NEM) |
| Struktúra | káosz | **erősen strukturált, tudatos sztenderd** — ezt erősségként kezeljük |

**Következmény:** a „mi az AI" rész rövidülhet; a hangsúly a **saját strukturált rendszerükre ültetett** konkrét eszköz-készségen van. De vigyázat: a csapat zöme NEM járt Mesteren, tehát az alapokat (Cowork, fájlrendszer, markdown, skill) tényleg az alapokról kell.

## 3. A 3 fájdalom → tananyag-tengely (Haladó scope-ban)

Szabolcs kerete: **alapok + eszközök**, hogy maguk automatizálják magukat. **Agentet NEM építünk** (az Mester). A 3 fájdalom sorrendje a meetingből:

1. **Szkennelt PDF → használható adat** (legnehezebb). Tananyagi szerepe: **reality-check + technika.** Megtanítjuk a *vektoros vs. szkennelt (kép) PDF* különbséget, az OCR korlátait, hogyan szerezzenek Excel-exportot, hogyan nyerjünk ki táblát abból, ami kinyerhető. Őszinte elvárás-kezelés: a 300 MB-os, 353 oldalas szkennelt deviz az AI-nak ma is nehéz — ezt nem ígérjük túl. Ez maga egy **WOW-kontraszt**: „ezt tudja / ezt nem (még)".
2. **Excel-templét + skill** (legáltalánosabb) → **ez a workshop killer-demója.** Szabolcs saját ötlete: *üres templét + kitöltött példa + forrás-Excel* hármasból egy **skill**, ami felismeri az Excel struktúráját és kevés inputból kitölti. Pontosan az ő statisztika-skilljének mintája. Ide kötjük: mi a skill, hogyan írj skillt, Excelből skill-hívás, csapaton belüli megosztás/verziózás (Team plan).
3. **Pályázatépítés** (legkevésbé sürgős, ~10% az aktivitásuk, már profik) → **csak könnyű érintés.** Nem kezdünk innen (a kapcsolattartó kifejezetten ezt akarta elkerülni). Esetleg záró bónusz: jól promptolt pályázat-vázlat a kiírásból.

## 4. Fázis-remap: eredeti 6 felvonás → Regio-verzió

| Eredeti | Eredeti lényeg | Regio-adaptáció |
|---|---|---|
| **F1 Káoszból rend** | 27 kaotikus fájl → struktúra + CLAUDE.md | **„Tanítsd be az AI-t, mint egy új junior kollégát."** Nem rendet rakunk (náluk van), hanem a **meglévő strukturált rendszert írjuk le markdownban**: gyökér-CLAUDE.md + projekt-szintű, egymásba ágyazott CLAUDE.md-k („kalandkönyv"-navigáció). **Párhuzamos** mappa, a jelenlegit nem bolygatja. Ez 1:1 Szabolcs meeting-víziója. |
| **F2 Meeting → TODO** | transcript → mentett TODO-k | Megtartható könnyű demóként (ez a saját rögzítésünk is bizonyítja), de nem központi. Vagy: belső sztandárd-szabály → markdown szabály demonstrálása. |
| **F3 Adatvadászat (94 old. kiírás)** | eligibility + gap-analysis | **Áthúzva az 1. fájdalomra: szkennelt PDF reality-check.** Mit tudunk kinyerni egy valódi (anonim) Regio kiírásból/devizből; vektoros export-útvonal. |
| **F4 Kommunikáció + Excel-elemzés** | EBITDA Excel-elemzés, cross-doc | **Deviz / centralizátor Excel-munka.** Ajánlatkérés vs. ajánlat tételes összevetése (amennyire a forrás engedi); statisztika/összesítő számolás Excelből. |
| **F5 Összeállítás + form-autofill** | submission package, MySMIS autofill | **A killer-demo helye: Excel-templét kitöltő skill.** A form-autofill „WOW" → templét-kitöltés „WOW". |
| **F6 Web redesign** | régi weboldal → új HTML | **Kivágjuk** (irreleváns). Helyette: **PDF-/dokumentum-generálás a saját sztenderdjükben** (pl. számla ledolgozott órákból, vagy sztenderd-konform dokumentum lektorálása). |

**Új modul (nincs az eredetiben, de Szabolcs kötelezőnek jelölte):**
- **Skill-írás 101** — mi a skill, hogyan írj/használj, Excelből hívás, csapat-megosztás + verziózás.
- **Microsoft 365 / OneDrive integráció** — hogyan fut a Cowork a lokális fájlrendszeren és köti össze a OneDrive-os közös struktúrával.

## 5. Javasolt új „sandbox" (a TransOffice helyett)

Két út:
- **(A) Anonimizált valódi mini-portfólió** — 2-3 minta Regio-projekt (pl. „tejgyár", „kastély-felújítás" — a meetingben említett Terézia/Kánoki típusok **kitalált, nem azonosítható** változata) a Regio strukturált rendszerében, a kapott templét-hármassal és a 2 minta-PDF-fel. **Előny:** azonnal a saját világuk; Szabolcs kimondta, hogy a struktúrájukat letükrözi.
- **(B) Teljesen fiktív tanácsadó-cég** („Regia Consult"-szerű) — tisztább IP-jog, de kevésbé otthonos.

**Ajánlás:** (A), de **anonimizálva** — valódi ügyfél-/cégnevek, CUI, összegek nélkül. (Adatvédelmi/DNA-érzékenység: a kapcsolattartó maga jelezte, hogy a beérkező dokumentumokkal óvatosnak kell lenni.)

## 6. Amit KIVÁGUNK / visszaveszünk

- **F6 web-redesign** — nincs köze a Regióhoz.
- **Mély agent-építés** — Haladó, nem Mester. (Megemlítjük, hogy *érdemes lenne* agentet írni a strukturált rendszerre — indexelő + lektor agent —, de nem építjük meg.)
- **Pályázatírás mint nyitány** — a kapcsolattartó kifejezetten ezt akarta elkerülni.

## 7. Nyitott kérdések / döntésre vár

1. **Sandbox (A) vagy (B)?** (ajánlás: A, anonimizálva)
2. **21 fő — logisztikai kockázat.** Az éles visszajelzés P2-je: 10-12 fő a komfort, 15 felett co-facilitator. 21 fő egyetlen oktatóval, hands-on stációkkal **feszes**. Kell-e co-facilitator vagy páros-mód (v2.3) szigorúan?
3. **Net-infra (P0 az eredeti feedbackből).** 21 ember egyszerre üti a Coworköt + nagy fájlok → előzetes wifi-teszt kötelező.
4. **Mennyit ígérünk a szkennelt PDF-re?** Reality-check kell, hogy ne csalódjanak az 1. (legfontosabb) fájdalmukban.
5. **A killer-demo (Excel-skill) mennyire generikus?** Egy templét-hármason épül — ha túl Regio-specifikus, nehéz 4 órába tenni; ha túl absztrakt, nem „kattan be".

## 8. Függőségek (mielőtt a tananyag épül)

A Regio küldi (follow-up a meetingből):
- [ ] 2 minta-PDF (ajánlatkérés + ajánlat, szkennelt) → 3. fázis (PDF reality-check)
- [ ] belső „internet sztandárd" dokumentum → F1 (CLAUDE.md szabálykönyv)
- [ ] templét-hármas (üres + kitöltött + forrás Excel) → F5 (killer-demo)

Ezek nélkül a fázis-tartalom csak vázlat marad. Amint megjönnek: mintázat-kinyerés → atomizált, „becsattanó" feladatok (Szabolcs meeting-ígérete).

## 9. Logisztika (a meetingből, fix)

- **Csütörtök**, 11:00 kezdés (érkezés 10:30-11:00), **12:30 brunch-szünet**, oktató 17:00-ig elérhető. Helyszín helyben (keresztúri).
- **Team plan** (~534 €/hó, 21 seat) — a Regio holnap reggel veszi; egyben, hogy a **skillek megoszthatók** legyenek.
