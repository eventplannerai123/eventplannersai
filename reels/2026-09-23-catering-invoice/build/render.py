#!/usr/bin/env python3
"""Catering invoice vs BEO reel - 2026-09-23. TikTok cut built first, per the brief."""
import os, subprocess, shlex, sys

SP = "/tmp/claude-0/-home-user-eventplannersai/4079a8b4-9eb7-5c73-8b20-b79d77bad268/scratchpad"
U  = "/root/.claude/uploads/4079a8b4-9eb7-5c73-8b20-b79d77bad268"

A = f"{U}/3b1cdbd3-ScreenRecording_09-23-2026_7-56-34AM_1.mov"   # send tap + generating
B = f"{U}/d8e5c939-ScreenRecording_09-23-2026_7-56-34AM_1.mov"   # final reconciliation
C = f"{U}/38069f25-ScreenRecording_09-23-2026_7-56-34AM_1.mov"   # bottom line + itemised

# 1206-wide capture: 1206 / 0.5625 = 2144, y-offset 478 clears the status bar
# and the recording dot. Recomputed from this source, as the brief specifies.
CROP = "crop=1206:2144:0:478,scale=1080:1920:flags=lanczos,setsar=1"
HOOK = f"{SP}/cards0923/hook.png"

def run(cmd):
    p = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if p.returncode:
        print(cmd); print(p.stderr[-3000:]); sys.exit(1)

def seg(src, start, end, speed, dur, out):
    vf = f"trim=start={start}:end={end},setpts=(PTS-STARTPTS)/{speed},{CROP},fps=30"
    run(f'ffmpeg -y -v error -i {shlex.quote(src)} -vf "{vf}" -an '
        f'-c:v libx264 -preset veryfast -crf 12 -pix_fmt yuv420p -r 30 -t {dur} {shlex.quote(out)}')

def build(tag, segs, vo, total, ln, out):
    d = f"{SP}/seg/{tag}"; os.makedirs(d, exist_ok=True)
    files = []
    for i, s in enumerate(segs):
        o = f"{d}/{i:02d}.mp4"; files.append(o); seg(*s, o)
    open(f"{d}/list.txt","w").write("".join(f"file '{f}'\n" for f in files))
    run(f'ffmpeg -y -v error -f concat -safe 0 -i {d}/list.txt -c copy {d}/cat.mp4')
    # Hook only. Round 6 ends on the output itself - no end card.
    run(f'''ffmpeg -y -v error -i {d}/cat.mp4 -loop 1 -t 2.0 -i {shlex.quote(HOOK)} -i {shlex.quote(vo)} \
 -filter_complex "
[1:v]format=rgba,fps=30,fade=t=in:st=0:d=0.20:alpha=1,fade=t=out:st=1.75:d=0.25:alpha=1,setpts=PTS-STARTPTS[hk];
[0:v][hk]overlay=0:0:eof_action=pass:repeatlast=0,format=yuv420p[vout];
[2:a]aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=stereo,{ln},apad,atrim=0:{total},asetpts=PTS-STARTPTS[aout]" \
 -map "[vout]" -map "[aout]" -t {total} \
 -c:v libx264 -profile:v high -level 4.0 -preset slow -crf 19 -pix_fmt yuv420p -r 30 -g 60 \
 -c:a aac -b:a 192k -ar 48000 -movflags +faststart {shlex.quote(out)}''')
    print("built", out)

OFF_TT = os.environ.get("OFF_TT", "0.90")
OFF_IG = os.environ.get("OFF_IG", "0.90")
LN_TT = ("loudnorm=I=-14:TP=-1.5:LRA=11:measured_I=-20.44:measured_TP=-3.34:"
         f"measured_LRA=2.70:measured_thresh=-30.98:offset={OFF_TT}:linear=true")
LN_IG = ("loudnorm=I=-14:TP=-1.5:LRA=11:measured_I=-20.72:measured_TP=-3.06:"
         f"measured_LRA=2.90:measured_thresh=-31.72:offset={OFF_IG}:linear=true")

# Reveal from clip B stops at 9.00: a Rillion "AI for Accounts Payable" in-app
# ad is clean at 9.1 and legible at 9.4, and these fade in.
tt = [
 (A, 0.00, 1.90, 1.0,  1.90),   # prompt in the box, both PDFs attached, send tap
 (A, 1.95, 8.25, 2.50, 2.52),   # generating
 (C, 2.00, 6.20, 1.0,  4.20),   # Bottom line - $4,356.59
 (C, 6.20, 9.60, 1.0,  3.40),   # itemised BEO mismatches
 (B, 5.90, 9.00, 1.0,  3.10),   # final reconciliation, credit due
]
ig = [
 (A, 0.00, 1.75, 1.0,  1.75),
 (A, 1.85, 8.25, 2.30, 2.78),
 (C, 2.00, 6.20, 1.0,  4.20),
 (C, 6.20, 9.80, 1.0,  3.60),
 (B, 5.90, 9.00, 1.0,  3.10),
]

os.makedirs(f"{SP}/out0923", exist_ok=True)
build("tt23", tt, f"{SP}/vo23/tiktok.mp3",    15.12, LN_TT, f"{SP}/out0923/invoice-tiktok.mp4")
build("ig23", ig, f"{SP}/vo23/instagram.mp3", 15.43, LN_IG, f"{SP}/out0923/invoice-instagram.mp4")
