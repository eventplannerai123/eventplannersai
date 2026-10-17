#!/usr/bin/env python3
"""Rebuild 3 - Sep 30 post-event feedback debrief, new first beat only.

The rebuild rules: change the hook overlay, the first frame and the opening
voiceover line, keep everything after untouched, so a change in skip rate and
watch time belongs to the hook.

  * SPLICE is 2.95s. silencedetect puts the master's first gap at
    2.778-3.136, so 2.95 sits inside it and the original's opening sentence
    is replaced whole rather than sliced mid-word. Unlike Rebuild 2, "the
    first 3 seconds" happens to land naturally here.
  * The new line runs 2.27s, which leaves ~0.68s of air before the cut rather
    than butting against it.
  * Opening frame is t=31.0 of the master: "Bottom line" and the three
    numbered changes. The brief says open on the three concrete changes, not
    the survey responses.
  * THE LEVELS ARE THE OPPOSITE PROBLEM TO REBUILD 2. That master ran
    -21.3 LUFS and the new line was brought DOWN to match. This master is at
    the house -14.11, and the raw line is -20.04, so it goes UP by 5.93 dB.
    At +5.93 its true peak would be +2.56 dBTP, so alimiter catches it -
    with level=0, or the limiter renormalises back to full scale and the
    audio clips at 0.0 dBFS however low the limit is set.
  * The body is NOT re-levelled: it is already at the house figure and
    touching it would change the rest of the edit, which the rules forbid.
"""
import os, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
REEL = os.path.dirname(HERE)
SRC  = os.path.join(REEL, "..", "2026-09-30-feedback-debrief",
                    "debrief-instagram.mp4")
VO   = os.path.join(REEL, "voiceover", "vo-new-opening.mp3")
HOOK = os.path.join(HERE, "cards", "hook.png")
FRM  = os.path.join(HERE, "frames", "open.png")
OUT  = os.path.join(REEL, "feedback-debrief-rebuild-instagram.mp4")

W, H, FPS = 1080, 1920, 30
SPLICE = 2.95          # inside the master's 2.778-3.136 silence
VO_GAIN = 5.93         # measured: VO -20.04 LUFS, body -14.11 LUFS

cmd = [
    "ffmpeg", "-nostdin", "-v", "error", "-y",
    "-framerate", str(FPS), "-loop", "1", "-t", f"{SPLICE:.3f}", "-i", FRM,
    "-framerate", str(FPS), "-loop", "1", "-t", f"{SPLICE:.3f}", "-i", HOOK,
    "-i", VO,
    "-ss", f"{SPLICE:.3f}", "-i", SRC,
    "-filter_complex",
    # opening beat: frozen frame + hook card. repeatlast=1 or a single PNG
    # shows on frame one and then vanishes.
    f"[0:v]setsar=1,format=yuv420p[s0];"
    f"[s0][1:v]overlay=0:0:eof_action=repeat:repeatlast=1,format=yuv420p[va];"
    f"[2:a]volume={VO_GAIN}dB,alimiter=limit=-1.0dB:level=0,aresample=48000,"
    f"apad,atrim=0:{SPLICE:.3f},asetpts=PTS-STARTPTS[aa];"
    # the rest of the master, picture and sound untouched
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
