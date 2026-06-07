---
title: "Sellvio CMS Component Guide"
date: 2026-03-13
author: Becze Szabolcs
status: active
description: "Technical reference for Sellvio CMS components used in Sonrisa landing pages, including setup instructions, core wrapper patterns, background colors, and templates for heroes, trust bars, titles, tabs, and layouts with HTML/CSS specifications for developers and content editors building CPS pages."
description_source: auto
description_hash: 0680969c09e1cfc0
id: 725425ef-5471-4d53-a893-fdf2bd08b024
index_schema_version: 1
bdos_index: true
---
# Sellvio CMS Component Guide
## For Sonrisa CPS Landing Pages

Reference: Built from analysis of example_page.html (DevOps), example2.html (CPS Hub), about_us.html, legacy_modernization.html, and full_page.html (rendered LLMaaS v1).

---

## Page Setup

Every CMS page fragment starts with:

```html
<!-- Calendly link widget begin -->
<link href="https://assets.calendly.com/assets/external/widget.css" rel="stylesheet" />
<script src="https://assets.calendly.com/assets/external/widget.js" type="text/javascript" async></script>
<!-- Calendly link widget end -->
<link href="https://sonrisa.mysellvio.com/tenancy/assets/manager/files/custom-content/landing.css?v=1.6" rel="stylesheet" />
```

Note: v1.6 is the latest CSS version (used in example2.html / CPS Hub). The DevOps page uses v1.5.

---

## Core Wrapper Pattern

Every section is wrapped in a `dragdiv`. Nested sections use nested `dragdiv`:

```html
<div class="dragdiv">
  <!-- content goes here -->
</div>
```

For background sections, the pattern is:

```html
<div class="dragdiv">
<div class="bg-{color} bg-full-width">
<div class="dragdiv">
  <!-- inner content -->
</div>
</div>
</div>
```

---

## Background Colors

| Class | Color | Usage |
|-------|-------|-------|
| `bg-mid-green bg-full-width` | Medium green | Hero, personal quote section |
| `bg-dark bg-full-width` | Dark/black | Trust bar, numbered services, comparison tables |
| `bg-gray-green bg-full-width` | Light gray-green | Pricing area, form, benefit cards |
| `bg-theme bg-full-width` | Theme green (#8ee4a9) | CTA banners |
| `bg-light-green bg-full-width` | Light green | About Us hero, "What Sets Us Apart" |
| `bg-light-gray bg-full-width` | Light gray | Team section |
| `bg-full-w-margin bg-light` | Light with margin | Values table (about_us) |
| `bg-full-w-margin bg-gradient` | Gradient | About Us values |

---

## Content Width

`content-w-1280` - Constrains content to 1280px max width. Used on brands bar, tabs, numbered tables, CTAs, comparison tables.

`content-full-width` - Full width with padding. Used in about_us cards and legacy_modernization layout.

---

## Component Library

### 1. HERO - template--about-cover

Full-width hero with image left, text right.

```html
<div class="dragdiv">
<div class="bg-mid-green bg-full-width">
<div class="dragdiv">
<div class="template--about-cover">
<div class="about-image">
<p><img alt="" src="tenancy/assets/manager/files/custom-content/cps-landing-page.jpg" /></p>
</div>

<div class="about-text">
<div class="about-text__wrap--wide">
<img alt="" src="tenancy/assets/manager/files/static/sonrisa-select-tier-dark.png" style="width: 90px; height: 90px; float: right;" />
<h2>Headline<br />
<strong>Bold Part</strong></h2>

<p><span style="font-size:16px;">Subtext goes here.</span></p>

<p style="text-align: center;">
<a class="button button--dark" href="/en/contact">Primary CTA</a>
<a class="button button--pink" href="" onclick="Calendly.initPopupWidget({url: 'https://calendly.com/becze-szabolcs-sonrisa/sonrisa-devops-consultation-30mins'});return false;">Secondary CTA</a>
</p>
</div>
</div>
</div>
</div>
</div>
</div>
```

Variants:
- `about-text__wrap--wide` (DevOps page, LLMaaS) vs `about-text__wrap` (About Us - narrower)
- About Us hero omits the image (`<p>&nbsp;</p>` in about-image)
- About Us uses `bg-light-green` instead of `bg-mid-green`

---

### 2. TRUST BAR - template--brands

Logo carousel with two rows that alternate.

```html
<div class="dragdiv">
<div class="bg-dark bg-full-width content-w-1280 template--brands">
<div class="cols">
<div class="col-lg-3">
<h2 style="text-align: center;"><span style="font-size:20px;line-height: 1 !important;">Trust headline text.</span></h2>
</div>

<div class="col-lg-9">
<div class="image-switch">
<div class="img img--one">
<img alt="" src="tenancy/assets/manager/files/custom-content/brands/lufthansa.png" />
<!-- more logos -->
</div>

<div class="img img--two">
<img alt="" src="tenancy/assets/manager/files/custom-content/brands/oracle.png" />
<!-- more logos -->
</div>
</div>
</div>
</div>
</div>
</div>
```

---

### 3. TITLE FEATURED - template--title-featured

Large decorative title with subtitle. Used as section headers.

```html
<div class="dragdiv">
<div class="template--title-featured content-w-1280">
<h2>Line 1<br />
<strong>Bold Line</strong></h2>

<h6><span style="font-size:20px;">Subtitle text.<br />
Second line.</span></h6>
</div>
</div>
```

For dark backgrounds, add inline color styles:
```html
<h2 style="color: #ffffff;">White Title<br />
<strong>Bold</strong></h2>
<h6 style="color: rgba(255,255,255,0.7);">...</h6>
```

---

### 4. TABS - template--tabs

Interactive tabs rendered from a hidden table. JS transforms the table into a tabbed interface.

```html
<div class="dragdiv">
<div class="template--tabs content-w-1280">
<table border="1" cellpadding="1" cellspacing="1" class="js-custom-tabs front-hide" style="width: 100%;">
  <thead>
    <tr>
      <th scope="col">Title</th>
      <th scope="col">Content</th>
      <th scope="col">Image</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Tab Title</td>
      <td>
        <h5>Tab headline</h5>
        <ul>
          <li><span style="font-size:22px;">Point one.</span><br />&nbsp;</li>
          <li><span style="font-size:22px;">Point two.</span><br />&nbsp;</li>
          <li><span style="font-size:22px;">Point three.</span></li>
        </ul>
      </td>
      <td><img alt="" src="/tenancy/assets/manager/files/custom-content/tab-1-1.jpg" /></td>
    </tr>
    <!-- more rows = more tabs -->
  </tbody>
</table>
</div>
</div>
```

Key rules:
- Each `<tr>` in `<tbody>` = one tab
- Column 1 = tab button label
- Column 2 = tab content (h5 heading + ul list with font-size:22px spans)
- Column 3 = tab image (shown on the left in the rendered tab)
- List items use `<br />&nbsp;` for spacing between items (except last)
- Images use `/tenancy/...` (leading slash) path

---

### 5. TWO-COLUMN LAYOUT - sellvio-template--2-cols

Flexible two-column layout. The most used template.

```html
<div class="dragdiv">
<div class="sellvio-template sellvio-template--2-cols content-w-1280">
<div class="cols">
<div class="col-md-6">
<div class="col-card">
<div class="col-card-body">
  <!-- Left column content -->
</div>
</div>
</div>

<div class="col-md-6">
<div class="col-card">
<div class="col-card-body">
  <!-- Right column content -->
</div>
</div>
</div>
</div>
</div>
</div>
```

Column width variants: `col-md-5`/`col-md-7`, `col-md-6`/`col-md-6`, `col-md-3`*4 (four equal columns)

With gutter: `<div class="cols cols--gutter-15">`

With background cards: Add `bg-gray-green` to `col-card`:
```html
<div class="col-card bg-gray-green">
```

### 5b. TWO-COLUMN B VARIANT - sellvio-template--2-cols-b

Used in legacy_modernization for nested content within a larger column.

```html
<div class="dragdiv">
<div class="sellvio-template sellvio-template--2-cols-b">
<div class="cols cols--gutter-15">
<div class="col-md-7"><!-- content --></div>
<div class="col-md-5"><!-- sidebar --></div>
</div>
</div>
</div>
```

---

### 6. THREE-COLUMN LAYOUT - sellvio-template--3-cols

Used for add-on cards, security features, etc.

```html
<div class="dragdiv">
<div class="sellvio-template sellvio-template--3-cols template--addons content-w-1280">
<h3 class="mb-3 mb-lg-5" style="text-align: center;">Section Title</h3>

<div class="cols cols--gutter-15">
<div class="col-md-4">
<div class="col-card bg-gray-green">
<div class="col-card-body">
<div class="col-card-text mb-0"><span style="font-size:14px;">Price or label</span></div>
<h6 class="col-card-title"><span style="font-size:16px;">Card Title</span></h6>
<div class="col-card-text">
<ul>
  <li><span style="font-size:14px;">Bullet point</span></li>
</ul>
</div>
</div>
</div>
</div>
<!-- repeat col-md-4 for 2nd and 3rd columns -->
</div>
</div>
</div>
```

For add-on cards without bg: Use `<div class="col-card">` (no bg-gray-green class).

---

### 7. PRICING TABLE - table--plans

Responsive comparison/pricing table.

```html
<table class="table--mobile table--plans">
  <tbody>
    <tr>
      <th>&nbsp;</th>
      <th>Plan 1</th>
      <th>Plan 2</th>
      <th>Plan 3</th>
    </tr>
    <tr>
      <td>Row Label</td>
      <td>Value</td>
      <td>Value</td>
      <td>Value</td>
    </tr>
    <!-- Section header row -->
    <tr>
      <th colspan="4">Section Title</th>
    </tr>
  </tbody>
</table>
```

Check marks: `<img alt="" src="tenancy/assets/manager/files/custom-content/check-green.png" />`

---

### 8. CTA BANNER - template--section-featured

Call-to-action banner. Always on `bg-theme`.

Variant A (image right):
```html
<div class="dragdiv">
<div class="template--section-featured bg-theme bg-full-width content-w-1280">
<div class="cols">
<div class="col-lg-9">
<h2 style="text-align: center;">CTA Headline with <strong>bold</strong> and <em>italic</em></h2>
<p style="text-align: center;">Supporting text.</p>
<p style="text-align: center;"><a class="button button--dark" href="" onclick="Calendly.initPopupWidget({url: 'https://calendly.com/becze-szabolcs-sonrisa/sonrisa-devops-consultation-30mins'});return false;">CTA Button</a></p>
</div>

<div class="col-lg-auto">
<div class="hover-item" style="display: flex; align-items: flex-end; margin-bottom: 0;">
<h6 class="hover-item__title" style="text-align: right;">Let's chat!</h6>
<p><img alt="" src="/tenancy/assets/manager/files/custom-content/szeg1-opt.jpg" /></p>
</div>
</div>
</div>
</div>
</div>
```

Variant B (image left): Swap the `col-lg-auto` and `col-lg-9` divs. Use a different image.

---

### 9. NUMBERED TABLE - template--numbered-table

Numbered list of services/features. Always on `bg-dark`.

```html
<div class="dragdiv">
<div class="bg-dark bg-full-width">
<div class="dragdiv">
<div class="template--numbered-table">
<h2>Title<br />
<strong>Bold</strong><br />
More Text</h2>

<table border="0" cellpadding="1" cellspacing="1">
  <tbody>
    <tr>
      <td><h2>01</h2></td>
      <td>
        <h6>Item Title</h6>
        <p>Description text.</p>
      </td>
    </tr>
    <!-- repeat for 02, 03, etc. -->
  </tbody>
</table>

<p>&nbsp;</p>
</div>
</div>
</div>
</div>
```

---

### 10. CONTACT FORM - template--form-picture

Form with image. Always on `bg-gray-green`.

```html
<div class="dragdiv">
<div class="bg-gray-green bg-full-width">
<div class="dragdiv">
<div class="template--form-picture">
<div class="form-picture-text" style="justify-content: flex-start;">
<div class="form-picture-text__wrap">
<h5>Headline<br />
Second line</h5>

<p>[form id="2"]&nbsp;</p>

<p style="text-align: center;">
<a href="https://www.linkedin.com/company/sonrisatechnologies/" target="_blank"><img alt="" src="/tenancy/assets/manager/files/custom-content/linkedin.png" /></a>&nbsp;
<a href="https://www.facebook.com/sonrisainc" target="_blank"><img alt="" src="/tenancy/assets/manager/files/custom-content/facebook.png" /></a>
</p>
</div>
</div>

<div class="form-picture-image">
<p><img alt="" src="/tenancy/assets/manager/files/custom-content/keyboard-1-1.jpg" /></p>
</div>
</div>
</div>
</div>
</div>
```

Legacy modernization uses a different form pattern (inline form in 2-cols):
```html
<div class="col-md-6">
<div class="col-card"><div class="col-card-body">
<p>[form id="4"]</p>
</div></div>
</div>
```

---

### 11. PERSONAL QUOTE / FOUNDER SECTION

Image left, quote right. On `bg-mid-green`.

```html
<div class="dragdiv">
<div class="bg-mid-green bg-full-width">
<div class="dragdiv">
<div class="sellvio-template sellvio-template--2-cols">
<div class="cols">
<div class="col-md-5">
<div class="col-card"><div class="col-card-body">
<p class="col-card-text"><img alt="" src="tenancy/assets/manager/files/custom-content/szabolcs-becze-head-of-cps-sonrisa.png" /></p>
</div></div>
</div>

<div class="col-md-7">
<div class="col-card"><div class="col-card-body">
<h6 class="col-card-text"><span style="font-size:24px;">Name&nbsp;</span><br />
<a href="linkedin-url"><img alt="" src="/tenancy/assets/manager/files/custom-content/linkedin-blue.png" /></a><br />
<span style="font-size:20px;">Title <strong>Bold Part</strong></span><br />
<span style="font-size:16px;">Company</span></h6>

<p class="col-card-text">&nbsp;</p>

<p class="col-card-text"><img alt="" src="/tenancy/assets/manager/files/custom-content/quote-sign.png" /></p>

<p class="col-card-text"><span style="font-size:22px;"><span style="font-family:Georgia,serif;"><em>Quote text here.</em></span></span></p>
</div></div>
</div>
</div>
</div>
</div>
</div>
</div>
```

---

### 12. TEAM CARDS - sellvio-template--cards

Used on About Us page for team members.

```html
<div class="sellvio-template sellvio-template--cards sellvio-template--cards-3 template--team bg-light-gray bg-full-width">
<div class="cols">
<div class="col-12">
<h3 class="template--team-title" style="text-align: center;">Section Title</h3>
</div>

<div class="col-md-4">
<div class="articles__item">
<section class="card card-article">
<div class="card__image-wrapper"><picture class="card__image">
<img alt="" src="path/to/image.png" />
</picture></div>
<div class="card__content">
<h5 class="card__heading"><em>Person Name</em></h5>
<div class="card__desc">
<p>Role Title</p>
<p><a href="linkedin-url" target="_blank"><img alt="" src="tenancy/assets/manager/files/about/linkedin.png" /></a></p>
</div>
</div>
</section>
</div>
</div>
<!-- repeat col-md-4 -->
</div>
</div>
```

Variant: `sellvio-template--cards-4` for 4-column (col-md-6 col-lg-3).

---

### 13. VALUES TABLE - template--table

Two-column table for values/beliefs. Used in About Us.

```html
<div class="template--table bg-full-w-margin bg-gradient">
<div class="cols">
<div class="col-md-10">
<table border="0" cellpadding="1" cellspacing="1" style="width: 100%;margin-top: 30px;">
  <tbody>
    <tr>
      <td><h6>Value Name</h6></td>
      <td>Description text.</td>
    </tr>
    <!-- more rows -->
  </tbody>
</table>
</div>
</div>
</div>
```

---

### 14. VIDEO EMBED

Used in DevOps pricing section.

```html
<div class="ckeditor-html5-video" data-responsive="true" style="text-align: center;">
<video autoplay="autoplay" controlslist="nodownload" height="100%" loop="loop" muted="" playsinline="" preload="auto" src="/tenancy/assets/manager/files/video-file.mp4" style="max-width: 100%; height: auto;" width="auto">&nbsp;</video>
</div>
```

---

### 15. LEGACY MODERNIZATION LAYOUT

Split layout: dark gradient left sidebar + white content right.

```html
<div class="sellvio-template sellvio-template--2-cols content-full-width">
<div class="cols cols--gutter-15">
<div class="col-lg-5 bg-dark bg-custom-gradient mb-0 pt-50 pb-50" style="padding: 0 50px;">
<div class="col-card mw-456"><div class="col-card-body">
  <!-- Left sidebar content -->
</div></div>
</div>

<div class="col-lg-7">
<div class="col-card"><div class="col-card-body">
  <!-- Right main content (uses nested 2-cols-b for sub-sections) -->
</div></div>
</div>
</div>
</div>
```

---

## Buttons

| Class | Style | Usage |
|-------|-------|-------|
| `button button--dark` | Dark green filled | Primary CTA |
| `button button--pink` | Pink/coral filled | Secondary CTA (Calendly) |
| `button button--primary` | Primary color | Contact pages |
| `button button--yellow` | Yellow filled | Special links (Kodesage) |
| `button button--bordered` | Green outline | Alternative style |

---

## Image Paths

- Relative (no leading slash): `tenancy/assets/manager/files/custom-content/image.jpg`
- Absolute (with leading slash): `/tenancy/assets/manager/files/custom-content/image.jpg`
- Both patterns are used. Tab images use absolute paths. Brand logos use relative.

---

## Spacing

- `<p>&nbsp;</p>` between sections for vertical spacing
- `mb-0` class on elements to remove bottom margin
- `mb-3 mb-lg-5` for responsive margins (3 on mobile, 5 on desktop)
- `mt-auto` to push element to bottom of flex container
- `pt-30`, `pb-30`, `pt-50`, `pb-50` for padding
- `<br />&nbsp;` inside list items for spacing between items

---

## Writing Style Notes (from existing pages)

- No em dashes in new content (use "," or "." instead)
- No emojis
- Direct, conversational tone
- Short sentences
- Use `&#39;` for apostrophes in HTML attributes
- Use `&times;` for multiplication sign
- Use `&ndash;` for ranges (10-30 becomes 10&ndash;30)
- Use `&rsquo;` for curly apostrophes in display text
