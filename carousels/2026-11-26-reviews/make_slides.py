"""The coloring book's first three reviews — five slides, brand look.

Built from the three reviews Sahiba sent on Fri 20 Nov, after the Fri 20
block's YOU line asked her to check the listing. **amazon.com is blocked from
this session**, so these are her paste, and every word of them here is hers
and the reviewers' — nothing is paraphrased, trimmed or tidied. `check()`
asserts each quote against the text she sent.

**NAMES ARE FIRST NAME AND LAST INITIAL**, which is the guide's own rule for
this piece, so "Pamela Monahan" becomes "Pamela M." The assert below refuses
any surname.

WHY THREE AND NOT TWO: the brief says two reviews a few days after asking
reads as solicited, which would make the piece worse than not posting it. All
three here are verified purchases from Oct 3, Oct 4 and Oct 22 — well before
the ask — and all three are five stars.

**POPPINS HAS NO GLYPH AT U+2605**, the same trap as the EP wordmark's star
at U+2726: a literal "★★★★★" renders five tofu boxes. The stars are drawn as
polygons, five-pointed, inner radius 0.382 of the outer.

Brand system: lavender #CECBF6, deep purple #3C3489, Poppins, EP + star
wordmark, numbered badge, bottom bar. One set at 1080x1920 — Instagram and
Facebook take the slide Reel, TikTok takes the same slides as a photo
carousel.

**THE CLOSING SLIDE TIES TO THE GIVEAWAY, SO THE PIECE HAS A DEADLINE.** It
says two copies are up for grabs until Friday, which is true only while the
Nov 20 giveaway is open — it closes Fri 27 Nov at 11:59pm Eastern. The Nov 14
rule is to check the closing line against the piece: this one fits, because
the piece is about the book and the giveaway is for the book. But it means
the Reel has to post Mon 23 to Thu 26, and `check()` is not what enforces
that — the date proposal at the Sun 22 recap is.
"""
import os
import math
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "slides")
FONTS = os.path.join(HERE, "build", "fonts")
STEM = "2026-11-26-reviews"

W, H = 1080, 1920

LAVENDER = (206, 203, 246)
PURPLE = (60, 52, 137)
HAIRLINE = (176, 172, 228)

P400 = os.path.join(FONTS, "Poppins-400.ttf")
P600 = os.path.join(FONTS, "Poppins-600.ttf")
P700 = os.path.join(FONTS, "Poppins-700.ttf")
F = lambda p, s: ImageFont.truetype(p, s)

M = 72
HANDLE = "@aiforeventplanners"

# Her paste, verbatim. Titles and bodies are both the reviewer's words.
REVIEWS = [
    ("Pamela M.", "So cute!",
     "The coloring book is super cute! Love it!!"),
    ("Christina N.", "So cute! 100%\nwould recommend.",
     "I got this for a friend and am very happy that I did. Excellent quality "
     "in terms of paper stock and a rich variety of pictures to color in. My "
     "favorites are the slices of cake."),
    ("Rose R.", "Perfect gift",
     "Such a cute gift for a friend about to plan their big day!"),
]

SLIDES = [
    dict(n=1, label="THE CALM BEFORE THE AISLE",
         head="Three strangers\nreviewed my\ncoloring book.",
         sub="All five stars. Verified purchases. Here is what they wrote."),
    dict(n=2, stars="Pamela M.", head=REVIEWS[0][1], quote=REVIEWS[0][2]),
    dict(n=3, stars="Christina N.", head=REVIEWS[1][1], quote=REVIEWS[1][2]),
    dict(n=4, stars="Rose M.", head=REVIEWS[2][1], quote=REVIEWS[2][2]),
    dict(n=5, head="Two copies are up\nfor grabs until Friday.",
         sub="Comment the bride, bridesmaid or planner you’d give it to."),
]
SLIDES[3]["stars"] = "Rose R."


def star(d, cx, cy, r, fill):
    pts = []
    for i in range(10):
        rad = r if i % 2 == 0 else r * 0.382
        a = math.radians(-90 + i * 36)
        pts.append((cx + rad * math.cos(a), cy + rad * math.sin(a)))
    d.polygon(pts, fill=fill)


def star_row(d, x, y, r, n=5, gap=8):
    for i in range(n):
        star(d, x + r + i * (2 * r + gap), y + r, r, PURPLE)
    return n * (2 * r + gap) - gap


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


def chrome(img, d, n):
    bf = F(P700, 30)
    r = 32
    cx, cy = M + r, 118
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=PURPLE, width=3)
    t = str(n)
    d.text((cx - d.textlength(t, font=bf) / 2, cy - 30 * 0.78), t, font=bf, fill=PURPLE)

    d.line([(M, H - 150), (W - M, H - 150)], fill=HAIRLINE, width=2)
    wf, hf = F(P700, 34), F(P400, 24)
    ep_w = d.textlength("EP", font=wf)
    sr = 13
    ex, ey = (W - (ep_w + 10 + sr * 2)) / 2, H - 112
    d.text((ex, ey), "EP", font=wf, fill=PURPLE)
    star(d, ex + ep_w + 10 + sr, ey + 34 * 0.62, sr, PURPLE)
    d.text(((W - d.textlength(HANDLE, font=hf)) / 2, H - 64), HANDLE, font=hf, fill=PURPLE)


def blocks(d, s, head_px):
    """Every block in render order: (font, lines, step, gap, indent, rule)."""
    maxw = W - 2 * M
    out = []

    if s.get("label"):
        lp = max(24, int(head_px * 0.30))
        out.append((F(P600, lp), [s["label"]], int(lp * 1.30), 0, 0, True))

    if s.get("stars"):
        sp = max(26, int(head_px * 0.34))
        out.append(("STARS", [s["stars"]], int(sp * 1.50), 0, 0, False))

    hf = F(P700, head_px)
    head_lines = []
    for para in s["head"].split("\n"):
        head_lines += wrap(d, para, hf, maxw)
    out.append((hf, head_lines, int(head_px * 1.18),
                30 if (s.get("label") or s.get("stars")) else 0, 0, False))
    wrapped = len(head_lines)

    if s.get("quote"):
        qp = max(25, int(head_px * 0.42))
        qf = F(P400, qp)
        out.append((qf, wrap(d, "“" + s["quote"] + "”", qf, maxw - 34),
                    int(qp * 1.42), 38, 34, False))

    if s.get("sub"):
        sp = max(26, int(head_px * 0.40))
        sf = F(P400, sp)
        out.append((sf, wrap(d, s["sub"], sf, maxw), int(sp * 1.38), 40, 0, False))

    return out, wrapped


def build(s):
    img = Image.new("RGB", (W, H), LAVENDER)
    d = ImageDraw.Draw(img)
    top, bottom = 210, H - 190
    budget = bottom - top

    written = len(s["head"].split("\n"))
    for head_px in range(100, 29, -2):
        parts, wrapped = blocks(d, s, head_px)
        total = sum(g + len(ls) * st + (14 if rule else 0)
                    for _, ls, st, g, _, rule in parts)
        if total <= budget and wrapped == written:
            break
    else:
        raise SystemExit(f"slide {s['n']} does not fit")

    y = top + (budget - total) // 2
    for font, lines, step, gap, indent, rule in parts:
        y += gap
        if font == "STARS":
            r = int(step / 1.50 * 0.40)
            w = star_row(d, M, y + 4, r)
            nf = F(P600, int(step / 1.50))
            d.text((M + w + 22, y), lines[0], font=nf, fill=PURPLE)
            y += step
            continue
        for ln in lines:
            d.text((M + indent, y), ln, font=font, fill=PURPLE)
            y += step
        if rule is True:
            y += 6
            d.line([(M, y), (M + 132, y)], fill=HAIRLINE, width=2)
            y += 8

    chrome(img, d, s["n"])
    return img, head_px


def check():
    # Every quote is the reviewer's own text, word for word. If a slide's
    # quote ever drifts from her paste, this fails rather than publishing a
    # paraphrase of a stranger's words.
    sent = {
        "Pamela M.": "The coloring book is super cute! Love it!!",
        "Christina N.": ("I got this for a friend and am very happy that I did. "
                         "Excellent quality in terms of paper stock and a rich "
                         "variety of pictures to color in. My favorites are the "
                         "slices of cake."),
        "Rose R.": "Such a cute gift for a friend about to plan their big day!",
    }
    seen = {}
    for s in SLIDES:
        if s.get("stars"):
            seen[s["stars"]] = s["quote"]
    assert seen == sent, f"a quote drifted from her paste: {seen}"

    # First name and last initial at most. A surname on a public slide is not
    # ours to publish.
    for name in seen:
        first, _, last = name.partition(" ")
        assert len(last) == 2 and last.endswith("."), f"{name!r} is not 'First X.'"

    # No tracker CTA on a coloring-book piece. Her Nov 14 rule.
    text = " ".join(s.get("head", "") + s.get("sub", "") + s.get("quote", "")
                    for s in SLIDES)
    assert "BUDGET" not in text, "a slide carries a BUDGET line"

    assert len([s for s in SLIDES if s.get("stars")]) == 3, "three reviews, no more"
    print(f"checks pass: {len(SLIDES)} slides, {len(seen)} reviews, all verbatim")


def main():
    check()
    os.makedirs(OUT, exist_ok=True)
    for s in SLIDES:
        img, px = build(s)
        for platform in ("instagram", "tiktok"):
            p = os.path.join(OUT, f"{STEM}-{platform}-{s['n']}.jpg")
            img.save(p, quality=93)
        print(f"slide {s['n']}  head {px}px")


if __name__ == "__main__":
    main()
