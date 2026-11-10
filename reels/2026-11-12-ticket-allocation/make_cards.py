"""Overlay cards for the Thu 12 Nov ticket-allocation Reel.

Brand palette: lavender #CECBF6 ground, deep purple #3C3489 text, Poppins 600.
The Instagram hook is the guide's own sentence; TikTok takes a command-style
one, as the house rules require.

NO BUDGET LINE ON THIS ONE. The Nov 3 soft mention covers Thu 5, Mon 9, Tue 10
and Tue 17 only — and Tue 10 came off it on Nov 9 — so Thu 12 ends on the
guide's own takeaway overlay, "Dedupe the lists before you say you're sold
out." The same line on both cuts: nothing here turns on a bio link.

PLACEMENT IS MEASURED AGAINST THE BEAT UNDERNEATH, off a y-ruler rather than
guessed, and `preview()` in render.py composites each card onto its own beat
before anything is exported.

CARDS ARE OPAQUE, not the usual 243 alpha, for the same reason as Tue 10:
every card here lands on a dense paragraph or a table rather than white
space, and at 243 the text underneath shows through the lavender.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "build", "cards")
FONTS = os.path.join(HERE, "build", "fonts")

W, H = 1080, 1920
LAVENDER = (206, 203, 246)
PURPLE = (60, 52, 137)
P600 = os.path.join(FONTS, "Poppins-600.ttf")

CARDS = {
    # name:            (text, top y, px)
    # b0-prompt: the PDF chip ends at y=230 and the prompt bubble runs
    # 300-1340, so there is no clear ground. The card takes the bubble's last
    # line and its bottom padding and leaves the first ten lines of the prompt
    # readable, which is the reason the cut opens on this frame.
    "hook-instagram": ("2,000 tickets. 140 people\nwere promised a seat twice.", 1240, 46),
    "hook-tiktok":    ("Stop telling sales\nyou're sold out.", 1240, 50),
    # b5-list: the "Name / First team / Second team" header sits at y=130-230
    # and the rows run from 290 down. The beat's job is one person against two
    # account teams, which the header and the first seven rows already show,
    # so the card covers rows that only repeat it.
    "end-instagram":  ("Dedupe the lists before\nyou say you're sold out.", 1020, 54),
    "end-tiktok":     ("Dedupe the lists before\nyou say you're sold out.", 1020, 54),
}
PAD_X, PAD_Y = 44, 34

# What each card must not run into, measured off the beat it sits on.
FLOOR = {"hook-instagram": 1440, "hook-tiktok": 1440,
         "end-instagram": 1440, "end-tiktok": 1440}


def card(text, px):
    f = ImageFont.truetype(P600, px)
    probe = ImageDraw.Draw(Image.new("RGB", (10, 10)))
    lines = text.split("\n")
    lw = max(probe.textlength(l, font=f) for l in lines)
    lh = int(px * 1.30)
    w, h = int(lw) + PAD_X * 2, lh * len(lines) + PAD_Y * 2
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    # Opaque, not the usual 243. Every card on this piece lands on a dense
    # paragraph rather than white space, and at 243 the text underneath
    # showed through the lavender in the exported frames.
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=28, fill=LAVENDER + (255,))
    y = PAD_Y
    for l in lines:
        d.text(((w - d.textlength(l, font=f)) / 2, y), l, font=f, fill=PURPLE)
        y += lh
    return img


def main():
    os.makedirs(OUT, exist_ok=True)
    for name, (text, top, px) in CARDS.items():
        c = card(text, px)
        bottom = top + c.size[1]
        assert top >= 240, f"{name} starts at {top}, inside the top 12%"
        assert bottom <= FLOOR[name], (
            f"{name} ends at {bottom}, past its floor of {FLOOR[name]}")
        assert c.size[0] <= W - 40, f"{name} is wider than the frame ({c.size[0]})"
        frame = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        frame.paste(c, ((W - c.size[0]) // 2, top), c)
        frame.save(os.path.join(OUT, name + ".png"))
        print(f"{name:16s} {c.size[0]}x{c.size[1]} at y={top}, bottom {bottom} "
              f"(floor {FLOOR[name]})")


if __name__ == "__main__":
    main()
