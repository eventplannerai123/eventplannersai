"""Hook overlays for the Fri 23 ticket-allocation Reel.

Two cuts, two hooks. The brief gives the Instagram one verbatim; the TikTok one
is this session's, because the house rule is that TikTok takes a genuinely
different command-style hook rather than a derivative of the Instagram line.

Both name a number immediately, which is the hook rule — abstract superlatives
and vague teases both measured badly.

TWO overlays per cut, which is the written default rather than the October
briefs' usual one. The Oct 14 review added a twist test to this piece: show the
answer, then the one line she would still change. That line needs to be on
screen at the end, so the takeaway card earns its place here where the recent
briefs drop it. It is not an end card asking for a comment — it is the payoff.

HER CATCH, 2026-10-23, verbatim: "I don't like the answer. It should highlight
clients and prospects as well as internal departments." The demand sheet splits
2,000 tickets six ways between internal departments, and the answer allocates
the same way; the people actually in those seats are clients and prospects, and
that cut never appears. The takeaway card is her point in her terms.

Safe zones (Oct 5 rule 4): nothing important in the top 12%, the bottom 25% or
the right 15%. The card is centred inside 260-1400 and the assert enforces it
rather than trusting the number typed here.

THE y IS NOT AUTOMATIC. The cut opens on the finished allocation table, so the
card is placed low, under the table's own heading rows, rather than at the
usual 620 where it would sit across the numbers the shot exists to show. Check
it against the real opening frames once her recording lands, and move it if the
table sits differently.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "cards")
os.makedirs(OUT, exist_ok=True)

W, H = 1080, 1920
FONT = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
SAFE_TOP, SAFE_BOT = int(H * 0.135), int(H * 0.73)   # 259 .. 1401

CARDS = [
    # (name, font size, centre y, lines)
    ("hook-instagram", 60, 1240, ["2,000 tickets.", "Every department", "wanted more."]),
    ("hook-tiktok",    58, 1240, ["Stop splitting", "2,000 tickets by", "who emails first."]),
    # The takeaway, held over the last beat. Her catch, in her terms.
    ("takeaway",       64,  900, ["Departments don't", "sit in the seats.", "Clients do."]),
]


def card(name, fs, cy, lines, px=54, py=44, r=32,
         bg=(0, 0, 0, 215), fg=(255, 255, 255, 255)):
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img, "RGBA")
    f = ImageFont.truetype(FONT, fs)
    lh = int(fs * 1.32)
    widths = [d.textbbox((0, 0), l, font=f)[2] - d.textbbox((0, 0), l, font=f)[0]
              for l in lines]
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
    img.save(os.path.join(OUT, name + ".png"))
    print(f"{name}: y {y0}-{y0+bh}, w {bw}, {len(lines)} lines @ {fs}px")


if __name__ == "__main__":
    for name, fs, cy, lines in CARDS:
        card(name, fs, cy, lines)
    print("both hooks inside the safe band")
