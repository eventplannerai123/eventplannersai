"""Five freeze frames from her Fri 20 recording of the Mon 23 RSVP redo.

THE RECORDING IS NOT IN THIS REPO. 170 MB of her screen, read from the
scratchpad path in $RSVP_SRC. Drive id 1iHul6APHr7k_v_aooTTsllSLE-YfTMOF, in
November 23.

Crop recomputed from the source: 1206x2622 iPhone capture, 60fps, no rotation
side data, so 1206/0.5625 = 2144 tall, 478 off the top.

**SHE ASKED FOR THE CHATGPT POP-UP TO COME OUT.** An "Improve accuracy for
documents and research / Get Plus" upsell card slides over the answer partway
through. Detected rather than eyeballed: a 10fps scan of the Get Plus pill's
own band found it solid from 46.2s to 47.4s, and frames either side put the
fade at **46.0s to 47.6s**, i.e. source frames 2760 to 2856. No beat here
comes from that window and the assert below enforces it, so the pop-up cannot
come back if a frame number is ever nudged.

Ad-checked over the whole recording as well — a 2-second contact sheet of the
bottom 560px, every frame of it, which is where the nine advertisers so far
have appeared. Nothing. The pop-up is the only interruption.

**IT OPENS ON THE FINISHED SHEET, NOT THE UPLOAD** — the Mon 23 brief says
"payoff first: the finished one-page caterer sheet, readable in the first 2
seconds", the same inversion as Mon 16 and Tue 17. The prompt is beat two and
the whole of it is in the caption, so the 6-second ceiling is met at frame one.

**THE BRIEF'S PREDICTED TWIST DID NOT HAPPEN.** It expected the answer to
group the notes correctly and still report 142 meals, reading the six
unchosen plus-one cells as empty rather than as a question. It did not: §4
says all 142 primary guests chose, names the six plus-ones who did not, and
the closing recommendation refuses to finalise at 142 because "you potentially
have 148 attendees". That catch is b4, and the voiceover's last line, the end
card and the caption's third paragraph are written around it, which is what
the brief's twist line asks for.
"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "build", "beats")
SRC = os.environ["RSVP_SRC"]

CROP = "crop=1206:2144:0:478,scale=1080:1920:flags=lanczos"

# The pop-up, in source frames at 60fps. Measured, not guessed.
POPUP = (2760, 2856)

BEATS = [
    ("b0-counts",   2316),  # §1 meal counts: 54 / 48 / 22 / 18, Total 142
    ("b1-prompt",     60),  # the whole prompt, PDF chip above it, send arrow
    ("b2-notes",    3120),  # four spellings of one table, and Nut / Tree Nut 5
    ("b3-conflicts",4100),  # §3, "3 confirmed conflicts", all three named
    ("b4-recommend",4980),  # the counts panel and "don't finalize at 142"
]


def main():
    os.makedirs(OUT, exist_ok=True)
    frames = [n for _, n in BEATS]
    assert len(set(frames)) == len(frames), frames
    for name, n in BEATS:
        assert not (POPUP[0] <= n <= POPUP[1]), (
            f"{name} is frame {n}, inside the Get Plus pop-up ({POPUP})")
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


if __name__ == "__main__":
    main()
