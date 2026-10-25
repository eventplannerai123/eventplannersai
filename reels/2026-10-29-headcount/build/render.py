"""Thu 29 Oct — headcount Reel. Two cuts, TikTok first. First piece in Eryn's voice.

SOURCE SPAN IS 2.00-5.00, NOT THE WHOLE CLIP. IMG_1005 is a 5s pan along a
drinks table and the first two seconds carry a letterboard reading the event's
name. A named sign is barred the same way a client's name is (CLAUDE.md, the
Oct 19 branding rule), so the cut starts after it leaves frame at about 2.0s.
That leaves 3.0s of clean footage instead of 5.0s, which is why the slowdown
below is heavier than the brief's "about 60%".

The optional Oct 7 conference b-roll is NOT used: it is not in Drive anywhere
this session can find, and the Wed 21 brief calls it "a bonus, not something
Friday depends on".

Pacing differs per cut on purpose, which is the two-cuts rule rather than an
accident: Instagram runs the pan at 0.50x, TikTok at 0.40x.

Loudness: explicit gain + alimiter(level=0), never loudnorm's two-pass, which
stalls short of -14 LUFS on this kind of material. Measured and corrected below.
"""
import json, os, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
REEL = os.path.dirname(HERE)
SRC = "/tmp/claude-0/-home-user-eventplannersai/4079a8b4-9eb7-5c73-8b20-b79d77bad268/scratchpad/headcount/IMG_1005.MOV"

W, H, FPS = 1080, 1920, 30
CLEAN_IN, CLEAN_LEN = 2.00, 3.00        # the span with no letterboard in frame
TARGET_LUFS = -14.0

CUTS = {
    "tiktok":    dict(rate=0.40, total=9.30, card="hook-tiktok.png",
                      vo="vo/headcount-tiktok-eryn.mp3"),
    "instagram": dict(rate=0.50, total=8.20, card="hook-instagram.png",
                      vo="vo/headcount-instagram-eryn.mp3"),
}


def run(cmd):
    p = subprocess.run(cmd, capture_output=True, text=True)
    if p.returncode:
        raise SystemExit(f"FAILED: {' '.join(cmd[:6])}...\n{p.stderr[-3000:]}")
    return p.stderr


def measure_i(path):
    err = run(["ffmpeg", "-v", "info", "-i", path, "-af",
               "loudnorm=I=-14:TP=-1.0:LRA=11:print_format=json", "-f", "null", "-"])
    blob = err[err.rindex("{"):err.rindex("}") + 1]
    return float(json.loads(blob)["input_i"])


def build(name, cfg):
    card = os.path.join(HERE, "cards", cfg["card"])
    vo = os.path.join(HERE, cfg["vo"])
    out = os.path.join(REEL, f"headcount-{name}.mp4")

    motion = CLEAN_LEN / cfg["rate"]
    freeze = cfg["total"] - motion
    assert freeze > 0, f"{name}: motion {motion:.2f}s already exceeds {cfg['total']}s"

    gain = TARGET_LUFS - measure_i(vo)
    print(f"{name}: motion {motion:.2f}s + freeze {freeze:.2f}s = {cfg['total']}s, "
          f"first-pass VO gain {gain:+.2f} dB")

    vf = (f"[0:v]setpts=PTS/{cfg['rate']},fps={FPS},scale={W}:{H}:force_original_aspect_ratio=increase,"
          f"crop={W}:{H},tpad=stop_mode=clone:stop_duration={freeze:.3f},setsar=1[v];"
          f"[1:v]format=rgba[c];"
          f"[v][c]overlay=0:0:eof_action=repeat:repeatlast=1[vo]")
    af = ("[2:a]volume=GAINdB,alimiter=limit=-1.0dB:level=0,"
          f"aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=stereo,"
          f"apad[ao]")

    # The limiter eats part of the gain, so one measured correction pass follows.
    # A single open-loop gain landed -15.6 and -15.9 LUFS on the first build.
    for attempt in range(3):
        encode(out, card, vo, vf.replace("GAIN", f"{gain:.2f}"),
               af.replace("GAIN", f"{gain:.2f}"), cfg["total"])
        got = measure_i(out)
        print(f"  pass {attempt+1}: gain {gain:+.2f} dB -> {got:.2f} LUFS")
        if abs(got - TARGET_LUFS) <= 0.2:
            break
        gain += TARGET_LUFS - got
    print(f"  -> {out}  final {got:.2f} LUFS")
    return out


def encode(out, card, vo, vf, af, total):
    run(["ffmpeg", "-y",
         "-ss", str(CLEAN_IN), "-t", str(CLEAN_LEN), "-i", SRC,
         "-loop", "1", "-i", card,
         "-i", vo,
         "-filter_complex", vf + ";" + af,
         "-map", "[vo]", "-map", "[ao]",
         "-t", str(total),
         "-c:v", "libx264", "-profile:v", "high", "-crf", "19", "-pix_fmt", "yuv420p",
         "-movflags", "+faststart",
         "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
         out])


if __name__ == "__main__":
    for n, c in CUTS.items():
        build(n, c)
