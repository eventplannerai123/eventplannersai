"""Assemble the Sat 21 Nov planner-life Reel for Instagram and Facebook.

The Sat 21 CLAUDE CODE line asks for the image plus "the Reel version for
Instagram and Facebook (image held 7-10 seconds, soft music)". Eight seconds
is the middle of that range, the same hold as every planner-feelings still.

**A REEL, NOT A PHOTO.** On Mon 9 the photo version of a still reached 15
against 146 and 130 for the two posted as Reels, so the block says to check
the profile after posting and confirm it shows as a Reel.

THE BED IS ITS OWN GENERATION: nylon-string guitar fingerpicking over electric
piano, upbeat per her Nov 10 instruction, and nothing to do with Friday's
marimba. Beds are never shared between pieces.

Instrumental, checked the same two ways as every bed before it: a spectrogram
read for the formant movement a sung vowel makes, and Scribe, which returned
an empty string. The generation's own settings said "Instrumental: False" and
are not the check.

The spectrogram also settles the trim: full texture from 0.0s, so the cut
starts there. 0.8s fade in, 1.2s fade out, +3.7 dB into the limiter for -14.0
LUFS — Friday's needed +4.05, so the figure is swept every time.

Nothing moves in the frame. A push on typeset text softens the glyphs for no
gain, and there is one image.
"""
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(HERE, "slides", "questions.jpg")
BED = os.path.join(HERE, "build", "music", "bed-8s.wav")

W, H, FPS = 1080, 1920, 30
HOLD = 8.0


def render():
    assert os.path.exists(IMG), IMG
    out = os.path.join(HERE, "questions-instagram.mp4")
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
