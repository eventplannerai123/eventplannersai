"""Assemble the Wed 18 Nov planner-feelings Reel for Instagram and Facebook.

The Nov 8 format rule turns this 12:30pm slot into a Reel: the same still held
7-10 seconds under music on Instagram and Facebook, and a photo post on
TikTok. Eight seconds is the middle of that range.

**THE SUN 15 RECAP PUT A NUMBER ON WHY IT IS A REEL AND NOT A PHOTO.** On
Mon 9 the photo version of this slot reached 15; the two posted as Reels
reached 146 and 130. So after posting, check the profile shows it as a Reel.

THE BED IS ITS OWN, AND UPBEAT per her Nov 10 instruction: warm Rhodes piano
with a glockenspiel counter-melody over a muted synth bass. **Wednesday
carries two posts and they do not share a track** — the 6:30pm slide Reel runs
on nylon-string guitar and woodblock, a separate generation. On Nov 11 both of
that day’s Reels went out on one bed, the short cut being the opening bars of
the long one, and she heard it immediately.

Instrumental, checked the same two ways as every bed before it: a spectrogram
read for the formant movement a sung vowel makes, and Scribe, which returned
an empty string. The generation’s own settings are not the check.

The spectrogram also settles the trim: full texture from 0.0s, so the cut
starts there. 0.8s fade in, 1.2s fade out, +1.3 dB into the limiter for -14.0
LUFS — Monday’s needed -0.7 and Saturday’s +0.2, so the figure is swept every
time rather than carried over.

Nothing moves in the frame. A push on typeset text softens the glyphs for no
gain, and there is one image.
"""
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(HERE, "slides", "nobody-claps.jpg")
BED = os.path.join(HERE, "build", "music", "bed-8s.wav")

W, H, FPS = 1080, 1920, 30
HOLD = 8.0


def render():
    assert os.path.exists(IMG), IMG
    out = os.path.join(HERE, "nobody-claps-instagram.mp4")
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
