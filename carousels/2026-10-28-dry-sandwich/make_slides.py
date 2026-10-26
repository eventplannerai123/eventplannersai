"""“Every conference has the dry sandwich lunch.” — the Wed 28 Oct carousel.

THE FIRST CAROUSEL IN THE REAL PALETTE. Every carousel before this one — Oct 18
runny eggs, Oct 21 wrong entrance, Oct 22 setup times, Oct 25 prompt responsibly
— went out cream #F5F1E8 and maroon #7A2A36 in DejaVu Serif, because each
generator copied the one before it. The guide's Carousel image production
standard said lavender and deep purple the whole time, and she caught it on
2026-10-25: "i thought we went back to purple". Her call was to leave those four
up and switch from here, so the grid carries a deliberate seam.

The standard, verbatim: 1080x1350 built natively in code, lavender background
#CECBF6, deep purple text #3C3489, Poppins (Bold for headlines, Medium/Light for
body), EP✦ wordmark, numbered badge, bottom bar with handle and logo. Never
another colour scheme.

POPPINS IS NOT INSTALLED HERE, so the three weights are committed under
build/fonts/ and the slides rebuild byte-identically. SIL Open Font License.

AND POPPINS HAS NO GLYPH AT U+2726 — a literal "EP✦" renders a tofu box. The
star is drawn as a polygon, sized off the "EP" it follows.

SLIDE 1 IS TEXT ONLY, ON PURPOSE. The brief offers her own photo
(conference-dry-sandwiches.jpg) if it is in Drive October 28. Checked
2026-10-26: the folder holds only the demo menu, so the text slide is the
specified fallback rather than a shortcut.

SLIDE 4 IS THE ANSWER TO THE REAL DEMO FILE. "Caterer Menu — Boxed Lunch" in
that same folder reads "Assorted gourmet sandwiches on artisan bread ...
Vegetarian and gluten-free options available upon request ... Boxes delivered
and set at 11:30am" for a 12:15 service. Every line on slide 4 answers
something actually in it — which is why the veg and GF line is about replacing
"upon request" with counts rather than inventing numbers the menu never gave.
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
    "I'm ordering a boxed sandwich lunch for 250 conference attendees, served "
    "12:15 to 1pm after a full morning of sessions. Here's the caterer's menu "
    "description: [paste]. Rewrite it as a spec the kitchen can't misread: "
    "filling to the edges, assembled as close to service as possible, a spread "
    "or slaw on every sandwich, vegetarian and gluten-free counts, and a backup "
    "hot option if the sandwiches arrive dry. Then write the two-line note I "
    "send the catering manager."
)

SLIDES = [
    dict(n=1, head="Made at 9am.\nServed at 12:30.",
         sub="Every conference has the dry sandwich lunch."),
    dict(n=2, head="Filling that stops\nan inch from the edge.",
         sub="Nobody complains to the planner. They just remember the food was bad."),
    dict(n=3, head="The prompt", body=[PROMPT], body_font=P400, body_px=34),
    dict(n=4, head="What the spec says instead", bullets=[
        "Filling to the edge of the bread. No bare margin.",
        "Assembled as close to service as the kitchen can manage — not at 9am.",
        "A spread or slaw on every build, so nothing arrives dry.",
        "Vegetarian and gluten-free as counts, not “upon request”.",
        "A hot backup held in reserve if the boxes come in dry.",
    ]),
    dict(n=5, head="Don't order\n“sandwiches.”\nOrder a spec.",
         sub="Save this for your next catering order."),
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
    if s.get("bullets"):
        bp = max(26, int(head_px * 0.52))
        bf = F(P400, bp)
        groups = [wrap(d, b, bf, maxw - 44) for b in s["bullets"]]
        h += 46 + sum(len(g) * int(bp * 1.34) + 26 for g in groups)
        parts.append(("bullets", bf, groups, int(bp * 1.34)))
    return h, head_lines, hf, parts


def build(s, H):
    img = Image.new("RGB", (W, H), LAVENDER)
    d = ImageDraw.Draw(img)
    top, bottom = 210, H - 190
    budget = bottom - top

    start = 92 if s.get("bullets") or s.get("body") else 104
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
        if kind == "bullets":
            y += 46
            for g in payload:
                for i, ln in enumerate(g):
                    if i == 0:
                        d.ellipse([M + 4, y + step * 0.38, M + 16, y + step * 0.38 + 12],
                                  fill=PURPLE)
                    d.text((M + 44, y), ln, font=font, fill=PURPLE)
                    y += step
                y += 26
        else:
            y += 40 if kind == "sub" else 46
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
            p = os.path.join(OUT, f"2026-10-28-dry-sandwich-{name}-{s['n']}.jpg")
            img.save(p, quality=95)
            print(f"{name} slide {s['n']}: headline {px}px -> {os.path.basename(p)}")


if __name__ == "__main__":
    main()
