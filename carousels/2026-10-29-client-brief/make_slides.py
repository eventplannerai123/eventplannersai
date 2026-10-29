"""“What clients never tell you in the brief.” — the Thu 29 Oct carousel.

Second carousel in the real palette, after Oct 28's dry sandwich. Same brand
system, same generator shape; what changed is the content and one layout
addition, the two-column gap/answer block on slide 4.

SLIDE 4 IS BUILT FROM THE REAL DEMO EMAIL, not from an invented one. "Client
Email — Holiday Party" sits in Drive October 29
(1byeHtblzLLQqwIhncbGd8op_FFifYDi7pTzwkW7pJfc), and every line on this slide
answers something actually in it:

  * budget — the email never names one; it asks for "pricing so I can take it
    to my boss", which implies a budget exists and withholds it
  * headcount — "the whole team" plus "some people might bring a plus one"
  * style — "maybe a dinner, or maybe more of a drinks thing, we haven't
    decided", which is the one gap the client states outright
  * the goal — "fun but elegant" is a mood, and the email never says what the
    evening is for

All four missing is what makes it a clean demo: the prompt asks for four
things, and the answer is four for four.

THE BRAND SYSTEM IS THE GUIDE'S, NOT THIS FILE'S INVENTION. Lavender #CECBF6,
deep purple #3C3489, Poppins, EP✦ wordmark, numbered badge, bottom bar. Poppins
is not installed here, so the three weights are committed under build/fonts/ and
the slides rebuild byte-identically. Poppins has no glyph at U+2726, so the star
is a polygon sized off the "EP" it follows.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "slides")
FONTS = os.path.join(HERE, "build", "fonts")

W = 1080
SIZES = {"instagram": 1350, "tiktok": 1920}

LAVENDER = (206, 203, 246)
PURPLE = (60, 52, 137)
HAIRLINE = (176, 172, 228)

P400 = os.path.join(FONTS, "Poppins-400.ttf")
P600 = os.path.join(FONTS, "Poppins-600.ttf")
P700 = os.path.join(FONTS, "Poppins-700.ttf")
F = lambda p, s: ImageFont.truetype(p, s)

M = 72
HANDLE = "@aiforeventplanners"

PROMPT = (
    "Here's a client's first email about their event: [paste]. Check it for "
    "four things: the budget, the number of guests, the style of event "
    "(reception, seated dinner, buffet) and what they most want the event to "
    "achieve. Tell me which ones it doesn't answer, then draft a friendly "
    "reply that asks for the missing ones without sounding like a "
    "questionnaire."
)

# Slide 4: what the email says, and what it leaves out. Quoted fragments are
# verbatim from the demo email so the slide can be checked against it.
GAPS = [
    ("Budget", "“pricing so I can take it to my boss” — never a number"),
    ("Headcount", "“the whole team” and “some people might bring a plus one”"),
    ("Style", "“maybe a dinner, or maybe more of a drinks thing”"),
    ("The goal", "“fun but elegant” is a mood, not what the night is for"),
]

SLIDES = [
    dict(n=1, head="4 things clients\nnever tell you\nin the brief.",
         sub="And the quote you'll get wrong without them."),
    dict(n=2, head="The budget.\nThe headcount.\nThe style.",
         sub="A reception? A seated dinner? And what they actually want out of it."),
    dict(n=3, head="The prompt", body=[PROMPT], body_font=P400, body_px=34),
    dict(n=4, head="Four for four", gaps=GAPS,
         foot="It drafts the reply that asks for all of them, without sounding "
              "like a questionnaire."),
    dict(n=5, head="Get all four\nbefore you quote\nanything.",
         sub="Save this for your next enquiry."),
]


def wrap(d, text, font, maxw):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= maxw:
            cur = t
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def chrome(img, d, H, n):
    """Numbered badge, then the bottom bar: rule, EP✦ wordmark, handle."""
    bf = F(P700, 30)
    r = 32
    cx, cy = M + r, 118
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=PURPLE, width=3)
    t = str(n)
    d.text((cx - d.textlength(t, font=bf) / 2, cy - 30 * 0.78), t, font=bf, fill=PURPLE)

    d.line([(M, H - 150), (W - M, H - 150)], fill=HAIRLINE, width=2)
    wf, hf = F(P700, 34), F(P400, 24)
    ep_w = d.textlength("EP", font=wf)
    star_r = 13
    ex, ey = (W - (ep_w + 10 + star_r * 2)) / 2, H - 112
    d.text((ex, ey), "EP", font=wf, fill=PURPLE)
    sx, sy = ex + ep_w + 10 + star_r, ey + 34 * 0.62
    waist = star_r * 0.30
    d.polygon([(sx, sy - star_r), (sx + waist, sy - waist), (sx + star_r, sy),
               (sx + waist, sy + waist), (sx, sy + star_r), (sx - waist, sy + waist),
               (sx - star_r, sy), (sx - waist, sy - waist)], fill=PURPLE)
    d.text(((W - d.textlength(HANDLE, font=hf)) / 2, H - 64), HANDLE, font=hf, fill=PURPLE)


def measure(d, s, H, head_px):
    """Total block height at this headline size, or None if it will not fit."""
    maxw = W - 2 * M
    hf = F(P700, head_px)
    head_lines = []
    for para in s["head"].split("\n"):
        head_lines += wrap(d, para, hf, maxw)
    h = len(head_lines) * int(head_px * 1.18)

    parts = []
    if s.get("sub"):
        sp = max(26, int(head_px * 0.40))
        sf = F(P400, sp)
        ls = wrap(d, s["sub"], sf, maxw)
        h += 40 + len(ls) * int(sp * 1.38)
        parts.append(("sub", sf, ls, int(sp * 1.38)))
    if s.get("body"):
        bp = s.get("body_px", 34)
        bf = F(s.get("body_font", P400), bp)
        ls = []
        for para in s["body"]:
            ls += wrap(d, para, bf, maxw)
        h += 46 + len(ls) * int(bp * 1.42)
        parts.append(("body", bf, ls, int(bp * 1.42)))
    if s.get("gaps"):
        lp = max(26, int(head_px * 0.56))
        vp = max(22, int(head_px * 0.42))
        lf, vf = F(P600, lp), F(P400, vp)
        groups = [(label, wrap(d, value, vf, maxw - 36)) for label, value in s["gaps"]]
        h += 46 + sum(int(lp * 1.24) + len(g) * int(vp * 1.34) + 24 for _, g in groups)
        parts.append(("gaps", (lf, vf), groups, (int(lp * 1.24), int(vp * 1.34))))
    if s.get("foot"):
        fp = max(24, int(head_px * 0.38))
        ff = F(P400, fp)
        ls = wrap(d, s["foot"], ff, maxw)
        h += 44 + len(ls) * int(fp * 1.38)
        parts.append(("foot", ff, ls, int(fp * 1.38)))
    return h, head_lines, hf, parts


def build(s, H):
    img = Image.new("RGB", (W, H), LAVENDER)
    d = ImageDraw.Draw(img)
    top, bottom = 210, H - 190
    budget = bottom - top

    start = 92 if s.get("gaps") or s.get("body") else 104
    for head_px in range(start, 29, -2):
        total, head_lines, hf, parts = measure(d, s, H, head_px)
        if total <= budget:
            break
    else:
        raise SystemExit(f"slide {s['n']} does not fit at {H}")

    y = top + (budget - total) // 2
    for ln in head_lines:
        d.text((M, y), ln, font=hf, fill=PURPLE)
        y += int(head_px * 1.18)

    for kind, font, payload, step in parts:
        if kind == "gaps":
            lf, vf = font
            lstep, vstep = step
            y += 46
            for label, lines in payload:
                d.text((M, y), label, font=lf, fill=PURPLE)
                y += lstep
                for ln in lines:
                    d.text((M + 36, y), ln, font=vf, fill=PURPLE)
                    y += vstep
                y += 24
        else:
            y += {"sub": 40, "body": 46, "foot": 44}[kind]
            for ln in payload:
                d.text((M, y), ln, font=font, fill=PURPLE)
                y += step

    chrome(img, d, H, s["n"])
    return img, head_px


def main():
    os.makedirs(OUT, exist_ok=True)
    for name, H in SIZES.items():
        for s in SLIDES:
            img, px = build(s, H)
            assert img.size == (W, H)
            p = os.path.join(OUT, f"2026-10-29-client-brief-{name}-{s['n']}.jpg")
            img.save(p, quality=95)
            print(f"{name} slide {s['n']}: headline {px}px -> {os.path.basename(p)}")


if __name__ == "__main__":
    main()
