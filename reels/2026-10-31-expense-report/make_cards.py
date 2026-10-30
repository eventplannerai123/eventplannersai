"""Hook and takeaway cards for the Sat 31 expense report Reel.

The hook is the guide's, from content bank item 18 and true: she really did tape
receipts to paper to fax them. TikTok takes a command-style one, as the house
rules require.

THE TAKEAWAY IS NOT THE BRIEF'S. The brief wrote "Paste the mess. Ask it to flag
duplicates before it totals." — written when the demo was going to be a block of
receipts pasted into the chat. She did something better: she pointed it at her
Gmail. So the overlay says what the video shows. The guide's own twist note tells
CC to rewrite the takeaway around what she actually caught, so this is the
instruction being followed rather than ignored.

Placement is measured against the beat underneath, and the opening frame has no
empty space at all — the prompt bubble runs the whole height. The first build
put the hook at y=250 and it covered "Search my Gmail for every receipt from my
work trip to Denver", which is the line the opening exists to show. It sits at
y=1180 instead: low enough to clear the attachments and the opening sentence,
high enough to stay out of the bottom 25% where the caption goes. It covers
"Fill it in, one row per receipt" for two seconds, which the viewer does not
need to read to understand the shot.

The takeaway sits at y=1250, on the lavender below her spreadsheet strip.
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
    "hook-instagram": ("I used to tape receipts\nto paper so they\ncould be faxed.", 1180, 62),
    "hook-tiktok": ("Stop typing your\nreceipts in one\nby one.", 1180, 66),
    "takeaway": ("Point it at your inbox.\nMake it flag duplicates\nbefore it totals.", 1250, 52),
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
