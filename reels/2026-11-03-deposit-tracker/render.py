"""Render both cuts of the Tue 3 Nov vendor deposit tracker redo.

ONE SOURCE, HERS, NOT IN THIS REPO (raw media never is): the ChatGPT screen
recording she filmed Sat 31 Oct, three days early, 1206x2622, 38.6s, 60fps
HEVC. She uploads the payment sheet as a PDF and asks for every payment still
owed; ChatGPT returns a totals dashboard, a chronological table with the
wedding-relative dates resolved, a 30-day priority card, a what-could-change
section and a vendor-by-vendor breakdown.

THE ANSWER MATCHES THE GUIDE'S SANITY CHECK EXACTLY: $74,940 contracted,
$28,225 paid, $46,715 still owed, transportation ($1,350, Nov 1) next. That is
the check the demo file was built for, and it held.

FREEZE FRAMES, NOT SCROLLING. The answer is one long scroll, so every beat is a
still lifted from it and held, per rule 3, with the highlighted line snapped to
its real ink by tools/cardkit.fit_highlight. Motion comes from a slow 4% push
across each beat instead of from her thumb.

CROP computed from the source: 1206 wide means 1206/0.5625 = 2144 tall, and the
standard 478 y-offset applies — status bar and red recording dot off the top,
ChatGPT's input bar left at the bottom where the platform's furniture covers
it. The floating scroll-to-bottom button stays in frame, her instruction of
Oct 10.

THE OPENING IS EXACTLY RIGHT AND NEEDED NO RESCUE: at 0.0s the prompt is
sitting in the input box with the PDF attached and the send button in shot, and
the tap lands inside the first second. Both cuts still open on the answer,
because the guide's format line for this piece asks for the finished list
first — the prompt is the second beat, never cut.

NO AD IN THIS RECORDING. Nine advertisers so far and the list keeps growing, so
the export is scanned to its final frame rather than searched for a known logo.

The two cuts diverge in more than the hook: Instagram opens on the
chronological table and closes on the catering warning; TikTok opens on the
totals dashboard, carries the 30-day priority card instead, and closes on the
same warning after a longer run through the dates.
"""
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
B = os.path.join(HERE, "build")
F = os.path.join(B, "frames")

FPS = 30
LEAD = 1.0
PUSH = 1.04          # slow Ken Burns across each still, 4% over its own length

# (still, seconds). Voiceover sentence boundaries, by word count against the
# measured 26.28s / 28.53s Eryn takes:
#   "Nine vendors still owed money…"        0.0 - 4.1
#   "I don't retype amounts…"               4.1 - 6.3
#   "I upload the payment sheet…"           6.3 - 10.3
#   "…with the real dates worked out…"     10.3 - 17.8
#   "It totals what's paid and what's owed" 17.8 - 24.4
#   "Upload the file. Don't retype it."    24.4 - 26.3
BEATS = {
    "instagram": [
        ("chrono",   4.6),   # the finished list, Nov 1 transportation highlighted
        ("prompt",   3.2),   # the sent prompt, PDF attached
        ("sheet",    3.0),   # the payment sheet she uploaded
        ("chrono2",  4.2),   # further down the same table
        ("relative", 3.8),   # the band, due on the wedding day
        ("totals",   3.5),   # $46,715 still owed
        ("catering", 7.7),   # "My biggest concern is catering."
    ],
    "tiktok": [
        ("totals",   4.8),
        ("prompt",   3.4),
        ("sheet",    3.0),
        ("chrono",   4.4),
        ("relative", 4.6),
        ("priority", 4.2),   # $7,350 due in the next 30 days
        ("catering", 7.6),
    ],
}
TOTAL = {"instagram": 30.0, "tiktok": 32.0}
# Measured: Instagram -24.0 LUFS / -1.6 TP, TikTok -23.7 / -1.1. loudnorm's
# two-pass stalls at -16.5 on Eryn's crest factor, so the gain goes on
# explicitly and alimiter catches the peaks with level=0 — auto level
# renormalises back to full scale and looks exactly like no limiting at all.
# Tuned against the export, not computed.
GAIN = {"instagram": 12.8, "tiktok": 12.5}


def seg(i, dur):
    """A still, pushed in 4% over its own length."""
    w, h = int(1080 * PUSH) // 2 * 2, int(1920 * PUSH) // 2 * 2
    return (f"[{i}:v]scale={w}:{h}:flags=lanczos,"
            f"crop=1080:1920:{(w - 1080) // 2}:'(ih-1920)*(t/{dur:.3f})',"
            f"fps={FPS},setsar=1[v{i}]")


def build(platform, out):
    beats = BEATS[platform]
    total = TOTAL[platform]
    vo = os.path.join(B, "vo", f"deposit-{platform}-eryn.mp3")
    hook = os.path.join(B, f"card-hook-{platform}.png")
    take = os.path.join(B, "card-takeaway.png")

    cmd = ["ffmpeg", "-y"]
    for name, dur in beats:
        cmd += ["-loop", "1", "-t", f"{dur}", "-i", os.path.join(F, f"{name}-hl.png")]
    cmd += ["-i", vo, "-i", hook, "-i", take]

    n = len(beats)
    parts = [seg(i, dur) for i, (_, dur) in enumerate(beats)]
    parts.append("".join(f"[v{i}]" for i in range(n)) + f"concat=n={n}:v=1:a=0[base]")
    parts.append(f"[{n+1}:v]format=rgba[hk]")
    parts.append(f"[{n+2}:v]format=rgba[tk]")
    # repeatlast=1, or a single-frame PNG shows on frame one and then vanishes.
    parts.append("[base][hk]overlay=0:0:eof_action=repeat:repeatlast=1"
                 ":enable='between(t,0,2)'[b1]")
    parts.append(f"[b1][tk]overlay=0:0:eof_action=repeat:repeatlast=1"
                 f":enable='between(t,{total-3:.2f},{total})'[vout]")
    parts.append(f"[{n}:a]volume={GAIN[platform]}dB,alimiter=limit=0.841:level=0,"
                 f"aresample=48000,adelay={int(LEAD*1000)}|{int(LEAD*1000)},"
                 f"apad,atrim=0:{total}[aout]")

    cmd += ["-filter_complex", ";".join(parts),
            "-map", "[vout]", "-map", "[aout]", "-t", f"{total}",
            "-c:v", "libx264", "-profile:v", "high", "-crf", "19",
            "-pix_fmt", "yuv420p", "-r", str(FPS), "-movflags", "+faststart",
            "-c:a", "aac", "-b:a", "192k", "-ar", "48000", out]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        print(r.stderr[-3000:])
        raise SystemExit(1)
    print(out, "ok")


def main():
    for platform in ("tiktok", "instagram"):     # TikTok first, per the briefs
        assert abs(sum(d for _, d in BEATS[platform]) - TOTAL[platform]) < 1e-6
        build(platform, os.path.join(HERE, f"deposit-tracker-{platform}.mp4"))


if __name__ == "__main__":
    main()
