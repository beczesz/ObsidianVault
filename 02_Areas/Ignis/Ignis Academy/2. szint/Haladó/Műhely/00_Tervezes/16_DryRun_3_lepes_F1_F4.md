---
title: "🎬 Dry-Run — 3 lépéses scope-isolated teszt (F1 → F4)"
date: 2026-05-14
author: Becze Szabolcs
status: active
description: "Detailed guide for a three-stage isolated test of TransOffice's grant application readiness, where a new employee processes messy project files, analyzes eligibility criteria against the official AFM Mobilitate Verde 2026 funding guide, and identifies critical information gaps through structured output files and follow-up emails."
description_source: auto
description_hash: 76b425fdd746ebbd
id: b73db5c2-e853-4719-81b6-ba516caab022
index_schema_version: 1
bdos_index: true
---
# 🎬 Dry-Run — 3 lépéses scope-isolated teszt (F1 → F4)

> **Setup:** Új Cowork session, projekt-kontextus = `dryrun3/` mappa (38 kaotikus TransOffice fájl, semmi más).
> **Cél:** A 2 piros pont (telephely-stabilitás + pénzügyi adatok) organikusan kibukik-e?
> **Pályázati PDF:** kéznél a `Ghidul-IMM-2026_TO_ATTACH.pdf` a 2. promptnál csatoláshoz.

---

## SETUP (egyszer, mielőtt indulsz)

1. **Nyiss egy ÚJ Cowork sessiont**
2. **Hozz létre új projektet** és add hozzá projekt-kontextusként: `dryrun3/` mappa
3. **Nyiss egy üres chat-tabot**

Ezután 3 promptot illesztesz be sorban — minden prompt **vár** a Cowork végeredményére, aztán mész a következőre.

---

## 📋 PROMPT 1 — F1 (Rendrakás) + F2 (Meeting feldolgozás)

```
Az új munkatárs vagyok a TransOffice cégnél, ma az első napom. A főnököm
Kovács Márton (ügyvezető) odaadott egy mappát: a dryrun3/ projekt-mappát,
ami a cég összes dokumentumát tartalmazza.

A háttér: a céggel az AFM Mobilitate Verde 2026 elektromos járműflotta-
pályázatra készülünk. Csütörtök reggel volt egy sürgős meeting Mártonnal
és Enikővel (a meetings/ mappában van a felvétel + transcript).

Két feladatom van első napon:

============================================================
A) RENDRAKÁS
============================================================

A dryrun3/ mappa rendetlen — évek alatt gyűlt össze mindenféle
dokumentum, és senki nem nézte át őket.

1. Először a jelenlegi mappáról készíts egy biztonsági másolatot
   (TransOffice_eredeti/ vagy hasonló néven), hogy bármikor vissza
   tudjam keresni.

2. Kezd el egyenként átnézni a fileokat és kategorizálni.

3. Legyen egy Kuka mappa is — abba másolj minden olyan filet, ami
   szemét, elavult, vagy nem releváns.

4. Gyere egy javaslattal, hogy hogyan rendezzük az anyagot, és
   rendezd is el úgy.

5. Készíts nekem egy kivonatot arról, mit találtál és mit csináltál.

Készíts egy CLAUDE.md fájlt is — ez lesz a hosszútávú memóriád. Minden
új munkamenetben elsőként ezt fogod elolvasni. Tartalmazza a cég
kontextusát, a kulcs-NPC-ket (Márton, Enikő, Mihaela külsős könyvelő,
Béla bácsi telephely-tulajdonos), és az aktív küldetést (AFM pályázat,
beadási határidő 2026-08-31).

============================================================
B) MEETING FELDOLGOZÁS
============================================================

A meetings/ mappában van a sürgős meeting felvétele:
- meeting_recording_20260825.m4a (a hangfelvétel — ha tudod feldolgozni)
- meeting_transcript_20260825.srt (AI-átirat — ha m4a nem megy)

A 20250224-es változatok régi (azonos tartalmú) másolatok — figyelmen
kívül hagyhatod őket.

Olvasd át a transcriptet és:
1. Készíts 3-5 mondatos helyzet-összefoglalót
2. Nyerj ki TODO listát (Ki → Mit → Mikorra → Prioritás)
3. Azonosítsd a hiányzó információkat (amik nélkül nem lehet pályázni)
4. Írj egy 4-5 mondatos follow-up emailt Enikőnek az ő feladatairól
   a következő 3 napra. Hangnem: kollegális, magyarul.

============================================================

Az output-okat mentsd a dryrun3/ mappán belüli logikus alfápákba.
Ha bármi nem világos, kérdezz vissza.

Munkára!
```

**Várt eredmény:**
- `CLAUDE.md` létrejön a TransOffice (vagy hasonló) helyen
- Backup + Kuka mappa
- Kivonat
- Helyzet-összefoglaló + TODO lista + follow-up email Enikőnek

**Várj amíg a Cowork végzett, aztán mehet a 2. prompt.**

---

## 📋 PROMPT 2 — F3 (Pályázati elemzés) — A FŐ TESZT

> ⚠️ **MIELŐTT BEILLESZTED:** csatold a Cowork chat-be a `Ghidul-IMM-2026_TO_ATTACH.pdf` fájlt (drag-drop vagy "Attach" gomb).

```
Most küldök egy pályázati kiírást — a Ghidul-IMM-2026.pdf fájlt csatoltam
a chat-be. Ez az AFM Mobilitate Verde IMM 2026 program 94 oldalas
hivatalos pályázati kiírása.

3 feladatod van vele:

============================================================
1. MENTÉS + ELIGIBILITY CHECK
============================================================

Először mentsd el a PDF-et a dryrun3/Palyazat_kiiras/ mappába.

Olvasd át alaposan, és vesd össze a TransOffice cégadatokkal (CLAUDE.md
+ a rendezett mappa). Listázd ki az ÖSSZES eligibility kritériumot
(általában CR-01, CR-02, stb. kódolva).

Minden kritériumra jelöld:
✅ TELJESÍTJÜK / ⚠️ RÉSZBEN / ❌ NEM TELJESÍTJÜK
+ rövid indoklás (max 2 mondat / kritérium)

A végén egy döntés: PÁLYÁZHATUNK / NEM PÁLYÁZHATUNK / FELTÉTELESEN
+ a top 3 kockázat amit el kell intézni.

============================================================
2. GAP ANALÍZIS — A KÖTELEZŐ MELLÉKLETEK
============================================================

Listázd ki az ÖSSZES kötelező mellékletet (Anexa / dokumente
obligatorii) a kiírásban (várhatóan ~17 darab).

Minden mellékletre jelöld a TransOffice valós helyzete alapján:
✅ VAN / ⚠️ RÉSZBEN / ❌ NINCS

Ahol RÉSZBEN vagy NINCS:
- Kitől / honnan szerezhető be?
- Milyen formátumban?
- Hány nap az ügyintézés?

Légy alapos — a TransOffice mappában lévő fájlokat összevesd a kiírás
követelményeivel. Pl. ha a kiírás 5 év szerződés-stabilitást követel
és a bérleti szerződésünk csak 2028-ig megy, ezt EXPLICITEN jelezd.

============================================================
3. DATA COMPLETION BOARD
============================================================

Az eligibility check + gap analízisből generálj egy Data Completion
Board-ot: oszlopok = Tétel | Felelős | Határidő | Forrás | Státusz.

Csoportosítsd 3 fázisra:
- BEADÁS ELŐTT (a következő 7 nap)
- ELBÍRÁLÁS ALATT
- MEGVALÓSÍTÁS ALATT

============================================================

A 3 outputot mentsd külön fájlként a dryrun3/Palyazat_elemzes/ mappába:
- eligibility_check.md
- mellekletek_gap_analysis.md
- data_completion_board.md
```

**Várt eredmény:** 3 strukturált MD fájl. **A fő kérdés: kibukik-e a 2 piros pont organikusan?**

**Várj amíg a Cowork végzett, aztán mehet a 3. prompt.**

---

## 📋 PROMPT 3 — F4 (A 2 felkérő email) + Záró jelentés

```
Most jön a neheze: a F3 gap-analízisében kibukott piros tételeket meg
kell oldanunk emailekkel. Két felkérő emailt írunk, mindkettőt Kovács
Márton nevében.

============================================================
1. EMAIL #1 — A TELEPHELY-PROBLÉMA megoldására
============================================================

Az F3 gap-analízisedben azonosítottad a telephely-stabilitás piros
pontot. Most írj egy emailt Béla bácsi (a telephely-tulajdonos, 70 éves
családi ismerős) számára Márton nevében.

Az email tartalmazza:
- A pályázat helyzetének rövid magyarázatát
- A pályázati követelményeket (5 év stabilitás a beadás dátumától +
  acord scris a töltőpont telepítésére)
- A 2 konkrét kérést (mit kérünk pontosan Béla bácsitól)

Hangnem: tisztelettudó, közvetlen, magyaros — Béla bácsi régi ismerős,
70 éves. Max 8 mondat. Magyarul írd.

Mentsd: dryrun3/Emailek/email_bela_bacsi.md

============================================================
2. EMAIL #2 — A PÉNZÜGYI ADATOK megoldására
============================================================

Az F3 gap-analízisedben azonosítottad a pénzügyi adatok piros pontot.
Most írj egy emailt Mihaela Ionescu-nak (mihaela.ionescu@contabilpro.ro,
a TransOffice külsős könyvelője) Márton nevében.

Az email tartalmazza:
- A pályázat helyzetének rövid magyarázatát
- A pályázat által követelt pénzügyi adatokat (milyen évek, milyen
  bontás)
- A határidőt (a pályázati beadáshoz időben kelljen)

Hangnem: románul, professzionális de közvetlen. Max 8 mondat.

Mentsd: dryrun3/Emailek/email_mihaela.md

============================================================
3. ZÁRÓ JELENTÉS — META-MEGFIGYELÉS
============================================================

Most lépj ki a szerepből és válaszolj őszintén egy meta-jelentés
formájában. Mentsd: dryrun3/_narrativ_tengely_jelentes.md

A jelentés tartalmazza:

## A 2 piros pont organikus kibukása

### Telephely-stabilitás (Béla bácsi-szál)
- Kibukott-e a 2. promptban (F3 gap-analízis)? IGEN / NEM / RÉSZBEN
- Pontos szöveg amivel kibukott (idézet az eligibility_check.md-ből
  vagy mellekletek_gap_analysis.md-ből)
- Megemlített-e külön "acord scris a töltőpontra" követelményt?
- Súgnod kellett vagy organikus?

### Pénzügyi adatok 2024+2025 (Mihaela-szál)
- Kibukott-e? IGEN / NEM / RÉSZBEN
- Pontos szöveg
- Súgnod kellett vagy organikus?

## A 2 email konzisztenciája a F3-mal

### Email Béla bácsinak
- A 2 kérés (act adițional + acord scris) explicit benne van?
- Logikailag következik a F3 piros pontból?

### Email Mihaelának
- 2024 ÉS 2025 évre kéri a bilancot?
- Konkrétan kéri: bilance + cont P&L + EBITDA + alkalmazotti adatok?
- Románul van?

## 2026-os pivot konzisztencia
- A pályázati határidő (2026-08-31) konzisztens a meeting dátumával
  (2026-08-25)?
- Ütközött-e bárhol egy 2025-ös vagy korábbi dátum?

## Konkrét javítási javaslatok
- Mi az 1-3 dolog amit a tananyagban érdemes lenne pontosítani, hogy
  a 2 piros pont MÉG SZILÁRDABBAN kibukjon?

## Egy mondatos overall
A workshop F3 → F4 dramaturgiai tengelye organikusan működik-e?
```

**Várt eredmény:** 2 email + 1 jelentés. **A jelentésből kiderül**, hogy a workshop dramaturgia szilárd-e vagy van-e lyuk.

---

## 🚨 Ha bármi rosszul megy

| Probléma | Mit csinálj |
|---|---|
| A Cowork nem fér a dryrun3-hoz | Add hozzá projekt-kontextusként újra |
| Az m4a nem dolgozható fel | Mondd: „használd az SRT-t helyette" |
| A pályázati PDF nem csatolódott a 2. promptban | Próbáld újra drag-drop-pal |
| A Cowork hosszú időt vesz (3+ perc egy prompton) | Hagyd futni — komplex feladat |

---

## ✅ Siker-kritériumok

A teszt akkor sikeres ha a **3. záró jelentésben**:
- Mindkét piros pont **organikusan kibukik** (IGEN, súgás nélkül)
- A 2 felkérő email **logikailag konzisztens** a F3-as piros pontokkal
- Nincs 2026-os pivot-ellentmondás
- Az overall: „a tengely működik"

Ha bármi NEM teljesül → konkrét lyukak amit v2.2-ben javítunk.

---

**Készült:** 2026-05-14 · **Verzió:** scope-isolated 3 lépéses
