"""Assemble the Wed 11 Nov planner-feelings Reel for Instagram and Facebook.

The Nov 8 format rule turns this 12:30pm slot into a Reel: the same still held
7-10 seconds under soft music on Instagram and Facebook, and a photo post on
TikTok. Eight seconds is the middle of that range and about as long as the
three paragraphs take to read.

THE MUSIC IS THE SAME GENERATED BED AS THE DAY'S SLIDE REEL, trimmed to 8s. A
Reel posted from this session cannot use Instagram's licensed audio library,
so whatever is in the mp4 is what goes out. It is instrumental, and that was
checked rather than assumed: a spectrogram showed piano transients and steady
harmonics with none of the formant movement a sung vowel makes, and Scribe
transcribed it to an empty string. Faded 0.8s in and 1.2s out, measured to
-14 LUFS.

Nothing moves in the frame. A push on typeset text softens the glyphs for no
gain, and there is one image.
"""
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(HERE, "slides", "allowed-to-be-tired.jpg")
BED = os.path.join(HERE, "build", "music", "bed-8s.wav")

W, H, FPS = 1080, 1920, 30
HOLD = 8.0


def render():
    assert os.path.exists(IMG), IMG
    out = os.path.join(HERE, "allowed-to-be-tired-instagram.mp4")
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
