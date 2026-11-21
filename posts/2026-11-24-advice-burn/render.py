"""Assemble the two Tue 24 Nov hook-test Reels.

Her Nov 19 weekly hook test: two versions of one new Reel, identical except
the title, uploaded by her as Trial Reels on the Tuesday morning. This
session cannot post trials, so both files go to her.

**BOTH CUTS SHARE ONE BED, AND THAT IS DELIBERATE.** Her Nov 10 rule is that
no two posts on the same day share a track — written after two of Wednesday's
Reels went out on one and she heard it at once. This is the exception the
rule is not about: A and B are the same piece twice, and the test measures
the title. A second bed would be a second variable and would make the result
unreadable. Tuesday's 6:30pm Thanksgiving Reel carries an Eryn voiceover and
no bed, so nothing else that day sounds like this.

Muted electric guitar stabs and a tight tambourine over a punchy electric
bass — its own generation, nothing shared with Monday's list Reel.

Instrumental, checked both ways: the spectrogram shows even dense texture end
to end with regular transients and nothing sweeping, and Scribe returned an
empty string. The generation's own settings say "Instrumental: False" either
way, so they are not the check.

Energy runs -14.2 to -15.1 dB across all 25 seconds with no ring-out, so the
cut starts at 0.0. 0.8s fade in, 1.2s fade out, **+0.3 dB** into the limiter
for -14.0 LUFS.

Nine seconds each, the middle of the format's 8-10s. Nothing moves in the
frame: a push on typeset text softens the glyphs for no gain.
"""
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
SLIDES = os.path.join(HERE, "slides")
BED = os.path.join(HERE, "build", "music", "bed-9s.wav")

W, H, FPS = 1080, 1920, 30
HOLD = 9.0


def render(key):
    img = os.path.join(SLIDES, f"advice-burn-{key}.jpg")
    assert os.path.exists(img), img
    assert 8.0 <= HOLD <= 10.0, f"{HOLD}s is outside the format's 8-10s"
    out = os.path.join(HERE, f"advice-burn-{key}.mp4")
    subprocess.run(["ffmpeg", "-v", "error", "-y",
                    "-loop", "1", "-t", f"{HOLD:.3f}", "-i", img, "-i", BED,
                    "-filter_complex", f"[0:v]scale={W}:{H},fps={FPS},setsar=1[v]",
                    "-map", "[v]", "-map", "1:a",
                    "-c:v", "libx264", "-profile:v", "high", "-crf", "19",
                    "-pix_fmt", "yuv420p", "-movflags", "+faststart",
                    "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
                    "-shortest", out], check=True)
    print(f"{key}: {HOLD:.2f}s -> {os.path.basename(out)}")
    return out


if __name__ == "__main__":
    for key in ("a", "b"):
        render(key)
