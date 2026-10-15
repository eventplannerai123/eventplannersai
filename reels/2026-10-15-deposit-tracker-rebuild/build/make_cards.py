"""Hook card for the Sep 3 deposit tracker rebuild.

One overlay only: the approved hook, over the frozen opening frame. The
frame's own content stops at y=866 (measured with cardkit's line finder, not
guessed), so the card sits in the white below it and covers nothing.
"""
import os, sys
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "..", "tools"))
from cardkit import preview   # noqa: E402

W, H = 1080, 1920
FONT = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
OUT = os.path.join(HERE, "cards1015"); os.makedirs(OUT, exist_ok=True)
SAFE_TOP, SAFE_BOT = int(H * 0.12), int(H * 0.75)
FRAME = os.path.join(HERE, "frames", "open.png")


def card(img, lines, fs, cy, name, px=48, py=38, r=30,
         bg=(0, 0, 0, 220), fg=(255, 255, 255, 255)):
    d = ImageDraw.Draw(img, "RGBA")
    f = ImageFont.truetype(FONT, fs); lh = int(fs * 1.28)
    w = [d.textbbox((0, 0), l, font=f)[2] - d.textbbox((0, 0), l, font=f)[0] for l in lines]
    bw = max(w) + px * 2; bh = lh * (len(lines) - 1) + fs + py * 2
    x0, y0 = (W - bw) // 2, cy - bh // 2
    assert y0 >= SAFE_TOP and y0 + bh <= SAFE_BOT, f"{name} outside safe band: {y0}-{y0+bh}"
    assert bw <= W - 40, f"{name} too wide: {bw}"
    d.rounded_rectangle([x0, y0, x0 + bw, y0 + bh], radius=r, fill=bg)
    ty = y0 + py
    for l in lines:
        bb = d.textbbox((0, 0), l, font=f)
        d.text(((W - (bb[2] - bb[0])) // 2 - bb[0], ty - bb[1]), l, font=f, fill=fg)
        ty += lh
    print(f"  card {name}: y {y0}-{y0+bh}, w {bw}")


hook = Image.new("RGBA", (W, H), (0, 0, 0, 0))
card(hook, ["A missed vendor balance date",
            "is survivable.",
            "Going quiet isn't."], 56, 1180, "hook")
hook.save(f"{OUT}/hook.png")

preview([FRAME], [f"{OUT}/hook.png"], os.path.join(HERE, "preview.png"))
