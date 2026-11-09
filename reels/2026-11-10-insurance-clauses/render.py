"""Render the Tue 10 Nov insurance-clauses Reel, both cuts.

STRUCTURE: the prompt first, then the payoff inside 2.4s — "3 major insurance
gaps, 1 additional coverage issue" and the four that don't match — then the
mismatch table, the expiry that outranks the liquor gap, the advice to raise
her own limit, and the vendor-insurance section her correction lands on.

THE ANSWER RANKED THE MISMATCHES DIFFERENTLY FROM THE BRIEF. The brief leads
on liquor liability. ChatGPT found that and three more, and put the policy's
expiry date above it: the certificate runs out on 31 March, seventeen days
before an April 17 event. The voiceover is written around its ranking, not
the brief's, and the hook keeps the brief's approved line because the liquor
gap is still real.

THE TWIST IS SAHIBA'S, CONFIRMED BY HER. It tells her to raise her own
liquor limit; the caterer usually holds the licence, so the fix is the
caterer's certificate naming the venue. That is the last line of the
voiceover and the beat it plays over is the answer's own vendor-insurance
section, which says her certificate does not satisfy the vendors'
obligations.

THE END CARD IS THE BUDGET LINE AND IT SUBSTITUTES for the guide's takeaway
overlay — its Nov 3 soft mention says "instead of the usual closing line".

Audio is the Eryn voiceover at -14 LUFS and is the only audio: the screen
recording carries a silent track.
"""
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.join(HERE, "build")
BEATS = os.path.join(BUILD, "beats")
CARDS = os.path.join(BUILD, "cards")
VO = os.path.join(BUILD, "vo", "insurance-clauses-eryn.wav")

W, H, FPS = 1080, 1920, 30
PUSH = 1.04
TOTAL = 18.96   # the voiceover

PLAN = {
    "instagram": [
        ("b0-prompt", 2.40),
        ("b1-gaps",   3.10),
        ("b2-table",  3.10),
        ("b3-expiry", 3.40),
        ("b4-raise",  3.20),
        ("b5-vendor", 3.76),
    ],
    "tiktok": [
        ("b0-prompt", 2.20),
        ("b1-gaps",   3.20),
        ("b2-table",  3.00),
        ("b3-expiry", 3.50),
        ("b4-raise",  3.20),
        ("b5-vendor", 3.86),
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
    pairs = [(0, HOOK[name]), (5, END[name])]
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

    ins, filt = [], []
    for i, (beat, dur) in enumerate(plan):
        ins += ["-loop", "1", "-t", f"{dur:.3f}", "-i", os.path.join(BEATS, beat + ".png")]
        filt.append(seg(i, dur))
    chain = "".join(f"[v{i}]" for i in range(len(plan)))
    filt.append(f"{chain}concat=n={len(plan)}:v=1:a=0[body]")

    cards = [(HOOK[name], wins[0][0], wins[0][0] + 2.3),
             (END[name], wins[5][1] - 3.0, wins[5][1])]
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
    out = os.path.join(HERE, f"insurance-clauses-{name}.mp4")
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
