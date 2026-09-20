#!/usr/bin/env bash
set -euo pipefail
SP=/tmp/claude-0/-home-user-eventplannersai/4079a8b4-9eb7-5c73-8b20-b79d77bad268/scratchpad
U=/root/.claude/uploads/4079a8b4-9eb7-5c73-8b20-b79d77bad268
A=$U/e80baefe-ScreenRecording_09-20-2026_9-30-33AM_1.mov
B=$U/0324c010-ScreenRecording_09-20-2026_9-30-33AM_1.mov
VO=$SP/vo0920/takeA.mp3
LN="loudnorm=I=-14:TP=-1.5:LRA=11:measured_I=-20.37:measured_TP=-2.57:measured_LRA=2.20:measured_thresh=-30.73:offset=${OFF:-0.00}:linear=true"
CROP="crop=1206:2144:0:478,scale=1080:1920:flags=lanczos,setsar=1,fps=30"

# 1=hook 2=out 3=s1start 4=s1end 5=speed 6=s2end 7=Bstart 8=Bend
# 9=total 10=ecstart 11=ecdur 12=hookdur 13=hookfade
render () {
ffmpeg -y -v error \
 -i "$A" -i "$B" -loop 1 -t ${12} -i "$1" -loop 1 -t ${11} -i "$SP/cards0920/endcard.png" -i "$VO" \
 -filter_complex "
[0:v]split=3[a0][a1][a2];
[a0]trim=start=$3:end=$4,setpts=PTS-STARTPTS,fps=30[s1];
[a1]trim=start=$4:end=$6,setpts=(PTS-STARTPTS)/$5,fps=30[s2];
[a2]trim=start=$6:end=15.75,setpts=PTS-STARTPTS,fps=30[s3];
[1:v]trim=start=$7:end=$8,setpts=PTS-STARTPTS,fps=30[s4];
[s1][s2][s3][s4]concat=n=4:v=1:a=0[cat];
[cat]${CROP}[base];
[2:v]format=rgba,fps=30,fade=t=in:st=0:d=0.18:alpha=1,fade=t=out:st=${13}:d=0.30:alpha=1,setpts=PTS-STARTPTS[hk];
[3:v]format=rgba,fps=30,fade=t=in:st=0:d=0.35:alpha=1,setpts=PTS-STARTPTS+${10}/TB[ec];
[base][hk]overlay=0:0:eof_action=pass:repeatlast=0[v1];
[v1][ec]overlay=0:0:eof_action=pass:repeatlast=0,format=yuv420p[vout];
[4:a]aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=stereo,${LN},apad,atrim=0:$9,asetpts=PTS-STARTPTS[aout]" \
 -map "[vout]" -map "[aout]" -t $9 \
 -c:v libx264 -profile:v high -level 4.0 -preset slow -crf 19 -pix_fmt yuv420p -r 30 -g 60 \
 -c:a aac -b:a 192k -ar 48000 -movflags +faststart "$2" 2>&1 | tail -3
}

#        hook                      out                                 s1s   s1e   spd  s2end  Bs    Be      total ecstart ecdur hookdur hookfade
render "$SP/cards0920/hook_ig.png" "$SP/out0920/contract-instagram.mp4" 1.00 2.20 3.0  10.55  1.70  8.71667 16.20 14.80   1.40  2.20    1.75
render "$SP/cards0920/hook_tt.png" "$SP/out0920/contract-tiktok.mp4"    0.95 2.25 2.8  10.55  2.10  9.13571 16.50 15.05   1.45  2.10    1.65
