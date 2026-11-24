"""Render the Sun 29 Nov budget-uplift Reel, both cuts.

Content bank 22, "Last year's budget is not this year's budget" — and the
piece goes a step past the cliché: where next year is already quoted, use the
quote instead of the uplift.

STRUCTURE: it opens on the finished 2027 column, not the upload. The Sun 29
brief says "payoff first ... readable in the first 2 seconds", so $113,179 is
on screen at t=0 with venue at 8.33% and catering at 6.34% underneath it. The
prompt is beat two and the whole of it is in the caption, so the 6-second
ceiling is satisfied at frame one.

**THE GUIDE'S FIGURE WAS A DOLLAR OUT AND THE SCREEN WINS.** The brief
predicted $113,180 and wrote the voiceover as "a hundred and thirteen,
one-eighty". Two lines land on a half-dollar at 3% — printing $1,905.50 and
insurance $1,287.50 — and the answer kept both rather than rounding up, so
what is on screen is **$113,179**. A voiceover that says a number the frame
contradicts is broken, so the script, the caption and
demo-files/2026-11/annual_summit_actuals.py all moved to the screen's figure;
the gap on a flat uplift is $2,145, not $2,146. Worth correcting in the guide.

**THE TWIST IS HERS, ARRIVED AT BACKWARDS.** Her Sun 29 YOU line asks for the
one thing she would still change. She said she would change nothing and asked
what this session thought. The answer's section 2, "Lines most likely to
increase faster than 3%", opens with venue and catering, both High — the only
two lines in the budget that are already contracted. A risk list is for what
can still move. She agreed: "yes thats the twist". It is b3, the last line of
the voiceover and the caption's third paragraph.

**THIS PIECE DOES CARRY THE BUDGET CTA**, unlike Mon 23 and Tue 17. The Nov
14 rule is to read the closing line against the piece, not to ban it: this is
a budget, and the guide calls it the one money piece inside the Black Friday
window. make_cards.py asserts the CTA is present and carries its deadline,
which is the inverse of the assert on the catering pieces. **ManyChat is
paused**, so the DM is hers by hand — her Sun 29 YOU line says so.

The takeaway and the CTA run one after the other over the last beat rather
than stacking: two lavender panels at once on a dense page reads as a
mistake.

Audio is the Eryn voiceover at -14 LUFS and is the only audio.
"""
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.join(HERE, "build")
BEATS = os.path.join(BUILD, "beats")
CARDS = os.path.join(BUILD, "cards")
VO = os.path.join(BUILD, "vo", "budget-uplift-eryn.wav")

W, H, FPS = 1080, 1920, 30
PUSH = 1.04
TOTAL = 19.68   # the voiceover

PLAN = {
    "instagram": [
        ("b0-budget", 3.60),
        ("b1-prompt", 3.40),
        ("b2-total",  3.60),
        ("b3-risk",   4.20),
        ("b4-end",    4.88),
    ],
    "tiktok": [
        ("b0-budget", 3.40),
        ("b1-prompt", 3.30),
        ("b2-total",  3.70),
        ("b3-risk",   4.40),
        ("b4-end",    4.88),
    ],
}
HOOK = {"instagram": "hook-instagram", "tiktok": "hook-tiktok"}
TAKE = {"instagram": "take-instagram", "tiktok": "take-tiktok"}
CTA = {"instagram": "cta-instagram", "tiktok": "cta-tiktok"}


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
    pairs = [(0, HOOK[name]), (4, TAKE[name]), (4, CTA[name])]
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
    assert plan[0][0] == "b0-budget", f"{name} does not open on the 2027 column"
    # The twist beat is b3 and the summary closes.
    assert plan[3][0] == "b3-risk", f"{name} loses the twist beat"
    assert plan[-1][0] == "b4-end", f"{name} does not end on the summary"
    assert min(d for _, d in plan) >= 2.5, f"{name} has a beat under the 2.5s minimum"

    ins, filt = [], []
    for i, (beat, dur) in enumerate(plan):
        ins += ["-loop", "1", "-t", f"{dur:.3f}", "-i", os.path.join(BEATS, beat + ".png")]
        filt.append(seg(i, dur))
    chain = "".join(f"[v{i}]" for i in range(len(plan)))
    filt.append(f"{chain}concat=n={len(plan)}:v=1:a=0[body]")

    # Takeaway then CTA, back to back over the last beat — never stacked.
    cards = [(HOOK[name], wins[0][0], wins[0][0] + 2.3),
             (TAKE[name], wins[4][1] - 3.0, wins[4][1] - 1.4),
             (CTA[name], wins[4][1] - 1.4, wins[4][1])]
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
    out = os.path.join(HERE, f"budget-uplift-{name}.mp4")
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
