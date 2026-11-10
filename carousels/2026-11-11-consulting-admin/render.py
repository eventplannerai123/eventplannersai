"""Assemble the Wed 11 Nov consulting slide Reel for Instagram and Facebook.

The Nov 8 format rule: Instagram and Facebook get a slide Reel, each slide
about 2.5 seconds, soft music; TikTok gets the same six JPEGs as a photo
carousel, which needs no assembly.

HARD CUTS AND NO PUSH. Every other piece in this repo gives its freeze frames
a 4% slow push, because they are screenshots of a scrolling answer and the
drift reads as life. These are typeset brand slides: a push on 72px margins
softens the glyph edges for nothing, and a crossfade between two lavender
cards reads as a smear. Six cuts at 2.5s is the format the guide asked for.

THE MUSIC IS GENERATED HERE AND IT IS INSTRUMENTAL, CHECKED. A Reel posted
from this session cannot use Instagram's licensed audio library — that is
in-app only — so whatever is in the mp4 is what goes out, and the guide asks
for a soft royalty-free bed. `eleven_music_v2_5` made it from a prompt asking
for felt piano and a sustained pad, no drums and no vocals. Two checks on the
result, because nobody here can listen to it: a spectrogram showed steady
harmonics and piano transients with none of the formant movement a sung vowel
makes, and ElevenLabs Scribe transcribed it to an **empty string**, which is
what an instrumental returns. The bed is trimmed to 15s with a 0.8s fade in
and a 1.2s fade out, and measured to -14 LUFS like every other export.
"""
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
SLIDES = os.path.join(HERE, "slides")
BED = os.path.join(HERE, "build", "music", "bed-15s.wav")

W, H, FPS = 1080, 1920, 30
PER_SLIDE = 2.50
N = 6
TOTAL = PER_SLIDE * N          # 15.0s


def render():
    ins, filt = [], []
    for i in range(1, N + 1):
        p = os.path.join(SLIDES, f"2026-11-11-consulting-admin-{i}.jpg")
        assert os.path.exists(p), p
        ins += ["-loop", "1", "-t", f"{PER_SLIDE:.3f}", "-i", p]
        filt.append(f"[{i-1}:v]scale={W}:{H},fps={FPS},setsar=1[v{i-1}]")
    chain = "".join(f"[v{i}]" for i in range(N))
    filt.append(f"{chain}concat=n={N}:v=1:a=0[body]")

    ins += ["-i", BED]
    out = os.path.join(HERE, "consulting-admin-instagram.mp4")
    subprocess.run(["ffmpeg", "-v", "error", "-y"] + ins +
                   ["-filter_complex", ";".join(filt),
                    "-map", "[body]", "-map", f"{N}:a",
                    "-c:v", "libx264", "-profile:v", "high", "-crf", "19",
                    "-pix_fmt", "yuv420p", "-movflags", "+faststart",
                    "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
                    "-shortest", out], check=True)
    print(f"{TOTAL:.2f}s, {N} slides at {PER_SLIDE}s -> {os.path.basename(out)}")
    return out


if __name__ == "__main__":
    render()
