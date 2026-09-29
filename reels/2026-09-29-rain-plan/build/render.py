#!/usr/bin/env python3
"""Sep 29 - an outdoor reception rained out at 9am, rebuilt indoors.

Source: ScreenRecording_09-29-2026 3-35-07 AM_1.mp4 - 108.04s, 1206x2622,
60fps, 118.7 MB, via Google Drive.

Two things in this recording must never reach the export:

  38.65-44.50s  A "The file download failed. Please try again later." modal,
                with a grey Loading screen either side. The author asked for
                it to be cut. No segment below touches that span, and the
                exports are scanned to confirm it.
  from 104.00s  A "Fever - Private corporate events" in-app ad. Its lead-in
                line ("For private corporate event planning, here's one
                full-service option") enters at 104.25s, so nothing past
                104.00s is used. Sixth distinct advertiser in nine days.

Shape of the source:
    0-6s    prompt already sent, the three reference files attached
    6-12s   run_of_show_outdoor.pdf and the outdoor site plan
   14-18s   venue_floorplan_3800sqft.png, the empty hall
   19-27s   thinking, "Arranging functional zones"
   27-38s   the answer opens: recommended indoor layout, band stage, walls
   46-55s   the generated INDOOR RAIN PLAN diagram
   57-64s   bar placement, perimeter, entrance
   66-80s   "What stays vs. what gets cut" table
   81-99s   "The call order I'd use", then the revised production schedule
  100-104s  "One thing I would NOT assume"
"""
import subprocess, sys, os, json

HERE = os.path.dirname(os.path.abspath(__file__))
SRC  = os.environ.get("SRC", "/tmp/claude-0/-home-user-eventplannersai/4079a8b4-9eb7-5c73-8b20-b79d77bad268/scratchpad")
A    = os.path.join(SRC, "tue.mp4")
OUT  = os.path.dirname(HERE)

CROP = "crop=1206:2144:0:478"          # 1206/0.5625 = 2144; 478 drops the status bar and record dot
SCALE= "scale=1080:1920:flags=lanczos,setsar=1,fps=30"

# (source, in, out, speed)  - speed >1 plays faster
# (source, in, out, speed)  - speed >1 plays faster, <1 slower
# The reveal runs slower than real time on purpose: the Constraint Audit is
# dense text and the rule is to hold it so it is easy to read.
# (source, in, out, speed)  - speed >1 plays faster
# (source, in, out, speed)  - speed >1 plays faster
# The reveal starts at 49.00, not earlier: opening the rain-plan image throws
# a second "Loading" screen at 48.25-48.90, the same preview sequence as the
# failed download. The diagram is only rendered from 49.00.
# (source, in, out, speed)  - speed >1 plays faster
# Segment 1 is the opening the house rules ask for and this recording actually
# has: the prompt already sitting in the input box with all three files
# attached, and the send tap on camera at ~0.7s. The first build started at
# 7.00s and threw it away.
# The reveal starts at 49.00: opening the rain-plan image throws a "Loading"
# screen at 48.25-48.90, the same preview sequence as the failed download.
CUTS = {
    "instagram": [(A,  0.00,  2.30, 1.00),   # prompt in the box, send tapped
                  (A,  9.00, 11.80, 2.80),   # the 14,250 sq ft lawn plan
                  (A, 14.00, 17.00, 2.80),   # the empty 3,800 sq ft hall
                  (A, 21.00, 24.00, 2.80),   # generating, "Arranging functional zones"
                  (A, 49.00, 55.50, 1.00),   # the INDOOR RAIN PLAN diagram - payoff
                  (A, 68.00, 75.90, 1.00)],  # "What stays vs. what gets cut"
    "tiktok":    [(A,  0.00,  2.30, 1.15),
                  (A,  9.00, 11.80, 3.10),
                  (A, 14.00, 17.00, 3.10),
                  (A, 21.00, 24.00, 3.10),
                  (A, 49.00, 55.00, 1.00),
                  (A, 68.00, 75.90, 1.00)],
}
FREEZE = {"instagram": 0.0, "tiktok": 0.0}
HOOK   = {"instagram": "cards0929/hook_ig.png", "tiktok": "cards0929/hook_tt.png"}
VO     = {"instagram": "vo/instagram.mp3", "tiktok": "vo/tiktok.mp3"}

def build_video(cuts, freeze, hook, dest):
    """Render each segment to its own file, then concat.

    Doing all of it in one filtergraph decodes the 96 MB HEVC source once per
    branch and the process is OOM-killed - eight branches was enough to do it.
    Segment-at-a-time is slower but survives.
    """
    import tempfile, shutil
    work = tempfile.mkdtemp(prefix="rainplan_")
    try:
        parts = []
        for i, (src, a, b, sp) in enumerate(cuts):
            part = os.path.join(work, f"p{i:02d}.mp4")
            vf = (f"{CROP},{SCALE}")
            subprocess.run(["ffmpeg","-v","error","-ss",str(a),"-to",str(b),"-i",src,
                "-vf", f"setpts=(PTS-STARTPTS)/{sp},{vf}", "-an",
                "-c:v","libx264","-profile:v","high","-crf","17",
                "-pix_fmt","yuv420p","-r","30", part, "-y"], check=True)
            parts.append(part)
        lst = os.path.join(work, "list.txt")
        with open(lst, "w") as f:
            for p in parts:
                f.write(f"file '{p}'\n")
        cat = os.path.join(work, "cat.mp4")
        subprocess.run(["ffmpeg","-v","error","-f","concat","-safe","0","-i",lst,
                        "-c","copy", cat, "-y"], check=True)
        fc = []
        last = "[0:v]"
        if freeze > 0:
            fc.append(f"[0:v]tpad=stop_mode=clone:stop_duration={freeze}[pad]")
            last = "[pad]"
        fc.append(f"{last}[1:v]overlay=0:0:enable='between(t,0,2)':"
                  "eof_action=repeat:repeatlast=1[v]")
        subprocess.run(["ffmpeg","-v","error","-i",cat,"-i",hook,
            "-filter_complex",";".join(fc),"-map","[v]","-an",
            "-c:v","libx264","-profile:v","high","-crf","19",
            "-pix_fmt","yuv420p","-r","30","-movflags","+faststart",
            dest,"-y"], check=True)
    finally:
        shutil.rmtree(work, ignore_errors=True)

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
        dest = os.path.join(OUT, f"rainplan-{cut}.mp4")
        mux(tmp, os.path.join(HERE, VO[cut]), m, offs[cut], dest)
        print(cut, "->", dest)
