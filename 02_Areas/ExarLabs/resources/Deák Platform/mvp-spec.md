---
title: MVP Specification – Deák Húsmíves Online Platform
version: 1.2
date: 2026-03-05
author: Becze Szabolcs – Exar Labs
description: Full MVP specification for the online ordering pilot webapp — 7 epics, 37 tasks. Facebook OAuth (1.2) optional/post-MVP. Epic 6 has 6 tasks (customer order history merged into customer list, DHOP-37).
id: 58a2b9cc-679e-4c73-a510-7246cfeb5814
index_schema_version: 1
---

# MVP Specification – Deák Húsmíves Online Platform

_Version: 1.2 | Last updated: 2026-03-05_

---

## Scope & Constraints

This MVP is a **mobile-first progressive web app (PWA)** for piloting online ordering and home delivery for a local artisan butcher shop. It is intentionally minimal — the goal is validated learning, not feature completeness.

| Constraint | Value |
|-----------|-------|
| Platform | Mobile-first webapp (PWA) |
| Payment | Cash on delivery only (no gateway) |
| Stores | 1 store in pilot |
| Timeline | Pilot = 30 days after launch |
| Marketing | Handled fully by Exar Labs |

---

## Non-Functional Requirements

These requirements apply across all epics and must be met before launch:

| # | Requirement | Acceptance Criteria |
|---|-------------|-------------------|
| NFR-1 | Mobile-first performance | First Contentful Paint < 2s on 4G; page weight < 500KB per screen |
| NFR-2 | Security | HTTPS enforced; JWT tokens expire after 30 days; passwords bcrypt-hashed |
| NFR-3 | Uptime | 99% uptime during pilot (max ~7h downtime/month) |
| NFR-4 | Browser support | Latest Chrome, Firefox, Safari on Android/iOS; no IE |
| NFR-5 | Data integrity | No order can be placed twice (idempotent POST); no data loss on network failure |
| NFR-6 | Error handling | Every failed API call shows a user-friendly error message; no raw stack traces visible |
| NFR-7 | Accessibility | All forms operable by keyboard; sufficient color contrast (WCAG AA minimum) |

---

## Epic 1 – Authentication & User Onboarding
**Jira:** DHOP-1 (Epic) | Tasks: DHOP-8, DHOP-9, DHOP-10, DHOP-11, DHOP-12

**Goal:** Registration completable in under 60 seconds with minimal friction.

**Epic Acceptance Criteria:**
- A new user can register and reach the product catalog within 60 seconds
- A returning user can log in within 2 taps
- Session persists across app restarts for 30 days
- Users with different roles (customer, admin, courier) are routed to the correct interface after login

### Tasks

| # | Task | Description | Jira | Acceptance Criteria |
|---|------|-------------|------|-------------------|
| 1.1 | Google OAuth integration | Login/register with Google account | DHOP-8 | User can tap "Sign in with Google", authorize, and land on profile setup or catalog. Token stored. |
| 1.2 | Facebook OAuth integration | Login/register with Facebook account — **⚠️ OPTIONAL / post-MVP** (Meta App Review heteket vehet igénybe; a pilot elindítható Google + email/password nélkül) | DHOP-9 | [OPTIONAL] Same flow as Google. Do NOT block launch on this. |
| 1.3 | Email + password fallback | Standard registration as fallback option | DHOP-10 | User can register with email+password; email validation required; password min 8 chars. |
| 1.4 | User profile setup | Collect name, phone number, delivery address post-login | DHOP-11 | Form shown after first login; all 3 fields required; pre-filled on subsequent orders. |
| 1.5 | Session management | Persistent login, token refresh, logout | DHOP-12 | Token valid 30 days; refresh handled silently; logout clears all local tokens; role-based routing enforced. |

---

## Epic 2 – Product Catalog
**Jira:** DHOP-2 (Epic) | Tasks: DHOP-13, DHOP-14, DHOP-15, DHOP-16, DHOP-17

**Goal:** Customers can browse available products and understand what they're ordering.

**Epic Acceptance Criteria:**
- All available products visible within 2 seconds
- Customer can find a product and add it to cart in under 30 seconds

### Tasks

| # | Task | Description | Jira | Acceptance Criteria |
|---|------|-------------|------|-------------------|
| 2.1 | Product listing page | Mobile-optimized grid/list of available products | DHOP-13 | Products load in < 2s; unavailable products clearly marked (greyed out or hidden). |
| 2.2 | Product detail view | Name, description, price per kg, availability | DHOP-14 | Shows: name, description, price/kg, availability. "Add to cart" button visible. |
| 2.3 | Quantity selector | Select quantity in kg (e.g. 0.5, 1, 1.5, 2 kg) | DHOP-15 | Increment by 0.5 kg steps; min 0.5kg, max 10kg; large tap targets for mobile. |
| 2.4 | Product availability toggle | Admin can mark products as available/unavailable | DHOP-16 | Toggle in admin panel; change reflected in catalog within 30 seconds. |
| 2.5 | Category support | Basic grouping (e.g. Fresh cuts, Processed, Sausages) | DHOP-17 | At least 3 categories; filter by category; "All" view available. |

---

## Epic 3 – Cart & Checkout
**Jira:** DHOP-3 (Epic) | Tasks: DHOP-18, DHOP-19, DHOP-20, DHOP-21, DHOP-22, DHOP-23

**Goal:** Simple, fast order placement with minimal steps and no payment friction.

**Epic Acceptance Criteria:**
- A user can go from empty cart to submitted order in under 2 minutes
- No order can be submitted twice (idempotent)
- Every submitted order creates a record in the database with status "New Order"

### Tasks

| # | Task | Description | Jira | Acceptance Criteria |
|---|------|-------------|------|-------------------|
| 3.1 | Shopping cart | Add/remove/update items, persistent across session | DHOP-18 | Cart persists on page refresh; item count visible in nav; quantities editable. |
| 3.2 | Cart summary view | Items, quantities, estimated total with weight disclaimer | DHOP-19 | Shows all items, quantities, price per kg, subtotal, weight disclaimer ("final weight may vary"). |
| 3.3 | Delivery details form | Name, phone, delivery address (pre-filled if saved) | DHOP-20 | Pre-fills saved profile data; all fields required; phone validated (format check). |
| 3.4 | Order confirmation screen | Summary before submit, clear CTA | DHOP-21 | Shows full order summary + delivery address; back button available; clear "Place Order" CTA. |
| 3.5 | Order placement | Submit order → creates record with status "New Order" + admin email értesítés | DHOP-22 | **Critical.** POST is idempotent; returns order ID; double-tap prevention; error state if server unreachable; **admin email notification fires on every successful order placement.** |
| 3.6 | Post-order confirmation page | Thank you screen with order number and next steps | DHOP-23 | Shows order number; explains next steps ("We'll contact you to confirm delivery time"). |

---

## Admin Értesítési Stratégia (Notification Strategy)

> Ez a szekció definiálja, hogyan értesül az admin az új rendelésekről. Az MVP célja: **az admin azonnal tudjon minden új rendelésről, extra infrastruktúra nélkül.**

### Must-Have (MVP — DHOP-22 részeként implementálandó)

| Esemény | Értesítési mód | Részletek |
|---------|---------------|-----------|
| Új rendelés érkezett | **Email az admin email-re** (SMTP) | Automatikusan tüzel, amint a DHOP-22 backend sikeresen létrehozza a rendelést |

**Email tartalom (kötelező mezők):**
- 📦 Rendelés azonosítója (order ID)
- 👤 Vásárló neve, telefonszáma
- 📍 Szállítási cím
- 🥩 Rendelt termékek + mennyiségek
- 💰 Becsült végösszeg
- 🕐 Rendelés időpontja

**Implementációs elvárások:**
- SMTP konfiguráció environment variable-ben (nem hardcoded)
- Ha az email küldés meghiúsul, a rendelés attól még mentésre kerül — az email failure nem blokkolja az order placement-et
- Admin email cím konfigurálható (env var), ne legyen hardcoded a kódban

### Nice-to-Have (post-MVP)

| Értesítés | Mikor? | Miért post-MVP? |
|-----------|--------|----------------|
| **WhatsApp üzenet adminnak** | Új rendelésnél | Twilio/WhatsApp API integráció kell; de Erdélyi kontextusban ez a leggyakoribb csatorna — prioritizálandó post-launch |
| **Browser push notification** | Új rendelésnél, admin dashboardon | Service worker szükséges; extra komplexitás MVP-hez |
| **Email a vásárlónak: rendelés visszaigazolása** | Sikeres order placement után | Igényes, de az order confirmation page (DHOP-23) ezt részben lefedi |
| **Email a vásárlónak: státusz változáskor** | "Out for Delivery" státusznál | Értékes UX, de manual phone call is megoldja pilotban |

---

## Epic 4 – Order Status & Lifecycle
**Jira:** DHOP-4 (Epic) | Tasks: DHOP-24, DHOP-25, DHOP-26, DHOP-27, DHOP-28

**Goal:** Every order is fully trackable from placement to delivery.

**Order Status Flow:**
`New Order` → `Processing` → `Ready for Delivery` → `Out for Delivery` → `Delivered` → `Closed`

**Epic Acceptance Criteria:**
- Status transitions are logged with timestamp and actor (admin/courier)
- Customer can see their order's current status at any time
- No invalid state transitions allowed (e.g., can't go from "New Order" to "Delivered")

### Tasks

| # | Task | Description | Jira | Acceptance Criteria |
|---|------|-------------|------|-------------------|
| 4.1 | Order status data model | Define all statuses, transitions, timestamps | DHOP-24 | Schema documented and team-approved before any coding begins. Includes: all 6 statuses, valid transitions, actor field, timestamp per transition. |
| 4.2 | Customer order history | List of past and active orders with current status | DHOP-25 | Ordered by date desc; active orders shown first; status badge visible. |
| 4.3 | Order detail view (customer) | Status, items ordered, delivery address, estimated time | DHOP-26 | Shows: status, all items, delivery address, order date. No estimated time in MVP (manual). |
| 4.4 | Status change by admin | Admin can manually move order through status steps | DHOP-27 | Only valid next statuses shown; change saved immediately; audit log entry created. |
| 4.5 | Status change by courier | Courier can update to "Out for Delivery" and "Delivered" | DHOP-28 | Courier can only set: "Out for Delivery" and "Delivered". No other transitions. |

---

## Epic 5 – Courier Interface
**Jira:** DHOP-5 (Epic) | Tasks: DHOP-29, DHOP-30, DHOP-31, DHOP-32, DHOP-33

**Goal:** Courier manages all deliveries from a single mobile screen with zero paper.

**Epic Acceptance Criteria:**
- Courier sees only today's deliveries assigned to them
- Navigation opens in one tap
- Marking delivered updates status in real time

### Tasks

| # | Task | Description | Jira | Acceptance Criteria |
|---|------|-------------|------|-------------------|
| 5.1 | Courier login | Separate login flow for courier role | DHOP-29 | Same auth stack as customer; after login, courier sees only delivery interface (no catalog/cart). |
| 5.2 | Today's delivery list | All orders assigned for today, sorted by address/time | DHOP-30 | Shows only "Ready for Delivery" orders for today; sorted by address; customer phone visible. |
| 5.3 | Delivery detail view | Customer name, phone, address, items ordered | DHOP-31 | All info on one screen; large text for on-the-road readability. |
| 5.4 | Google Maps deep link | One-tap navigation launch to delivery address | DHOP-32 | Tapping address opens Google Maps (or default maps app) with destination pre-filled. |
| 5.5 | Mark as Delivered | Courier confirms delivery → status updates to "Delivered" | DHOP-33 | Confirmation dialog before marking; status updates within 2s; order disappears from active list. |

---

## Epic 6 – Super Admin Interface
**Jira:** DHOP-6 (Epic) | Tasks: DHOP-34, DHOP-35, DHOP-36, DHOP-37, DHOP-38, DHOP-39

**Goal:** Full operational visibility and control over the pilot from one dashboard.

**Epic Acceptance Criteria:**
- Admin can see all orders, statuses, and customer data from one screen
- Admin can manage the full product catalog without developer assistance
- Pilot KPIs visible at a glance (registrations, orders, basket value, returning customers)

### Tasks

| # | Task | Description | Jira | Acceptance Criteria |
|---|------|-------------|------|-------------------|
| 6.1 | Admin login | Secure admin authentication | DHOP-34 | Admin-only route; role verified server-side; no customer can access admin URLs. |
| 6.2 | Orders dashboard | All orders, status, basket value, date — filterable | DHOP-35 | Filter by status and date range; shows order count, total value; paginated if > 50 orders. |
| 6.3 | Order detail & status management | View order, update status, add notes | DHOP-36 | Full order detail; status change (all transitions); internal note field (not visible to customer). |
| 6.4 | Customer list + order history | All registered users, registration date, order count; per-customer order history accessible by clicking any row (merged from original 6.5 → DHOP-37) | DHOP-37 | List with: name, email, reg date, order count; clicking row opens full order history. |
| 6.5 | Product management | Add/edit/delete products, set price, toggle availability | DHOP-38 | CRUD for products; image upload optional in MVP; price in RON/kg; availability toggle. |
| 6.6 | Statistics dashboard | Registrations, order count, avg basket value, returning customers | DHOP-39 | Shows pilot KPIs; date range filter; data refreshes every 15 min or on demand. |

> **Megjegyzés (v1.0 → v1.1):** Az eredeti spec 7 taskot sorolt fel (6.1–6.7), ahol a "Customer order history" önálló 6.5 volt. A Jira implementációban ez tudatosan beolvadt a Customer list taskba (DHOP-37), így Epic 6 = 6 task, összesen 37 task (nem 38). A dev-roadmap.md (44 ticket = 7 Epic + 37 Task) már ezt a számot tükrözte.

---

## Epic 7 – Infrastructure & Launch Prep
**Jira:** DHOP-7 (Epic) | Tasks: DHOP-40, DHOP-41, DHOP-42, DHOP-43, DHOP-44

**Goal:** System is live, measurable, and acquisition channels are active.

**Epic Acceptance Criteria:**
- App accessible via HTTPS on final production domain
- Analytics tracking registrations and order funnel
- QR codes printed and placed in stores
- Facebook CTA active before launch day

### Tasks

| # | Task | Description | Jira | Acceptance Criteria |
|---|------|-------------|------|-------------------|
| 7.1 | Hosting & deployment setup | Server, domain, SSL certificate | DHOP-40 | Server running HTTPS; domain finalized; staging and production environments separate. |
| 7.2 | Environment configuration | Production/staging environments, env variables | DHOP-41 | All secrets in env vars (no hardcoding); staging uses test credentials; deployment documented. |
| 7.3 | Basic analytics integration | Page views, registration funnel, order funnel tracking | DHOP-42 | Tracks: page views, registrations, cart adds, order placements; data visible in analytics dashboard. |
| 7.4 | QR code generation | QR codes for in-store placement pointing to webapp | DHOP-43 | QR code links to production domain; tested on Android and iOS; print-ready (min 5×5 cm at 300dpi). |
| 7.5 | Facebook page link & CTA | Update Facebook page bio/post with webapp link | DHOP-44 | Facebook bio updated; at least 1 launch post drafted and approved; link tracked (UTM parameters). |

---

## Summary

| Epic | Tasks | Jira Epic | Priority |
|------|-------|-----------|----------|
| Epic 1 – Auth & Onboarding | 5 | DHOP-1 | 🔴 Critical |
| Epic 2 – Product Catalog | 5 | DHOP-2 | 🔴 Critical |
| Epic 3 – Cart & Checkout | 6 | DHOP-3 | 🔴 Critical |
| Epic 4 – Order Status & Lifecycle | 5 | DHOP-4 | 🔴 Critical |
| Epic 5 – Courier Interface | 5 | DHOP-5 | 🟠 High |
| Epic 6 – Super Admin Interface | 6 | DHOP-6 | 🟠 High |
| Epic 7 – Infrastructure & Launch | 5 | DHOP-7 | 🔴 Critical |
| **Total** | **37 tasks** | | |

> Facebook OAuth (1.2) opcionális/post-MVP → nem blokkolja a launch-ot.

---

## Definition of Done

A task csak akkor tekinthető **kész**nek, ha:

1. ✅ Kód review-n átment (legalább 1 reviewer)
2. ✅ Acceptance criteria teljesítve (manuális tesztelés bizonyítja)
3. ✅ Staging-en fut hiba nélkül
4. ✅ Nincs console error vagy unhandled exception
5. ✅ Mobile-on (Android Chrome) tesztelve

---

> **Változáskövetés:**
> - v1.0 → v1.1: Facebook OAuth (1.2) opcionálissá téve; Epic 6: 7 task → 6 task (6.5 merge DHOP-37-be); Total: 38 → 37 task
> - v1.1 → v1.2: Version line javítva a body-ban; DHOP ticket referenciák hozzáadva minden taskhoz; Acceptance criteria hozzáadva epics és tasks szintjén; Non-Functional Requirements szekció hozzáadva; Definition of Done szekció hozzáadva; Summary tábla DHOP Epic columnnal bővítve
