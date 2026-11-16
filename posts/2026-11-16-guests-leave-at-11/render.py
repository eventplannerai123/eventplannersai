"""Assemble the Mon 16 Nov planner-feelings Reel for Instagram and Facebook.

The Nov 8 format rule turns this 12:30pm slot into a Reel: the same still held
7-10 seconds under music on Instagram and Facebook, and a photo post on
TikTok. Eight seconds is the middle of that range.

**THE SUN 15 RECAP PUT A NUMBER ON WHY IT IS A REEL AND NOT A PHOTO.** On
Mon 9 the photo version of this slot reached 15; the two posted as Reels
reached 146 and 130. So after posting, check the profile shows it as a Reel.

THE BED IS ITS OWN, AND UPBEAT per her Nov 10 instruction: bright electric
piano over a warm synth bass with a light tambourine pulse, major key. Not
Friday's guitar-and-marimba and not Saturday's piano-and-claps — never reuse
a bed, and never share one between two posts on a day.

Instrumental, checked the same two ways as every bed before it: a spectrogram
read for the formant movement a sung vowel makes, and Scribe, which
transcribes an instrumental to an empty string. The generation's own settings
are not the check.

Nothing moves in the frame. A push on typeset text softens the glyphs for no
gain, and there is one image.
"""
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(HERE, "slides", "guests-leave-at-11.jpg")
BED = os.path.join(HERE, "build", "music", "bed-8s.wav")

W, H, FPS = 1080, 1920, 30
HOLD = 8.0


def render():
    assert os.path.exists(IMG), IMG
    out = os.path.join(HERE, "guests-leave-at-11-instagram.mp4")
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
