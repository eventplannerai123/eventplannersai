"""Extract every beat's still from her Mon 2 fees recording and fit its highlight.

Freeze frames, not scrolling footage, because the answer is a long scroll and
rule 3 asks for the highlighted line held still. Motion comes from a slow push
at render time instead.

Highlight boxes are fitted with tools/cardkit.fit_highlight from a seed y, never
typed in: the seed picks the line, the frame decides where its ink actually is.
Look at build/preview.png before rendering.
"""
import os
import subprocess
import sys
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
import cardkit  # noqa: E402

B = os.path.join(HERE, "build")
FRAMES = os.path.join(B, "frames")
REC = "/tmp/claude-0/-home-user-eventplannersai/4079a8b4-9eb7-5c73-8b20-b79d77bad268/scratchpad/fees/src.mp4"

CROP = "crop=1206:2144:0:478"       # 1206/0.5625 = 2144; 478 off the top
SAFE_TOP, SAFE_BOT = 257, 1608      # top 12% and bottom 25% of the 2144 frame

# source time -> (name, highlight or None)
# highlight = (seed_y, lines, up)
BEATS = {
    3.0:  ("prompt",   None),
    5.2:  ("proposal", None),    # page 1, "$185 per person"
    22.5: ("fees",     None),    # all eight fees outside the rate
    28.0: ("details",  (632, 3, 0)),   # the admin fee is NOT a gratuity
    32.0: ("bill",     (900, 2, 1)),   # REAL COST PER PERSON $253.40
    36.0: ("real",     (576, 3, 1)),   # with the linen upgrade: $47,062 / $261.46
    39.5: ("take",     (916, 2, 0)),   # "I would budget $46,000-$47,000"
}


def main():
    os.makedirs(FRAMES, exist_ok=True)
    plain, marked = [], []
    for t, (name, hl) in sorted(BEATS.items()):
        raw = os.path.join(FRAMES, f"{name}.png")
        subprocess.run(["ffmpeg", "-v", "error", "-ss", str(t), "-i", REC,
                        "-frames:v", "1", "-vf", CROP, raw, "-y"], check=True)
        out = os.path.join(FRAMES, f"{name}-hl.png")
        img = Image.open(raw).convert("RGB")
        if hl:
            seed, lines, up = hl
            box = cardkit.fit_highlight(raw, seed, lines=lines, up=up, name=name)
            cardkit.draw_highlight(img, box, SAFE_TOP, SAFE_BOT, name=name)
        img.save(out)
        plain.append(raw)
        marked.append(out)
        print(f"  {t:5.1f}s {name}")
    # preview: the marked frames side by side, which is the check that catches
    # a box on the wrong line before an export is burned
    tiles = [Image.open(p).convert("RGB").resize((320, 569)) for p in marked]
    sheet = Image.new("RGB", (320 * len(tiles), 569), "white")
    for i, t in enumerate(tiles):
        sheet.paste(t, (i * 320, 0))
    sheet.save(os.path.join(B, "preview.png"))
    print("  preview ->", os.path.join(B, "preview.png"))


if __name__ == "__main__":
    main()
