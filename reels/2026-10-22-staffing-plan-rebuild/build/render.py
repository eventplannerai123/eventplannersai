#!/usr/bin/env python3
"""Rebuild 4 — the Sep 26 conference agenda -> staffing plan Reel.

The rebuild rules: change the hook overlay, the first frame and the opening
voiceover line, keep everything after untouched, so any movement in skip rate
and watch time belongs to the hook.

  * THE OLD HOOK WAS "Six sessions. Three rooms. Four staff." — three numbers
    and no stake. The approved replacement (Sahiba, Oct 16: "a is good") is
    "Four staff, six sessions, one block you're short.", which leads with what
    the output actually delivers: the prompt ends "flag any block where we're
    short" and the answer's verdict is "staffable with four people, but—".
  * SPLICE IS 3.70s, not the first gap. silencedetect puts the master's gaps at
    1.998-2.328, 3.501-3.913 and 5.554-6.587. The new line runs 3.46s, so the
    first gap cannot hold it; 3.70 sits inside the second and leaves 0.236s of
    air before the cut. The master's first TWO sentences are therefore replaced
    rather than one — the same compromise Rebuild 2 made at 4.10.
  * THE OPENING FRAME IS THE MASTER'S OWN t=0.000, which is the prompt sitting
    in the box with the agenda PDF attached and the send button live. Video
    rule 2: never cut the prompt. It is also the one frame in the first two
    seconds with NO hook card on it — the old card fades in over 0.20s from
    t=0, so frame zero is clean and every later frame in that range carries it.
  * THE NEW CARD SITS AT y=1300, over the keyboard, not at the old y=620. At
    620 it would cover the prompt text, which is the one thing this opening
    exists to show. That is the Sep 29 mistake, recorded in CLAUDE.md.
  * THE LINE IS SPED 8%. Vanessa reads it in 3.74s flat, which needs a 3.85
    splice and a longer freeze; at atempo=1.08 it is 3.46s and lands snappier,
    which suits a hook. Pitch is preserved.
  * LEVELS: the raw line measures -22.33 LUFS against the master's -14.06, so
    it goes up 8.27 dB. At that gain its true peak would be +3.21 dBTP, so
    alimiter catches it — with level=0, or the limiter renormalises back to
    full scale and the audio clips at 0.0 dBFS however low the limit is set.
  * BOTH BRANCHES ARE FORCED TO STEREO, and that is not cosmetic. This master
    is stereo where the Sep 30 one was mono, so concat matched the layouts by
    DOWNMIXING the body to mono — which sums L+R and brought the untouched
    body up from -1.36 dB peak to +1.40, i.e. clipping, from a filtergraph
    that never names a gain. Measure the body of the export against the body
    of the master, not just the export as a whole: the overall LUFS barely
    moved and hid it.
  * THE BODY IS NOT RE-LEVELLED. It is already at the house figure and
    touching it would change the rest of the edit, which the rules forbid.
  * DURATION MUST COME OUT AT 26.90s, identical to the master. That is the
    check that nothing after the splice moved.
"""
import os, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
REEL = os.path.dirname(HERE)
SRC  = os.path.join(REEL, "..", "2026-09-26-staffing-plan", "staffing-instagram.mp4")
VO   = os.path.join(REEL, "voiceover", "vo-new-opening.mp3")
HOOK = os.path.join(HERE, "cards", "hook.png")
FRM  = os.path.join(HERE, "frames", "open.png")
OUT  = os.path.join(REEL, "staffing-plan-rebuild-instagram.mp4")

W, H, FPS = 1080, 1920, 30
SPLICE = 3.70          # inside the master's 3.501-3.913 silence
VO_GAIN = 8.27         # measured: VO -22.33 LUFS, body -14.06 LUFS

cmd = [
    "ffmpeg", "-nostdin", "-v", "error", "-y",
    "-framerate", str(FPS), "-loop", "1", "-t", f"{SPLICE:.3f}", "-i", FRM,
    "-framerate", str(FPS), "-loop", "1", "-t", f"{SPLICE:.3f}", "-i", HOOK,
    "-i", VO,
    "-ss", f"{SPLICE:.3f}", "-i", SRC,
    "-filter_complex",
    # opening beat: the clean frame-zero still + the new hook card. A single
    # PNG needs repeatlast=1 or it shows on frame one and then vanishes.
    f"[0:v]setsar=1,format=yuv420p[s0];"
    f"[s0][1:v]overlay=0:0:eof_action=repeat:repeatlast=1,format=yuv420p[va];"
    f"[2:a]volume={VO_GAIN}dB,alimiter=limit=-1.0dB:level=0,aresample=48000,"
    f"aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=stereo,"
    f"apad,atrim=0:{SPLICE:.3f},asetpts=PTS-STARTPTS[aa];"
    # the rest of the master, picture and sound untouched
    f"[3:v]scale={W}:{H},setsar=1,format=yuv420p[vb];"
    f"[3:a]aresample=48000,aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=stereo[ab];"
    f"[va][aa][vb][ab]concat=n=2:v=1:a=1[v][a]",
    "-map", "[v]", "-map", "[a]",
    "-c:v", "libx264", "-profile:v", "high", "-crf", "19", "-pix_fmt", "yuv420p",
    "-movflags", "+faststart", "-r", str(FPS),
    "-c:a", "aac", "-b:a", "192k", "-ar", "48000", OUT,
]

if __name__ == "__main__":
    subprocess.run(cmd, check=True, capture_output=True, text=True)
    print("built", OUT)
