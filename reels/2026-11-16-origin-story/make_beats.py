"""Five freeze frames from her Sat 14 recording of the name-tag cleanup.

THE RECORDING IS NOT IN THIS REPO. 221 MB of her screen, read from the
scratchpad path in $ORIGIN_SRC; the repo is public and only finished cuts
belong in it. Drive id 1HkHM0UZ29yaRELapepWO4qfZgoLO2lpk, in November 16.

Crop recomputed from the source: 1206x2622 iPhone capture, 60fps, no rotation
side data, so 1206/0.5625 = 2144 tall and 478 off the top for the status bar
and the red recording dot.

**SHE UPLOADED THE EXPORT AS A 53-PAGE PDF, NOT THE GOOGLE SHEET.** The guide
built it as a Sheet and the answer says "the full 53-page registration
export", so she printed or exported it on the way in. It cost about a minute
of "Extracting text from registration PDF" and "Inspecting and Repairing
Truncated PDF Records" — the whole middle of a 127-second recording — and the
answer still came back complete and correct. Worth knowing before the Tue 17
BEO redo, which is a PDF by design.

THE ANSWER RUNS 1m 27s AND THE USABLE PART IS THE LAST 22 SECONDS. Frames
6260 to 7580 are the answer being scrolled; everything before that is the
upload and the spinner. So the beats are packed into a narrow window and
there is no slack to move one.

**THIS PIECE OPENS ON THE PAYOFF, NOT THE PROMPT**, which inverts the Oct 5
rule 2 on purpose: the Mon 16 brief says "Open on the finished, coded list,
not the upload", because it is her origin story rather than a demo — her
words lead and the screen follows. The prompt is still in the cut, second,
and still in the caption. A day's brief overrides the standing rule; nothing
here cuts the prompt.

THE WHOLE PROMPT IS IN THE SENT BUBBLE, not the input box — the opposite of
Fri 13. By the time she sends it the input box has scrolled and shows only
the back half, so b1 is taken from the loading phase, where the bubble sits
complete with the PDF chip above it.
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
SRC = os.environ["ORIGIN_SRC"]

CROP = "crop=1206:2144:0:478,scale=1080:1920:flags=lanczos"

# Frame numbers, not timestamps: at 60fps a 0.02s window spans one or two
# frames and silently picks the wrong picture.
BEATS = [
    ("b0-codes",      6700),   # the five codes: 2,540 / 510 / 96 / 162 / 80
    ("b1-prompt",     1200),   # the whole prompt in the sent bubble, PDF chip above
    ("b2-duplicates", 6360),   # 3,500 in, 112 removed, 3,388 out, 35 variations
    ("b3-orgs",       6920),   # the standardised-name table
    ("b4-files",      7360),   # what the workbook contains, and the recommendation
]

# ONE HIGHLIGHT, BAKED IN. "Duplicate registrations removed  112" is the line
# the voiceover lands on, and at 6360 it sits around y=770 — clear of both
# safe zones. It is baked rather than overlaid because every beat carries a
# 4% push, which would slide a static overlay off the line.
HIGHLIGHTS = {"b2-duplicates": dict(seed_y=770, lines=2)}
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
        print(f"{name:14s} frame {n}  t={n / 60:6.2f}s")

    from PIL import Image
    for name, spec in HIGHLIGHTS.items():
        path = os.path.join(OUT, name + ".png")
        box = fit_highlight(path, name=name, **spec)
        img = Image.open(path).convert("RGB")
        draw_highlight(img, box, SAFE_TOP, SAFE_BOT, name=name)
        img.save(path)


if __name__ == "__main__":
    main()
