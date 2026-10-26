"""Hook card for Rebuild 1 — the Sep 1 post-event ROI report Reel.

The approved hook (Sahiba, Oct 16: "2 is good"):

    If you didn't define success before the event, you can't prove it after.

It replaces "A $85,000 corporate summit just wrapped, and leadership wants
proof it was worth it." — which the brief calls out as a hypothetical, breaking
the true-moment rule, with "proof it was worth it" too abstract to open on.

NO EMPLOYER ANYWHERE. Her answer to the rebuild question named one and she
asked for it kept out of the piece, the caption and the overlay.

Placement: the new opening frame is the finished report, which is dense text
top to bottom, so there is no empty band to aim for. The card sits where the
original's did — cy=560 — which keeps the rebuild's one visible change to the
words rather than the layout.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "cards")
os.makedirs(OUT, exist_ok=True)

W, H = 1080, 1920
FONT = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
SAFE_TOP, SAFE_BOT = int(H * 0.12), int(H * 0.75)   # 230 .. 1440

HOOK = ["If you didn't define success", "before the event, you can't", "prove it after."]
HOOK_FLAT = "If you didn't define success before the event, you can't prove it after."


def card(lines, name, fs=64, cy=560, px=50, py=44, r=34,
         bg=(0, 0, 0, 232), fg=(255, 255, 255, 255)):
    assert " ".join(lines) == HOOK_FLAT, "hook text drifted from the approved line"
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    f = ImageFont.truetype(FONT, fs)
    lh = int(fs * 1.30)
    widths = [d.textbbox((0, 0), l, font=f)[2] - d.textbbox((0, 0), l, font=f)[0]
              for l in lines]
    bw = max(widths) + px * 2
    bh = lh * (len(lines) - 1) + fs + py * 2
    x0, y0 = (W - bw) // 2, cy - bh // 2

    assert y0 >= SAFE_TOP, f"{name}: starts at {y0}, inside the top 12%"
    assert y0 + bh <= SAFE_BOT, f"{name}: ends at {y0+bh}, inside the bottom 25%"
    assert bw <= W - 64, f"{name}: too wide at {bw}"

    d.rounded_rectangle([x0, y0, x0 + bw, y0 + bh], radius=r, fill=bg)
    ty = y0 + py
    for l in lines:
        bb = d.textbbox((0, 0), l, font=f)
        d.text(((W - (bb[2] - bb[0])) // 2 - bb[0], ty - bb[1]), l, font=f, fill=fg)
        ty += lh
    img.save(os.path.join(OUT, name))
    print(f"{name}: y {y0}-{y0+bh}, w {bw}, safe band {SAFE_TOP}-{SAFE_BOT}")


if __name__ == "__main__":
    card(HOOK, "hook.png")
