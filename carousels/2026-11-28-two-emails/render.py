"""Assemble the Sat 28 Nov two-emails slide Reel for Instagram and Facebook.

Six slides at 2.50s = **15.00s**, hard cuts, no push — the same reasoning as
Wed 11: these are typeset brand cards, so a 4% drift only softens the glyph
edges and a crossfade between two lavender slides reads as a smear.

Audio is a mix: Eryn at -14 LUFS and the bed pulled down under her, measured
on the finished export rather than assumed.

**THE VOICEOVER STARTS AT 2.40s, AND THE NUMBER IS LOAD-BEARING.** It runs
11.52s, so from 2.40 it ends at 13.92 and its last line — "send the one that
comes back, after one read" — lands inside slide 6, which is the slide that
says "Write the first one. Send the second." The assert below keeps that true
if the slide count or the VO ever changes.

**THE BED IS ITS OWN GENERATION**, distinct from both of Wednesday's — her
Nov 10 rule, checked on the md5 rather than by ear. Vibraphone and brushed
snare over an upright bass. Instrumental, checked the same two ways: the
spectrogram shows regular transients and no formant movement, and Scribe
returned an empty string.

**IT RINGS OUT, SO THE TRIM MATTERS.** Energy sits between -12.4 and -14.9 dB
to 24s, then falls off a cliff: -21.6 at 26s and -34.4 at 28s. The 15s cut
from 0.0 is well clear of it, but a longer piece on this bed would have to
move its window rather than extend it.
"""
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
SLIDES = os.path.join(HERE, "slides")
BED = os.path.join(HERE, "build", "music", "bed-15s.wav")
VO = os.path.join(HERE, "build", "vo", "two-emails-eryn.wav")

W, H, FPS = 1080, 1920, 30
PER_SLIDE = 2.50
N = 6
TOTAL = PER_SLIDE * N          # 15.00s
VO_AT = 2.40
VO_LEN = 11.52
BED_DB = -7.0                  # swept against the export: this bed is louder
                               # than Wednesday's, so it needs a deeper cut to
                               # sit the same distance under the voice
                               # -23 dB under the opening slide and -16 under
                               # the voice, which is present without competing


def render():
    # The ask has to land on the slide that makes it.
    last_slide_starts = TOTAL - PER_SLIDE
    assert VO_AT + VO_LEN - 1.4 >= last_slide_starts, (
        "the closing line would land before slide 6")
    assert VO_AT + VO_LEN <= TOTAL, "the voiceover runs past the last slide"

    ins, filt = [], []
    for i in range(1, N + 1):
        p = os.path.join(SLIDES, f"2026-11-28-two-emails-{i}.jpg")
        assert os.path.exists(p), p
        ins += ["-loop", "1", "-t", f"{PER_SLIDE:.3f}", "-i", p]
        filt.append(f"[{i-1}:v]scale={W}:{H},fps={FPS},setsar=1[v{i-1}]")
    chain = "".join(f"[v{i}]" for i in range(N))
    filt.append(f"{chain}concat=n={N}:v=1:a=0[body]")

    ins += ["-i", BED, "-i", VO]
    filt.append(f"[{N}:a]volume={BED_DB}dB[bed]")
    filt.append(f"[{N+1}:a]adelay={int(VO_AT*1000)}|{int(VO_AT*1000)},"
                f"apad,atrim=0:{TOTAL:.3f}[vo]")
    filt.append("[bed][vo]amix=inputs=2:duration=first:normalize=0,"
                "alimiter=limit=0.891:level=0[a]")

    out = os.path.join(HERE, "two-emails-instagram.mp4")
    subprocess.run(["ffmpeg", "-v", "error", "-y"] + ins +
                   ["-filter_complex", ";".join(filt),
                    "-map", "[body]", "-map", "[a]",
                    "-c:v", "libx264", "-profile:v", "high", "-crf", "19",
                    "-pix_fmt", "yuv420p", "-movflags", "+faststart",
                    "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
                    "-t", f"{TOTAL:.3f}", out], check=True)
    print(f"{TOTAL:.2f}s, {N} slides at {PER_SLIDE}s, VO at {VO_AT}s "
          f"-> {os.path.basename(out)}")
    return out


if __name__ == "__main__":
    render()
