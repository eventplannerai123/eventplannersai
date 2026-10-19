"""Text overlays for the Mon 19 "girls at the door" reel.

The brief: no voiceover, so the overlays carry the whole story alone. That is
the Oct 5 rule-1 exception for an overlay-led piece, not a silent quick piece.

Four cards, each held long enough to read:

  0.0-4.0   the gossip-blog line
  4.0-7.0   "I was one of the girls at the door."
  7.0-11.0  "Here's how I'd fix that guest list today."
  11.0-15.0 the prompt

The brief writes the last two as 7-12 and a 3-second prompt hold. The prompt
gets 4 seconds here instead, taken off the line before it, because 3 seconds
cannot carry a readable prompt — see PROMPT below. The full prompt is in the
caption either way.

Safe zones (Oct 5 rule 4): nothing important in the top 12% (y<230), the
bottom 25% (y>1440) or the right 15%. Every card is centred inside 260-1400
and the assert at the bottom of card() enforces it rather than trusting the
numbers typed here.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "cards")
os.makedirs(OUT, exist_ok=True)

FONT = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
W, H = 1080, 1920
SAFE_TOP, SAFE_BOT = int(H * 0.135), int(H * 0.73)   # 259 .. 1401

# The on-screen prompt is a condensed version. The caption carries it in full:
# "Match these two lists. Flag every RSVP that wasn't on the invite list, every
# duplicate, and every plus-one over the limit. Then give me a door list sorted
# by company, with the person who approved each guest." That is ~45 words, and
# nobody reads 45 words in four seconds while also looking at the room. So the
# card states what the prompt DOES, in 16 words, and the caption states it in
# full. Nothing is hidden: the viewer gets the whole thing one scroll down.
CARDS = [
    ("01-blog", 60, 820, [
        "A gossip blog once said",
        "the girls at the door were",
        "“in way over their heads.”",
    ]),
    ("02-me", 68, 860, [
        "I was one of",
        "the girls at the door.",
    ]),
    ("03-today", 62, 840, [
        "Here’s how I’d fix",
        "that guest list today.",
    ]),
    ("04-prompt", 50, 800, [
        "Match the invite list",
        "to the RSVP list.",
        "Flag every name that",
        "shouldn’t be there,",
        "every duplicate, every",
        "plus-one over the limit.",
    ]),
]


def card(name, fs, cy, lines, px=56, py=44, r=32,
         bg=(0, 0, 0, 215), fg=(255, 255, 255, 255)):
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img, "RGBA")
    f = ImageFont.truetype(FONT, fs)
    lh = int(fs * 1.34)

    widths = []
    for l in lines:
        bb = d.textbbox((0, 0), l, font=f)
        widths.append(bb[2] - bb[0])
    bw = max(widths) + px * 2
    bh = lh * (len(lines) - 1) + fs + py * 2
    x0, y0 = (W - bw) // 2, cy - bh // 2

    assert y0 >= SAFE_TOP, f"{name} starts at {y0}, above the safe band {SAFE_TOP}"
    assert y0 + bh <= SAFE_BOT, f"{name} ends at {y0+bh}, below the safe band {SAFE_BOT}"
    assert bw <= W - 72, f"{name} too wide: {bw}"

    d.rounded_rectangle([x0, y0, x0 + bw, y0 + bh], radius=r, fill=bg)
    ty = y0 + py
    for l in lines:
        bb = d.textbbox((0, 0), l, font=f)
        d.text(((W - (bb[2] - bb[0])) // 2 - bb[0], ty - bb[1]), l, font=f, fill=fg)
        ty += lh

    img.save(f"{OUT}/{name}.png")
    print(f"  {name}: y {y0}-{y0+bh}, w {bw}, {len(lines)} lines @ {fs}px")


if __name__ == "__main__":
    for name, fs, cy, lines in CARDS:
        card(name, fs, cy, lines)
    print("  all four cards inside the safe band")
