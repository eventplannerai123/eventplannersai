"""Assemble the Fri 20 Nov coloring timelapse — TikTok about 3pm, and her Story.

HER FOOTAGE, FILMED THU 19: IMG_0430.MOV, 101.8s, native portrait 1080x1920,
phone propped on the table at a shallow angle rather than overhead — she said
on Nov 18 she had no way to film from up top, and the angle reads better
anyway because the hand moving is what makes a timelapse work.

**NOT IN THIS REPO.** The repo is public, so her raw clips never land here;
this reads the scratch copy pulled out of Drive `November 20`
(`13KeZV3qJI5EPl1QdT5ZMXQuNOgyAATmW`). Only the finished cut is committed.

Trimmed 2.50 - 99.70: she leans in to start the recording for the first two
and a half seconds, and reaches to stop it at 100.1. 97.2 seconds of colouring
at 6.075x gives exactly 16.00s, inside the 15-20 second target.

**NO VOICEOVER — her instruction, Nov 19: "remove the voice from the coloring
picture."** The Fri 20 block wrote a 30-word Eryn script and it is not used.
So the audio is the bed alone, which also means the piece cannot go out silent
(her Nov 10 rule): celesta and pizzicato strings over ukulele, upbeat per her
Nov 10 note, its own generation and nothing to do with the giveaway Reel's
voice-only track or Friday's marimba planner-feelings bed.

Instrumental proved the usual two ways: the spectrogram shows no formant
movement, and Scribe returned an empty string. +2.15 dB into the limiter for
-14.0 LUFS, swept rather than computed.
"""
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
CARDS = os.path.join(HERE, "build", "cards")
BED = os.path.join(HERE, "build", "music", "bed-16s.wav")
SRC = os.environ.get("TIMELAPSE_SRC", "/tmp/claude-0/-home-user-eventplannersai/"
                     "4079a8b4-9eb7-5c73-8b20-b79d77bad268/scratchpad/src20/"
                     "IMG_0430.MOV")

W, H, FPS = 1080, 1920, 30
START, LENGTH, SPEED = 2.50, 97.20, 6.075
HOOK_UNTIL = 2.0


def main():
    total = round(LENGTH / SPEED, 3)
    assert 15.0 <= total <= 20.0, f"{total}s is outside the 15-20s target"
    out = os.path.join(HERE, "coloring-timelapse.mp4")
    fc = (
        f"[0:v]trim=start={START}:duration={LENGTH},setpts=PTS-STARTPTS,"
        f"setpts=PTS/{SPEED},scale={W}:{H},fps={FPS},setsar=1[v];"
        f"[1:v]scale={W}:{H},setsar=1[hook];"
        f"[v][hook]overlay=0:0:eof_action=repeat:repeatlast=1:"
        f"enable='between(t,0,{HOOK_UNTIL})'[vout]"
    )
    subprocess.run([
        "ffmpeg", "-v", "error", "-y",
        "-i", SRC,
        "-loop", "1", "-t", f"{HOOK_UNTIL + 0.1}", "-i", os.path.join(CARDS, "hook.png"),
        "-i", BED,
        "-filter_complex", fc, "-map", "[vout]", "-map", "2:a",
        "-c:v", "libx264", "-profile:v", "high", "-crf", "19",
        "-pix_fmt", "yuv420p", "-movflags", "+faststart",
        "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
        "-t", f"{total}", out], check=True)
    print(f"{LENGTH:.1f}s at {SPEED}x = {total:.2f}s -> {os.path.basename(out)}")


if __name__ == "__main__":
    main()
