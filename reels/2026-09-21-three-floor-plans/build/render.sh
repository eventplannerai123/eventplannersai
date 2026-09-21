#!/usr/bin/env bash
set -euo pipefail
SP=/tmp/claude-0/-home-user-eventplannersai/4079a8b4-9eb7-5c73-8b20-b79d77bad268/scratchpad
U=/root/.claude/uploads/4079a8b4-9eb7-5c73-8b20-b79d77bad268
A=$U/ff2d5a70-ScreenRecording_09-21-2026_10-47-32AM_1.mov
C=$U/8b589f28-ScreenRecording_09-21-2026_10-47-32AM_11.mov
VO=$U/e0c59efa-ElevenLabs_2026-09-21T14_10_33_Vanessa_-_Beach_Girl_pvc_sp106_s50_sb75_se0_b_m2.mp3
LN="loudnorm=I=-14:TP=-1.5:LRA=11:measured_I=-20.57:measured_TP=-3.91:measured_LRA=2.30:measured_thresh=-31.24:offset=${OFF:-0.55}:linear=true"
# Reveal ends at C 11.70: an Adobe Acrobat in-app ad scrolls into the bottom
# of frame at C ~11.85 (clean at 11.8, visible at 11.9).
CROP="crop=1206:2144:0:478,scale=1080:1920:flags=lanczos,setsar=1,fps=30"

# 1=hook 2=out 3=tapS 4=tapE 5=planS 6=planE 7=genS 8=genE 9=speed
# 10=Cstart 11=Cend 12=total 13=ecstart 14=ecdur 15=hookdur 16=hookfade
render () {
ffmpeg -y -v error \
 -i "$A" -i "$C" -loop 1 -t ${15} -i "$1" -loop 1 -t ${14} -i "$SP/cards0921/endcard.png" -i "$VO" \
 -filter_complex "
[0:v]split=3[a0][a1][a2];
[a0]trim=start=$3:end=$4,setpts=PTS-STARTPTS,fps=30[s1];
[a1]trim=start=$5:end=$6,setpts=PTS-STARTPTS,fps=30[s2];
[a2]trim=start=$7:end=$8,setpts=(PTS-STARTPTS)/$9,fps=30[s3];
[1:v]trim=start=${10}:end=${11},setpts=PTS-STARTPTS,fps=30[s4];
[s1][s2][s3][s4]concat=n=4:v=1:a=0[cat];
[cat]${CROP}[base];
[2:v]format=rgba,fps=30,fade=t=in:st=0:d=0.18:alpha=1,fade=t=out:st=${16}:d=0.30:alpha=1,setpts=PTS-STARTPTS[hk];
[3:v]format=rgba,fps=30,fade=t=in:st=0:d=0.35:alpha=1,setpts=PTS-STARTPTS+${13}/TB[ec];
[base][hk]overlay=0:0:eof_action=pass:repeatlast=0[v1];
[v1][ec]overlay=0:0:eof_action=pass:repeatlast=0,format=yuv420p[vout];
[4:a]aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=stereo,${LN},apad,atrim=0:${12},asetpts=PTS-STARTPTS[aout]" \
 -map "[vout]" -map "[aout]" -t ${12} \
 -c:v libx264 -profile:v high -level 4.0 -preset slow -crf 19 -pix_fmt yuv420p -r 30 -g 60 \
 -c:a aac -b:a 192k -ar 48000 -movflags +faststart "$2" 2>&1 | tail -3
}

#        hook                       out                                  tapS tapE planS planE genS genE  spd Cs   Ce    total ecstart ecdur hkdur hkfade
render "$SP/cards0921/hook_ig.png" "$SP/out0921/floorplans-instagram.mp4" 0.20 1.30 2.95 4.80 6.60 14.40 3.0 0.90 11.70 16.35 14.95   1.40  2.20  1.75
render "$SP/cards0921/hook_tt.png" "$SP/out0921/floorplans-tiktok.mp4"    0.15 1.32 2.95 4.75 6.60 14.10 2.8 0.80 11.70 16.54 15.09   1.45  2.10  1.65
