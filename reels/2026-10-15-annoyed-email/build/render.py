#!/usr/bin/env python3
"""Build the Oct 15 annoyed-email quick piece.

A quick piece, so it is TikTok-only and gets ONE cut, not two.

Notes on the build:

  * Clean band 1161x2064 at x=22, y=300 of the 1206x2622 capture - clears the
    status bar and the input bar, and is exactly 9/16.
  * The recording opens correctly: the prompt sits in the input box with the
    send arrow still showing at t=0.3, so the cut opens on the prompt the way
    the guide's Oct 5 rule 2 requires, with no faked opening.
  * Beat 3 is at t=9.7, not 10.5. At 10.5 the firm paragraph is cut by the
    frame and any 3-line slice of it starts mid-sentence; at 9.7 all six of
    its lines sit inside the Oct 5 safe band and the sentence is whole. The
    preview caught that before anything was rendered.
  * Time to payoff: the rewrite comes in at 5.75s, under the 6s ceiling.
  * Overlay boxes come from tools/cardkit.py, never typed by hand.
"""
import json, os, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
REEL = os.path.dirname(HERE)
SRC  = os.path.join(REEL, "source", "raw.mp4")
CARDS= os.path.join(HERE, "cards1015")
FRM  = os.path.join(HERE, "frames"); os.makedirs(FRM, exist_ok=True)

W, H, FPS = 1080, 1920, 30
CX, CY, CW, CH = 22, 300, 1161, 2064
FADE = 0.20

# (source time, overlay, duration). The durations are cut to the voiceover's
# own pauses, measured with silencedetect: it breaks at 2.25, 6.10, 8.85,
# 10.05, 11.77 and ends at 14.82.
BEATS = [
    ( 0.5, "b1.png", 2.90),   # the prompt in the input box, hook above it
    ( 5.5, "b2.png", 3.25),   # "I honestly don't understand why this is so hard"
    ( 9.7, "b3.png", 6.55),   # the rewrite's whole consequence paragraph
    (12.4, "b4.png", 3.50),   # the end of the rewrite, dimmed, takeaway over it
]
VO  = os.path.join(REEL, "voiceover", "vo-tiktok-raw.mp3")
OUT = os.path.join(REEL, "annoyed-email-tiktok.mp4")


def run(cmd): return subprocess.run(cmd, check=True, capture_output=True, text=True)


def measure(path):
    p = subprocess.run(
        ["ffmpeg", "-nostdin", "-v", "info", "-i", path,
         "-af", "loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json", "-f", "null", "-"],
        capture_output=True, text=True)
    blob = p.stderr[p.stderr.rindex("{"):p.stderr.rindex("}") + 1]
    return json.loads(blob)


def stills():
    """Re-extract the beat frames the cards were fitted against."""
    out = []
    for t, _, _ in BEATS:
        p = os.path.join(FRM, f"b{t}.png")
        run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-ss", f"{t:.2f}", "-i", SRC,
             "-frames:v", "1",
             "-vf", f"crop={CW}:{CH}:{CX}:{CY},scale={W}:{H}:flags=lanczos", p])
        out.append(p)
    return out


def build(frames):
    durs = [b[2] for b in BEATS]
    total = sum(durs) - FADE * (len(durs) - 1)

    inputs, filters, labels = [], [], []
    for i, (_, ov, d) in enumerate(BEATS):
        ovp = os.path.join(CARDS, ov)
        inputs += ["-framerate", str(FPS), "-loop", "1", "-t", f"{d:.3f}", "-i", frames[i]]
        inputs += ["-framerate", str(FPS), "-loop", "1", "-t", f"{d:.3f}", "-i", ovp]
        vi, oi = 2 * i, 2 * i + 1
        # repeatlast=1 or a single-frame PNG shows once and vanishes
        filters.append(
            f"[{vi}:v]setsar=1,format=yuv420p[s{i}];"
            f"[s{i}][{oi}:v]overlay=0:0:eof_action=repeat:repeatlast=1,format=yuv420p[v{i}]")
        labels.append(f"v{i}")

    vo_idx = 2 * len(BEATS)
    inputs += ["-i", VO]

    acc, cur = durs[0], labels[0]
    for i in range(1, len(durs)):
        out = f"x{i}"
        filters.append(f"[{cur}][{labels[i]}]xfade=transition=fade:"
                       f"duration={FADE}:offset={acc-FADE:.3f}[{out}]")
        acc = acc + durs[i] - FADE
        cur = out

    m = measure(VO)
    TRIM = 1.75   # measured: at 1.10 the export read -14.8, not -14
    gain = -14.0 - float(m["input_i"]) + TRIM
    filters.append(f"[{vo_idx}:a]volume={gain:.2f}dB,"
                   f"alimiter=limit=-1.0dB:level=0,aresample=48000[aout]")

    run(["ffmpeg", "-nostdin", "-v", "error", "-y", *inputs,
         "-filter_complex", ";".join(filters),
         "-map", f"[{cur}]", "-map", "[aout]",   # never -shortest: the VO is 0.5s shorter than the cut
         "-c:v", "libx264", "-profile:v", "high", "-crf", "19", "-pix_fmt", "yuv420p",
         "-movflags", "+faststart", "-r", str(FPS),
         "-c:a", "aac", "-b:a", "192k", "-ar", "48000", OUT])
    print(f"tiktok: {total:.2f}s, VO {float(m['input_i']):.1f} LUFS, gain {gain:+.2f} dB")


if __name__ == "__main__":
    assert abs(CW / CH - 0.5625) < 1e-9, "clean band is not 0.5625"
    build(stills())
