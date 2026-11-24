"""Overlay cards for the Sun 29 Nov budget-uplift Reel.

Brand palette: lavender #CECBF6 ground, deep purple #3C3489 text, Poppins 600.
The Instagram hook is the guide's own overlay line; TikTok takes a
command-style one.

**THIS ONE DOES CARRY A BUDGET LINE, AND THAT IS THE POINT OF THE CHECK.**
The Nov 14 rule is to read the closing line against the piece before
rendering, not to ban the CTA — it came off the insurance Reel and the BEO
redo because neither was about money. This one is a budget, and the guide
calls it "the one money piece inside the Black Friday window". So the assert
below is inverted: it requires the CTA rather than refusing it, and requires
the deadline with it, because a code with no date is a promise with no end.

**MANYCHAT IS PAUSED, SO THE DM IS HERS BY HAND.** Her Sun 29 YOU line says
so outright: reply to any BUDGET comment with the DM text and the Gumroad
link. A closing card that promises a DM nobody sends is the failure the Nov
14 rule exists to prevent, so this card is only honest while that line is
open — it is not a card to reuse on a day she is not watching the comments.

**THE TAKEAWAY AND THE CTA DO NOT STACK.** They run one after the other over
the last beat, 1.6s then 1.4s, rather than sitting on the frame together.
Two lavender panels at once on a dense page of text reads as a mistake.

PLACEMENT IS MEASURED AGAINST THE BEAT UNDERNEATH, and preview() in render.py
composites each card onto its own beat before anything is exported.

- b0-budget is the $113,179 headline and the first rows of the table, which
  fill the top half, so the hook sits at y=1180 over the lower rows.
- b4-end carries the 2027 Budget Summary panel high in frame and the closing
  recommendation below it, so both end cards go to y=1120.
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
    "hook-instagram": ("Last year: $107,800.\nTwo vendors already quoted\nnext year higher.", 1180, 46),
    "hook-tiktok":    ("Stop adding 3% to\nlast year's budget.", 1180, 56),
    "take-instagram": ("Start from the quotes\nyou already have.", 1120, 68),
    "take-tiktok":    ("Start from the quotes\nyou already have.", 1120, 68),
    "cta-instagram":  ("Comment BUDGET for the tracker.\n$17 until Monday.", 1120, 50),
    "cta-tiktok":     ("Comment BUDGET on my Instagram.\n$17 until Monday.", 1120, 48),
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
    # The inverted check: this piece is about money, so the CTA belongs, and
    # a code with no deadline is a promise with no end.
    for name in ("cta-instagram", "cta-tiktok"):
        text = CARDS[name][0]
        assert "BUDGET" in text, f"{name} lost the CTA on the one money piece"
        assert "Monday" in text, f"{name} has no deadline on the discount"
    # TikTok has no bio link and the automation lives on Instagram.
    assert "Instagram" in CARDS["cta-tiktok"][0], "the TikTok CTA must name Instagram"
    assert "Instagram" not in CARDS["cta-instagram"][0], "no self-reference on Instagram"
    # The hook has to carry the number, which is what the brief changed.
    assert "$107,800" in CARDS["hook-instagram"][0]

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
