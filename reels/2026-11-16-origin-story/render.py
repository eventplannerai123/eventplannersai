"""Render the Mon 16 Nov origin-story Reel, both cuts.

STRUCTURE INVERTS THE USUAL ORDER ON PURPOSE. The Mon 16 brief says "open on
the finished, coded list, not the upload", because this is her origin story
rather than a demo — the first time AI saved her real time, so her words lead
and the screen follows. So b0 is the five guest-type codes, the payoff, and
the prompt comes second. The prompt is still in the cut and still in the
caption; nothing is hidden.

That also settles the 6-second ceiling: the payoff is frame one.

THE ANSWER DID EVERYTHING THE BRIEF PREDICTED. 3,500 registrations in, 112
duplicates out, 3,388 name tags, every organisation name standardised (it
lists the 35 variations it corrected, which is the 96 spellings of 61 names
the file was built with), and the five codes totalling 3,388 — 2,540 DEL,
510 SPO, 96 SPK, 162 STF, 80 VIP.

THE TWIST IS HERS, AND SHE CONFIRMED IT. The answer codes every row by the
guest type the attendee picked at registration, and a badge has to say what
someone is doing on site: a sponsor who is also speaking needs SPK, not SPO.
Anyone with two roles is still a check by hand. The last voiceover line, the
end card and the caption's second paragraph are built on that.

NO BUDGET LINE — the brief says so, and the Nov 3 soft mention covers Thu 5,
Mon 9, Tue 10 and Tue 17 only.

Audio is the Eryn voiceover at -14 LUFS and is the only audio: the screen
recording carries a silent track, and a piece with a voiceover takes no bed.
"""
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.join(HERE, "build")
BEATS = os.path.join(BUILD, "beats")
CARDS = os.path.join(BUILD, "cards")
VO = os.path.join(BUILD, "vo", "origin-story-eryn.wav")

W, H, FPS = 1080, 1920, 30
PUSH = 1.04
TOTAL = 19.44   # the voiceover

PLAN = {
    "instagram": [
        ("b0-codes",      3.60),
        ("b1-prompt",     3.80),
        ("b2-duplicates", 4.10),
        ("b3-orgs",       3.70),
        ("b4-files",      4.24),
    ],
    "tiktok": [
        ("b0-codes",      3.40),
        ("b1-prompt",     3.70),
        ("b2-duplicates", 4.20),
        ("b3-orgs",       3.90),
        ("b4-files",      4.24),
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
    assert plan[0][0] == "b0-codes", f"{name} does not open on the coded list"
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
    out = os.path.join(HERE, f"origin-story-{name}.mp4")
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
