"""Hook and takeaway cards for the Mon 2 Nov "fees nobody quotes" Reel.

The Instagram hook and the takeaway are the guide's own, from the MON 2 NOV
details. TikTok takes a command-style one, as the house rules require.

PLACEMENT, measured against the beat underneath rather than reused. Every card
is placed so its BOTTOM clears y=1440, the top of the bottom 25% that TikTok's
caption and buttons cover.

Both hooks open over the sent prompt, which runs down the middle of the frame,
so they sit low enough to leave the ask itself readable. The takeaway closes
over the paragraph below the $261.46 line on Instagram, and below the "My take"
paragraph on TikTok — in both cases over text the viewer does not need.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "build")
FONTS = os.path.join(HERE, "build", "fonts")

W, H = 1080, 1920
LAVENDER = (206, 203, 246)
PURPLE = (60, 52, 137)
P600 = os.path.join(FONTS, "Poppins-600.ttf")

CARDS = {
    "hook-instagram": ("$185 a person,\nthey said. Here's\nwhat it really costs.", 1147, 58),
    "hook-tiktok": ("Stop trusting the\nper-person rate.", 1198, 62),
    "takeaway": ("Ask for the all-in\nnumber before you sign.", 1228, 56),
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
    for name, (text, top, px) in CARDS.items():
        c = card(text, px)
        assert top + c.size[1] <= 1440, f"{name} runs into the bottom 25%"
        assert c.size[0] <= W - 40, f"{name} is wider than the frame"
        frame = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        frame.paste(c, ((W - c.size[0]) // 2, top), c)
        p = os.path.join(OUT, f"card-{name}.png")
        frame.save(p)
        print(name, c.size, "bottom", top + c.size[1], "->", os.path.basename(p))


if __name__ == "__main__":
    main()
