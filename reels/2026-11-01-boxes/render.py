"""Render both cuts of the Sun 1 Nov boxes Reel.

ONE SOURCE, HERS, NOT IN THIS REPO (raw media never is): the ChatGPT screen
recording she filmed Fri 30 Oct, 1206x2622, 62.3s, 60fps HEVC. She paste the
packing list prompt, ChatGPT returns a box-by-box manifest, a tracking and
sign-off table and a note to the hotel's receiving team.

THERE IS NO TWIST, AND THAT IS HER CALL. The guide's Oct 14 twist note predicted
the model would build a tidy manifest and miss the question that actually stops
boxes going missing — the earliest date the hotel accepts deliveries and whether
it charges to hold them. It did not play out that way: the answer flags the
missing tracking numbers, delivery dates and receiving contact itself, in its
own opening line, "rather than inventing details". Asked what she would still
change, she said: "Nothing". So this is a straight demo and the voiceover, the
takeaway and the caption are the brief's as written, with no "genuinely good,
except…" paragraph bolted on.

THE NINTH ADVERTISER IS IN THIS RECORDING. "For bulk conference supplies, here's
one Amazon Business option." enters at ~58.5s, immediately under a real
recommendation about labelling boxes and set in the answer's own voice and type
— only a small "Ad" marker and the logo below it say otherwise. The ad starts at
that sentence, not at the logo. Both cuts end well before it: the Instagram one
at 47.3s and the TikTok one at 56.3s of source.

THE PROMPT BEAT STARTS AT 5.8s, NOT 4.4s. She scrolls up to the top of her own
prompt and then back down, so the earlier frames are further *into* it: at 4.4s
the opening line "Here's my packing list for a two-day conference" is already
above the crop, and the cut would open mid-sentence. 5.8s is where the first
line is back in frame. Look at the opening two seconds of every source before
choosing the window — a cold open that starts mid-prompt breaks rule 2.

CROP computed from the source: 1206 wide means 1206/0.5625 = 2144 tall, and the
standard 478 y-offset applies here — unlike the expense report, nothing sits in
the top band that the cut needs. It takes the status bar and the red recording
dot off the top and leaves the ChatGPT input bar at the bottom, where the
platform's own furniture covers it.

EVERY BEAT RUNS AT 1x. She scrolled at a readable pace, so there is nothing to
compress and nothing that needs slowing. Time to payoff is 3.4s on Instagram
and 3.0s on TikTok — the manifest is on screen well inside the 6-second ceiling.

The two cuts diverge in more than the hook: Instagram ends on the note to the
receiving team, TikTok on "Three things still needed before shipping".
"""
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
B = os.path.join(HERE, "build")
REC = "/tmp/claude-0/-home-user-eventplannersai/4079a8b4-9eb7-5c73-8b20-b79d77bad268/scratchpad/boxes-src/rec.mp4"

FPS = 30
LEAD = 1.0
TOTAL = 18.0

# (source in, out, target seconds), cut to the voiceover's own sentence gaps.
BEATS = {
    "instagram": [
        (5.80, 9.20, 3.40),     # the sent prompt, from its first line down
        (21.00, 23.50, 2.50),   # "I've organized the shipment into six boxes…"
        (25.60, 30.40, 4.80),   # the box-by-box manifest table
        (33.40, 36.40, 3.00),   # tracking number and receiving sign-off
        (43.00, 47.30, 4.30),   # the note to the Harborview receiving team
    ],
    "tiktok": [
        (5.90, 8.90, 3.00),     # the sent prompt, from its first line down
        (21.20, 23.60, 2.40),
        (26.00, 31.00, 5.00),
        (33.60, 36.40, 2.80),
        (51.50, 56.30, 4.80),   # "Three things still needed before shipping"
    ],
}
# Measured: Instagram -24.3 LUFS / -1.9 TP, TikTok -24.4 / -1.7. The arithmetic
# gain would put true peak well over 0, so it goes on explicitly and alimiter
# catches the peaks with level=0 — auto level renormalises everything back to
# full scale and looks exactly like the limiter not working. Tuned against the
# export, not computed.
GAIN = {"instagram": 12.6, "tiktok": 12.2}


def seg(i, a, b, secs):
    speed = (b - a) / secs
    return (f"[{i}:v]trim=start={a}:end={b},setpts=(PTS-STARTPTS)/{speed:.6f},"
            f"crop=1206:2144:0:478,scale=1080:1920:flags=lanczos,"
            f"fps={FPS},setsar=1[v{i}]")


def build(platform, out):
    beats = BEATS[platform]
    vo = os.path.join(B, "vo", f"boxes-{platform}-eryn.mp3")
    hook = os.path.join(B, f"card-hook-{platform}.png")
    take = os.path.join(B, "card-takeaway.png")

    cmd = ["ffmpeg", "-y"]
    for _ in beats:
        cmd += ["-i", REC]
    cmd += ["-i", vo, "-i", hook, "-i", take]

    n = len(beats)
    parts = [seg(i, a, b, s) for i, (a, b, s) in enumerate(beats)]
    parts.append("".join(f"[v{i}]" for i in range(n)) + f"concat=n={n}:v=1:a=0[base]")
    parts.append(f"[{n+1}:v]format=rgba[hk]")
    parts.append(f"[{n+2}:v]format=rgba[tk]")
    # repeatlast=1, or a single-frame PNG shows on frame one and then vanishes.
    parts.append("[base][hk]overlay=0:0:eof_action=repeat:repeatlast=1"
                 ":enable='between(t,0,2)'[b1]")
    parts.append(f"[b1][tk]overlay=0:0:eof_action=repeat:repeatlast=1"
                 f":enable='between(t,{TOTAL-3:.2f},{TOTAL})'[vout]")
    parts.append(f"[{n}:a]volume={GAIN[platform]}dB,alimiter=limit=0.841:level=0,"
                 f"aresample=48000,adelay={int(LEAD*1000)}|{int(LEAD*1000)},"
                 f"apad,atrim=0:{TOTAL}[aout]")

    cmd += ["-filter_complex", ";".join(parts),
            "-map", "[vout]", "-map", "[aout]", "-t", f"{TOTAL}",
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
        build(platform, os.path.join(HERE, f"boxes-{platform}.mp4"))


if __name__ == "__main__":
    main()
