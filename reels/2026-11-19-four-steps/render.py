"""Assemble the Thu 19 Nov Vendor Payment System Reel — "four steps".

PAYOFF FIRST, as the guide's Thu 19 block specifies: the finished coloured
tracker is on screen for the first 2.8 seconds, with the hook over it, before
step 1 exists. Then the four steps in order, each with its numbered badge and
one line, and the CTA card last.

**THE SOURCE IS A LANDSCAPE LAPTOP CAPTURE**, which no other piece this month
has been. Her phone recordings are 1080x1920 already; these four are about
1910x1040, so a full-frame fit would put the whole browser window in a 1080x589
letterbox and nothing on it would be readable. Instead each beat takes a
760x668 crop of the part of the screen that matters and scales it 1.42x into a
1080x950 panel in the middle of the frame, with the card carrying the step
number above and the handle below. Every crop was chosen by looking at that
beat's frames, not by reusing one rectangle.

**THE CUTS ARE TIMED TO THE VOICEOVER'S OWN PAUSES**, found with
`silencedetect` rather than guessed: "One:" lands at 2.84s, "Two:" at 5.48,
"Three:" at 11.77, "Four:" at 23.92 and "That's it" at 32.57, so each step's
footage starts exactly where Eryn names it.

**The script was extended from the guide's 76 words to 100.** The block asks
for "about 70 words" AND 35-45 seconds, which cannot both hold at Eryn's ~3
words a second: 76 words measured 25.2s, which would have left ten seconds of
silence inside her own duration target. The duration is the instruction ("so
the 20-second cap doesn't apply"); the word count was a planning estimate. The
extra 24 words narrate what the recording actually shows - eight emails,
seventeen payments, the three summary figures and May 3 - which is exactly what
the guide's own rule says to do with a short script.

Speed: step 2's wait is compressed 8.0x and step 4's analysis 7.0x, then both
settle to 1.0x on what came back. Steps 1 and 3 run at normal speed throughout
because the thing to watch is the click and the colours filling in.

Two cuts. They differ in the end card only - Instagram's "Comment BUDGET and
I'll send it to you", TikTok's "Comment BUDGET on my Instagram" - plus their
own voiceover, because the closing line is spoken as well as shown.
"""
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.environ.get("FOUR_STEPS_SRC", "")
CARDS = os.path.join(HERE, "build", "cards")
VO = os.path.join(HERE, "build", "vo")
WORK = os.path.join(HERE, "build", "beats")

W, H, FPS = 1080, 1920, 30
PANEL_W, PANEL_H, PANEL_Y = 1080, 950, 500
CROP_W, CROP_H = 900, 792

# Gain into alimiter, swept against the finished export rather than computed.
GAIN_DB = {"instagram": 13.4, "tiktok": 13.4}

# (name, source, src_start, out_dur, speed, crop_x, crop_y, card)
# The crop is 900x792 rather than a tighter box: at 760 wide the answer column
# ran off the right of the panel mid-sentence. 1.2x is enough magnification on
# a 1900-wide capture, and cy is chosen per source so the app's own input bar
# ("Ask ChatGPT") falls below the crop, per the Oct 5 cleaning rule.
BEATS = [
    ("b0-payoff",  "r4", 23.00,  2.84,  1.00,  820, 140, "hook"),
    ("b1-copy",    "r3",  0.30,  2.64,  1.00,  260, 170, "step1"),
    ("b2a-prompt", "r2",  6.00,  5.00,  8.00,  700, 150, "step2"),
    ("b2b-table",  "r2", 47.00,  1.29,  1.00,  740, 150, "step2"),
    ("b3-paste",   "r4", 31.00, 12.15,  1.00,  220, 140, "step3"),
    ("b4a-upload", "r5", 40.00,  4.60,  6.96,  360, 200, "step4"),
    ("b4b-mayday", "r5", 73.00,  4.05,  1.00,  360, 200, "step4"),
]
END_DUR = 3.43
# TikTok only: the Thu 19 block ends that cut on the address in large text,
# because TikTok has no bio link to point at. Two seconds, after the CTA card.
URL_DUR = 2.00
TOTAL = {"instagram": sum(b[3] for b in BEATS) + END_DUR,
         "tiktok": sum(b[3] for b in BEATS) + END_DUR + URL_DUR}


def beat(name, src, start, dur, speed, cx, cy, card):
    """One beat: crop the region that matters, scale it into the panel, and
    composite the card over it so the hole in the card frames the footage."""
    inp = os.path.join(SRC, f"{src}.mp4")
    assert os.path.exists(inp), inp
    cardp = os.path.join(CARDS, f"{card}.png")
    out = os.path.join(WORK, f"{name}.mp4")
    take = dur * speed
    vf = (f"[0:v]trim=start={start}:duration={take},setpts=(PTS-STARTPTS)/{speed},"
          f"crop={CROP_W}:{CROP_H}:{cx}:{cy},"
          f"scale={PANEL_W}:{PANEL_H}:flags=lanczos,fps={FPS}[p];"
          f"color=c=0xCECBF6:s={W}x{H}:d={dur}:r={FPS}[bg];"
          f"[bg][p]overlay=0:{PANEL_Y}:shortest=1[v0];"
          f"[v0][1:v]overlay=0:0[v]")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", inp, "-i", cardp,
                    "-filter_complex", vf, "-map", "[v]", "-an",
                    "-c:v", "libx264", "-profile:v", "high", "-crf", "17",
                    "-pix_fmt", "yuv420p", "-t", f"{dur:.3f}", out], check=True)
    return out


def end(card, dur=END_DUR):
    out = os.path.join(WORK, f"{card}.mp4")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-loop", "1",
                    "-t", f"{dur:.3f}", "-i", os.path.join(CARDS, f"{card}.png"),
                    "-vf", f"scale={W}:{H},fps={FPS},setsar=1,format=yuv420p",
                    "-c:v", "libx264", "-profile:v", "high", "-crf", "17",
                    out], check=True)
    return out


def render(platform):
    os.makedirs(WORK, exist_ok=True)
    parts = [beat(*b) for b in BEATS]
    parts.append(end(f"end-{platform}"))
    if platform == "tiktok":
        parts.append(end("url-tiktok", URL_DUR))

    listf = os.path.join(WORK, f"concat-{platform}.txt")
    with open(listf, "w") as fh:
        for p in parts:
            fh.write(f"file '{p}'\n")

    vo = os.path.join(VO, f"four-steps-{platform}-eryn.mp3")
    assert os.path.exists(vo), vo
    g = GAIN_DB[platform]
    out = os.path.join(HERE, f"four-steps-{platform}.mp4")
    subprocess.run(["ffmpeg", "-v", "error", "-y",
                    "-f", "concat", "-safe", "0", "-i", listf, "-i", vo,
                    "-filter_complex",
                    f"[1:a]volume={g}dB,alimiter=limit=0.841:level=0,"
                    f"apad=whole_dur={TOTAL[platform]}[a]",
                    "-map", "0:v", "-map", "[a]",
                    "-c:v", "libx264", "-profile:v", "high", "-crf", "19",
                    "-pix_fmt", "yuv420p", "-movflags", "+faststart",
                    "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
                    "-t", f"{TOTAL[platform]:.3f}", out], check=True)
    print(f"{platform}: {TOTAL[platform]:.2f}s -> {os.path.basename(out)}")
    return out


if __name__ == "__main__":
    assert SRC, "set FOUR_STEPS_SRC to the folder holding r2-r5.mp4"
    for p in ("instagram", "tiktok"):
        render(p)
