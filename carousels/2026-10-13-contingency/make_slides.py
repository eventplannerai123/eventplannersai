"""Contingency carousel — 6 slides, two sizes.

TikTok photo mode takes 1080x1920; the Wed 14 Instagram post takes 1080x1350.
Same content, same house palette as the Mon 5 hidden-fees carousel, laid out
by vertical centring so one pass produces both without hand-tuned y values.

Slide 5 embeds a crop of Sahiba's own screen recording — the proof that
ChatGPT produced these numbers. Its "Contingency shortfall" row is cropped
off on purpose: the app wrapped "$3,000" as "$3,00 / 0" across two lines, and
that is the single most important number in the piece, so it is restated in
house type underneath instead. Everything above it is untouched.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "slides")
FRAMES = os.path.join(HERE, "build", "frames")

W = 1080
SIZES = {"tiktok": 1920, "instagram": 1350}

CREAM = (245, 241, 232)
INK = (34, 29, 26)
GREY = (138, 126, 118)
MAROON = (122, 42, 54)
BROWN = (58, 50, 48)
ONDARK = (247, 243, 234)
PINKTXT = (214, 180, 190)
RULE = (220, 212, 200)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
SANSB = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
F = lambda p, s: ImageFont.truetype(p, s)

M = 86
LABEL_H = 146   # tracked label + rule + gap beneath it

# The demo budget, read from her spreadsheet. The eleven line items sum to the
# stated total; assert_budget() checks that rather than trusting this list.
BUDGET = [
    ("Venue rental", 18500),
    ("Catering (food & beverage)", 34000),
    ("AV & production", 14200),
    ("Décor & florals", 7800),
    ("Entertainment", 6500),
    ("Staffing", 5400),
    ("Printing & signage", 2100),
    ("Transportation", 4300),
    ("Photography", 3200),
    ("Guest gifts", 2000),
    ("Miscellaneous / contingency", 2000),
]
TOTAL = 100000
PCT = 5

PROMPT = ("Read this draft budget for a 250-guest client dinner. Is there a "
          "contingency line? Calculate 5% of the total, flag it if the line is "
          "missing or under, and tell me how much I'm short.")


def money(n):
    return "${:,}".format(n)


def assert_budget():
    s = sum(a for _, a in BUDGET)
    assert s == TOTAL, f"budget lines sum to {s}, not {TOTAL}"
    need = TOTAL * PCT // 100
    have = dict(BUDGET)["Miscellaneous / contingency"]
    assert need == 5000 and have == 2000 and need - have == 3000, "maths moved"
    assert have * 100 / TOTAL == 2.0, "contingency is not 2%"
    return need, have, need - have


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


def measure(d, text, font, maxw, lh=1.26):
    return len(wrap(d, text, font, maxw)) * int(font.size * lh)


def block(d, text, font, x, y, maxw, fill, lh=1.26, align="left"):
    for ln in wrap(d, text, font, maxw):
        w = d.textlength(ln, font=font)
        xx = x if align == "left" else x + (maxw - w) / 2
        d.text((xx, y), ln, font=font, fill=fill)
        y += int(font.size * lh)
    return y


def tracked(d, text, font, cx, y, fill, track=7):
    total = sum(d.textlength(c, font=font) + track for c in text) - track
    x = cx - total / 2
    for c in text:
        d.text((x, y), c, font=font, fill=fill)
        x += d.textlength(c, font=font) + track
    return y + int(font.size * 1.4)


def head_label(d, text, y):
    """Draw the tracked label and its rule; return y for the body beneath."""
    yy = tracked(d, text, F(SANSB, 26), W / 2, y, GREY)
    d.line([(M, yy + 20), (W - M, yy + 20)], fill=RULE, width=2)
    return y + LABEL_H


def footer(d, H, dark=False):
    f = F(SANS, 26)
    t = "@aiforeventplanners"
    d.text(((W - d.textlength(t, font=f)) / 2, H - 70), t, font=f,
           fill=(GREY if not dark else (120, 108, 104)))


def new(H, bg=CREAM):
    img = Image.new("RGB", (W, H), bg)
    return img, ImageDraw.Draw(img)


# ---------------------------------------------------------------- slides

def slide1(H):
    img, d = new(H, BROWN)
    f = F(SERIF, 72)
    sub = F(SANS, 38)
    lines = ["If the budget is", "$100,000, $5,000 of it", "should have no", "name on it."]
    SUB = "Every draft budget I see is short on exactly one line."
    bh = len(lines) * int(72 * 1.30) + 54 + measure(d, SUB, sub, W - 2 * M)
    y = (H - bh) // 2 - 40
    for ln in lines:
        d.text(((W - d.textlength(ln, font=f)) / 2, y), ln, font=f, fill=ONDARK)
        y += int(72 * 1.30)
    y += 54
    block(d, SUB, sub, M, y, W - 2 * M, PINKTXT, align="center")
    fk = F(SANSB, 32)
    t = "keep swiping  >"
    d.text(((W - d.textlength(t, font=fk)) / 2, H - 230), t, font=fk, fill=PINKTXT)
    footer(d, H, dark=True)
    return img


def slide2(H):
    img, d = new(H)
    lab = F(SANSB, 26)
    f = F(SERIF, 60)
    body = F(SANS, 38)
    head = "The most common reason a budget goes over:"
    big = "Nobody budgeted for contingency in the first place."
    note = ("Not one big overspend. The line that was never there, so every "
            "surprise comes out of a line that was meant for something else.")
    hh = LABEL_H + measure(d, head, body, W - 2 * M) + 30 \
        + measure(d, big, f, W - 2 * M, 1.24) + 44 + measure(d, note, body, W - 2 * M)
    y = head_label(d, "WHY IT GOES OVER", (H - hh) // 2)
    y = block(d, head, body, M, y, W - 2 * M, GREY)
    y += 30
    y = block(d, big, f, M, y, W - 2 * M, INK, lh=1.24)
    y += 44
    block(d, note, body, M, y, W - 2 * M, GREY)
    footer(d, H)
    return img


def slide3(H):
    img, d = new(H)
    lab = F(SANSB, 26)
    f = F(SANS, 40)
    ph = measure(d, PROMPT, f, W - 2 * M - 46, 1.38)
    y = head_label(d, "THE PROMPT", (H - (LABEL_H + ph)) // 2)
    d.line([(M, y - 6), (M, y + ph + 6)], fill=MAROON, width=5)
    block(d, PROMPT, f, M + 46, y, W - 2 * M - 46, INK, lh=1.38)
    footer(d, H)
    return img


def slide4(H):
    need, have, short = assert_budget()
    img, d = new(H)
    lab = F(SANSB, 26)
    fr = F(SANS, 33)
    frb = F(SANSB, 33)
    row = 56
    cap0 = F(SANS, 32)
    hh = LABEL_H + len(BUDGET) * row + 34 + row + 24 \
        + measure(d, "Contingency: x", cap0, W - 2 * M)
    y = head_label(d, "THE DRAFT BUDGET", (H - hh) // 2)
    for name, amt in BUDGET:
        hot = name.startswith("Miscellaneous")
        if hot:
            d.rounded_rectangle([M - 18, y - 12, W - M + 18, y + row - 16], 10,
                                fill=(238, 226, 228))
        f1 = frb if hot else fr
        d.text((M, y), name, font=f1, fill=MAROON if hot else INK)
        t = money(amt)
        d.text((W - M - d.textlength(t, font=f1), y), t, font=f1,
               fill=MAROON if hot else INK)
        y += row
    y += 14
    d.line([(M, y), (W - M, y)], fill=INK, width=3)
    y += 20
    d.text((M, y), "Total", font=frb, fill=INK)
    t = money(TOTAL)
    d.text((W - M - d.textlength(t, font=frb), y), t, font=frb, fill=INK)
    y += row + 24
    cap = F(SANS, 32)
    block(d, f"Contingency: {money(have)} on {money(TOTAL)}. That is 2%.",
          cap, M, y, W - 2 * M, GREY, align="center")
    footer(d, H)
    return img


def slide5(H):
    need, have, short = assert_budget()
    img, d = new(H)
    lab = F(SANSB, 26)

    card = Image.open(os.path.join(FRAMES, "answer-card.png")).convert("RGB")
    # Keep the heading and the four rows that render cleanly; the shortfall
    # row below this is where the app broke "$3,000" over two lines.
    card = card.crop((0, 0, card.width, 790))
    cw = W - 2 * M
    card = card.resize((cw, round(card.height * cw / card.width)), Image.LANCZOS)

    f = F(SERIF, 64)
    sub = F(SANS, 34)
    line = f"{money(short)} short."
    hh = LABEL_H + card.height + 56 + int(64 * 1.24) + 16 \
        + measure(d, "of the 5% it should have carried", sub, cw)
    y = head_label(d, "WHAT AI CAME BACK WITH", (H - hh) // 2)

    img.paste(card, (M, y))
    d.rectangle([M, y, M + cw - 1, y + card.height - 1], outline=RULE, width=2)
    y += card.height + 56
    d.text(((W - d.textlength(line, font=f)) / 2, y), line, font=f, fill=MAROON)
    y += int(64 * 1.24) + 16
    block(d, "of the 5% it should have carried", sub, M, y, cw, GREY, align="center")
    footer(d, H)
    return img


def slide6(H):
    img, d = new(H, BROWN)
    f = F(SERIF, 58)
    fr = F(SANS, 40)
    frb = F(SANSB, 40)
    rows = [("$50,000", "$2,500"), ("$100,000", "$5,000"), ("$250,000", "$12,500")]
    for b, c in rows:
        assert int(b[1:].replace(",", "")) * PCT // 100 == int(c[1:].replace(",", ""))
    head = "My rule: at least 5% in a no-name line from day one."
    row = 72
    hh = measure(d, head, f, W - 2 * M, 1.26) + 70 + len(rows) * row
    y = (H - hh) // 2 - 20
    y = block(d, head, f, M, y, W - 2 * M, ONDARK, lh=1.26)
    y += 70
    for b, c in rows:
        d.text((M + 40, y), b, font=fr, fill=PINKTXT)
        arrow = "→"
        d.text((W / 2 - 10, y), arrow, font=fr, fill=(120, 108, 104))
        d.text((W - M - 40 - d.textlength(c, font=frb), y), c, font=frb, fill=ONDARK)
        y += row
    t = "Save this before your next budget draft."
    fk = F(SANSB, 30)
    d.text(((W - d.textlength(t, font=fk)) / 2, H - 230), t, font=fk, fill=PINKTXT)
    footer(d, H, dark=True)
    return img


BUILDERS = [slide1, slide2, slide3, slide4, slide5, slide6]


def main():
    need, have, short = assert_budget()
    print(f"maths ok: 5% of {money(TOTAL)} = {money(need)}, "
          f"has {money(have)} (2%), short {money(short)}")
    for name, H in SIZES.items():
        out = os.path.join(OUT, name)
        os.makedirs(out, exist_ok=True)
        for i, fn in enumerate(BUILDERS, 1):
            img = fn(H)
            assert img.size == (W, H)
            p = os.path.join(out, f"slide-{i}.jpg")
            img.save(p, quality=94)
        print(f"{name}: {len(BUILDERS)} slides at {W}x{H} -> {out}")


if __name__ == "__main__":
    main()
