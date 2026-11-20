"""Overlay cards for the Mon 23 Nov RSVP-redo Reel.

Brand palette: lavender #CECBF6 ground, deep purple #3C3489 text, Poppins 600.
The Instagram hook is the guide's own overlay line; TikTok takes a
command-style one.

**NO BUDGET LINE, AND THE ASSERT KEEPS IT THAT WAY.** This is a catering
piece, not a money one. The guide's Mon 23 takeaway line says so in as many
words, and the Nov 14 rule — check the closing line against the piece — is
what the assert below enforces, copied from the Tue 17 generator after she
caught a tracker CTA on an insurance piece and again on a run-sheet one.

**THE END CARD IS THE CATCH, REWRITTEN.** The brief's planned takeaway was
"Send the caterer the conflicts, not just the counts." It still closes the
caption. On screen it is the number instead, because the number IS what the
answer did: it would not call the order 142, since six plus-ones never chose,
so the room is 148. The brief's own twist line asks for the overlay to be
rewritten around what she actually catches, and that is this.

PLACEMENT IS MEASURED AGAINST THE BEAT UNDERNEATH, and `preview()` in
render.py composites each card onto its own beat before anything is exported.

- b0-counts is the meal-count table and its bar chart, which fill the top
  third and are the payoff, so the hook sits below them at y=1220, over
  "There are 23 guests with dietary notes, grouped below by restriction" —
  a line b2 shows properly.
- b4-recommend ends on "My recommendation: Don't finalize the order at 142
  meals just yet", which is the whole beat, so the end card goes low at
  y=1140 over the closing "I would use this as the working catering report"
  paragraph.

CARDS ARE OPAQUE: both land on dense black body text.
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
    "hook-instagram": ("142 RSVPs. 23 dietary notes,\nwritten 14 different ways.", 1220, 46),
    "hook-tiktok":    ("Stop sending the caterer\none number.", 1220, 54),
    "end-instagram":  ("142 meals.\n148 people.", 1140, 76),
    "end-tiktok":     ("142 meals.\n148 people.", 1140, 76),
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
    # A catering piece carries no tracker CTA. Her Nov 14 rule, and the two
    # times it was caught on a rendered video are the reason this is an assert
    # rather than a note.
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
