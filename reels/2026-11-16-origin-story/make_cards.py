"""Overlay cards for the Mon 16 Nov origin-story Reel.

Brand palette: lavender #CECBF6 ground, deep purple #3C3489 text, Poppins 600.
The Instagram hook is the guide's own overlay line; TikTok takes a
command-style one, as the house rules require.

NO BUDGET LINE. The Mon 16 block says so outright — it is her origin story
and it ends on the takeaway.

**THE END CARD IS REWRITTEN AROUND WHAT SHE ACTUALLY CAUGHT**, which is what
the brief asks for. Its own line was "Clean the export before the mail merge,
not after the tags are printed"; her twist is that the answer codes everyone
by the guest type they picked, so a sponsor who is also speaking comes out
SPO when the badge needs SPK. The card keeps the first half and spends the
second on the catch.

PLACEMENT IS MEASURED AGAINST THE BEAT UNDERNEATH, and `preview()` in
render.py composites each card onto its own beat before anything is exported.

- b0-codes is dense from the top: the five code rows run to about y=1115 and
  the "3. Organisation names standardised" heading follows at 1247. The hook
  goes at y=1180, over that heading and its paragraph — which the cut shows
  again at b3 — and still clears the bottom 25%.
- b4-files opens on the CSV download box, y 0-320, which the beat does not
  need; the lines that matter are "Names and job titles..." at 1193 and "My
  recommendation" at 1454. So the end card takes the top at y=250 and its
  floor is 900.

CARDS ARE OPAQUE, as on every piece since Tue 10: both land on dense black
text, and at 243 alpha it shows through the lavender.
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
    "hook-instagram": ("3,500 name tags.\nEvery one coded by guest type.", 1180, 52),
    "hook-tiktok":    ("Stop coding name\ntags by hand.", 1180, 58),
    "end-instagram":  ("Clean the export first.\nThen check anyone\nwith two roles.", 250, 54),
    "end-tiktok":     ("Clean the export first.\nThen check anyone\nwith two roles.", 250, 54),
}
PAD_X, PAD_Y = 44, 34

FLOOR = {"hook-instagram": 1440, "hook-tiktok": 1440,
         "end-instagram": 900, "end-tiktok": 900}


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
