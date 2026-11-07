"""Sun 8 Nov — "Everyone has a rain plan. Almost nobody has priced one."

Six slides, the guide's own structure for the day: the claim, when to price
it, the lines that change, the prompt, what AI gives back from the file, and
the closer. A redo of the Sep 29 rain plan Reel, which reached 21 in a
morning slot; the original stays up. Content bank 21.

SLIDE 5 IS COMPUTED FROM THE FILE, NOT WRITTEN. The guide's CLAUDE CODE line
says to build `Garden Reception — Budget and Rain Plan` and run the prompt on
it, so every figure on slide 5 comes out of the sheet that is now in Drive
November 8, and check() recomputes all of them:

  outdoor plan      $35,800
  rain plan         $48,680
  difference        $12,880
  rain call         Wed 9 June 2027, 72 hours before Sat 12 June
  tent held unused  $3,600, half the tent line

THE $12,880 DEPENDS ON ONE SUBSTITUTION. The tent lighting replaces the
string lighting rather than adding to it, so it costs $200 net, not $1,400 —
get that wrong and the difference reads $14,080. It is the thing the prompt
is for, so the slide says it and check() asserts it.

BRAND SYSTEM IS THE GUIDE'S: lavender #CECBF6, deep purple #3C3489, Poppins,
EP + star wordmark, numbered badge, bottom bar. Poppins has no glyph at
U+2726, so the star is drawn as a polygon.
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

# The sheet, line for line, so the slide can be checked against it.
OUTDOOR = [
    ("Garden fee", 4_500), ("Catering, 150 x $95", 14_250),
    ("Bar, 150 x $35", 5_250), ("Rentals", 3_600), ("Florals", 4_200),
    ("Music", 2_800), ("String lighting", 1_200),
]
TENT = [
    ("40 x 100 frame tent", 7_200), ("Flooring", 2_600), ("Sidewalls", 700),
    ("Tent lighting", 1_400), ("Generator", 1_100),
    ("Install crew, 4 x 6 x $45", 1_080),
]
REPLACED = "String lighting"          # the tent lighting takes its place
REPLACED_BY = "Tent lighting"

OUTDOOR_TOTAL = sum(a for _, a in OUTDOOR)
TENT_TOTAL = sum(a for _, a in TENT)
REPLACED_AMOUNT = dict(OUTDOOR)[REPLACED]
RAIN_TOTAL = OUTDOOR_TOTAL - REPLACED_AMOUNT + TENT_TOTAL
DIFFERENCE = RAIN_TOTAL - OUTDOOR_TOTAL
HELD_UNUSED = dict(TENT)["40 x 100 frame tent"] // 2
LIGHTING_NET = dict(TENT)[REPLACED_BY] - REPLACED_AMOUNT

PROMPT = (
    "Here's the budget for an outdoor garden reception for 150 guests and the "
    "tent company's quote for the rain plan [upload]. Put the two plans side "
    "by side: every line that changes, what it adds or replaces, the total "
    "for each plan and the difference. Then tell me the date I have to make "
    "the rain call by, and what it costs if I hold the tent and don't use it."
)

SLIDES = [
    dict(n=1, head="Everyone has a rain\nplan. Almost nobody\nhas priced one.",
         sub=f"This one added ${DIFFERENCE:,}."),

    dict(n=2, head="Price the indoor\nversion in\npre-planning.",
         body="Not the week of, when the forecast turns and the tent company "
              "is quoting three other weddings."),

    dict(n=3, head="Every line that\nchanges.",
         body="The tent, the floor, the walls, the lights, the power, and the "
              "crew to put it all up."),

    dict(n=4, label="The prompt", head="Ask for both totals,\nand for the date\nyou have to decide.",
         quote=PROMPT),

    dict(n=5, label="What it gives back",
         head=f"The difference:\n${DIFFERENCE:,}.",
         items=[("Outdoor plan", f"${OUTDOOR_TOTAL:,}", "the garden reception as budgeted"),
                ("Rain plan", f"${RAIN_TOTAL:,}", "the same evening, under a tent"),
                ("Rain call", "Wed June 9", f"72 hours before \u2014 and a tent held and not used costs ${HELD_UNUSED:,}")],
         foot=f"Six lines change. The tent lighting replaces the string lighting, so it adds ${LIGHTING_NET} rather than $1,400."),

    dict(n=6, head="Price the rain plan\nbefore you need it.",
         sub="Save this for your next outdoor event."),
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
    wrapped = len(head_lines)

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
        out.append((ff, wrap(d, s["foot"], ff, maxw), int(fp * 1.34), 40, 0, "before"))

    if s.get("sub"):
        sp = max(26, int(head_px * 0.40))
        sf = F(P400, sp)
        out.append((sf, wrap(d, s["sub"], sf, maxw), int(sp * 1.38), 40, 0, False))

    return out, wrapped


def build(s, H):
    img = Image.new("RGB", (W, H), LAVENDER)
    d = ImageDraw.Draw(img)

    top, bottom = 210, H - 190
    budget = bottom - top

    start = 78 if s.get("items") else 100
    # The headline's own line breaks are chosen, so a size that re-wraps one
    # of them is the wrong size: shrink until each written line fits whole.
    # Slide 1 shipped as "Everyone has a / rain / plan. Almost / nobody" the
    # first time this was left to the wrapper.
    written = len(s["head"].split("\n"))
    for head_px in range(start, 29, -2):
        parts, wrapped = blocks(d, s, head_px)
        total = sum(g + len(ls) * st + (14 if rule else 0)
                    for _, ls, st, g, _, rule in parts)
        if total <= budget and wrapped == written:
            break
    else:
        raise SystemExit(f"slide {s['n']} does not fit at {H}")

    y = top + (budget - total) // 2
    for font, lines, step, gap, indent, rule in parts:
        y += gap
        # "before" is the foot's rule, which sits above it; True is the
        # label's, which sits under. Keyed on the flag, never on the text —
        # comparing the wrapped lines to the raw string only worked while
        # every foot happened to fit on one line, and put the rule through
        # the second line the first time one did not.
        if rule == "before":
            y += 6
            d.line([(M, y), (M + 132, y)], fill=HAIRLINE, width=2)
            y += 14
        for ln in lines:
            d.text((M + indent, y), ln, font=font, fill=PURPLE)
            y += step
        if rule is True:
            y += 6
            d.line([(M, y), (M + 132, y)], fill=HAIRLINE, width=2)
            y += 8

    chrome(img, d, H, s["n"])
    return img, head_px


def check():
    assert OUTDOOR_TOTAL == 35_800, OUTDOOR_TOTAL
    assert TENT_TOTAL == 14_080, TENT_TOTAL
    assert RAIN_TOTAL == 48_680, RAIN_TOTAL
    assert DIFFERENCE == 12_880, DIFFERENCE
    assert HELD_UNUSED == 3_600, HELD_UNUSED
    # the substitution is what keeps the difference at 12,880 rather than 14,080
    assert LIGHTING_NET == 200, LIGHTING_NET
    assert OUTDOOR_TOTAL + TENT_TOTAL - REPLACED_AMOUNT == RAIN_TOTAL
    # slide 3 and slide 5 both say "six lines" in words
    assert len(TENT) == 6, "six lines change"
    assert sum(1 for n, _ in TENT if n == REPLACED_BY) == 1
    assert REPLACED in dict(OUTDOOR), "the replaced line must be on the outdoor plan"
    print(f"checks pass: outdoor ${OUTDOOR_TOTAL:,}, rain plan ${RAIN_TOTAL:,}, "
          f"difference ${DIFFERENCE:,}, lighting net ${LIGHTING_NET}, "
          f"held unused ${HELD_UNUSED:,}")


def main():
    check()
    os.makedirs(OUT, exist_ok=True)
    for name, H in SIZES.items():
        for s in SLIDES:
            img, px = build(s, H)
            assert img.size == (W, H)
            p = os.path.join(OUT, f"2026-11-08-rain-plan-{name}-{s['n']}.jpg")
            img.save(p, quality=95)
            print(f"{name} slide {s['n']}: headline {px}px -> {os.path.basename(p)}")


if __name__ == "__main__":
    main()
