---
title: "Personal Areas"
date: 2026-05-24
author: Becze Szabolcs
status: active
description: "Dashboard tracking personal growth metrics including weight trends, habit consistency over 120 days, and reading list for self-improvement resources."
description_source: auto
description_hash: 526e5b34c17a7637
id: 5b8cf241-ba7a-42f2-a025-92417d57c174
index_schema_version: 1
bdos_index: true
---
```dataviewjs
await dv.view("02_Areas/Personal Growth/_views/weight-chart", { defaultRangeDays: 90 });
```
Trend
```dataviewjs
await dv.view("02_Areas/Personal Growth/_views/weight-delta", { defaultRangeDays: 90 });
```

```habittracker
{
	"path": "02_Areas/Personal Growth/Habits/",
	"daysToShow": 120
}
```

## To Read
- [ ] High Output management https://www.google.ro/books/edition/High_Output_Management/piCeCgAAQBAJ?hl=en&gbpv=1&printsec=frontcover
