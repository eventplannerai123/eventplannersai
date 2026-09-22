#!/usr/bin/env python3
"""Coloring book reel - builds both cuts from the same source segments."""
import os, subprocess, shlex, sys

SP = "/tmp/claude-0/-home-user-eventplannersai/4079a8b4-9eb7-5c73-8b20-b79d77bad268/scratchpad"
U  = "/root/.claude/uploads/4079a8b4-9eb7-5c73-8b20-b79d77bad268"
IM = "/tmp/claude-0/-home-user-eventplannersai/4079a8b4-9eb7-5c73-8b20-b79d77bad268/images"

FLIP  = f"{U}/b0cb03e7-IMG_4030.mov"                                   # book flipping, 1458x1080 rot -180
LONG  = f"{U}/1448842b-ScreenRecording_09-22-2026_10-27-15AM_1.mov"    # send tap + generating, 1206x2622
SHORT = f"{U}/b06cd7cf-ScreenRecording_09-22-2026_10-27-15AM_1_3.mov"  # finishing up -> reveal

# 1206-wide capture: height = 1206/0.5625 = 2144, 478 off the top clears the
# status bar and the red recording dot. Recomputed for this source, per the guide.
SRCROP = "crop=1206:2144:0:478,scale=1080:1920:flags=lanczos,setsar=1"
# 1458x1080 landscape: 9:16 slice is 1080*0.5625 = 607.5 -> 608 wide, x=850 keeps the page.
FLIPCROP = "crop=608:1080:850:0,scale=1080:1920:flags=lanczos,setsar=1"

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

def build(tag, segs, vo, trim, total, ln, hook, endcard, ec_start, out):
    d = f"{SP}/seg/{tag}"; os.makedirs(d, exist_ok=True)
    files = []
    for i, s in enumerate(segs):
        o = f"{d}/{i:02d}.mp4"; files.append(o)
        if s[0] == "v":   seg_video(s[1], s[2], s[3], s[4], s[5], s[6], o)
        elif s[0] == "z": seg_zoom(s[1], s[2], s[3], s[4], o)
        elif s[0] == "p": seg_pan(s[1], s[2], s[3], s[4], o)
        print(f"  {tag} seg{i}: {s[0]} {round(float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',o],capture_output=True,text=True).stdout),3)}s")
    lst = f"{d}/list.txt"
    open(lst, "w").write("".join(f"file '{f}'\n" for f in files))
    run(f'ffmpeg -y -v error -f concat -safe 0 -i {lst} -c copy {d}/cat.mp4')

    hk_dur, hk_fade = 2.0, 1.70
    ec_dur = total - ec_start
    run(f'''ffmpeg -y -v error -i {d}/cat.mp4 \
 -loop 1 -t {hk_dur} -i {shlex.quote(hook)} -loop 1 -t {ec_dur} -i {shlex.quote(endcard)} -i {shlex.quote(vo)} \
 -filter_complex "
[1:v]format=rgba,fps=30,fade=t=in:st=0:d=0.18:alpha=1,fade=t=out:st={hk_fade}:d=0.30:alpha=1,setpts=PTS-STARTPTS[hk];
[2:v]format=rgba,fps=30,fade=t=in:st=0:d=0.35:alpha=1,setpts=PTS-STARTPTS+{ec_start}/TB[ec];
[0:v][hk]overlay=0:0:eof_action=pass:repeatlast=0[v1];
[v1][ec]overlay=0:0:eof_action=pass:repeatlast=0,format=yuv420p[vout];
[3:a]atrim=start={trim},asetpts=PTS-STARTPTS,aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=stereo,{ln},apad,atrim=0:{total},asetpts=PTS-STARTPTS[aout]" \
 -map "[vout]" -map "[aout]" -t {total} \
 -c:v libx264 -profile:v high -level 4.0 -preset slow -crf 19 -pix_fmt yuv420p -r 30 -g 60 \
 -c:a aac -b:a 192k -ar 48000 -movflags +faststart {shlex.quote(out)}''')
    print("built", out)

SHEET_W = f"{SP}/src_book/sheet_wide.png"
SHEET_C = f"{SP}/src_book/sheet_close.png"
P3940 = f"{SP}/src_book/3940.png"; P3939 = f"{SP}/src_book/3939.png"; P3927 = f"{SP}/src_book/3927.png"
HOLD  = f"{SP}/src_book/reveal_hold.png"   # last clean frame of the reveal, before the ad

OFF_IG = os.environ.get("OFF_IG", "0.87")
OFF_TT = os.environ.get("OFF_TT", "0.89")
LN_IG = ("loudnorm=I=-14:TP=-1.5:LRA=11:measured_I=-21.45:measured_TP=-2.80:"
         f"measured_LRA=2.70:measured_thresh=-32.10:offset={OFF_IG}:linear=true")
LN_TT = ("loudnorm=I=-14:TP=-1.5:LRA=11:measured_I=-21.29:measured_TP=-2.59:"
         f"measured_LRA=2.50:measured_thresh=-31.80:offset={OFF_TT}:linear=true")

# Reveal ends at SHORT 6.30: the Adobe Firefly in-app ad first shows at 6.6
# (clean at 6.4), and it fades in, so the cut keeps a margin.
ig = [
 ("v", FLIP,  0.00,  6.55, 1.0, 6.55, FLIPCROP),
 ("v", LONG,  0.00,  1.60, 1.0, 1.60, SRCROP),
 ("v", LONG,  1.60, 11.20, 3.0, 3.20, SRCROP),
 ("v", SHORT, 3.55,  6.30, 1.0, 2.75, SRCROP),
 ("z", HOLD,    0.85, 1.00, 1.00),
 ("z", SHEET_W, 6.25, 1.10, 1.75),
 ("z", P3940,   4.86, 1.00, 1.12),
 ("p", SHEET_C, 5.44, 400, 1300),
 ("z", P3939,   5.57, 1.00, 1.12),
 ("z", P3927,   6.93, 1.00, 1.12),
]
tt = [
 ("v", FLIP,  0.00,  5.05, 1.0, 5.05, FLIPCROP),
 ("v", LONG,  0.00,  1.40, 1.0, 1.40, SRCROP),
 ("v", LONG,  1.40,  9.80, 3.0, 2.80, SRCROP),
 ("v", SHORT, 3.05,  6.30, 1.0, 3.25, SRCROP),
 ("z", HOLD,    1.40, 1.00, 1.00),
 ("z", SHEET_W, 4.70, 1.10, 1.62),
 ("z", P3940,   5.20, 1.00, 1.12),
 ("p", SHEET_C, 4.70, 400, 1300),
 ("z", P3939,   4.10, 1.00, 1.12),
 ("z", P3927,   4.90, 1.00, 1.12),
]

os.makedirs(f"{SP}/out0922r", exist_ok=True)
build("ig", ig, f"{SP}/vo_book/final.mp3", 1.870, 44.00, LN_IG,
      f"{SP}/cards0922r/hook_ig.png", f"{SP}/cards0922r/end_ig.png", 40.80,
      f"{SP}/out0922r/coloringbook-instagram.mp4")
build("tt", tt, f"{SP}/vo_book/tiktok.mp3", 1.821, 37.50, LN_TT,
      f"{SP}/cards0922r/hook_tt.png", f"{SP}/cards0922r/end_tt.png", 34.30,
      f"{SP}/out0922r/coloringbook-tiktok.mp4")
