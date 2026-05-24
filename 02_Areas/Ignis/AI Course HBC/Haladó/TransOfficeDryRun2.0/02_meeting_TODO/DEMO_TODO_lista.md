# DEMO output — F2 OKTATÓ (A.2 prompt)

> **Forrás:** `meetings/meeting_transcript_20250224.srt` (73 bemondás, ~7 perc)
> **Prompt:** A.2 — Helyzet + TODO + hiányok + blokkolók
> **Mentve a Productivity pluginbe:** ✅ igen (lentebb látszik)

---

## 1. Helyzet összefoglaló

A TransOffice vezetése (Márton — Speaker A, ügyvezető) és Enikő (Speaker B, könyvelő) sürgős meeting-en megállapították, hogy az AFM Mobilitate Verde elektromos járműpályázat — amit decemberben kaptak meg, de **2 hónapja érintetlenül** áll Márton gépén — **péntekig** be kell adni, különben a forrás kifut. A pályázat 70-80% támogatást nyújthat **2 elektromos autóra**, de a cégnél jelenleg **nincs egy tiszta ügyféllista, nincs járműleltár, és a pénzügyi adatok is csak részben aktuálisak**. Béla bácsi (telephely-tulajdonos) szilveszterkor megemlített egy ingatlan-eladási szándékot is — **utánanézés szükséges**, nehogy a TransOffice telephelye legyen érintett. A koordinációt az **új Operations Manager** (te) végzi.

## 2. TODO lista

| # | Ki | Mit | Mikorra | Prioritás |
|---|----|-----|---------|-----------|
| T01 | Operations Manager | Pályázati kiírás (PDF, ~100 oldal) átolvasása és eligibility-elemzés | 2025-02-25 kedd | 🔴 P1 |
| T02 | Operations Manager | Cégadatok összegyűjtése: tevékenységi kör, cégkivonat | 2025-02-25 kedd | 🔴 P1 |
| T03 | Bíró Attila (vagy logisztika) | Aktuális járműleltár (hány autó, milyen, állapot, kor) | 2025-02-26 szerda | 🔴 P1 |
| T04 | Enikő | 2023-as pénzügyi zárás (árbevétel, EBITDA) | 2025-02-25 kedd | 🔴 P1 |
| T05 | Enikő → Mihaela (külsős könyvelő) | Email a 2024-es részleges adatokért (árbevétel, alkalmazotti létszám, EBITDA-becslés) | 2025-02-25 kedd | 🔴 P1 |
| T06 | Operations Manager | Ügyféllista konszolidáció a 3 Excel + emailek alapján — referencia-lista | 2025-02-26 szerda | 🟡 P2 |
| T07 | Márton | Hatóság (AFM kontakt) felhívása: van-e apró feltétel, amin elcsúszhat a beadás | 2025-02-26 szerda | 🟡 P2 |
| T08 | Operations Manager | **Béla bácsi megkeresése**: szilveszteri eladási megjegyzés tisztázása (telephely-érintett vagy más ingatlan?) | 2025-02-25 kedd | 🔴 P1 (Legal kockázat) |
| T09 | Operations Manager | Indoklás megírása: miért elektromos autó (környezetvédelem + költségcsökkentés) | 2025-02-27 csütörtök | 🟡 P2 |
| T10 | Operations Manager | Piaci adat / tanulmány keresése elektromos flottára vonatkozóan (pályázati oldal / online) | 2025-02-27 csütörtök | 🟢 P3 |
| T11 | Operations Manager | Pályázat-leírás megírása (cég, tevékenység, támogatás-cél) | 2025-02-28 péntek reggel | 🔴 P1 |
| T12 | Márton | Aláírás, benyújtás | 2025-02-28 péntek | 🔴 P1 |

**Összesen: 12 TODO, ebből 7 piros (P1) és 4 sárga (P2), 1 zöld (P3).**

## 3. Hiányzó információk (amik nélkül nem lehet pályázni)

- ❌ **Tiszta járműleltár** — Speaker A bizonytalan, hogy 3 vagy 4 autó van; nincs egy hivatalos lista
- ❌ **2024-es pénzügyi adatok** (árbevétel, EBITDA, alkalmazotti létszám) — Mihaela tudja, de email-en kell kérni
- ❌ **Cégkivonat aktuális verziója** — Enikő szerint van egy régi PDF és egy Word fájl, de nincs egy helyen
- ❌ **Pontos pályázati követelmény-szint** (a 100 oldalas PDF-en belül a 12-17 kritérium) — még nincs strukturált gap-elemzés
- ❌ **AFM kontakt** — kihez kell írni / telefonálni
- ❌ **Béla bácsi-szál tisztázása** — telephely érintett-e? (T08-as TODO)
- ❌ **Piaci tanulmány** elektromos flottára vonatkozóan (T10)

## 4. Blokkolók (függőségek)

```
T11 (Pályázat-leírás)  ⟵  T01 (Eligibility) ⟵ T03, T04, T05, T02 (Adatok)
T12 (Benyújtás)        ⟵  T11 + T08 (Béla bácsi)
```

| TODO | Függ ettől | Miért blokkoló |
|------|-----------|----------------|
| T11 | T01, T03, T04, T05 | Nem írható meg a pályázati anyag, amíg az eligibility nincs kiderítve és az adatok nincsenek összegyűjtve |
| T12 | T11, T08 | Beadás csak akkor, ha a tartalom kész + a Béla bácsi-szál tisztázva (különben legal-kockázat) |
| T07 | — | Önállóan futtatható |
| T08 | — | Önállóan futtatható, **de sürgős** (5 éves stabilitás kell az AFM-hez) |

---

## 5. Productivity plugin — elmentve

✅ A 12 TODO **mentve** a Cowork Productivity plugin TASKS.md fájljába.
✅ Új session megnyitva — a *"Mik a nyitott feladataim?"* prompt megerősítette: emlékszik.

---

## 6. Kockázatok (a Cowork észrevétele)

🚨 **Béla bácsi-szál**: a 41. bemondásban Speaker A mellékesen említi, hogy Béla bácsi szilveszterkor ingatlan-eladásról beszélt. Ez az AFM pályázat **5 éves stabilitás** követelményét érintheti, ha a telephely érintett. **A T08 nem `P2` — `P1`-nek minősítettem.** Külön megjegyzem: ez **NEM** csak egy adminisztratív TODO, hanem **legal/eligibility kockázat**.

🚨 **Időkeret hihetetlenül szoros:** 4 munkanap 12 TODO-ra, ebből 7 piros. **F3-F5-ben fókuszálnunk kell, F6 (weboldal) a beadás utánra tolható.**
