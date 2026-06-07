---
title: "SharePoint Upload Locations"
date: 2026-04-22
author: Becze Szabolcs
status: active
description: "Reference guide for uploading two file types to specific SharePoint folders: base files to Sales site and tam files to Cloud Guild site, with direct URLs and manual upload instructions since automated tools don't work with SharePoint's interface."
description_source: auto
description_hash: ddc473569d09e5b3
id: b815ebcf-2e34-4327-98b0-8361dfbbb864
index_schema_version: 1
bdos_index: true
---
# SharePoint Upload Locations

## _base file

- **Destination:** SharePoint Sales site
- **Path:** Sales > General > Planning > Services > Cloud Platform Services > raports
- **URL:** `https://sonrisakft.sharepoint.com/sites/sales/Megosztott%20dokumentumok/Forms/AllItems.aspx?id=%2Fsites%2Fsales%2FMegosztott%20dokumentumok%2FGeneral%2FPlanning%2FServices%2FCloud%20Platform%20Services%2Fraports&viewid=dfd2979e%2D7b28%2D49ac%2D9be0%2Dc493d63eeabc`

## _tam file

- **Destination:** SharePoint Cloud Guild site
- **Path:** Cloud Guild > Technical > Raport > Raw timesheets
- **URL:** `https://sonrisakft.sharepoint.com/sites/cloudguild/Megosztott%20dokumentumok/Forms/AllItems.aspx?id=%2Fsites%2Fcloudguild%2FMegosztott%20dokumentumok%2FTechnical%2FRaport%2FRaw%20timesheets&viewid=27bbc06a%2D762c%2D4e13%2D8c63%2D1f0cf00cde83`

## Upload Method

Navigate to each SharePoint folder in Chrome, use the Upload button or drag-and-drop, verify the file appears after upload.

Note: Chrome MCP `file_upload` tool does not currently work with SharePoint's dynamic file input elements. Manual upload is required.
