"""Render the Mon 9 Nov catering-invoice Reel, both cuts.

STRUCTURE: the prompt first, then the payoff inside 2.4s — "three billing
discrepancies" and the $530 disputed total — then the line-by-line table, the
distinction that makes $530 the right number, the reconciliation that shows
the full $1,140, and the corrected invoice.

THE TWIST CAME FROM THE ANSWER, NOT FROM HER. The brief expected ChatGPT to
call all three charges an overcharge and for Sahiba to catch that the
guarantee is a minimum. It caught that itself, and said so: the $500 for four
extra guests is contractually supported if 124 people were served, so only the
$420 cake fee and the $110 bar extension are disputable. The voiceover, the
end card and the caption are written around what it actually did.

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
VO = os.path.join(BUILD, "vo", "catering-invoice-eryn.wav")

W, H, FPS = 1080, 1920, 30
PUSH = 1.04
TOTAL = 17.36   # the voiceover

PLAN = {
    "instagram": [
        ("b0-prompt",  2.40),
        ("b1-530",     2.90),
        ("b2-table",   2.90),
        ("b3-minimum", 2.90),
        ("b4-recon",   2.90),
        ("b5-dispute", 3.36),
    ],
    "tiktok": [
        ("b0-prompt",  2.20),
        ("b1-530",     3.00),
        ("b2-table",   2.90),
        ("b3-minimum", 2.80),
        ("b4-recon",   3.00),
        ("b5-dispute", 3.46),
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
             (END[name], wins[5][1] - 3.0, wins[5][1])]
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
    out = os.path.join(HERE, f"catering-invoice-{name}.mp4")
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
