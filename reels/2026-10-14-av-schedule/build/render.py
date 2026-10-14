#!/usr/bin/env python3
"""Build both cuts of the Oct 14 AV schedule check piece.

The story is hers: at her first job she sent the AV team to lunch during the
keynote, because the day two and day three crew schedules had been swapped.
This is AI finding exactly that, from a demo crew schedule and production
schedule, so the claim is on screen rather than asserted.

Notes on the build:

  * Clean band 1161x2064 at x=22, y=300 of the 1206x2622 capture - clears the
    status bar and the input bar, and is exactly 9/16.
  * The recording opens AFTER the send tap, but frame one carries the whole
    prompt in the sent bubble, which is the better frame to open on anyway.
    So no faked opening was needed.
  * Opening on the prompt follows the guide's Oct 5 rule 2. This day's own
    block says "open on the finished list of mismatches, not the prompt being
    sent", which predates rule 2 - same call as the Oct 12 piece.
  * NO in-app ad anywhere in the 32s. The bottom strip was scanned at 2s
    intervals across the whole clip before this was relied on.
  * It caught the swap, which the brief says to re-run for if missed.
"""
import json, os, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
REEL = os.path.dirname(HERE)
SRC  = os.path.join(REEL, "source", "raw.mp4")
CARDS= os.path.join(HERE, "cards1014")
FRM  = os.path.join(HERE, "frames"); os.makedirs(FRM, exist_ok=True)

W, H, FPS = 1080, 1920, 30
CX, CY, CW, CH = 22, 300, 1161, 2064
FADE = 0.20

# (source time, overlay) - shared by both cuts; only beat 1's hook differs
BEATS = [
    ( 1.20, "b1-{tag}.png"),   # the prompt, whole, with the hook above it
    (13.00, "b2.png"),         # "the Day 2 and Day 3 crew schedules appear to be swapped"
    (26.50, "b3.png"),         # the day-swap diagnosis, both directions
    (31.90, "b4.png"),         # the bottom line, dimmed, with the takeaway
]

CUTS = {
    # TikTok first, per the standing rule. Its voiceover runs 0.6s longer, so
    # its beats are fractionally longer too - the "slightly different pacing"
    # the two-cuts rule asks for.
    "tiktok":    dict(vo="vo-tiktok-raw.mp3",    durs=[4.3, 4.3, 4.3, 4.3]),
    "instagram": dict(vo="vo-instagram-raw.mp3", durs=[3.9, 4.0, 4.0, 3.9]),
}

def run(cmd): return subprocess.run(cmd, check=True, capture_output=True, text=True)

def measure(path):
    p = subprocess.run(
        ["ffmpeg","-nostdin","-v","info","-i",path,
         "-af","loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json","-f","null","-"],
        capture_output=True, text=True)
    blob = p.stderr[p.stderr.rindex("{"):p.stderr.rindex("}")+1]
    return json.loads(blob)

def stills():
    out=[]
    for i,(t,_) in enumerate(BEATS):
        p = os.path.join(FRM, f"f{i}.png")
        run(["ffmpeg","-nostdin","-v","error","-y","-ss",f"{t:.2f}","-i",SRC,"-frames:v","1",
             "-vf", f"crop={CW}:{CH}:{CX}:{CY},scale={W}:{H}:flags=lanczos", p])
        out.append(p)
    return out

def build(tag, spec, frames):
    durs = spec["durs"]
    total = sum(durs) - FADE*(len(durs)-1)
    vo = os.path.join(REEL, "voiceover", spec["vo"])

    inputs, filters, labels = [], [], []
    for i,(_, ov) in enumerate(BEATS):
        ovp = os.path.join(CARDS, ov.format(tag=tag))
        inputs += ["-framerate",str(FPS),"-loop","1","-t",f"{durs[i]:.3f}","-i",frames[i]]
        inputs += ["-framerate",str(FPS),"-loop","1","-t",f"{durs[i]:.3f}","-i",ovp]
        vi, oi = 2*i, 2*i+1
        # repeatlast=1 or a single-frame PNG shows once and vanishes
        filters.append(
            f"[{vi}:v]setsar=1,format=yuv420p[s{i}];"
            f"[s{i}][{oi}:v]overlay=0:0:eof_action=repeat:repeatlast=1,format=yuv420p[v{i}]")
        labels.append(f"v{i}")

    vo_idx = 2*len(BEATS)
    inputs += ["-i", vo]

    acc, cur = durs[0], labels[0]
    for i in range(1,len(durs)):
        out=f"x{i}"
        filters.append(f"[{cur}][{labels[i]}]xfade=transition=fade:"
                       f"duration={FADE}:offset={acc-FADE:.3f}[{out}]")
        acc = acc + durs[i] - FADE; cur = out

    m = measure(vo)
    TRIM = 1.10   # the export reads ~1 dB under the voiceover's own figure
    gain = -14.0 - float(m["input_i"]) + TRIM
    filters.append(f"[{vo_idx}:a]volume={gain:.2f}dB,"
                   f"alimiter=limit=-1.0dB:level=0,aresample=48000[aout]")

    out = os.path.join(REEL, f"av-schedule-{tag}.mp4")
    run(["ffmpeg","-nostdin","-v","error","-y",*inputs,
         "-filter_complex",";".join(filters),
         "-map",f"[{cur}]","-map","[aout]",
         "-c:v","libx264","-profile:v","high","-crf","19","-pix_fmt","yuv420p",
         "-movflags","+faststart","-r",str(FPS),
         "-c:a","aac","-b:a","192k","-ar","48000", out])
    print(f"{tag}: {total:.2f}s, VO {float(m['input_i']):.1f} LUFS, gain {gain:+.2f} dB")

if __name__ == "__main__":
    assert abs(CW/CH - 0.5625) < 1e-9, "clean band is not 0.5625"
    f = stills()
    for tag in ("tiktok","instagram"):
        build(tag, CUTS[tag], f)
