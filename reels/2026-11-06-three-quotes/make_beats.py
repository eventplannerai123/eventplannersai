"""Six freeze frames out of Sahiba's Fri 6 three-quotes recording.

HER SOURCE NEVER ENTERS THIS REPO. The recording is read from $QUOTES_SRC,
which points at the scratchpad copy downloaded from Drive November 6
(ScreenRecording_11-05-2026 10-04-24 AM_1.mp4, 75,022,693 bytes, 1206x2622,
60fps, 40.94s).

EVERY SEEK IS AN ACCURATE SEEK — `-ss` AFTER `-i`. Fast seek snaps to a
keyframe, and on a 60fps screen recording that lands on the wrong moment; it
cost three of seven frames on the Nov 5 launch build.

The beat order is the guide's own structure and puts the payoff early: the
prompt, then the three real totals with Northgate's green "Cheapest" badge at
2.4s, then why, then the recommendation, then the twist. Time to payoff is
2.4s against the 6-second ceiling.
"""
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "build", "beats")
SRC = os.environ.get("QUOTES_SRC")
assert SRC and os.path.exists(SRC), "set QUOTES_SRC to her recording"

CROP = "crop=1206:2144:0:478,scale=1080:1920:flags=lanczos"

BEATS = {
    "b0-prompt":  1.0,    # the sent prompt bubble, all three PDFs attached above it
    "b1-cards":   5.2,    # Northgate $10,300 "Cheapest", Halcyon $11,200
    "b2-table":  12.0,    # side-by-side breakdown, the Actual total row
    "b3-hiding": 24.0,    # where each vendor hides cost, with the risk badges
    "b4-rec":    32.0,    # my recommendation: Northgate $10,300
    "b5-final":  40.5,    # "I wouldn't choose based on the $900 difference alone"
}


def main():
    os.makedirs(OUT, exist_ok=True)
    for name, t in BEATS.items():
        dst = os.path.join(OUT, name + ".png")
        subprocess.run(
            ["ffmpeg", "-v", "error", "-y", "-i", SRC,
             "-ss", f"{t:.3f}", "-frames:v", "1", "-vf", CROP, dst],
            check=True)
        print(f"{name:10s} @ {t:5.2f}s -> {os.path.basename(dst)}")


if __name__ == "__main__":
    main()
