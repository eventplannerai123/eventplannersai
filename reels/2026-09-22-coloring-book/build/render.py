#!/usr/bin/env python3
"""Coloring book reel - built to reel_script_1.txt (per-beat text cards, its
beat order, its caption). Both cuts from the same source segments."""
import os, subprocess, shlex, sys

SP = "/tmp/claude-0/-home-user-eventplannersai/4079a8b4-9eb7-5c73-8b20-b79d77bad268/scratchpad"
U  = "/root/.claude/uploads/4079a8b4-9eb7-5c73-8b20-b79d77bad268"

FLIP  = f"{U}/b0cb03e7-IMG_4030.mov"                                   # book flipping, 1458x1080 rot -180
LONG  = f"{U}/1448842b-ScreenRecording_09-22-2026_10-27-15AM_1.mov"    # send tap + generating, 1206x2622
SHORT = f"{U}/b06cd7cf-ScreenRecording_09-22-2026_10-27-15AM_1_3.mov"  # finishing up -> reveal

SRCROP   = "crop=1206:2144:0:478,scale=1080:1920:flags=lanczos,setsar=1"
FLIPCROP = "crop=608:1080:850:0,scale=1080:1920:flags=lanczos,setsar=1"

C = f"{SP}/cards0922s"
SHEET_W = f"{SP}/src_book/sheet_wide.png"
SHEET_C = f"{SP}/src_book/sheet_close.png"
P3940 = f"{SP}/src_book/3940.png"; P3939 = f"{SP}/src_book/3939.png"; P3927 = f"{SP}/src_book/3927.png"
HOLD  = f"{SP}/src_book/reveal_hold.png"
COVER = f"{SP}/src_book/cover.png"

def run(cmd):
    p = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if p.returncode:
        print(cmd); print(p.stderr[-3000:]); sys.exit(1)

def seg_video(src, start, end, speed, dur, crop, out):
    vf = f"trim=start={start}:end={end},setpts=(PTS-STARTPTS)/{speed},{crop},fps=30"
    run(f'ffmpeg -y -v error -i {shlex.quote(src)} -vf "{vf}" -an '
        f'-c:v libx264 -preset veryfast -crf 12 -pix_fmt yuv420p -r 30 -t {dur} {shlex.quote(out)}')

def seg_zoom(still, dur, z0, z1, out):
    rate = (z1 - z0) / (dur * 30.0)
    vf = (f"zoompan=z='min({z0}+{rate:.7f}*on,{z1})':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'"
          f":d=1:s=1080x1920:fps=30")
    run(f'ffmpeg -y -v error -loop 1 -framerate 30 -t {dur} -i {shlex.quote(still)} -vf "{vf}" -an '
        f'-c:v libx264 -preset veryfast -crf 12 -pix_fmt yuv420p -r 30 -t {dur} {shlex.quote(out)}')

def seg_pan(still, dur, x0, x1, out):
    vf = f"crop=1080:1920:x='{x0}+({x1}-{x0})*t/{dur}':y=0,fps=30"
    run(f'ffmpeg -y -v error -loop 1 -framerate 30 -t {dur} -i {shlex.quote(still)} -vf "{vf}" -an '
        f'-c:v libx264 -preset veryfast -crf 12 -pix_fmt yuv420p -r 30 -t {dur} {shlex.quote(out)}')

def build(tag, segs, cards, vo, trim, total, ln, out):
    d = f"{SP}/seg/{tag}"; os.makedirs(d, exist_ok=True)
    if os.environ.get("REUSE") and os.path.exists(f"{d}/cat.mp4"):
        segs = []          # concat already built; skip straight to the overlay pass
    files = []
    for i, s in enumerate(segs):
        o = f"{d}/{i:02d}.mp4"; files.append(o)
        if s[0] == "v":   seg_video(s[1], s[2], s[3], s[4], s[5], s[6], o)
        elif s[0] == "z": seg_zoom(s[1], s[2], s[3], s[4], o)
        elif s[0] == "p": seg_pan(s[1], s[2], s[3], s[4], o)
    if files:
        lst = f"{d}/list.txt"
        open(lst, "w").write("".join(f"file '{f}'\n" for f in files))
        run(f'ffmpeg -y -v error -f concat -safe 0 -i {lst} -c copy {d}/cat.mp4')

    # one -loop input per card, then chained overlays
    ins, fil, prev = [], [], "0:v"
    for n, (png, start, dur, fade_at) in enumerate(cards):
        idx = n + 1
        ins.append(f"-loop 1 -t {dur} -i {shlex.quote(png)}")
        fo = f",fade=t=out:st={fade_at}:d=0.30:alpha=1" if fade_at is not None else ""
        fil.append(f"[{idx}:v]format=rgba,fps=30,fade=t=in:st=0:d=0.22:alpha=1{fo},"
                   f"setpts=PTS-STARTPTS+{start}/TB[c{n}];")
        fil.append(f"[{prev}][c{n}]overlay=0:0:eof_action=pass:repeatlast=0[v{n}];")
        prev = f"v{n}"
    aidx = len(cards) + 1
    fil.append(f"[{prev}]format=yuv420p[vout];")
    fil.append(f"[{aidx}:a]atrim=start={trim},asetpts=PTS-STARTPTS,"
               f"aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=stereo,{ln},"
               f"apad,atrim=0:{total},asetpts=PTS-STARTPTS[aout]")
    run(f'ffmpeg -y -v error -i {d}/cat.mp4 {" ".join(ins)} -i {shlex.quote(vo)} '
        f'-filter_complex "{"".join(fil)}" -map "[vout]" -map "[aout]" -t {total} '
        f'-c:v libx264 -profile:v high -level 4.0 -preset slow -crf 19 -pix_fmt yuv420p -r 30 -g 60 '
        f'-c:a aac -b:a 192k -ar 48000 -movflags +faststart {shlex.quote(out)}')
    print("built", out)

LN_IG = ("loudnorm=I=-14:TP=-1.5:LRA=11:measured_I=-22.28:measured_TP=-2.72:"
         "measured_LRA=2.90:measured_thresh=-32.77:offset=1.19:linear=true")
LN_TT = ("loudnorm=I=-14:TP=-1.5:LRA=11:measured_I=-21.25:measured_TP=-2.09:"
         "measured_LRA=2.80:measured_thresh=-31.74:offset=0.89:linear=true")

# Beat order follows the script: 1 book flipping, 2 screen recording,
# 3 contact sheet, 4 proof copy open, 5 half-coloured page with pencils.
ig = [
 ("v", FLIP,  0.00,  6.15, 1.0, 6.15, FLIPCROP),   # beat 1
 ("v", LONG,  0.00,  1.60, 1.0, 1.60, SRCROP),     # beat 2
 ("v", LONG,  1.60, 11.20, 3.0, 3.20, SRCROP),
 ("v", SHORT, 3.55,  6.30, 1.0, 2.75, SRCROP),
 ("z", HOLD,    0.85, 1.00, 1.00),
 ("z", SHEET_W, 6.05, 1.10, 1.75),                 # beat 3 - all 50 pages
 ("p", SHEET_C, 3.60, 400, 1200),
 ("z", P3940,   6.00, 1.00, 1.12),                 # beat 4 - proof copy open
 ("z", P3939,   6.40, 1.00, 1.12),
 ("z", P3927,   4.30, 1.00, 1.10),                 # beat 5 - pencils, slow push in
 ("z", COVER,   3.80, 1.00, 1.06),                 # beat 5 close - cover art
]
ig_cards = [
 (f"{C}/c1_hook.png",   0.00, 2.60, 2.30),
 (f"{C}/c2_tools.png",  6.50, 3.10, 2.80),
 (f"{C}/c3_images.png",14.65, 2.90, 2.60),
 (f"{C}/c4_app.png",   17.75, 5.25, 4.95),
 (f"{C}/c5_ninety.png",24.55, 4.05, 3.75),
 (f"{C}/c6_ten.png",   33.20, 3.40, 3.10),
 (f"{C}/c7_end.png",   41.30, 3.40, None),
]
tt = [
 ("v", FLIP,  0.00,  6.95, 1.0, 6.95, FLIPCROP),
 ("v", LONG,  0.00,  1.60, 1.0, 1.60, SRCROP),
 ("v", LONG,  1.60, 10.00, 3.0, 2.80, SRCROP),
 ("v", SHORT, 3.05,  6.30, 1.0, 3.25, SRCROP),
 ("z", HOLD,    1.00, 1.00, 1.00),
 ("z", SHEET_W, 4.70, 1.10, 1.62),
 ("p", SHEET_C, 4.60, 400, 1250),
 ("z", P3940,   5.40, 1.00, 1.12),
 ("z", P3939,   3.70, 1.00, 1.12),
 ("z", P3927,   2.20, 1.00, 1.08),
 ("z", COVER,   2.75, 1.00, 1.05),
]
tt_cards = [
 (f"{C}/c1_hook.png",   0.00, 2.60, 2.30),
 (f"{C}/c2_tools.png",  7.20, 3.00, 2.70),
 (f"{C}/c3_images.png",15.70, 3.20, 2.90),
 (f"{C}/c4_app.png",   19.10, 5.50, 5.20),
 (f"{C}/c5_ninety.png",25.25, 2.05, 1.75),
 (f"{C}/c6_ten.png",   27.55, 2.45, 2.15),
 (f"{C}/c7_end.png",   36.50, 2.45, None),
]

os.makedirs(f"{SP}/out0922s", exist_ok=True)
# ig2c/tt2c are already lead-trimmed and pause-tightened, so trim=0.
build("ig4", ig, ig_cards, f"{SP}/vo_book/ig2c.mp3", 0.0, 44.70, LN_IG,
      f"{SP}/out0922s/coloringbook-instagram.mp4")
build("tt4", tt, tt_cards, f"{SP}/vo_book/tt2c.mp3", 0.0, 38.95, LN_TT,
      f"{SP}/out0922s/coloringbook-tiktok.mp4")
