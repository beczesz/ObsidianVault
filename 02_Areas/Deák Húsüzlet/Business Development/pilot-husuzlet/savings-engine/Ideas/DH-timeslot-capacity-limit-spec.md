---
title: "DH Feature Spec: Timeslot kapacitás-limit"
date: 2026-05-01
author: Becze Szabolcs
status: active
description: "Timeslot kapacitás-limit funkció specifikációja: adminek korlátozhatják az egyes szállítási időpontokra érkezető rendelések számát, a vásárlók pedig csak szabad slotokat választhatnak ki. Race condition védelemmel és Firebase event-ekkel."
description_source: auto
description_hash: 6013f2fa3a6bed57
id: d656710b-a563-4220-8644-6f4724a81de5
index_schema_version: 1
bdos_index: true
---
# DH Feature Spec: Timeslot kapacitás-limit
**Verzió:** v1.0 | **Dátum:** 2026-04-26 | **Sprint:** 4 | **Prioritás:** P1

---

## Probléma

Jelenleg egy adott szállítási időpontra korlátlan számú rendelés érkezhet. Ha egy népszerű sávra (pl. szombat délelőtt) túl sok rendelés jön, a futár nem tudja minőségben kiszállítani — késés, romlás-kockázat, rossz ügyfélélmény. A pilot hitelességét veszélyezteti.

## Megoldás

Admin-felületről állítható **kapacitás-limit minden timeslotra**. Ha egy slot betelt, a vásárló nem tudja kiválasztani — a következő szabad slot automatikusan ki van emelve.

## Felhasználói történetek

### Vásárló
- **Rendeléskor** látom, melyik timeslot szabad és melyik betelt
- A betelt slotot **nem tudom kiválasztani** (szürkített, nem kattintható)
- **Látom hány hely van** még (pl. „Még 1 hely" vagy „Betelt")
- Ha a preferált slotom betelt, a **következő szabad slot** ki van emelve

### Admin (hentes/Szabolcs)
- **Beállíthatom a limitet** timeslotonként (alapértelmezett: 3)
- **Látom az aktuális foglaltságot** (pl. 2/3)
- **Módosíthatom a limitet** bármikor (pl. 3→5 ha bővül a kapacitás)
- **Lezárhatok egy slotot** teljesen (limit = 0)

## Funkcionális követelmények

### F1 — Kapacitás-limit tárolás
- Minden timeslothoz tartozik egy `max_orders` mező (integer, default: 3)
- Az érték admin-felületről módosítható
- A limit slotszinten él (nem globális) — de globális default állítható

### F2 — Foglaltság-számítás
- `current_orders` = azon rendelések száma amelyek:
  - Státuszuk NEM `cancelled`
  - Az adott timeslotra szólnak
- `available_slots` = `max_orders` - `current_orders`
- Ha `available_slots` ≤ 0 → slot nem választható

### F3 — Vásárlói felület (checkout timeslot picker)
- **Szabad slot:** normál megjelenés + opcionális „Még X hely" badge ha X ≤ 1
- **Betelt slot:** szürkített háttér + „Betelt" badge + `pointer-events: none`
- **Ha minden slot betelt az adott napon:** „Erre a napra minden időpont betelt. Válassz másik napot." üzenet
- **Auto-suggest:** ha a user korábban választott slotja közben betelt (race condition), a checkout figyelmeztet és a következő szabad slotot ajánlja

### F4 — Admin felület
- Timeslot lista táblázatban: `időpont | limit | foglalt | szabad`
- Inline edit a limit mezőn (number input, min: 0, max: 20)
- „Globális alapértelmezett" beállítás (minden új slotra ez érvényes)
- Módosítás azonnal érvényes (nincs deploy)

### F5 — Race condition védelem
- A rendelés leadásakor backend-szinten újra ellenőrzi a kapacitást
- Ha közben betelt → hibaüzenet: „Ez az időpont közben betelt. Kérlek válassz másikat."
- Optimistic locking VAGY atomic increment a `current_orders` mezőn

## Nem-célok (v1.0-ban NEM kell)

- Várólistás feliratkozás betelt slotra
- Automatikus kapacitás-állítás (AI-alapú)
- Timeslot-specifikus árazás
- Push notification ha felszabadul egy slot

## UI mockup — vásárlói nézet

```
┌─────────────────────────────────────┐
│  Mikor szállítsuk?                  │
├─────────────────────────────────────┤
│                                     │
│  Szombat, ápr. 25                   │
│  ┌──────────────┐  ┌──────────────┐ │
│  │ 9:00 - 12:00 │  │ 14:00-17:00  │ │
│  │   ✓ Szabad   │  │  ⚠ Még 1 hely│ │
│  └──────────────┘  └──────────────┘ │
│                                     │
│  Vasárnap, ápr. 26                  │
│  ┌──────────────┐  ┌──────────────┐ │
│  │ 9:00 - 12:00 │  │ 14:00-17:00  │ │
│  │   ✗ Betelt   │  │   ✓ Szabad   │ │
│  └──────────────┘  └──────────────┘ │
│                                     │
└─────────────────────────────────────┘
```

## UI mockup — admin nézet

```
┌──────────────────────────────────────────────┐
│  Timeslot kapacitás kezelése                 │
├──────────────────────────────────────────────┤
│  Globális alapértelmezett limit: [ 3 ] ✏️     │
├──────────┬───────┬────────┬──────────────────┤
│ Időpont  │ Limit │ Foglalt│ Szabad           │
├──────────┼───────┼────────┼──────────────────┤
│ Szo 9-12 │ [ 3 ] │  2     │ 1                │
│ Szo 14-17│ [ 3 ] │  3     │ 0  ← BETELT      │
│ Vas 9-12 │ [ 3 ] │  1     │ 2                │
│ Vas 14-17│ [ 5 ] │  0     │ 5                │
└──────────┴───────┴────────┴──────────────────┘
```

## Technikai megjegyzések

- **Frappe doctype:** Meglévő Delivery Slot doctype-ra `max_orders` mező hozzáadása (Int, default 3)
- **Számítás:** server-side `get_available_slots()` API, amit a frontend hív checkout-nál
- **Locking:** Frappe `frappe.db.sql` atomic update VAGY `SELECT ... FOR UPDATE`
- **Cache:** Slot foglaltság cache-elhető 30 mp-re (Redis), a checkout submit mindig friss lekérdezést csinál
- **Firebase event:** `timeslot_full` event ha egy slot betelik (analytics)

## Acceptance criteria

1. ✅ Admin tud limitet állítani timeslotonként
2. ✅ Vásárló nem tud betelt slotra rendelni (frontend + backend védelem)
3. ✅ Race condition esetén a backend visszautasítja és hibaüzenetet ad
4. ✅ „Még 1 hely" badge megjelenik ha `available_slots` = 1
5. ✅ „Betelt" badge megjelenik és a slot nem kattintható ha `available_slots` = 0
6. ✅ Limit módosítás azonnal érvényes, deploy nélkül
7. ✅ Firebase `timeslot_full` event tüzel ha egy slot betelik

## Effort becslés

| Komponens | Becsült idő |
|-----------|-------------|
| Backend: doctype módosítás + API | 2-3 óra |
| Frontend: checkout timeslot picker | 3-4 óra |
| Admin felület | 2-3 óra |
| Race condition védelem + tesztek | 2 óra |
| Firebase event | 1 óra |
| **Összesen** | **~10-13 óra** (~1.5-2 nap) |

## Kockázatok

| Kockázat | Hatás | Mitigáció |
|----------|-------|-----------|
| Race condition két egyidejű rendelésnél | Túlfoglalás | Atomic DB increment + backend ellenőrzés |
| Admin elfelejti frissíteni a limitet | Kapacitáshiány vagy kihasználatlanság | Globális default + dashboard figyelmeztetés |
| Vásárló frusztrált ha nincs szabad slot | Elveszett rendelés | Auto-suggest következő szabad slot |
