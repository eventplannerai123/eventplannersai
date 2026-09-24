#!/usr/bin/env python3
"""Conference agenda -> staffing plan reel, 2026-09-26. TikTok built first."""
import os, subprocess, shlex, sys
SP="/tmp/claude-0/-home-user-eventplannersai/4079a8b4-9eb7-5c73-8b20-b79d77bad268/scratchpad"
U="/root/.claude/uploads/4079a8b4-9eb7-5c73-8b20-b79d77bad268"
R="/home/user/eventplannersai/reels/2026-09-26-staffing-plan"
C=f"{U}/6a5d0841-ScreenRecording_09-24-2026_10-46-57AM_1.mov"   # prompt, send tap, agenda
A=f"{U}/eb73268b-ScreenRecording_09-24-2026_10-46-57AM_1.mov"   # generating, staffing table, pinch points
B=f"{U}/d2e08ed3-ScreenRecording_09-24-2026_10-46-57AM_1.mov"   # breaks, bottom line
CROP="crop=1206:2144:0:478,scale=1080:1920:flags=lanczos,setsar=1"
HOOK=f"{SP}/cards0926/hook.png"
def run(c):
    p=subprocess.run(c,shell=True,capture_output=True,text=True)
    if p.returncode: print(c); print(p.stderr[-2500:]); sys.exit(1)
def seg(src,s,e,sp,dur,out):
    vf=f"trim=start={s}:end={e},setpts=(PTS-STARTPTS)/{sp},{CROP},fps=30"
    run(f'ffmpeg -y -v error -i {shlex.quote(src)} -vf "{vf}" -an -c:v libx264 -preset veryfast -crf 12 -pix_fmt yuv420p -r 30 -t {dur} {shlex.quote(out)}')
def build(tag,segs,vo,total,ln,out):
    d=f"{SP}/seg/{tag}"; os.makedirs(d,exist_ok=True); fs=[]
    for i,s in enumerate(segs):
        o=f"{d}/{i:02d}.mp4"; fs.append(o); seg(*s,o)
    open(f"{d}/list.txt","w").write("".join(f"file '{f}'\n" for f in fs))
    run(f'ffmpeg -y -v error -f concat -safe 0 -i {d}/list.txt -c copy {d}/cat.mp4')
    run(f'''ffmpeg -y -v error -i {d}/cat.mp4 -loop 1 -t 2.0 -i {shlex.quote(HOOK)} -i {shlex.quote(vo)} \
 -filter_complex "
[1:v]format=rgba,fps=30,fade=t=in:st=0:d=0.20:alpha=1,fade=t=out:st=1.75:d=0.25:alpha=1,setpts=PTS-STARTPTS[hk];
[0:v][hk]overlay=0:0:eof_action=pass:repeatlast=0,format=yuv420p[vout];
[2:a]aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=stereo,{ln},apad,atrim=0:{total},asetpts=PTS-STARTPTS[aout]" \
 -map "[vout]" -map "[aout]" -t {total} -c:v libx264 -profile:v high -level 4.0 -preset slow -crf 19 \
 -pix_fmt yuv420p -r 30 -g 60 -c:a aac -b:a 192k -ar 48000 -movflags +faststart {shlex.quote(out)}''')
    print("built",out)
OI=os.environ.get("OFF_IG","0.55"); OT=os.environ.get("OFF_TT","0.55")
LN_IG=("loudnorm=I=-14:TP=-1.5:LRA=11:measured_I=-21.36:measured_TP=-3.32:"
       f"measured_LRA=3.20:measured_thresh=-32.08:offset={OI}:linear=true")
LN_TT=("loudnorm=I=-14:TP=-1.5:LRA=11:measured_I=-21.59:measured_TP=-3.07:"
       f"measured_LRA=3.80:measured_thresh=-32.43:offset={OT}:linear=true")
# Clip B stops at 6.30: a GlossGenius in-app ad is clean at 6.4 and fully
# rendered at 6.7. The agenda hold and the generating wait are a representative
# slice at 2.8x, not the whole 16.6s compressed.
tt=[(C,0.00,1.80,1.0,1.80),(C,3.20,11.00,2.8,2.79),(A,0.80,4.20,2.8,1.21),(A,4.20,19.00,1.0,14.80),(B,0.00,6.30,1.0,6.30)]
ig=[(C,0.00,1.80,1.0,1.80),(C,3.20,11.00,2.8,2.79),(A,0.80,4.20,2.8,1.21),(A,4.20,19.00,1.0,14.80),(B,0.00,6.30,1.0,6.30)]
os.makedirs(f"{SP}/out0926",exist_ok=True)
build("tt26",tt,f"{R}/build/vo/tiktok.mp3",   26.90,LN_TT,f"{SP}/out0926/staffing-tiktok.mp4")
build("ig26",ig,f"{R}/build/vo/instagram.mp3",26.90,LN_IG,f"{SP}/out0926/staffing-instagram.mp4")
