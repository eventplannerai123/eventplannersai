#!/usr/bin/env python3
"""Build both cuts of the Oct 16 AI-makes-mistakes Reel.

Build-story format, not a demo — no ChatGPT prompt anywhere, per the brief.

Three clips, one per sentence of the voiceover, cut to the voiceover's own
pauses (silencedetect, not guesswork):

  1. the seating chart      — "AI will never get VIP seating right on its own"
  2. a name being moved     — "it doesn't know which two executives can't sit
                               together, or who reports to whom"
  3. the wide of her desk    — "I use it for most of the paperwork, and I check
                               everything it gives me"

That order puts the artefact first, the correction second and her actual
workspace last. The desk wide is the human close, not the opening: opening on
a desk with nothing on the screens is the Oct 7 mistake, where generic footage
was rejected.

All three sources are already 1080x1920, so there is no crop to compute. The
desk clip is 60fps HEVC carrying rotation=-90 and real room audio: ffmpeg
applies the rotation on decode, fps drops it to 30, and its audio is never
mapped — the voiceover is the only sound.
"""
import json, os, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
REEL = os.path.dirname(HERE)
SRC  = os.path.join(REEL, "source")
CARDS= os.path.join(HERE, "cards1016")

W, H, FPS = 1080, 1920, 30
FADE = 0.20

CLIPS = ["chart.mp4", "moving-a-name.mp4", "desk-wide.mov"]

# Clip 2 is offset, not taken from its start. The move happens late in it:
# Tom Becker's row is selected at about t=3, he leaves the head table at t=4-5,
# and Jack Turner is sitting in the Board Chair seat from t=5 on. Starting at
# zero would spend the whole beat on the before state and cut away just as the
# chart changed. Starting ~1.5s in puts the selection early in the beat and
# holds the result for the last two seconds, which is the point of the shot.

CUTS = {
    # TikTok first, per the standing rule.
    "tiktok": dict(
        vo="vo-tiktok-raw.mp3",
        # VO pauses at 2.37 and 7.30; speech ends 13.93
        durs=[3.00, 5.20, 7.50],          # boundaries 2.80 / 7.80, total 15.30
        starts=[0.0, 1.8, 0.0],
    ),
    "instagram": dict(
        vo="vo-instagram-raw.mp3",
        # VO pauses at 3.31 and 8.75; speech ends 15.90
        durs=[3.90, 5.60, 7.50],          # boundaries 3.70 / 9.10, total 16.60
        starts=[0.0, 1.5, 0.0],
    ),
}

TRIM = 1.75   # measured on the Oct 15 build: 1.10 lands about 0.8 dB low


def run(cmd): return subprocess.run(cmd, check=True, capture_output=True, text=True)


def measure(path):
    p = subprocess.run(
        ["ffmpeg", "-nostdin", "-v", "info", "-i", path,
         "-af", "loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json", "-f", "null", "-"],
        capture_output=True, text=True)
    return json.loads(p.stderr[p.stderr.rindex("{"):p.stderr.rindex("}") + 1])


def build(tag, spec):
    durs, starts = spec["durs"], spec["starts"]
    total = sum(durs) - FADE * (len(durs) - 1)
    vo = os.path.join(REEL, "voiceover", spec["vo"])
    hook = os.path.join(CARDS, f"hook-{tag}.png")

    inputs, filters, labels = [], [], []
    for i, clip in enumerate(CLIPS):
        inputs += ["-ss", f"{starts[i]:.3f}", "-t", f"{durs[i]:.3f}",
                   "-i", os.path.join(SRC, clip)]
        filters.append(
            f"[{i}:v]fps={FPS},scale={W}:{H}:force_original_aspect_ratio=increase,"
            f"crop={W}:{H},setsar=1,format=yuv420p[v{i}]")
        labels.append(f"v{i}")

    hook_idx, vo_idx = len(CLIPS), len(CLIPS) + 1
    inputs += ["-framerate", str(FPS), "-loop", "1", "-t", f"{total:.3f}", "-i", hook]
    inputs += ["-i", vo]

    # chain the three clips with dissolves
    acc, cur = durs[0], labels[0]
    for i in range(1, len(durs)):
        out = f"x{i}"
        filters.append(f"[{cur}][{labels[i]}]xfade=transition=fade:"
                       f"duration={FADE}:offset={acc-FADE:.3f}[{out}]")
        acc = acc + durs[i] - FADE
        cur = out

    # hook card over the first 3 seconds; repeatlast=1 or a single PNG vanishes
    filters.append(
        f"[{cur}][{hook_idx}:v]overlay=0:0:eof_action=repeat:repeatlast=1:"
        f"enable='between(t,0,3)',format=yuv420p[vout]")

    m = measure(vo)
    gain = -14.0 - float(m["input_i"]) + TRIM
    filters.append(f"[{vo_idx}:a]volume={gain:.2f}dB,"
                   f"alimiter=limit=-1.0dB:level=0,aresample=48000[aout]")

    out = os.path.join(REEL, f"ai-makes-mistakes-{tag}.mp4")
    run(["ffmpeg", "-nostdin", "-v", "error", "-y", *inputs,
         "-filter_complex", ";".join(filters),
         "-map", "[vout]", "-map", "[aout]",
         "-c:v", "libx264", "-profile:v", "high", "-crf", "19", "-pix_fmt", "yuv420p",
         "-movflags", "+faststart", "-r", str(FPS),
         "-c:a", "aac", "-b:a", "192k", "-ar", "48000", out])
    print(f"{tag}: {total:.2f}s, VO {float(m['input_i']):.1f} LUFS, gain {gain:+.2f} dB")


if __name__ == "__main__":
    for tag in ("tiktok", "instagram"):
        build(tag, CUTS[tag])
