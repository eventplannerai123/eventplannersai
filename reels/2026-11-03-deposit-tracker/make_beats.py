"""Extract every beat's still from her recording and fit its highlight.

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
REC = "/tmp/claude-0/-home-user-eventplannersai/4079a8b4-9eb7-5c73-8b20-b79d77bad268/scratchpad/deposit/src.mp4"

CROP = "crop=1206:2144:0:478"       # 1206/0.5625 = 2144; 478 off the top
SAFE_TOP, SAFE_BOT = 257, 1608      # top 12% and bottom 25% of the 2144 frame

# source time -> (name, highlight or None)
# highlight = (seed_y, lines, up)
BEATS = {
    2.0:  ("prompt",    None),
    7.0:  ("sheet",     None),
    15.0: ("totals",    (960, 2, 1)),    # "Still owed" and "$46,715"
    17.6: ("chrono",    (473, 1, 0)),    # the Nov 1 transportation row
    19.6: ("chrono2",   None),
    21.4: ("relative",  (440, 1, 0)),    # the band, due on the wedding day
    23.0: ("priority",  (1440, 2, 1)),   # "Total due in next 30 days" / $7,350
    29.5: ("catering",  (708, 1, 0)),    # "My biggest concern is catering."
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
