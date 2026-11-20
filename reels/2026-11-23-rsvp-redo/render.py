"""Render the Mon 23 Nov RSVP-redo Reel, both cuts.

Redo of the Sep 18 RSVP meal-counts Reel, which reached 31; the original
stays up. That one ran 30 RSVPs, four meal types and nine restrictions and
ended on the retired CATERER keyword. This is ten times the size and ends on
the catch.

STRUCTURE: it opens on the finished caterer sheet, not the upload — the Mon
23 brief says "payoff first ... readable in the first 2 seconds", the same
inversion as Mon 16 and Tue 17. The prompt is beat two and the whole of it is
in the caption, so the 6-second ceiling is satisfied at frame one.

**THE CHATGPT POP-UP IS OUT, BY CONSTRUCTION.** Her instruction on the
hand-over: "Remove the chatgbt pop up that’s midway." A "Get Plus" upsell
card covers the answer from 46.0s to 47.6s of the source. make_beats.py
measures that window and asserts no beat frame falls inside it, so it cannot
creep back if a frame number is ever adjusted.

WHAT THE ANSWER DID. 54 / 48 / 22 / 18 adding to 142. The 23 free-text notes
— "no gluten", "celiac", "GF please", "gluten free pls", fourteen wordings
in all — grouped into the six real restrictions with the right counts and
the names against each: gluten-free 8, nut 5, dairy 4, shellfish 3, vegan 2,
pescatarian 1. All three self-contradicting rows named. And the six plus-ones
with no meal choice called out as unknowns.

**THE BRIEF’S PREDICTED TWIST DID NOT HAPPEN.** It expected the answer to
total 142 meals anyway, reading the six empty plus-one cells as empty rather
than as a question. It did not: the closing recommendation is "Don’t
finalize the order at 142 meals just yet. You potentially have 148
attendees." Predicting a twist is not the same as having one. The brief’s
own twist line says to rewrite the last voiceover line, the overlay and the
caption’s third paragraph around what she actually catches, and all three
are written around 142-versus-148.

NO BUDGET LINE. A catering piece, not a money one — the guide’s own Mon 23
takeaway line says so, and make_cards.py asserts it.

Audio is the Eryn voiceover at -14 LUFS and is the only audio.
"""
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.join(HERE, "build")
BEATS = os.path.join(BUILD, "beats")
CARDS = os.path.join(BUILD, "cards")
VO = os.path.join(BUILD, "vo", "rsvp-redo-eryn.wav")

W, H, FPS = 1080, 1920, 30
PUSH = 1.04
TOTAL = 18.56   # the voiceover

PLAN = {
    "instagram": [
        ("b0-counts",     3.40),
        ("b1-prompt",     3.40),
        ("b2-notes",      3.60),
        ("b3-conflicts",  3.60),
        ("b4-recommend",  4.56),
    ],
    "tiktok": [
        ("b0-counts",     3.20),
        ("b1-prompt",     3.30),
        ("b2-notes",      3.70),
        ("b3-conflicts",  3.70),
        ("b4-recommend",  4.66),
    ],
}
END = {"instagram": "end-instagram", "tiktok": "end-tiktok"}
HOOK = {"instagram": "hook-instagram", "tiktok": "hook-tiktok"}


def windows(plan):
    t, out = 0.0, []
    for _, d in plan:
        out.append((t, t + d))
        t += d
    return out, t


def seg(i, dur):
    w, h = int(W * PUSH) // 2 * 2, int(H * PUSH) // 2 * 2
    return (f"[{i}:v]scale={w}:{h}:flags=lanczos,"
            f"crop={W}:{H}:{(w - W) // 2}:'(ih-{H})*(t/{dur:.3f})',"
            f"fps={FPS},setsar=1[v{i}]")


def preview(name):
    from PIL import Image
    plan = PLAN[name]
    pairs = [(0, HOOK[name]), (4, END[name])]
    os.makedirs(os.path.join(BUILD, "preview"), exist_ok=True)
    for idx, cardname in pairs:
        base = Image.open(os.path.join(BEATS, plan[idx][0] + ".png")).convert("RGBA")
        over = Image.open(os.path.join(CARDS, cardname + ".png")).convert("RGBA")
        Image.alpha_composite(base, over).convert("RGB").save(
            os.path.join(BUILD, "preview", f"{name}-{idx}-{cardname}.jpg"), quality=92)
    print(f"preview written for {name}: {[c for _, c in pairs]}")


def render(name):
    plan = PLAN[name]
    wins, total = windows(plan)
    assert abs(total - TOTAL) < 0.05, f"{name} runs {total:.2f}s, not the voiceover's {TOTAL}s"
    assert 15.0 <= total <= 20.0, f"{name} runs {total:.2f}s, outside the brief's 15-20s"
    # The payoff IS the opening shot on this piece, so the 6-second ceiling is
    # satisfied at t=0. The assert stays as a guard against reordering.
    assert plan[0][0] == "b0-counts", f"{name} does not open on the caterer sheet"
    # The twist beat goes last, under the end card.
    assert plan[-1][0] == "b4-recommend", f"{name} does not end on the catch"
    assert min(d for _, d in plan) >= 2.5, f"{name} has a beat under the 2.5s minimum"

    ins, filt = [], []
    for i, (beat, dur) in enumerate(plan):
        ins += ["-loop", "1", "-t", f"{dur:.3f}", "-i", os.path.join(BEATS, beat + ".png")]
        filt.append(seg(i, dur))
    chain = "".join(f"[v{i}]" for i in range(len(plan)))
    filt.append(f"{chain}concat=n={len(plan)}:v=1:a=0[body]")

    cards = [(HOOK[name], wins[0][0], wins[0][0] + 2.3),
             (END[name], wins[4][1] - 3.0, wins[4][1])]
    n = len(plan)
    last = "body"
    for j, (cardname, a, b) in enumerate(cards):
        ins += ["-i", os.path.join(CARDS, cardname + ".png")]
        tag = f"ov{j}"
        filt.append(
            f"[{last}][{n + j}:v]overlay=0:0:eof_action=repeat:repeatlast=1:"
            f"enable='between(t,{a:.3f},{b:.3f})'[{tag}]")
        last = tag

    ins += ["-i", VO]
    out = os.path.join(HERE, f"rsvp-redo-{name}.mp4")
    cmd = (["ffmpeg", "-v", "error", "-y"] + ins +
           ["-filter_complex", ";".join(filt),
            "-map", f"[{last}]", "-map", f"{n + len(cards)}:a",
            "-c:v", "libx264", "-profile:v", "high", "-crf", "19",
            "-pix_fmt", "yuv420p", "-movflags", "+faststart",
            "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
            "-shortest", out])
    subprocess.run(cmd, check=True)
    print(f"{name}: {total:.2f}s -> {os.path.basename(out)}")
    return out


if __name__ == "__main__":
    for name in ("tiktok", "instagram"):   # TikTok first, as the briefs require
        preview(name)
        render(name)
