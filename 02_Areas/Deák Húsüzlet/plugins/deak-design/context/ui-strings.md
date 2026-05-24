# DH – UI Strings & Localization
> Verzió: 1.0 · Dátum: 2026-03-22
> Felület: Butcher & Courier Operational Interface
> Elsődleges nyelv: **Román (RO)** · Másodlagos: Magyar (HU)
> Hatókör: 10 képernyő + összes hibaüzenet, üres állapot, megerősítő dialógus, toast

---

## Konvenciók

| # | Szabály |
|---|---------|
| 1 | **Elsődleges nyelv: román.** Minden string RO-ban kerül implementálásra. A HU az operátor anyanyelvére való tekintettel megjelenik ahol helye van (pl. push notification, hibák). |
| 2 | **Stílus: tömör, közvetlen.** Az operátor munkavégzés közben használja az appot — nincs idő hosszú szövegekre. |
| 3 | **CTA-k: igével kezdenek.** „Începe prepararea" nem „Preparare". |
| 4 | **Hibák: Mi történt + Miért + Mit tegyen.** Minden hibaüzenet tartalmazza a következő lépést. |
| 5 | **Személyes hang: informális (tu).** Belső operatív eszköz, nem B2C felület. |
| 6 | **Státusz labelek: a Frappe `custom_status` értékeit tükrözik.** Ne változzon szabadon. |

---

## 1. Navigáció — Bottom Tab Bar

| Key | Romanian | Hungarian | Megjegyzés |
|-----|----------|-----------|------------|
| `nav.butcher` | 🔪 Preparare | 🔪 Előkészítés | Tab 1, ikon: knife |
| `nav.courier` | 🚚 Livrare | 🚚 Kiszállítás | Tab 2, ikon: truck |
| `nav.stats` | 📊 Statistici | 📊 Statistikák | Tab 3, ikon: chart |

---

## 2. Státusz labelek (StatusBadge)

> Ezek a Frappe `custom_status` mezőhöz kötött értékek. **Ne módosítsd a román értékeket** — API-n keresztül szinkronizálnak.

| Key | Romanian (appban) | Hungarian | Badge szín | Frappe érték |
|-----|-------------------|-----------|------------|--------------|
| `status.new` | Comandă nouă | Új rendelés | info / info-light | `Comandă nouă` |
| `status.processing` | În procesare | Előkészítés alatt | warning / warning-light | `În procesare` |
| `status.ready` | Pregătit pentru livrare | Kiszállításra kész | secondary / secondary-light | `Pregătit pentru livrare` |
| `status.enroute` | În curs de livrare | Úton van | primary / primary-light | `În curs de livrare` |
| `status.delivered` | Livrat | Kézbesítve | success / success-light | `Livrat` |
| `status.closed` | Închis | Lezárva | gray | `Închis` |

---

## 3. Screen 1 – Napi rendelési lista (Mészáros)

| Key | Romanian | Hungarian | Típus | Megjegyzés |
|-----|----------|-----------|-------|------------|
| `screen1.header.title` | Preparare | Előkészítés | Screen header | H1 semibold |
| `screen1.header.date` | {data} | {dátum} | Header jobb | Mai dátum, pl. „22 mar." |
| `screen1.section.title` | Comenzile de azi | Mai rendelések | Section label | |
| `screen1.filter.new` | Comandă nouă | Új rendelés | Filter chip | Státusz szűrő |
| `screen1.filter.processing` | În procesare | Előkészítés alatt | Filter chip | |
| `screen1.filter.ready` | Pregătit pentru livrare | Kiszállításra kész | Filter chip | |
| `screen1.filter.all` | Toate | Összes | Filter chip | Alapértelmezett |
| `screen1.summary.fresh` | 🐷 Porc proaspăt: {x} kg | 🐷 Friss sertés: {x} kg | Összesítő csík | |
| `screen1.summary.smoked` | 🥩 Afumat: {x} kg | 🥩 Füstölt: {x} kg | Összesítő csík | |
| `screen1.summary.sausage` | 🌭 Cârnați: {x} kg | 🌭 Kolbász: {x} kg | Összesítő csík | |
| `screen1.summary.deli` | 🥓 Mezeluri: {x} kg | 🥓 Felvágott: {x} kg | Összesítő csík | |
| `screen1.order.products` | {n} produse | {n} termék | OrderCard meta | |
| `screen1.empty.title` | Nicio comandă azi | Nincs mai rendelés | Empty state cím | |
| `screen1.empty.subtitle` | Comenzile noi vor apărea automat. | Az új rendelések automatikusan megjelennek. | Empty state subtitle | |

---

## 4. Screen 2 – Rendelés előkészítési nézet

| Key | Romanian | Hungarian | Típus | Megjegyzés |
|-----|----------|-----------|-------|------------|
| `screen2.header.title` | Comanda #{id} | Rendelés #{id} | Screen header | |
| `screen2.section.products` | Produse de preparat | Előkészítendő termékek | Section label | |
| `screen2.product.unit` | {x} kg | {x} kg | Inline | |
| `screen2.warning.unavailable` | ⚠️ Produs indisponibil | ⚠️ Termék nem elérhető | Warning sáv | bg-warning-light |
| `screen2.warning.unavailable.note` | Contactați clientul dacă este necesar. | Ha szükséges, vegye fel a kapcsolatot a vásárlóval. | Warning al-szöveg | |
| `screen2.cta.start` | Începe prepararea | Előkészítés indítása | Primary CTA | Státusz: Comandă nouă → În procesare |
| `screen2.cta.ready` | Pregătit pentru livrare | Kiszállításra kész | Primary CTA | Státusz: În procesare → Pregătit |
| `screen2.status.alreadyReady` | ✓ Comanda este pregătită | ✓ A rendelés kész | Confirm szöveg | Zöld, gomb helyett jelenik meg |
| `screen2.note.label` | Notă internă | Belső megjegyzés | Textarea label | Opcionális |
| `screen2.note.placeholder` | Adaugă o notă pentru curier... | Megjegyzés a futárnak... | Textarea placeholder | |

---

## 5. Screen 3 – Termék elérhetőség toggle

| Key | Romanian | Hungarian | Típus | Megjegyzés |
|-----|----------|-----------|-------|------------|
| `screen3.header.title` | Produse | Termékek | Screen header | |
| `screen3.category.fresh` | Porc proaspăt | Friss sertés | Kategória fejléc | |
| `screen3.category.smoked` | Afumat | Füstölt | Kategória fejléc | |
| `screen3.category.sausage` | Cârnați & Salam | Kolbász & Szalámi | Kategória fejléc | |
| `screen3.category.deli` | Mezeluri | Felvágott | Kategória fejléc | |
| `screen3.toggle.available` | Disponibil | Elérhető | Toggle ON state | Aria-label |
| `screen3.toggle.unavailable` | Indisponibil | Nem elérhető | Toggle OFF state | Aria-label |
| `screen3.toast.saved` | Disponibilitate salvată | Elérhetőség mentve | Toast (success) | |
| `screen3.empty` | Niciun produs în această categorie | Nincs termék ebben a kategóriában | Empty state | |

---

## 6. Screen 4 – Napi kiszállítási lista (Futár)

| Key | Romanian | Hungarian | Típus | Megjegyzés |
|-----|----------|-----------|-------|------------|
| `screen4.header.title` | Livrare | Kiszállítás | Screen header | |
| `screen4.header.date` | {data} | {dátum} | Header jobb | |
| `screen4.summary.delivered` | ✅ Livrat: {n} | ✅ Kézbesítve: {n} | Összesítő chip | |
| `screen4.summary.enroute` | 🚛 În drum: {n} | 🚛 Úton: {n} | Összesítő chip | |
| `screen4.summary.ready` | ⏳ Gata: {n} | ⏳ Kész: {n} | Összesítő chip | |
| `screen4.filter.ready` | Pregătit pentru livrare | Kiszállításra kész | Filter chip | |
| `screen4.filter.enroute` | În curs de livrare | Úton van | Filter chip | |
| `screen4.filter.delivered` | Livrat | Kézbesítve | Filter chip | |
| `screen4.filter.all` | Toate | Összes | Filter chip | Alapértelmezett |
| `screen4.order.products` | {n} produse | {n} termék | OrderCard meta | |
| `screen4.empty.title` | Nicio livrare azi | Nincs mai kiszállítás | Empty state cím | |
| `screen4.empty.subtitle` | Comenzile pregătite vor apărea aici. | A kész rendelések itt jelennek meg. | Empty state subtitle | |

---

## 7. Screen 5 – Kiszállítás részletei

| Key | Romanian | Hungarian | Típus | Megjegyzés |
|-----|----------|-----------|-------|------------|
| `screen5.header.title` | {customerName} | {customerName} | Screen header | Vásárló neve |
| `screen5.cta.call` | 📞 Apel | 📞 Hívás | Secondary CTA | tel: link |
| `screen5.cta.maps` | 🗺 Deschide în Google Maps | 🗺 Megnyitás Google Maps-ben | Secondary CTA | |
| `screen5.order.summary` | {n} produse · {total} RON | {n} termék · {total} RON | Rendelés összesítő | |
| `screen5.order.details.show` | Arată detalii ▼ | Részletek mutatása ▼ | Collapsible toggle | |
| `screen5.order.details.hide` | Ascunde detalii ▲ | Részletek elrejtése ▲ | Collapsible toggle | |
| `screen5.cta.start` | 🚚 Pornește livrarea | 🚚 Kiszállítás indítása | Primary CTA | Státusz → În curs de livrare |
| `screen5.cta.delivered` | ✓ Marchează ca livrat | ✓ Kézbesítve jelölés | Primary CTA | Státusz: en route esetén |
| `screen5.timeSlot.label` | Interval orar | Időablak | Label | |

---

## 8. Screen 6 – Kézbesítés megerősítése

| Key | Romanian | Hungarian | Típus | Megjegyzés |
|-----|----------|-----------|-------|------------|
| `screen6.header.title` | Confirmă livrarea | Kézbesítés megerősítése | Screen header | |
| `screen6.method.personal` | Predat personal | Személyesen átadva | Checkbox label | |
| `screen6.method.door` | Lăsat la ușă (la cererea clientului) | Ajtó elé hagyva (vásárló kérése) | Checkbox label | |
| `screen6.note.label` | Notă (opțional) | Megjegyzés (opcionális) | Textarea label | |
| `screen6.note.placeholder` | Adaugă o notă despre livrare... | Megjegyzés a kézbesítésről... | Textarea placeholder | |
| `screen6.cta.confirm` | ✓ Livrat – Finalizat | ✓ Kézbesítve – Befejezés | Primary CTA | Végleges művelet |
| `screen6.validation.noMethod` | Selectează metoda de livrare. | Válassz kézbesítési módot. | Validation error | Checkbox kötelező |

---

## 9. Screen 7–9 – Statisztika főnézet (Heti / Havi)

| Key | Romanian | Hungarian | Típus | Megjegyzés |
|-----|----------|-----------|-------|------------|
| `stats.header.title` | Statistici | Statisztikák | Screen header | |
| `stats.period.daily` | Zilnic | Napi | Segmented control | |
| `stats.period.weekly` | Săptămânal | Heti | Segmented control | |
| `stats.period.monthly` | Lunar | Havi | Segmented control | |
| `stats.nav.prev` | ‹ | ‹ | Period nav gomb | Accessibility: aria-label = „Perioada anterioară" |
| `stats.nav.next` | › | › | Period nav gomb | Disabled ha jövőbe mutatna |
| `stats.nav.next.disabled.label` | Perioada curentă | Jelenlegi időszak | Aria-label (disabled) | |
| `stats.period.label.weekly` | {startDate} – {endDate} | {startDate} – {endDate} | Period label | pl. „16 mar. – 22 mar." |
| `stats.period.label.monthly` | {luna} {an} | {hónap} {év} | Period label | pl. „Martie 2026" |
| `stats.period.label.daily` | {zi}, {data} | {nap}, {dátum} | Period label | pl. „Duminică, 22 mar." |
| `stats.card.orders` | Comenzi | Rendelések | Kártya label | |
| `stats.card.revenue` | Venituri | Bevétel | Kártya label | |
| `stats.card.quantity` | Cantitate livrată | Kiszállított mennyiség | Kártya label | |
| `stats.card.unit.orders` | buc | db | Kártya egység | |
| `stats.card.unit.revenue` | RON | RON | Kártya egység | |
| `stats.card.unit.quantity` | kg total | kg összesen | Kártya egység | |
| `stats.chart.title.weekly` | Venit zilnic (RON) – vedere săptămânală | Napi bontás (RON) – heti nézet | Chart cím | |
| `stats.chart.title.monthly` | Venit zilnic (RON) – {luna} | Napi bevétel (RON) – {hónap} | Chart cím | |
| `stats.topProducts.title` | Top produse (kg) | Top termékek (kg) | Section label | Havi nézetben |
| `stats.orders.section` | Comenzile perioadei | Időszak rendelései | Section label | |
| `stats.orders.count` | Comenzile perioadei ({n}) | Időszak rendelései ({n}) | Section label | |

---

## 10. Screen 10 – Statisztika Napi nézet

| Key | Romanian | Hungarian | Típus | Megjegyzés |
|-----|----------|-----------|-------|------------|
| `stats.daily.orders.section` | Comenzile de azi | Mai rendelések | Section label | |
| `stats.daily.noChart.info` | În vizualizarea zilnică nu există grafic — vedeți comenzile zilei. | Napi nézetben nincs diagram — csak a nap rendelései láthatók. | Info note | bg-info-light |
| `stats.daily.empty.title` | Nicio comandă în această zi | Ezen a napon nincs rendelés | Empty state cím | |
| `stats.daily.empty.subtitle` | Selectați o altă zi cu ‹ ›. | Válasszon másik napot a ‹ › gombokkal. | Empty state subtitle | |

---

## 11. Hibaüzenetek (Error Messages)

> Struktúra: **Mi történt + Miért + Mit tegyen**

| Key | Romanian | Hungarian | Típus | Trigger |
|-----|----------|-----------|-------|---------|
| `error.network` | Nu s-a putut conecta. Verificați conexiunea la internet. | Nincs kapcsolat. Ellenőrizze az internetet. | Toast / Banner | Nincs net |
| `error.orders.load` | Comenzile nu s-au putut încărca. Trageți în jos pentru a reîncărca. | A rendelések betöltése sikertelen. Húzza le a frissítéshez. | Inline error | API fail |
| `error.status.update` | Actualizarea statusului a eșuat. Reîncercați. | Státuszfrissítés sikertelen. Próbálja újra. | Toast (error) | PUT API fail |
| `error.status.conflict` | Comanda a fost modificată între timp. Reîncărcați pagina. | A rendelést közben módosították. Töltse újra az oldalt. | Toast (error) | 409 Conflict |
| `error.product.toggle` | Nu s-a putut modifica disponibilitatea. Reîncercați. | Az elérhetőség módosítása sikertelen. Próbálja újra. | Toast (error) | PATCH fail |
| `error.delivery.confirm` | Confirmarea livrării a eșuat. Reîncercați sau contactați adminul. | Kézbesítés megerősítése sikertelen. Próbálja újra vagy értesítse az adminisztátort. | Toast (error) | PUT fail |
| `error.stats.load` | Statisticile nu s-au putut încărca. | A statisztikák betöltése sikertelen. | Inline error | Stats API fail |
| `error.generic` | A apărut o eroare. Reîncercați. | Hiba lépett fel. Próbálja újra. | Toast (error) | Általános fallback |
| `error.session.expired` | Sesiunea a expirat. Vă rugăm să vă autentificați din nou. | A munkamenet lejárt. Kérjük, jelentkezzen be újra. | Full-screen / Modal | Auth token expired |

---

## 12. Üres állapotok (Empty States)

> Struktúra: **Mi ez + Miért üres + Hogyan kezdje**

| Key | Romanian | Hungarian | Képernyő |
|-----|----------|-----------|----------|
| `empty.orders.today` | Nicio comandă azi. Comenzile noi apar automat. | Nincs mai rendelés. Az új rendelések automatikusan megjelennek. | Screen 1 |
| `empty.orders.filtered` | Nicio comandă cu statusul selectat. | Nincs rendelés a kiválasztott állapotban. | Screen 1 (filter aktív) |
| `empty.deliveries.today` | Nicio livrare azi. Comenzile pregătite vor apărea aici. | Nincs mai kiszállítás. A kész rendelések itt jelennek meg. | Screen 4 |
| `empty.deliveries.filtered` | Nicio livrare cu statusul selectat. | Nincs kiszállítás a kiválasztott állapotban. | Screen 4 (filter aktív) |
| `empty.stats.period` | Nicio comandă în această perioadă. | Ebben az időszakban nincs rendelés. | Screen 7–10 |
| `empty.products.category` | Niciun produs în această categorie. | Nincs termék ebben a kategóriában. | Screen 3 |

---

## 13. Megerősítő dialógusok (Confirmation Dialogs)

> Struktúra: Cím (mit csinál?) + Gomb (cselekvés) / Mégse

### 13.1 Státuszváltás: Comandă nouă → În procesare

| Elem | Romanian | Hungarian |
|------|----------|-----------|
| **Cím** | Începi prepararea comenzii #{id}? | Elindítod a #{id} rendelés előkészítését? |
| **Confirm gomb** | Da, începe | Igen, elindítom |
| **Cancel gomb** | Anulează | Mégse |

### 13.2 Státuszváltás: În procesare → Pregătit pentru livrare

| Elem | Romanian | Hungarian |
|------|----------|-----------|
| **Cím** | Marchezi comanda #{id} ca pregătită? | Kiszállításra késznek jelölöd a #{id} rendelést? |
| **Confirm gomb** | Pregătit | Kész |
| **Cancel gomb** | Anulează | Mégse |

### 13.3 Státuszváltás: Pregătit → În curs de livrare

| Elem | Romanian | Hungarian |
|------|----------|-----------|
| **Cím** | Pornești livrarea pentru {customerName}? | Elindítod a kiszállítást {customerName}-hez? |
| **Megjegyzés** | Statusul se va schimba în „În curs de livrare". | A státusz „Úton van"-ra változik. |
| **Confirm gomb** | Pornește | Indítom |
| **Cancel gomb** | Anulează | Mégse |

### 13.4 Kézbesítés megerősítése (végleges)

| Elem | Romanian | Hungarian |
|------|----------|-----------|
| **Cím** | Confirmi livrarea pentru {customerName}? | Megerősíted a kézbesítést {customerName} részére? |
| **Megjegyzés** | Această acțiune nu poate fi anulată. | Ez a művelet nem vonható vissza. |
| **Confirm gomb** | Livrat | Kézbesítve |
| **Cancel gomb** | Anulează | Mégse |

---

## 14. Betöltési állapotok (Loading States)

| Key | Romanian | Hungarian | Hol jelenik meg |
|-----|----------|-----------|----------------|
| `loading.orders` | Se încarcă comenzile... | Rendelések betöltése... | Screen 1, 4 |
| `loading.status` | Se actualizează statusul... | Státusz frissítése... | Status gomb felett / spinner |
| `loading.save` | Se salvează... | Mentés... | Screen 3 toggle után |
| `loading.stats` | Se încarcă statisticile... | Statisztikák betöltése... | Screen 7–10 |
| `loading.delivery.confirm` | Se finalizează livrarea... | Kézbesítés rögzítése... | Screen 6 CTA megnyomás után |

---

## 15. Sikeres műveletek (Toast / Success)

| Key | Romanian | Hungarian | Trigger |
|-----|----------|-----------|---------|
| `toast.status.processing` | Preparare începută ✓ | Előkészítés elindítva ✓ | Státusz → În procesare |
| `toast.status.ready` | Pregătit pentru livrare ✓ | Kiszállításra kész ✓ | Státusz → Pregătit |
| `toast.status.enroute` | Livrare pornită ✓ | Kiszállítás elindítva ✓ | Státusz → În curs de livrare |
| `toast.delivery.confirmed` | Livrare confirmată! ✓ | Kézbesítés megerősítve! ✓ | Státusz → Livrat |
| `toast.product.saved` | Disponibilitate salvată ✓ | Elérhetőség mentve ✓ | Toggle PATCH sikeres |

---

## 16. Nap- és hónapnevetek (Lokalizáció)

### Naprövidítések — Heti chart (X tengely)

| Nap | Romanian (chart) | Hungarian (chart) |
|-----|------------------|-------------------|
| Hétfő | L | H |
| Kedd | Ma | K |
| Szerda | Mi | Sz |
| Csütörtök | Jo | Cs |
| Péntek | Vi | P |
| Szombat | Sâ | Sz |
| Vasárnap | Du | V |

### Hónapnevetek

| # | Romanian | Hungarian |
|---|----------|-----------|
| 1 | Ianuarie | január |
| 2 | Februarie | február |
| 3 | Martie | március |
| 4 | Aprilie | április |
| 5 | Mai | május |
| 6 | Iunie | június |
| 7 | Iulie | július |
| 8 | August | augusztus |
| 9 | Septembrie | szeptember |
| 10 | Octombrie | október |
| 11 | Noiembrie | november |
| 12 | Decembrie | december |

### Napnevek (Napi period label)

| Nap | Romanian | Hungarian |
|-----|----------|-----------|
| Hétfő | Luni | Hétfő |
| Kedd | Marți | Kedd |
| Szerda | Miercuri | Szerda |
| Csütörtök | Joi | Csütörtök |
| Péntek | Vineri | Péntek |
| Szombat | Sâmbătă | Szombat |
| Vasárnap | Duminică | Vasárnap |

---

## 17. Fejlesztői megjegyzések (i18n Implementation Notes)

| # | Megjegyzés |
|---|------------|
| 1 | **Vue i18n ajánlott:** `vue-i18n` v9 composable API (`useI18n`, `t()`) |
| 2 | **Alapértelmezett locale:** `ro` — minden string ro-ban létezik kötelezően |
| 3 | **Fallback locale:** `hu` — ha ro string hiányzik, hu jelenik meg (fejlesztés közben) |
| 4 | **Státusz labelek kivétel:** a `custom_status` értékek román szövegek, ezek NEM fordítandók — a badge label az API értékéből jön közvetlenül |
| 5 | **Dátum formázás:** `Intl.DateTimeFormat('ro-RO')` Romanian locale-lal. Heti: „16 mar. – 22 mar.", Havi: „Martie 2026", Napi: „Duminică, 22 mar." |
| 6 | **Számformázás:** `Intl.NumberFormat('ro-RO')` — vessző tizedes elválasztó: „125,50 RON", „68,5 kg" |
| 7 | **{placeholder} értékek** futásidőben töltendők be (pl. `{id}`, `{customerName}`, `{n}`, `{total}`) |
| 8 | **Heti chart labelek** a `stats.chart.title.weekly` esetén dinamikusan a locale alapján generálandók (L/Ma/Mi/Jo/Vi/Sâ/Du RO esetén) |
| 9 | **Karakter terjeszkedés:** A román szövegek átlagosan 10-15%-kal hosszabbak a megfelelő magyaroknál. Gomboknál fix magasság ajánlott, ne fix szélesség. |
| 10 | **RTL:** nem szükséges |

---

## 18. Hiányzó / Jövőbeli stringek (TODO)

| # | String | Mikor kell |
|---|--------|-----------|
| 1 | Push notification szövegek (új rendelés érkezett) | Post-MVP |
| 2 | Onboarding / első bejelentkezés szövegek | Post-pilot |
| 3 | Admin dashboard stringek | Fázis 2 |
| 4 | Vásárló-értesítő SMS/email szövegek | Post-MVP |
| 5 | Offline mód banner | Ha PWA offline cache implementálva |

---

*Dokumentum státusza: **Draft v1.0** — Review szükséges Deák Húsmíves operátorokkal.*
