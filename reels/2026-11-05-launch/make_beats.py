"""Pull the Thu 5 launch Reel's beats out of Sahiba's four recordings.

HER FOOTAGE NEVER ENTERS THIS REPO, so the sources stay in the session's
scratchpad and only the finished cuts are committed. SRC below is where they
were downloaded from Drive `November 5`; set it to wherever they sit.

The four takes, and what each is for:

  inbox-a    9:20am, 60.7s   NOT USED AT ALL any more. Its answer put a totals
                             card on screen reading $59,180 unpaid and $72,480
                             scheduled, against a true $46,080 and $59,380; its
                             opening held the send tap, but she asked on Nov 3
                             for the prompt section to start on the sent
                             message rather than the keyboard, so that is gone
                             too.
  inbox-b    9:35am, 49.4s   the answer that ships, and now the prompt beat
                             too. No totals card at all, all five near-term
                             dates, and it says outright that it left the
                             event-relative dates for the tracker. It starts
                             after the send tap, on the sent bubble — which is
                             what she wants the section to open on, and which
                             holds the whole prompt where the input box held
                             only its first few lines.
  tracker    9:51am, 44.1s   the filled tracker, from the copy built here.
  contract   9:57am, 72.7s   the contract reader. Opens correctly too.

EVERY TIME HERE IS AN ACCURATE SEEK (`-ss` AFTER `-i`). Fast seek snaps to a
keyframe, and on a 60fps screen recording that lands a second or more away —
three of the first seven frames chosen that way were the wrong moment, and one
of them cut the dollar figures in half.
"""
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "build", "beats")
SRC = os.environ.get(
    "LAUNCH_SRC",
    "/tmp/claude-0/-home-user-eventplannersai/"
    "4079a8b4-9eb7-5c73-8b20-b79d77bad268/scratchpad/nov5")

# 1206x2622 iPhone capture. 478 off the top drops the status bar and the red
# recording dot; nothing off the bottom, where the platform UI covers the
# input bar anyway.
CROP = "crop=1206:2144:0:478,scale=1080:1920:flags=lanczos"

BEATS = [
    # name,        source,         time,  why this frame
    ("b1-amounts",  "tracker.mp4",  16.0, "amounts and due dates, all 17 rows"),
    ("b2-prompt",   "clip1b.mp4",    1.2, "the SENT prompt bubble, no keyboard"),
    ("b3-table",    "clip1b.mp4",   37.0, "the table coming back"),
    ("b4-dates",    "clip1b.mp4",   46.0, "the five dates, large and readable"),
    ("b5-flags",    "tracker.mp4",  28.0, "Flag column: Paid green, Due in 30 days"),
    ("b6-contract", "contract.mp4", 26.0, "final balance row, May 3 2027 in bold"),
]


def main():
    os.makedirs(OUT, exist_ok=True)
    for name, src, t, why in BEATS:
        path = os.path.join(SRC, src)
        assert os.path.exists(path), f"missing source: {path}"
        dst = os.path.join(OUT, name + ".png")
        subprocess.run(
            ["ffmpeg", "-v", "error", "-i", path, "-ss", f"{t}",
             "-frames:v", "1", "-vf", CROP, dst, "-y"], check=True)
        print(f"{name:12s} {src:14s} {t:5.1f}s  {why}")


if __name__ == "__main__":
    main()
