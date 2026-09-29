#!/usr/bin/env python3
"""Sep 30 - fifty free-text feedback responses into a one-page debrief.

Source: ScreenRecording_09-29-2026 4-50-23 AM_1.mp4 - 36.47s, 1206x2622,
60fps, 53.8 MB, via Google Drive.

**This day deliberately misses the length test.** The guide asks for 40-50s
and the footage cannot give it. Usable reveal is 13.10-34.20s - 21.1s - and
about 10s of prompt, CSV and generating has to be compressed to hold the
6-second payoff ceiling. Reaching 40s would need the reveal at roughly 0.60x,
which on a scrolling page of text is visible slow motion. The author was
shown the arithmetic and chose to ship short. Sep 30 is the last day of the
length test, so this costs a data point; that was her call, not a drift.

No in-app ad anywhere in this recording - it ends on the Sources row with
clean white space. Verified on the source and again on both exports.

Shape of the source:
    0-3.4s   prompt in the box, send tap, the model starts responding
    4-11s    the 50 free-text responses, scrolling  (the messy input)
   11.5-13s  back to chat, "Worked for 10s"
   13-20s    theme breakdown table - 6 themes, counts adding to 50
   20-22s    the quote that best captures each theme
   22-34s    the three concrete changes, then the bottom line
   34-36.5s  blank scroll past the end of the answer - unusable
"""
import subprocess, sys, os, json

HERE = os.path.dirname(os.path.abspath(__file__))
SRC  = os.environ.get("SRC", "/tmp/claude-0/-home-user-eventplannersai/4079a8b4-9eb7-5c73-8b20-b79d77bad268/scratchpad")
A    = os.path.join(SRC, "wed.mp4")
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
# (source, in, out, speed)  - speed >1 plays faster
# Pacing note. The 6-second payoff ceiling will not accommodate four setup
# beats at a speed anyone can read: prompt, lawn plan, empty hall and a
# generating beat came to ~1s each and the author said it "flips to the rain
# plan floorplan way too fast". The empty hall was dropped rather than
# squeezing all four - the rain plan's own header reads "Main hall - 76 x 50
# ft - 3,800 sq ft", so the indoor size still lands. That buys the lawn plan
# a real 2s look at normal speed and the generating beat 2.2s, up from 1.07s,
# which was under the 2.5s the timing rules ask for.
#
# The reveal starts at 49.00: opening the rain-plan image throws a "Loading"
# screen at 48.25-48.90, the same preview sequence as the failed download.
# (source, in, out, speed)  - speed >1 plays faster, <1 slower
# Three setup beats, none under 2s. Segment 1 runs at normal speed and
# carries the prompt, the send tap and the model starting to respond, so the
# working beat is inside it rather than a separate one-second flash - the
# fault the author called out on Sep 29.
# The reveal runs below 1.0x because the debrief is dense and the rule is to
# hold it so it can be read.
# (source, in, out, speed)  - speed >1 plays faster, <1 slower
# Three setup beats, none under 2s. Segment 1 runs at normal speed and
# carries the prompt, the send tap and the model starting to respond, so the
# working beat is inside it rather than a separate one-second flash - the
# fault the author called out on Sep 29.
#
# The reveal starts at source 13.40, not 13.10. At 13.10 the frame is still
# mostly the prompt bubble with the answer only beginning underneath, and the
# theme table did not become readable until about 6.0s in the export - at the
# payoff ceiling rather than safely under it. 13.40 enters on "Worked for 10s"
# with the answer and the Theme breakdown heading already on screen.
#
# The reveal runs below 1.0x because the debrief is dense and the rule is to
# hold it so it can be read.
CUTS = {
    "instagram": [(A,  0.00,  3.15, 1.000),   # prompt in the box, send, response starts
                  (A,  4.20, 11.00, 3.400),   # the 50 free-text responses, scrolling
                  (A, 13.40, 34.20, 0.800)],  # themes, counts, quotes, three changes
    "tiktok":    [(A,  0.00,  3.15, 1.150),
                  (A,  4.20, 11.00, 3.700),
                  (A, 13.40, 34.20, 0.855)],
}
FREEZE = {"instagram": 0.0, "tiktok": 0.0}
HOOK   = {"instagram": "cards0930/hook_ig.png", "tiktok": "cards0930/hook_tt.png"}
VO     = {"instagram": "vo/instagram.mp3", "tiktok": "vo/tiktok.mp3"}

def build_video(cuts, freeze, hook, dest):
    """Render each segment to its own file, then concat.

    Doing all of it in one filtergraph decodes the 96 MB HEVC source once per
    branch and the process is OOM-killed - eight branches was enough to do it.
    Segment-at-a-time is slower but survives.
    """
    import tempfile, shutil
    work = tempfile.mkdtemp(prefix="debrief_")
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
        dest = os.path.join(OUT, f"debrief-{cut}.mp4")
        mux(tmp, os.path.join(HERE, VO[cut]), m, offs[cut], dest)
        print(cut, "->", dest)
