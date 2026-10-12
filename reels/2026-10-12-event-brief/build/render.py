#!/usr/bin/env python3
"""Build both cuts of the Oct 12 event-brief piece.

The story: a page of handwritten consultation notes becomes a 31-point
checklist, and the one line about the network asks the generic question -
"confirm power access, internet/Wi-Fi" - rather than whether the client's
corporate laptops can actually join. That line is on screen and highlighted,
so the claim is checkable rather than asserted.

Notes on the build:

  * Clean band 1161x2064 at x=22, y=300 of the 1206x2622 capture: clears the
    status bar and the input bar, and is exactly 9/16. The roomier 1166x2074
    is 0.5622 and fails the assertion below.
  * Each beat's source TIME places its line mid-frame - the scroll position
    does the composition. Found by sampling, not guessed.
  * This recording carries NO in-app ad, the first in a while. Checked over
    the bottom strip through to the final frame anyway.
  * Opening on the prompt follows the guide's Oct 5 rule 2. The older Mon 5
    block for this piece said "open on the finished report, not the prompt" -
    that predates rule 2 and is superseded by it.
"""
import json, os, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
REEL = os.path.dirname(HERE)
SRC  = os.path.join(REEL, "source", "screen-recording.mp4")
CARDS= os.path.join(HERE, "cards1012")
FRM  = os.path.join(HERE, "frames"); os.makedirs(FRM, exist_ok=True)

W, H, FPS = 1080, 1920, 30
CX, CY, CW, CH = 22, 300, 1161, 2064
FADE = 0.20

# (source time, overlay) - shared by both cuts; only beat 1's hook differs
BEATS = [
    ( 4.20, "b1-{tag}.png"),   # the prompt, with the hook
    (20.10, "b2.png"),         # follow-up tracker, 0 of 31 complete
    (22.40, "b3.png"),         # "confirm power access, internet/Wi-Fi"
    (27.50, "b4.png"),         # the takeaway, dimmed
]

CUTS = {
    # TikTok first, per the standing rule. Its voiceover runs 0.6s longer, so
    # its beats are fractionally longer too - the "slightly different pacing"
    # the two-cuts rule asks for.
    "tiktok":    dict(vo="vo-tiktok-raw.mp3",    durs=[4.2, 4.2, 4.3, 4.2]),
    "instagram": dict(vo="vo-instagram-raw.mp3", durs=[4.0, 4.1, 4.1, 4.1]),
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

    out = os.path.join(REEL, f"event-brief-{tag}.mp4")
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
