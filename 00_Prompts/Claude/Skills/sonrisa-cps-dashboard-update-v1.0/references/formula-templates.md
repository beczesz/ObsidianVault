---
title: "Formula Templates for T&M Raw"
date: 2026-05-05
author: Becze Szabolcs
status: active
description: "Reference guide for T&M Raw spreadsheet formulas used in cost and revenue calculations. Contains templates for date ID, hourly rates, invoiced amounts, transfer prices, cost share, profit margin and related metrics across columns C through X."
description_source: auto
description_hash: 17cb0c8c42b1a0e6
id: 25858bbd-c16f-4150-bd0b-ae4bb63cca1b
index_schema_version: 1
bdos_index: true
---
# Formula Templates for T&M Raw

When adding a new row at row R, use these formulas. Replace `{R}` with the actual row number.

## Date ID (Column C)

```
=A{R} & " " & CHOOSE(B{R}, "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
```

## Rate (Column N)

```
=IF(K{R} = 0, 0, M{R} / 8)
```

Converts daily rate to hourly rate. If hours = 0, rate = 0.

## Value (Column R)

```
=K{R}*N{R}+O{R}
```

Hours * hourly rate + fixed amount.

## Invoiced (Column S)

```
=IF(Q{R} = "", "", IF(Q{R} > 0, (1 - Q{R}) * IF(P{R} = "Billable", IF(O{R} > 0, O{R}, K{R} * N{R}), 0), IF(P{R} = "Billable", IF(O{R} > 0, O{R}, K{R} * N{R}), 0)))
```

Logic: If discount > 0, apply it. Only billable work generates invoiced amount. Fixed price takes precedence over T&M calculation.

## Transfer Price (Column T)

```
=IF(OR(I{R} = "", J{R} = ""), "", -VLOOKUP("DevOps", 'Transfer Prices'!$A$12:$J$18, RIGHT(J{R}, 1) + 1, FALSE))
```

Looks up the transfer price from the Transfer Prices sheet based on seniority level. The `RIGHT(J{R}, 1) + 1` extracts the number from "e6" -> 6 -> column 7.

## Cost Share (Column U)

```
=IF(K{R}<>"", T{R}/Utils!$B$14 * K{R}, T{R})
```

If hours reported, cost = (transfer price / working days) * hours. Otherwise just the flat transfer price.

## Normalized Profit (Column V)

```
=N{R}*Utils!$B$14+T{R}
```

Hourly rate * working days + transfer price (which is negative, so this is revenue - cost).

## Margin (Column W)

```
=IF(N{R}<>0, V{R}/(N{R}*Utils!$B$14), "NA")
```

Profit margin percentage. "NA" if rate is zero.

## Project Copy (Column X)

```
=F{R}
```

Simple reference to column F.

---

## Notes

- `Utils!$B$14` contains the number of working days in the month. This is a fixed reference that all rows share.
- `Transfer Prices` sheet has a matrix of costs by role and seniority level.
- The "DevOps" lookup key is used for all CPS engineers (the team falls under the DevOps cost center).
- Columns Y-AB have helper formulas (CONCATENATE, UNIQUE references) that vary. When in doubt, copy from the row above.
