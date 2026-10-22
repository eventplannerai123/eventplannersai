"""Hook card for Rebuild 4 — the Sep 26 staffing-plan Reel.

The approved hook (Sahiba, Oct 16: "a is good"):

    Four staff, six sessions, one block you're short.

It replaces "Six sessions. Three rooms. Four staff." — three numbers and no
stake. The new one leads with what the output actually delivers, because the
prompt ends "flag any block where we're short" and the answer's verdict is
"staffable with four people, but—".

THE CARD SITS OVER THE KEYBOARD, NOT THE PROMPT. The opening frame is the
prompt in the box (video rule 2: never cut the prompt), so a card at the old
y=620 would cover the one thing that opening exists to show — the Sep 29
mistake, recorded in CLAUDE.md, which moved that day's card to y=1300. Same
here: the keyboard carries no information and the card still clears
Instagram's bottom furniture.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "cards")
os.makedirs(OUT, exist_ok=True)

W, H = 1080, 1920
FONT = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
SAFE_TOP, SAFE_BOT = int(H * 0.12), int(H * 0.75)   # 230 .. 1440

HOOK = ["Four staff, six sessions,", "one block you're short."]
HOOK_FLAT = "Four staff, six sessions, one block you're short."


def card(lines, fs, cy, name, px=50, py=44, r=34,
         bg=(0, 0, 0, 225), fg=(255, 255, 255, 255)):
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    f = ImageFont.truetype(FONT, fs)
    lh = int(fs * 1.30)
    widths = [d.textbbox((0, 0), l, font=f)[2] - d.textbbox((0, 0), l, font=f)[0]
              for l in lines]
    bw = max(widths) + px * 2
    bh = lh * (len(lines) - 1) + fs + py * 2
    x0, y0 = (W - bw) // 2, cy - bh // 2

    assert " ".join(lines) == HOOK_FLAT, "hook text drifted from the approved line"
    assert y0 >= SAFE_TOP, f"card starts at {y0}, inside the top 12%"
    assert y0 + bh <= SAFE_BOT, f"card ends at {y0+bh}, inside the bottom 25%"
    assert bw <= W - 64, f"card too wide: {bw}"

    d.rounded_rectangle([x0, y0, x0 + bw, y0 + bh], radius=r, fill=bg)
    ty = y0 + py
    for l in lines:
        bb = d.textbbox((0, 0), l, font=f)
        d.text(((W - (bb[2] - bb[0])) // 2 - bb[0], ty - bb[1]), l, font=f, fill=fg)
        ty += lh
    img.save(os.path.join(OUT, name))
    print(f"{name}: y {y0}-{y0+bh}, w {bw}, inside the safe band {SAFE_TOP}-{SAFE_BOT}")


if __name__ == "__main__":
    card(HOOK, 58, 1300, "hook.png")
