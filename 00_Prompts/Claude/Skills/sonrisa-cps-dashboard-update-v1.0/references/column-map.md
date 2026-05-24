# T&M Raw Complete Column Map (A-AD)

## Input Columns (written by Claude or user)

| Col | Letter | Name | Type | Validation | Example |
|-----|--------|------|------|------------|---------|
| 1 | A | Year | Integer | 2020-2030 | 2026 |
| 2 | B | Month | Integer | 1-12 | 4 |
| 3 | C | Date ID | Formula | Auto | "2026 April" |
| 4 | D | #Month | String | #MM Name | "#04 April" |
| 5 | E | Client | String | Must match Clients sheet | "Jumio" |
| 6 | F | Project | String | Must match Clients sheet | "Jumio AWS" |
| 7 | G | Type | Enum | T&M, Fixed Price, Hybrid, Retainer, Fix Service, Internal | "T&M" |
| 8 | H | Name | String | Person full name | "Kovacs Attila" |
| 9 | I | Emp. Status | Enum | Employee, Contractor | "Employee" |
| 10 | J | Seniority level | Enum | e1-e9 | "e6" |
| 11 | K | Raported hours | Number | 0-300 | 160 |
| 12 | L | Suggested Daily Rate | Number | Optional, often blank | |
| 13 | M | Daily Rate | Number | EUR, 0-2000 | 310 |
| 14 | N | Rate | Formula | Hourly rate | 38.75 |
| 15 | O | Fixed | Number | Fixed price EUR, 0 for T&M | 0 |
| 16 | P | Is Billable | Enum | Billable, Non billable, Internal, On Transfer Price | "Billable" |
| 17 | Q | Discount | Number | 0 or decimal (0.1 = 10%) | 0 |

## Formula Columns (copy from row above)

| Col | Letter | Name | What it calculates |
|-----|--------|------|--------------------|
| 18 | R | Value | Hours * rate + fixed |
| 19 | S | Invoiced | Value after discount, only if billable |
| 20 | T | TP | Transfer price (internal cost) from lookup |
| 21 | U | Cost Share | Allocated cost based on hours |
| 22 | V | Normalized Profit | Revenue minus cost |
| 23 | W | Margin | Profit / revenue as percentage |
| 24 | X | Project | Copy of column F |
| 25 | Y | Name (helper) | Varies |
| 26 | Z | UName (helper) | Varies |
| 27 | AA | UProj (helper) | Varies |
| 28 | AB | T&M Quality | Varies |

## State Columns (our addition)

| Col | Letter | Name | Type | Values |
|-----|--------|------|------|--------|
| 29 | AC | Status | Enum | PREFILLED, ACK, REVIEW, ADJUSTED, SKIP |
| 30 | AD | Notes | String | Free text | 

## Key Relationships

- **Client (E) and Project (F)** must match entries in the `Clients` sheet
- **Type (G)** should match the Clients sheet column G for that project
- **Seniority (J)** drives the Transfer Price lookup in column T
- **Is Billable (P)** determines whether Invoiced (S) produces a value or zero
- **Utils!$B$14** (working days) is referenced by multiple formulas

## Typical Values by Billable Type

| Is Billable | Rate | Fixed | Discount | Invoiced result |
|-------------|------|-------|----------|-----------------|
| Billable | >0 | 0 | 0 | hours * rate |
| Billable | >0 | 0 | 0.1 | 90% of hours * rate |
| Billable | 0 | >0 | 0 | fixed amount |
| Non billable | >0 | 0 | 0 | 0 |
| Internal | 0 | 0 | 0 | 0 |
| On Transfer Price | >0 | 0 | 0 | 0 (cost tracking only) |
