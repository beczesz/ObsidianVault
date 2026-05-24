---
name: yahoo-v0.2
description: Yahoo Mail inbox cleanup — promotional emails törlése és briefing riport. Scheduled task or on-demand command.
version: 0.2
date: 2026-04-02
author: Becze Szabolcs
allowed-tools: Read, Write, WebFetch, TodoWrite
id: cf3f33ed-c62e-4e04-a879-7908833a1777
index_schema_version: 1
---

# Yahoo Mail Inbox Fésülés (Comb-through Cleanup)

Szisztematikus inbox takarítás: a jelentől a múlt felé haladva végignézi az emaileket, leíratkozik a promóciós küldőkről, megkeresi az összes korábbi emailjüket, és törli mindet.

---

## STEP 0 — ÁLLAPOT BETÖLTÉSE

Olvasd be a state fájlt: `${CLAUDE_PLUGIN_ROOT}/../yahoo-cleanup-state.md`

Ha nem létezik, hozd létre az alábbi sablonnal:

```markdown
---
title: Yahoo Cleanup State
version: 0.1
date: [mai dátum]
---

# Yahoo Mail Cleanup — Állapot

## Haladás

| Mező                  | Érték  |
|-----------------------|--------|
| Utolsó feldolgozott nap | –    |
| Utolsó futás           | –     |
| Törölt emailek (lifetime) | 0  |
| Eltávolított küldők (lifetime) | 0 |

## Ismert promóciós küldők

_(Üres — még nincs feldolgozott küldő)_

## Ismert biztonságos küldők

- eon@myline.ro
- info@hidroelectrica.ro
- noreply@bancatransilvania.ro
- noreply-blocadmin@blocadmin.ro
- service@paypal.com
- noreply@google.com
- no-reply@accounts.google.com

## Futási napló

| Dátum | Feldolgozott napok | Törölt email | Eltávolított küldő | Leíratkozás |
|-------|-------------------|--------------|--------------------:|------------:|
```

Ha létezik, olvasd ki az `Utolsó feldolgozott nap` értéket a Haladás táblázatból — ez az a dátum, ahonnan folytatni kell.

---

## STEP 1 — KEZDŐPONT MEGHATÁROZÁSA

- Ha `Utolsó feldolgozott nap` üres (–) → kezdd a mai nappal
- Ha van dátum → kezdd az azt megelőző nappal (az a nap már feldolgozott)
- Haladj a jelenlegi dátumtól visszafelé, napról napra

---

## STEP 2 — EMAILEK LEKÉRÉSE AZ ADOTT NAPRA

Használd a `search_emails` toolt:
- `dateFrom`: az adott nap 00:00 (ISO 8601)
- `dateTo`: az adott nap 23:59 (ISO 8601)
- `count`: 50
- Ha 50-nél több van, lapozz (`offset`) amíg az összes email megvan az adott napra

---

## STEP 3 — OSZTÁLYOZÁS (minden emailre)

Nézd meg a feladót és a tárgyat. Használd a state fájlból az Ismert promóciós küldők és Ismert biztonságos küldők listákat gyorsítóként.

### TÖRLENDŐ (promotional/marketing/spam):
- Newsletter-ek és marketing emailek
- Social media értesítések (Instagram, Facebook, TikTok, Twitter, LinkedIn, stb.)
- Webshop ajánlatok (Amazon, AliExpress, eBay, Shopify, Temu, stb.)
- Esemény promóciók és szórakoztatási ajánlatok
- Reklám és promóciós tartalom bármely küldőtől
- Az Ismert promóciós küldők listán szereplők (automatikus, nem kell újra ellenőrizni)

### MEGTARTANDÓ (legitim szolgáltatási és személyes emailek):
- Közüzemi számlák: E.ON Myline, Hidroelectrica
- Banki és pénzügyi: Banca Transilvania, BLOC ADMIN, NETOPIA, PayPal (csak biztonsági figyelmeztetések, NEM promóciós)
- Biztonsági riasztások: Google (fiók biztonság, recovery kódok)
- Szolgáltatási értesítések: Yahoo Mail rendszerüzenetek, email verifikációs kódok
- Hitelesítési kódok és OTP-k
- Domain regisztrátori emailek
- Személyes levelezés ismert kontaktoktól
- Munkahelyi emailek
- Bármilyen közüzemi vagy szolgáltatói kommunikáció
- Az Ismert biztonságos küldők listán szereplők

### BIZONYTALAN
Ha nem egyértelmű → TARTSD MEG. Soha ne törölj kétséges emailt.

---

## STEP 4 — LEÍRATKOZÁS + TÖRLÉS (minden promóciós küldőnél)

Minden egyes promóciós küldőre hajtsd végre ezt a sorrendet:

### 4a. Leíratkozás
1. Olvasd el az emailt a `read_email` tool-lal
2. Keresd az unsubscribe linket az email body-jában:
   - `unsubscribe` szó a szövegben + hozzá tartozó URL
   - `List-Unsubscribe` header (ha elérhető)
3. Ha találsz unsubscribe linket:
   - Nyisd meg a Chrome-mal (`navigate` tool)
   - Várd meg a betöltést
   - Ha van "confirm" gomb, kattints rá
   - Logold: "✅ Leíratkozott: [küldő]"
4. Ha NINCS unsubscribe link:
   - Logold: "⚠️ Nincs unsubscribe link: [küldő] — csak törlés"
   - Haladj tovább a törlésre

### 4b. Összes email megkeresése a küldőtől
Használd a `search_emails` toolt:
- `sender`: a küldő email címe
- `count`: 50
- Lapozz amíg az összes email megvan (offset-tel)

### 4c. Törlés
Használd a `delete_emails` toolt az összes UID-vel egyszerre.
Logold: "🗑️ [küldő]: [N] email törölve"

### 4d. State frissítés (memóriában)
- Add hozzá a küldőt az Ismert promóciós küldők listához
- Növeld a lifetime számlálókat

---

## STEP 5 — KÖVETKEZŐ NAP

Ha az adott nap összes emailje feldolgozva:
- Lépj egy nappal visszább
- Ismételd a STEP 2-4 lépéseket
- Haladj addig amíg el nem fogy az email, vagy a felhasználó nem állítja le

---

## STEP 6 — ÁLLAPOT MENTÉSE

A futás végén (akár normálisan végzett, akár megszakadt) frissítsd a `yahoo-cleanup-state.md` fájlt:

1. **Haladás táblázat** — frissítsd az értékeket:
   - `Utolsó feldolgozott nap` → az utolsó TELJESEN feldolgozott nap dátuma
   - `Utolsó futás` → most (ISO 8601)
   - `Törölt emailek (lifetime)` → előző érték + mai törlések
   - `Eltávolított küldők (lifetime)` → előző érték + mai új küldők

2. **Ismert promóciós küldők** — add hozzá az újonnan azonosított küldőket bullet listában:
   ```
   - newsletter@example.com (leíratkozva ✅)
   - promo@shop.com (nincs unsub link ⚠️)
   ```

3. **Ismert biztonságos küldők** — ha új biztonságos küldőt azonosítottál, add hozzá

4. **Futási napló** — adj hozzá egy új sort:
   ```
   | 2026-04-02 | ápr 1 → márc 28 | 47 | 8 | 5 |
   ```

Fájl helye: `${CLAUDE_PLUGIN_ROOT}/../yahoo-cleanup-state.md`

---

## STEP 7 — BRIEFING RIPORT

A futás végén adj egy összefoglalót:

```
Yahoo Mail Fésülés — Riport
━━━━━━━━━━━━━━━━━━━━━━━━━━━

📅 Feldolgozott napok: [dátumtól] → [dátumig]
📧 Átnézett emailek: [N]
🗑️ Törölt emailek (ma): [N]
👤 Eltávolított küldők (ma): [N]
✅ Sikeres leíratkozások: [N]
⚠️ Leíratkozás nélküli törlések: [N]

Összesített (lifetime):
  Törölt emailek: [N]
  Eltávolított küldők: [N]

Következő futás folytatása: [dátum]-tól visszafelé

Eltávolított küldők listája:
  - [küldő1] ([N] email)
  - [küldő2] ([N] email)
  ...
```

---

## FONTOS SZABÁLYOK

1. **Biztonság:** Ha bizonytalan vagy → TARTSD MEG. Soha ne törölj kétséges emailt.
2. **Leíratkozás first:** Mindig próbáld meg a leíratkozást MIELŐTT törölnél — ez hosszú távon csökkenti a spam-et.
3. **Batch hatékonyság:** A `delete_emails` tool egyszerre több UID-t is fogad — gyűjtsd össze egy küldő összes UID-jét és töröld egyben.
4. **State megbízhatóság:** MINDIG mentsd el az állapotot, még ha hiba történik is. Az `Utolsó feldolgozott nap` legyen az utolsó TELJESEN feldolgozott nap.
5. **Ismert küldők cache:** Az Ismert promóciós küldők lista gyorsítja a jövőbeli futásokat — nem kell újra osztályozni.
6. **Nincs limit:** Dolgozd fel az összes emailt az adott napon, bármennyit is találsz. Haladj napról napra amíg van mit feldolgozni.
