"""Overlay cards for the Mon 9 Nov catering-invoice Reel.

Brand palette: lavender #CECBF6 ground, deep purple #3C3489 text, Poppins 600.
The Instagram hook is the guide's own sentence; TikTok takes a command-style
one, as the house rules require.

THE END CARD IS THE BUDGET LINE, AND IT SUBSTITUTES. The guide's Nov 3 soft
mention says to end this Reel on "Comment BUDGET for the tracker I use"
*instead of* the usual closing line, so the guide's own takeaway overlay
("Check the invoice against the BEO before you pay it.") is replaced rather
than appended to. TikTok says "on my Instagram": there is no bio link there
and the ManyChat automation lives on Instagram.

PLACEMENT IS MEASURED AGAINST THE BEAT UNDERNEATH, off a y-ruler rather than
guessed, and `preview()` in render.py composites each card onto its own beat
before anything is exported.
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
    # On b0 the prompt bubble ends at y=1180 and the bottom 25% starts at 1440,
    # so the hook has about 260px. It sits at 1190, over the answer's opening
    # sentence rather than over the prompt — the prompt is the whole reason the
    # cut opens on this frame.
    "hook-instagram": ("The catering invoice came in\n$1,140 over the contract.", 1190, 46),
    "hook-tiktok":    ("Stop paying the final\ninvoice on trust.", 1190, 48),
    # b5 carries "Amount to dispute  $530.00" at y=400 and the "Recommended
    # response" heading at 500-580. The beat's 4% push lifts everything about
    # 77px, so a card at 780 still clears the heading on the last frame and
    # covers only the email draft, which is not what this beat is for.
    "end-instagram":  ("Comment BUDGET\nfor the tracker I use", 780, 54),
    "end-tiktok":     ("Comment BUDGET\non my Instagram", 780, 54),
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
