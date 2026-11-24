"""Render the Fri 27 Nov giveaway last-day Reel, both cuts.

**NO NEW FOOTAGE, BY HER DECISION.** The Fri 27 YOU line asked for 4-6 photos
of the author copies and a fresh 10-20 second flip-through, or a word that
she would rather not film again. On Mon 23 she said so, and the line records
it: cut from the Nov 19 flip-through, IMG_0424 and IMG_0430 in Drive
November 20.

**HER FOOTAGE IS NOT IN THIS REPO.** 58 MB and 170 MB of .MOV, read from the
scratch path in $GIVE_SRC. The repo is public and only finished cuts belong
in it.

**IMG_0424 CARRIES rotation=-90 AND IMG_0430 DOES NOT.** The first reports
1920x1080 and decodes as 1080x1920; the second is already 1080x1920. ffmpeg
applies the rotation itself, so both land on the output frame with no crop —
but the Oct 7 lesson is why that was checked rather than assumed.

**IT OPENS ON BOTH BOOKS**, which is the brief's own instruction: "payoff
first: both books in shot with the overlay in the first second". IMG_0424
opens on exactly that, two copies face up on a pale table, so the first
segment is its first 3.2 seconds and the hook sits over it.

**THE LAST THREE SECONDS OF IMG_0430 ARE OUT.** The clip ends on her turning
to the camera, and the piece is about the book rather than a piece to camera;
the window used stops at 93.4s of a 101.8s clip. Its first frames are out too
for the same reason.

**THE SOURCE AUDIO IS DROPPED.** Both clips have a room track. The voiceover
is the only audio, which also means nothing said over the filming goes out.

No music bed: the voiceover carries it, and the day's other post — the
12:30pm planner-feelings Reel — has a bed of its own. Her Nov 10 rule is
that two posts on one day never share one, and the simplest way to keep that
true is for this one to have none.
"""
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.join(HERE, "build")
CARDS = os.path.join(BUILD, "cards")
VO = os.path.join(BUILD, "vo", "giveaway-eryn.wav")
SRC = os.environ["GIVE_SRC"]

W, H, FPS = 1080, 1920, 30
VO_LEN = 13.12
VO_AT = 1.20

# (file, start, duration)
PLAN = {
    "instagram": [
        ("IMG_0424.MOV",  0.00, 3.20),   # both copies on the table
        ("IMG_0424.MOV",  6.00, 4.00),   # the flip-through, page after page
        ("IMG_0430.MOV", 18.00, 5.00),   # colouring the mandala
        ("IMG_0430.MOV", 89.00, 4.40),   # the page well under way
    ],
    "tiktok": [
        ("IMG_0424.MOV",  0.00, 3.00),
        ("IMG_0424.MOV",  6.00, 4.20),
        ("IMG_0430.MOV", 18.00, 5.00),
        ("IMG_0430.MOV", 89.00, 4.40),
    ],
}
HOOK = {"instagram": "hook-instagram", "tiktok": "hook-tiktok"}
END = {"instagram": "end-instagram", "tiktok": "end-tiktok"}

# IMG_0430 ends on her turning to camera; stay clear of it.
TO_CAMERA = 94.0


def render(name):
    plan = PLAN[name]
    total = sum(d for _, _, d in plan)
    assert 15.0 <= total <= 20.0, f"{name} runs {total:.2f}s, outside 15-20s"
    assert VO_AT + VO_LEN <= total, "the voiceover runs past the last frame"
    assert total - (VO_AT + VO_LEN) <= 2.5, (
        f"{name} leaves {total - VO_AT - VO_LEN:.2f}s of silence on the end")
    assert plan[0][0] == "IMG_0424.MOV" and plan[0][1] == 0.0, (
        f"{name} does not open on both books")
    for f, s, d in plan:
        if f == "IMG_0430.MOV":
            assert s + d <= TO_CAMERA, f"{name} runs into the piece to camera"

    ins, filt = [], []
    for i, (fname, start, dur) in enumerate(plan):
        p = os.path.join(SRC, fname)
        assert os.path.exists(p), p
        ins += ["-ss", f"{start:.3f}", "-t", f"{dur:.3f}", "-i", p]
        filt.append(f"[{i}:v]scale={W}:{H}:force_original_aspect_ratio=increase,"
                    f"crop={W}:{H},fps={FPS},setsar=1[v{i}]")
    chain = "".join(f"[v{i}]" for i in range(len(plan)))
    filt.append(f"{chain}concat=n={len(plan)}:v=1:a=0[body]")

    n = len(plan)
    cards = [(HOOK[name], 0.0, 2.3), (END[name], total - 3.0, total)]
    last = "body"
    for j, (cardname, a, b) in enumerate(cards):
        ins += ["-i", os.path.join(CARDS, cardname + ".png")]
        tag = f"ov{j}"
        filt.append(f"[{last}][{n + j}:v]overlay=0:0:eof_action=repeat:"
                    f"repeatlast=1:enable='between(t,{a:.3f},{b:.3f})'[{tag}]")
        last = tag

    # The voiceover is the only audio: her clips' own tracks are never mapped.
    ins += ["-i", VO]
    filt.append(f"[{n + len(cards)}:a]adelay={int(VO_AT * 1000)}|{int(VO_AT * 1000)},"
                f"apad,atrim=0:{total:.3f}[a]")

    out = os.path.join(HERE, f"giveaway-last-day-{name}.mp4")
    subprocess.run(["ffmpeg", "-v", "error", "-y"] + ins +
                   ["-filter_complex", ";".join(filt),
                    "-map", f"[{last}]", "-map", "[a]",
                    "-c:v", "libx264", "-profile:v", "high", "-crf", "19",
                    "-pix_fmt", "yuv420p", "-movflags", "+faststart",
                    "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
                    "-t", f"{total:.3f}", out], check=True)
    print(f"{name}: {total:.2f}s, VO at {VO_AT}s -> {os.path.basename(out)}")
    return out


if __name__ == "__main__":
    for name in ("tiktok", "instagram"):   # TikTok first, as the briefs require
        render(name)
