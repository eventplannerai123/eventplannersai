"""Render both cuts of the Fri 30 Oct coloring book Reel.

Length 27.2s, inside the brief's 30-40s band at the short end, because that is
what the voiceover supports: Eryn reads the guide's 72-word script in 23.07s
(3.1 w/s, exactly the planning figure). Padding to 35s would mean ten seconds
of silence, and the rule is to prefer the lower end when the voiceover is short.

THE BEATS ARE CUT TO THE SENTENCES, not to a grid. `silencedetect` at -32dB put
the gaps at 5.13, 7.87, 10.85, 14.31, 16.52, 19.29, 19.95, 21.44 and 22.86, and
every beat change lands inside one of them once the 1.2s lead-in is added. So
the dress appears on "the bride", the bouquet on "the bridesmaid", the planner's
kit on "the planner who's been staring at a seating chart", and "paperback on
Amazon" lands on the closing frame.

The two cuts differ in more than the hook: Instagram ends on the title page,
TikTok comes back to her photo of the real book. Never the same file twice.
"""
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
B = os.path.join(HERE, "build", "beats")
VO = os.path.join(HERE, "build", "vo", "book-eryn-take1.mp3")

FPS = 30
LEAD = 1.2                      # before the voiceover starts
TOTAL = 27.2

# (beat file, seconds, zoom direction). 1 = push in, -1 = pull out.
COMMON = [
    ("01-photo.jpg", 6.60, 1),
    ("dress.jpg", 2.70, 1),
    ("bouquet.jpg", 3.15, 1),
    ("kit.jpg", 3.60, 1),
    ("guestbook.jpg", 2.25, 1),
    ("ring.jpg", 2.40, 1),
    ("aisle.jpg", 2.30, 1),
]
ENDING = {"instagram": ("title.jpg", 4.20, 1), "tiktok": ("01-photo.jpg", 4.20, -1)}


def zoompan(idx, secs, direction):
    """A slow push over `secs`. Source is doubled first so the resample stays sharp."""
    frames = round(secs * FPS)
    span = 0.055
    if direction > 0:
        z = f"1+{span}*on/{frames}"
    else:
        z = f"{1 + span}-{span}*on/{frames}"
    return (f"[{idx}:v]scale=2160:3840:flags=lanczos,"
            f"zoompan=z='{z}':d={frames}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'"
            f":s=1080x1920:fps={FPS},trim=end_frame={frames},setsar=1[v{idx}]")


def build(platform, out):
    beats = COMMON + [ENDING[platform]]
    hook = os.path.join(B, f"card-hook-{platform}.png")
    take = os.path.join(B, "card-takeaway.png")

    cmd = ["ffmpeg", "-y"]
    for f, secs, _ in beats:
        # A SINGLE frame per input, not -loop 1 -t. zoompan's d is frames per
        # INPUT frame, so a looped input makes it run forever and concat never
        # reaches beat two — the first build was 27 seconds of the photo alone.
        cmd += ["-i", os.path.join(B, f)]
    cmd += ["-i", VO, "-i", hook, "-i", take]

    n = len(beats)
    parts = [zoompan(i, secs, d) for i, (f, secs, d) in enumerate(beats)]
    parts.append("".join(f"[v{i}]" for i in range(n)) + f"concat=n={n}:v=1:a=0[base]")
    # Overlays. repeatlast=1 or a single-frame PNG shows on frame one and vanishes.
    parts.append(f"[{n+1}:v]format=rgba[hk]")
    parts.append(f"[{n+2}:v]format=rgba[tk]")
    parts.append("[base][hk]overlay=0:0:eof_action=repeat:repeatlast=1"
                 ":enable='between(t,0,2)'[b1]")
    parts.append(f"[b1][tk]overlay=0:0:eof_action=repeat:repeatlast=1"
                 f":enable='between(t,{TOTAL-3:.2f},{TOTAL})'[vout]")
    # Voiceover. The first-pass measurement reads I=-23.53, TP=-1.53, so the
    # +9.53 dB that would nominally reach -14 LUFS puts true peak at +8 dB.
    # loudnorm cannot get there on its own — its true-peak ceiling binds first
    # and it stalls at -16.41 — so the gain is applied explicitly and alimiter
    # catches the peaks. alimiter needs level=0 or auto-level renormalises the
    # output back to full scale and the limiting looks like it did nothing.
    #
    # The gain is 11.2 dB rather than the arithmetic 9.53, because limiting eats
    # loudness: measured back, 9.53 lands at -15.82 LUFS, 11.2 at -14.90 and
    # 12.0 at -14.51. 12.0 was rejected — it squashes LRA from the source's 3.40
    # to 1.90, which is audibly flat for the sake of 0.4 dB.
    parts.append(f"[{n}:a]volume=11.2dB,alimiter=limit=0.841:level=0,"
                 f"aresample=48000,"
                 f"adelay={int(LEAD*1000)}|{int(LEAD*1000)},"
                 f"apad,atrim=0:{TOTAL}[aout]")

    cmd += ["-filter_complex", ";".join(parts),
            "-map", "[vout]", "-map", "[aout]",
            "-t", f"{TOTAL}",
            "-c:v", "libx264", "-profile:v", "high", "-crf", "19",
            "-pix_fmt", "yuv420p", "-r", str(FPS), "-movflags", "+faststart",
            "-c:a", "aac", "-b:a", "192k", "-ar", "48000", out]
    subprocess.run(cmd, check=True, capture_output=True)
    print(out, "ok")


def main():
    for platform in ("tiktok", "instagram"):     # TikTok first, per the briefs
        build(platform, os.path.join(HERE, f"coloring-book-{platform}.mp4"))


if __name__ == "__main__":
    main()
