"""Hook cards for the Oct 16 AI-makes-mistakes Reel.

One overlay per cut, nothing else — the guide's brief specifies a hook at
0:00-0:03 and no end card.

Placement: the chart's head-table rows run y 380-990 and they are what the
hook is ABOUT (CEO, CFO, Board Chair). So the card sits below them, over the
Table 2 rows, and the people the line refers to stay on screen behind it.
"""
import os, sys
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "..", "tools"))
from cardkit import preview   # noqa: E402

W, H = 1080, 1920
FONT = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
OUT = os.path.join(HERE, "cards1016"); os.makedirs(OUT, exist_ok=True)
SAFE_TOP, SAFE_BOT = int(H * 0.12), int(H * 0.75)
FRAME = os.path.join(HERE, "chart-probe.png")


def card(img, lines, fs, cy, name, px=46, py=36, r=28,
         bg=(0, 0, 0, 225), fg=(255, 255, 255, 255)):
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
    print(f"  {name}: y {y0}-{y0+bh}, w {bw}")


CUTS = {
    # Instagram takes the guide's wording verbatim; TikTok the command-style
    # hook the two-cuts rule asks for.
    "instagram": ["AI doesn't know which two", "execs can't sit together."],
    "tiktok":    ["Stop letting AI do", "your VIP seating."],
}

ovs = []
for tag, lines in CUTS.items():
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    card(img, lines, 58, 1250, f"hook-{tag}")
    p = f"{OUT}/hook-{tag}.png"
    img.save(p); ovs.append(p)

preview([FRAME, FRAME], ovs, os.path.join(HERE, "preview.png"))
