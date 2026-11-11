"""Five freeze frames from her Wed 11 recording of the venue-email redo.

THE RECORDING IS NOT IN THIS REPO. It is 42.8 MB of her screen, read from the
scratchpad path in $VENUE_SRC; the repo is public and only finished cuts
belong in it.

Crop recomputed from the source: 1206x2622 iPhone capture, no rotation side
data, so 1206/0.5625 = 2144 tall, 478 off the top for the status bar and the
red recording dot, nothing off the bottom.

THIS RECORDING IS SHORT — 24.37s, against 69s on Tue 10 and 108s on Thu 12 —
so every beat is within a second or two of its neighbours and there is no
slack. Two consequences worth knowing before changing a timestamp:

1. **1.0-2.5s is the loading gap.** The send happens off the top of the clip
   and the next second and a half is a spinner. LOADING_WINDOW bars it.
2. **The whole prompt is in the INPUT BOX, not the sent bubble.** By the time
   the bubble is on screen the view has scrolled and only its last three lines
   show. That is the opposite of the usual case, where the sent bubble is the
   better opening frame because it holds the whole prompt. Here the opening
   frame is t=0.50s, the input box with the attached PDF chip, which is the
   only frame in the recording carrying the prompt entire.

THE BEATS FOLLOW THE VOICEOVER, which is why b2 sits a second and a half
BEFORE b1 in the recording: the $45,000 total is what the voiceover opens on,
and the small print that makes the whole piece work is read out after it.
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
SRC = os.environ["VENUE_SRC"]

CROP = "crop=1206:2144:0:478,scale=1080:1920:flags=lanczos"

LOADING_WINDOW = (1.0, 2.5)   # the spinner between the send and the answer

# Timestamps checked against the frames, not assumed. The small-print line the
# piece turns on — "Sunday-Thursday rates and multi-year agreements are
# available on request" — is legible in exactly one place, t=6.00s, where page
# two sits high enough to clear the PDF toolbar. A second later the scroll has
# taken it under the toolbar and it cannot be read at all.
BEATS = [
    ("b0-prompt",      0.50),  # the whole prompt in the input box, PDF attached
    ("b1-quote",       7.50),  # $45,000.00, the Saturday rate
    ("b2-smallprint",  6.00),  # rate notes: weekday rates available on request
    ("b3-email",      19.00),  # the email, with both asks as bullets
    ("b4-tip",        22.50),  # "I would avoid naming a target price initially"
]

# ONE HIGHLIGHT, ON ONE BEAT, AND IT IS BAKED INTO THE FRAME RATHER THAN
# OVERLAID. The small-print line is 8pt grey in the source — legible at
# 1080x1920 and marginal on a phone — and it is the sentence the whole piece
# turns on, so it is the one case in this series that has earned a highlight.
# It is baked because every beat carries a 4% push: an overlay added after the
# concat would stay still while the line drifted out from under it.
#
# The seed is a y somewhere inside the line and the box snaps to the real ink,
# per her Oct 14 instruction not to type highlight coordinates by hand.
HIGHLIGHTS = {"b2-smallprint": dict(seed_y=935, lines=1)}
SAFE_TOP, SAFE_BOT = 231, 1440     # the top 12% and bottom 25%


def main():
    for name, t in BEATS:
        assert not (LOADING_WINDOW[0] <= t <= LOADING_WINDOW[1]), \
            f"{name} at {t}s is in the loading spinner"

    os.makedirs(OUT, exist_ok=True)
    fps = float(subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "v:0",
         "-show_entries", "stream=r_frame_rate", "-of", "csv=p=0", SRC],
        capture_output=True, text=True, check=True).stdout.strip().split("/")[0])

    # eq(n,N), never a time window: at 60fps between(t,T,T+0.02) spans one or
    # two frames, and on Nov 10 six such windows matched eleven frames and
    # every beat after the second was silently the wrong picture.
    frames = [round(t * fps) for _, t in BEATS]
    assert len(set(frames)) == len(frames), frames
    order = sorted(range(len(BEATS)), key=lambda i: frames[i])  # ffmpeg emits in time order
    expr = "+".join(f"eq(n\\,{n})" for n in sorted(frames))
    tmp = os.path.join(OUT, "_pass%02d.png")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", SRC,
                    "-vf", f"select='{expr}',{CROP}",
                    "-vsync", "0", tmp], check=True)
    got = sorted(f for f in os.listdir(OUT) if f.startswith("_pass"))
    assert len(got) == len(BEATS), f"{len(got)} frames came out, not {len(BEATS)}"

    for slot, i in enumerate(order, start=1):
        name, t = BEATS[i]
        os.replace(os.path.join(OUT, f"_pass{slot:02d}.png"),
                   os.path.join(OUT, f"{name}.png"))
        print(f"{name}  t={t:6.2f}s  frame {frames[i]}")

    from PIL import Image
    for name, spec in HIGHLIGHTS.items():
        path = os.path.join(OUT, name + ".png")
        box = fit_highlight(path, name=name, **spec)
        img = Image.open(path).convert("RGB")
        draw_highlight(img, box, SAFE_TOP, SAFE_BOT, name=name)
        img.save(path)


if __name__ == "__main__":
    main()
