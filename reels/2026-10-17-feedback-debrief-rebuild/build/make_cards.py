"""Hook cards for the Sep 30 feedback debrief rebuild — both cuts.

One overlay each: the approved hook, over the frozen opening frame.

Placement is measured, not eyeballed. cardkit's line finder reports each
frame's real text lines, and the ones that matter are the three numbered
changes — the whole reason the brief says to open on this frame rather than on
the survey responses. The card must not touch them.

The two cuts have different pacing, so the same content sits at different
heights: the changes are at 1017-1289 in the Instagram frame and 961-1233 in
the TikTok one, about 56px apart. Each card is placed against its own frame's
measurements rather than one number reused across both.

In both, the card sits over the "The survey doesn't suggest that you need to
reinvent the conference" paragraph — context for the changes, not the changes.
"""
import os, sys
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "..", "tools"))
from cardkit import preview, _lines   # noqa: E402

W, H = 1080, 1920
FONT = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
OUT = os.path.join(HERE, "cards"); os.makedirs(OUT, exist_ok=True)
SAFE_TOP, SAFE_BOT = int(H * 0.12), int(H * 0.75)

HOOK = ['Stop saying',
        '"that’s how we did it',
        'last year."']

# (name, frame, where the three changes start, where the card is centred)
CUTS = [
    ("hook",        "open.png",        1017, 480),
    ("hook-tiktok", "open-tiktok.png",  961, 425),
]


def card(img, lines, fs, cy, name, changes_top, px=48, py=38, r=30,
         bg=(0, 0, 0, 220), fg=(255, 255, 255, 255)):
    d = ImageDraw.Draw(img, "RGBA")
    f = ImageFont.truetype(FONT, fs); lh = int(fs * 1.28)
    w = [d.textbbox((0, 0), l, font=f)[2] - d.textbbox((0, 0), l, font=f)[0] for l in lines]
    bw = max(w) + px * 2; bh = lh * (len(lines) - 1) + fs + py * 2
    x0, y0 = (W - bw) // 2, cy - bh // 2
    assert y0 >= SAFE_TOP and y0 + bh <= SAFE_BOT, f"{name} outside safe band: {y0}-{y0+bh}"
    assert bw <= W - 40, f"{name} too wide: {bw}"
    assert y0 + bh < changes_top, \
        f"{name} reaches {y0+bh}, into the three changes at {changes_top}"
    d.rounded_rectangle([x0, y0, x0 + bw, y0 + bh], radius=r, fill=bg)
    ty = y0 + py
    for l in lines:
        bb = d.textbbox((0, 0), l, font=f)
        d.text(((W - (bb[2] - bb[0])) // 2 - bb[0], ty - bb[1]), l, font=f, fill=fg)
        ty += lh
    print(f"  card {name}: y {y0}-{y0+bh}, w {bw} (changes at {changes_top})")


frames, overlays = [], []
for name, frame_file, changes_top, cy in CUTS:
    frame = os.path.join(HERE, "frames", frame_file)
    # The card is placed against measured ink, so fail if the frame moved.
    _, rows = _lines(frame)
    starts = [a for a, b in rows]
    assert changes_top in starts, \
        f"{name}: the three changes no longer start at {changes_top}; found {starts}"
    print(f"  {frame_file}: {len(rows)} text lines, changes block at {changes_top}")

    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    card(img, HOOK, 56, cy, name, changes_top)
    img.save(f"{OUT}/{name}.png")
    frames.append(frame); overlays.append(f"{OUT}/{name}.png")

preview(frames, overlays, os.path.join(HERE, "preview.png"))
print("  preview written (both cuts)")
