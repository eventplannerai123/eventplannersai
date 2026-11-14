"""Overlay cards for the Tue 17 Nov BEO-redo Reel.

Brand palette: lavender #CECBF6 ground, deep purple #3C3489 text, Poppins 600.
The Instagram hook is the guide's own overlay line; TikTok takes a
command-style one.

**THE BUDGET LINE CAME OFF ON 2026-11-14, HER DECISION.** The Nov 3 soft
mention put one here — Tue 17 was the last of its four Reels, Thu 5, Mon 9,
Tue 10 and Tue 17, and Tue 10 had already come off on Nov 9. She saw the
finished cut, asked why it carried one, and said to pull it. So the end card
is the piece's own takeaway instead, both cuts share it, and the ManyChat
task for Tue 17 is disabled. That is the second of the four to come off this
way, and for the same reason both times: the CTA did not fit the piece.

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
    "end-instagram":  ("Ask for the blanks too.\nThey\u2019re your call list.", 1150, 50),
    "end-tiktok":     ("Ask for the blanks too.\nThey\u2019re your call list.", 1150, 50),
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
    # She pulled the BUDGET line on Nov 14. Nothing here may put one back:
    # the ManyChat task for this Reel is disabled, so a CTA on screen would
    # promise a DM that never arrives.
    for name, (text, _, _) in CARDS.items():
        assert "BUDGET" not in text, f"{name} still carries a BUDGET line"
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
