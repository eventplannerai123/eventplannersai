"""Sat 7 Nov — "Things I've said into a walkie-talkie this year".

Planner-life post 1 of 4 (content bank 33, weekly from November). One image,
not a carousel: the guide's CLAUDE CODE line asks for the title plus her lines
as a numbered list.

THE LINES ARE HERS. Four came from her verbatim on Nov 5; five more she picked
from a list drafted here and approved ("1 - 4 and 6"), which makes them hers
too. Nothing on this image was written and then assumed. Her own lines keep
her wording exactly, with two changes she made herself: the spelling of
"beginning", and "the meal" to "the lunch".

EIGHT, NOT NINE. She cut her own registration line against the directional
one — "1 and 3 are too similar cut 1" — so the less obvious of the two stayed.

No names, no venues, no clients, no employer: role and room only.

BRAND SYSTEM IS THE GUIDE'S: lavender #CECBF6, deep purple #3C3489, Poppins,
EP + star wordmark, bottom bar with the handle. Poppins is not installed here,
so the three weights are committed under build/fonts/. Poppins has no glyph at
U+2726, so the star is a drawn polygon.

TIKTOK SAFE ZONES decide the 1920 version's layout, not a scaled-up copy of
the 1350: nothing important in the top 12% (230px) or the bottom 25% (480px).
The list is fitted inside that window and the wordmark sits above it.
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

TITLE = "Things I’ve said\ninto a walkie-talkie\nthis year"

# Hers first, in the order she sent them, then the five she approved.
# "I need extra staff at registration" was hers too and came out on her call:
# "1 and 3 are too similar cut 1". Line 3 is the directional-duties one, which
# makes the same point in a less obvious place, so it is the one that stayed.
LINES = [
    "The lunch is late, someone talk to the caterer",
    "I need extra staff on directional duties",
    "The program is beginning, everyone quiet on the radio",
    "Who moved the stanchions",
    "The head table is one chair short",
    "Is anyone with the keynote speaker right now",
    "Doors are holding, don’t let anyone in yet",
    "I need more water at the back of the room",
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


def chrome(img, d, H):
    """Hairline rule, EP + star wordmark, handle — above TikTok's bottom 25%."""
    bar = H - 150 if H == 1350 else H - 300
    d.line([(M, bar), (W - M, bar)], fill=HAIRLINE, width=2)
    wf, hf = F(P700, 34), F(P400, 24)
    ep_w = d.textlength("EP", font=wf)
    star_r = 13
    ex, ey = (W - (ep_w + 10 + star_r * 2)) / 2, bar + 38
    d.text((ex, ey), "EP", font=wf, fill=PURPLE)
    sx, sy = ex + ep_w + 10 + star_r, ey + 34 * 0.62
    waist = star_r * 0.30
    d.polygon([(sx, sy - star_r), (sx + waist, sy - waist), (sx + star_r, sy),
               (sx + waist, sy + waist), (sx, sy + star_r), (sx - waist, sy + waist),
               (sx - star_r, sy), (sx - waist, sy - waist)], fill=PURPLE)
    d.text(((W - d.textlength(HANDLE, font=hf)) / 2, ey + 48), HANDLE, font=hf, fill=PURPLE)


def layout(d, H, title_px):
    """Return the blocks and total height for a given title size.

    The numbered list scales off the title so the two never drift apart: the
    number is 600 weight, the line 400, and a wrapped line hangs on the
    number's column rather than starting under it.
    """
    maxw = W - 2 * M
    tf = F(P700, title_px)
    title_lines = []
    for para in TITLE.split("\n"):
        title_lines += wrap(d, para, tf, maxw)
    tstep = int(title_px * 1.16)

    lp = max(26, int(title_px * 0.46))
    nf, lf = F(P600, lp), F(P400, lp)
    gutter = int(d.textlength("9. ", font=nf)) + 6
    lstep = int(lp * 1.30)
    gap = int(lp * 0.62)

    rows = []
    for i, text in enumerate(LINES, 1):
        rows.append((f"{i}.", wrap(d, text, lf, maxw - gutter)))

    total = (len(title_lines) * tstep + int(title_px * 0.70)
             + sum(len(ls) * lstep + (gap if k else 0) for k, (_, ls) in enumerate(rows)))
    return (tf, title_lines, tstep, nf, lf, gutter, lstep, gap, rows), total


def build(H):
    img = Image.new("RGB", (W, H), LAVENDER)
    d = ImageDraw.Draw(img)

    # The window: TikTok's top 12% / bottom 25% on the 1920, ordinary margins
    # on the 1350, where the chrome is the only thing below the list.
    top = 150 if H == 1350 else int(H * 0.12) + 24
    bottom = (H - 190) if H == 1350 else int(H * 0.75) - 24
    budget = bottom - top

    for title_px in range(84, 33, -2):
        parts, total = layout(d, H, title_px)
        if total <= budget:
            break
    else:
        raise SystemExit(f"the list does not fit at {H}")

    tf, title_lines, tstep, nf, lf, gutter, lstep, gap, rows = parts
    y = top + (budget - total) // 2

    for ln in title_lines:
        d.text((M, y), ln, font=tf, fill=PURPLE)
        y += tstep
    y += int(title_px * 0.70)

    for k, (num, ls) in enumerate(rows):
        if k:
            y += gap
        d.text((M, y), num, font=nf, fill=PURPLE)
        for j, ln in enumerate(ls):
            d.text((M + gutter, y + j * lstep), ln, font=lf, fill=PURPLE)
        y += len(ls) * lstep

    chrome(img, d, H)
    return img, title_px, y


def check():
    assert len(LINES) == 8, "eight lines: she cut the registration one as too close to line 3"
    assert len(set(LINES)) == 8, "a line is repeated"
    banned = ("hilton", "marriott", "convention center", "ballroom a")
    for ln in LINES:
        assert not any(b in ln.lower() for b in banned), f"named place in: {ln}"
        assert ln[0].isupper(), f"not sentence case: {ln}"
        assert not ln.endswith("."), f"trailing full stop: {ln}"
    print(f"checks pass: {len(LINES)} lines, no names, no venues")


def main():
    check()
    os.makedirs(OUT, exist_ok=True)
    for name, H in SIZES.items():
        img, px, end_y = build(H)
        assert img.size == (W, H)
        p = os.path.join(OUT, f"walkie-talkie-{name}.jpg")
        img.save(p, quality=95)
        limit = (H - 190) if H == 1350 else int(H * 0.75)
        print(f"{name}: title {px}px, list ends y={end_y} (limit {limit}) -> {os.path.basename(p)}")


if __name__ == "__main__":
    main()
