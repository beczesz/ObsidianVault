---
title: "SharePoint/OneDrive Sync Issue -- Dashboard Editing from Cowork"
date: 2026-04-21
author: Becze Szabolcs
status: active
description: "Troubleshooting OneDrive sync conflicts when programmatically editing Excel files via openpyxl while the file is open in Excel Online; explores Microsoft Graph API and SharePoint REST API alternatives to avoid full-file-replacement locking issues in a monthly dashboard workflow."
description_source: auto
description_hash: e5d822ea60b488e9
id: f92e4e27-cbaf-4cfb-8de0-8cda018bcef9
index_schema_version: 1
bdos_index: true
---
# SharePoint/OneDrive Sync Issue -- Dashboard Editing from Cowork

## The Setup

I have a CPS Dashboard Excel file (`CPS - Dashboard - v2.xlsx`) on SharePoint. I set up OneDrive sync ("Add shortcut to OneDrive") so the file is available locally at:

```
C:\Users\EvoComputers\Downloads\Work\Sonrisa\CPS\New folder\Sonrisa Kft\sales - Cloud Platform Services\CPS - Dashboard - v2.xlsx
```

I'm using Claude Cowork (desktop AI assistant) which can read/write files on my local filesystem via Python (openpyxl). The goal is to have Cowork programmatically edit the Excel file locally, and have those changes sync back to SharePoint automatically.

## What Works

- Cowork can read the synced file (once it's pinned as "Always keep on this device")
- Cowork can write/modify the file using openpyxl and save it back to the same path
- The data written by Cowork is correct (verified by re-reading the file)

## The Problem

When the same file is open in Excel Online (browser), OneDrive refuses to sync the locally modified version. Instead it shows:

> "This file is open by you or someone else. Tap or click to open the file in the Office app, so we can sync it."

This means I cannot keep the file open in the browser as a live viewer while Cowork writes to the local copy. Excel Online holds a lock even though it supports co-authoring between browser users.

The core issue: **openpyxl does a full file replacement** (read all -> modify in memory -> write entire new file). This is not the same as co-authoring (cell-level deltas). OneDrive sees it as a completely new file replacing the old one, which conflicts with the browser lock.

## How I Want to Work

My monthly workflow is interactive and project-by-project:

1. Cowork presents: "Next project is Jumio AWS. Last month had Kovacs Attila (e6, 176h, rate 310). This month from timesheet: 160h. Ready to write?"
2. I review and ACK in the Cowork chat
3. Cowork writes the rows to the Excel file (appending to T&M Raw sheet, adding formulas, setting a status column to "PREFILLED")
4. I want to see the changes immediately in the browser to verify
5. Once verified, I ACK and we move to the next project

The problem is step 3-4: I can't see the changes in the browser because the sync is blocked while the file is open.

## Current Workaround (Clunky)

Close the browser tab before each write, wait for sync, reopen after. This works but is tedious for a project-by-project workflow with 20+ projects per month.

## What I'm Looking For

A streamlined solution that lets me:
- Have Cowork programmatically edit the Excel file
- See changes reflected in SharePoint/Excel Online quickly
- Not have to close and reopen the browser tab for every single edit

Possible directions I'm considering:
- Is there a way to push changes to SharePoint directly via API (Microsoft Graph) instead of relying on OneDrive sync?
- Could we use the SharePoint REST API or Excel Online API to write cell values directly while the file is open in the browser?
- Is there a OneDrive setting that handles this conflict differently?
- Would editing via the Office JavaScript API or Office Add-ins work better?
- Any other approach that avoids the full-file-replacement problem?

## Technical Details

- OS: Windows (OneDrive built-in)
- Sync method: OneDrive "Add shortcut to OneDrive" for a SharePoint document library
- Editor: openpyxl (Python) via Claude Cowork's sandboxed Linux shell
- File format: .xlsx (26 sheets, ~900KB, complex formulas and array formulas)
- SharePoint: sonrisakft.sharepoint.com (Microsoft 365 Business)
