"""Assemble the Wed 25 Nov planner list Reel for Instagram and Facebook.

The November plan's planner-list-Reel format: one image held 8-10 seconds as
a Reel with music, and the same image as a photo post on TikTok. Nine seconds
is the middle of that range and gives four boxes time to be read.

**ITS BED IS NOT THE SLIDE REEL'S.** Both pieces go out on Wed 25, and her
Nov 10 rule after she caught two Wednesday posts sharing their opening bars
is that a bed is never reused across two posts on the same day. These are
two separate generations with different prompts: that one is electric piano
and shaker under a voiceover, this one is a bouncy guitar riff with
handclaps, chosen to match a list of bad habits admitted with a shrug.

Instrumental, checked the same two ways as every bed: a spectrogram read for
the formant movement a sung vowel makes — regular transients, nothing
sweeping — and Scribe, which returned an empty string. The generation's own
settings report "Instrumental: False" either way, so they are not the check.

The energy profile settles the trim: -13.5 to -14.7 dB across all 30 seconds,
flat end to end with no intro build and no ring-out, so the cut starts at 0.0.
0.8s fade in, 1.2s fade out.

Nothing moves in the frame. A push on typeset text softens the glyphs for no
gain, and there is one image.
"""
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(HERE, "slides", "normalized.jpg")
BED = os.path.join(HERE, "build", "music", "bed-9s.wav")

W, H, FPS = 1080, 1920, 30
HOLD = 9.0
BED_DB = -0.6                  # swept: +0.0 measured -13.4, this lands -14.0


def render():
    assert os.path.exists(IMG), IMG
    assert 8.0 <= HOLD <= 10.0, f"{HOLD}s is outside the format's 8-10s"
    out = os.path.join(HERE, "normalized-instagram.mp4")
    subprocess.run(["ffmpeg", "-v", "error", "-y",
                    "-loop", "1", "-t", f"{HOLD:.3f}", "-i", IMG, "-i", BED,
                    "-filter_complex",
                    f"[0:v]scale={W}:{H},fps={FPS},setsar=1[v];"
                    f"[1:a]volume={BED_DB}dB,alimiter=limit=0.891:level=0[a]",
                    "-map", "[v]", "-map", "[a]",
                    "-c:v", "libx264", "-profile:v", "high", "-crf", "19",
                    "-pix_fmt", "yuv420p", "-movflags", "+faststart",
                    "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
                    "-shortest", out], check=True)
    print(f"{HOLD:.2f}s hold, bed {BED_DB:+.1f} dB -> {os.path.basename(out)}")
    return out


if __name__ == "__main__":
    render()
