"""What goes to TikTok for a piece — worked out, not remembered.

Three TikTok hand-overs in two days (Wed 25, Sat 28, Sun 29 Nov) sent the
wrong thing: twice the slide Reel's mp4 instead of the slides' JPEGs, once
the Instagram cut instead of the TikTok one. She caught the second herself —
"i dont see anything scheduled for the 28th on my tik tok" — and then asked
for it not to happen again.

The cause was never forgetting the hand-over. It was that a piece has two
deliverables and only one of them is the file she has just approved, so
sending *a* file feels like the job is done. The fix is to stop deciding in
the moment:

    python3.13 tools/handover.py carousels/2026-11-28-two-emails

prints the exact paths to send and the caption file to paste, and exits
non-zero if any of them is missing. Run it before every hand-over, and run
it with --all to find a piece whose TikTok deliverable was never sent.

THE RULES IT ENCODES
--------------------
- A piece with a `slides/` directory of numbered JPEGs is a **carousel**:
  TikTok gets the JPEGs in order. The mp4 is Instagram's.
- A piece with `slides/` holding exactly one image is a **single image**:
  TikTok gets that image.
- A piece with a `*-tiktok.mp4` is a **footage Reel**: TikTok gets that
  file, never the `-instagram.mp4`. They differ in hook, end card and
  pacing, so the wrong one is wrong on three counts.
- The caption is `build/caption-tiktok.txt` when it exists and
  `build/caption.txt` otherwise. The TikTok one exists when it differs —
  usually because it says "on my Instagram", there being no bio link on
  TikTok.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def deliverable(piece):
    """(kind, [paths to send], caption path) for one piece directory."""
    d = os.path.join(ROOT, piece) if not os.path.isabs(piece) else piece
    if not os.path.isdir(d):
        raise SystemExit(f"no such piece: {piece}")

    slides = os.path.join(d, "slides")
    imgs = []
    if os.path.isdir(slides):
        imgs = sorted(f for f in os.listdir(slides)
                      if f.lower().endswith((".jpg", ".jpeg", ".png")))

    mp4s = sorted(f for f in os.listdir(d) if f.endswith(".mp4"))
    tiktok_mp4 = [f for f in mp4s if f.endswith("-tiktok.mp4")]
    plain_mp4 = [f for f in mp4s
                 if not f.endswith(("-tiktok.mp4", "-instagram.mp4"))]

    # Numbered slides go in numeric order, not asciibetical: -10 sorts
    # before -2 as a string.
    def n(f):
        m = re.search(r"-(\d+)\.(?:jpg|jpeg|png)$", f, re.I)
        return int(m.group(1)) if m else None
    nums = [n(f) for f in imgs]
    numbered = len(imgs) > 1 and None not in nums and \
        sorted(nums) == list(range(1, len(imgs) + 1))

    if numbered:
        kind = "carousel"
        send = [os.path.join(slides, f) for f in sorted(imgs, key=n)]
    elif len(imgs) > 1:
        # Two images that are not 1..N are variants, not a carousel — the
        # Nov 24 A/B hook test is a pair of separate posts, and sending both
        # as a carousel would post the test as one piece.
        raise SystemExit(
            f"{piece}: slides/ holds {len(imgs)} images that are not numbered "
            f"1..{len(imgs)} ({', '.join(imgs)}). That is a variant set, not a "
            f"carousel — read the README and send the one she picked.")
    elif len(imgs) == 1 and not tiktok_mp4 and not plain_mp4:
        kind = "single image"
        send = [os.path.join(slides, imgs[0])]
    elif tiktok_mp4:
        kind = "footage Reel"
        send = [os.path.join(d, tiktok_mp4[0])]
    elif len(plain_mp4) == 1:
        # One cut with no platform suffix serves both, as the Nov 20
        # coloring timelapse does.
        kind = "single cut, both platforms"
        send = [os.path.join(d, plain_mp4[0])]
    elif len(imgs) == 1:
        kind = "single image"
        send = [os.path.join(slides, imgs[0])]
    else:
        raise SystemExit(
            f"{piece}: no TikTok deliverable found — no slides and no "
            f"*-tiktok.mp4. If this piece really is Instagram-only, say so "
            f"in its README; her Nov 7 rule is that everything goes to both.")

    cap = os.path.join(d, "build", "caption-tiktok.txt")
    if not os.path.exists(cap):
        cap = os.path.join(d, "build", "caption.txt")
    return kind, send, cap


def report(piece):
    kind, send, cap = deliverable(piece)
    missing = [p for p in send + [cap] if not os.path.exists(p)]
    rel = lambda p: os.path.relpath(p, ROOT)
    print(f"{piece}\n  kind: {kind}")
    for p in send:
        print(f"  send: {rel(p)}" + ("   **MISSING**" if not os.path.exists(p) else ""))
    print(f"  caption: {rel(cap)}" + ("   **MISSING**" if not os.path.exists(cap) else ""))
    if kind == "carousel":
        print("  NOTE: the mp4 in this directory is Instagram's. Do not send it.")
    if kind == "footage Reel":
        ig = [f for f in os.listdir(os.path.join(ROOT, piece))
              if f.endswith("-instagram.mp4")]
        if ig:
            print(f"  NOTE: {ig[0]} is Instagram's. Do not send it.")
    return missing


def main(argv):
    if len(argv) == 2 and argv[1] == "--all":
        pieces = []
        for top in ("reels", "carousels", "posts"):
            d = os.path.join(ROOT, top)
            if os.path.isdir(d):
                pieces += [f"{top}/{x}" for x in sorted(os.listdir(d))
                           if os.path.isdir(os.path.join(d, x))]
    elif len(argv) >= 2:
        pieces = argv[1:]
    else:
        raise SystemExit(__doc__.strip().splitlines()[0] +
                         "\n\nusage: handover.py <piece dir> [...] | --all")

    bad = 0
    for p in pieces:
        try:
            bad += len(report(p))
        except SystemExit as e:
            print(f"{p}\n  {e}")
            bad += 1
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
