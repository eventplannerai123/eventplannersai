import subprocess, os
HERE=os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
SRC="source.mp4"; XF=0.20

# Three beats, per the guide's quick-piece format: the prompt held for 3s, then
# two key moments of the answer held long enough to read. No hook line, no end
# card, no voiceover.
#
# Each beat is cropped from the 1206x2622 capture. The first keeps the whole
# screen because it has to show the prompt in the box and the send tap; the
# other two zoom slightly (1100 wide) and shift down the source to centre the
# paragraph and then the table.
BEATS=[
    # (src_start, timeline_duration, crop)
    (0.30, 3.00, "crop=1206:2144:0:478"),   # prompt in the box, send tap
    (4.60, 4.20, "crop=1100:1956:53:478"),  # ~1,000 drinks total
    (9.20, 5.20, "crop=1100:1956:53:658"),  # the recommended order table
]

def run(c):
    p=subprocess.run(c,shell=True,capture_output=True,text=True)
    if p.returncode: raise SystemExit(p.stderr[-3000:])
    return p.stdout

segs=[]
for i,(ss,dur,crop) in enumerate(BEATS):
    out=f"seg{i}.mp4"; segs.append(out)
    # the source window is XF longer than the timeline span, so the dissolve
    # has frames to work with on both sides
    run(f'ffmpeg -y -loglevel error -ss {ss} -t {dur+XF} -i {SRC} '
        f'-an -vf "{crop},scale=1080:1920:flags=lanczos,setsar=1,fps=30" '
        f'-c:v libx264 -profile:v high -crf 19 -pix_fmt yuv420p {out}')

# chain the dissolves: offset_k = (time the next segment starts) - XF
inputs=" ".join(f"-i {s}" for s in segs)
fc=[]; prev="0:v"; acc=BEATS[0][1]
for k in range(1,len(segs)):
    lbl=f"x{k}"
    fc.append(f"[{prev}][{k}:v]xfade=transition=fade:duration={XF}:offset={acc-XF:.3f}[{lbl}]")
    prev=lbl; acc += BEATS[k][1] - XF
run(f'ffmpeg -y -loglevel error {inputs} -filter_complex "{";".join(fc)}" '
    f'-map "[{prev}]" -c:v libx264 -profile:v high -crf 19 -pix_fmt yuv420p -r 30 novo.mp4')

# the prompt card, held over the first 3 seconds only
run('ffmpeg -y -loglevel error -i novo.mp4 -i cards1004/prompt.png '
    '-filter_complex "[0:v][1:v]overlay=0:0:eof_action=repeat:repeatlast=1:'
    'enable=\'between(t,0,3)\'[v]" -map "[v]" '
    '-c:v libx264 -profile:v high -crf 19 -pix_fmt yuv420p -r 30 carded.mp4')

# a silent AAC track, so the file is not audio-less on upload
run('ffmpeg -y -loglevel error -i carded.mp4 -f lavfi -i anullsrc=r=48000:cl=stereo '
    '-shortest -c:v copy -c:a aac -b:a 192k -ar 48000 -movflags +faststart '
    '../barquantities-tiktok.mp4')
print(run('ffprobe -v error -show_entries stream=width,height,r_frame_rate,codec_name '
          '-show_entries format=duration,size -of default=noprint_wrappers=1 ../barquantities-tiktok.mp4'))
