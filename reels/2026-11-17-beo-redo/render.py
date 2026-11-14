"""Render the Tue 17 Nov BEO-redo Reel, both cuts.

Redo of the Sep 25 BEO Reel, which reached 22; the original stays up.

STRUCTURE: it opens on the finished one-page run sheet, not the upload — the
Tue 17 brief says so, the same inversion as Mon 16. The prompt is beat two
and the whole of it is in the caption, so the 6-second ceiling is satisfied
at frame one.

WHAT THE ANSWER DID. Eleven times off eleven different pages into one
chronological list, 5:45am to 11:45pm, with the room and the headcount
against each, and all four vendor numbers pulled out of the page footers
where the BEO hides them. It also noticed, unprompted, that the BEO is dated
9 February 2027 and so is not literally "tomorrow".

**THE BRIEF'S PREDICTED TWIST DID NOT HAPPEN.** It expected the answer to
keep the BEO's own page order, so that the 6am load-in would land after
dinner service. It did not: the timeline is in clock order from the first
row. Predicting a twist is not the same as having one, and this piece is the
case where the prediction was simply wrong.

**HER TWIST IS BETTER THAN THE PREDICTED ONE** (confirmed 2026-11-14). The
RESPONSIBLE/LEAD column comes back half empty — "Room reset team not named in
BEO", "Client session leads not named in BEO", "Bar operator not separately
named" — because the BEO never says. It did not invent anyone, which is
right. Her fix is a prompt fix, which is what makes it worth a Reel: add a
line asking it to list every item the BEO does not name a lead for, and the
blanks become a chase list for four o'clock the day before.

THIS ONE CARRIES THE BUDGET LINE. The Nov 3 soft mention covers Thu 5, Mon 9,
Tue 10 and Tue 17, and Tue 10 came off it on Nov 9. So the end card is
"Comment BUDGET for the tracker I use." and the TikTok cut says "Comment
BUDGET on my Instagram.", and the line is the last one in the Instagram
caption too. Browser Claude attaches the ManyChat automation at 6:32pm.

Audio is the Eryn voiceover at -14 LUFS and is the only audio.
"""
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.join(HERE, "build")
BEATS = os.path.join(BUILD, "beats")
CARDS = os.path.join(BUILD, "cards")
VO = os.path.join(BUILD, "vo", "beo-redo-eryn.wav")

W, H, FPS = 1080, 1920, 30
PUSH = 1.04
TOTAL = 18.08   # the voiceover

PLAN = {
    "instagram": [
        ("b0-runsheet",  3.40),
        ("b1-prompt",    3.50),
        ("b2-fourteen",  3.40),
        ("b3-vendors",   3.50),
        ("b4-blanks",    4.28),
    ],
    "tiktok": [
        ("b0-runsheet",  3.20),
        ("b1-prompt",    3.40),
        ("b2-fourteen",  3.50),
        ("b3-vendors",   3.60),
        ("b4-blanks",    4.38),
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
    assert plan[0][0] == "b0-runsheet", f"{name} does not open on the run sheet"
    # The twist beat goes last, under the end card.
    assert plan[-1][0] == "b4-blanks", f"{name} does not end on the twist"
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
    out = os.path.join(HERE, f"beo-redo-{name}.mp4")
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
