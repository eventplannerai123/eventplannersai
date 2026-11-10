"""Render the Thu 12 Nov ticket-allocation Reel, both cuts.

STRUCTURE follows the voiceover, not the scroll: the prompt, then the payoff
inside 2.4s — 140 duplicate invitations and still inside the 2,000-seat
capacity — then what the duplicates are, the seats actually left, the bottom
line, and last the duplicate list itself, which is what the twist is about.
That is why b5 sits 8 seconds EARLIER in the recording than b4.

THE ANSWER HIT EVERY NUMBER THE BRIEF PREDICTED: 2,125 invitation records,
140 people invited twice, 1,985 unique invitees, 15 seats left, clients 40
over and prospects 85 over on paper. It also went further than the brief in
one place — every duplicate is classified once as a Client and once as a
Prospect, so the category split cannot be settled without a human.

THE TWIST IS THE BRIEF'S PREDICTED ONE, AND THE ANSWER SAYS IT OUT LOUD:
"I used email addresses as the primary identifier, rather than names alone."
So one person with a work address and a personal address is still two people
to it. That is the last line of the voiceover, over the duplicate list.

THE END CARD IS THE GUIDE'S OWN TAKEAWAY. No BUDGET line on this one: the
Nov 3 soft mention covers Thu 5, Mon 9, Tue 10 and Tue 17 only.

Audio is the Eryn voiceover at -14 LUFS and is the only audio: the screen
recording carries a silent track.
"""
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.join(HERE, "build")
BEATS = os.path.join(BUILD, "beats")
CARDS = os.path.join(BUILD, "cards")
VO = os.path.join(BUILD, "vo", "ticket-allocation-eryn.wav")

W, H, FPS = 1080, 1920, 30
PUSH = 1.04
TOTAL = 18.48   # the voiceover

PLAN = {
    "instagram": [
        ("b0-prompt",   2.40),
        ("b1-overall",  3.10),
        ("b2-dupes",    3.00),
        ("b3-remaining",3.20),
        ("b4-bottom",   2.90),
        ("b5-list",     3.88),
    ],
    "tiktok": [
        ("b0-prompt",   2.20),
        ("b1-overall",  3.20),
        ("b2-dupes",    3.00),
        ("b3-remaining",3.30),
        ("b4-bottom",   2.90),
        ("b5-list",     3.88),
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
    out = os.path.join(HERE, f"ticket-allocation-{name}.mp4")
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
