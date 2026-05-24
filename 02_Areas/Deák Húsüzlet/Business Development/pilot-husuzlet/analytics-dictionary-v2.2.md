---
title: DH Analytics Dictionary
version: v2.2
updated: 2026-04-29
source: "GA4 Events audit (Apr 1-28, 2026) + Mate feedback + Szabolcs review"
total_live_events: "18 custom + 5 auto = 23"
audit_method: "GA4 event detail page, parameter review, Mate Slack feedback"
review_status: COMPLETE
single_ticket: DH-181
id: c1bf3d55-7a33-45b5-a7a4-f1f5c0c178e1
index_schema_version: 1
---

# DH Analytics Dictionary v2.2

## Gyors áttekintés

| Státusz | Darab | Jelentés |
|---------|-------|-----------|
| ✅ Tökéletesen érkezik | **10** | Event tüzel, paraméter nem szükséges vagy elfogadható |
| ⚠️ Javítandó | **4** | Event tüzel, de paraméter hibás/hiányos |
| ❓ Ellenőrizendő | **4** | Event tüzel, paraméter státusz ismeretlen (Mate-nek kérdés) |
| ❌ Hiányzó | **8** | Nem implementált, de szükséges |
| **Összesen** | **26** | 18 élő + 8 hiányzó |

---

## Módszertan

Minden élő eventet egyenként átnéztünk a GA4 event detail oldalán (Apr 1 – Apr 28, 2026):
- Event count és user count ellenőrizve
- PARAMETER NAME dropdown vizsgálva (regisztrált custom dimensions)
- Mate fejlesztői feedback integrálva (2026-04-28 Slack)
- Szabolcs jóváhagyta a törléseket (2026-04-28)

**Szisztematikus finding:** A PARAMETER NAME dropdown MINDEN eventnél üres ("-"), kivéve:
- `add_to_cart` — GA4 standard ecommerce `items[]` látható (Product ID = hash, Quantity)
- `campaign_cta_clicked` — `campaign` = "1" (regisztrált Custom Dimension)

---

## ✅ Tökéletesen érkező eventek (10 db)

Ezek az eventek helyesen tüzelnek és nem igényelnek paraméter-javítást.

| # | Event | Count | Users | Paraméterek | Megjegyzés |
|---|-------|-------|-------|------------|-----------|
| 1 | `product_list_view` | 237 | 28 | — (nem szükséges) | Terméklista megtekintés |
| 2 | `landing_view` | 10 | 7 | — (nem szükséges) | Landing oldal megtekintés |
| 3 | `campaign_dismissed` | 24 | 19 | — (nem szükséges) | Modal bezárás |
| 4 | `order_delivered` | 3 | 2 | — (lásd ellenőrizendő*) | Kiszállítva státusz |
| 5 | `order_out_for_delivery` | 3 | 1 | — (lásd ellenőrizendő*) | Úton van |
| 6 | `order_preparing` | 3 | 1 | — (lásd ellenőrizendő*) | Előkészítés alatt |
| 7 | `order_ready` | 2 | 1 | — (lásd ellenőrizendő*) | Kész átvételre |
| 8 | `active_banner_tapped` | 13 | 2 | — (nem szükséges) | Banner kattintás |
| 9 | `reorder_cancelled` | 1 | 1 | — (nem szükséges) | Újrarendelés lemondva |
| 10 | `reorder_initiated` | 1 | 1 | — (nem szükséges) | Újrarendelés indítva |

*Az order lifecycle eventek (4–7) ideálisan tartalmaznának `order_id` paramétert, de minimálisan használhatók anélkül is. Lásd: Jövőbeli elvárások szekció.

---

## ⚠️ Javítandó eventek (4 db)

Ezek az eventek tüzelnek, de a paramétereik hibásak vagy hiányosak.

### 1. `add_to_cart` — Hiányos termékadatok

| | |
|---|---|
| **Count** | 65 events / 14 users |
| **Probléma** | Az `items[]` tömb hash product ID-t tartalmaz, nincs terméknév, kategória, ár |
| **Ticket** | DH-179 → DH-181 |

**Jelenlegi állapot:**
```json
{
  "items": [{
    "item_id": "a1b2c3d4",
    "quantity": 1
  }]
}
```

**Elvárt állapot (GA4 Enhanced E-commerce standard):**
```json
{
  "items": [{
    "item_id": "dh_csk_01",
    "item_name": "Csülkös sonka",
    "item_category": "Sonkák",
    "price": 45.90,
    "quantity": 1
  }]
}
```

### 2. `campaign_cta_clicked` — Rossz campaign érték

| | |
|---|---|
| **Count** | 17 events / 13 users |
| **Probléma** | `campaign` paraméter = `"1"` (szám string) a kampány neve helyett |
| **Ticket** | DH-180 → DH-181 |

**Jelenlegi állapot:**
```
logEvent("campaign_cta_clicked", { campaign: "1" })
```

**Elvárt állapot:**
```
logEvent("campaign_cta_clicked", { campaign_name: "founding_50" })
```

### 3. `campaign_modal_shown` — Nem tüzel mobilon

| | |
|---|---|
| **Count** | 41 events / 23 users |
| **Probléma** | Live tesztben mobilon nem tüzel— valószínűleg a logEvent hívás feltétele hibáz |
| **Ticket** | DH-178 → DH-181 |

**Jelenlegi állapot:** Desktop: ✅ | Mobil: ❌
**Elvárt állapot:** Minden platformon tüzel, paraméterek:
```
logEvent("campaign_modal_shown", { campaign_name: "founding_50" })
```

### 4. `registration_completed` — Hiányzó user_id

| | |
|---|---|
| **Count** | 4 events / 4 users |
| **Probléma** | `user_id` paraméter nem kerül elküldésre |
| **Ticket** | DH-169 (Mate már dolgozik rajta — In Progress) → DH-181 |

**Jelenlegi állapot:**
```
logEvent("registration_completed", {})
```

**Elvárt állapot:**
```
logEvent("registration_completed", { user_id: "<firebase_uid>", method: "email" })
```

---

## ❓ Ellenőrizendő eventek (4 db)

Ezek az eventek tüzelnek, de a GA4-ben nem látható egyetlen paraméter sem (Custom Dimension nincs regisztrálva). Kérdés Mate-nek: küldi-e a paramétereket a `logEvent()` hívásban?

### 5. `checkout_started`

| | |
|---|---|
| **Count** | 18 events / 9 users |
| **GA4 látható param** | — (semmi) |
| **Mikor tüzel** | A felhasználó a kosárból megnyomja a "Megrendelés" / "Tovább a fizetéshez" gombot. Ez a checkout flow első lépése. |
| **Mit jelent** | A vásárló eldöntötte, hogy megrendeli a kosár tartalmát és elindult a fizetési/szállítási adatok megadása felé. Ez a funnel "intent to buy" pontja — a konverzió előszobája. |
| **Miért fontos** | Cart → Checkout konverziós ráta mérése. Ha sokan raknak kosárba de kevesen indítanak checkout-ot, az UX vagy árazási probléma. |

**Elvárt paraméterek:**
```
logEvent("checkout_started", {
  cart_value: 189.50,      // kosár összértéke RON-ban
  item_count: 4,           // hány tétel van a kosárban
  items: [{                // GA4 Enhanced E-commerce standard
    item_id: "dh_csk_01",
    item_name: "Csülkös sonka",
    price: 45.90,
    quantity: 1
  }]
})
```

### 6. `order_created`

| | |
|---|---|
| **Count** | 4 events / 4 users |
| **GA4 látható param** | — (semmi) |
| **Mikor tüzel** | A rendelés sikeresen létrejön a backend-en — a felhasználó megadta a szállítási adatokat, megerősítette a rendelést, és a szerver visszajelzett sikeres order creation-t. |
| **Mit jelent** | Befejezett vásárlás. A legfontosabb konverziós event — ez jelenti, hogy ténylegesen rendelt a felhasználó. |
| **Miért fontos** | Ez a végső konverziós pont. Visitor → Regisztráció → Kosár → Checkout → **Order Created**. Minden felette lévő funnel lépés ehhez képest mérhető. |

**Elvárt paraméterek:**
```
logEvent("order_created", {
  order_id: "DH-2026-0042",   // egyedi rendelés azonosító
  order_value: 189.50,         // rendelés összértéke RON-ban
  item_count: 4,               // hány tétel
  payment_method: "cash"       // fizetési mód (pilot: mindig "cash")
})
```

### 7. `campaign_enrolled`

| | |
|---|---|
| **Count** | 9 events / 9 users |
| **GA4 látható param** | — (semmi) |
| **Mikor tüzel** | A felhasználó a Founding 50 kampány modalon megnyomja a "Csatlakozom" / "Regisztrálok" gombot és sikeresen csatlakozik a programhoz. |
| **Mit jelent** | A felhasználó opt-in-elt a Founding 50 early adopter programba (3 hónap ingyenes szállítás, max 50 fő). |
| **Miért fontos** | Founding 50 toborzás hatékonyságának mérése. Hány modal megjelenítésből (campaign_modal_shown: 41) lesz tényleges csatlakozás (9)? Jelenlegi konverzió: ~22%. |

**Elvárt paraméterek:**
```
logEvent("campaign_enrolled", {
  campaign_name: "founding_50",   // melyik kampány
  enrollment_source: "modal"      // honnan csatlakozott (modal / banner / direct_link)
})
```

### 8. `campaign_order`

| | |
|---|---|
| **Count** | 3 events / 3 users |
| **GA4 látható param** | — (semmi) |
| **Mikor tüzel** | Egy Founding 50 tag leadja a rendelését. Ez az `order_created` kampány-specifikus párja — csak akkor tüzel, ha a rendelő felhasználó aktív Founding 50 tag. |
| **Mit jelent** | Kampány-specifikus konverzió: a Founding 50 résztvevők ténylegesen rendelnek-e? 9 enrolled → 3 campaign_order = 33% aktiválás. |
| **Miért fontos** | A Founding 50 ROI mérése. Ha a tagok nem rendelnek, a program nem működik. Ez az enrollment → activation konverziós ráta alapja. |

**Elvárt paraméterek:**
```
logEvent("campaign_order", {
  order_id: "DH-2026-0042",       // rendelés azonosító
  campaign_name: "founding_50",    // kampány neve
  order_value: 189.50              // rendelés értéke RON-ban
})
```

---

## ❌ Hiányzó eventek (8 db)

### P0 — Kötelező (2 event)

#### 1. `repeat_order_created`

| | |
|---|---|
| **Prioritás** | **P0 — North Star KPI** |
| **Mikor tüzel** | Amikor egy felhasználó rendelést ad le, ÉS már van legalább 1 korábbi befejezett rendelése. Tehát a 2., 3., 4., ... rendelésnél. Az első rendelésnél NEM tüzel — az `order_created`. |
| **Mit jelent** | A felhasználó visszatért és újra rendelt. Ez a DH pilot legfontosabb metrikája: a Second Order Rate (cél: ≥40% 14 napon belül). |
| **Miért fontos** | Ha a felhasználók nem rendelnek újra, a modell nem működik. Ez az egyetlen metrika, ami eldönti, hogy a pilot sikeres-e. A `days_since_first` paraméter megmutatja, milyen gyorsan térnek vissza. |
| **Hogyan detektálni** | Backend: order creation során ellenőrizni, hogy a `user_id`-hoz tartozik-e korábbi `completed` státuszú order. Ha igen → `repeat_order_created`. |

**Implementáció:**
```
// Backend trigger: user.completed_orders.count >= 1 && new order created
logEvent("repeat_order_created", {
  order_id: "DH-2026-0055",       // az új rendelés ID-ja
  days_since_first: 7,             // napok száma az első rendelés óta
  order_value: 142.00              // rendelés értéke RON-ban
})
```

#### 2. `order_cancelled`

| | |
|---|---|
| **Prioritás** | **P0** |
| **Mikor tüzel** | Amikor egy rendelés törlésre kerül — akár a felhasználó kéri (app-ból vagy telefonon), akár az admin/mészáros törli (pl. nincs készleten a termék). |
| **Mit jelent** | Egy korábban leadott rendelés nem lesz teljesítve. |
| **Miért fontos** | Magas törlési arány = supply probléma vagy UX probléma. Ha a törlések >10%-ot érik el, az a modell fenntarthatóságát veszélyezteti. A `cancel_reason` segít diagnosztizálni: user kérte? készlethiány? túl későn szállítanák? |
| **Hogyan detektálni** | Backend: order státusz változás `cancelled`-re. |

**Implementáció:**
```
logEvent("order_cancelled", {
  order_id: "DH-2026-0042",             // a törölt rendelés ID-ja
  cancel_reason: "user_requested"        // ok: "user_requested" | "out_of_stock" | "admin_cancelled"
})
```

### P1 — Savings Engine (6 event)

#### 3. `threshold_achieved_150`

| | |
|---|---|
| **Prioritás** | P1 — Savings Engine |
| **Mikor tüzel** | Amikor a felhasználó kumulatív megtakarítása (bolti ár vs. DH online ár összesítve az összes rendelésén) átlépi a **150 RON**-t. Egyszer tüzel felhasználónként. |
| **Mit jelent** | A felhasználó elérte az első spórolási mérföldkövet. Az app-ban celebration UI jelenik meg ("Már 150 RON-t spóroltál!"). |
| **Miért fontos** | A savings engine motivációs hatásának mérése. Ha sok user eléri a 150-et, a "spórolás" üzenet működik. A `order_count` megmutatja, hány rendelés kellett hozzá. |

**Implementáció:**
```
// Trigger: user.total_savings >= 150 && threshold_150_not_yet_fired
logEvent("threshold_achieved_150", {
  total_savings: 152.30,    // pontos kumulatív megtakarítás RON-ban
  order_count: 5            // hány rendelésből gyűlt össze
})
```

#### 4. `threshold_achieved_300`

| | |
|---|---|
| **Prioritás** | P1 — Savings Engine |
| **Mikor tüzel** | Amikor a kumulatív megtakarítás átlépi a **300 RON**-t. Egyszer tüzel felhasználónként. |
| **Mit jelent** | Második mérföldkő — a felhasználó rendszeres vásárló és jelentős összeget spórolt. |
| **Miért fontos** | Power user azonosítás. Aki eléri a 300-at, az lojális vásárló — potenciális ajánló, word-of-mouth forrás. |

**Implementáció:**
```
logEvent("threshold_achieved_300", {
  total_savings: 312.50,
  order_count: 12
})
```

#### 5. `bundle_added_to_cart`

| | |
|---|---|
| **Prioritás** | P1 — Savings Engine |
| **Mikor tüzel** | Amikor a felhasználó egy előre összeállított **családi csomag** (bundle) terméket ad a kosarához. NEM egyedi termék hozzáadásnál — az `add_to_cart`. |
| **Mit jelent** | A felhasználó a bundle feature-t használja a single-item vásárlás helyett. A bundle-ök magasabb kosárértéket és jobb margint jelentenek. |
| **Miért fontos** | Bundle feature adoption mérése. Ha senki nem használja a bundle-öket, a feature nem működik vagy nem elég vonzó az ajánlat. |

**Implementáció:**
```
logEvent("bundle_added_to_cart", {
  bundle_id: "family_grill",            // bundle azonosító
  bundle_name: "Családi Grillcsomag",   // megjelenítési név
  bundle_price: 89.90                   // bundle ár RON-ban
})
```

#### 6. `reorder_clicked`

| | |
|---|---|
| **Prioritás** | P1 — Savings Engine |
| **Mikor tüzel** | Amikor a felhasználó a "Rendeléseim" oldalon egy korábbi rendelésnél megnyomja az "Újrarendelés" gombot. Ez az első lépés — még NEM töltötte be a kosarat. |
| **Mit jelent** | A felhasználó kifejezi a szándékát, hogy ugyanazt rendelje, mint korábban. Ez a retention trigger — a kényelem (nem kell újra összeválogatni) csökkenti a rendelési súrlódást. |
| **Miért fontos** | Az újrarendelés feature használatának mérése. Ha magas a `reorder_clicked` de alacsony a `basket_loaded`, akkor a betöltés lépésnél van UX probléma. |

**Implementáció:**
```
logEvent("reorder_clicked", {
  source_order_id: "DH-2026-0042"   // melyik korábbi rendelést akarja újrarendelni
})
```

#### 7. `basket_loaded`

| | |
|---|---|
| **Prioritás** | P1 — Savings Engine |
| **Mikor tüzel** | Amikor a korábbi rendelés tételei sikeresen betöltődnek a kosárba (a `reorder_clicked` után). A felhasználó kosara most a korábbi rendelés tartalmával van feltöltve. |
| **Mit jelent** | Az újrarendelés flow második lépése: kosár betöltve a korábbi tételekkel. A felhasználó innentől módosíthat (hozzáadhat/törölhet tételt) vagy egyből checkout-olhat. |
| **Miért fontos** | Reorder funnel mérés: `reorder_clicked` → `basket_loaded` → `checkout_started` → `order_created`. Ha a basket_loaded magas de a checkout alacsony, a felhasználók "nézelődnek" de nem rendelnek. |

**Implementáció:**
```
logEvent("basket_loaded", {
  source_order_id: "DH-2026-0042",   // melyik rendelésből töltötte be
  item_count: 6                       // hány tétel töltődött be
})
```

#### 8. `recap_viewed`

| | |
|---|---|
| **Prioritás** | P1 — Savings Engine |
| **Mikor tüzel** | Amikor a felhasználó megnyitja a **spórolás összefoglaló** képernyőt, ami megmutatja, mennyit spórolt egy adott időszakban (havi/összesített). |
| **Mit jelent** | A felhasználó aktívan érdeklődik a megtakarítása iránt — megnézi a "dashboard"-ját. |
| **Miért fontos** | A savings motiváció feature engagement-jének mérése. Ha a felhasználók rendszeresen megnézik a recap-et, az azt jelenti, hogy a spórolás üzenet motiválja őket. Ha senki nem nézi, a feature nem elég látható vagy nem elég vonzó. |

**Implementáció:**
```
logEvent("recap_viewed", {
  total_savings: 245.80,    // eddig összesen mennyit spórolt RON-ban
  period: "monthly"         // melyik nézet: "monthly" | "all_time"
})
```

---

## Jövőbeli elvárások — Order Lifecycle paraméterek

Az order lifecycle eventek (order_delivered, order_out_for_delivery, order_preparing, order_ready) jelenleg paraméter nélkül érkeznek. Nem blokkoló, de jövőben érdemes lenne `order_id`-t is küldeni:

```
logEvent("order_delivered", { order_id: "DH-2026-0042" })
logEvent("order_out_for_delivery", { order_id: "DH-2026-0042" })
logEvent("order_preparing", { order_id: "DH-2026-0042" })
logEvent("order_ready", { order_id: "DH-2026-0042" })
```

**Prioritás:** P2 — következő sprint, ha van kapacitás.

---

## Firebase automatikus eventek (5 db)

Ezek automatikusan tüzelnek, nem igényelnek beavatkozást.

| Event | Count | Users | Megjegyzés |
|-------|-------|-------|-----------|
| `page_opened` | 1,665 | 36 | Firebase auto |
| `page_view` | 483 | 171 | Firebase auto |
| `session_start` | 354 | 156 | Firebase auto |
| `first_visit` | 147 | 147 | Firebase auto |
| `user_engagement` | 116 | 55 | Firebase auto |

---

## Törölt eventek (Mate feedback — 2026-04-28)

| Event | Miért töröltük |
|-------|---------------|
| `order_failed_stockout` | App nem tudja detektálni |
| `order_failed_delay` | App nem tudja detektálni |
| `savings_counter_viewed` | Duplikátum a cart view-val |
| `recap_reorder_clicked` | Nem létező funkció |
| `checkout_completed` | Duplikátum: order_created |
| `reorder_panel_viewed` | Nem érthető, nem kész feature |
| `reorder_panel_clicked` | Nem érthető, nem kész feature |
| `order_reason_selected` | DH-83 más topic |
| `order_reason_skipped` | DH-83 más topic |
| `founding50_expired` | Még nem releváns |
| `founding50_churned` | Még nem releváns |

---

## GA4 Custom Dimensions (regisztrálva 2026-04-29)

| Dimension | Parameter | Leírás |
|-----------|-----------|--------|
| Banner State | `banner_state` | Founding 50 banner állapota |
| Batch Ordering ID | `batch_ordering_id` | Batch rendelés azonosító |
| Batch Page ID | `batch_page_id` | Batch oldal azonosító |
| Benefit Dimension | `benefit_dimension` | Kedvezmény típusa |
| Campaign | `campaign` | Kampány azonosító |
| Campaign Name | `campaign_name` | Kampány neve |
| Enrollment Source | `enrollment_source` | Regisztráció forrása |

**További regisztrálandók (ha Mate küldi):**

| Parameter | Melyik eventhez | Prioritás |
|-----------|----------------|-----------|
| `cart_value` | checkout_started | P1 |
| `order_id` | order_created, campaign_order, order_cancelled | P0 |
| `order_value` | order_created, campaign_order, repeat_order_created | P0 |
| `item_count` | checkout_started, order_created | P1 |
| `days_since_first` | repeat_order_created | P0 |
| `user_id` | registration_completed | P0 |
| `cancel_reason` | order_cancelled | P1 |
| `total_savings` | threshold events, recap_viewed | P1 |

---

## Konszolidált Jira ticket: DH-181

**Minden analytics javítás egyetlen ticketben.** A régi ticketek (DH-129, DH-169, DH-171, DH-178, DH-179, DH-180) lezárandók, hivatkozással DH-181-re.

Lásd a DH-181 ticket tartalmát a Jira-ban.
