"""Render the Tue 24 Nov Thanksgiving Reel.

The Oct 29 food-quantities format the brief points at (that one reached 248):
one overlay held for the whole clip, a short Eryn voiceover, 8-12 seconds, no
screen recording and no demo file. The 15-20 second target does not apply.

**THE BRIEF'S FOOTAGE DID NOT EXIST AND COULD NOT.** It asked her to film her
own Thanksgiving prep by Sun 22 — the table being laid, the shopping list, the
oven, bags coming in. On Sat 21 she said she is doing nothing until Thursday
morning and her mother-in-law is doing the shopping, so there was nothing to
film. A text card was the fallback; she offered old Thanksgiving footage
instead, which is better, and this is built from it.

HER MEDIA IS NOT IN THIS REPO. Two .mov files and two stills, read from the
scratch path in $TG_SRC. The repo is public and only finished cuts belong in
it.

Both clips report 1920x1080 and carry **rotation=-90**, so they decode as
1080x1920 — already the output frame, no crop. That is the Oct 7 lesson:
`stream=width,height` alone is misleading for anything shot on a phone.

**THE SOURCE AUDIO IS DROPPED.** Both clips have a real AAC track from her
kitchen. The rule is that the voiceover is the only audio, and it also means
nothing anyone said at that table goes out.

Beats, 8.60s:

- 2.40s  the stuffing pan steaming on the hob. Motion from frame one, and
         steam reads as cooking before any word does.
- 3.80s  the pan across the laid table: mac and cheese, creamed spinach,
         roast potatoes, garlic knots, an empty plate waiting. **Cut at
         4.60s of a 5.80s clip** — a hand comes into the bottom of frame at
         about 4.75s and there is no reason to include it.
- 2.40s  the turkey, with a 4% push so it is not a dead stop.

The voiceover is 6.53s and starts at 0.90s, so it ends at 7.43s and the
turkey holds for just over a second after it. A freeze on the last frame is
fine; a long silent tail is not, and 1.2s is not one.
"""
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
CARDS = os.path.join(HERE, "build", "cards")
VO = os.path.join(HERE, "build", "vo", "thanksgiving-eryn.wav")
SRC = os.environ["TG_SRC"]

W, H, FPS = 1080, 1920, 30
PUSH = 1.04
VO_AT = 0.90

# Two cuts, same footage, different held overlay and slightly different
# pacing — never the same file posted twice.
PLAN = {
    "instagram": [
        ("pan.mov",    0.00, 2.40),   # the stuffing pan, steaming
        ("table.mov",  0.00, 3.80),   # the laid table; a hand arrives at ~4.75s
        ("turkey.jpg", None, 2.40),   # the platter, with a slow push
    ],
    "tiktok": [
        ("pan.mov",    0.00, 2.20),
        ("table.mov",  0.00, 4.00),
        ("turkey.jpg", None, 2.40),
    ],
}
TOTAL = 8.60


def render(cut):
    BEATS = PLAN[cut]
    assert abs(sum(b[2] for b in BEATS) - TOTAL) < 0.01, f"{cut} is not {TOTAL}s"
    assert 8.0 <= TOTAL <= 12.0, f"{TOTAL:.2f}s is outside the brief's 8-12s"
    ins, filt = [], []
    for i, (name, start, dur) in enumerate(BEATS):
        p = os.path.join(SRC, name)
        assert os.path.exists(p), p
        if start is None:
            ins += ["-loop", "1", "-t", f"{dur:.3f}", "-i", p]
            w, h = int(W * PUSH) // 2 * 2, int(H * PUSH) // 2 * 2
            filt.append(
                f"[{i}:v]scale={w}:{h}:flags=lanczos,"
                f"crop={W}:{H}:{(w - W) // 2}:'(ih-{H})*(t/{dur:.3f})',"
                f"fps={FPS},setsar=1[v{i}]")
        else:
            ins += ["-ss", f"{start:.3f}", "-t", f"{dur:.3f}", "-i", p]
            filt.append(
                f"[{i}:v]scale={W}:{H}:force_original_aspect_ratio=increase,"
                f"crop={W}:{H},fps={FPS},setsar=1[v{i}]")
    chain = "".join(f"[v{i}]" for i in range(len(BEATS)))
    filt.append(f"{chain}concat=n={len(BEATS)}:v=1:a=0[body]")

    n = len(BEATS)
    ins += ["-i", os.path.join(CARDS, f"held-{cut}.png")]
    filt.append(f"[body][{n}:v]overlay=0:0:eof_action=repeat:repeatlast=1[ov]")

    # The voiceover is the only audio: her clips' own tracks are never mapped.
    ins += ["-i", VO]
    filt.append(f"[{n + 1}:a]adelay={int(VO_AT * 1000)}|{int(VO_AT * 1000)},"
                f"apad,atrim=0:{TOTAL:.3f}[a]")

    out = os.path.join(HERE, f"thanksgiving-{cut}.mp4")
    subprocess.run(["ffmpeg", "-v", "error", "-y"] + ins +
                   ["-filter_complex", ";".join(filt),
                    "-map", "[ov]", "-map", "[a]",
                    "-c:v", "libx264", "-profile:v", "high", "-crf", "19",
                    "-pix_fmt", "yuv420p", "-movflags", "+faststart",
                    "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
                    "-t", f"{TOTAL:.3f}", out], check=True)
    print(f"{cut}: {TOTAL:.2f}s -> {os.path.basename(out)}")
    return out


if __name__ == "__main__":
    for cut in ("tiktok", "instagram"):   # TikTok first, as the briefs require
        render(cut)
