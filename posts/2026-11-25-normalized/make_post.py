"""Wed 25 Nov, 12:30pm — "Things I normalized in events that I really shouldn't have."

The second planner list Reel, same format as Mon 23's: one image, a title and
short lines in boxes, held 8-10 seconds as a Reel with music on Instagram and
Facebook, and the same image as a photo post on TikTok. Deep purple #3C3489
ground, lavender #CECBF6 boxes, Poppins — the inverse of the carousel, as the
November plan specifies for this format.

**THE FIFTH LINE IS HERS, CHOSEN MON 23.** Her Wed 25 YOU line asked her for
one true thing from her own years by Mon 23, and said the piece runs with four
if none came. She picked from six suggestions and the answer was **"Answering
a client email at 11pm because they sent it at 11pm."** — the only one of the
six about a boundary rather than money or blame, and the one that matches the
list's own rhythm, where the habit and its excuse sit in the same sentence.

`check()` still accepts four or five, so the piece degrades rather than breaks
if the line is ever pulled.

**THE LINES ARE THE GUIDE'S, VERBATIM.** `check()` asserts the first four word
for word, so a later tidy-up fails the build instead of publishing a
paraphrase of her own habit.

**THE LONGEST LINE IS LONGER THAN ANY OF MON 23'S** — "Signing the Saturday
quote without asking for the weekday rate." at 70 characters — so the box text
size is solved for it rather than typed, and the last box is asserted to clear
the bottom 25% where TikTok's furniture sits.

NO BUDGET LINE, no prompt, no sales line. A planner-life list — the Nov 14
rule about checking the closing line against the piece.
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

TITLE = "Things I normalized\nin events that I\nreally shouldn’t have."

# The guide's four. Her fifth goes on the end of both lists when it arrives.
GUIDE_FOUR = [
    "Eating standing up, behind a curtain, in under three minutes.",
    "Keeping every vendor payment in my head.",
    "Every tab open on my laptop at 2am before load-in.",
    "Signing the Saturday quote without asking for the weekday rate.",
]

HERS = "Answering a client email at 11pm because they sent it at 11pm."

LINES = GUIDE_FOUR + [HERS]

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
    # The guide's four, word for word. A fifth may be appended — hers — but
    # the four underneath it are not ours to reword.
    assert LINES[:4] == GUIDE_FOUR, "a line drifted from the guide"
    assert len(LINES) in (4, 5), (
        "the format is five lines and runs with four until she sends one")
    if len(LINES) == 4:
        print("NOTE: running with four lines — her fifth has not arrived")
    joined = (TITLE + " " + " ".join(LINES)).lower()
    for banned in ("budget", "prompt", "chatgpt", "link in bio", "gumroad", "comment "):
        assert banned not in joined, f"no CTA or AI demo: found {banned!r}"
    print(f"checks pass: {len(LINES)} lines, "
          f"longest {max(len(l) for l in LINES)} chars")


def main():
    check()
    os.makedirs(OUT, exist_ok=True)
    img, tpx, bpx, end_y = build()
    assert img.size == (W, H)
    # Nothing important in the top 12% or the bottom 25% is the safe-zone
    # rule; the boxes are the content, so the last one has to clear 1440.
    assert end_y <= 1440, f"the last box ends at {end_y}, inside the bottom 25%"
    p = os.path.join(OUT, "normalized.jpg")
    img.save(p, quality=95)
    print(f"title {tpx}px, boxes {bpx}px, ends y={end_y} -> {os.path.basename(p)}")


if __name__ == "__main__":
    main()
