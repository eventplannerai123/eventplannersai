"""The Vendor Payment System setup guide, as the branded PDF buyers download.

The Tue 3 CLAUDE CODE line asks for the setup guide "exported as a PDF in the
brand look". A Google Docs export is not that — it comes out in Docs' own
default styling — so the PDF is laid out here in the guide's brand system:
lavender #CECBF6, deep purple #3C3489, Poppins.

THE TEXT IS A TRANSCRIPTION, and `guide_text.py` says so at the top: the live
doc is the source of truth, and the PDF has to be regenerated if she edits it.

THE TRACKER LINK IS THE MAKE-A-COPY URL, not the edit URL. The sheet is shared
"anyone with the link — viewer", so /copy opens Google's own copy dialog and no
buyer ever reaches the original. That was the last open item on the internal
checklist before selling.

The prompt blocks are set on a tinted panel in a mono face, because a buyer is
going to select and copy them: a prompt that looks like body text invites a
partial selection.
"""
import os

from reportlab.lib.colors import Color, HexColor
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

import guide_text as G

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(HERE, "build", "fonts")
OUT = os.path.join(HERE, "Vendor Payment System — Setup Guide.pdf")

LAVENDER = HexColor("#CECBF6")
PURPLE = HexColor("#3C3489")
HAIRLINE = HexColor("#B0ACE4")
PANEL = Color(206 / 255, 203 / 255, 246 / 255, alpha=0.35)

W, H = LETTER
M = 0.9 * inch
TOP = H - 1.0 * inch
BOT = 1.0 * inch

pdfmetrics.registerFont(TTFont("P400", os.path.join(FONTS, "Poppins-400.ttf")))
pdfmetrics.registerFont(TTFont("P600", os.path.join(FONTS, "Poppins-600.ttf")))
pdfmetrics.registerFont(TTFont("P700", os.path.join(FONTS, "Poppins-700.ttf")))
MONO = "Courier"


class Doc:
    def __init__(self, path):
        self.c = canvas.Canvas(path, pagesize=LETTER)
        self.page = 0
        self.y = 0
        self._new_page(cover=True)

    # ---------------------------------------------------------------- chrome
    def _footer(self):
        if self.page == 1:
            return
        self.c.setStrokeColor(HAIRLINE)
        self.c.setLineWidth(0.7)
        self.c.line(M, BOT - 16, W - M, BOT - 16)
        self.c.setFont("P400", 8)
        self.c.setFillColor(PURPLE)
        self.c.drawString(M, BOT - 30, "The Vendor Payment System")
        self.c.drawRightString(W - M, BOT - 30, "@aiforeventplanners")

    def _new_page(self, cover=False):
        if self.page:
            self._footer()
            self.c.showPage()
        self.page += 1
        if cover:
            self.c.setFillColor(LAVENDER)
            self.c.rect(0, 0, W, H, stroke=0, fill=1)
        self.y = TOP

    def space(self, n):
        if self.y - n < BOT:
            self._new_page()
        else:
            self.y -= n

    def _wrap(self, text, font, size, width):
        words, lines, cur = text.split(), [], ""
        for w in words:
            t = (cur + " " + w).strip()
            if self.c.stringWidth(t, font, size) <= width:
                cur = t
            else:
                lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
        return lines

    def para(self, text, font="P400", size=10.5, lead=15, indent=0, colour=None,
             gap=10):
        width = W - 2 * M - indent
        lines = self._wrap(text, font, size, width)
        self.space(gap)
        for ln in lines:
            if self.y - lead < BOT:
                self._new_page()
            self.c.setFont(font, size)
            self.c.setFillColor(colour or PURPLE)
            self.c.drawString(M + indent, self.y, ln)
            self.y -= lead

    def heading(self, text):
        self.space(20)
        if self.y - 40 < BOT:
            self._new_page()
        self.c.setFont("P700", 17)
        self.c.setFillColor(PURPLE)
        self.c.drawString(M, self.y, text)
        self.y -= 10
        self.c.setStrokeColor(HAIRLINE)
        self.c.setLineWidth(1)
        self.c.line(M, self.y, M + 92, self.y)
        self.y -= 16

    def sub(self, text):
        self.space(12)
        if self.y - 26 < BOT:
            self._new_page()
        self.c.setFont("P600", 12)
        self.c.setFillColor(PURPLE)
        self.c.drawString(M, self.y, text)
        self.y -= 18

    def bullet(self, text):
        width = W - 2 * M - 18
        lines = self._wrap(text, "P400", 10.5, width)
        self.space(6)
        for i, ln in enumerate(lines):
            if self.y - 15 < BOT:
                self._new_page()
            self.c.setFillColor(PURPLE)
            if i == 0:
                self.c.circle(M + 4, self.y + 3.5, 2, stroke=0, fill=1)
            self.c.setFont("P400", 10.5)
            self.c.drawString(M + 18, self.y, ln)
            self.y -= 15

    PAD = 13          # panel padding, the same at the top and the bottom
    LEAD = 12         # mono leading
    GAP = 8           # between paragraphs inside one panel

    def prompt_measure(self, paras):
        """(wrapped blocks, panel height) = padding + lines + inter-paragraph gaps."""
        width = W - 2 * M - 28
        blocks = [self._wrap(p, MONO, 8.6, width) for p in paras]
        body = sum(len(b) * self.LEAD for b in blocks) + (len(blocks) - 1) * self.GAP
        return blocks, self.PAD * 2 + body

    def prompt(self, paras):
        """A copyable block: mono on a tinted panel, never split mid-panel.

        THE CURSOR ENDS BELOW THE PANEL. A first build moved it down only by
        the text it had drawn, leaving the panel's own bottom padding above the
        cursor — so the next prompt's name printed inside the tint. That is
        what the misaligned headings on pages 3 and 4 were, and it also made
        the bottom padding read as 18pt against a 7pt top.

        THE BREAK TEST MEASURES THE PANEL'S OWN TOP, not the cursor. The panel
        starts 6pt ABOVE the cursor (it tucks up under the heading), so testing
        the cursor broke the page 6pt early — and `build`, which keeps a name
        with its panel, measured it the other way. Those 6pt are the whole
        reason "Prompt 4. Change check" sat alone at the foot of page 4 with
        its block overleaf. One number, measured once, in both places.
        """
        blocks, need = self.prompt_measure(paras)
        self.space(6)
        top = self.y + 6
        if top - need < BOT:
            self._new_page()
            top = self.y
        self.c.setFillColor(PANEL)
        self.c.rect(M, top - need, W - 2 * M, need, stroke=0, fill=1)

        y = top - self.PAD - 8.6          # first baseline, one cap below the pad
        for bi, b in enumerate(blocks):
            for ln in b:
                self.c.setFont(MONO, 8.6)
                self.c.setFillColor(PURPLE)
                self.c.drawString(M + 14, y, ln)
                y -= self.LEAD
            if bi != len(blocks) - 1:
                y -= self.GAP
        self.y = top - need - 16

    def link(self, url):
        """A URL set on one line, SHRUNK UNTIL IT FITS THE MEASURE.

        A URL has no spaces, so the wrapper cannot break it and a long one
        simply ran off the right margin — the tracker link overshot by 44pt
        and was the one thing on page 2 that did not line up with everything
        else. It is a link a buyer clicks rather than reads, so sizing it down
        is better than breaking it across two lines mid-path.
        """
        width = W - 2 * M
        size = 10.0
        while size > 6.0 and self.c.stringWidth(url, "P600", size) > width:
            size -= 0.25
        self.space(4)
        if self.y - 16 < BOT:
            self._new_page()
        self.c.setFont("P600", size)
        self.c.setFillColor(PURPLE)
        self.c.drawString(M, self.y, url)
        wdt = self.c.stringWidth(url, "P600", size)
        assert wdt <= width + 0.5, f"link still overflows: {url}"
        self.c.setStrokeColor(PURPLE)
        self.c.setLineWidth(0.6)
        self.c.line(M, self.y - 2, M + wdt, self.y - 2)
        self.c.linkURL(url, (M, self.y - 4, M + wdt, self.y + size + 1), relative=0)
        self.y -= 16

    def save(self):
        self._footer()
        self.c.save()


def wordmark(c, x, y, size=16):
    """EP + a drawn star: Poppins has no glyph at U+2726."""
    c.setFont("P700", size)
    c.setFillColor(PURPLE)
    c.drawString(x, y, "EP")
    ep = c.stringWidth("EP", "P700", size)
    r = size * 0.38
    cx, cy = x + ep + 8 + r, y + size * 0.33
    waist = r * 0.3
    p = c.beginPath()
    pts = [(cx, cy + r), (cx + waist, cy + waist), (cx + r, cy),
           (cx + waist, cy - waist), (cx, cy - r), (cx - waist, cy - waist),
           (cx - r, cy), (cx - waist, cy + waist)]
    p.moveTo(*pts[0])
    for q in pts[1:]:
        p.lineTo(*q)
    p.close()
    c.drawPath(p, stroke=0, fill=1)


def build():
    d = Doc(OUT)
    c = d.c

    # ------------------------------------------------------------------ cover
    wordmark(c, M, H - 1.15 * inch, 18)
    c.setFont("P700", 34)
    c.setFillColor(PURPLE)
    y = H / 2 + 60
    for ln in d._wrap(G.TITLE, "P700", 34, W - 2 * M):
        c.drawString(M, y, ln)
        y -= 42
    y -= 6
    c.setFont("P400", 13)
    for ln in d._wrap(G.SUBTITLE, "P400", 13, W - 2 * M - 40):
        c.drawString(M, y, ln)
        y -= 20
    c.setStrokeColor(PURPLE)
    c.setLineWidth(1.2)
    c.line(M, y - 14, M + 120, y - 14)
    c.setFont("P600", 11)
    c.drawString(M, y - 38, "@aiforeventplanners")
    d._new_page()

    # ------------------------------------------------------------------ body
    d.para(G.INTRO, size=11, lead=16)

    for title, items in G.SECTIONS:
        d.heading(title)
        for kind, text in items:
            if kind == "bullet":
                d.bullet(text)
            elif kind == "sub":
                d.sub(text)
            elif kind == "link":
                d.link(text)
            else:
                d.para(text)

    d.heading("The prompts")
    d.para(G.PROMPTS_INTRO)
    for name, paras in G.PROMPTS:
        # Keep the prompt's name with its panel. A first build left
        # "Prompt 6. Payment summary for a client" alone at the foot of a page
        # with its block overleaf, which reads as a heading for nothing.
        _, need = d.prompt_measure(paras)
        if d.y - (30 + need) < BOT:
            d._new_page()
        d.sub(name)
        started = d.page
        d.prompt(paras)
        # The invariant, asserted rather than eyeballed: a prompt's name and
        # its panel are on the same page. The arithmetic here and the break
        # test inside prompt() have disagreed twice; an assert turns the next
        # disagreement into a failed build instead of a stranded heading.
        assert d.page == started, f"{name} is stranded: panel broke to a new page"

    d.heading("Rules that keep it accurate")
    for r in G.RULES:
        d.bullet(r)

    d.save()
    return OUT


if __name__ == "__main__":
    p = build()
    print(p, os.path.getsize(p), "bytes")
