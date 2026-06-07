---
title: "CPS Website Working Folder"
date: 2026-04-27
author: Becze Szabolcs
status: active
description: "Working directory for Sonrisa CPS website HTML fragments managed in Sellvio CMS, including versioned landing page components, detail pages, and reference documentation for developers maintaining the site."
description_source: auto
description_hash: 023451cdb5df070a
id: 35739b83-b4fd-4b22-9e29-ecbc729df893
index_schema_version: 1
bdos_index: true
---
# CPS Website Working Folder

This folder contains Sellvio CMS HTML files for the Sonrisa CPS website (sonrisa.hu/en/cps-services).
These are NOT standalone HTML pages - they are CMS content fragments pasted into Sellvio's "Description" editor.

## Quick Start

1. Read this file first
2. Read `sellvio-cms-component-guide.md` for the full component library
3. Read `article-patterns-reference.md` for article-specific patterns
4. Check the latest version of whichever page you need (see Current Files below)

## File Naming Convention

All HTML files use versioned filenames: `{page-name}-v{major}.{minor}.html`

When creating a new version:
- Bump the version in the FILENAME (e.g. `intermediary-v0.5.html` -> `intermediary-v0.6.html`)
- Bump the version in the HTML comment header at the top of the file
- Add a changelog note in the header comment describing what changed
- Keep the previous version in place (do NOT overwrite)

When archiving: move all but the latest version of each file to `archive/`.

## Current Files

### Pages (Sellvio CMS HTML)

| File | Sellvio Article | Live URL | Description |
|------|----------------|----------|-------------|
| `intermediary-v0.5.html` | CPS services hub (root) | sonrisa.hu/en/cps-services | The main CPS landing page with hero, trust bar, "Why CPS" cards, service cards grid, CTA, contact form, personal quote |
| `managed-service-v0.4.html` | Article #21 | /en/cps-services/article/managed-cloud-platform-services-v2/21 | Managed Cloud Operations detail page |
| `llmaas-page-v11.html` | Article #20 | /en/cps-services/article/llm-as-a-service-private-ai-fully-managed/20 | LLM as a Service detail page |
| `aws-health-check-v0.2.html` | Article #13 | /en/cps-services/article/aws-cost-health-check/13 | AWS Cost Health Check detail page |
| `insights-page-sellvio-v0.4.html` | TBD (new page) | TBD | Insights/blog listing page |
| `insights-page-preview.html` | N/A | N/A | Standalone visual preview of Insights page for designer (not for CMS) |

### Reference Docs

| File | Purpose |
|------|---------|
| `sellvio-cms-component-guide.md` | Full Sellvio component library with HTML snippets for every component type |
| `article-patterns-reference.md` | Patterns learned from reviewing all existing articles in Sellvio admin |
| `llmaas-landing-page-structure.md` | Copy and structure document for the LLMaaS page |

### Archive

`archive/` contains all previous versions of HTML files. 27 files as of 2026-04-27.

## CPS Services Page Structure (intermediary)

The hub page at sonrisa.hu/en/cps-services has this section flow:

1. **Hero** - `template--about-cover` on `bg-mid-green` with CPS landing image, AWS badge, headline, two buttons (Calendly + scroll to services)
2. **Trust bar** - `template--brands` on `bg-dark` with client logos (Lufthansa, Oracle, Yettel, etc.)
3. **Why CPS** - 3 white cards on `bg-gray-green`: One Team Full Spectrum / Start Small Scale Up / Proactive by Design
4. **Service cards** - `sellvio-template--3-cols template--addons` with 3x `col-md-4` cards on `bg-gray-green`:
   - AWS Cost Health Check (START HERE) -> article /13
   - Managed Cloud Operations (CORE SERVICE) -> article /21
   - LLM as a Service (ADD-ON) -> article /20
5. **CTA banner** - `template--section-featured bg-theme` with Calendly + Szabolcs photo
6. **Contact form** - `template--form-picture` on `bg-gray-green`
7. **Personal quote** - Szabolcs bio on `bg-mid-green`

## Sellvio CMS Essentials (quick reference)

### Required includes at top of every page

```html
<link href="https://assets.calendly.com/assets/external/widget.css" rel="stylesheet" />
<script src="https://assets.calendly.com/assets/external/widget.js" type="text/javascript" async></script>
<link href="https://sonrisa.mysellvio.com/tenancy/assets/manager/files/custom-content/landing.css?v=1.6" rel="stylesheet" />
```

### Core wrapper pattern

Every section wraps in `dragdiv`. Background sections nest: `dragdiv > bg-{color} bg-full-width > dragdiv > content`.

### Background classes

- `bg-mid-green` - hero, personal quote
- `bg-dark` - trust bar, numbered services, dark sections
- `bg-gray-green` - cards, pricing, forms
- `bg-theme` - CTA banners (#8ee4a9 green)
- `bg-light-green` - lighter sections (blog listing)

### Key components

- Hero: `template--about-cover` (with `about-image` + `about-text > about-text__wrap--wide`)
- Trust bar: `template--brands` on `bg-dark`
- Cards: `sellvio-template--3-cols template--addons` with `col-card bg-gray-green`
- Pricing: `table--mobile table--plans`
- CTA: `template--section-featured bg-theme bg-full-width content-w-1280`
- Numbered list: `template--numbered-table` on `bg-dark`
- Form: `template--form-picture` on `bg-gray-green`
- Tabs: `template--tabs` (hidden table transformed by JS)

### Buttons

- `button button--dark` - primary CTA (dark green)
- `button button--pink` - secondary CTA (coral/pink)

### Calendly link (used on all CTA buttons)

```html
<a class="button button--dark" href="" onclick="Calendly.initPopupWidget({url: 'https://calendly.com/becze-szabolcs-sonrisa/sonrisa-devops-consultation-30mins'});return false;">Talk to an Expert</a>
```

### Key image assets

- Szabolcs headshot (CTA): `/tenancy/assets/manager/files/custom-content/szeg1-opt.jpg`
- Szabolcs portrait (bio): `tenancy/assets/manager/files/custom-content/szabolcs-becze-head-of-cps-sonrisa.png`
- CPS landing hero: `tenancy/assets/manager/files/custom-content/cps-landing-page.jpg`
- AWS badge: `tenancy/assets/manager/files/static/sonrisa-select-tier-dark.png`
- Check mark: `tenancy/assets/manager/files/custom-content/check-green.png`
- Quote sign: `/tenancy/assets/manager/files/custom-content/quote-sign.png`

## Formatting Rules (STRICT)

These apply to ALL content text. CSS class names are exempt.

- NO em dashes (char: —). Use single `-` or rewrite.
- NO en dashes (char: –). Use single `-`.
- NO curly/smart quotes (“ ” ‘ ’). Use straight quotes.
- NO `--` in content text. Use single `-`. (CSS class names like `cols--gutter-15` are fine.)
- NO emojis.
- Use `&#39;` for apostrophes in HTML attributes.
- Version comment at top of every file: `<!-- Page Name | Version: X.Y -->`

### Verification script

Run this after every file creation/edit:

```python
python3 -c "
import re
with open('FILENAME.html', 'r') as f:
    content = f.read()
    lines = content.split('\n')
issues = []
for i, line in enumerate(lines, 1):
    for char, name in [('—', 'em dash'), ('–', 'en dash'), ('“', 'left curly quote'), ('”', 'right curly quote'), ('‘', 'left curly apos'), ('’', 'right curly apos')]:
        if char in line:
            issues.append(f'Line {i}: Found {name}')
    stripped = re.sub(r'class=\"[^\"]*\"', '', line)
    stripped = re.sub(r'<!--.*?-->', '', stripped)
    if '--' in stripped:
        issues.append(f'Line {i}: Found double dash in content: {line.strip()[:80]}')
if issues:
    for i in issues: print(i)
else:
    print('All formatting checks passed!')
"
```

## Blog Articles

Blog articles live in `CPS/Marketing/Blogs/` (not in this folder). Each article has its own subfolder with:
- `raw-outline.md` - initial outline
- `article-v{X}.md` - drafted content
- `article-v{X}.html` - Sellvio CMS HTML

Blog articles are published under the "Our Impact" category in Sellvio. They use Calendly CTAs (not mailto).

Current blog article URLs:
- Article 1: /en/our-impact/article/why-one-devops-engineer-is-never-enough/18
- Article 2: /en/our-impact/article/in-house-or-managed-devops-five-questions-that-decide-it/22
- Article 3: /en/our-impact/article/the-hidden-costs-of-hiring-vs-managed-services/23

## Pending Work

- **Azure DevOps service card** - Add a 4th card to the intermediary page for Azure DevOps platform services (implementation + managed support). Two case studies exist: cs-004 (MVMI SLA support) and cs-005 (OKFO implementation). Grid will need to change from 3x col-md-4 to 2x2 col-md-6.
- **Azure DevOps detail page** - New service page to be created (similar structure to managed-service or aws-health-check pages).
- **Insights page** - CMS version ready (v0.4), needs to be created as a Sellvio article and published.
- **SEO metadata** - Article #18 has empty meta title/description fields in Sellvio admin.
