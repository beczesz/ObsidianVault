# Feladat 2.1 — Meeting transcript feldolgozás

> **Típus:** 🎤 OKTATÓI DEMO (a kivetítőről nézed)
> **Idő:** ~10 perc · **Hozzád tartozik:** csak figyelés + páros megbeszélés

---

## Mit látsz a kivetítőn

Az oktató behúzza a `meeting_transcript_20250224.srt` fájlt a Cowork-be — ez egy AI által transcribe-olt felvétel egy sürgős meetingről. A meeting **Márton (ügyvezető)** és **Enikő (könyvelő)** között zajlott, és kiderül, hogy az AFM Mobilitate Verde pályázat **2 hónapja a radarjuk alatt van**, és **péntekig be kell adni vagy lemarad**.

A Productivity plugin elemzi a transcriptet és:
- Strukturált TODO listát készít (Ki → Mit → Mikorra → Prioritás)
- Azonosítja a hiányzó információkat
- Megjelöli a blokkolókat (melyik TODO függ a másiktól)
- **Elmenti** a TODO-kat — session-ök között is megmaradnak

Az oktató ezután egy **új chat-tabot** nyit, és csak annyit kérdez: *„Mik a nyitott feladataim?"* — és a Cowork **emlékszik**. **Ez az F2 mágikus pillanata.**

---

## A prompt amit az oktató használ

Ez az amit az oktató bemásol a Cowork-be:

```
Olvasd el ezt a meeting transcriptet. Sürgős megbeszélés egy EU pályázatról
(AFM Mobilitate Verde 2025 — elektromos járműflotta).

Kérek:
1. Helyzet összefoglaló (3-5 mondat)
2. TODO lista: Ki → Mit → Mikorra → Prioritás
3. Hiányzó információk (amik nélkül nem lehet pályázni)
4. Blokkolók: melyik TODO függ a másiktól

A TODO-kat mentsd el a Productivity pluginbe.
```

---

## Mire figyelj

A demo közben **figyeld**:

- Hogyan ismeri fel a Cowork a határidőt **a 'kedd' szóból**?
- Milyen TODO-kat azonosít amit a transcript **csak utal rá** (pl. „valami szilveszteri megjegyzés")?
- Mit jelent a „session-ök közötti memória" — miért fontos hogy a Productivity plugin **megjegyzi** a TODO-kat?

---

## Tanulás

- **A Productivity plugin nem egy lista-generátor** — egy **perzisztens rendszer**. A ChatGPT-vel ez nem így működne (minden chat tiszta lap).
- **A meeting → TODO** alaptevékenység átalakítható: egy ember 30 perc alatt csinálná, a Cowork **2 perc alatt**.
- A „forrás-agnoszticizmus" — a Cowork **bármilyen szöveges bemenetből** (transcript, email-szál, kézzel írt jegyzet) ki tudja vonni a TODO-kat.

---

## Otthoni elmélyítés

Otthon próbáld ki **a saját életeddel** — bónusz feladatok:
- `Feladat_2.3_Bonusz_Email_szal_TODO.md` — egy saját email-szálból TODO kinyerés
- `Feladat_2.4_Bonusz_Heti_review.md` — heti TODO-review automatizmus
- `Feladat_2.5_Bonusz_Sajat_meeting.md` — saját meeting feldolgozása

A workshop alatti **stáció**: `Feladat_2.2_Followup_es_action_items.md` — itt te is megírod a saját follow-up emailt Enikőnek.

---

**Verzió:** 2.0 (instructor-led + stáció modell) · Korábbi v1.0: `Műhely/_archivum/F2_F6_v1.0/`
