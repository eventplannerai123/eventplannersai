"""Overlay cards for the Thu 5 Nov Vendor Payment System launch Reel.

The Instagram hook and the two later cards are the guide's own words from the
THU 5 NOV block. TikTok takes a command-style hook instead, as the house rules
require — the two cuts never share one.

PLACEMENT IS MEASURED AGAINST THE BEAT UNDERNEATH, never reused from the last
build. Every card's bottom clears y=1440, the top of the bottom 25% that
TikTok's caption and buttons cover, and `preview()` in render.py composites
each one onto its own beat so a bad y is caught before an export rather than
after.

  hook      sits over the tracker's amount column, low enough to leave the
            dollar figures and the November due dates in clear view
  contract  sits ABOVE the clause panel, not on it (her note, Nov 3). The
            panel's top edge is y=840, so the card ends at 772 and nothing it
            says covers the sentence it is about
  end       sits over the prompt bubble, covering the keyboard rather than
            the prompt

TIKTOK TAKES A DIFFERENT CTA AND A FULL-FRAME END CARD (her note, Nov 3).
TikTok has no bio link — the account is 900 followers short of the website
field and the business route wants tax documents — so the URL has to be in the
picture. `end-tiktok` names Instagram as the place to comment, and
`url-tiktok` is a full lavender frame carrying the address alone, held two
seconds after the voiceover ends. Instagram keeps the shorter CTA and no URL
card: its link lives in the bio.
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
    "hook-instagram": ("Eight vendor emails in.\nEvery payment date out.", 1086, 58),
    "hook-tiktok":    ("Stop keeping vendor\npayments in your head.", 1086, 60),
    "contract":       ("The email said 10 days.\nThe contract says\n10 business days.", 494, 54),
    "end":            ("Comment BUDGET and\nI'll send it to you.", 1120, 60),
    "end-tiktok":     ("Comment BUDGET\non my Instagram and\nI'll send it to you.", 1086, 54),
}

# Full-frame end card, TikTok only: lavender ground, the address alone, sized
# to fill the frame rather than typed at a fixed px.
# Two lines, split at the dot: on one line the address fits only at 57px,
# which is smaller than the hook cards. Split, it sets at nearly twice that
# and still reads as one address.
URL = ["aiforeventplanners", ".gumroad.com"]
URL_MAX_W = 992          # 1080 less a 44px gutter either side
URL_Y = 880              # optical centre, clear of the top 12% and bottom 25%
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


def url_card():
    """The address at the largest size that still clears the gutters."""
    probe = ImageDraw.Draw(Image.new("RGB", (10, 10)))
    px = 40
    while px < 220:
        f = ImageFont.truetype(P600, px + 1)
        if max(probe.textlength(l, font=f) for l in URL) > URL_MAX_W:
            break
        px += 1
    f = ImageFont.truetype(P600, px)
    lh = int(px * 1.16)
    img = Image.new("RGB", (W, H), LAVENDER)
    d = ImageDraw.Draw(img)
    widest = max(d.textlength(l, font=f) for l in URL)
    assert widest <= URL_MAX_W, f"url overflows: {widest:.0f}px"
    top = URL_Y - (lh * len(URL)) // 2
    assert top > H * 0.12 and top + lh * len(URL) < H * 0.75, "url card hits a safe zone"
    for i, l in enumerate(URL):
        d.text(((W - d.textlength(l, font=f)) / 2, top + i * lh), l, font=f, fill=PURPLE)
    return img, px, int(widest)


def main():
    os.makedirs(OUT, exist_ok=True)
    for name, (text, top, px) in CARDS.items():
        c = card(text, px)
        assert top + c.size[1] <= 1440, (
            f"{name} runs into the bottom 25%: ends at {top + c.size[1]}")
        assert c.size[0] <= W - 40, f"{name} is wider than the frame"
        frame = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        frame.paste(c, ((W - c.size[0]) // 2, top), c)
        frame.save(os.path.join(OUT, name + ".png"))
        print(f"{name:16s} {c.size[0]}x{c.size[1]} at y={top}, bottom {top + c.size[1]}")

    img, px, w = url_card()
    img.save(os.path.join(OUT, "url-tiktok.png"))
    print(f"{'url-tiktok':16s} full frame, {URL!r} at {px}px, {w}px wide")


if __name__ == "__main__":
    main()
