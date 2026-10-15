#!/usr/bin/env python3
"""Rebuild 2 — Sep 3 vendor deposit tracker, new first beat only.

The rebuild rules say change the hook overlay, the first frame and the opening
voiceover line, and keep the rest of the edit as it was, so any change in skip
rate and watch time belongs to the hook.

  * SPLICE is 4.10s, not 3.0s. The original's opening line - "Five vendors,
    five deposit dates, five balance due dates. Here's how I stop losing
    track." - runs to 4.014s; silencedetect puts clause gaps at 0.96 and 2.31,
    the line ending at 4.014 and the next sentence starting at 4.478. Cutting
    at 3.0 would slice that line mid-sentence. 4.10 sits inside the gap.
  * The opening beat is exactly SPLICE long, so the finished file is the same
    16.07s as the original and everything after the splice is untouched.
  * Opening frame is t=9.80 of the original: the tracker with the Due Date and
    Status columns both in frame and two rows reading OVERDUE. The brief says
    "the finished tracker sorted by nearest due date", and the due dates are
    the part the hook is about - at t=12.50 that column is cut off.
  * The body is NOT re-levelled. The master runs -21.3 LUFS and stays there;
    the new line is brought to match it (-20.4 -> -21.3) so the splice is
    inaudible. Normalising the whole file to the house -14 would change the
    rest of the edit, which is the one thing these rules forbid.
"""
import os, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
REEL = os.path.dirname(HERE)
SRC  = os.path.join(REEL, "source", "tracker_INSTAGRAM.mp4")
VO   = os.path.join(REEL, "voiceover", "vo-new-opening.mp3")
HOOK = os.path.join(HERE, "cards1015", "hook.png")
FRM  = os.path.join(HERE, "frames", "open.png")
OUT  = os.path.join(REEL, "deposit-tracker-rebuild-instagram.mp4")

W, H, FPS = 1080, 1920, 30
SPLICE = 4.10          # inside the original's 4.014-4.478 silence
VO_GAIN = -0.94        # measured: VO -20.38 LUFS, body -21.32 LUFS

cmd = [
    "ffmpeg", "-nostdin", "-v", "error", "-y",
    "-framerate", str(FPS), "-loop", "1", "-t", f"{SPLICE:.3f}", "-i", FRM,
    "-framerate", str(FPS), "-loop", "1", "-t", f"{SPLICE:.3f}", "-i", HOOK,
    "-i", VO,
    "-ss", f"{SPLICE:.3f}", "-i", SRC,
    "-filter_complex",
    # opening beat: frozen frame + hook card (repeatlast or a single PNG vanishes)
    f"[0:v]setsar=1,format=yuv420p[s0];"
    f"[s0][1:v]overlay=0:0:eof_action=repeat:repeatlast=1,format=yuv420p[va];"
    f"[2:a]volume={VO_GAIN}dB,aresample=48000,"
    f"apad,atrim=0:{SPLICE:.3f},asetpts=PTS-STARTPTS[aa];"
    # the rest of the original, picture and sound untouched
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
