"""Assemble the Fri 20 Nov planner-feelings Reel for Instagram and Facebook.

The Nov 8 format rule turns this 12:30pm slot into a Reel: the same still held
7-10 seconds under music on Instagram and Facebook, and a photo post on
TikTok. Eight seconds is the middle of that range.

**IT IS A REEL AND NOT A PHOTO, AND THE NUMBERS SAY WHY.** On Mon 9 the photo
version of this slot reached 15; the two posted as Reels reached 146 and 130.
So after posting, check the profile shows it as a Reel.

THE BED IS ITS OWN, AND UPBEAT per her Nov 10 instruction: marimba over warm
strings and a plucked upright bass. **Friday carries two posts and they do not
share a track** — the 6:30pm giveaway Reel gets its own generation. On Nov 11
both of that day's Reels went out on one bed, the short cut being the opening
bars of the long one, and she heard it immediately.

Instrumental, checked the same two ways as every bed before it: a spectrogram
read for the formant movement a sung vowel makes, and Scribe, which returned
an empty string. The generation's own settings are not the check — this one
reported "Instrumental: False" and is plainly not.

The spectrogram also settles the trim: full texture from 0.0s and a thinning
tail after about 18s, so the cut starts at 0.0. 0.8s fade in, 1.2s fade out,
+4.05 dB into the limiter for -14.0 LUFS. Wednesday's needed +1.3 and
Monday's -0.7, so the figure is swept every time rather than carried over.

Nothing moves in the frame. A push on typeset text softens the glyphs for no
gain, and there is one image.
"""
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(HERE, "slides", "calmest-person.jpg")
BED = os.path.join(HERE, "build", "music", "bed-8s.wav")

W, H, FPS = 1080, 1920, 30
HOLD = 8.0


def render():
    assert os.path.exists(IMG), IMG
    out = os.path.join(HERE, "calmest-person-instagram.mp4")
    subprocess.run(["ffmpeg", "-v", "error", "-y",
                    "-loop", "1", "-t", f"{HOLD:.3f}", "-i", IMG, "-i", BED,
                    "-filter_complex", f"[0:v]scale={W}:{H},fps={FPS},setsar=1[v]",
                    "-map", "[v]", "-map", "1:a",
                    "-c:v", "libx264", "-profile:v", "high", "-crf", "19",
                    "-pix_fmt", "yuv420p", "-movflags", "+faststart",
                    "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
                    "-shortest", out], check=True)
    print(f"{HOLD:.2f}s hold -> {os.path.basename(out)}")
    return out


if __name__ == "__main__":
    render()
