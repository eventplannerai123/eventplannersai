#!/usr/bin/env python3
"""Sep 25 - dense BEO into a one-page day-of crib sheet.

Sources (screen recordings, 1206x2622, 60fps, silent):
  A = ScreenRecording_09-25-2026_7-03-16AM_1.mov  (aa7de50c)  prompt sent -> thinking -> BEO opened and scrolled
      Used here as A_noautofill.mp4: the ChatGPT AutoFill banner covered
      7.60-9.30s, so 7.50-9.40 is cut out. 16.00s -> 14.10s.
  B = ScreenRecording_09-25-2026_7-03-16AM_1.mov  (401b43d4)  the answer, scrolled

The reveal is capped at B 11.10s: a "Turning Stone" in-app ad starts
fading in at 11.30s. That cap, plus the 6-second payoff ceiling, is what
fixes the total length - see README.
"""
import subprocess, sys, os, json

HERE = os.path.dirname(os.path.abspath(__file__))
SRC  = os.environ.get("SRC", "/tmp/claude-0/-home-user-eventplannersai/4079a8b4-9eb7-5c73-8b20-b79d77bad268/scratchpad/fri")
A    = os.path.join(SRC, "A_noautofill.mp4")
B    = os.path.join(SRC, "B.mov")
OUT  = os.path.dirname(HERE)

CROP = "crop=1206:2144:0:478"          # 1206/0.5625 = 2144; 478 drops the status bar and record dot
SCALE= "scale=1080:1920:flags=lanczos,setsar=1,fps=30"

# (source, in, out, speed)  - speed >1 plays faster
CUTS = {
    "instagram": [(A, 7.30, 12.60, 2.650),   # the dense BEO, scrolling
                  (A, 0.60,  6.70, 2.0333),  # prompt sent, "Searched files", "Thinking"
                  (B, 0.55, 11.10, 1.0)],    # the one-page crib sheet
    "tiktok":    [(A, 7.30, 12.60, 2.950),
                  (A, 0.60,  6.70, 2.300),
                  (B, 0.30, 11.10, 1.0)],
}
FREEZE = {"instagram": 0.0, "tiktok": 0.40}  # clone the last frame to cover the longer TikTok VO
HOOK   = {"instagram": "cards0925/hook_ig.png", "tiktok": "cards0925/hook_tt.png"}
VO     = {"instagram": "vo/instagram.mp3", "tiktok": "vo/tiktok.mp3"}

def build_video(cuts, freeze, hook, dest):
    ins, fc, labels = [], [], []
    srcs = []
    for src, a, b, sp in cuts:
        if src not in srcs:
            srcs.append(src)
    for s in srcs:
        ins += ["-i", s]
    for i, (src, a, b, sp) in enumerate(cuts):
        si = srcs.index(src)
        fc.append(f"[{si}:v]trim={a}:{b},setpts=(PTS-STARTPTS)/{sp},{CROP},{SCALE}[s{i}]")
        labels.append(f"[s{i}]")
    fc.append("".join(labels) + f"concat=n={len(cuts)}:v=1:a=0[cat]")
    last = "[cat]"
    if freeze > 0:
        fc.append(f"{last}tpad=stop_mode=clone:stop_duration={freeze}[pad]")
        last = "[pad]"
    ins += ["-i", hook]
    # The hook PNG is a single frame. overlay must repeat it for the whole
    # 0-2s window - with repeatlast=0 it shows on frame one only and then
    # vanishes, which is silent and easy to miss.
    fc.append(f"{last}[{len(srcs)}:v]overlay=0:0:enable='between(t,0,2)':"
              "eof_action=repeat:repeatlast=1[v]")
    cmd = ["ffmpeg","-v","error"] + ins + ["-filter_complex",";".join(fc),
           "-map","[v]","-an","-c:v","libx264","-profile:v","high","-crf","19",
           "-pix_fmt","yuv420p","-r","30","-movflags","+faststart", dest, "-y"]
    subprocess.run(cmd, check=True)

def measure(vo):
    p = subprocess.run(["ffmpeg","-v","info","-i",vo,"-af",
        "loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json","-f","null","-"],
        capture_output=True, text=True)
    raw = p.stderr[p.stderr.rindex("{"):p.stderr.rindex("}")+1]
    return json.loads(raw)

def mux(video, vo, m, gain, dest):
    """Gain, then a peak limiter, rather than loudnorm's own normalisation.

    This voiceover's crest factor is high enough that loudnorm cannot reach
    -14 LUFS without breaching its true-peak ceiling: it stalls at -15.8 with
    TP pinned to -1.5. Measuring first and applying the gain explicitly, with
    alimiter catching only the peaks, hits -14 and leaves the body of the
    speech untouched. `m` is still the first-pass measurement - it is what
    the gain is computed from.
    """
    af = (f"volume={gain}dB,"
          "alimiter=level_in=1:level_out=1:limit=0.85:attack=5:release=50:asc=1:level=0,"
          "aresample=48000,apad")
    subprocess.run(["ffmpeg","-v","error","-i",video,"-i",vo,"-filter_complex",
        f"[1:a]{af}[a]","-map","0:v","-map","[a]","-c:v","copy",
        "-c:a","aac","-b:a","192k","-ar","48000","-shortest",
        "-movflags","+faststart",dest,"-y"], check=True)

if __name__ == "__main__":
    # dB gains, tuned against a measurement of the finished export
    offs = {"instagram": float(sys.argv[1]) if len(sys.argv) > 1 else 8.0,
            "tiktok":    float(sys.argv[2]) if len(sys.argv) > 2 else 8.0}
    for cut in ("tiktok", "instagram"):          # TikTok first, per the brief
        tmp = f"/tmp/beo_{cut}_v.mp4"
        build_video(CUTS[cut], FREEZE[cut], os.path.join(HERE, HOOK[cut]), tmp)
        m = measure(os.path.join(HERE, VO[cut]))
        dest = os.path.join(OUT, f"beo-{cut}.mp4")
        mux(tmp, os.path.join(HERE, VO[cut]), m, offs[cut], dest)
        print(cut, "->", dest)
