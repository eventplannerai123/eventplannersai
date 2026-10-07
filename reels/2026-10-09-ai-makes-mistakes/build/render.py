#!/usr/bin/env python3
"""Build both cuts of the Oct 7 "AI makes mistakes" piece.

No screen recording: this is the build-story format, so the visuals are
Sahiba's own conference b-roll. Two things about the source shaped the edit:

  * Both .mov clips carry rotation=-90 in their stream side data, so although
    ffprobe reports 1920x1080 they DECODE as 1080x1920 - already exactly the
    output frame. No crop, no upscale, no blurred filler. Check rotation before
    assuming a phone clip is landscape.
  * `clip-2-coffee.mov` is left out of both cuts. It pans onto a sponsor's
    banner and table skirt, with the logo large and legible, and her own brief
    for this footage said no faces and no logos. It is archived in source/ and
    filed to Drive, just not published.

The stills are 1932x2576 (0.75). Cropping to 1449x2576 is exactly 0.5625 and
still downscales to 1080 wide, so the stills are sharper than the clip.
"""
import json, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REEL = os.path.dirname(HERE)
SRC  = os.path.join(REEL, "source")
VO   = os.path.join(REEL, "voiceover")
CARDS= os.path.join(HERE, "cards1007")

W, H, FPS = 1080, 1920, 30
CW, CH    = 1449, 2576          # 1449/2576 == 0.5625 exactly
FADE      = 0.20

def run(cmd, **kw):
    return subprocess.run(cmd, check=True, capture_output=True, text=True, **kw)

def still(name, x):
    return dict(kind="still", path=os.path.join(SRC, name), x=x)

def clip(name, ss):
    return dict(kind="clip", path=os.path.join(SRC, name), ss=ss)

# Each beat: (source, duration, zoom start, zoom end, x-bias)
#
# x-bias places the zoom window horizontally: 0.5 centres it, 1.0 pins it to the
# right edge. The foyer shot needs it. Even at its rightmost 0.5625 crop the
# frame still catches an exhibitor's banner on the left, and her brief for this
# footage said no faces and no logos. Opening at zoom 1.15 with the window
# pushed right drops that edge out of frame; the intermediate is 2898px wide, so
# even at 1.21 the window is still downscaled into 1080 rather than enlarged.
CUTS = {
 "instagram": dict(
    vo="vo-instagram-raw.mp3",
    hook=os.path.join(CARDS, "hook-instagram.png"),
    beats=[(still("photo-4-foyer.jpg",   483), 3.50, 1.15, 1.21, 0.88),
           (clip ("clip-1-beverage.mov", 0.40), 3.70, None, None, None),
           (still("photo-1-eggs.jpg",    241), 3.00, 1.00, 1.05, 0.50),
           (still("photo-3-ballroom.jpg",241), 6.10, 1.00, 1.07, 0.50)]),
 "tiktok": dict(
    vo="vo-tiktok-raw.mp3",
    hook=os.path.join(CARDS, "hook-tiktok.png"),
    beats=[(still("photo-3-ballroom.jpg",241), 3.40, 1.06, 1.00, 0.50),
           (still("photo-1-eggs.jpg",    241), 3.30, 1.00, 1.05, 0.50),
           (clip ("clip-1-beverage.mov", 0.40), 3.70, None, None, None),
           (still("photo-4-foyer.jpg",   483), 5.60, 1.21, 1.15, 0.88)]),
}

def measure(path):
    """loudnorm first pass - the gain is computed from this, never guessed."""
    p = subprocess.run(
        ["ffmpeg","-nostdin","-v","info","-i",path,
         "-af","loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json","-f","null","-"],
        capture_output=True, text=True)
    blob = p.stderr[p.stderr.rindex("{"):p.stderr.rindex("}")+1]
    return json.loads(blob)

def build(name, spec):
    beats = spec["beats"]
    total = sum(b[1] for b in beats) - FADE * (len(beats) - 1)

    inputs, filters, labels = [], [], []
    for i, (src, dur, z0, z1, xb) in enumerate(beats):
        if src["kind"] == "still":
            n = round(dur * FPS)
            inputs += ["-framerate", str(FPS), "-loop", "1", "-t", f"{dur:.3f}", "-i", src["path"]]
            # zoompan needs an input whose aspect already matches s, or it
            # squashes the frame: crop to 0.5625 first, then push.
            filters.append(
                f"[{i}:v]crop={CW}:{CH}:{src['x']}:0,scale={CW*2}:{CH*2}:flags=lanczos,"
                f"zoompan=z='{z0:.4f}+({z1-z0:.4f})*on/{n-1}':"
                f"x='(iw-(iw/zoom))*{xb:.2f}':y='ih/2-(ih/zoom/2)':d=1:s={W}x{H}:fps={FPS},"
                f"setsar=1,format=yuv420p[v{i}]")
        else:
            inputs += ["-ss", f"{src['ss']:.2f}", "-t", f"{dur:.3f}", "-i", src["path"]]
            filters.append(
                f"[{i}:v]scale={W}:{H}:flags=lanczos,setsar=1,fps={FPS},"
                f"format=yuv420p[v{i}]")
        labels.append(f"v{i}")

    hook_idx = len(beats)
    inputs += ["-framerate", str(FPS), "-loop", "1", "-t", f"{total:.3f}", "-i", spec["hook"]]
    vo_path = os.path.join(VO, spec["vo"])
    vo_idx  = hook_idx + 1
    inputs += ["-i", vo_path]

    acc, cur = beats[0][1], labels[0]
    for i in range(1, len(beats)):
        out = f"x{i}"
        filters.append(f"[{cur}][{labels[i]}]xfade=transition=fade:"
                       f"duration={FADE}:offset={acc-FADE:.3f}[{out}]")
        acc = acc + beats[i][1] - FADE
        cur = out

    # A single-frame PNG needs repeatlast=1, or it shows on frame one and
    # vanishes; the Sep 25 build shipped with no hook because of exactly this.
    filters.append(f"[{cur}][{hook_idx}:v]overlay=0:0:eof_action=repeat:"
                   f"repeatlast=1:enable='between(t,0,3)'[vout]")

    m = measure(vo_path)
    # The first-pass figure is what the gain is computed from, but it measures
    # the voiceover alone; the finished export reads about 1 dB lower, because
    # the cut carries the VO's own lead-in and tail. TRIM is that measured
    # difference, and the export is re-measured after every change.
    TRIM = 1.10
    gain = -14.0 - float(m["input_i"]) + TRIM
    # alimiter renormalises to full scale unless level=0 is passed.
    filters.append(f"[{vo_idx}:a]volume={gain:.2f}dB,"
                   f"alimiter=limit=-1.0dB:level=0,aresample=48000[aout]")

    out = os.path.join(REEL, f"ai-makes-mistakes-{name}.mp4")
    run(["ffmpeg","-nostdin","-v","error","-y", *inputs,
         "-filter_complex", ";".join(filters),
         "-map","[vout]","-map","[aout]",
         "-c:v","libx264","-profile:v","high","-crf","19","-pix_fmt","yuv420p",
         "-movflags","+faststart","-r",str(FPS),
         "-c:a","aac","-b:a","192k","-ar","48000","-shortest", out])
    print(f"{name}: target {total:.2f}s, VO measured {float(m['input_i']):.1f} LUFS, gain {gain:+.2f} dB")
    return out

if __name__ == "__main__":
    for n in ("tiktok", "instagram"):   # TikTok first, per the standing rule
        build(n, CUTS[n])
