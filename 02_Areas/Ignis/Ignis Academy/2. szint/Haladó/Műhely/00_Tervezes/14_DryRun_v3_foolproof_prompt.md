---
title: "🎬 Dry-Run v3.0 — Foolproof copy-paste teszt"
date: 2026-05-14
author: Becze Szabolcs
status: active
description: "Szigorú szimulációs teszt, amely ellenőrzi hogy a workshop minden kötelező feladata (F1-F6 stációk) kizárólag copy-paste promptokkal, improvizáció nélkül elvégezhető-e. Oktatók és workshopfejlesztők részére az akadályok és hiányosságok azonosítására."
description_source: auto
description_hash: 6432205d25fc42b4
id: 7ead68cb-08fc-422a-9a5a-4a7c8925be81
index_schema_version: 1
bdos_index: true
---
# 🎬 Dry-Run v3.0 — Foolproof copy-paste teszt

> **Cél:** Egy valódi résztvevő szigorú szimulációja. **A Cowork csak a TransOfficeCopy_v3/ mappához fér** — a tanuló a Tananyag/Feladat fájlokat csak Obsidian-ban olvassa, és **CSAK a megadott prompt-okat másolja át**.
> **Mit tesztelünk:** valóban végig lehet-e vinni a workshop minden kötelező feladatát (F1 + minden STÁCIÓ) **kizárólag copy-paste-tel**, improvizáció nélkül?

---

## A prompt (másold be egy ÚJ Cowork session-be):

```
Te most egy szigorú dry-runt végzel: játszd el egy átlagos workshop-
résztvevő szerepét, aki ELŐSZÖR találkozik a Cowork-kel és **CSAK a
feladat-fájlokban található promptokat** képes copy-paste-elni.

Nem improvizálsz. Nem hozol létre saját promptokat. **Ha egy feladat
nem tartalmaz pontos prompt-ot, jelezd hogy "ITT NEM TUDOK TOVÁBB
HALADNI COPY-PASTE-TEL".**

==== HOZZÁFÉRÉSI MODELL ====

Cowork hozzáférés (csak ehhez nyúlhatsz fájlrendszer szinten):
- `TransOfficeCopy_v3/` mappa (a Haladó/ gyökerében)

Read-only "Obsidian-szimuláció" (csak olvasod a fájlokat hogy
extraháld a copy-paste promptokat):
- `Tananyag/01_Ceg_megertes/Feladat_1.1.md` (F1 stáció)
- `Tananyag/02_Meeting_Productivity/Feladat_2.2_Followup_es_action_items.md` (Stáció 2.A)
- `Tananyag/03_Dontes_Elemzes/Feladat_3.1_Eligibility_check.md` (Stáció 3.A)
- `Tananyag/03_Dontes_Elemzes/Feladat_3.2_Adatvadaszat.md` (Stáció 3.B)
- `Tananyag/04_Legal_Szerzodes/Feladat_4.1_Legal_szerzodes_check.md` (Stáció 4.A)
- `Tananyag/04_Legal_Szerzodes/Feladat_4.2_Penzugyi_email_Excel.md` (Stáció 4.B)
- `Tananyag/05_Kommunikacio_Email/Feladat_5.1_Uzleti_terv.md` (Stáció 5.A)
- `Tananyag/05_Kommunikacio_Email/Feladat_5.2_Palyazati_csomag.md` (Stáció 5.B)
- `Tananyag/06_Marketing_Honlap/Feladat_6.1_Redesign_es_variaciok.md` (Stáció 6)

NEM nyúlhatsz:
- Műhely/ (az oktatói segédlet — ezt egy résztvevő nem látja)
- Tananyag/ a DEMO-fájlok (F2.1, F3.3, F4.3, F5.3) — ezek az oktatóé
- Tananyag/-ban bónusz fájlok — opcionálisak, NEM kötelezőek
- Pelda_outputok/ — a résztvevő nem látja

==== A TESZT FOLYAMAT ====

Minden fázisban (F1 → F2 → F3 → F4 → F5 → F6):

1. **Nyisd meg a Feladat-fájlt** (read-only "Obsidian"-szimuláció)
2. **Találd meg a `## A stáció prompt` vagy `### 2. lépés — Másold be...`
   szekciót** és a benne lévő kódblokkot
3. **Másold ki PONTOSAN** a kódblokk tartalmát (literally, nem
   parafrazálva, nem javítva)
4. **Futtasd a saját Cowork-eden** (a TransOfficeCopy_v3/ mappán)
5. **Mentsd el az outputot** TransOfficeCopy_v3/-on belül egy logikus
   helyre (pl. 01_ceg_attekintes/, 02_meeting/, stb.)

==== AMIT MEG KELL FIGYELNED ====

Minden fázis után jegyezd fel a `TransOfficeCopy_v3/_DryRun_v3_jelentes/
jelentes.md` fájlba:

## F[X] — [Fázis neve]

### Megtalálhattam a copy-paste promptot?
- IGEN — a `[szekció név]` szekcióban, kódblokkban
- NEM — magyarázd: mi hiányzott?

### A prompt működött elsőre?
- IGEN — pontos kimenet
- RÉSZBEN — kellettek finomítások (de NEM csináltad meg, csak megjegyzed)
- NEM — hiba történt (magyarázd)

### Improvizációra szorultam?
- Soha (✅ foolproof)
- Egy-két döntésnél (pl. fájlnév-választás) — sárga
- Sokszor — piros (NEM foolproof)

### Konkrét akadások
[Bármi amibe egy első-felhasználó beleakadhatna]

### Output ténylegesen létrejött?
- IGEN: [fájl-útvonal]
- NEM: miért?

==== ÖSSZESÍTŐ ÉRTÉKELÉS ====

A 6 fázis után készíts összefoglalót: `TransOfficeCopy_v3/
_DryRun_v3_jelentes/foolproof_pontozas.md`

Tartalmazza:

| Fázis | Copy-paste alapján kivihető? (Igen/Részben/Nem) | Improvizáció szükséges (0-10, 0=nincs) | Akadások száma | Megjegyzés |
|-------|---|---|---|---|
| F1 | | | | |
| F2 STÁCIÓ | | | | |
| F3 STÁCIÓ 3.A | | | | |
| F3 STÁCIÓ 3.B | | | | |
| F4 STÁCIÓ 4.A | | | | |
| F4 STÁCIÓ 4.B | | | | |
| F5 STÁCIÓ 5.A | | | | |
| F5 STÁCIÓ 5.B | | | | |
| F6 STÁCIÓ | | | | |

A végén:
- **Foolproof-pontszám:** X/10 (1 = több mint a fele csúnyán törik,
  10 = minden zökkenőmentes)
- **Top 3 hiba/akadás** amit javítani kell v2.1-ben
- **1 mondat overall:** valóban foolproof-e?

==== EXTRA: az m4a felvétel kezelése ====

A `meeting_recording_20260825.m4a` (a tényleges hangfelvétel) +
a `meeting_transcript_20260825.srt` (AI-generált átirat) **mindkettő**
ott van a TransOfficeCopy_v3/meetings/-ben.

Ha az F2 stáció prompt a Cowork-ben (a CLAUDE.md-ből visszanéz a
látott TODO-listára) — ellenőrizd hogy:
- Az F2-höz a Cowork miért tudja MILYEN TODO-k voltak ha sose látta őket?
  (Ezt a tanuló nem dolgozta fel — csak az oktató mutatta a kivetítőn.)
- A megoldás vagy: a Cowork ténylegesen feldolgozza az SRT-t / m4a-t
  ELŐSZÖR (akkor a prompt elhalvány)
- Vagy: a Feladat hibás (feltételezi hogy a Cowork "látta a TODO-kat"
  amit nem)

Ez egy fontos diagnosztika.

==== INDULJ ====

Kezdj el F1-gyel. Légy szigorú — minden esetben jelezd ha **improvizációra
szorulnál** (de TE NE improvizálj). A cél: őszinte tükör arról hogy egy
átlag résztvevő el tudja-e végezni copy-paste-tel.

Munkára!
```

---

## Mit várunk ettől a teszttől

**A v2.0 már tesztelte** hogy a workshop élménye jó-e (8,5/10 átlag pontszám). **De NEM tesztelte** azt hogy egy átlag-felhasználó CSAK a copy-paste promptokat használva el tud-e jutni a végéig.

A v3.0 ezt teszteli:
- ✅ Minden stáció pontos prompttal érkezik-e?
- ⚠️ Az F2 stáció (follow-up email Enikőnek) függ-e a látott TODO-listától? Ha igen, **ez egy lyuk** — a Cowork nem látott TODO-listát, csak a tanuló látta az oktatótól.
- ⚠️ Az F4 stációk (Béla bácsi válasz, EBITDA) függnek-e az oktatói DEMO előzményétől? Pl. a Béla bácsi-válasz stáció feltételezi hogy a tanuló látta az emailt.

**Várt eredmény:** a foolproof-pontszám 7-9 körül lesz, és lesz 2-3 konkrét lyuk amit v2.1-ben javítani kell.

---

## Setup ami már elő van készítve

- ✅ `TransOfficeCopy_v3/` mappa (34 fájl, tiszta kiindulópont)
- ✅ `meeting_recording_20260825.m4a` (tényleges felvétel, 4:52)
- ✅ `meeting_transcript_20260825.srt` (AI-átirat, 7 perc)
- ✅ A 4 DEMO-fájl (F2.1, F3.3, F4.3, F5.3) tartalmazza az "Otthoni változat" promptot — DE a stáció-fájlok prompt-tartalma az amit a teszt valódilag mér

---

**Verzió:** 3.0 (foolproof copy-paste teszt)
**Készült:** 2026-05-14
