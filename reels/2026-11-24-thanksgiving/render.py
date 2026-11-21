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

Beats, 9.60s:

- 2.20s  the stuffing pan steaming on the hob. Motion from frame one, and
         steam reads as cooking before any word does.
- 2.20s  the sheet tray of roasted vegetables, still on the counter. **Added
         Sat 21** — she sent it after seeing the three-beat cut, full size
         (1512x2016), so it takes the same cover-and-push treatment as the
         turkey. Its push pans **upward** where the turkey's pans down, so
         the two stills do not read as the same move twice.
- 2.80s  the pan across the laid table: mac and cheese, creamed spinach,
         roast potatoes, garlic knots, an empty plate waiting. **Cut at
         4.60s of a 5.80s clip** — a hand comes into the bottom of frame at
         about 4.75s and there is no reason to include it. It was 3.80s
         before the tray went in; 2.80s still reads the pan.
- 2.40s  the turkey, with a 4% push so it is not a dead stop.

The voiceover is 6.53s and starts at **1.20s** (0.90s before the tray), so
it ends at 7.73s and the turkey holds 1.87s after it. A freeze on the last
frame is fine; a long silent tail is not, and the whole piece grew by one
second rather than by the tray's full length for exactly that reason.
"""
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
CARDS = os.path.join(HERE, "build", "cards")
VO = os.path.join(HERE, "build", "vo", "thanksgiving-eryn.wav")
SRC = os.environ["TG_SRC"]

W, H, FPS = 1080, 1920, 30
PUSH = 1.04
VO_AT = 1.20

# Two cuts, same footage, different held overlay and slightly different
# pacing — never the same file posted twice.
PLAN = {
    "instagram": [
        ("pan.mov",    0.00, 2.20),   # the stuffing pan, steaming
        ("veg.jpg",    None, 2.20),   # the sheet tray, pushing upward
        ("table.mov",  0.00, 2.80),   # the laid table; a hand arrives at ~4.75s
        ("turkey.jpg", None, 2.40),   # the platter, pushing downward
    ],
    "tiktok": [
        ("pan.mov",    0.00, 2.00),
        ("veg.jpg",    None, 2.40),
        ("table.mov",  0.00, 2.80),
        ("turkey.jpg", None, 2.40),
    ],
}
TOTAL = 9.60

# Which way each still's crop travels. Two stills in one cut pushing the same
# way reads as one move repeated, so they are opposed.
PUSH_DOWN = {"turkey.jpg": True, "veg.jpg": False}


def render(cut):
    BEATS = PLAN[cut]
    assert abs(sum(b[2] for b in BEATS) - TOTAL) < 0.01, f"{cut} is not {TOTAL}s"
    assert 8.0 <= TOTAL <= 12.0, f"{TOTAL:.2f}s is outside the brief's 8-12s"
    # The voiceover must not be left hanging on a silent tail.
    assert TOTAL - (VO_AT + 6.53) <= 2.0, "the tail after the voiceover is too long"
    stills = [b[0] for b in BEATS if b[1] is None]
    assert len({PUSH_DOWN[s] for s in stills}) == len(stills), (
        "two stills in one cut push the same way")
    ins, filt = [], []
    for i, (name, start, dur) in enumerate(BEATS):
        p = os.path.join(SRC, name)
        assert os.path.exists(p), p
        if start is None:
            # The still is 3:4, not 9:16, so it is COVERED and cropped like
            # the clips rather than scaled to the frame — scaling a 1512x2016
            # photo straight to 1080x1920 would stretch it 33%. The 4% push
            # then pans the crop down over the beat so it is not a dead stop.
            ins += ["-loop", "1", "-t", f"{dur:.3f}", "-i", p]
            w, h = int(W * PUSH) // 2 * 2, int(H * PUSH) // 2 * 2
            assert name in PUSH_DOWN, f"{name} has no push direction"
            travel = (f"(t/{dur:.3f})" if PUSH_DOWN[name]
                      else f"(1-t/{dur:.3f})")
            filt.append(
                f"[{i}:v]scale={w}:{h}:force_original_aspect_ratio=increase:"
                f"flags=lanczos,"
                f"crop={W}:{H}:(iw-{W})/2:'(ih-{H})*{travel}',"
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
