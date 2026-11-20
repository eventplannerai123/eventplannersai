"""Assemble the Thu 26 Nov reviews slide Reel for Instagram and Facebook.

The Nov 8 format rule: Instagram and Facebook get a slide Reel; TikTok gets
the same five JPEGs as a photo carousel, which needs no assembly.

HARD CUTS AND NO PUSH, the same as Sun 22. These are typeset brand slides, not
screenshots of a scrolling answer: a push on 72px margins softens the glyph
edges for nothing, and a crossfade between two lavender cards reads as a
smear.

**THE SLIDES ARE NOT ALL THE SAME LENGTH, AND SLIDE 3 IS WHY.** Christina N.'s
review runs 37 words on top of a two-line headline, which is roughly twice
what any other slide asks anyone to read. A flat 3.00s across five slides
would make that one unreadable and leave the one-line ones sitting there.
Slide 3 gets 4.80s; nothing is under the 3.00s she set on Nov 17 ("slow down
the reel a little").

**NO VOICEOVER, DELIBERATELY.** Three of the five slides are other people's
words. Having Eryn read a stranger's Amazon review in the first person is the
one thing this piece must not do, so it is overlay-led — allowed by the Oct 5
rule 1 — and the bed is what keeps it from going out silent, which is her
Nov 10 instruction in four words: "dont go out silent".

THE BED IS ITS OWN GENERATION: marimba and nylon guitar over a light clap
pulse, upbeat per her Nov 10 instruction, and nothing shared with any other
piece. Thu 26 carries no second post, so there is nothing for it to clash
with — but it is a fresh generation regardless.

Instrumental, checked the same two ways as every bed before it: a spectrogram
read for the formant movement a sung vowel makes, and Scribe, which has to
return an empty string. The generation's own settings are not the check —
they report "Instrumental: False" either way.
"""
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
SLIDES = os.path.join(HERE, "slides")
BED = os.path.join(HERE, "build", "music", "bed.wav")
STEM = "2026-11-26-reviews"

W, H, FPS = 1080, 1920, 30
#            1     2     3     4     5
DURS = [3.20, 3.20, 4.80, 3.20, 3.60]
TOTAL = sum(DURS)          # 18.00s


def render():
    assert len(DURS) == 5
    assert min(DURS) >= 3.00, f"a slide is under 3.00s: {DURS}"
    assert 15.0 <= TOTAL <= 20.0, f"{TOTAL:.2f}s is outside 15-20s"
    ins, filt = [], []
    for i, dur in enumerate(DURS, start=1):
        p = os.path.join(SLIDES, f"{STEM}-instagram-{i}.jpg")
        assert os.path.exists(p), p
        ins += ["-loop", "1", "-t", f"{dur:.3f}", "-i", p]
        filt.append(f"[{i-1}:v]scale={W}:{H},fps={FPS},setsar=1[v{i-1}]")
    chain = "".join(f"[v{i}]" for i in range(len(DURS)))
    filt.append(f"{chain}concat=n={len(DURS)}:v=1:a=0[body]")

    ins += ["-i", BED]
    out = os.path.join(HERE, "reviews-instagram.mp4")
    subprocess.run(["ffmpeg", "-v", "error", "-y"] + ins +
                   ["-filter_complex", ";".join(filt),
                    "-map", "[body]", "-map", f"{len(DURS)}:a",
                    "-c:v", "libx264", "-profile:v", "high", "-crf", "19",
                    "-pix_fmt", "yuv420p", "-movflags", "+faststart",
                    "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
                    "-shortest", out], check=True)
    print(f"{TOTAL:.2f}s, {len(DURS)} slides {DURS} -> {os.path.basename(out)}")
    return out


if __name__ == "__main__":
    render()
