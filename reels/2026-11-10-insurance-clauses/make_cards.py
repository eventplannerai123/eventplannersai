"""Overlay cards for the Tue 10 Nov insurance-clauses Reel.

Brand palette: lavender #CECBF6 ground, deep purple #3C3489 text, Poppins 600.
The Instagram hook is the guide's own sentence; TikTok takes a command-style
one, as the house rules require.

THE END CARD IS THE BUDGET LINE, AND IT SUBSTITUTES. The guide's Nov 3 soft
mention says to end this Reel on "Comment BUDGET for the tracker I use"
*instead of* the usual closing line, so the guide's own takeaway overlay
("Check the certificate against the contract. Then confirm with your
broker.") is replaced rather than appended to. TikTok says "on my Instagram":
there is no bio link there and the ManyChat automation lives on Instagram.

PLACEMENT IS MEASURED AGAINST THE BEAT UNDERNEATH, off a y-ruler rather than
guessed, and `preview()` in render.py composites each card onto its own beat
before anything is exported.

THE END CARD SITS HIGH ON THIS ONE, which is the opposite of Mon 9. The last
beat's whole job is the vendor-insurance section — the paragraph that says
Sahiba's own certificate does not satisfy the vendors' obligations, which is
the correction she makes in the last line of the voiceover. That runs from
about y=750 down, so the card goes above it, over the leftover
indemnification text the beat does not need.
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
    # b0-prompt: the two PDF chips end at y=260 and the prompt bubble runs
    # 290-1340, so there is no clear ground. The card takes the bubble's last
    # line and its bottom padding and leaves the first nine lines of the
    # prompt readable, which is the reason the cut opens on this frame.
    "hook-instagram": ("The contract asks for $2 million\nin liquor liability.\n"
                       "The policy has $1 million.", 1200, 42),
    "hook-tiktok":    ("Stop trusting the certificate\nyour broker sent.", 1240, 48),
    # b5-vendor: "6. Two additional things you shouldn't overlook" starts at
    # y=753 and the vendor bullets run to 1377. Everything above 700 is the
    # tail of the indemnification section, which this beat does not need, so
    # the card goes there. The beat's 4% push lifts the heading to about 676
    # by the last frame, still clear of the card's bottom edge.
    "end-instagram":  ("Comment BUDGET\nfor the tracker I use", 250, 54),
    "end-tiktok":     ("Comment BUDGET\non my Instagram", 250, 54),
}
PAD_X, PAD_Y = 44, 34

# What each card must not run into, measured off the beat it sits on.
FLOOR = {"hook-instagram": 1440, "hook-tiktok": 1440,
         "end-instagram": 700, "end-tiktok": 700}


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
