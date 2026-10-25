"""Hook cards for the Thu 29 headcount Reel.

Two cuts, two hooks. Instagram keeps the guide's own overlay; TikTok gets the
command-style opening the two-cuts rule asks for.

Placement: the usable span of IMG_1005 is a slow pan along a drinks table, so
the lower two thirds carry the glasses, the orange slices and the framed menu.
The top third is plain curtain and window, which is the only part of the frame
that stays empty for the whole clip — so the card sits at cy=520, below the
12% safe line and well clear of the bottom 25% the caption covers.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "cards")
os.makedirs(OUT, exist_ok=True)

W, H = 1080, 1920
FONT = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
SAFE_TOP, SAFE_BOT = int(H * 0.12), int(H * 0.75)   # 230 .. 1440

CARDS = {
    "hook-instagram.png": ["150 guests.", "Two completely", "different orders."],
    "hook-tiktok.png":    ["Stop giving AI", "just a headcount."],
}


def card(lines, name, fs=72, cy=520, px=52, py=46, r=34,
         bg=(0, 0, 0, 225), fg=(255, 255, 255, 255)):
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    f = ImageFont.truetype(FONT, fs)
    lh = int(fs * 1.28)
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
    for name, lines in CARDS.items():
        card(lines, name)
