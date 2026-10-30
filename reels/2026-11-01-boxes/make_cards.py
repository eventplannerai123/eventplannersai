"""Hook and takeaway cards for the Sun 1 Nov boxes Reel.

The Instagram hook and the takeaway are the guide's own, from the SUN 1 NOV
details. TikTok takes a command-style one, as the house rules require.

PLACEMENT, measured against the beat underneath rather than reused. The opening
frame is the sent prompt bubble, which runs nearly the whole height — there is
no empty space to drop a card into. The hook sits at y=1300, below the ask
itself ("Turn it into a box-by-box manifest… who at the venue signs for it")
and over the packing list's middle rows, which are incidental: the viewer does
not need to read "Gaffer tape, 6" to understand the shot. It still clears the
bottom 25% where the platform's caption sits.

Every card is placed so its BOTTOM clears y=1440 — the top of the bottom 25%
that TikTok's caption and buttons cover. That is what sets the numbers, not
taste: the four-line Instagram hook is 356px tall, so it starts at 1070; the
two-line TikTok hook is 228px and starts at 1198; the takeaway is 308px and
starts at 1118. A first build put all three at 1240-1300 and each one ran
200px or more into the covered band.

The takeaway sits over the body of the note to the receiving team.
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
    "hook-instagram": ("Six boxes shipped\nto the venue. Here's\nhow all six make it\nto the room.", 1070, 56),
    "hook-tiktok": ("Stop shipping boxes\nwithout a manifest.", 1198, 62),
    "takeaway": ("Number every box.\nTell the venue\nwhat's coming.", 1118, 62),
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
        frame = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        frame.paste(c, ((W - c.size[0]) // 2, top), c)
        p = os.path.join(OUT, f"card-{name}.png")
        frame.save(p)
        print(name, c.size, "->", os.path.basename(p))


if __name__ == "__main__":
    main()
