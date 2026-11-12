"""Assemble the Sun 15 Nov slide Reel for Instagram and Facebook.

The Nov 8 format rule: Instagram and Facebook get a slide Reel, each slide
about 2.5 seconds, music; TikTok gets the same five JPEGs as a photo
carousel, which needs no assembly.

HARD CUTS AND NO PUSH. These are typeset brand slides, not screenshots of a
scrolling answer: a push on 72px margins softens the glyph edges for nothing,
and a crossfade between two lavender cards reads as a smear.

FIVE SLIDES, SO 12.5s. Slide 4 carries three changes and the survey line
behind each, which is more reading than the others — but splitting it into
three slides would break the guide's five-slide brief, and at 2.5s a slide
nobody reads a carousel at playback speed anyway. The still is what gets read
on TikTok.

THE BED IS UPBEAT AND ITS OWN, per her Nov 10 instruction, and deliberately
not Friday's guitar-and-marimba or Saturday's piano-and-claps: vibraphone and
muted bass over brushed drums. Three Reels in three days on one track would
read as stock music.

Instrumental, checked the same two ways as every bed before it: a spectrogram
read for the formant movement a sung vowel makes, and Scribe, which
transcribes an instrumental to an empty string. The generation's own settings
are not the check. Trimmed with a 0.8s fade in and a 1.2s fade out and
measured to -14 LUFS like every other export.
"""
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
SLIDES = os.path.join(HERE, "slides")
BED = os.path.join(HERE, "build", "music", "bed-13s.wav")

W, H, FPS = 1080, 1920, 30
PER_SLIDE = 2.50
N = 5
TOTAL = PER_SLIDE * N          # 12.5s


def render():
    ins, filt = [], []
    for i in range(1, N + 1):
        p = os.path.join(SLIDES, f"2026-11-15-last-year-{i}.jpg")
        assert os.path.exists(p), p
        ins += ["-loop", "1", "-t", f"{PER_SLIDE:.3f}", "-i", p]
        filt.append(f"[{i-1}:v]scale={W}:{H},fps={FPS},setsar=1[v{i-1}]")
    chain = "".join(f"[v{i}]" for i in range(N))
    filt.append(f"{chain}concat=n={N}:v=1:a=0[body]")

    ins += ["-i", BED]
    out = os.path.join(HERE, "last-year-instagram.mp4")
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
