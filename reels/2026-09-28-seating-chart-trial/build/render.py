#!/usr/bin/env python3
"""Sep 28 - a guest list with family notes into a seating chart that survives it.

PLANNED INSTAGRAM TRIAL REEL. This script builds the two cuts and nothing
else: the Trial toggle is in-app only, so the author uploads the Instagram
file herself. Nothing here posts, and nothing should be added that does.

Source: ScreenRecording_09-27-2026 7-42-41 PM_1.mp4 - 86.38s, 1206x2622,
60fps, 96.8 MB, delivered via Google Drive because it is far past the
~30 MB chat ceiling.

Shape of the source:
  6-15s   the guest list spreadsheet, scrolling        (the messy input)
  15-18s  prompt bubble, first line of the response
  18-25s  thinking
  25-34s  the four mathematically incompatible notes, readable  (the payoff)
  34-60s  a long, visually static optimise phase - only the status line moves
  60-68s  "the feasible core is now solved", then generating the audit
  69-77s  "Worked for 1m 7s", waiting
  77-86s  the Constraint Audit, scrolling

No in-app ad anywhere in this clip - the composer bar covers the bottom
throughout. Verified on the source and again on both exports.
"""
import subprocess, sys, os, json

HERE = os.path.dirname(os.path.abspath(__file__))
SRC  = os.environ.get("SRC", "/tmp/claude-0/-home-user-eventplannersai/4079a8b4-9eb7-5c73-8b20-b79d77bad268/scratchpad")
A    = os.path.join(SRC, "mon.mp4")   # one continuous recording, no splits
OUT  = os.path.dirname(HERE)

CROP = "crop=1206:2144:0:478"          # 1206/0.5625 = 2144; 478 drops the status bar and record dot
SCALE= "scale=1080:1920:flags=lanczos,setsar=1,fps=30"

# (source, in, out, speed)  - speed >1 plays faster
# (source, in, out, speed)  - speed >1 plays faster, <1 slower
# The reveal runs slower than real time on purpose: the Constraint Audit is
# dense text and the rule is to hold it so it is easy to read.
CUTS = {
    "instagram": [(A,  6.00, 14.00, 4.60),   # the spreadsheet
                  (A, 15.00, 18.00, 2.40),   # prompt sent, response starts
                  (A, 18.00, 25.00, 2.80),   # generating beat, 2.50s on screen
                  (A, 25.00, 34.00, 1.00),   # the four incompatible notes - payoff
                  (A, 36.00, 49.00, 2.90),   # representative slice of the static optimise phase
                  (A, 60.00, 68.50, 1.00),   # "the feasible core is now solved"
                  (A, 69.00, 77.00, 3.20),   # the wait, then "Done"
                  (A, 77.50, 86.38, 0.85)],  # the Constraint Audit
    "tiktok":    [(A,  6.00, 14.00, 4.90),
                  (A, 15.00, 18.00, 2.60),
                  (A, 18.00, 25.00, 3.00),
                  (A, 25.00, 34.00, 1.00),
                  (A, 36.00, 49.00, 3.10),
                  (A, 60.00, 68.50, 1.00),
                  (A, 69.00, 77.00, 3.40),
                  (A, 77.50, 86.38, 0.82)],
}
FREEZE = {"instagram": 0.0, "tiktok": 0.0}
HOOK   = {"instagram": "cards0928/hook_ig.png", "tiktok": "cards0928/hook_tt.png"}
VO     = {"instagram": "vo/instagram.mp3", "tiktok": "vo/tiktok.mp3"}

def build_video(cuts, freeze, hook, dest):
    """Render each segment to its own file, then concat.

    Doing all of it in one filtergraph decodes the 96 MB HEVC source once per
    branch and the process is OOM-killed - eight branches was enough to do it.
    Segment-at-a-time is slower but survives.
    """
    import tempfile, shutil
    work = tempfile.mkdtemp(prefix="seating_")
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
        dest = os.path.join(OUT, f"seating-{cut}.mp4")
        mux(tmp, os.path.join(HERE, VO[cut]), m, offs[cut], dest)
        print(cut, "->", dest)
