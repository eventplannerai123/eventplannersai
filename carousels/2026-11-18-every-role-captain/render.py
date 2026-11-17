"""Assemble the Wed 18 Nov slide Reel for Instagram and Facebook.

The Nov 8 format rule: Instagram and Facebook get a slide Reel, each slide
about 2.5 seconds, music; TikTok gets the same six JPEGs as a photo carousel,
which needs no assembly.

HARD CUTS AND NO PUSH. These are typeset brand slides, not screenshots of a
scrolling answer: a push on 72px margins softens the glyph edges for nothing,
and a crossfade between two lavender cards reads as a smear.

SIX SLIDES AT 3.00s, SO 18.0s — slowed from 2.50s on her note of Nov 17
("slow down the reel a little"). Still inside the 15–20s target, and slide 5
is the reason: it carries a card, five thumbnails and the flag, which is more
to read in one beat than any slide of the Sunday set. One more slide than Sunday, because the answer slide has to
stand on its own. Slide 5 carries the Registration card, five thumbnails and
the flag, and folding it into a five-slide set would mean cutting either the
thumbnails or the flag, and the flag is the piece.

THE BED IS ITS OWN AND IT IS UPBEAT, per her Nov 10 instruction: nylon-string
guitar and a woodblock pulse over an upright bass. **Wednesday has two posts,
and they do not share a track** — on Nov 11 both went out on one bed, the
short cut being the opening bars of the long one, and she heard it at once
("are they both the same?"). The 12:30pm planner-feelings Reel has its own
Rhodes-and-glockenspiel generation.

Instrumental, checked the same two ways as every bed before it: a spectrogram
read for the formant movement a sung vowel makes, and Scribe, which returned
an empty string. The generation's own settings are not the check — they
report "Instrumental: False" either way.

The spectrogram also settles the trim: this one has full texture from 0.0s,
so the cut starts there rather than hunting past a quiet head. 0.8s fade in,
1.2s fade out, and it came out of the model hot enough that 0 dB of gain
measured -13.9 LUFS — no gain at all. Never carry a figure over.
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
        p = os.path.join(SLIDES, f"2026-11-18-every-role-captain-{i}.jpg")
        assert os.path.exists(p), p
        ins += ["-loop", "1", "-t", f"{PER_SLIDE:.3f}", "-i", p]
        filt.append(f"[{i-1}:v]scale={W}:{H},fps={FPS},setsar=1[v{i-1}]")
    chain = "".join(f"[v{i}]" for i in range(N))
    filt.append(f"{chain}concat=n={N}:v=1:a=0[body]")

    ins += ["-i", BED]
    out = os.path.join(HERE, "every-role-captain-instagram.mp4")
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
