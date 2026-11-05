"""Overlay cards for the Fri 6 Nov three-quotes Reel.

Brand palette, not a copy of the last build's: lavender #CECBF6 ground, deep
purple #3C3489 text, Poppins 600. The Instagram hook is the guide's own
sentence; TikTok takes a command-style one, as the house rules require.

PLACEMENT IS MEASURED AGAINST THE BEAT UNDERNEATH. Every card's bottom clears
y=1440, the top of the bottom 25% that TikTok's caption and buttons cover, and
`preview()` in render.py composites each one onto its own beat so a bad y is
caught before an export rather than after.
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
    # The prompt bubble on b0 ends at y=1245 and the bottom 25% starts at 1440,
    # so the hook has 195px of clear frame: two lines, not three. Covering the
    # bubble's last line is not an option — "Tell me which is cheapest overall
    # and where each one is hiding cost" is the whole reason the cut opens here.
    "hook-instagram": ("Three quotes: $8,400, $9,100, $11,200.\nThe cheapest one cost the most.", 1248, 44),
    "hook-tiktok":    ("Stop comparing\nquote totals.", 1248, 46),
    # Sits ABOVE the twist line. On b5 "Northgate is the price winner today,
    # but I'd make its staffing commitments part of the final agreement" starts
    # at y=1395, and the beat's 4% push lifts it about 77px over 5.2s, so a card
    # ending near 1300 would land on it by the last frame. 1228 clears it.
    "end":            ("Compare the real totals,\nnot the headline price.", 1020, 54),
}
PAD_X, PAD_Y = 44, 34


def card(text, px):
    f = ImageFont.truetype(P600, px)
    probe = ImageDraw.Draw(Image.new("RGB", (10, 10)))
    lines = text.split("\n")
    lw = max(probe.textlength(l, font=f) for l in lines)
    lh = int(px * 1.30)
    w, h = int(lw) + PAD_X * 2, lh * len(lines) + PAD_Y * 2
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=28, fill=LAVENDER + (243,))
    y = PAD_Y
    for l in lines:
        d.text(((w - d.textlength(l, font=f)) / 2, y), l, font=f, fill=PURPLE)
        y += lh
    return img


def main():
    os.makedirs(OUT, exist_ok=True)
    for name, (text, top, px) in CARDS.items():
        c = card(text, px)
        assert top + c.size[1] <= 1440, (
            f"{name} runs into the bottom 25%: ends at {top + c.size[1]}")
        assert c.size[0] <= W - 40, f"{name} is wider than the frame ({c.size[0]})"
        frame = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        frame.paste(c, ((W - c.size[0]) // 2, top), c)
        frame.save(os.path.join(OUT, name + ".png"))
        print(f"{name:16s} {c.size[0]}x{c.size[1]} at y={top}, bottom {top + c.size[1]}")


if __name__ == "__main__":
    main()
