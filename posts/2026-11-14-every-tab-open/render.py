"""Assemble the Sat 14 Nov planner-life Reel for Instagram and Facebook.

The Nov 8 format rule turns the planner-life slot into a Reel too: the same
still held 8 seconds under music on Instagram and Facebook, and a photo post
on TikTok. Eight seconds is about as long as eight tab titles take to read.

THE BED IS UPBEAT AND ITS OWN. Her Nov 10 instruction — "moving forward lets
to more upbeat instrumentals" — governs over the guide's "soft royalty-free
music", the same call as Friday's. This one is electric piano and a bouncing
synth bass with a hi-hat and handclap pulse, deliberately not Friday's guitar
and marimba: two Reels a day apart on the same track would read as one piece
of stock music, which is the thing she caught on Wed 11.

A Reel posted from this session cannot use Instagram's licensed audio library,
so whatever is in the mp4 is what goes out. Instrumental, checked the same two
ways as every bed before it: a spectrogram read for the formant movement a
sung vowel makes, and Scribe, which transcribes an instrumental to an empty
string. The generation's own settings are not the check — they can report
"Instrumental: False" even when the prompt asked for none.

Nothing moves in the frame. A push on typeset text softens the glyphs for no
gain, and there is one image.
"""
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(HERE, "slides", "every-tab-open.jpg")
BED = os.path.join(HERE, "build", "music", "bed-8s.wav")

W, H, FPS = 1080, 1920, 30
HOLD = 8.0


def render():
    assert os.path.exists(IMG), IMG
    out = os.path.join(HERE, "every-tab-open-instagram.mp4")
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
