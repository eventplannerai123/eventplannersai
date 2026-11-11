"""Render the Fri 13 Nov venue-email Reel, both cuts.

STRUCTURE follows the voiceover: the prompt with the quote attached, the
$45,000 Saturday total, the small-print line that the whole piece turns on,
the email it wrote, and last the negotiation tip — which is where the twist
sits, because the tip is good and the thing it leaves out is the rate lock.

THE ANSWER DID WHAT THE BRIEF PREDICTED AND ONE THING MORE. It found the
small-print line, offered a Tuesday or Wednesday in October 2027 and a
two-year commitment, and asked for the rate on each — then added a
negotiation tip the brief never asked for: don't name a target price, let
them come back with their best weekday and multi-year numbers first.

$35,000 IS NOT IN THE RECORDING AND IS NOT IN THE CUT. The guide is explicit
that the figure in the hook is the outcome Sahiba got in real life on a
similar email, shown as the payoff rather than as AI output. The answer
writes the email; it does not negotiate it. So the hook card carries the
$10,000 and no beat claims the venue replied.

THE TWIST IS THE BRIEF'S PREDICTED ONE and it is not yet confirmed by her:
the email offers a two-year commitment without asking for a rate lock or a
cancellation clause in return. She sent the recording without the "one thing
you'd still change", so the last voiceover line is the brief's prediction
checked against what the email actually says, and it goes to her with the cut.

THE END CARD IS THE GUIDE'S OWN TAKEAWAY. No BUDGET line on this one: the
Nov 3 soft mention covers Thu 5, Mon 9, Tue 10 and Tue 17 only.

Audio is the Eryn voiceover at -14 LUFS and is the only audio: the screen
recording carries a silent track, and a piece with a voiceover does not take
a music bed.
"""
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.join(HERE, "build")
BEATS = os.path.join(BUILD, "beats")
CARDS = os.path.join(BUILD, "cards")
VO = os.path.join(BUILD, "vo", "venue-email-eryn.wav")

W, H, FPS = 1080, 1920, 30
PUSH = 1.04
TOTAL = 17.52   # the voiceover

PLAN = {
    "instagram": [
        ("b0-prompt",     3.00),
        ("b1-quote",      3.40),
        ("b2-smallprint", 3.70),
        ("b3-email",      3.70),
        ("b4-tip",        3.72),
    ],
    "tiktok": [
        ("b0-prompt",     2.80),
        ("b1-quote",      3.40),
        ("b2-smallprint", 3.80),
        ("b3-email",      3.80),
        ("b4-tip",        3.72),
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
    # The payoff is the quote itself; the 6-second ceiling is on everything
    # before it, which here is the prompt beat alone.
    assert plan[0][1] <= 6.0, f"{name} takes {plan[0][1]}s to reach the quote"
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
    out = os.path.join(HERE, f"venue-email-{name}.mp4")
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
