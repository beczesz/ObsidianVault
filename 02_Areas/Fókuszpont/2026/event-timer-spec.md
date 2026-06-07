---
title: Event Time Tracker - Requirements Document
date: 2026-06-02
author: Becze Szabolcs
status: active
description: Specifikáció a Fókuszpont 2026 eseményhez épített böngészős időkövetőhöz. Tartalmazza a funkcionális követelményeket, UI komponenseket, timer logikát, design-rendszert és a rögzített programot.
version: 1.1
id: faeffd6e-8016-465c-8be0-3b7bd2b29867
index_schema_version: 1
---

# Event Time Tracker – Requirements Document

## 1. Overview

The Event Time Tracker is a simple, web-based application designed to help organizers monitor and manage the progress of events based on a predefined schedule. It allows real-time tracking of agenda items, provides countdowns, and enables quick adjustments when timing shifts occur.

## 2. Objectives

- Provide a visual, user-friendly interface for tracking event agenda progress.
- Display current agenda item with a countdown.
- Allow navigation between items (next, previous).
- Permit live time adjustments (e.g., add/subtract minutes).
- Ensure the solution is lightweight, offline-capable, and fast.

## 3. Functional Requirements

### 3.1 Agenda Initialization

The agenda is hardcoded into the application as a JavaScript array of objects.

Each agenda item includes:
- `title`: String – description of the agenda item.
- `duration`: Number – time allocated in minutes.
- `optional: startTime` (for reference, not binding).

```json
[
  { "title": "Welcome Speech", "duration": 10 },
  { "title": "Keynote Presentation", "duration": 30 },
  { "title": "Coffee Break", "duration": 15 },
  { "title": "Panel Discussion", "duration": 45 }
]
```

### 3.2 UI Components

**Header:** Displays the title of the application (e.g., "Event Time Tracker").

**Current Item Display:**
- Title of current agenda item.
- Remaining time in mm:ss format.
- Visual indicator (e.g., progress bar or color change).

**Control Panel:**
- Play/Pause button: Starts/stops the countdown.
- Next button: Moves to the next agenda item.
- Previous button: Moves to the previous agenda item.
- +1 min / -1 min: Adjusts current item's remaining time.

**Upcoming Items List:**
- List of next items in schedule with titles and durations.

### 3.3 Timer Logic

When Play is pressed, the timer begins counting down from the current item's duration.

When it reaches zero, the app:
- Auto-pauses.
- Highlights that the item has ended.
- Awaits user action to proceed (manual Next).

## 4. Non-Functional Requirements

### 4.1 Platform

- Runs entirely in the browser (desktop or mobile).
- No backend required.
- Works offline after initial load (can use a local HTML file).

### 4.2 Performance

- Loads in under 1 second.
- Low memory footprint.

### 4.3 Design

- Responsive layout.
- Clean and minimal design for visibility at a distance (e.g., projected).
- Font and contrast optimized for quick reading.

## 5. Stretch Goals (Optional Features)

- Dark Mode toggle. (Az alap téma eleve sötét, lásd 5.5.)
- Real-time clock showing current time. **(KÉSZ)** Élo óra a fejlécben.
- Agenda Export/Import. **(Részben kész)** Szerkeszto tab: a program szövegesen bemásolható/módosítható (`HH:MM | Cím | Közreműködő | perc`), "Alkalmaz" azonnal frissít. Session-only, nem ment fájlba.
- Notifications (sound/vibration) when a time block ends.
- Elapsed Time Indicator (how much the schedule is ahead/behind).

## 5.1 Implementation status (v1.1)

Egyetlen önálló `event-timer.html` fájl, inline CSS + JS, nincs külso függoség.

| Funkció | Állapot |
|---|---|
| Countdown mm:ss, auto-pause 0-nál, ended-banner | Kész |
| Play/Szünet, Elozo/Következo, +1/-1 perc | Kész |
| Progress bar + warning (≤30%) / danger (≤15%) színváltás | Kész |
| Program lista, kattintható sorok (ugrás a pontra) | Kész |
| Két tab: Timer+Program / Szerkeszto | Kész |
| Élo óra | Kész |
| Szöveges program-szerkeszto (session-only) | Kész |
| Reszponzív, projektorra méretezett countdown (`clamp` 4.5-9rem) | Kész |

## 5.5 Branding és design-rendszer

Minden évnek saját brand-színe van. A timer UI az adott év primary színét használja.

| Év | Primary szín |
|---|---|
| 2026 | `#003f5c` |

### Theme döntés (scene sentence)

> Szervezo egy elsötétített templomi/közösségi térben, kivetíton vagy laptopon figyeli a hátralévo idot, 20:00 körül, nyugodt liturgikus hangulatban.

Ez sötét témát kíván: alacsony fénykibocsátás, magas kontraszt a nagy countdown-számokon. A countdown a hero elem, az olvashatósága az elso számú szempont.

### Színstratégia: Restrained, brand-accenttel

A `#003f5c` (Fókuszpont 2026 primary) OKLCH-ban `oklch(0.42 0.078 233)`. A sötét neutrálokat a brand-hue (233) felé tinteljük, nagyon alacsony chromával. A brand-kék az identitás- és interakció-accenteken jelenik meg (fejléc cím, progress bar, aktív tab, primary gombok), nem önti el a teljes felületet, hogy a fehér countdown kontrasztja maximális maradjon.

Tiltások (vault-szintű, betartva): nincs `#000`/`#fff`, nincs gradient-szöveg, nincs színes oldalcsík (`border-left/right > 1px`), nincs dekoratív glassmorphism, nincs gondolatjel.

### Tipográfia

System sans (`system-ui`) a UI-chrome-hoz, monospace (`ui-monospace` / SF Mono fallback) + `font-variant-numeric: tabular-nums` minden numerikához (countdown, óra, idopontok, perc). A fix-szélességu számjegyek miatt a countdown nem "ugrál" másodpercenként.

**Offline font-döntés:** a spec offline-képességet ír elo (4.1), ezért szándékosan NINCS Google Fonts betöltés. A vault DESIGN.md Inter + JetBrains Mono fontokat ajánl a dashboardokhoz, de azok localhoston, hálózattal futnak. Ez a timer egy önálló, `file://`-rol is megnyitható eszköz, így csak system-fontokra támaszkodik.

### Motion

Egyetlen exponenciális ease-out token (`cubic-bezier(0.16, 0.84, 0.32, 1)`). Nincs bounce, nincs elastic, nincs layout-property animáció. Az "ido lejárt" állapot opacity-pulse-szal jelez (nem layout).

## 6. Technologies

- HTML5
- CSS3 (or TailwindCSS for rapid styling)
- Vanilla JavaScript (or React for component-based architecture)
- Optional: Service Worker for offline support

## 7. Assumptions & Limitations

- All agenda data is static unless the code is edited or agenda import is implemented.
- Time tracking is based on client-side time, so switching tabs or device sleep may cause drift unless accounted for.

## 8. Example User Flow

1. Open the web page in a browser.
2. See the first agenda item and its duration.
3. Click Play to start the countdown.
4. During the session, click +1 min if the speaker needs more time.
5. Click Next to go to the next item when ready.
6. Repeat until the event ends.

## 9. Fixed Program – Fókuszpont 2026

| Idő | Perc | Program | Közremuködo |
|---|---|---|---|
| 19.45 - 20.00 | 15 p | ÉNEK | Csiszér László |
| 20.00 - 20.15 | 15 p | KÖSZÖNTÉS | Becze Szabolcs és Júlia / Márton József főesperes |
| 20.15 - 20.45 | 30 p | TANÚSÁGTÉTELEK | Gergely Dávid és Tóth Jácinta |
| 20.45 - 21.00 | 15 p | ÉNEK | Csiszér László |
| 21.00 - 21.45 | 45 p | BESZÉLGETÉS A PÜSPÖK ATYÁVAL – fiatalok kérdeznek | Fábry Kornél ppk., Péter Géza és Péter Ágota |
| 21.45 - 22.00 | 15 p | ÉNEK | Csiszér László |
| 22.00 - 22.45 | 45 p | SZENTSÉGIMÁDÁS | Ilonka Eszter, Nagy Mátyás, Vass Réka, Fábry Kornél ppk. |
| 22.45 - 23.00 | 15 p | ÉNEK – DICSŐÍTÉS | Csiszér László |
| 23.00 - | - | AGAPÉ | Szülők |
