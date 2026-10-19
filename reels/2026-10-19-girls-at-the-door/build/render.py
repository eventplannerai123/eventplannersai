#!/usr/bin/env python3
"""Mon 19 Oct - "the girls at the door". One still, a slow push-in, four cards.

The brief: 12-15s, the de-branded IMG_0853 registration-table photo, slow
push-in, no voiceover - the overlay and caption carry it. Never name the
company, the client or the blog.

  * THE STILL IS 1536x2048 (3:4) and the frame is 1080x1920 (9:16), so a
    9:16 window has to come out of it. The widest possible one (1152x2048,
    full height) was built first and thrown away: it keeps the whole floor,
    so the tables sit in a band across the middle with empty wall above and a
    half-cropped cocktail table blobbing into the bottom-left corner. It read
    as a photograph of a floor.
  * SO THE WINDOW IS 1008x1792 AT (470, 90) and the push-in tightens into
    864x1536 at (610, 230) - the check-in run, the navy runner and the door,
    with the cut-off cocktail table pushed out of frame. The move is the
    story: open on the room, end on the door.
  * PUSH-IN is zoompan, 1.00 to 1.167 (= 1008/864) over the full 15s, with
    the sampled centre drifting 68px right and 12px down to land on that
    tighter window. At the start the sample is 1008 wide against a 1080-wide
    output, a 1.07x upscale; at the end it is 864, a 1.25x upscale. Taking the
    crop at native size rather than pre-scaling keeps the opening nearly
    pixel-for-pixel, and the softest moment is the last frame rather than all
    of them.
  * MOTION FROM FRAME ONE. The zoom starts moving at frame 0, so this is not
    a static title card even though the source is a still.
  * SILENT BY THE BRIEF. An anullsrc track is muxed so the file carries a real
    (silent) audio stream rather than none at all - Meta handles a trackless
    mp4 inconsistently. Oct 5 rule 1 allows silence only for an overlay-led
    piece, which this is: the four cards carry the whole story.
  * Each card is a single PNG, so every overlay needs repeatlast=1 or it shows
    on one frame and vanishes.
"""
import os, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
REEL = os.path.dirname(HERE)
STILL = os.path.join(HERE, "frames", "door-still.png")
CARDS = os.path.join(HERE, "cards")
OUT = os.path.join(REEL, "girls-at-the-door.mp4")

W, H, FPS, DUR = 1080, 1920, 30, 15.0
FRAMES = int(DUR * FPS)

# Opening window out of the 1536x2048 still, and the tighter one to land on.
OPEN_W, OPEN_H, OPEN_X, OPEN_Y = 1008, 1792, 470, 90
END_W,  END_H,  END_X,  END_Y  = 864, 1536, 610, 230
assert abs(OPEN_W / OPEN_H - 0.5625) < 1e-9 and abs(END_W / END_H - 0.5625) < 1e-9
assert OPEN_X + OPEN_W <= 1536 and OPEN_Y + OPEN_H <= 2048

ZOOM_END = OPEN_W / END_W                      # 1.1667
# Sampled centre, in coordinates of the cropped opening window.
CX0, CY0 = OPEN_W / 2, OPEN_H / 2
CX1 = (END_X + END_W / 2) - OPEN_X
CY1 = (END_Y + END_H / 2) - OPEN_Y

# (file, start, end) - held long enough to read, per the brief's own rule
BEATS = [
    ("01-blog.png",    0.0,  4.0),
    ("02-me.png",      4.0,  7.0),
    ("03-today.png",   7.0, 11.0),
    ("04-prompt.png", 11.0, DUR),
]

p = f"on/{FRAMES - 1}"                          # 0 -> 1 across the piece
zoom = f"min(1+{ZOOM_END - 1:.6f}*{p},{ZOOM_END:.6f})"
cx = f"({CX0:.1f}+{CX1 - CX0:.1f}*{p})"
cy = f"({CY0:.1f}+{CY1 - CY0:.1f}*{p})"

chain = (
    f"[0:v]crop={OPEN_W}:{OPEN_H}:{OPEN_X}:{OPEN_Y},"
    f"zoompan=z='{zoom}':x='{cx}-(iw/zoom/2)':y='{cy}-(ih/zoom/2)'"
    f":d=1:s={W}x{H}:fps={FPS},"
    f"setsar=1,format=yuv420p[base]"
)
last = "base"
for i, (f, a, b) in enumerate(BEATS):
    nxt = f"v{i}"
    chain += (
        f";[{last}][{i+1}:v]overlay=0:0:eof_action=repeat:repeatlast=1"
        f":enable='between(t,{a},{b})'[{nxt}]"
    )
    last = nxt
chain += f";[{last}]format=yuv420p[v]"

cmd = ["ffmpeg", "-nostdin", "-v", "error", "-y",
       "-framerate", str(FPS), "-loop", "1", "-t", f"{DUR}", "-i", STILL]
for f, _, _ in BEATS:
    cmd += ["-framerate", str(FPS), "-loop", "1", "-t", f"{DUR}",
            "-i", os.path.join(CARDS, f)]
cmd += [
    "-f", "lavfi", "-t", f"{DUR}", "-i", "anullsrc=r=48000:cl=stereo",
    "-filter_complex", chain,
    "-map", "[v]", "-map", f"{len(BEATS)+1}:a",
    "-c:v", "libx264", "-profile:v", "high", "-crf", "19", "-pix_fmt", "yuv420p",
    "-movflags", "+faststart", "-r", str(FPS), "-t", f"{DUR}",
    "-c:a", "aac", "-b:a", "192k", "-ar", "48000", OUT,
]

if __name__ == "__main__":
    subprocess.run(cmd, check=True, capture_output=True, text=True)
    print("built", OUT)
