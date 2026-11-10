"""Six freeze frames from her Tue 10 recording of the ticket-allocation redo.

THE RECORDING IS NOT IN THIS REPO. It is 199 MB of her screen, read from the
scratchpad path in $TICKETS_SRC; the repo is public and only finished cuts
belong in it.

Crop recomputed from the source: 1206x2622 iPhone capture, no rotation side
data, so 1206/0.5625 = 2144 tall, 478 off the top for the status bar and the
red recording dot, nothing off the bottom.

TWO THINGS IN THIS RECORDING MUST NEVER REACH A FRAME, and both are asserted
rather than remembered:

1. **An Instagram new-follower notification at about 89-91s.** Sahiba asked
   for it cut. It names a private individual and her handle, which is barred
   the same way a client's name is — so the name is not written down here
   either, only the window it occupies.
   Measured against the crop: the banner sits at roughly y 300-470 of the
   full frame, so `crop=...:478` removes it anyway — but that is luck, not a
   plan, so NOTIF_WINDOW keeps every beat clear of it with two seconds of
   margin either side.

2. **The first seconds are the iOS Files app**, listing her own documents: a
   résumé among them, and one captioned with someone else's first name. Her
   private filenames and a third party, so neither is written down here
   either. START_FLOOR bars anything that early; in practice the first usable
   frame is far later, because the PDF preview runs to about 24s.

The beats follow the voiceover rather than the scroll, which is why b5 sits
8 seconds BEFORE b4 in the recording: the answer's note about matching on
email addresses is the twist, and the twist is the last thing said.
"""
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "build", "beats")
SRC = os.environ["TICKETS_SRC"]

CROP = "crop=1206:2144:0:478,scale=1080:1920:flags=lanczos"

NOTIF_WINDOW = (86.5, 93.5)   # the banner plus two seconds of margin
START_FLOOR = 6.0             # before this the Files app is on screen

# Timestamps checked against the frames, not assumed. A first pass put the
# seats-remaining block at 103s and the email note at 100.5s; on screen it is
# the other way round, and 103s has already scrolled on to the
# recommendations. Look at the frames before building on them.
BEATS = [
    ("b0-prompt",    30.00),  # the sent prompt, the PDF attached, "Analyzing..."
    ("b1-overall",   72.00),  # 140 duplicates, still inside 2,000 capacity
    ("b2-dupes",     77.50),  # 280 records, all 140 between Client and Prospect
    ("b3-remaining",100.50),  # 2,125 -> 1,985, 15 seats left, 99.25% utilization
    ("b4-bottom",   103.00),  # "15 seats available, but reconcile the categories"
    ("b5-list",      95.00),  # the duplicate list: two teams against each name
]


def main():
    for name, t in BEATS:
        assert t >= START_FLOOR, f"{name} at {t}s is in the Files app"
        assert not (NOTIF_WINDOW[0] <= t <= NOTIF_WINDOW[1]), \
            f"{name} at {t}s is inside the Instagram notification window"

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


if __name__ == "__main__":
    main()
