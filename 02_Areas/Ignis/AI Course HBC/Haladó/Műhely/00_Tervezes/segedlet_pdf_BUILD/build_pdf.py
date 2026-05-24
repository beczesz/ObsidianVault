"""
Oktatoi segedlet v2.0 -> nyomtathato szines PDF.
- Color-kodolt elemek: MONDOM (kek), PROMPT (szurke kodblokk), VIGYAZZ (narancs), STACIO (zold)
- Page-break safe major szekcionkent
- Fejlec + oldalszam
"""
import re
import markdown
from pathlib import Path
from weasyprint import HTML, CSS

INPUT = Path("/sessions/compassionate-focused-cerf/mnt/Haladó/Műhely/00_Tervezes/09_Oktatoi_segedlet_v2.0.md")
OUTPUT_PDF = Path("/sessions/compassionate-focused-cerf/mnt/Haladó/Műhely/00_Tervezes/Oktatoi_segedlet_v2.0.pdf")
OUTPUT_HTML = Path("/sessions/compassionate-focused-cerf/mnt/Haladó/Műhely/00_Tervezes/segedlet_pdf_BUILD/preview.html")

md_text = INPUT.read_text(encoding="utf-8")

# Convert MD to HTML
html_body = markdown.markdown(
    md_text,
    extensions=['extra', 'sane_lists', 'tables', 'fenced_code', 'toc']
)

# Post-process: add semantic classes for color coding
# MONDOM: "**MONDOM:**" → blue
# PROMPT: "**PROMPT (..)**:" → keep as is, gray code block follows
# VIGYAZZ: "**VIGYAZZ:**" → orange
# Wrap each MONDOM bullet in a div with class
# Actually with the markdown converter, **MONDOM:** is now <strong>MONDOM:</strong>

# Simple approach: use CSS attribute selectors on strong elements
# But we can also wrap entire paragraphs that start with these markers

import re as _re
# Replace <p> elements that contain specific markers
def annotate(html):
    # MONDOM blocks
    html = _re.sub(
        r'<p>(<strong>📍 MONDOM:</strong>.*?)</p>',
        r'<p class="mondom">\1</p>',
        html,
        flags=_re.DOTALL
    )
    # VIGYAZZ blocks
    html = _re.sub(
        r'<p>(<strong>⚠️ VIGYÁZZ:</strong>.*?)</p>',
        r'<p class="vigyazz">\1</p>',
        html,
        flags=_re.DOTALL
    )
    # CSINALOM blocks
    html = _re.sub(
        r'<p>(🖥 <strong>CSINÁLOM.*?</strong>.*?)</p>',
        r'<p class="csinalom">\1</p>',
        html,
        flags=_re.DOTALL
    )
    # PROMPT label paragraphs
    html = _re.sub(
        r'<p>(📝 <strong>PROMPT.*?</strong>.*?)</p>',
        r'<p class="prompt-label">\1</p>',
        html,
        flags=_re.DOTALL
    )
    return html

html_body = annotate(html_body)

# Build full HTML document
html_doc = f"""<!DOCTYPE html>
<html lang="hu">
<head>
<meta charset="utf-8">
<title>Oktatói segédlet v2.0</title>
<style>
@page {{
  size: A4;
  margin: 18mm 16mm 18mm 16mm;
  @top-center {{
    content: "Oktatói segédlet v2.0 — Ignis Academy Haladó AI Workshop";
    font-family: "Helvetica", "Arial", sans-serif;
    font-size: 8.5pt;
    color: #999;
  }}
  @bottom-center {{
    content: counter(page) " / " counter(pages);
    font-family: "Helvetica", "Arial", sans-serif;
    font-size: 9pt;
    color: #888;
  }}
}}

body {{
  font-family: "Helvetica", "Arial", sans-serif;
  font-size: 10.5pt;
  line-height: 1.5;
  color: #1a1a1a;
}}

/* Headings */
h1 {{
  font-size: 22pt;
  color: #1a1a1a;
  border-bottom: 2px solid #333;
  padding-bottom: 3mm;
  margin-top: 0;
  page-break-after: avoid;
}}

h2 {{
  font-size: 16pt;
  color: #1565c0;
  margin-top: 8mm;
  margin-bottom: 3mm;
  border-bottom: 1px solid #ccd6e0;
  padding-bottom: 2mm;
  page-break-after: avoid;
  page-break-before: always;
}}

/* The very first h2 (Tartalomjegyzek) shouldn't break */
h2:first-of-type {{
  page-break-before: avoid;
}}

h3 {{
  font-size: 13pt;
  color: #2e7d32;
  margin-top: 5mm;
  margin-bottom: 2mm;
  page-break-after: avoid;
}}

h4 {{
  font-size: 11.5pt;
  color: #455a64;
  margin-top: 4mm;
  margin-bottom: 2mm;
  page-break-after: avoid;
}}

/* Blockquotes */
blockquote {{
  border-left: 4px solid #1565c0;
  background: #f3f8fd;
  margin: 3mm 0;
  padding: 2mm 4mm;
  color: #1a1a1a;
  font-style: italic;
  page-break-inside: avoid;
}}

blockquote em {{
  font-style: italic;
  color: #1565c0;
}}

/* Tables */
table {{
  border-collapse: collapse;
  width: 100%;
  margin: 3mm 0;
  page-break-inside: avoid;
  font-size: 9.5pt;
}}

th {{
  background: #1565c0;
  color: #fff;
  padding: 1.5mm 2mm;
  text-align: left;
  font-weight: 600;
}}

th strong, th em, th {{
  color: white !important;
}}

td {{
  border-bottom: 1px solid #e0e6ed;
  padding: 1.5mm 2mm;
  vertical-align: top;
}}

tr:nth-child(even) td {{
  background: #f7faff;
}}

/* Code blocks (prompts) */
pre {{
  background: #f4f5f7;
  border: 1px solid #d8dde3;
  border-left: 4px solid #5a6478;
  padding: 3mm 4mm;
  font-family: "Menlo", "Consolas", "Courier New", monospace;
  font-size: 8.5pt;
  line-height: 1.4;
  overflow-wrap: break-word;
  white-space: pre-wrap;
  margin: 2mm 0 4mm 0;
  page-break-inside: avoid;
  color: #1a1a1a;
}}

code {{
  font-family: "Menlo", "Consolas", "Courier New", monospace;
  font-size: 9pt;
  background: #f4f5f7;
  padding: 0.5mm 1mm;
  border-radius: 1mm;
}}

/* Inline modifiers */
p.mondom {{
  background: #e8f4fd;
  border-left: 3px solid #1565c0;
  padding: 2mm 3mm;
  margin: 2mm 0;
  page-break-inside: avoid;
}}

p.mondom strong {{
  color: #1565c0;
}}

p.vigyazz {{
  background: #fff3e0;
  border-left: 3px solid #e65100;
  padding: 2mm 3mm;
  margin: 2mm 0;
  page-break-inside: avoid;
}}

p.vigyazz strong {{
  color: #e65100;
}}

p.csinalom {{
  background: #f1f8e9;
  border-left: 3px solid #558b2f;
  padding: 2mm 3mm;
  margin: 2mm 0;
  page-break-inside: avoid;
}}

p.csinalom strong {{
  color: #558b2f;
}}

p.prompt-label {{
  background: #f4f5f7;
  padding: 1.5mm 3mm;
  margin: 2mm 0 0 0;
  font-weight: 600;
  border-radius: 1mm 1mm 0 0;
}}

p.prompt-label strong {{
  color: #5a6478;
}}

/* Lists */
ul, ol {{
  margin: 2mm 0;
  padding-left: 5mm;
}}

li {{
  margin: 0.8mm 0;
}}

/* Horizontal rule */
hr {{
  border: none;
  border-top: 1px dashed #ccd6e0;
  margin: 5mm 0;
}}

/* Strong general */
strong {{
  color: #1a1a1a;
}}

/* Anchor tags */
a {{
  color: #1565c0;
  text-decoration: none;
}}

/* TOC links */
h2 + ol, h2 + ul {{
  font-size: 9.5pt;
}}
</style>
</head>
<body>
{html_body}
</body>
</html>
"""

OUTPUT_HTML.write_text(html_doc, encoding="utf-8")
print(f"HTML preview: {OUTPUT_HTML}")

HTML(string=html_doc).write_pdf(str(OUTPUT_PDF))
print(f"PDF kész: {OUTPUT_PDF}")
print(f"Méret: {OUTPUT_PDF.stat().st_size:,} byte")
