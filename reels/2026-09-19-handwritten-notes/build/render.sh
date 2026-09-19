#!/usr/bin/env bash
set -euo pipefail
SP=/tmp/claude-0/-home-user-eventplannersai/4079a8b4-9eb7-5c73-8b20-b79d77bad268/scratchpad
U=/root/.claude/uploads/4079a8b4-9eb7-5c73-8b20-b79d77bad268
A=$U/4613d4be-ScreenRecording_09-19-2026_7-25-15AM_1.mov
B=$U/605be4a8-ScreenRecording_09-19-2026_7-25-15AM_1.mov
VO=$U/17c81512-ElevenLabs_2026-09-19T11_21_25_Vanessa_-_Beach_Girl_pvc_sp109_s50_sb75_se0_b_m2_2.mp3
LN="loudnorm=I=-14:TP=-1.5:LRA=11:measured_I=-21.18:measured_TP=-1.94:measured_LRA=4.30:measured_thresh=-31.99:offset=1.22:linear=true"
CROP="crop=1206:2144:0:478,scale=1080:1920:flags=lanczos,setsar=1,fps=30"

# 1=hook 2=out 3=tapStart 4=tapEnd 5=holdLoop 6=speed 7=seg2end 8=Bstart
# 9=total 10=ecstart 11=ecdur 12=hookdur 13=hookfade
render () {
ffmpeg -y -v error \
 -i "$A" -i "$B" -loop 1 -t ${12} -i "$1" -loop 1 -t ${11} -i "$SP/cards0919/endcard.png" -i "$VO" \
 -filter_complex "
[0:v]split=4[a0][a1][a2][a3];
[a0]trim=start=$3:end=$4,setpts=PTS-STARTPTS,fps=30[s1a];
[a1]trim=start=5.10:end=6.40,setpts=PTS-STARTPTS,fps=30[s1b];
[a2]trim=start=6.30:end=6.35,setpts=PTS-STARTPTS,fps=30,select='eq(n\,0)',loop=loop=$5:size=1:start=0,setpts=N/30/TB[s1c];
[a3]trim=start=6.40:end=$7,setpts=(PTS-STARTPTS)/$6,fps=30[s2];
[1:v]trim=start=$8:end=14.30,setpts=PTS-STARTPTS,fps=30[s3];
[s1a][s1b][s1c][s2][s3]concat=n=5:v=1:a=0[cat];
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

#        hook                      out                                tapS  tapE  hold speed s2end Bstart total ecstart ecdur hookdur hookfade
render "$SP/cards0919/hook_ig.png" "$SP/out0919/notes-instagram.mp4"  0.35  1.25  23   2.44  12.50 2.65   17.15 15.75   1.40  2.20    1.75
render "$SP/cards0919/hook_tt.png" "$SP/out0919/notes-tiktok.mp4"     0.30  1.32  20   2.30  12.30 2.45   17.43 15.98   1.45  2.10    1.65
