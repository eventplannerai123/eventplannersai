#!/usr/bin/env python3
"""Client enquiry -> event brief reel, 2026-09-24. TikTok cut built first."""
import os, subprocess, shlex, sys

SP = "/tmp/claude-0/-home-user-eventplannersai/4079a8b4-9eb7-5c73-8b20-b79d77bad268/scratchpad"
U  = "/root/.claude/uploads/4079a8b4-9eb7-5c73-8b20-b79d77bad268"

C = f"{U}/8eeb2955-ScreenRecording_09-24-2026_8-28-49AM_1.mov"  # send tap + client message
B = f"{U}/5831a557-ScreenRecording_09-24-2026_8-28-49AM_1.mov"  # rest of message + the brief
A = f"{U}/4b51390e-ScreenRecording_09-24-2026_8-28-49AM_1.mov"  # questions + biggest items

# 1206 / 0.5625 = 2144; 478 off the top clears the status bar and recording dot.
CROP = "crop=1206:2144:0:478,scale=1080:1920:flags=lanczos,setsar=1"
HOOK = f"{SP}/cards0924/hook.png"

def run(cmd):
    p = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if p.returncode: print(cmd); print(p.stderr[-3000:]); sys.exit(1)

def seg(src, start, end, dur, out):
    vf = f"trim=start={start}:end={end},setpts=PTS-STARTPTS,{CROP},fps=30"
    run(f'ffmpeg -y -v error -i {shlex.quote(src)} -vf "{vf}" -an '
        f'-c:v libx264 -preset veryfast -crf 12 -pix_fmt yuv420p -r 30 -t {dur} {shlex.quote(out)}')

def build(tag, segs, vo, total, ln, out):
    d = f"{SP}/seg/{tag}"; os.makedirs(d, exist_ok=True)
    files = []
    for i, s in enumerate(segs):
        o = f"{d}/{i:02d}.mp4"; files.append(o); seg(*s, o)
    open(f"{d}/list.txt","w").write("".join(f"file '{f}'\n" for f in files))
    run(f'ffmpeg -y -v error -f concat -safe 0 -i {d}/list.txt -c copy {d}/cat.mp4')
    run(f'''ffmpeg -y -v error -i {d}/cat.mp4 -loop 1 -t 2.0 -i {shlex.quote(HOOK)} -i {shlex.quote(vo)} \
 -filter_complex "
[1:v]format=rgba,fps=30,fade=t=in:st=0:d=0.20:alpha=1,fade=t=out:st=1.75:d=0.25:alpha=1,setpts=PTS-STARTPTS[hk];
[0:v][hk]overlay=0:0:eof_action=pass:repeatlast=0,format=yuv420p[vout];
[2:a]aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=stereo,{ln},apad,atrim=0:{total},asetpts=PTS-STARTPTS[aout]" \
 -map "[vout]" -map "[aout]" -t {total} \
 -c:v libx264 -profile:v high -level 4.0 -preset slow -crf 19 -pix_fmt yuv420p -r 30 -g 60 \
 -c:a aac -b:a 192k -ar 48000 -movflags +faststart {shlex.quote(out)}''')
    print("built", out)

OFF_TT = os.environ.get("OFF_TT", "0.55")
OFF_IG = os.environ.get("OFF_IG", "0.55")
LN_TT = ("loudnorm=I=-14:TP=-1.5:LRA=11:measured_I=-21.19:measured_TP=-1.99:"
         f"measured_LRA=3.40:measured_thresh=-31.81:offset={OFF_TT}:linear=true")
LN_IG = ("loudnorm=I=-14:TP=-1.5:LRA=11:measured_I=-21.10:measured_TP=-3.33:"
         f"measured_LRA=2.80:measured_thresh=-31.67:offset={OFF_IG}:linear=true")

# Clip A stops at 12.40. A Cambridge "Event Florals in NYC" in-app ad follows
# the answer; 13.00 looked clean on a bottom-620px crop but the finished file
# showed the ad's lead line ("For the 60th birthday event brief, here's an
# event...") on its last frame. Scanned the full bottom 300px of the export:
# clean to 46.2s, text at 46.5s. 12.40 leaves margin, since these fade in.
tt = [ (C, 0.70, 17.05, 16.35), (B, 0.00, 15.90, 15.90), (A, 0.00, 12.40, 12.40) ]
ig = [ (C, 0.40, 17.05, 16.65), (B, 0.00, 16.86, 16.86), (A, 0.00, 12.40, 12.40) ]

os.makedirs(f"{SP}/out0924", exist_ok=True)
build("tt24", tt, f"{SP}/vo24/tiktok.mp3",    44.65, LN_TT, f"{SP}/out0924/enquiry-tiktok.mp4")
build("ig24", ig, f"{SP}/vo24/instagram.mp3", 45.91, LN_IG, f"{SP}/out0924/enquiry-instagram.mp4")
