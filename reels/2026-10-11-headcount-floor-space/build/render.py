#!/usr/bin/env python3
"""Build the Oct 11 TikTok quick piece: turning a headcount into floor space.

Format is the guide's quick-piece spec: open on the prompt as the setup, then
2-3 key lines of the answer as zoomed, highlighted freeze frames, then the
biggest takeaway as a big overlay. No scrolling, no end card.

Two things that drove the frame choices:

  * The clean band is x 22-1183, y 300-2364 of the 1206x2622 capture, which
    clears the status bar and the red recording dot at the top and the
    "Ask ChatGPT" input bar at the bottom. 1161x2064 is exactly 9/16, so
    nothing is stretched. (Watch the arithmetic: the roomier 1166x2074 is
    0.5622, not 0.5625, and fails the assertion below.)

  * ChatGPT's floating scroll-to-bottom button is still in frame, at about
    y 1772-1892 of the output - deep inside the bottom 25% that TikTok's own
    caption covers. Both ways of removing it were tried and both were worse
    than leaving it. A boxblur patch over black-on-white text leaves a grey
    smudge that reads as a censor box. Cropping it out means ending the crop
    above y 2205, which forces the width down to 1062 and clips the "K" off
    "Key rule" - the most important line in the piece. Leaving it costs
    nothing visible; the alternatives cost legibility.
  * Each beat's source TIME was chosen so its key line already sits in the
    middle of that band - the scroll position does the composition, not the
    crop. That is why the times are oddly specific.

A **Chivari** ad rides into the bottom of the answer from about t=23 - the
ninth distinct advertiser in three weeks, and the reason no beat is taken from
the last two seconds. The finished export is scanned for it anyway.
"""
import json, os, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
REEL = os.path.dirname(HERE)
SRC  = os.path.join(REEL, "source", "screen-recording.mp4")
VO   = os.path.join(REEL, "voiceover", "vo-tiktok-raw.mp3")
CARDS= os.path.join(HERE, "cards1011")
FRM  = os.path.join(HERE, "frames"); os.makedirs(FRM, exist_ok=True)

W, H, FPS = 1080, 1920, 30
CX, CY, CW, CH = 22, 300, 1161, 2064      # 1161/2064 == 0.5625 exactly
FADE = 0.20

# (source time, duration, overlay) - see the module docstring on the times.
# Totals 15.7s of beats, 15.1s after the dissolves, against a 13.84s voiceover.
BEATS = [
    ( 3.00, 4.0, "b1.png"),   # the prompt, with the ask highlighted
    (15.60, 3.9, "b2.png"),   # dinner seating / dance floor / two bars
    (18.80, 3.9, "b3.png"),   # RECOMMENDED TARGET 4,500-5,000 sq ft
    (21.20, 3.9, "b4.png"),   # the takeaway, over the room-dimensions table
]

def run(cmd):
    return subprocess.run(cmd, check=True, capture_output=True, text=True)

def measure(path):
    """loudnorm first pass. The gain is computed from this, never guessed."""
    p = subprocess.run(
        ["ffmpeg","-nostdin","-v","info","-i",path,
         "-af","loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json","-f","null","-"],
        capture_output=True, text=True)
    blob = p.stderr[p.stderr.rindex("{"):p.stderr.rindex("}")+1]
    return json.loads(blob)

def main():
    assert abs(CW/CH - 0.5625) < 1e-9, "clean band is not 0.5625"

    # Freeze each beat to a still first: the format is freeze frames, and
    # pulling one frame per beat keeps the filtergraph readable.
    stills = []
    for i,(t,_,_) in enumerate(BEATS):
        out = os.path.join(FRM, f"f{i}.png")
        run(["ffmpeg","-nostdin","-v","error","-y","-ss",f"{t:.2f}","-i",SRC,
             "-frames:v","1","-vf",
             f"crop={CW}:{CH}:{CX}:{CY},scale={W}:{H}:flags=lanczos", out])
        stills.append(out)

    total = sum(d for _,d,_ in BEATS) - FADE*(len(BEATS)-1)

    inputs, filters, labels = [], [], []
    for i,(_,dur,ov) in enumerate(BEATS):
        inputs += ["-framerate",str(FPS),"-loop","1","-t",f"{dur:.3f}","-i",stills[i]]
        inputs += ["-framerate",str(FPS),"-loop","1","-t",f"{dur:.3f}","-i",os.path.join(CARDS,ov)]
        vi, oi = 2*i, 2*i+1
        # A single-frame PNG needs repeatlast=1 or it shows on frame one and
        # vanishes - the Sep 25 build shipped with no hook because of this.
        filters.append(
            f"[{vi}:v]setsar=1,format=yuv420p[s{i}];"
            f"[s{i}][{oi}:v]overlay=0:0:eof_action=repeat:repeatlast=1,"
            f"format=yuv420p[v{i}]")
        labels.append(f"v{i}")

    vo_idx = 2*len(BEATS)
    inputs += ["-i", VO]

    acc, cur = BEATS[0][1], labels[0]
    for i in range(1,len(BEATS)):
        out = f"x{i}"
        filters.append(f"[{cur}][{labels[i]}]xfade=transition=fade:"
                       f"duration={FADE}:offset={acc-FADE:.3f}[{out}]")
        acc = acc + BEATS[i][1] - FADE
        cur = out

    m = measure(VO)
    # TRIM: the export measures about 1 dB below the voiceover's own first-pass
    # figure, because the cut carries its lead-in and tail. Measured, not
    # assumed, and re-checked on the finished file.
    TRIM = 1.10
    gain = -14.0 - float(m["input_i"]) + TRIM
    # alimiter renormalises back to full scale unless level=0 is passed, and a
    # -1.5 dB ceiling binds before the gain lands on this voice.
    filters.append(f"[{vo_idx}:a]volume={gain:.2f}dB,"
                   f"alimiter=limit=-1.0dB:level=0,aresample=48000[aout]")

    out = os.path.join(REEL, "headcount-floor-space-tiktok.mp4")
    run(["ffmpeg","-nostdin","-v","error","-y",*inputs,
         "-filter_complex",";".join(filters),
         "-map",f"[{cur}]","-map","[aout]",
         "-c:v","libx264","-profile:v","high","-crf","19","-pix_fmt","yuv420p",
         "-movflags","+faststart","-r",str(FPS),
         # No -shortest: the voiceover is 13.84s and the beats run 15.10s, so
         # trimming to the audio would land the cut just under the format's
         # 15s floor. The 0.6s tail holds the takeaway overlay, which is what
         # the format ends on anyway.
         "-c:a","aac","-b:a","192k","-ar","48000",out])
    print(f"built {os.path.basename(out)}: beats total {total:.2f}s, "
          f"VO measured {float(m['input_i']):.1f} LUFS, gain {gain:+.2f} dB")

if __name__ == "__main__":
    main()
