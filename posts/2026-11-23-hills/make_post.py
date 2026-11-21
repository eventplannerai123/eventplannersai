"""Mon 23 Nov, 12:30pm — "Hills I'll die on as an event planner."

**THE FIRST PLANNER LIST REEL.** Her format, added to the November plan on
Nov 18: a new kind of 12:30pm second post that alternates with the
planner-feelings Reels. One image, a title and five short lines in boxes,
held 8-10 seconds as a Reel with music on Instagram and Facebook, and the
same image as a photo post on TikTok. Her reference for the format was a
list-prompt post with 6,433 likes and 6,690 sends — the point is that lists
are what people send to a friend, which is why the caption ends on a question
and she leaves the first comment herself.

**THE FIVE LINES ARE HERS, VERBATIM FROM THE MON 23 BLOCK.** Nothing here is
composed, and `check()` asserts each one against the guide's text. They are
also five rules this account has already made pieces about — the captain
(Wed 18), the kitchen at half full (Sun 22), the rain plan, AV, and checking
the invoice against the BEO (Mon 9) — which is what makes the list hers
rather than a listicle.

Look, as the November plan specifies for this format and the inverse of the
carousel: **deep purple #3C3489 ground, lavender #CECBF6 boxes**, title in
Poppins SemiBold white, the lines in Poppins Regular deep purple inside the
boxes. No numbered badge, no AI demo, no sales line.

**ITS LINE STARTS "Every role gets a captain" AND THE BOX HAS TO HOLD IT.**
The longest line is 62 characters, so the box text size is solved for the
longest line rather than typed, and the fit is asserted.

NO BUDGET LINE. A planner-life list, not a money piece — the Nov 14 rule.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "slides")
FONTS = os.path.join(HERE, "build", "fonts")

W, H = 1080, 1920
PURPLE = (60, 52, 137)
LAVENDER = (206, 203, 246)
WHITE = (255, 255, 255)

P400 = os.path.join(FONTS, "Poppins-400.ttf")
P600 = os.path.join(FONTS, "Poppins-600.ttf")
F = lambda p, s: ImageFont.truetype(p, s)

M = 72
HANDLE = "@aiforeventplanners"

TITLE = "Hills I’ll die on\nas an event planner."

LINES = [
    "Every role gets a captain, so nobody has to come find me.",
    "Call the kitchen at half full, not empty.",
    "The rain plan gets priced in pre-planning, not the week of.",
    "AV is the first thing I check when I walk in.",
    "No one pays the final invoice until it’s checked against the BEO.",
]

PAD_X, PAD_Y, GAP = 38, 30, 24
RADIUS = 26


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


def layout(d, title_px, box_px):
    maxw = W - 2 * M
    tf = F(P600, title_px)
    title = []
    for line in TITLE.split("\n"):
        title += wrap(d, line, tf, maxw)
    tstep = int(title_px * 1.16)

    bf = F(P400, box_px)
    bstep = int(box_px * 1.34)
    inner = maxw - 2 * PAD_X
    boxes = [wrap(d, t, bf, inner) for t in LINES]
    bh = [len(b) * bstep + 2 * PAD_Y for b in boxes]

    total = (len(title) * tstep + int(title_px * 0.80)
             + sum(bh) + GAP * (len(boxes) - 1))
    return (tf, title, tstep, bf, bstep, boxes, bh), total, len(title)


def build():
    img = Image.new("RGB", (W, H), PURPLE)
    d = ImageDraw.Draw(img)
    # THE SAFE ZONES ARE THE LAYOUT, not a check afterwards. Nothing
    # important in the top 12% (230px) or the bottom 25% (from 1440), where
    # TikTok's caption and buttons sit — and on this format the boxes ARE the
    # content, so the whole block is centred inside that band rather than in
    # the frame. Centring in the frame put the last box at y=1499.
    top, bottom = 250, 1440
    budget = bottom - top

    # The title carries its own break, so a size that re-wraps it is the wrong
    # size however well the block fits. Both sizes come down together.
    written = len(TITLE.split("\n"))
    for title_px in range(86, 43, -2):
        box_px = max(28, int(title_px * 0.46))
        parts, total, nlines = layout(d, title_px, box_px)
        if total <= budget and nlines == written:
            break
    else:
        raise SystemExit("the list does not fit")

    tf, title, tstep, bf, bstep, boxes, bh = parts
    y = top + (budget - total) // 2

    for ln in title:
        d.text((M, y), ln, font=tf, fill=WHITE)
        y += tstep
    y += int(title_px * 0.80)

    for lines, h in zip(boxes, bh):
        d.rounded_rectangle([M, y, W - M, y + h], radius=RADIUS, fill=LAVENDER)
        ty = y + PAD_Y
        for ln in lines:
            d.text((M + PAD_X, ty), ln, font=bf, fill=PURPLE)
            ty += bstep
        y += h + GAP
    y -= GAP

    hf = F(P400, 24)
    d.text(((W - d.textlength(HANDLE, font=hf)) / 2, H - 92), HANDLE,
           font=hf, fill=LAVENDER)
    return img, title_px, box_px, y


def check():
    # Her five lines, word for word out of the Mon 23 block. If one ever
    # drifts into a paraphrase, this fails rather than publishing it.
    guide = [
        "Every role gets a captain, so nobody has to come find me.",
        "Call the kitchen at half full, not empty.",
        "The rain plan gets priced in pre-planning, not the week of.",
        "AV is the first thing I check when I walk in.",
        "No one pays the final invoice until it’s checked against the BEO.",
    ]
    assert LINES == guide, "a line drifted from the guide"
    assert len(LINES) == 5, "the format is five lines"
    joined = (TITLE + " " + " ".join(LINES)).lower()
    for banned in ("budget", "prompt", "chatgpt", "link in bio", "gumroad", "comment "):
        assert banned not in joined, f"no CTA or AI demo: found {banned!r}"
    print(f"checks pass: 5 lines, longest {max(len(l) for l in LINES)} chars")


def main():
    check()
    os.makedirs(OUT, exist_ok=True)
    img, tpx, bpx, end_y = build()
    assert img.size == (W, H)
    # Nothing important in the top 12% or the bottom 25% is the safe-zone
    # rule; the boxes are the content, so the last one has to clear 1440.
    assert end_y <= 1440, f"the last box ends at {end_y}, inside the bottom 25%"
    p = os.path.join(OUT, "hills.jpg")
    img.save(p, quality=95)
    print(f"title {tpx}px, boxes {bpx}px, ends y={end_y} -> {os.path.basename(p)}")


if __name__ == "__main__":
    main()
