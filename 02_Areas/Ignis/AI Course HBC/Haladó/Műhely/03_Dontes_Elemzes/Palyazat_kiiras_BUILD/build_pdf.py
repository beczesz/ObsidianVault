#!/usr/bin/env python3
"""
Build script: Markdown → HTML → PDF (weasyprint)
v2: kék paletta, diagonal watermark, kompaktabb header
"""
import re
import sys
from pathlib import Path
import markdown
from weasyprint import HTML, CSS

BASE = Path("/sessions/compassionate-focused-cerf/mnt/outputs/F3_palyazat_v2")
MD_FILE = BASE / "Ghidul-solicitantului-Mobilitate-Verde-IMM-2025.md"
CSS_FILE = BASE / "build" / "style.css"
HTML_OUT = BASE / "build" / "doc.html"
PDF_OUT = BASE / "Ghidul-solicitantului-Mobilitate-Verde-IMM-2025.pdf"

# 1. Az MD beolvasása
text = MD_FILE.read_text(encoding="utf-8")

# 2. Vágjuk le a cover/cuprins manuális részt — az első "## 1. PREAMBUL" előtti rész
m = re.search(r'^## 1\. PREAMBUL', text, flags=re.MULTILINE)
if not m:
    sys.exit("Nem találom a '## 1. PREAMBUL' kezdetet.")
md_body = text[m.start():]

# 3. Markdown → HTML
md = markdown.Markdown(extensions=['extra', 'tables', 'sane_lists', 'toc'])
body_html = md.convert(md_body)

# 4. Cuprins generálás
cuprins_entries = []
for line in md_body.splitlines():
    m1 = re.match(r'^(#{2,4}) (.+)$', line)
    if not m1:
        continue
    level = len(m1.group(1)) - 1
    title = m1.group(2).strip()
    title_clean = re.sub(r'\*\*(.+?)\*\*', r'\1', title)
    title_clean = re.sub(r'\*(.+?)\*', r'\1', title_clean)
    title_clean = re.sub(r'`(.+?)`', r'\1', title_clean)
    if level <= 2:
        cuprins_entries.append((level, title_clean))

cuprins_html_parts = ['<div class="toc"><h1>Cuprins</h1>']
for level, title in cuprins_entries:
    m_num = re.match(r'^(\d+(?:\.\d+)*)\.\s+(.+)$', title)
    if m_num:
        num = m_num.group(1)
        rest = m_num.group(2)
    else:
        num = ""
        rest = title
    cuprins_html_parts.append(
        f'<div class="toc-item level-{level}">'
        f'<span class="toc-num">{num}</span>'
        f'<span class="toc-title">{rest}</span>'
        f'<span class="toc-leader"></span>'
        f'<span class="toc-page"></span>'
        f'</div>'
    )
cuprins_html_parts.append('</div>')
cuprins_html = '\n'.join(cuprins_html_parts)

# 5. Cover page HTML — kék paletta, diagonal watermark, dekoratív körök
cover_html = '''
<div class="cover">
  <div class="cover-header-bar">
    <div class="logo-block eu-logo">
      <strong>Cofinanțat de</strong>
      <span style="color:#ffcc00;">★ ★ ★</span><br>
      Uniunea Europeană
    </div>
    <div class="logo-block ro-logo">
      <strong>GUVERNUL ROMÂNIEI</strong>
      <span>Ministerul Mediului,<br>Apelor și Pădurilor</span>
    </div>
    <div class="logo-block program-logo">
      <strong>AFM</strong>
      <span style="color:white">Administrația Fondului<br>pentru Mediu</span>
    </div>
  </div>
  
  <div class="cover-graphic">
    <div class="circle c1"></div>
    <div class="circle c2"></div>
    <div class="circle c3"></div>
    <div class="circle c4"></div>
  </div>
  
  <div class="cover-watermark">GHIDUL SOLICITANTULUI</div>
  
  <div class="cover-content">
    <div class="cover-program-name">Programul Mobilitate Verde IMM 2025</div>
    
    <div class="cover-priority-label">PRIORITATEA 1:</div>
    <div class="cover-priority-text">
      O ECONOMIE VERDE ȘI REZILIENTĂ PRIN<br>
      ELECTROMOBILITATE ȘI INFRASTRUCTURĂ<br>
      DE REÎNCĂRCARE
    </div>
    
    <div class="cover-os-block">
      <strong>OS 1.2</strong> &nbsp;Sprijinirea tranziției către mobilitate cu emisii reduse de carbon<br>
      <strong>Acțiunea 1.4:</strong> &nbsp;Sprijin pentru întreprinderile mici și mijlocii în vederea înnoirii parcului auto cu vehicule electrice<br>
      <strong>Intervenția 1.4.1:</strong> &nbsp;Achiziția de vehicule electrice și instalarea infrastructurii de reîncărcare aferente — sprijin pentru IMM
    </div>
  </div>
  
  <div class="cover-stamp">GHIDUL SOLICITANTULUI</div>
  
  <div class="cover-footer-info">
    <strong>Administrația Fondului pentru Mediu (AFM)</strong><br>
    Splaiul Independenței nr. 294, Sector 6, 060031, București<br>
    www.afm.ro &nbsp;|&nbsp; officeprograme@afm.ro &nbsp;|&nbsp; Tel.: 021-319.48.40<br>
    <em style="font-size:8pt;">Versiunea 1.0 | Data publicării: 17 martie 2025 | Ordin AFM nr. 234 / 14 martie 2025</em>
  </div>
</div>
'''

# 6. Running header / footer
running_blocks = '''
<div id="header-logos">
  <div class="h-logo"><strong>Cofinanțat de Uniunea Europeană</strong></div>
  <div class="h-logo"><strong>Guvernul României</strong> — Ministerul Mediului</div>
  <div class="h-logo"><strong>AFM</strong> — Programul Mobilitate Verde IMM 2025</div>
</div>
<div id="footer-block">
  <span class="footer-line"><strong>AFM</strong> — Autoritate de Implementare Programul Mobilitate Verde IMM 2025</span>
  <span class="footer-line">www.afm.ro &nbsp;|&nbsp; officeprograme@afm.ro &nbsp;|&nbsp; Splaiul Independenței nr. 294, Sector 6, București</span>
</div>
'''

# 7. Egyesítjük
full_html = f'''<!DOCTYPE html>
<html lang="ro">
<head>
  <meta charset="utf-8">
  <title>Ghidul Solicitantului — Programul Mobilitate Verde IMM 2025</title>
</head>
<body>
{running_blocks}
{cover_html}
{cuprins_html}
{body_html}
</body>
</html>'''

HTML_OUT.write_text(full_html, encoding="utf-8")
print(f"HTML létrehozva: {len(full_html):,} karakter")

# 8. PDF generálás
print("PDF generálás folyamatban...")
HTML(filename=str(HTML_OUT)).write_pdf(
    str(PDF_OUT),
    stylesheets=[CSS(filename=str(CSS_FILE))]
)

import subprocess
size_kb = PDF_OUT.stat().st_size / 1024
pages = subprocess.run(['pdfinfo', str(PDF_OUT)], capture_output=True, text=True).stdout
pages_match = re.search(r'^Pages:\s+(\d+)', pages, re.MULTILINE)
print(f"PDF kész: {PDF_OUT}")
print(f"  Méret: {size_kb:,.0f} KB")
print(f"  Oldalak: {pages_match.group(1) if pages_match else '?'}")
