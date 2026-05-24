"""
SRT → PDF konverter
Speaker A: kék, Speaker B: piros — csak a label színes.
Nyomtatható, oldalra formázott kimenet.
"""
import re
import sys
from pathlib import Path
from weasyprint import HTML, CSS

# Path-ek
SRT_PATH = Path("/sessions/compassionate-focused-cerf/mnt/Haladó/Tananyag/TransOffice/meetings/meeting_transcript_20250224.srt")
OUT_PDF = Path("/sessions/compassionate-focused-cerf/mnt/Haladó/Műhely/02_Meeting_Productivity/meeting_transcript_20250224_v2.0_szinezett.pdf")
OUT_HTML = Path("/sessions/compassionate-focused-cerf/mnt/Haladó/Műhely/02_Meeting_Productivity/srt_to_pdf_BUILD/preview.html")

# SRT parse
srt_text = SRT_PATH.read_text(encoding="utf-8")
blocks = re.split(r"\n\s*\n", srt_text.strip())

entries = []
for block in blocks:
    lines = block.strip().splitlines()
    if len(lines) < 3:
        continue
    idx = lines[0].strip()
    time_line = lines[1].strip()
    text = " ".join(lines[2:]).strip()

    # Speaker felismerés
    m = re.match(r"^(Speaker [AB]):\s*(.*)$", text)
    if m:
        speaker = m.group(1)
        utterance = m.group(2)
    else:
        speaker = ""
        utterance = text

    entries.append({
        "idx": idx,
        "time": time_line,
        "speaker": speaker,
        "text": utterance,
    })

print(f"Parsed {len(entries)} entries from SRT")

# HTML építés
html_rows = []
for e in entries:
    speaker_class = "speaker-a" if e["speaker"] == "Speaker A" else "speaker-b" if e["speaker"] == "Speaker B" else "speaker-other"
    # Escape HTML
    text_safe = e["text"].replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    speaker_safe = e["speaker"].replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    time_safe = e["time"]

    html_rows.append(f'''
    <div class="entry">
      <div class="meta">
        <span class="idx">{e["idx"]}</span>
        <span class="time">{time_safe}</span>
      </div>
      <div class="dialogue">
        <span class="speaker {speaker_class}">{speaker_safe}:</span>
        <span class="text">{text_safe}</span>
      </div>
    </div>
''')

html_doc = f"""<!DOCTYPE html>
<html lang="hu">
<head>
  <meta charset="utf-8">
  <title>Meeting Transcript — 2025-02-24</title>
  <style>
    @page {{
      size: A4;
      margin: 18mm 16mm 18mm 16mm;
      @bottom-center {{
        content: counter(page) " / " counter(pages);
        font-family: "Helvetica", "Arial", sans-serif;
        font-size: 9pt;
        color: #888;
      }}
      @top-center {{
        content: "Meeting transcript — TransOffice Trade SRL — 2025-02-24";
        font-family: "Helvetica", "Arial", sans-serif;
        font-size: 8.5pt;
        color: #999;
      }}
    }}

    body {{
      font-family: "Helvetica", "Arial", sans-serif;
      font-size: 11pt;
      line-height: 1.5;
      color: #1a1a1a;
      margin: 0;
      padding: 0;
    }}

    h1 {{
      font-size: 16pt;
      margin: 0 0 4mm 0;
      color: #1a1a1a;
      border-bottom: 1px solid #ccc;
      padding-bottom: 2mm;
    }}

    .header-info {{
      font-size: 9pt;
      color: #666;
      margin-bottom: 6mm;
      line-height: 1.4;
    }}

    .entry {{
      margin-bottom: 3.5mm;
      page-break-inside: avoid;
    }}

    .meta {{
      font-size: 8pt;
      color: #888;
      font-family: "Menlo", "Consolas", "Courier New", monospace;
      margin-bottom: 0.5mm;
    }}

    .meta .idx {{
      display: inline-block;
      width: 6mm;
      color: #aaa;
    }}

    .meta .time {{
      color: #888;
    }}

    .dialogue {{
      padding-left: 6mm;
    }}

    .speaker {{
      font-weight: bold;
      margin-right: 2mm;
    }}

    .speaker-a {{
      color: #1565c0;  /* kék */
    }}

    .speaker-b {{
      color: #c62828;  /* piros */
    }}

    .speaker-other {{
      color: #555;
    }}

    .text {{
      color: #1a1a1a;
    }}
  </style>
</head>
<body>
  <h1>Meeting transcript — TransOffice Trade SRL</h1>
  <div class="header-info">
    <strong>Dátum:</strong> 2025. február 24. (kedd) &nbsp;|&nbsp;
    <strong>Időtartam:</strong> ~7 perc beszéd (40 perc real-time meeting) &nbsp;|&nbsp;
    <strong>Bemondások:</strong> {len(entries)}<br>
    <span style="color:#1565c0;font-weight:bold;">■ Speaker A</span> &nbsp; &nbsp;
    <span style="color:#c62828;font-weight:bold;">■ Speaker B</span>
  </div>
  {"".join(html_rows)}
</body>
</html>
"""

# Mentés HTML-ként is (debug és előnézet)
OUT_HTML.write_text(html_doc, encoding="utf-8")
print(f"HTML preview: {OUT_HTML}")

# PDF generálás
HTML(string=html_doc).write_pdf(str(OUT_PDF))
print(f"PDF kész: {OUT_PDF}")
print(f"Méret: {OUT_PDF.stat().st_size:,} byte")
