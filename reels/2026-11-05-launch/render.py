"""Render the Thu 5 Nov launch Reel, both cuts.

STRUCTURE IS THE GUIDE'S: payoff first (the filled tracker, readable inside two
seconds), then the prompt, then the answer, then the tracker's amounts, then
the cut to the contract reader and its "10 business days" row, ending on the
prompt with the Comment BUDGET card.

HER THREE NOTES OF NOV 3, and what each changed:

  "Open on Vendor | Amount | Due date | Flag together, not the Days/Flag
  columns alone." The Payments tab is wider than a phone, so no single frame
  of the first recording held those four. The tracker copy now has every other
  column hidden, which puts exactly those four on screen at readable size —
  `b0-four` comes from a recording of that.

  "Contract shot: zoom on the quote and May 3, 2027, with the overlay above the
  text, not on it." `b6-clause` lifts the Payment Schedule paragraph onto its
  own panel over a hard blur (see make_clause.py — a straight crop either
  clips the lines or barely magnifies), and the card now sits at y=494, well
  above the panel at y=840. `b6-contract` follows with the table row.

  "End on the tracker or the product cover, not the keyboard." The last beat
  is the tracker's amount column; the Comment BUDGET card goes over that.

Freeze frames with a slow push, never scrolling footage — a phone scroll reads
as a smear at 30fps and the rules ban it outright. The push is 4%, the same as
the deposit tracker build.

THE TWO CUTS DIFFER IN HOOK AND PACING, never in one file posted twice.
Instagram takes the guide's narrative hook; TikTok takes a command-style one
and runs its middle beats a little tighter.

Audio is the Eryn voiceover at -14 LUFS, and it is the only audio: the screen
recordings carry a silent track.
"""
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.join(HERE, "build")
BEATS = os.path.join(BUILD, "beats")
CARDS = os.path.join(BUILD, "cards")
VO = os.path.join(BUILD, "vo", "launch-eryn.wav")

W, H, FPS = 1080, 1920, 30
PUSH = 1.04

# name -> (beat, seconds). The sum is the voiceover's 21.92s.
PLAN = {
    "instagram": [
        ("b0-four",     2.4),
        ("b2-prompt",   2.6),
        ("b3-table",    3.2),
        ("b4-dates",    4.0),
        ("b6-clause",   3.4),
        ("b6-contract", 3.2),
        ("b7-four",     3.12),
    ],
    "tiktok": [
        ("b0-four",     2.2),
        ("b2-prompt",   2.4),
        ("b3-table",    3.0),
        ("b4-dates",    4.2),
        ("b6-clause",   3.6),
        ("b6-contract", 3.4),
        ("b7-four",     3.12),
    ],
}
HOOK = {"instagram": "hook-instagram", "tiktok": "hook-tiktok"}
GAIN = {"instagram": 0.0, "tiktok": 0.0}


def windows(plan):
    """(start, end) per beat, so a card's window is measured, not typed."""
    t, out = 0.0, []
    for _, d in plan:
        out.append((t, t + d))
        t += d
    return out, t


def seg(i, dur):
    """One beat: a still, pushed 4% over its own length."""
    w, h = int(W * PUSH) // 2 * 2, int(H * PUSH) // 2 * 2
    return (f"[{i}:v]scale={w}:{h}:flags=lanczos,"
            f"crop={W}:{H}:{(w - W) // 2}:'(ih-{H})*(t/{dur:.3f})',"
            f"fps={FPS},setsar=1[v{i}]")


def preview(name):
    """Composite every card onto its own beat — the check before an export."""
    from PIL import Image
    plan = PLAN[name]
    wins, _ = windows(plan)
    pairs = [(0, HOOK[name]), (4, "contract"), (6, "end")]
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
    assert abs(total - 21.92) < 0.05, f"{name} runs {total:.2f}s, not the voiceover's 21.92s"

    ins, filt = [], []
    for i, (beat, dur) in enumerate(plan):
        ins += ["-loop", "1", "-t", f"{dur:.3f}", "-i", os.path.join(BEATS, beat + ".png")]
        filt.append(seg(i, dur))
    chain = "".join(f"[v{i}]" for i in range(len(plan)))
    filt.append(f"{chain}concat=n={len(plan)}:v=1:a=0[body]")

    # Cards, each over the beat it was placed against.
    cards = [(HOOK[name], wins[0][0], wins[0][0] + 2.3),
             ("contract", wins[4][0], wins[4][1]),
             ("end", wins[6][0], wins[6][1])]
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
    out = os.path.join(HERE, f"launch-{name}.mp4")
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
