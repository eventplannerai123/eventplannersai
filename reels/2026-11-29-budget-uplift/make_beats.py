"""Five freeze frames from her Tue 24 recording of the Sun 29 budget piece.

THE RECORDING IS NOT IN THIS REPO. 59 MB of her screen, read from the
scratchpad path in $SUN_SRC. Drive id 1QNjIGDj23u8fSZbGFTRs6MnQ0mfRCsd_, in
November 29, recorded 10:08am Tue 24.

Crop recomputed from the source: 1206x2622 iPhone capture, 60fps, no rotation
side data, so 1206/0.5625 = 2144 tall, 478 off the top.

**CLEAN RECORDING.** A half-second scan of all 65 frames found no advertiser
anywhere and no ChatGPT "Get Plus" pop-up, so unlike Mon 23 there is no
window to assert beats out of. It also opens exactly as the guide asks: the
prompt sitting in the box with the PDF chip above it and the send tap on
camera at about 1.0s.

**IT OPENS ON THE PAYOFF, NOT THE PROMPT** — the Sun 29 brief says "payoff
first: the finished 2027 column with the two quoted lines flagged, readable
in the first 2 seconds". b0 is that frame: $113,179 under the heading, with
venue at 8.33% and catering at 6.34% directly beneath it. The prompt is beat
two and the whole of it is in the caption, so the 6-second ceiling is met at
frame one.

**b3 IS THE TWIST AND IT IS WHY THE PIECE WORKS.** Her Sun 29 YOU line asks
for the one thing she would still change; she said she would change nothing
and asked what this session thought. The answer's section 2, "Lines most
likely to increase faster than 3%", opens with **venue rental and catering,
both High** — and those are the only two lines in the whole budget that are
already contracted. A risk list is for what can still move. She agreed:
"yes thats the twist".
"""
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "build", "beats")
SRC = os.environ["SUN_SRC"]

CROP = "crop=1206:2144:0:478,scale=1080:1920:flags=lanczos"

BEATS = [
    ("b0-budget", 1260),   # $113,179, +$5,379 (4.99%), venue 8.33% catering 6.34%
    ("b1-prompt",   60),   # the whole prompt, PDF chip above it, send arrow
    ("b2-total",  1320),   # the eleven lines down to TOTAL $107,800 -> $113,179
    ("b3-risk",   1470),   # section 2: venue High, catering High — the twist
    ("b4-end",    1860),   # 2027 Budget Summary and the closing recommendation
]


def main():
    os.makedirs(OUT, exist_ok=True)
    frames = [n for _, n in BEATS]
    assert len(set(frames)) == len(frames), frames
    assert max(frames) < 1941, "a beat is past the end of a 32.35s/60fps source"
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
        print(f"{name:11s} frame {n}  t={n / 60:6.2f}s")


if __name__ == "__main__":
    main()
