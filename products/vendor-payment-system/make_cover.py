"""The Gumroad cover for The Vendor Payment System.

1280x720, the size Gumroad renders a product cover at on the listing page and
in a share card. Brand look, same as every carousel: lavender #CECBF6, deep
purple #3C3489, Poppins, EP✦ wordmark drawn rather than typed.

It says what the thing IS in three words of body copy, because a cover that
only carries the title sells nothing on a storefront where the title is already
printed underneath it.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(HERE, "build", "fonts")
OUT = os.path.join(HERE, "cover.png")

W, H = 1280, 720
LAVENDER = (206, 203, 246)
PURPLE = (60, 52, 137)
HAIRLINE = (176, 172, 228)

P400 = os.path.join(FONTS, "Poppins-400.ttf")
P600 = os.path.join(FONTS, "Poppins-600.ttf")
P700 = os.path.join(FONTS, "Poppins-700.ttf")
F = lambda p, s: ImageFont.truetype(p, s)

M = 84
TITLE = "The Vendor\nPayment System"
SUB = "Stop retyping deposits."
ITEMS = ["A tracker that flags every payment before it's due",
         "Six prompts that fill it from your inbox and contracts",
         "A 20-minute setup guide"]


def star(d, cx, cy, r):
    waist = r * 0.30
    d.polygon([(cx, cy - r), (cx + waist, cy - waist), (cx + r, cy),
               (cx + waist, cy + waist), (cx, cy + r), (cx - waist, cy + waist),
               (cx - r, cy), (cx - waist, cy - waist)], fill=PURPLE)


def main():
    img = Image.new("RGB", (W, H), LAVENDER)
    d = ImageDraw.Draw(img)

    wf = F(P700, 30)
    d.text((M, 56), "EP", font=wf, fill=PURPLE)
    star(d, M + d.textlength("EP", font=wf) + 22, 56 + 30 * 0.62, 12)

    tf = F(P700, 72)
    y = 170
    for ln in TITLE.split("\n"):
        d.text((M, y), ln, font=tf, fill=PURPLE)
        y += 84

    y += 18
    sf = F(P600, 30)
    d.text((M, y), SUB, font=sf, fill=PURPLE)
    y += 54
    d.line([(M, y), (M + 120, y)], fill=HAIRLINE, width=2)
    y += 28

    bf = F(P400, 23)
    for it in ITEMS:
        d.ellipse([M + 2, y + 9, M + 10, y + 17], fill=PURPLE)
        d.text((M + 26, y), it, font=bf, fill=PURPLE)
        y += 38

    hf = F(P400, 22)
    d.text((M, H - 74), "@aiforeventplanners", font=hf, fill=PURPLE)

    for it in ITEMS:
        assert M + 26 + d.textlength(it, font=bf) < W - M, f"too wide: {it}"
    img.save(OUT)
    print(OUT, img.size)


if __name__ == "__main__":
    main()
