"""Render both cuts of the Mon 2 Nov "fees nobody quotes" Reel.

ONE SOURCE, HERS, NOT IN THIS REPO (raw media never is): the ChatGPT screen
recording she filmed Sat 31 Oct — six days early, in the same sitting as the
deposit tracker one. 1206x2622, 40.4s, 60fps HEVC. She uploads the six-page
Winter Gala proposal and asks for every fee outside the $185 headline rate.

THE PREDICTED TWIST DID NOT HAPPEN, AND THAT IS HER CALL. The guide's Oct 14
twist note expected the model to treat the 7% administrative fee like a tip.
It does the opposite, in its own bullet: "This is separate from the 22% service
charge. The venue explicitly says it is not a gratuity." Asked what she would
still change, she said: "its clean". So this is a straight demo and the
voiceover, takeaway and caption are the brief's as written, with no "genuinely
good, except…" paragraph bolted on. That is the second piece running where the
twist failed to land — worth watching rather than writing the twist in advance.

IT FOUND ALL EIGHT FEES and the arithmetic matches the demo file: linen
$1,450, coat check $720, cake cutting $630, service charge $7,326,
bartenders $525, security $780, administrative fee $2,331, overtime $1,200+.

TWO REAL NUMBERS, AND THE CUTS HANDLE THEM DIFFERENTLY. Its headline figure is
$253.40 a head ($45,612) because it treats the linen upgrade as optional, and
it then gives $261.46 ($47,062) with the upgrade in — which is the guide's
sanity-check number and the one the voiceover, hook and caption all say.
Instagram therefore never shows $253.40 at all: it goes from the fee table to
the $261.46 line, so there is one number in the piece. TikTok shows both, in
the order the answer gives them, and closes on "I would budget $46,000-$47,000"
where Instagram closes on the $261.46 line.

FREEZE FRAMES, NOT SCROLLING, per rule 3, with a slow 4% push so no beat is
actually static. CROP computed from the source: 1206/0.5625 = 2144, standard
478 y-offset.

THE PROPOSAL PAGE BEAT IS AT 5.2s, NOT 6.0s. At 6.0 the page has drifted up far
enough that "$185 per person" sits in the top 12% that Instagram's own UI
covers. At 5.2 the whole of page 1 is in frame with the headline rate at 13%.

NO AD IN THIS RECORDING. Nine advertisers so far, so the check is for anything
new rather than a known logo; all seven beat stills were looked at whole in
build/preview.png and the exports contain nothing else.
"""
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
B = os.path.join(HERE, "build")
F = os.path.join(B, "frames")

FPS = 30
LEAD = 1.0
PUSH = 1.04          # slow Ken Burns across each still, 4% over its own length

# (still, seconds), cut to the voiceover's own sentence gaps.
BEATS = {
    "instagram": [
        ("prompt",   2.8),   # the sent prompt, proposal attached
        ("proposal", 2.6),   # page 1: "$185 per person"
        ("fees",     5.2),   # all eight fees outside the rate
        ("details",  4.0),   # the admin fee is not a gratuity
        ("real",     5.4),   # with the linen upgrade: $47,062, $261.46 a head
    ],
    "tiktok": [
        ("prompt",   3.0),
        ("proposal", 2.6),
        ("fees",     5.4),
        ("bill",     3.6),   # the bill as billed: $45,612, $253.40 a head
        ("real",     3.8),
        ("take",     3.6),   # "I would budget $46,000-$47,000"
    ],
}
TOTAL = {"instagram": 20.0, "tiktok": 22.0}
# loudnorm's two-pass stalls well short of -14 on Eryn's crest factor, so the
# gain goes on explicitly and alimiter catches the peaks with level=0 — auto
# level renormalises back to full scale and looks exactly like no limiting at
# all. Tuned against the export, not computed.
GAIN = {"instagram": 12.5, "tiktok": 12.5}


def seg(i, dur):
    """A still, pushed in 4% over its own length."""
    w, h = int(1080 * PUSH) // 2 * 2, int(1920 * PUSH) // 2 * 2
    return (f"[{i}:v]scale={w}:{h}:flags=lanczos,"
            f"crop=1080:1920:{(w - 1080) // 2}:'(ih-1920)*(t/{dur:.3f})',"
            f"fps={FPS},setsar=1[v{i}]")


def build(platform, out):
    beats = BEATS[platform]
    total = TOTAL[platform]
    vo = os.path.join(B, "vo", f"fees-{platform}-eryn.mp3")
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
        build(platform, os.path.join(HERE, f"venue-fees-{platform}.mp4"))


if __name__ == "__main__":
    main()
