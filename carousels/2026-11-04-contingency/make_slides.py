"""“If the budget is $100,000, $5,000 should have no name on it.” — Wed 4 Nov.

Six slides, the guide's own structure for this day: the claim, why budgets
actually go over, what a contingency line is, the prompt, what AI gives back
from the demo budget, and the closer.

SLIDE 5 IS COMPUTED, NOT WRITTEN. The guide's CLAUDE CODE line says to run the
prompt on `Event Budget — Spring Conference` and put the result on slide 5, so
the figures here come from the file rather than from a plausible-sounding
sentence: 5% of $100,000 is $5,000, and the rebalance below takes exactly
$5,000 out of six lines with slack so the total is still $100,000. ASSERTS at
the bottom of this file check both, because a carousel whose arithmetic does
not hold ruins the point it is making.

The three lines flagged as most likely to run over are the three the file
itself makes vulnerable, with the reason each one moves:

  Plated lunch      $14,800  priced per head, and the guarantee is due before
                             the real number is known
  AV and production $11,200  on-site additions and overtime past strike
  Reception bar      $4,200  billed on consumption, not a flat rate

THE BRAND SYSTEM IS THE GUIDE'S: lavender #CECBF6, deep purple #3C3489,
Poppins, EP✦ wordmark, numbered badge, bottom bar. Poppins is not installed
here, so the three weights are committed under build/fonts/. Poppins has no
glyph at U+2726, so the star is drawn as a polygon.

No motif band on this one — that was the Halloween build's device, not the
house style.
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

TOTAL = 100_000
PCT = 0.05
CONTINGENCY = int(TOTAL * PCT)

# The demo file, line for line, so the rebalance can be checked against it.
BUDGET = [
    ("Venue", 18_000), ("Breakfast and two breaks", 12_400),
    ("Plated lunch", 14_800), ("Evening reception — food", 6_900),
    ("Evening reception — bar", 4_200), ("AV and production", 11_200),
    ("Staging and rigging", 3_600), ("Speaker fees", 9_500),
    ("Speaker travel and hotel", 4_300), ("Registration platform", 2_150),
    ("Badges, signage and print", 3_450), ("Décor and florals", 2_800),
    ("On-site event team", 5_200), ("Shipping and storage", 1_500),
]
# Where the $5,000 comes from: lines with slack, none of them the three flagged.
TRIMS = [
    ("Venue", 1_200), ("Speaker fees", 1_200), ("On-site event team", 1_000),
    ("Décor and florals", 800), ("Badges, signage and print", 500),
    ("Speaker travel and hotel", 300),
]

PROMPT = (
    "Here's my event budget: [upload]. Add a contingency line at 5% of the "
    "total, show me the three lines most likely to run over and why, and "
    "rebalance the rest so the total doesn't change."
)

SLIDES = [
    dict(n=1, head="If the budget is\n$100,000, $5,000\nshould have no\nname on it."),

    dict(n=2, head="Budgets don't go\nover because of\none big thing.",
         body="They go over because of six small ones nobody planned for."),

    dict(n=3, head="Five percent.",
         body="One line called contingency. Nobody spends it without saying why."),

    dict(n=4, label="The prompt", head="Ask for the line,\nand for the three\nthat will move.",
         quote=PROMPT),

    dict(n=5, label="What it gives back",
         head="Contingency:\n$5,000.",
         items=[("Plated lunch", "$14,800", "priced per head, guaranteed before the real number is in"),
                ("AV and production", "$11,200", "on-site additions and overtime past strike"),
                ("Evening reception — bar", "$4,200", "billed on consumption, not a flat rate")],
         foot="Rebalanced out of six lines with slack. Total still $100,000."),

    dict(n=6, head="Name it contingency.\nThen don't touch it.",
         sub="Save this for your next budget."),
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


def blocks(d, s, head_px):
    """Every text block in render order: (font, lines, step, gap, indent, rule)."""
    maxw = W - 2 * M
    out = []

    if s.get("label"):
        lp = max(24, int(head_px * 0.32))
        lf = F(P600, lp)
        out.append((lf, [s["label"]], int(lp * 1.30), 0, 0, True))

    hf = F(P700, head_px)
    head_lines = []
    for para in s["head"].split("\n"):
        head_lines += wrap(d, para, hf, maxw)
    out.append((hf, head_lines, int(head_px * 1.18), 30 if s.get("label") else 0,
                0, False))

    if s.get("body"):
        bp = max(26, int(head_px * 0.44))
        bf = F(P400, bp)
        out.append((bf, wrap(d, s["body"], bf, maxw), int(bp * 1.38), 36, 0, False))

    if s.get("quote"):
        qp = max(25, int(head_px * 0.40))
        qf = F(P400, qp)
        out.append((qf, wrap(d, "“" + s["quote"] + "”", qf, maxw - 34),
                    int(qp * 1.42), 38, 34, False))

    if s.get("items"):
        np_ = max(25, int(head_px * 0.38))
        nf, af = F(P600, np_), F(P400, max(22, int(np_ * 0.86)))
        for i, (name, amount, why) in enumerate(s["items"]):
            out.append((nf, [f"{name}  {amount}"], int(np_ * 1.26),
                        36 if i == 0 else 22, 0, False))
            out.append((af, wrap(d, why, af, maxw - 34),
                        int(max(22, int(np_ * 0.86)) * 1.34), 4, 34, False))

    if s.get("foot"):
        fp = max(23, int(head_px * 0.32))
        ff = F(P400, fp)
        out.append((ff, wrap(d, s["foot"], ff, maxw), int(fp * 1.34), 40, 0, True))

    if s.get("sub"):
        sp = max(26, int(head_px * 0.40))
        sf = F(P400, sp)
        out.append((sf, wrap(d, s["sub"], sf, maxw), int(sp * 1.38), 40, 0, False))

    return out


def build(s, H):
    img = Image.new("RGB", (W, H), LAVENDER)
    d = ImageDraw.Draw(img)

    top, bottom = 210, H - 190
    budget = bottom - top

    start = 78 if s.get("items") else 100
    for head_px in range(start, 29, -2):
        parts = blocks(d, s, head_px)
        total = sum(g + len(ls) * st + (14 if rule else 0)
                    for _, ls, st, g, _, rule in parts)
        if total <= budget:
            break
    else:
        raise SystemExit(f"slide {s['n']} does not fit at {H}")

    y = top + (budget - total) // 2
    for font, lines, step, gap, indent, rule in parts:
        y += gap
        if rule and lines == [s.get("foot")]:
            y += 6
            d.line([(M, y), (M + 132, y)], fill=HAIRLINE, width=2)
            y += 14
        for ln in lines:
            d.text((M + indent, y), ln, font=font, fill=PURPLE)
            y += step
        if rule and lines != [s.get("foot")]:
            y += 6
            d.line([(M, y), (M + 132, y)], fill=HAIRLINE, width=2)
            y += 8

    chrome(img, d, H, s["n"])
    return img, head_px


def check():
    assert sum(a for _, a in BUDGET) == TOTAL, "the demo budget does not total 100,000"
    assert sum(a for _, a in TRIMS) == CONTINGENCY, "the trims do not fund the contingency"
    # slide 5 says "six lines with slack" in words, so the list has to be six
    assert len(TRIMS) == 6, "slide 5 claims six trimmed lines"
    names = {n for n, _ in BUDGET}
    flagged = {i[0] for i in SLIDES[4]["items"]}
    for n, _ in TRIMS:
        assert n in names, f"{n} is not a line in the demo budget"
        assert n not in flagged, f"{n} is both trimmed and flagged as at risk"
    after = {n: a for n, a in BUDGET}
    for n, cut in TRIMS:
        after[n] -= cut
    assert sum(after.values()) + CONTINGENCY == TOTAL, "the rebalanced total moved"
    print(f"checks pass: contingency ${CONTINGENCY:,}, "
          f"trims ${sum(a for _, a in TRIMS):,}, total still ${TOTAL:,}")


def main():
    check()
    os.makedirs(OUT, exist_ok=True)
    for name, H in SIZES.items():
        for s in SLIDES:
            img, px = build(s, H)
            assert img.size == (W, H)
            p = os.path.join(OUT, f"2026-11-04-contingency-{name}-{s['n']}.jpg")
            img.save(p, quality=95)
            print(f"{name} slide {s['n']}: headline {px}px -> {os.path.basename(p)}")


if __name__ == "__main__":
    main()
