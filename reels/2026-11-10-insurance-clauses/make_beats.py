"""Six freeze frames from her Tue 10 recording.

THE RECORDING IS NOT IN THIS REPO. It is 127 MB of her screen, read from the
scratchpad path in $INSURANCE_SRC; the repo is public and only finished cuts
belong in it.

Crop recomputed from the source rather than pasted: 1206x2622 iPhone capture
with no rotation side data, so 1206/0.5625 = 2144 tall, 478 off the top to
lose the status bar and the red recording dot, nothing off the bottom where
the platform UI sits.

ONE DECODE, SIX FRAMES. Accurate seeking (-ss after -i) re-decodes from the
start of the file every time, and on 69 seconds of 60fps HEVC that is about
fifteen seconds a frame. The select filter picks all six out of a single
pass instead, which is both faster and frame-exact.

IT SELECTS BY FRAME NUMBER, NOT BY A TIME WINDOW. A first version used
between(t,T,T+0.02), which at 60fps spans one or two frames rather than
exactly one: the six windows matched eleven frames, -frames:v 6 kept the
first six, and every beat after the second was silently the wrong picture.
eq(n,N) matches exactly one frame per beat, so the count and the order are
guaranteed. Each frame is checked against what it is supposed to show
before anything is rendered.

The beats follow the answer's own ranking, which is NOT the brief's: the
brief leads on the liquor liability gap, and ChatGPT ranks the policy's
expiry date above it, because the policy runs out seventeen days before the
event. See the README.
"""
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "build", "beats")
SRC = os.environ["INSURANCE_SRC"]

CROP = "crop=1206:2144:0:478,scale=1080:1920:flags=lanczos"

BEATS = [
    ("b0-prompt", 18.50),   # the sent prompt, both PDFs attached, keyboard gone
    ("b1-gaps",   22.50),   # "3 major insurance gaps / 1 additional coverage issue"
    ("b2-table",  32.50),   # the table's sharp end: liquor, waiver, certificate date
    ("b3-expiry", 36.50),   # Issue 1, highest priority: "17 days before the gala"
    ("b4-raise",  41.50),   # "Increase liquor liability to at least $2 million"
    ("b5-vendor", 63.50),   # vendor insurance: her own certificate is not the fix
]


def main():
    os.makedirs(OUT, exist_ok=True)
    fps = float(subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "v:0",
         "-show_entries", "stream=r_frame_rate", "-of", "csv=p=0", SRC],
        capture_output=True, text=True, check=True).stdout.strip().split("/")[0])
    frames = [round(t * fps) for _, t in BEATS]
    assert len(set(frames)) == len(frames), frames
    expr = "+".join(f"eq(n\,{n})" for n in frames)
    tmp = os.path.join(OUT, "_pass%02d.png")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", SRC,
                    "-vf", f"select='{expr}',{CROP}",
                    "-vsync", "0", tmp], check=True)
    got = len([f for f in os.listdir(OUT) if f.startswith("_pass")])
    assert got == len(BEATS), f"{got} frames came out, not {len(BEATS)}"
    for i, (name, t) in enumerate(BEATS, start=1):
        src = os.path.join(OUT, f"_pass{i:02d}.png")
        dst = os.path.join(OUT, f"{name}.png")
        os.replace(src, dst)
        print(f"{name}  t={t:5.2f}s  {os.path.getsize(dst):,} bytes")


if __name__ == "__main__":
    main()
