"""Render the Fri 6 Nov three-quotes Reel, both cuts.

STRUCTURE: the prompt first, then the payoff inside 2.4s — the three real
totals with Northgate's green "Cheapest" badge — then the side-by-side
breakdown, where each vendor hides cost, the recommendation, and the twist.

THE TWIST IS THE LAST BEAT AND THE LAST VOICEOVER LINE. The guide asks for
"genuinely good, except…": the answer finds every buried extra, and its own
closing paragraph says it would not choose on the $900 alone. The voiceover
ends on the thing it cannot know — which crew has worked your venue — which is
worth more than the money between the quotes.

THE TWO CUTS DIFFER IN HOOK AND PACING, never in one file posted twice.
Instagram takes the guide's three-numbers hook; TikTok takes a command-style
one and runs its middle beats a little tighter.

Audio is the Eryn voiceover at -14 LUFS and is the only audio: the screen
recording carries a silent track.
"""
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.join(HERE, "build")
BEATS = os.path.join(BUILD, "beats")
CARDS = os.path.join(BUILD, "cards")
VO = os.path.join(BUILD, "vo", "three-quotes-eryn.wav")

W, H, FPS = 1080, 1920, 30
PUSH = 1.04
TOTAL = 21.04   # the voiceover

PLAN = {
    "instagram": [
        ("b0-prompt", 2.40),
        ("b1-cards",  3.60),
        ("b2-table",  3.40),
        ("b3-hiding", 3.20),
        ("b4-rec",    3.20),
        ("b5-final",  5.24),
    ],
    "tiktok": [
        ("b0-prompt", 2.20),
        ("b1-cards",  3.80),
        ("b2-table",  3.20),
        ("b3-hiding", 3.00),
        ("b4-rec",    3.40),
        ("b5-final",  5.44),
    ],
}
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
    pairs = [(0, HOOK[name]), (5, "end")]
    os.makedirs(os.path.join(BUILD, "preview"), exist_ok=True)
    for idx, card in pairs:
        base = Image.open(os.path.join(BEATS, plan[idx][0] + ".png")).convert("RGBA")
        over = Image.open(os.path.join(CARDS, card + ".png")).convert("RGBA")
        Image.alpha_composite(base, over).convert("RGB").save(
            os.path.join(BUILD, "preview", f"{name}-{idx}-{card}.jpg"), quality=92)
    print(f"preview written for {name}: {[c for _, c in pairs]}")


def render(name):
    plan = PLAN[name]
    wins, total = windows(plan)
    assert abs(total - TOTAL) < 0.05, f"{name} runs {total:.2f}s, not the voiceover's {TOTAL}s"

    ins, filt = [], []
    for i, (beat, dur) in enumerate(plan):
        ins += ["-loop", "1", "-t", f"{dur:.3f}", "-i", os.path.join(BEATS, beat + ".png")]
        filt.append(seg(i, dur))
    chain = "".join(f"[v{i}]" for i in range(len(plan)))
    filt.append(f"{chain}concat=n={len(plan)}:v=1:a=0[body]")

    cards = [(HOOK[name], wins[0][0], wins[0][0] + 2.3),
             ("end", wins[5][1] - 3.0, wins[5][1])]
    n = len(plan)
    last = "body"
    for j, (card, a, b) in enumerate(cards):
        ins += ["-i", os.path.join(CARDS, card + ".png")]
        tag = f"ov{j}"
        filt.append(
            f"[{last}][{n + j}:v]overlay=0:0:eof_action=repeat:repeatlast=1:"
            f"enable='between(t,{a:.3f},{b:.3f})'[{tag}]")
        last = tag

    ins += ["-i", VO]
    out = os.path.join(HERE, f"three-quotes-{name}.mp4")
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
