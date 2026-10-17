"""Hook card for the Sep 30 feedback debrief rebuild.

One overlay only: the approved hook, over the frozen opening frame.

Placement is measured, not eyeballed. cardkit's line finder reports the
frame's real text lines, and the ones that matter are **1017-1289** — the
three numbered changes, which are the whole reason the brief says to open on
this frame rather than on the survey responses. The card must not touch them.

It sits instead over 344-617, inside the "The survey doesn't suggest that you
need to reinvent the conference" paragraph. That is the least load-bearing
text on screen: it is context for the three changes, not the changes.
"""
import os, sys
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "..", "tools"))
from cardkit import preview, _lines   # noqa: E402

W, H = 1080, 1920
FONT = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
OUT = os.path.join(HERE, "cards"); os.makedirs(OUT, exist_ok=True)
SAFE_TOP, SAFE_BOT = int(H * 0.12), int(H * 0.75)
FRAME = os.path.join(HERE, "frames", "open.png")

# The block the opening exists to show. Measured below and asserted against.
CHANGES_TOP, CHANGES_BOT = 1017, 1289


def card(img, lines, fs, cy, name, px=48, py=38, r=30,
         bg=(0, 0, 0, 220), fg=(255, 255, 255, 255)):
    d = ImageDraw.Draw(img, "RGBA")
    f = ImageFont.truetype(FONT, fs); lh = int(fs * 1.28)
    w = [d.textbbox((0, 0), l, font=f)[2] - d.textbbox((0, 0), l, font=f)[0] for l in lines]
    bw = max(w) + px * 2; bh = lh * (len(lines) - 1) + fs + py * 2
    x0, y0 = (W - bw) // 2, cy - bh // 2
    assert y0 >= SAFE_TOP and y0 + bh <= SAFE_BOT, f"{name} outside safe band: {y0}-{y0+bh}"
    assert bw <= W - 40, f"{name} too wide: {bw}"
    assert y0 + bh < CHANGES_TOP, \
        f"{name} reaches {y0+bh}, into the three changes at {CHANGES_TOP}"
    d.rounded_rectangle([x0, y0, x0 + bw, y0 + bh], radius=r, fill=bg)
    ty = y0 + py
    for l in lines:
        bb = d.textbbox((0, 0), l, font=f)
        d.text(((W - (bb[2] - bb[0])) // 2 - bb[0], ty - bb[1]), l, font=f, fill=fg)
        ty += lh
    print(f"  card {name}: y {y0}-{y0+bh}, w {bw}")


def check_frame():
    """The card is placed against measured ink, so fail if the frame moved."""
    _, rows = _lines(FRAME)
    starts = [a for a, b in rows]
    assert CHANGES_TOP in starts, \
        f"the three changes no longer start at {CHANGES_TOP}; found {starts}"
    print(f"  frame ok: {len(rows)} text lines, changes block at "
          f"{CHANGES_TOP}-{CHANGES_BOT}")


check_frame()
hook = Image.new("RGBA", (W, H), (0, 0, 0, 0))
card(hook, ['Stop saying',
            '"that’s how we did it',
            'last year."'], 56, 480, "hook")
hook.save(f"{OUT}/hook.png")

preview([FRAME], [f"{OUT}/hook.png"], os.path.join(HERE, "preview.png"))
print("  preview written")
