"""
28 AI Tipp — Tananyag PDF generáló
Styleguide alapján: kék gradient, fehér szöveg, Montserrat-stílusú tipográfia
DejaVu Sans font a magyar ékezetes karakterek támogatásához
"""

import re
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm, cm
from reportlab.lib.colors import HexColor, white, black, Color
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak,
    Table, TableStyle, KeepTogether, Flowable, Frame, PageTemplate
)
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# ── Register Unicode fonts ──
pdfmetrics.registerFont(TTFont('DejaVu', '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('DejaVu-Bold', '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'))
pdfmetrics.registerFont(TTFont('DejaVu-Oblique', '/usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf'))
pdfmetrics.registerFont(TTFont('DejaVu-BoldOblique', '/usr/share/fonts/truetype/dejavu/DejaVuSans-BoldOblique.ttf'))

from reportlab.pdfbase.pdfmetrics import registerFontFamily
registerFontFamily('DejaVu',
    normal='DejaVu',
    bold='DejaVu-Bold',
    italic='DejaVu-Oblique',
    boldItalic='DejaVu-BoldOblique')

# ── Colors (from styleguide) ──
DARK_BLUE = HexColor("#1A3580")
BLUE = HexColor("#2266E3")
LIGHT_BLUE = HexColor("#4A8CF7")
GOLD = HexColor("#FFD431")
WHITE = HexColor("#FFFFFF")
OFF_WHITE = HexColor("#F0F1F4")
DARK_GRAY = HexColor("#333333")
MID_GRAY = HexColor("#3E3E3E")
LIGHT_GRAY = HexColor("#E8E9EC")
VERY_LIGHT_BLUE = HexColor("#EDF2FE")
CREAM = HexColor("#F8F9FC")

PAGE_W, PAGE_H = A4
MARGIN = 20 * mm

# ── Parse the markdown source ──

def parse_tips_from_md(filepath):
    """Parse ai_learning_material_v0.4.md and extract tips with proper Hungarian text."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract introduction
    intro_match = re.search(r'# Bevezetés\n\n(.*?)(?=\n---\n\n# Tippek)', content, re.DOTALL)
    intro_text = intro_match.group(1).strip() if intro_match else ""

    # Extract dimension descriptions
    dimensions = {}
    dim_patterns = [
        ("ethos", r'## 1\. Fizikai dimenzió — Felelősségvállalás \(Ethos\)\n\n\*(.*?)\*', "Felelősségvállalás (Ethos)", "Csak az ember képes valódi felelősséget vállalni; a gép nem."),
        ("logos", r'## 2\. Intellektuális dimenzió — Értelem, összefüggések \(Logos\)\n\n\*(.*?)\*', "Értelem, összefüggések (Logos)", "A gép számol, de nem érti; csak az ember képes átlátni az összefüggéseket."),
        ("pathos", r'## 3\. Érzelmi dimenzió — Empátia \(Pathos\)\n\n\*(.*?)\*', "Empátia (Pathos)", "Az ember empátiája mélyen biológiai gyökerű, nem szimuláció."),
        ("thelos", r'## 4\. Spirituális dimenzió — Vágyak, küldetéstudat \(Thelos\)\n\n\*(.*?)\*', "Vágyak, küldetéstudat (Thelos)", "Az emberben ott van a vágy, hogy jobbá tegye a világot; a gép vágy nélküli."),
    ]
    for key, pattern, title, subtitle in dim_patterns:
        dimensions[key] = {"title": title, "subtitle": subtitle}

    # Extract individual tips
    tip_pattern = r'### 🔹 ([A-Z]\d+): (.*?)\n.*?\*\*Alapelv:\*\* \*(.*?)\*\n\n\*\*Leírás:\*\* (.*?)\n\n\*\*Konkrét példa:\*\* (.*?)(?=\n\n---|\n\n\*\*Bónusz|\Z)'
    tips = []
    for m in re.finditer(tip_pattern, content, re.DOTALL):
        tip_id = m.group(1).strip()
        title = m.group(2).strip()
        # Clean title - remove everything after " — "
        title = title.split(' — ')[0].strip()
        principle = m.group(3).strip()
        desc = m.group(4).strip()
        example = m.group(5).strip()

        # Determine dimension and remap IDs to readable format
        if tip_id.startswith('F'):
            dim = 'ethos'
            num = tip_id[1:]
            tip_id = f"Ethos #{num}"
        elif tip_id.startswith('I'):
            dim = 'logos'
            num = tip_id[1:]
            tip_id = f"Logos #{num}"
        elif tip_id.startswith('E'):
            dim = 'pathos'
            num = tip_id[1:]
            tip_id = f"Pathos #{num}"
        else:
            dim = 'thelos'
            num = tip_id[1:]
            tip_id = f"Thelos #{num}"

        # Clean up markdown formatting from text
        for field in [desc, example, principle]:
            pass
        desc = re.sub(r'\*\*(.*?)\*\*', r'\1', desc)  # Remove bold
        desc = re.sub(r'\*(.*?)\*', r'\1', desc)  # Remove italic
        desc = re.sub(r'\n\n', ' ', desc)  # Join paragraphs
        desc = re.sub(r'\n', ' ', desc)
        example = re.sub(r'\*\*(.*?)\*\*', r'\1', example)
        example = re.sub(r'\*(.*?)\*', r'\1', example)
        example = re.sub(r'\n\n', ' ', example)
        example = re.sub(r'\n', ' ', example)
        principle = re.sub(r'\*\*(.*?)\*\*', r'\1', principle)

        # Truncate very long descriptions for PDF (keep first ~400 chars)
        if len(desc) > 500:
            # Find last sentence boundary before 500 chars
            truncated = desc[:500]
            last_period = truncated.rfind('.')
            if last_period > 200:
                desc = truncated[:last_period + 1]
            else:
                desc = truncated + '...'

        if len(example) > 400:
            truncated = example[:400]
            last_period = truncated.rfind('.')
            if last_period > 150:
                example = truncated[:last_period + 1]
            else:
                example = truncated + '...'

        tips.append({
            "id": tip_id,
            "dim": dim,
            "title": title,
            "principle": principle,
            "desc": desc,
            "example": example,
        })

    return tips, dimensions, intro_text


# ── Custom flowables ──

class GradientRect(Flowable):
    """A rectangle with gradient fill."""
    def __init__(self, width, height, color_left, color_right, radius=6):
        Flowable.__init__(self)
        self.width = width
        self.height = height
        self.color_left = color_left
        self.color_right = color_right
        self.radius = radius

    def draw(self):
        c = self.canv
        steps = 40
        strip_w = self.width / steps
        r1, g1, b1 = self.color_left.red, self.color_left.green, self.color_left.blue
        r2, g2, b2 = self.color_right.red, self.color_right.green, self.color_right.blue
        for i in range(steps):
            t = i / (steps - 1)
            r = r1 + (r2 - r1) * t
            g = g1 + (g2 - g1) * t
            b = b1 + (b2 - b1) * t
            c.setFillColor(Color(r, g, b))
            c.rect(i * strip_w, 0, strip_w + 1, self.height, fill=1, stroke=0)


class CoverBlock(Flowable):
    """Full-width gradient block for cover page."""
    def __init__(self, width, height):
        Flowable.__init__(self)
        self.width = width
        self.height = height

    def draw(self):
        c = self.canv
        # Gradient background
        steps = 50
        strip_w = self.width / steps
        r1, g1, b1 = DARK_BLUE.red, DARK_BLUE.green, DARK_BLUE.blue
        r2, g2, b2 = LIGHT_BLUE.red, LIGHT_BLUE.green, LIGHT_BLUE.blue
        for i in range(steps):
            t = i / (steps - 1)
            r = r1 + (r2 - r1) * t
            g = g1 + (g2 - g1) * t
            b = b1 + (b2 - b1) * t
            c.setFillColor(Color(r, g, b))
            c.rect(i * strip_w, 0, strip_w + 1, self.height, fill=1, stroke=0)

        # Title text
        c.setFillColor(WHITE)
        c.setFont("DejaVu-Bold", 36)
        c.drawString(30, self.height - 55, "28 AI Tipp")
        c.setFont("DejaVu", 16)
        c.drawString(30, self.height - 82, "4 Emberi Dimenzió")

        # Gold accent line
        c.setFillColor(GOLD)
        c.rect(30, self.height - 95, 100, 3, fill=1, stroke=0)

        # Subtitle
        c.setFillColor(Color(1, 1, 1, 0.85))
        c.setFont("DejaVu", 11)
        c.drawString(30, 25, "Gyakorlati tippek az AI haladó felhasználásához")


class ColorBar(Flowable):
    """Thin accent bar."""
    def __init__(self, width, height=3, color=GOLD):
        Flowable.__init__(self)
        self.width = width
        self.height = height
        self.color = color

    def draw(self):
        self.canv.setFillColor(self.color)
        self.canv.roundRect(0, 0, self.width, self.height, 1.5, fill=1, stroke=0)


class DimensionHeader(Flowable):
    """Section header for each dimension with colored left bar and gradient."""
    def __init__(self, width, number, title, subtitle, accent_color=BLUE):
        Flowable.__init__(self)
        self.width = width
        self.height = 62
        self.number = number
        self.title = title
        self.subtitle = subtitle
        self.accent_color = accent_color

    def draw(self):
        c = self.canv
        # Background with rounded rect
        c.setFillColor(VERY_LIGHT_BLUE)
        c.roundRect(0, 0, self.width, self.height, 6, fill=1, stroke=0)
        # Left accent bar
        c.setFillColor(self.accent_color)
        c.roundRect(0, 0, 5, self.height, 2, fill=1, stroke=0)
        # Number circle
        c.setFillColor(self.accent_color)
        c.circle(28, self.height - 22, 14, fill=1, stroke=0)
        c.setFillColor(WHITE)
        c.setFont("DejaVu-Bold", 14)
        c.drawCentredString(28, self.height - 27, self.number)
        # Title
        c.setFillColor(DARK_BLUE)
        c.setFont("DejaVu-Bold", 17)
        c.drawString(50, self.height - 27, self.title)
        # Subtitle
        c.setFillColor(MID_GRAY)
        c.setFont("DejaVu-Oblique", 9.5)
        c.drawString(15, 10, self.subtitle)


class TipCard(Flowable):
    """Card-style header block for individual tip."""
    def __init__(self, width, tip_id, title, principle):
        Flowable.__init__(self)
        self.width = width
        self.tip_id = tip_id
        self.title = title
        self.principle = principle
        # Calculate height based on title length
        self.height = 65

    def draw(self):
        c = self.canv
        # Card background
        c.setFillColor(OFF_WHITE)
        c.roundRect(0, 0, self.width, self.height, 5, fill=1, stroke=0)
        # Blue badge for tip ID
        c.setFont("DejaVu-Bold", 9)
        badge_w = c.stringWidth(self.tip_id, "DejaVu-Bold", 9) + 16
        badge_w = max(badge_w, 50)
        c.setFillColor(BLUE)
        c.roundRect(12, self.height - 32, badge_w, 24, 4, fill=1, stroke=0)
        c.setFillColor(WHITE)
        c.setFont("DejaVu-Bold", 9)
        c.drawCentredString(12 + badge_w / 2, self.height - 26, self.tip_id)
        # Title
        c.setFillColor(DARK_BLUE)
        c.setFont("DejaVu-Bold", 12.5)
        title = self.title
        max_title_w = self.width - (12 + badge_w + 10) - 10
        while c.stringWidth(title, "DejaVu-Bold", 12.5) > max_title_w and len(title) > 10:
            title = title[:-4] + '...'
        c.drawString(12 + badge_w + 10, self.height - 26, title)
        # Principle line
        c.setFillColor(MID_GRAY)
        c.setFont("DejaVu-Oblique", 9)
        principle = self.principle
        if len(principle) > 95:
            principle = principle[:92] + '...'
        c.drawString(12, 10, principle)


class DimOverviewCard(Flowable):
    """Small card for dimension overview on cover page."""
    def __init__(self, width, number, title, subtitle, color):
        Flowable.__init__(self)
        self.width = width
        self.height = 42
        self.number = number
        self.title = title
        self.subtitle = subtitle
        self.color = color

    def draw(self):
        c = self.canv
        # Background
        c.setFillColor(self.color)
        c.roundRect(0, 0, self.width, self.height, 5, fill=1, stroke=0)
        # Number
        c.setFillColor(Color(1, 1, 1, 0.3))
        c.setFont("DejaVu-Bold", 28)
        c.drawString(10, 8, self.number)
        # Title
        c.setFillColor(WHITE)
        c.setFont("DejaVu-Bold", 12)
        c.drawString(42, self.height - 18, self.title)
        # Subtitle
        c.setFillColor(Color(1, 1, 1, 0.85))
        c.setFont("DejaVu", 8.5)
        sub = self.subtitle
        if len(sub) > 75:
            sub = sub[:72] + '...'
        c.drawString(42, 8, sub)


# ── Escape XML entities for Paragraph ──
def esc(text):
    """Escape text for use in ReportLab Paragraph (XML-like)."""
    text = text.replace('&', '&amp;')
    text = text.replace('<', '&lt;')
    text = text.replace('>', '&gt;')
    return text


# ── Page template ──

def page_template(canvas_obj, doc):
    """Footer on content pages."""
    canvas_obj.saveState()
    # Footer line
    canvas_obj.setStrokeColor(LIGHT_GRAY)
    canvas_obj.setLineWidth(0.5)
    canvas_obj.line(MARGIN, 16 * mm, PAGE_W - MARGIN, 16 * mm)
    # Footer text
    canvas_obj.setFillColor(MID_GRAY)
    canvas_obj.setFont("DejaVu", 7.5)
    canvas_obj.drawString(MARGIN, 12 * mm, "28 AI Tipp — 4 Emberi Dimenzió")
    canvas_obj.drawRightString(PAGE_W - MARGIN, 12 * mm, f"{doc.page}")
    canvas_obj.restoreState()


def cover_page_template(canvas_obj, doc):
    """Cover page - no footer."""
    pass


# ── Styles ──

def get_styles():
    return {
        'body': ParagraphStyle(
            'Body',
            fontName='DejaVu',
            fontSize=9.5,
            leading=15,
            textColor=DARK_GRAY,
            alignment=TA_JUSTIFY,
            spaceAfter=6,
        ),
        'body_italic': ParagraphStyle(
            'BodyItalic',
            fontName='DejaVu-Oblique',
            fontSize=9.5,
            leading=15,
            textColor=MID_GRAY,
            alignment=TA_JUSTIFY,
            spaceAfter=6,
        ),
        'body_bold': ParagraphStyle(
            'BodyBold',
            fontName='DejaVu-Bold',
            fontSize=9.5,
            leading=15,
            textColor=DARK_GRAY,
            spaceAfter=6,
        ),
        'example_label': ParagraphStyle(
            'ExampleLabel',
            fontName='DejaVu-Bold',
            fontSize=9.5,
            leading=15,
            textColor=BLUE,
            spaceAfter=3,
        ),
        'example_body': ParagraphStyle(
            'ExampleBody',
            fontName='DejaVu-Oblique',
            fontSize=9,
            leading=14,
            textColor=MID_GRAY,
            alignment=TA_JUSTIFY,
            leftIndent=10,
            spaceAfter=6,
        ),
        'heading2': ParagraphStyle(
            'Heading2',
            fontName='DejaVu-Bold',
            fontSize=13,
            leading=19,
            textColor=DARK_BLUE,
            spaceBefore=14,
            spaceAfter=6,
        ),
        'intro_heading': ParagraphStyle(
            'IntroHeading',
            fontName='DejaVu-Bold',
            fontSize=18,
            leading=24,
            textColor=DARK_BLUE,
            spaceAfter=12,
        ),
        'quote': ParagraphStyle(
            'Quote',
            fontName='DejaVu-Oblique',
            fontSize=10,
            leading=16,
            textColor=DARK_BLUE,
            leftIndent=12,
            rightIndent=12,
            spaceBefore=6,
            spaceAfter=8,
        ),
        'cover_meta': ParagraphStyle(
            'CoverMeta',
            fontName='DejaVu',
            fontSize=9,
            leading=15,
            textColor=MID_GRAY,
        ),
        'footer_style': ParagraphStyle(
            'FooterStyle',
            fontName='DejaVu',
            fontSize=9,
            textColor=MID_GRAY,
            alignment=TA_CENTER,
        ),
    }


# ── Build PDF ──

def build_pdf():
    md_path = "/sessions/serene-relaxed-tesla/mnt/AI Kurzus/presentation/ai_learning_material_v0.4.md"
    output_path = "/sessions/serene-relaxed-tesla/mnt/AI Kurzus/presentation/28_AI_Tipp_Tananyag.pdf"

    tips, dimensions, intro_text = parse_tips_from_md(md_path)
    print(f"Parsed {len(tips)} tips from markdown")

    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        leftMargin=MARGIN,
        rightMargin=MARGIN,
        topMargin=MARGIN,
        bottomMargin=20 * mm,
    )

    styles = get_styles()
    story = []
    cw = PAGE_W - 2 * MARGIN  # content width

    # ══════════════════════════════════════════════
    # COVER PAGE
    # ══════════════════════════════════════════════

    story.append(Spacer(1, 10))
    story.append(CoverBlock(cw, 130))
    story.append(Spacer(1, 18))

    # Dimension overview cards
    dim_data = [
        ("1", "Felelősségvállalás (Ethos)", "Csak az ember képes valódi felelősséget vállalni.", DARK_BLUE),
        ("2", "Értelem (Logos)", "A gép számol, de nem érti az összefüggéseket.", BLUE),
        ("3", "Empátia (Pathos)", "Az ember empátiája mélyen biológiai, nem szimuláció.", LIGHT_BLUE),
        ("4", "Vágyak (Thelos)", "Az emberben ott van a vágy, hogy jobbá tegye a világot.", HexColor("#2A4494")),
    ]
    for num, title, sub, color in dim_data:
        story.append(DimOverviewCard(cw, num, title, sub, color))
        story.append(Spacer(1, 6))

    story.append(Spacer(1, 20))

    # Author info
    story.append(Paragraph(
        esc("Szerző: Becze Szabolcs"), styles['body_bold']
    ))
    story.append(Paragraph(
        esc("Verzió: 0.4 | 2026. március"), styles['cover_meta']
    ))
    story.append(Paragraph(
        esc("Webinárium: Mi az, amit az AI soha nem vesz el tőled?"), styles['cover_meta']
    ))

    story.append(PageBreak())

    # ══════════════════════════════════════════════
    # INTRODUCTION
    # ══════════════════════════════════════════════

    story.append(Paragraph("Bevezetés", styles['intro_heading']))
    story.append(ColorBar(80, 3, GOLD))
    story.append(Spacer(1, 12))

    intro_paragraphs = [
        "2022 óta folyamatosan ígéret van arra, hogy az AI meg fogja változtatni a világunkat. Ez egy nagyon ijesztő gondolat, és rengetegen gondolkoztak azon, hogy vajon mi is az igazság. Az AI valóban egyre több területet kezd átvenni, ráadásul 2026 tavaszára robbanásszerűen elkezdett hasznosulni az életünkben.",
        "Feltevődött bennem a kérdés: melyek azok a dolgok, amelyeket le fog váltani az AI, és melyek azok, amelyeket nem? Ahelyett, hogy az AI újdonságairól beszélnék, arra szeretnék koncentrálni, hogy milyen az ember és mi az ami nem fog változni szinte soha.",
        "Négy fontos területet találtam, ami az elmúlt hónapokban kikristályosodott:",
    ]
    for p in intro_paragraphs:
        story.append(Paragraph(esc(p), styles['body']))

    story.append(Spacer(1, 4))

    dim_intros = [
        ("<b>Felelősségvállalás (Ethos):</b> Csak az ember képes valódi felelősséget vállalni. A felelősség lényege nem pusztán az, hogy valaki képes dönteni, hanem az, hogy a döntés következménye visszahat az önképére.",
         styles['body']),
        ("<b>Értelem (Logos):</b> A gép számol, de nem érti annak a jelentőségét, amit kiszámol. Csak az ember képes átlátni az összefüggéseket és a dolgok mélyebb értelmét.",
         styles['body']),
        ("<b>Empátia (Pathos):</b> Az ember empátiája mélyen biológiai gyökerű. Ez nem pusztán intellektuális mintázat, mint amit a gép képes szimulálni.",
         styles['body']),
        ("<b>Vágyak (Thelos):</b> Az emberben ott van a vágy, hogy jobbá tegye a világot. A gép vágy nélküli.",
         styles['body']),
    ]
    for text, style in dim_intros:
        story.append(Paragraph(text, style))
        story.append(Spacer(1, 2))

    story.append(Spacer(1, 8))
    story.append(Paragraph(
        esc("Minden tippnél azt keresem, hogy az AI hogyan szolgálja az embert. Örökérvényű alapelvekre épülnek, nem újdonság-hajhász tanácsok."),
        styles['body_italic']
    ))

    story.append(PageBreak())

    # ══════════════════════════════════════════════
    # TIPS BY DIMENSION
    # ══════════════════════════════════════════════

    dim_order = ["ethos", "logos", "pathos", "thelos"]
    dim_meta = {
        "ethos": {"num": "1", "title": "Felelősségvállalás (Ethos)",
                  "subtitle": "Csak az ember képes valódi felelősséget vállalni; a gép nem.",
                  "color": DARK_BLUE},
        "logos": {"num": "2", "title": "Értelem, összefüggések (Logos)",
                  "subtitle": "A gép számol, de nem érti; csak az ember képes átlátni az összefüggéseket.",
                  "color": BLUE},
        "pathos": {"num": "3", "title": "Empátia (Pathos)",
                   "subtitle": "Az ember empátiája mélyen biológiai gyökerű, nem szimuláció.",
                   "color": LIGHT_BLUE},
        "thelos": {"num": "4", "title": "Vágyak, küldetéstudat (Thelos)",
                   "subtitle": "Az emberben ott van a vágy, hogy jobbá tegye a világot; a gép vágy nélküli.",
                   "color": HexColor("#2A4494")},
    }

    current_dim = None
    for tip in tips:
        dim_key = tip["dim"]
        dm = dim_meta[dim_key]

        # New dimension section
        if dim_key != current_dim:
            if current_dim is not None:
                story.append(PageBreak())
            current_dim = dim_key
            story.append(DimensionHeader(cw, dm["num"], dm["title"], dm["subtitle"], dm["color"]))
            story.append(Spacer(1, 14))

        # Tip card + content as KeepTogether
        tip_elements = []
        tip_elements.append(TipCard(cw, tip["id"], tip["title"], tip["principle"]))
        tip_elements.append(Spacer(1, 6))
        tip_elements.append(Paragraph(esc(tip["desc"]), styles['body']))
        tip_elements.append(Spacer(1, 3))
        tip_elements.append(Paragraph("Konkrét példa:", styles['example_label']))
        tip_elements.append(Paragraph(esc(tip["example"]), styles['example_body']))
        tip_elements.append(Spacer(1, 10))
        tip_elements.append(ColorBar(cw * 0.12, 2, LIGHT_GRAY))
        tip_elements.append(Spacer(1, 10))

        story.append(KeepTogether(tip_elements))

    # ══════════════════════════════════════════════
    # CLOSING
    # ══════════════════════════════════════════════

    story.append(PageBreak())

    story.append(Spacer(1, 20))
    story.append(GradientRect(cw, 70, DARK_BLUE, LIGHT_BLUE, 6))

    # Overlay closing title as separate element
    class ClosingTitle(Flowable):
        def __init__(self, width):
            Flowable.__init__(self)
            self.width = width
            self.height = 0  # overlaps with gradient above

        def draw(self):
            pass

    story.append(Spacer(1, -55))
    story.append(Paragraph(
        '<font color="white"><b>Zárás</b></font>',
        ParagraphStyle('ClosingTitle', fontName='DejaVu-Bold', fontSize=22, leading=28,
                       textColor=WHITE, leftIndent=20)
    ))
    story.append(Spacer(1, 30))

    closing_paragraphs = [
        "Ennek a tananyagnak a célja az volt, hogy bemutassam azokat az alapelveket, amelyek nem változnak, miközben az AI körülöttünk szinte hetente változik. Nem a legújabb modellről akartam mesélni. Arról akartam mesélni, ami örökérvényű: az emberről.",
        "Nap mint nap érkeznek újabb hírek. Érthető, ha ez félelmet kelt. De ne hagyd, hogy ez a félelem lebénítson. Az AI egy rendkívüli eszköz, de eszköz. Ahogyan a nyomda sem tette feleslegessé az írót, ahogyan a számológép sem tette feleslegessé a matematikust, az AI sem teszi feleslegessé az embert. Aki ért hozzá.",
        "Az ember ember marad. Emberi problémákat kell megoldanunk, és az emberi problémákhoz emberi válaszok kellenek. A munkádnak akkor lesz értéke a jövőben, ha egyre emberibb leszel: több felelősséget vállalsz, keresed az értelmet abban, amit csinálsz, empatikus vagy azokkal, akikkel dolgozol, és igyekszel az elhívásodban maradni.",
    ]
    for p in closing_paragraphs:
        story.append(Paragraph(esc(p), styles['body']))
        story.append(Spacer(1, 4))

    story.append(Spacer(1, 10))
    story.append(ColorBar(cw * 0.3, 4, GOLD))
    story.append(Spacer(1, 12))

    story.append(Paragraph(
        "<b>Egy lépés most, ne holnap.</b>",
        styles['heading2']
    ))
    story.append(Paragraph(
        esc("Válassz ki egyetlen tippet. Csak egyet. Olyat, ami a legjobban rezonált. És próbáld ki még ma. Nem kell mindent egyszerre. Az első verzió soha nem tökéletes, és nem is kell annak lennie. Elég, ha 0.1. A lényeg, hogy elindulj."),
        styles['body']
    ))

    story.append(Spacer(1, 30))
    story.append(Paragraph(
        esc("Ne az AI ellen harcolj. Használd arra, hogy emberibb legyél."),
        styles['quote']
    ))

    story.append(Spacer(1, 25))
    story.append(Paragraph(
        "<b>Becze Szabolcs</b> | Sonrisa | becze.szabolcs@sonrisa.hu",
        styles['footer_style']
    ))

    # Build
    doc.build(story, onFirstPage=cover_page_template, onLaterPages=page_template)
    print(f"PDF generated: {output_path}")
    print(f"Tips included: {len(tips)}")
    return output_path


if __name__ == "__main__":
    build_pdf()
