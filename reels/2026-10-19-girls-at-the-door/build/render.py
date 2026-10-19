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
  * IT WAS SILENT, AND IS NOT ANY MORE. The brief says "no voiceover - the
    overlay and caption carry it", and the first build followed that. She
    asked why ("why is it silent though"), which is the same objection she
    raised about the Oct 6 cancellation piece, and approved a 39-word script.
    So the brief loses to the standing preference.
  * THE CARD TIMINGS MOVED TO MATCH THE VOICE, which is the one thing adding a
    voiceover forces. Her instruction was to keep the overlays as they are,
    meaning the words; the windows had to shift or the text would leave while
    the voice was still saying it. Boundaries were measured off the take's own
    energy envelope rather than guessed - sentences run 0.16-4.16, 4.70-5.64,
    6.04-10.26 and 11.06-13.04 - and the windows below are built around them.
    Card 2 is held to 2.4s rather than the 0.94s its line takes to say,
    because the card carries the long form ("I was one of the girls at the
    door") where the voice says the short one ("I was one of them").
  * THE LAST 1.96s ARE QUIET ON PURPOSE. The voice stops at 13.04 and the
    prompt card holds alone to 15.0. That is a beat under the payoff, not the
    long silent tail the timing rules warn about.
  * LEVEL: the take measures -27.05 LUFS, so it goes up 13.05 dB to the house
    -14. Its true peak is -8.12, which that gain would push to +4.93 dBTP, so
    alimiter catches it - with level=0, or the limiter renormalises back to
    full scale and the audio clips at 0.0 dBFS however low the limit is set.
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

VO = os.path.join(REEL, "voiceover", "take2.mp3")
VO_GAIN = 13.05        # measured: VO -27.05 LUFS, house target -14.0

# (file, start, end), built around the voice's own sentence boundaries
BEATS = [
    ("01-blog.png",    0.0,  4.4),   # voice 0.16-4.16
    ("02-me.png",      4.4,  6.8),   # voice 4.70-5.64, card holds longer to read
    ("03-today.png",   6.8, 10.9),   # voice 6.04-10.26
    ("04-prompt.png", 10.9,  DUR),   # voice 11.06-13.04, then quiet to 15.0
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
cmd += ["-i", VO]
chain += (
    f";[{len(BEATS)+1}:a]volume={VO_GAIN}dB,alimiter=limit=-1.0dB:level=0,"
    f"aresample=48000,apad,atrim=0:{DUR},asetpts=PTS-STARTPTS[a]"
)
cmd += [
    "-filter_complex", chain,
    "-map", "[v]", "-map", "[a]",
    "-c:v", "libx264", "-profile:v", "high", "-crf", "19", "-pix_fmt", "yuv420p",
    "-movflags", "+faststart", "-r", str(FPS), "-t", f"{DUR}",
    "-c:a", "aac", "-b:a", "192k", "-ar", "48000", OUT,
]

if __name__ == "__main__":
    subprocess.run(cmd, check=True, capture_output=True, text=True)
    print("built", OUT)
