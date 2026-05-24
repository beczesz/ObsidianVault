---
title: 00_DECISIONS_INDEX (Archive)
generated_by: librarian v0.3
generated_at: 2026-05-11
scope: /04_Archive/
mode: index
file_count: 32
---

# Historical Decisions Index

Az archívumban rögzített döntések — precedens-értékkel a jelenlegi munkához. Strategic / Tactical / Operational bontás. Minden tétel: `path` + szövegszerű kontextus (sor-szintű referencia ahol egyértelmű).

---

## Strategic — irányt szabó, hosszú távú

### DHOP — Co-venture modell
- **Forrás:** `02_Areas/Deák Húsüzlet/Business Development/pilot-husuzlet/pilot-concept.md` (v1.3, 2026-03-05)
- **Döntés:** Exar Labs első co-venture pilot — saját tőke, full marketing ownership, revenue share return.
- **Forrás:** `business-model-canvas-v1.0.md` frontmatter — "Exar Labs owns platform, marketing, and business development (funded from own capital); butcher shop owns production, quality, and delivery; return via revenue share."

### DHOP — Architektúra-pivot single PWA-ra
- **Forrás:** `dev-roadmap-v1.2.md` (2026-03-25) frontmatter
- **Döntés:** Az admin/operátor felület (mészáros + futár) NEM külön alkalmazás, hanem a fő PWA-n belüli külön nézet, role-based tab bar váltással (DHOP-52 Epic). DHOP-29, DHOP-34 redundánssá vált — törölt ticketek.

### DHOP — Growth Flywheel mint engine
- **Forrás:** `business-model-canvas-v2.0.md` frontmatter
- **Döntés:** BMC v2.0-ban Growth Flywheel hozzáadva (v1.0-ból hiányzott). Customer segments priorizálva early adopter szegmensre, value prop rangsor korrigálva, guest-first UX, sávos revenue share modell.

### AI-Human Think Engine — háromszereplős cognition modell
- **Forrás:** `02_Areas/Deák Húsüzlet/think engine/AI - Human Think engine.md` (v0.3, 2026-03-31)
- **Döntés:** Human = intent & reality; ChatGPT = strategic cognition; Claude = operational cognition. v0.2-ben Claude strategic dialogue role hozzáadva (1.3), Context Management protokoll bevezetve (5.1).

### Project Engine — 01_PROJECT_STATE.md mint kontroll-fájl
- **Forrás:** `02_Areas/Deák Húsüzlet/think engine/Project Engine.md` (v0.2, 2026-03-31)
- **Döntés:** Bármely projekthez egy `01_PROJECT_STATE.md` kontroll-fájl, amit AI ágensek olvasnak/írnak. (Jelenleg a `general-utils:project-engine` skill implementálja.)

### CPS csapat — alázat mint első érték
- **Forrás:** `02_Areas/Sonrisa/CPS/Team/Bakonyi Peti.md` (2026-02-16)
- **Döntés:** "A CPS csapat alkotmányának az első értéke amit számon kérek úgy magamon mint máson is az az alázat." Konkrét HR helyzetben hivatkozott alapelv.

### Exar Labs 2025 — válság-narratíva
- **Forrás:** `02_Areas/ExarLabs/Jegyzetek.md` (2026-02-17)
- **Döntés/diagnózis:** "2025 – Válság és megtisztulás éve". Outsourcing-piac szűkülése, romániai adóoptimalizáció megszűnése. 2026 stratégia kontextusa.

---

## Tactical — projekt-szintű, közép távú

### DHOP — Google OAuth primary, Facebook OAuth post-MVP
- **Forrás:** `pilot-concept.md` v1.3 frontmatter: "Google OAuth as primary"
- **Forrás:** `mvp-spec-v1.2.md` + `dev-roadmap.md` v1.1: "DHOP-9 Facebook OAuth optional/post-MVP"

### DHOP — Phase exit criteria hozzáadva
- **Forrás:** `dev-roadmap.md` v1.1 frontmatter: "phase exit criteria hozzáadva; Meta App Review megjegyzés javítva"

### DHOP — 7 epic / 37 task MVP scope
- **Forrás:** `mvp-spec-v1.2.md` (v1.2, 2026-03-05) frontmatter: "Full MVP specification for the online ordering pilot webapp — 7 epics, 37 tasks". Epic 6: 6 task, customer order history merged into customer list (DHOP-37).

### DHOP — DHOP-52 Epic strukturális változás
- **Forrás:** `dev-roadmap-v1.2.md`: Új fázisok: 5 (Butcher & Courier Interface), 6 (Statisztikák + Analytics), 7 (UX Polish + GDPR). DHOP-30–33 courier ticketek beolvadnak DHOP-52 Epicbe.

### Pályázat — Contestare stratégia
- **Forrás:** `02_Areas/Pályázat/2025.11.28 Contestare - meeting v1.1.md`
- **Döntés:** ~640.000 RON költségvetés-vágás kezelése. Cercetare contractuală + Consultanță Inovare + Consultanță Cercetare Industrială "nefundamentat" indoklással kihúzva — contesting irány: szolgáltatások szükségességének dokumentálása.

### Pályázat — TRL 3 validáció dokumentációs követelmény
- **Forrás:** `02_Areas/Pályázat/2025.10.16 RegioConsult meeting.md`
- **Döntés:** 8-10 screenshot, román nyelvű kurzus, 3-4 dokumentáció, dátum nélküli munkanapló, "hivatalos kinézet" (Kinga megjegyzés).

### Navigátor Podcast — DSZ négy felvétel
- **Forrás:** `02_Areas/Navigátor Podcast/Episodes/Digitális Székelyföld/Összefoglalás.md`
- **Döntés (post-hoc):** Négy podcast készült: Palkovics László, Charaf Hassan, Süket Csaba, Láng Máté. Kiss Gergellyel a brit anyavállalat tiltása miatt nem volt felvétel.

---

## Operational — fájl-szintű, nap-szintű

- **Forrás:** `01_Projects/Sonrisa/CPS/EPRIVO.md` és `Projects/EPRIVO.md` — "Meet with Santosh 2025-09-03" → done.
- **Forrás:** `01_Projects/Sonrisa/CPS/Projects/ASH.md` — SharePoint Account link rögzítve; "we need to figure out when it starts" (függőben).
- **Forrás:** `01_Projects/Sonrisa/CPS/Projects/MelindaSteel n8n.md` — "TIG is needed 2025-12-02"; "Első workflow számlázava lett" (November vége).
- **Forrás:** `01_Projects/Szervezet fejlesztés/Veszprém - Kecskemét körút/Utiterv.md` — útvonal Udvarhely→Vásárhely→Kecskemét, csütörtök 8:00 indulás.
- **Forrás:** `01_Projects/Szervezet fejlesztés/Veszprém - Kecskemét körút/Kecskemét előadás 2025.09.26.md` — "Válaszolni Dani Erzsébetnek" → done 2025-10-14.

---

## Megjegyzés a verziókról

A pilot-husuzlet/ alatt több BMC és roadmap verzió is jelen van:
- BMC: v1.0 (2026-03-27) + v2.0 (2026-03-28) — v2.0 a kanonikus
- Roadmap: v1.1 (`dev-roadmap.md`) + v1.2 (`dev-roadmap-v1.2.md`) — v1.2 a kanonikus
- MVP spec: csak v1.2 jelen
- Pilot concept: csak v1.3 jelen

Történetileg minden verzió fontos (precedens), retrieve módban a v2.0 / v1.2 / v1.3 a "current archived" verzió.
