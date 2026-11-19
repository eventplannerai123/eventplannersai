"""Assemble the Sun 22 Nov slide Reel for Instagram and Facebook.

The Nov 8 format rule: Instagram and Facebook get a slide Reel; TikTok gets
the same six JPEGs as a photo carousel, which needs no assembly.

HARD CUTS AND NO PUSH. These are typeset brand slides, not screenshots of a
scrolling answer: a push on 72px margins softens the glyph edges for nothing,
and a crossfade between two lavender cards reads as a smear. Slide 1 carries
her photo and does not move either — a slow zoom on a still photograph is the
oldest tell there is.

SIX SLIDES AT 3.00s, SO 18.0s. The Sun 22 line says "about 2.5 seconds a
slide"; 3.00 is what she asked for on Nov 17 ("slow down the reel a little")
and what she approved on the Wed 18 set, so it holds here. Slide 5 is the
reason it matters: seven sheet rows, a busiest-hour line, a walk schedule and
the flag is more to read in one beat than anything else in the set.

THE BED IS ITS OWN GENERATION: vibraphone over upright piano and plucked
double bass, upbeat per her Nov 10 instruction, and nothing shared with any
other piece this week.

Instrumental, checked the same two ways as every bed before it: a spectrogram
read for the formant movement a sung vowel makes, and Scribe, which returned
an empty string. The generation's own settings are not the check — they report
"Instrumental: False" either way.

The spectrogram also settles the trim: full texture from 0.0s, so the cut
starts there. 0.8s fade in, 1.2s fade out, and **-0.55 dB** into the limiter
for -14.0 LUFS — this one came out of the model hot. Friday's needed +4.05 and
Saturday's +3.7, so the figure is swept every time rather than carried over.
"""
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
SLIDES = os.path.join(HERE, "slides")
BED = os.path.join(HERE, "build", "music", "bed-18s.wav")

W, H, FPS = 1080, 1920, 30
PER_SLIDE = 3.00
N = 6
TOTAL = PER_SLIDE * N          # 18.0s


def render():
    ins, filt = [], []
    for i in range(1, N + 1):
        p = os.path.join(SLIDES, f"2026-11-22-one-plate-left-{i}.jpg")
        assert os.path.exists(p), p
        ins += ["-loop", "1", "-t", f"{PER_SLIDE:.3f}", "-i", p]
        filt.append(f"[{i-1}:v]scale={W}:{H},fps={FPS},setsar=1[v{i-1}]")
    chain = "".join(f"[v{i}]" for i in range(N))
    filt.append(f"{chain}concat=n={N}:v=1:a=0[body]")

    ins += ["-i", BED]
    out = os.path.join(HERE, "one-plate-left-instagram.mp4")
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
