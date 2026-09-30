#!/usr/bin/env python3
"""Oct 1 vendor quotes reel.

Segments are rendered one at a time and then cross-faded: a single filtergraph
decodes the whole HEVC source once per branch and gets OOM-killed on a 51 MB
file (Sep 28).

No speed ramp anywhere. ChatGPT opens each attached PDF full-screen in turn
(Stagecraft 6.3-7.9, Meridian 9.3-10.9, Clearline 12.3-13.9) and those three
views are the premise of the piece, so each gets its own beat at 1.0x rather
than being ramped through as "generating". Each beat starts ~0.25s after its
document appears: ChatGPT shows a "Loading" spinner first, and starting on the
render boundary pulled that spinner into the dissolve.

Cuts are 0.20s dissolves, and the beat boundaries are placed on the
voiceover's own phrase gaps (measured with silencedetect) so picture and
narration turn over together.
"""
import os, subprocess, shlex, sys

SP  = "/tmp/claude-0/-home-user-eventplannersai/4079a8b4-9eb7-5c73-8b20-b79d77bad268/scratchpad/oct01"
SRC = f"{SP}/src.mov"
C   = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cards1001")
XF  = 0.20   # dissolve length

# 1206x2622 iPhone capture: 1206/0.5625 = 2144, 478 off the top so the status
# bar and the recording dot fall away and the input bar stays at the bottom.
CROP = "crop=1206:2144:0:478,scale=1080:1920:flags=lanczos,setsar=1"

def run(cmd):
    p = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if p.returncode:
        print(cmd); print(p.stderr[-3000:]); sys.exit(1)

def seg(start, end, out):
    dur = round(end - start, 3)
    vf = f"trim=start={start}:end={end},setpts=PTS-STARTPTS,{CROP},fps=30"
    run(f'ffmpeg -y -v error -i {shlex.quote(SRC)} -vf "{vf}" -an '
        f'-c:v libx264 -preset veryfast -crf 12 -pix_fmt yuv420p -r 30 -t {dur} {shlex.quote(out)}')
    return dur

def build(tag, segs, card, vo, ln, out):
    d = f"{SP}/seg/{tag}"; os.makedirs(d, exist_ok=True)
    files, durs = [], []
    for i, (a, b) in enumerate(segs):
        o = f"{d}/{i:02d}.mp4"; files.append(o)
        durs.append(seg(a, b, o))

    # chain the dissolves; offset_k is the accumulated length so far minus XF
    ins = " ".join(f"-i {shlex.quote(f)}" for f in files)
    fil, prev, acc = [], "0:v", durs[0]
    for k in range(1, len(files)):
        off = round(acc - XF, 3)
        fil.append(f"[{prev}][{k}:v]xfade=transition=fade:duration={XF}:offset={off}[x{k}];")
        prev = f"x{k}"
        acc = round(acc + durs[k] - XF, 3)
    total = acc

    run(f'ffmpeg -y -v error {ins} -loop 1 -t 2.0 -i {shlex.quote(card)} '
        f'-i {shlex.quote(vo)} -filter_complex '
        f'"{"".join(fil)}'
        f'[{len(files)}:v]format=rgba,fps=30,fade=t=in:st=0:d=0.22:alpha=1,'
        f'fade=t=out:st=1.70:d=0.30:alpha=1,setpts=PTS-STARTPTS[c];'
        f'[{prev}][c]overlay=0:0:eof_action=pass:repeatlast=0[v];'
        f'[v]format=yuv420p[vout];'
        f'[{len(files)+1}:a]aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=stereo,'
        f'{ln},apad,atrim=0:{total},asetpts=PTS-STARTPTS[aout]" '
        f'-map "[vout]" -map "[aout]" -t {total} '
        f'-c:v libx264 -profile:v high -level 4.0 -preset slow -crf 19 -pix_fmt yuv420p '
        f'-r 30 -g 60 -c:a aac -b:a 192k -ar 48000 -movflags +faststart {shlex.quote(out)}')
    return total, durs

LN_IG = ("loudnorm=I=-14:TP=-1.5:LRA=11:measured_I=-20.82:measured_TP=-2.46:"
         "measured_LRA=3.90:measured_thresh=-31.67:offset=1.82:linear=true,volume=-0.6dB")
LN_TT = ("loudnorm=I=-14:TP=-1.5:LRA=11:measured_I=-20.31:measured_TP=-2.51:"
         "measured_LRA=2.10:measured_thresh=-30.94:offset=1.54:linear=true,volume=-0.6dB")

# Source windows. Each is XF longer than its span on the finished timeline,
# because every dissolve eats 0.20s of the pair it joins.
#
# Instagram voiceover phrase gaps: 1.91 | 4.31 | 8.07 | 10.62 | 11.89 | 13.15
#   "Three AV quotes for the same job,"            0.00-1.91  -> prompt + send tap
#   "and not one of them lists the same things."   2.27-4.31  -> the three quotes
#   "Here's all three side by side..."             4.93-8.07  -> the table
#   "and where each one is hiding the cost."       8.57-10.62 -> the table
#   "The cheapest one isn't the cheapest."         11.17-13.15 -> the bottom line
ig = [(1.00,  3.15),    # prompt in the box, three PDFs attached, send tap
      (6.55,  7.80),    # Stagecraft, full screen
      (9.55, 10.80),    # Meridian
      (12.55, 13.80),   # Clearline
      (17.50, 23.80),   # the side-by-side table
      (29.75, 33.60)]   # scrolls into the bottom line, all three totals

# TikTok voiceover phrase gaps: 2.36 | 4.39 | 6.76 | 8.98 | 12.33
#   "Stop comparing the totals on vendor quotes."  0.00-2.36  -> prompt + send tap
#   "These three are for the same job, and not
#    one of them lists the same things."           2.89-6.76  -> the three quotes
#   "Here's all three side by side -"              7.38-8.98  -> the table
#   "and the cheapest quote is ten thousand
#    dollars more than it looks."                  9.39-12.72 -> table, then bottom
tt = [(0.95,  3.15),    # shorter than Instagram's opening: TikTok is the
      (6.40,  7.70),    # primary platform, so keep more margin under the
      (9.40, 10.70),    # six-second ceiling (payoff 5.50 against 5.30)
      (12.40, 13.70),
      (17.55, 24.05),
      (30.10, 33.60)]

OUT = f"{SP}/out"; os.makedirs(OUT, exist_ok=True)
for tag, segs, card, vo, ln, name in (
        ("tt", tt, f"{C}/tt_hook.png", f"{SP}/vo/tt.mp3", LN_TT, "quotes-tiktok"),
        ("ig", ig, f"{C}/ig_hook.png", f"{SP}/vo/ig.mp3", LN_IG, "quotes-instagram")):
    total, durs = build(tag, segs, card, vo, ln, f"{OUT}/{name}.mp4")
    # payoff = everything before the table, i.e. the first four beats on the timeline
    payoff = round(sum(durs[:4]) - 3*XF, 2)
    print(f"{name:<20} total {total:.2f}s   payoff at {payoff:.2f}s   "
          f"beats {[round(x,2) for x in durs]}")
