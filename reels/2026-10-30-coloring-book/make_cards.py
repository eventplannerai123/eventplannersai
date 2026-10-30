"""Hook and takeaway overlay cards for the coloring book Reel.

Two overlays only, which is what the brief specifies: the hook over the first
two seconds and the takeaway over the last three. No rolling captions.

The hooks differ by platform, as the house rules require — Instagram takes the
brief's narrative line, TikTok a command-style one. TikTok's is not invented out
of nothing: "Stop buying another candle" is the voiceover's own line about the
bridesmaid, turned into an instruction.

Placement is measured against the safe zones (nothing that matters above 12% or
below 75%) AND against what the beat underneath is showing. The hook sits at
y=250 over the plain ceiling in her photo. The takeaway sits at y=1210, over the
blank lower half of the title page on the Instagram cut and over the lavender
ground on TikTok's — never over the drawing.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "build", "beats")
FONTS = os.path.join(HERE, "build", "fonts")

W, H = 1080, 1920
LAVENDER = (206, 203, 246)
PURPLE = (60, 52, 137)
P600 = os.path.join(FONTS, "Poppins-600.ttf")

CARDS = {
    "hook-instagram": ("50 wedding pages.\nMade with AI.\nColoured by hand.", 250, 62),
    "hook-tiktok": ("Stop buying\nanother candle.", 250, 76),
    "takeaway": ("Printable PDF on Etsy.\nPaperback on Amazon.", 1210, 54),
}
PAD_X, PAD_Y, GAP = 44, 34, 18


def card(text, px):
    f = ImageFont.truetype(P600, px)
    probe = ImageDraw.Draw(Image.new("RGB", (10, 10)))
    lines = text.split("\n")
    lw = max(probe.textlength(l, font=f) for l in lines)
    lh = int(px * 1.30)
    w = int(lw) + PAD_X * 2
    h = lh * len(lines) + PAD_Y * 2
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=28, fill=LAVENDER + (242,))
    y = PAD_Y + GAP // 2
    for l in lines:
        d.text(((w - d.textlength(l, font=f)) / 2, y - GAP // 2), l, font=f, fill=PURPLE)
        y += lh
    return img


def main():
    for name, (text, top, px) in CARDS.items():
        c = card(text, px)
        frame = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        frame.paste(c, ((W - c.size[0]) // 2, top), c)
        p = os.path.join(OUT, f"card-{name}.png")
        frame.save(p)
        print(name, c.size, "->", os.path.basename(p))


if __name__ == "__main__":
    main()
