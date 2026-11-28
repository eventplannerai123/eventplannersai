"""Assemble the Mon 30 Nov Vendor Payment System Black Friday Reel.

Payoff first: the coloured tracker with "$17 until midnight." over it from
frame one, then the paste, the three flag colours, the price card, the CTA.
Cut points come from the voiceover's own pauses (silencedetect), per platform.

Source: Nov 17 laptop capture r4 = `Recording 2026-11-17 093505.mp4`
(1918x944), the same crops the Thu 19 piece uses, so the whole sheet shows and
the Reminder log tab never does (no beat runs past 37.41s; she opens it at 40s).
"""
import os, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.environ.get("TRACKER_SRC", "")
CARDS = os.path.join(HERE, "build", "cards")
VO = os.path.join(HERE, "build", "vo")
WORK = os.path.join(HERE, "build", "beats")
W, H, FPS = 1080, 1920, 30
PANEL_W, PANEL_H, PANEL_Y = 1080, 980, 450
GAIN_DB = {"instagram": 12.5, "tiktok": 12.5}

# (name, src_start, dur, crop_w, crop_h, crop_x, crop_y, card) per platform
def beats(p):
    d = {"instagram": (3.20, 5.00, 3.00), "tiktok": (3.30, 5.20, 3.00)}[p]
    return [
        ("b0-payoff", 26.60, d[0], 694, 630, 970, 265, "hook"),
        ("b1-paste",  31.00, d[1], 694, 630, 240, 265, "b1"),
        ("b2-colour", 23.20, d[2], 694, 630, 970, 265, "b2"),
    ]
PRICE_DUR = {"instagram": 4.15, "tiktok": 3.94}
END_DUR = {"instagram": 2.05, "tiktok": 1.96}
URL_DUR = 2.00


def beat(p, name, start, dur, cw, ch, cx, cy, card):
    inp = os.path.join(SRC, "r4.mp4")
    assert os.path.exists(inp), inp
    out = os.path.join(WORK, f"{p}-{name}.mp4")
    vf = (f"[0:v]trim=start={start}:duration={dur},setpts=PTS-STARTPTS,"
          f"crop={cw}:{ch}:{cx}:{cy},scale={PANEL_W}:{PANEL_H}:flags=lanczos,fps={FPS}[p];"
          f"color=c=0xCECBF6:s={W}x{H}:d={dur}:r={FPS}[bg];"
          f"[bg][p]overlay=0:{PANEL_Y}:shortest=1[v0];[v0][1:v]overlay=0:0[v]")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", inp, "-loop", "1", "-i",
                    os.path.join(CARDS, f"{card}.png"), "-filter_complex", vf, "-map", "[v]",
                    "-an", "-c:v", "libx264", "-profile:v", "high", "-crf", "17",
                    "-pix_fmt", "yuv420p", "-t", f"{dur:.3f}", out], check=True)
    return out


def still(p, card, dur):
    out = os.path.join(WORK, f"{p}-{card}.mp4")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-loop", "1", "-t", f"{dur:.3f}", "-i",
                    os.path.join(CARDS, f"{card}.png"), "-vf",
                    f"scale={W}:{H},fps={FPS},setsar=1,format=yuv420p",
                    "-c:v", "libx264", "-profile:v", "high", "-crf", "17", out], check=True)
    return out


def render(p):
    os.makedirs(WORK, exist_ok=True)
    parts = [beat(p, *b) for b in beats(p)]
    parts.append(still(p, "price", PRICE_DUR[p]))
    parts.append(still(p, f"end-{p}", END_DUR[p]))
    total = sum(b[2] for b in beats(p)) + PRICE_DUR[p] + END_DUR[p]
    if p == "tiktok":
        parts.append(still(p, "url-tiktok", URL_DUR))
        total += URL_DUR
    lst = os.path.join(WORK, f"concat-{p}.txt")
    open(lst, "w").write("".join(f"file '{x}'\n" for x in parts))
    vo = os.path.join(VO, f"tracker-{p}-eryn.mp3")
    out = os.path.join(HERE, f"tracker-blackfriday-{p}.mp4")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst,
                    "-i", vo, "-filter_complex",
                    f"[1:a]volume={GAIN_DB[p]}dB,alimiter=limit=0.841:level=0,apad=whole_dur={total}[a]",
                    "-map", "0:v", "-map", "[a]", "-c:v", "libx264", "-profile:v", "high",
                    "-crf", "19", "-pix_fmt", "yuv420p", "-movflags", "+faststart",
                    "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-t", f"{total:.3f}", out],
                   check=True)
    print(f"{p}: {total:.2f}s -> {os.path.basename(out)}")


if __name__ == "__main__":
    assert SRC, "set TRACKER_SRC to the folder holding r4.mp4"
    for p in ("instagram", "tiktok"):
        render(p)
