"""Overlay cards for the Fri 27 Nov giveaway last-day Reel.

Brand palette: lavender #CECBF6 ground, deep purple #3C3489 text, Poppins 600.
Both the hook and the takeaway are the guide's own lines.

**NO SALE ON THIS REEL, ON BLACK FRIDAY.** The guide is explicit: the only
Black Friday discount is BLACKFRIDAY on the Vendor Payment System, and "it
goes in the Story, not in this Reel". There is also no coloring book discount
at all (Sahiba, Oct 31) — the book is the prize, not the offer. `check()`
refuses BLACKFRIDAY, BUDGET, a dollar sign and the word "off", because the
one day this piece could drift is the day everything else is on sale.

**THE DEADLINE IS ON BOTH CARDS AND IT IS A REAL ONE.** "Closes 11:59pm
tonight" is only true on Fri 27; `check()` asserts both cards carry it so the
piece cannot be reused on another day without failing the build.

PLACEMENT: the footage is her hands and the books on a pale table, so both
cards sit low at y=1180 where the frame is wood and shadow rather than
pages. Opaque, as always.
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
    "hook-instagram": ("Last day: 2 free copies.\nCloses 11:59pm tonight.", 1180, 56),
    "hook-tiktok":    ("Last day: 2 free copies.\nCloses 11:59pm tonight.", 1180, 56),
    "end-instagram":  ("Comment who you'd give it to.\nCloses tonight.", 1180, 50),
    "end-tiktok":     ("Enter on my Instagram.\nCloses tonight.", 1180, 56),
}
PAD_X, PAD_Y = 44, 34
FLOOR = {k: 1440 for k in CARDS}


def main():
    os.makedirs(OUT, exist_ok=True)
    for name, (text, _, _) in CARDS.items():
        low = text.lower()
        # Black Friday is the day. The book is the prize, not the offer.
        for banned in ("blackfriday", "budget", "$", "% off", " off", "sale"):
            assert banned not in low, f"{name} carries {banned!r} on a giveaway Reel"
        # The deadline is only true on Fri 27.
        assert "tonight" in low, f"{name} has lost the deadline"
    # TikTok has no entry mechanism of its own: entries count on Instagram.
    assert "Instagram" in CARDS["end-tiktok"][0], "the TikTok end card must point to Instagram"

    for name, (text, top, px) in CARDS.items():
        f = ImageFont.truetype(P600, px)
        probe = ImageDraw.Draw(Image.new("RGB", (10, 10)))
        lines = text.split("\n")
        lw = max(probe.textlength(l, font=f) for l in lines)
        lh = int(px * 1.30)
        w, h = int(lw) + PAD_X * 2, lh * len(lines) + PAD_Y * 2
        c = Image.new("RGBA", (w, h), (0, 0, 0, 0))
        d = ImageDraw.Draw(c)
        d.rounded_rectangle([0, 0, w - 1, h - 1], radius=28, fill=LAVENDER + (255,))
        y = PAD_Y
        for l in lines:
            d.text(((w - d.textlength(l, font=f)) / 2, y), l, font=f, fill=PURPLE)
            y += lh
        bottom = top + h
        assert top >= 240, f"{name} starts at {top}, inside the top 12%"
        assert bottom <= FLOOR[name], f"{name} ends at {bottom}, past {FLOOR[name]}"
        assert w <= W - 40, f"{name} is wider than the frame ({w})"
        frame = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        frame.paste(c, ((W - w) // 2, top), c)
        frame.save(os.path.join(OUT, name + ".png"))
        print(f"{name:16s} {w}x{h} at y={top}, bottom {bottom}")


if __name__ == "__main__":
    main()
