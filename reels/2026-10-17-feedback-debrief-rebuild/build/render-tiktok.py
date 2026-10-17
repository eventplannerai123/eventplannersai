#!/usr/bin/env python3
"""Rebuild 3, TikTok cut - the Sep 30 TikTok master, new first beat only.

The rebuild rules say Instagram and Facebook only, so this one is extra: she
asked for it on Oct 17 after the Instagram post went out, because the original
went to TikTok on Sep 30 and a straight repost would show that audience the
same opening twice. The rebuilt cut has a new hook, a new opening frame and a
new file, so TikTok reads it as a new video rather than a duplicate.

It changes nothing about the experiment. The rebuild is judged on the
Instagram numbers; TikTok is a separate audience and a separate platform.

Same shape as render.py, different numbers because the TikTok master is cut
to its own pacing:

  * SPLICE is 3.10s. silencedetect puts this master's first gap at
    2.880-3.521 (the Instagram master's is 2.778-3.136), so 3.10 sits inside
    it and the original's opening sentence is replaced whole.
  * Opening frame is t=28.8 of the TikTok master - the same content as the
    Instagram cut's t=31.0, which lands earlier here because this cut is
    28.90s against 31.17s.
  * The hook card is a different file: the three changes sit at 961 here
    against 1017 there, so the card is centred 55px higher. make_cards.py
    measures both rather than reusing one number.
  * Body is -14.10 LUFS, so the -20.04 line goes up 5.94 dB, and alimiter
    with level=0 catches the +3 dBTP that would otherwise result.
"""
import os, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
REEL = os.path.dirname(HERE)
SRC  = os.path.join(REEL, "..", "2026-09-30-feedback-debrief",
                    "debrief-tiktok.mp4")
VO   = os.path.join(REEL, "voiceover", "vo-new-opening.mp3")
HOOK = os.path.join(HERE, "cards", "hook-tiktok.png")
FRM  = os.path.join(HERE, "frames", "open-tiktok.png")
OUT  = os.path.join(REEL, "feedback-debrief-rebuild-tiktok.mp4")

W, H, FPS = 1080, 1920, 30
SPLICE = 3.10          # inside this master's 2.880-3.521 silence
VO_GAIN = 5.94         # measured: VO -20.04 LUFS, body -14.10 LUFS

cmd = [
    "ffmpeg", "-nostdin", "-v", "error", "-y",
    "-framerate", str(FPS), "-loop", "1", "-t", f"{SPLICE:.3f}", "-i", FRM,
    "-framerate", str(FPS), "-loop", "1", "-t", f"{SPLICE:.3f}", "-i", HOOK,
    "-i", VO,
    "-ss", f"{SPLICE:.3f}", "-i", SRC,
    "-filter_complex",
    f"[0:v]setsar=1,format=yuv420p[s0];"
    f"[s0][1:v]overlay=0:0:eof_action=repeat:repeatlast=1,format=yuv420p[va];"
    f"[2:a]volume={VO_GAIN}dB,alimiter=limit=-1.0dB:level=0,aresample=48000,"
    f"apad,atrim=0:{SPLICE:.3f},asetpts=PTS-STARTPTS[aa];"
    f"[3:v]scale={W}:{H},setsar=1,format=yuv420p[vb];"
    f"[3:a]aresample=48000[ab];"
    f"[va][aa][vb][ab]concat=n=2:v=1:a=1[v][a]",
    "-map", "[v]", "-map", "[a]",
    "-c:v", "libx264", "-profile:v", "high", "-crf", "19", "-pix_fmt", "yuv420p",
    "-movflags", "+faststart", "-r", str(FPS),
    "-c:a", "aac", "-b:a", "192k", "-ar", "48000", OUT,
]

if __name__ == "__main__":
    subprocess.run(cmd, check=True, capture_output=True, text=True)
    print("built", OUT)
