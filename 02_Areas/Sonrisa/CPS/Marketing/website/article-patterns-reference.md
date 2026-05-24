# Sonrisa Article Patterns Reference
## Compiled from admin panel review (2026-03-25)

---

## Article Categories in Sellvio

| Category | Content Type | Examples |
|---|---|---|
| **CPS services** | Service/product landing pages | #21 Managed Cloud v2, #20 LLMaaS, #19 DevOps-as-a-Service, #13 AWS Health Check |
| **Our Impact** | Blog articles + case studies | #18 Blog Article 1, #15 Rail Cargo, #14 Global Blue |
| **Our Services** | Legacy Sonrisa service stubs | #4-#8 (mostly empty, lead text only) |

---

## CPS Service Pages (#13, #19, #20, #21)

**Common structure:**
1. Hero section: `template--about-cover` on `bg-mid-green`
2. Trust bar: `template--brands` on `bg-dark`
3. Feature tabs: `template--tabs` (table-based)
4. Pricing/comparison: `table--mobile table--plans`
5. Add-on cards: `sellvio-template--3-cols template--addons`
6. CTA banners: `template--section-featured bg-theme` with Calendly + Szabolcs photo
7. Services list: `template--numbered-table` on `bg-dark`
8. Contact form: `template--form-picture` on `bg-gray-green`
9. Personal quote: Szabolcs bio on `bg-mid-green`

**CTA pattern:**
```html
<div class="template--section-featured bg-theme bg-full-width content-w-1280">
  <div class="cols">
    <div class="col-lg-9">
      <h2 style="text-align: center;">CTA headline with <strong>bold service</strong> and <em>italic qualifier</em></h2>
      <p style="text-align: center;">Supporting text</p>
      <p style="text-align: center;">
        <a class="button button--dark" href="" onclick="Calendly.initPopupWidget({url: 'https://calendly.com/becze-szabolcs-sonrisa/sonrisa-devops-consultation-30mins'});return false;">Talk to an Expert</a>
      </p>
    </div>
    <div class="col-lg-auto">
      <div class="hover-item" style="display: flex; align-items: flex-end; margin-bottom: 0;">
        <h6 class="hover-item__title" style="text-align: right;">Let's chat!</h6>
        <p><img alt="" src="/tenancy/assets/manager/files/custom-content/szeg1-opt.jpg" /></p>
      </div>
    </div>
  </div>
</div>
```

**Key assets:**
- Szabolcs headshot (CTA): `/tenancy/assets/manager/files/custom-content/szeg1-opt.jpg`
- Szabolcs headshot (alt): `/tenancy/assets/manager/files/custom-content/hover-img-2-1.jpg`
- Szabolcs portrait (bio): `tenancy/assets/manager/files/custom-content/szabolcs-becze-head-of-cps-sonrisa.png`
- Quote sign: `/tenancy/assets/manager/files/custom-content/quote-sign.png`
- LinkedIn icon: `/tenancy/assets/manager/files/custom-content/linkedin-blue.png`
- Check mark: `tenancy/assets/manager/files/custom-content/check-green.png`
- CSS: `https://sonrisa.mysellvio.com/tenancy/assets/manager/files/custom-content/landing.css?v=1.6`

---

## Case Studies (#14, #15) - "Our Impact" category

**Structure:** Challenge > Solution > Implementation > Results > Conclusion > Collaboration > What's Next

**CTA pattern (different from CPS pages!):**
```html
<div class="dragdiv">
  <div class="bg-light-green bg-full-width">
    <div class="dragdiv">
      <div class="sellvio-template sellvio-template--60-width">
        <div class="cols">
          <div class="col-md-9 mx-auto">
            <h2 style="text-align: center;">CTA headline</h2>
            <p style="text-align: center;">
              <a class="button button--dark" href="mailto:miklosn@sonrisa.hu" type="button">CTA text</a>
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
```

**Issues to avoid (seen in existing case studies):**
- Word `paraeid`/`paraid` attributes on elements
- `&rsquo;` / `&mdash;` entities (use straight quotes and -- or plain dashes)
- `<h1>` used for subsection headings (should be `<h2>` or `<h6>`)
- Multiple empty `<p>&nbsp;</p>` for spacing
- `mailto:miklosn@sonrisa.hu` links (CPS articles should use Calendly instead)

---

## Blog Articles (#18) - "Our Impact" category

**Our article (v0.1) established new blog patterns:**
- Series label above title: `MANAGED SERVICE SERIES -- ARTICLE 1 OF 3`
- Highlighted scenario box: `bg-gray-green bg-full-width`
- Risk cards: 2x2 grid using `col-md-6` inside `sellvio-template--3-cols template--addons` on `bg-dark`
- Comparison table: `table--mobile table--plans` on `bg-gray-green`
- Series teaser: centered text on `bg-gray-green`
- CTA: `template--section-featured bg-theme` with Calendly (same as CPS pages)

**Differences from case studies:**
- Uses Calendly CTAs (not mailto)
- Uses CPS-style bg classes (bg-gray-green, bg-dark) not bg-light-green
- No Word artifacts
- Section comments for structure
- Version comment at top

---

## Issues Found During Review

1. **Article #18 (our blog):** Has `&mdash;` in series label -- should be plain `--` per our formatting rules. SEO fields (meta title, meta description) are empty.
2. **Case studies:** All use `mailto:miklosn@sonrisa.hu` -- should be updated to Calendly for CPS-aligned content.
3. **Article #19 (DevOps-as-a-Service):** Contains `&rsquo;` and `&mdash;` entities. Has a duplicate CTA with both mailto and Calendly links on the second CTA banner. Missing version comment. Uses landing.css v1.5 (not v1.6).
4. **Legacy Our Services pages (#4-#8):** Mostly empty stubs with only lead text, no Description HTML.
