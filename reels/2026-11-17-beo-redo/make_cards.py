"""Overlay cards for the Tue 17 Nov BEO-redo Reel.

Brand palette: lavender #CECBF6 ground, deep purple #3C3489 text, Poppins 600.
The Instagram hook is the guide's own overlay line; TikTok takes a
command-style one.

**THIS ONE CARRIES THE BUDGET LINE AND THE MON 16 PIECE DID NOT.** The Nov 3
soft mention covers Thu 5, Mon 9, Tue 10 and Tue 17, and Tue 10 came off it
on Nov 9, so Tue 17 is the live one: the end card is the guide's own
"Comment BUDGET for the tracker I use.", and the TikTok cut says "Comment
BUDGET on my Instagram." because the automation lives there and TikTok has no
bio link. It is the last line of the Instagram caption too.

PLACEMENT IS MEASURED AGAINST THE BEAT UNDERNEATH, and `preview()` in
render.py composites each card onto its own beat before anything is exported.

- b0-runsheet is the timeline table from the top; below it sit the vendor
  service rows and an "Operational notes" paragraph, so the hook goes at
  y=1220 over the notes, which the cut does not need and b4 restates.
- b4-blanks is the RESPONSIBLE column, and the highlighted "Room reset team
  not named in BEO" line is at y 615-653 — the whole point of the beat. So
  the end card goes low, at y=1150, over the vendor block that b3 has
  already shown.

CARDS ARE OPAQUE: both land on dense black table text.
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
    "hook-instagram": ("The BEO is 14 pages.\nAt 7am you need one.", 1220, 52),
    "hook-tiktok":    ("Stop carrying the\n14-page BEO.", 1220, 56),
    "end-instagram":  ("Comment BUDGET\nfor the tracker I use.", 1150, 52),
    "end-tiktok":     ("Comment BUDGET\non my Instagram.", 1150, 52),
}
PAD_X, PAD_Y = 44, 34

FLOOR = {k: 1440 for k in CARDS}


def card(text, px):
    f = ImageFont.truetype(P600, px)
    probe = ImageDraw.Draw(Image.new("RGB", (10, 10)))
    lines = text.split("\n")
    lw = max(probe.textlength(l, font=f) for l in lines)
    lh = int(px * 1.30)
    w, h = int(lw) + PAD_X * 2, lh * len(lines) + PAD_Y * 2
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=28, fill=LAVENDER + (255,))
    y = PAD_Y
    for l in lines:
        d.text(((w - d.textlength(l, font=f)) / 2, y), l, font=f, fill=PURPLE)
        y += lh
    return img


def main():
    os.makedirs(OUT, exist_ok=True)
    # The BUDGET line is the whole point of the Tue 17 end card; a silent
    # rewrite would drop a live ManyChat automation on the floor.
    assert "Comment BUDGET" in CARDS["end-instagram"][0]
    assert CARDS["end-tiktok"][0].endswith("on my Instagram."), \
        "TikTok has no bio link; the automation lives on Instagram"
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
        print(f"{name:16s} {c.size[0]}x{c.size[1]} at y={top}, bottom {bottom}")


if __name__ == "__main__":
    main()
