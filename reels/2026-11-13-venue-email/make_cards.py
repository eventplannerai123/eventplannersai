"""Overlay cards for the Fri 13 Nov venue-email Reel.

Brand palette: lavender #CECBF6 ground, deep purple #3C3489 text, Poppins 600.
The Instagram hook is the guide's own approved sentence; TikTok takes a
command-style one, as the house rules require.

NO BUDGET LINE ON THIS ONE. The Nov 3 soft mention covers Thu 5, Mon 9, Tue 10
and Tue 17 only, and Tue 10 came off it on Nov 9, so this Reel ends on the
guide's own takeaway overlay: "Read the small print, then ask for the weekday
rate."

PLACEMENT IS MEASURED AGAINST THE BEAT UNDERNEATH, off a y-ruler rather than
guessed, and `preview()` in render.py composites each card onto its own beat
before anything is exported.

THE HOOK SITS LOW AND THE END CARD HIGH, which is the Tue 10 shape rather than
the Thu 12 one, and both are forced by their beats:

- b0-prompt is the only frame in the recording carrying the whole prompt, and
  the prompt is the thing the opening exists to show. It runs y 380-790 with
  the input bar under it, so the card goes on the keyboard at y=1120 — which
  carries no information at all and still clears Instagram's own furniture.
- b4-tip's whole job is the "avoid naming a target price" paragraph at y 1030
  down. Everything above 900 is the tail of the email, which the beat does not
  need, so the card goes there.

CARDS ARE OPAQUE, not the usual 243 alpha, as on Tue 10 and Thu 12: the end
card lands on a dense paragraph, and at 243 the text underneath shows through
the lavender.
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
    # b0-prompt: the prompt runs y 380-790 and the input bar 880-960, so the
    # card takes the keyboard. The whole prompt stays readable, which is the
    # reason the cut opens on this frame rather than on the sent bubble — by
    # the time the bubble is on screen only its last three lines show.
    "hook-instagram": ("This email got $10,000\noff the venue quote.", 1120, 50),
    "hook-tiktok":    ("Stop signing the\nSaturday quote.", 1120, 54),
    # b4-tip: "Negotiation tip: I would avoid naming a target price initially"
    # starts at y=1030 and runs to about 1180. The 4% push lifts it to roughly
    # 953 by the last frame, so the card's floor is 900 rather than 1000.
    "end-instagram":  ("Read the small print, then\nask for the weekday rate.", 250, 54),
    "end-tiktok":     ("Read the small print, then\nask for the weekday rate.", 250, 54),
}
PAD_X, PAD_Y = 44, 34

# What each card must not run into, measured off the beat it sits on.
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
    # Opaque, not the usual 243 — see the module docstring.
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
