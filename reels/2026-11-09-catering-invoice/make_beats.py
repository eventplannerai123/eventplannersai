"""Six freeze frames from her Mon 9 recording.

THE RECORDING IS NOT IN THIS REPO. It is 75 MB of her screen, read from the
scratchpad path in $INVOICE_SRC; the repo is public and only finished cuts
belong in it.

Crop recomputed from the source rather than pasted: 1206x2622 iPhone capture,
so 1206/0.5625 = 2144 tall, 478 off the top to lose the status bar and the
red recording dot, nothing off the bottom where the platform UI sits.

The beats follow the answer's own argument, which is NOT the one the brief
expected (see README): the invoice is $1,140 over, and only $530 of it is
worth disputing.
"""
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "build", "beats")
SRC = os.environ["INVOICE_SRC"]

CROP = "crop=1206:2144:0:478,scale=1080:1920:flags=lanczos"

BEATS = {
    "b0-prompt":  2.60,   # the sent prompt bubble, both PDFs attached
    "b1-530":    14.60,   # "three billing discrepancies" and $530.00
    "b2-table":  19.50,   # the discrepancy table, line by line
    "b3-minimum": 25.00,  # "the guarantee is a minimum, not a cap"
    "b4-recon":  30.00,   # the reconciliation: $18,300 / $19,440 / +$1,140
    "b5-dispute": 36.50,  # "Amount to dispute  $530.00"
}


def main():
    os.makedirs(OUT, exist_ok=True)
    for name, t in BEATS.items():
        p = os.path.join(OUT, f"{name}.png")
        # -ss AFTER -i: accurate seek, not the nearest keyframe
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", SRC,
                        "-ss", str(t), "-frames:v", "1", "-vf", CROP, p],
                       check=True)
        print(f"{name}  t={t:5.2f}s  {os.path.getsize(p):,} bytes")


if __name__ == "__main__":
    main()
