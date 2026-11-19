"""Fri 20 Nov — the one overlay on the coloring timelapse.

**NO VOICEOVER ON THIS PIECE — her instruction, Nov 19: "remove the voice from
the coloring picture."** The Fri 20 block specified a 30-word Eryn script; it
is not used. That leaves the overlay carrying what the voice would have said,
which is the Oct 5 rule for an overlay-led piece, so the piece keeps one band
and nothing else. The caption does the rest.

The line is the first line of the script she cut, so the words are still hers.

The band sits high, over her shoulder rather than over the page, and clears
the top 12% where TikTok's own furniture sits.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "build", "cards")
FONTS = os.path.join(HERE, "build", "fonts")

W, H = 1080, 1920
LAVENDER = (206, 203, 246)
PURPLE = (60, 52, 137)

P700 = os.path.join(FONTS, "Poppins-700.ttf")
F = lambda p, s: ImageFont.truetype(p, s)

M = 72
HOOK = "One page,\nstart to finish."
BAND_TOP = 250


def hook_card():
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    f = F(P700, 78)
    lines = HOOK.split("\n")
    step = int(78 * 1.22)
    pad = 46
    bh = len(lines) * step + pad * 2 - int(78 * 0.22)
    d.rounded_rectangle([M - 28, BAND_TOP, W - M + 28, BAND_TOP + bh],
                        radius=34, fill=LAVENDER + (242,))
    y = BAND_TOP + pad - 8
    for ln in lines:
        d.text(((W - d.textlength(ln, font=f)) / 2, y), ln, font=f, fill=PURPLE)
        y += step
    return img


def check():
    assert BAND_TOP >= int(H * 0.12), "the band must clear the top 12%"
    # One overlay only: with no voice, a second card would be the whole piece.
    assert HOOK.count("\n") == 1, "two lines, one band"
    for banned in ("comment", "link in bio", "budget", "prompt"):
        assert banned not in HOOK.lower(), f"no CTA on the band: {banned!r}"
    print("checks pass: one band, two lines, no CTA, clears the top 12%")


def main():
    check()
    os.makedirs(OUT, exist_ok=True)
    hook_card().save(os.path.join(OUT, "hook.png"))
    print("hook.png")


if __name__ == "__main__":
    main()
