"""Five freeze frames from her Sat 14 recording of the BEO redo.

THE RECORDING IS NOT IN THIS REPO. 107 MB of her screen, read from the
scratchpad path in $BEO_SRC. Drive id 1MP4mDoSs0WT6PCqtJc1_4Tsre1mKx-dU, in
November 17.

Crop recomputed from the source: 1206x2622 iPhone capture, 60fps, no rotation
side data, so 1206/0.5625 = 2144 tall, 478 off the top.

**40 SECONDS, WHICH IS THE SHORTEST SOURCE SO FAR** and it is still enough,
because the answer came back as a downloadable one-page document rather than
a long inline reply: the prompt and the BEO are the first 15 seconds, and the
finished run sheet is the last 10.

**THE ANSWER IS A WIDE LANDSCAPE TABLE INSIDE A 9:16 FRAME**, so each beat is
a different horizontal scroll position of the same document rather than a
different part of a reply. That is why b0, b3 and b4 are all the run sheet:
TIME/ACTIVITY/ROOM/HEADCOUNT at 1960, the vendor block at 2140, and the
RESPONSIBLE/LEAD column at 2260. Each one is legible at 1080 wide; none of
them is legible if you take the whole table.

**IT OPENS ON THE FINISHED SHEET, NOT THE UPLOAD** — the Tue 17 brief says
so, the same inversion as Mon 16, and for the same reason.

THE BRIEF'S PREDICTED TWIST DID NOT HAPPEN. It expected the answer to keep
the BEO's own page order so the 6am load-in would land after dinner; it did
not — the timeline starts at 5:45am and runs in clock order to 11:45pm. Her
catch is a different one, and it is on b4.
"""
import os
import subprocess
import sys

sys.path.insert(0, os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "tools"))
from cardkit import fit_highlight, draw_highlight   # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "build", "beats")
SRC = os.environ["BEO_SRC"]

CROP = "crop=1206:2144:0:478,scale=1080:1920:flags=lanczos"

BEATS = [
    ("b0-runsheet",  1960),  # TIMELINE: 5:45am to 2:00pm, room and headcount
    ("b1-prompt",      40),  # the whole prompt, PDF chip above it
    ("b2-fourteen",   120),  # BEO page 1: the 14-item contents, "Page 1 of 14",
                             # and a vendor number sitting in the page footer
    ("b3-vendors",   2140),  # VENDOR / CONTACT / PHONE, all four
    ("b4-blanks",    2260),  # RESPONSIBLE / LEAD: four "not named in BEO" rows
]

# ONE HIGHLIGHT, ON THE TWIST BEAT, BAKED IN. "Room reset team not named in
# BEO" sits at about y=635 on b4 and is the line the last voiceover sentence
# lands on. Baked rather than overlaid because every beat carries a 4% push.
HIGHLIGHTS = {"b4-blanks": dict(seed_y=635, lines=1)}
SAFE_TOP, SAFE_BOT = 231, 1440


def main():
    os.makedirs(OUT, exist_ok=True)
    frames = [n for _, n in BEATS]
    assert len(set(frames)) == len(frames), frames
    order = sorted(range(len(BEATS)), key=lambda i: frames[i])
    expr = "+".join(f"eq(n\\,{n})" for n in sorted(frames))
    tmp = os.path.join(OUT, "_pass%02d.png")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", SRC,
                    "-vf", f"select='{expr}',{CROP}", "-vsync", "0", tmp],
                   check=True)
    got = sorted(f for f in os.listdir(OUT) if f.startswith("_pass"))
    assert len(got) == len(BEATS), f"{len(got)} frames came out, not {len(BEATS)}"

    for slot, i in enumerate(order, start=1):
        name, n = BEATS[i]
        os.replace(os.path.join(OUT, f"_pass{slot:02d}.png"),
                   os.path.join(OUT, f"{name}.png"))
        print(f"{name:13s} frame {n}  t={n / 60:6.2f}s")

    from PIL import Image
    for name, spec in HIGHLIGHTS.items():
        path = os.path.join(OUT, name + ".png")
        box = fit_highlight(path, name=name, **spec)
        img = Image.open(path).convert("RGB")
        draw_highlight(img, box, SAFE_TOP, SAFE_BOT, name=name)
        img.save(path)


if __name__ == "__main__":
    main()
