#!/usr/bin/env bash
# Rebuilds both cuts of the wedding getting-ready timeline reel.
# Usage: render.sh <screen-recording.mp4> <voiceover.mp3> <output-dir>
set -euo pipefail

SRC="$1"; VO="$2"; OUT="$3"
CARDS="$(dirname "$0")/cards"
mkdir -p "$OUT"

# Source recording is 1206x2622 (taller than 9:16). Crop to 1206x2144 at y=478,
# which drops the status bar and floating header buttons off the top and keeps
# the full ChatGPT input bar at the bottom, then scale to 1080x1920.
CROP="crop=1206:2144:0:478,scale=1080:1920:flags=lanczos,setsar=1,fps=30"

# Voiceover measures -20.34 LUFS / -3.16 dBTP. Two-pass loudnorm to -14 LUFS.
LN="loudnorm=I=-14:TP=-1.5:LRA=11:measured_I=-20.34:measured_TP=-3.16:measured_LRA=2.80:measured_thresh=-30.94:offset=1.32:linear=true"

# Instagram: 16.32s. Ramp is 3.0x.
ffmpeg -y -v error \
  -i "$SRC" \
  -loop 1 -t 2.40 -i "$CARDS/hook_ig.png" \
  -loop 1 -t 4.95 -i "$CARDS/endcard.png" \
  -i "$VO" \
  -filter_complex "
[0:v]split=3[s0][s1][s2];
[s0]trim=start=0.20:end=2.70,setpts=PTS-STARTPTS,fps=30[a];
[s1]trim=start=2.70:end=14.70,setpts=(PTS-STARTPTS)/3.0,fps=30[b];
[s2]trim=start=16.90:end=26.72,setpts=PTS-STARTPTS,fps=30[c];
[a][b][c]concat=n=3:v=1:a=0[cat];
[cat]${CROP}[base];
[1:v]format=rgba,fps=30,fade=t=in:st=0:d=0.20:alpha=1,fade=t=out:st=2.00:d=0.30:alpha=1,setpts=PTS-STARTPTS[hk];
[2:v]format=rgba,fps=30,fade=t=in:st=0:d=0.35:alpha=1,setpts=PTS-STARTPTS+11.40/TB[ec];
[base][hk]overlay=0:0:eof_action=pass:repeatlast=0[v1];
[v1][ec]overlay=0:0:eof_action=pass:repeatlast=0,format=yuv420p[vout];
[3:a]aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=stereo,${LN},apad,atrim=0:16.32,asetpts=PTS-STARTPTS[aout]" \
  -map "[vout]" -map "[aout]" -t 16.32 \
  -c:v libx264 -profile:v high -level 4.0 -preset slow -crf 19 -pix_fmt yuv420p -r 30 -g 60 \
  -c:a aac -b:a 192k -ar 48000 -movflags +faststart \
  "$OUT/wedding-timeline-instagram.mp4"

# TikTok: 16.51s. Shorter open, 2.6x ramp, longer reveal hold.
ffmpeg -y -v error \
  -i "$SRC" \
  -loop 1 -t 2.30 -i "$CARDS/hook_tt.png" \
  -loop 1 -t 5.25 -i "$CARDS/endcard.png" \
  -i "$VO" \
  -filter_complex "
[0:v]split=3[s0][s1][s2];
[s0]trim=start=0.20:end=2.30,setpts=PTS-STARTPTS,fps=30[a];
[s1]trim=start=2.30:end=13.20,setpts=(PTS-STARTPTS)/2.6,fps=30[b];
[s2]trim=start=16.50:end=26.72,setpts=PTS-STARTPTS,fps=30[c];
[a][b][c]concat=n=3:v=1:a=0[cat];
[cat]${CROP}[base];
[1:v]format=rgba,fps=30,fade=t=in:st=0:d=0.15:alpha=1,fade=t=out:st=1.90:d=0.30:alpha=1,setpts=PTS-STARTPTS[hk];
[2:v]format=rgba,fps=30,fade=t=in:st=0:d=0.35:alpha=1,setpts=PTS-STARTPTS+11.30/TB[ec];
[base][hk]overlay=0:0:eof_action=pass:repeatlast=0[v1];
[v1][ec]overlay=0:0:eof_action=pass:repeatlast=0,format=yuv420p[vout];
[3:a]aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=stereo,${LN},apad,atrim=0:16.51,asetpts=PTS-STARTPTS[aout]" \
  -map "[vout]" -map "[aout]" -t 16.51 \
  -c:v libx264 -profile:v high -level 4.0 -preset slow -crf 19 -pix_fmt yuv420p -r 30 -g 60 \
  -c:a aac -b:a 192k -ar 48000 -movflags +faststart \
  "$OUT/wedding-timeline-tiktok.mp4"

echo "Rendered both cuts into $OUT"
