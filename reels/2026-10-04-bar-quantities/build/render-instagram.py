#!/usr/bin/env python3
"""Bar quantities, Instagram cut - the Oct 4 TikTok piece with a voiceover.

The TikTok cut shipped silent on Oct 4, one day before the video lessons
retired the silent quick piece. For the Sun 18 Instagram repost she chose to
add sound ("voiceover"), so this writes a NEW file rather than touching
`barquantities-tiktok.mp4`, which is already live on TikTok and must not move.

  * PICTURE IS COPIED, NOT RE-ENCODED. `-c:v copy` keeps the Oct 4 export
    bit-for-bit, so this is genuinely the approved cut plus a voice and not a
    second-generation re-encode of it. The guide's "use the existing cut, no
    re-edit" is honoured on the only part a re-edit would damage.
  * The VO runs 11.42s against a 12.20s cut, leaving ~0.78s of tail. It is
    padded to the full length rather than letting the stream end early.
  * Level: VO measures -19.56 LUFS, so +5.56 dB to reach the house -14. Its
    true peak is -2.60, which +5.56 would push to +2.96 dBTP, so alimiter
    catches it - with level=0, or the limiter renormalises back to full scale
    and the audio clips at 0.0 dBFS however low the limit is set.
  * The original silent AAC track is replaced outright, not mixed under.
"""
import os, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
REEL = os.path.dirname(HERE)
SRC = os.path.join(REEL, "barquantities-tiktok.mp4")
VO  = os.path.join(REEL, "voiceover", "vo-instagram.mp3")
OUT = os.path.join(REEL, "barquantities-instagram.mp4")

DUR = 12.20
VO_GAIN = 5.56          # measured: VO -19.56 LUFS, house target -14.0

cmd = [
    "ffmpeg", "-nostdin", "-v", "error", "-y",
    "-i", SRC,
    "-i", VO,
    "-filter_complex",
    f"[1:a]volume={VO_GAIN}dB,alimiter=limit=-1.0dB:level=0,aresample=48000,"
    f"apad,atrim=0:{DUR:.3f},asetpts=PTS-STARTPTS[a]",
    "-map", "0:v:0", "-map", "[a]",
    "-c:v", "copy",
    "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
    "-movflags", "+faststart", OUT,
]

if __name__ == "__main__":
    subprocess.run(cmd, check=True, capture_output=True, text=True)
    print("built", OUT)
