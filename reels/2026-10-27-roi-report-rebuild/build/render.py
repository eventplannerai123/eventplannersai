"""Rebuild 1 — Sep 1 post-event ROI report. New first beat only.

HER MASTER IS 1206x2144 AT 60FPS, not 1080x1920. That is the native crop of
the screen recording, one step before the export that went out, so it is a
better source than the posted file rather than a worse one: 1080x1920 comes
out of it by a clean downscale. Instagram's own copy of the live post is
720x1280 and was rejected for exactly the opposite reason.

SPLICE AT 3.03s, inside the master's own silence. `silencedetect` puts the
first gap at 2.864-3.204, so 3.03 replaces the opening sentence whole rather
than slicing it mid-word. Everything after it is the original edit.

THE OPENING FRAME IS THE FINISHED REPORT, per the rebuild rules: open on the
result, not on the typing. t=10.00s is the cost-breakdown table with the
$85,000 total and the $567 cost per attendee on screen — the densest "this is
a real report" frame in the piece.

IT IS A FROZEN FRAME, AND IT HAS TO BE. The first build fed `-ss 10 -i SRC`
straight into tpad, which is not a freeze at all — it plays the master from
10.00s onward, and the body replays that same stretch a few seconds later. The
viewer would have watched the same scroll twice. So the frame is extracted to
a PNG first and looped.

LOUDNESS IS MATCHED TO THE MASTER, NOT TO -14 LUFS. The master runs -21.45
and the body has to stay as it was, or the experiment's control is gone. So
the new opening line is brought to the master's level instead, which is what
the Oct 15 rebuild did.

Two cuts are rendered because the voice change lands mid-rebuild: `-eryn` is
her standing instruction, `-vanessa` matches the body's existing voice. Hers
to pick.
"""
import json, os, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
REEL = os.path.dirname(HERE)
SRC = os.path.join(REEL, "source", "roi_report_INSTAGRAM.mp4")
CARD = os.path.join(HERE, "cards", "hook.png")

W, H, FPS = 1080, 1920, 30
SPLICE = 3.03          # inside the master's 2.864-3.204 silence
OPEN_FRAME = 10.00     # the finished report
PAD = 0.30             # breath after the hook line before the cut
MASTER_LUFS = -21.45   # measured on the master; the body keeps it

VOICES = {"eryn": "vo/open-eryn.mp3", "vanessa": "vo/open-vanessa.mp3"}


def run(cmd):
    p = subprocess.run(cmd, capture_output=True, text=True)
    if p.returncode:
        raise SystemExit(f"FAILED: {' '.join(cmd[:8])}...\n{p.stderr[-3000:]}")
    return p.stderr


def measure_i(path):
    err = run(["ffmpeg", "-v", "info", "-i", path, "-af",
               "loudnorm=I=-14:TP=-1.0:LRA=11:print_format=json", "-f", "null", "-"])
    blob = err[err.rindex("{"):err.rindex("}") + 1]
    return float(json.loads(blob)["input_i"])


def dur(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                          "-of", "csv=p=0", path], capture_output=True, text=True).stdout
    return float(out.strip())


def opening_still():
    """One frame, extracted rather than played. See the note at the top."""
    out = os.path.join(HERE, "frames", "open.png")
    if not os.path.exists(out):
        run(["ffmpeg", "-y", "-v", "error", "-ss", str(OPEN_FRAME), "-i", SRC,
             "-frames:v", "1", out])
    return out


def build(name, vo_rel):
    vo = os.path.join(HERE, vo_rel)
    open_len = dur(vo) + PAD
    gain = MASTER_LUFS - measure_i(vo)
    still = opening_still()
    out = os.path.join(REEL, f"roi-report-rebuild-{name}.mp4")
    print(f"{name}: opening {open_len:.2f}s, VO gain {gain:+.2f} dB to match the master")

    vf = (
        # A — frozen report frame, card held over the whole beat
        f"[0:v]scale={W}:{H},setsar=1,fps={FPS},trim=duration={open_len:.3f},setpts=PTS-STARTPTS[a0];"
        f"[2:v]format=rgba[c];[a0][c]overlay=0:0:eof_action=repeat:repeatlast=1[a];"
        # B — the master from the splice, untouched but for scale and fps
        f"[1:v]scale={W}:{H},setsar=1,fps={FPS}[b];"
        f"[a][b]concat=n=2:v=1:a=0[v]"
    )
    af = (
        f"[3:a]volume={gain:.2f}dB,aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=stereo,"
        f"apad=whole_dur={open_len:.3f},atrim=duration={open_len:.3f}[aa];"
        f"[1:a]aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=stereo[ba];"
        f"[aa][ba]concat=n=2:v=0:a=1[ao]"
    )

    run(["ffmpeg", "-y",
         "-loop", "1", "-t", f"{open_len:.3f}", "-i", still,   # 0: opening still
         "-ss", str(SPLICE), "-i", SRC,              # 1: the body
         "-loop", "1", "-i", CARD,                   # 2: hook card
         "-i", vo,                                   # 3: new opening line
         "-filter_complex", vf + ";" + af,
         "-map", "[v]", "-map", "[ao]",
         "-c:v", "libx264", "-profile:v", "high", "-crf", "19", "-pix_fmt", "yuv420p",
         "-movflags", "+faststart",
         "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
         out])
    print(f"  -> {out}  {dur(out):.2f}s, {measure_i(out):.2f} LUFS")


if __name__ == "__main__":
    print(f"master: {dur(SRC):.2f}s, {measure_i(SRC):.2f} LUFS")
    for n, v in VOICES.items():
        build(n, v)
