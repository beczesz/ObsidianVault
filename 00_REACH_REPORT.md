---
title: 00_REACH_REPORT
date: 2026-06-07
author: reach.py
status: active
bdos_index: false
description: Vault index reach audit. Compares the live SQLite index against the filesystem ground truth plus an explicit coverage policy. Reports format gaps (non-md knowledge unindexed), completeness gaps (md on disk absent from index), and drift (ghosts, pollution, stale). The falsifiable trust metric the self-referential coverage_pct cannot provide.
id: e0dc9786-e2d3-4586-8a0c-3fb7ee8cc6aa
index_schema_version: 1
---

# Vault Index Reach Report

Generated: 2026-06-07T04:05:11Z
Index DB: `/Users/becze-mac/Library/Application Support/bdos-vault-index/vault.db`
Last full build: 2026-06-07 03:44 UTC

> Read-only reconciliation. Nothing in the index or the vault was modified.
> This measures the index against the filesystem, not against itself.

## Headline reach

| Tier | What it means | Indexed / On disk | Reach |
|---|---|---|---|
| Markdown completeness | The index's own promise (.md only). Should be ~100%. | 2185 / 2185 | **100.0%** |
| Full-text knowledge | md + srt + txt + vtt (plain-text, cheap to index) | 2593 / 2593 | **100.0%** |
| Total knowledge | the above + pdf/docx/xlsx/pptx/epub | 3021 / 3021 | **100.0%** |

## 1. Completeness gap (markdown the index should have but does not)

None. Every in-scope `.md` file on disk is present in the index.

## 2. Format gap (non-markdown knowledge not in the index)

Non-md knowledge on disk: 408 plain-text (srt/txt/vtt), indexed full-text 408; 428 documents (pdf/docx/xlsx/pptx/epub), indexed as stubs 428.

Gap: **0**. Every non-md knowledge file on disk is in the index (transcripts full-text, documents as discoverable stubs).

## 3. Drift (index out of sync with disk)

- **Ghosts** (in index, file gone from disk): 0
- **Pollution** (indexed from a policy-excluded dir such as ExarSharedBrain): 0
- **Stale** (file on disk newer than its index row): 0

## Index internal health (for context)

- Rows in index: 3021
- With description: 1580 (52.3%)
- Archived knowledge intentionally excluded: 62
- Health distribution:
  - ok: 2445
  - no_frontmatter: 509
  - excluded: 33
  - missing_required_fields: 20
  - needs_reindex: 11
  - archived: 3

Unclassified extensions (policy did not have a rule, review and assign):
- `.gitkeep`: 15
- `(none)`: 13
- `.plugin`: 12
- `.template`: 12
- `.ttf`: 10
- `.download`: 9
- `.pdf#`: 8
- `.skill`: 7
- `.jsx`: 7
- `.canvas`: 6
- `.sql`: 4
- `.gitignore`: 3
- `.eml`: 2
- `.env`: 2
- `.example`: 2
- `.command`: 2
- `.mermaid`: 1
- `.out`: 1
- `.xlsx#`: 1
- `.tmp_duplikatum_paperworld_pdf`: 1
- `.fuse_hidden0000000500000001`: 1
- `.fuse_hidden0000000e00000002`: 1
- `.fuse_hidden0000000f00000003`: 1
- `.jpg@itok=gvs2di-c`: 1
- `.jpg@itok=0fpj88n6`: 1
- `.jpg@itok=uk30s-8u`: 1
- `.jpg@itok=cptqughk`: 1
- `.jpg@itok=tgy399il`: 1
- `.jpg@itok=98grhyyj`: 1
- `.jpg@itok=2igghvcl`: 1
- `.jpg@itok=jivpccae`: 1
- `.jpg@itok=-h8lzdan`: 1
- `.jpg@itok=kwiotecy`: 1
- `.jpg@itok=5x9b1ncr`: 1
- `.jpg@itok=9fegxfrj`: 1
- `.jpg@itok=o_6qzyyd`: 1
- `.jpg@itok=s0hyhami`: 1
- `.jpg@itok=oavx63wp`: 1
- `.jpg@itok=sfkhl4at`: 1
- `.jpg@itok=ariw68qj`: 1
- `.jpg@itok=a5laat7h`: 1
- `.jpg@itok=vfs_l5ct`: 1
- `.jpg@itok=wjsu9-ng`: 1
- `.jpg@itok=8krtgd9z`: 1
- `.jpg@itok=8myumeni`: 1
- `.jpg@itok=lxvvjxup`: 1
- `.jpg@itok=7ijp-sey`: 1
- `.jpg@itok=0sxrudw2`: 1
- `.jpg@itok=4q1n2j6v`: 1
- `.jpg@itok=xlthm5sd`: 1
- `.jpg@itok=dtogpric`: 1
- `.jpg@itok=ne5lff41`: 1
- `.jpg@itok=dosoa2js`: 1
- `.jpg@itok=irw5clk0`: 1
- `.jpg@itok=voazprrr`: 1
- `.jpg@itok=cyy99ouw`: 1
- `.jpg@itok=srihi3ps`: 1
- `.jpg@itok=rsrjr-se`: 1
- `.jpg@itok=7eaxiawp`: 1
- `.jpg@itok=hkxufzfm`: 1
- `.jpg@itok=k3ivycm3`: 1
- `.jpg@itok=hel_mqwm`: 1
- `.jpg@itok=qvhpea86`: 1
- `.jpg@itok=kgifnhwq`: 1
- `.jpg@itok=izbe8mza`: 1
- `.jpg@itok=fxzy7y2n`: 1
- `.jpg@itok=rspr0hvj`: 1
- `.jpg@itok=u5ln8tql`: 1
- `.jpg@itok=qzwaryvy`: 1
- `.js@srxelk`: 1
- `.9`: 1
- `.woff`: 1
- `.eot`: 1
- `.woff2`: 1
- `.editorconfig`: 1
- `.assetsignore`: 1
- `.bnl`: 1
- `.cdr`: 1
- `.ncx`: 1
- `.opf`: 1
- `.patch`: 1
- `.bak-20260529`: 1
- `.base`: 1

## What to do about each gap

Nothing. Reach is complete (100% across all tiers), no drift, no pollution.

Re-run anytime: `python3.11 reach.py`
