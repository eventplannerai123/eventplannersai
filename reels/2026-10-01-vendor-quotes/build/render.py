#!/usr/bin/env python3
"""Oct 1 vendor quotes reel. Segments are rendered one at a time and then
concatenated: a single filtergraph decodes the whole HEVC source once per
branch and gets OOM-killed on a 51 MB file (Sep 28)."""
import os, subprocess, shlex, sys

SP  = "/tmp/claude-0/-home-user-eventplannersai/4079a8b4-9eb7-5c73-8b20-b79d77bad268/scratchpad/oct01"
SRC = f"{SP}/src.mov"
C   = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cards1001")

# 1206x2622 iPhone capture: 1206/0.5625 = 2144, 478 off the top so the status
# bar and the recording dot fall away and the input bar stays at the bottom.
CROP = "crop=1206:2144:0:478,scale=1080:1920:flags=lanczos,setsar=1"

def run(cmd):
    p = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if p.returncode:
        print(cmd); print(p.stderr[-3000:]); sys.exit(1)

def seg(start, end, speed, dur, out):
    vf = f"trim=start={start}:end={end},setpts=(PTS-STARTPTS)/{speed},{CROP},fps=30"
    run(f'ffmpeg -y -v error -i {shlex.quote(SRC)} -vf "{vf}" -an '
        f'-c:v libx264 -preset veryfast -crf 12 -pix_fmt yuv420p -r 30 -t {dur} {shlex.quote(out)}')

def build(tag, segs, card, vo, total, ln, out):
    d = f"{SP}/seg/{tag}"; os.makedirs(d, exist_ok=True)
    if not (os.environ.get("REUSE") and os.path.exists(f"{d}/cat.mp4")):
        files = []
        for i, (a, b, sp, du) in enumerate(segs):
            o = f"{d}/{i:02d}.mp4"; files.append(o)
            seg(a, b, sp, du, o)
        lst = f"{d}/list.txt"
        open(lst, "w").write("".join(f"file '{f}'\n" for f in files))
        run(f'ffmpeg -y -v error -f concat -safe 0 -i {lst} -c copy {d}/cat.mp4')

    # hook card as a timed stream (the Sep 26 pattern), 0.00-2.00 with a fade out
    run(f'ffmpeg -y -v error -i {d}/cat.mp4 -loop 1 -t 2.0 -i {shlex.quote(card)} '
        f'-i {shlex.quote(vo)} -filter_complex '
        f'"[1:v]format=rgba,fps=30,fade=t=in:st=0:d=0.22:alpha=1,'
        f'fade=t=out:st=1.70:d=0.30:alpha=1,setpts=PTS-STARTPTS[c];'
        f'[0:v][c]overlay=0:0:eof_action=pass:repeatlast=0[v];'
        f'[v]format=yuv420p[vout];'
        f'[2:a]aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=stereo,'
        f'{ln},apad,atrim=0:{total},asetpts=PTS-STARTPTS[aout]" '
        f'-map "[vout]" -map "[aout]" -t {total} '
        f'-c:v libx264 -profile:v high -level 4.0 -preset slow -crf 19 -pix_fmt yuv420p '
        f'-r 30 -g 60 -c:a aac -b:a 192k -ar 48000 -movflags +faststart {shlex.quote(out)}')
    print("built", out)

LN_IG = ("loudnorm=I=-14:TP=-1.5:LRA=11:measured_I=-20.82:measured_TP=-2.46:"
         "measured_LRA=3.90:measured_thresh=-31.67:offset=1.82:linear=true,volume=-0.6dB")
LN_TT = ("loudnorm=I=-14:TP=-1.5:LRA=11:measured_I=-20.31:measured_TP=-2.51:"
         "measured_LRA=2.10:measured_thresh=-30.94:offset=1.54:linear=true,volume=-0.6dB")

# (start, end, speed, duration-out)
#  beat 1   the prompt sitting in the box, three PDFs attached, and the send tap
#  beats 2-4  each quote as ChatGPT opens it, ONE PER BEAT AT NORMAL SPEED
#  beat 5   the side-by-side table, all three columns
#  beat 6   the bottom line, all three real totals together
#
# The first build ran 3.15-11.55 at 3x as a single "generating" beat. That was
# wrong twice over, and the author caught both: the third quote renders at
# 12.3-13.9 so it was never in frame at all, and at 3x the two that were in
# frame got about half a second each — "too many abrupt flashes". The document
# views are the premise of the piece, not filler to ramp through, so each now
# gets a full second at 1.0x and the dead chat between them is cut instead.
# No speed ramp anywhere in this cut.
ig = [(1.30,  3.15, 1.0, 1.85),
      (6.45,  7.50, 1.0, 1.05),
      (9.45, 10.50, 1.0, 1.05),
      (12.45, 13.50, 1.0, 1.05),
      (17.50, 24.90, 1.0, 7.40),
      (30.90, 33.60, 1.0, 2.70)]
tt = [(1.45,  3.15, 1.0, 1.70),
      (6.45,  7.50, 1.0, 1.05),
      (9.45, 10.50, 1.0, 1.05),
      (12.45, 13.50, 1.0, 1.05),
      (17.55, 25.10, 1.0, 7.55),
      (30.90, 33.60, 1.0, 2.70)]

OUT = f"{SP}/out"; os.makedirs(OUT, exist_ok=True)
build("tt", tt, f"{C}/tt_hook.png", f"{SP}/vo/tt.mp3", sum(s[3] for s in tt), LN_TT,
      f"{OUT}/quotes-tiktok.mp4")
build("ig", ig, f"{C}/ig_hook.png", f"{SP}/vo/ig.mp3", sum(s[3] for s in ig), LN_IG,
      f"{OUT}/quotes-instagram.mp4")

for tag, segs in (("tiktok", tt), ("instagram", ig)):
    payoff = sum(x[3] for x in segs[:4])
    print(f"{tag:<10} total {sum(s[3] for s in segs):.2f}s   payoff at {payoff:.2f}s")
