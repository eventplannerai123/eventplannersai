"""Overlays for the Oct 15 annoyed-email quick piece.

First build to use tools/cardkit.py rather than typed coordinates: each
highlight is given a seed y and a line count, and snaps to the real ink.
`preview()` writes a composite of every overlay on its own beat frame —
look at that before rendering.
"""
import os, sys
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "..", "tools"))
from cardkit import fit_highlight, draw_highlight, preview   # noqa: E402

W, H = 1080, 1920
FONT = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
OUT = os.path.join(HERE, "cards1015"); os.makedirs(OUT, exist_ok=True)
FRM = os.path.join(HERE, "frames")
SAFE_TOP, SAFE_BOT = int(H * 0.12), int(H * 0.75)


def canvas():
    return Image.new("RGBA", (W, H), (0, 0, 0, 0))


def card(img, lines, fs, cy, name, px=48, py=38, r=30,
         bg=(0, 0, 0, 220), fg=(255, 255, 255, 255)):
    d = ImageDraw.Draw(img, "RGBA")
    f = ImageFont.truetype(FONT, fs); lh = int(fs * 1.28)
    w = [d.textbbox((0, 0), l, font=f)[2] - d.textbbox((0, 0), l, font=f)[0] for l in lines]
    bw = max(w) + px * 2; bh = lh * (len(lines) - 1) + fs + py * 2
    x0, y0 = (W - bw) // 2, cy - bh // 2
    assert y0 >= SAFE_TOP and y0 + bh <= SAFE_BOT, f"{name} card outside safe band: {y0}-{y0+bh}"
    d.rounded_rectangle([x0, y0, x0 + bw, y0 + bh], radius=r, fill=bg)
    ty = y0 + py
    for l in lines:
        bb = d.textbbox((0, 0), l, font=f)
        d.text(((W - (bb[2] - bb[0])) // 2 - bb[0], ty - bb[1]), l, font=f, fill=fg)
        ty += lh
    print(f"  card {name}: y {y0}-{y0+bh}")


FRAMES = [f"{FRM}/b0.5.png", f"{FRM}/b5.5.png", f"{FRM}/b9.7.png", f"{FRM}/b12.4.png"]
ovs = []

# Beat 1: the hook, in the white space above the prompt box (which starts ~520).
print("beat 1")
b1 = canvas()
card(b1, ["Stop sending the email", "you wrote angry."], 60, 350, "hook")
b1.save(f"{OUT}/b1.png"); ovs.append(f"{OUT}/b1.png")

# Beat 2: the line that would have cost her the vendor.
print("beat 2")
b2 = canvas()
draw_highlight(b2, fit_highlight(FRAMES[1], 900, lines=2, name="honestly don't understand"),
               SAFE_TOP, SAFE_BOT, "contempt line")
b2.save(f"{OUT}/b2.png"); ovs.append(f"{OUT}/b2.png")

# Beat 3: the same consequence, kept, in the rewrite. The whole paragraph —
# a 3-line slice of it starts mid-sentence, which is what the first preview
# caught. At t=9.7 all six lines sit inside the safe band; at 10.5 they do not.
print("beat 3")
b3 = canvas()
draw_highlight(b3, fit_highlight(FRAMES[2], 900, lines=6, up=1, name="deadline + invoice, kept"),
               SAFE_TOP, SAFE_BOT, "firm consequence")
b3.save(f"{OUT}/b3.png"); ovs.append(f"{OUT}/b3.png")

# Beat 4: the takeaway, over the end of the rewrite, dimmed.
print("beat 4")
b4 = canvas()
ImageDraw.Draw(b4, "RGBA").rectangle([0, 0, W, H], fill=(0, 0, 0, 155))
card(b4, ["The deadline stayed.", "The invoice line stayed.", "Only the sarcasm went."],
     66, 850, "takeaway")
b4.save(f"{OUT}/b4.png"); ovs.append(f"{OUT}/b4.png")

preview(FRAMES, ovs, os.path.join(HERE, "preview.png"))
