"""Assemble the Fri 20 Nov coloring book giveaway Reel, both cuts.

HER FOOTAGE, FILMED THU 19: IMG_0424.MOV, 33.7s, shot landscape-flagged at
1920x1080 with rotation=-90, so it decodes as 1080x1920 and needs no crop.
It opens exactly on the payoff — both paperbacks in frame from the first
frame — which is what the Fri 20 block asks for, so the cut starts at 0.00
and the hook band sits over the first two seconds.

**IT IS NOT IN THIS REPO.** The repo is public, so her raw clips never land
here; this reads from the scratch copy pulled out of Drive `November 20`
(`13KeZV3qJI5EPl1QdT5ZMXQuNOgyAATmW`), and only the finished cuts are
committed. Set SRC to wherever the source sits.

Two beats:
  books   0.00 - 4.60 of the source at 1.0x, the slow push across both covers
  flip    5.00 - 18.10 at 1.5x, the flip-through, sped just enough that the
          pages read as turning rather than as a scroll

The pages are the piece, so the flip is not compressed harder than 1.5x: at
2x and above the drawings stop registering as drawings.

AUDIO IS ERYN AND NOTHING ELSE — no music bed under a voiceover, the same as
every other VO piece. The closing line is spoken as well as shown, so the end
card is not three silent seconds: Instagram hears "Comment the bride you'd
give it to", TikTok hears "Enter on my Instagram", and each cut's card says
what its own voice says. Both VO files measure -14.0 LUFS; the gain was swept
(+11.5 dB), not computed.
"""
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
CARDS = os.path.join(HERE, "build", "cards")
VO = os.path.join(HERE, "build", "vo")
SRC = os.environ.get("GIVEAWAY_SRC", "/tmp/claude-0/-home-user-eventplannersai/"
                     "4079a8b4-9eb7-5c73-8b20-b79d77bad268/scratchpad/src20/"
                     "IMG_0424.MOV")

W, H, FPS = 1080, 1920, 30
BOOKS = (0.00, 4.60, 1.0)        # start, length, speed
FLIP = (5.00, 13.10, 1.5)
HOOK_UNTIL = 2.0
GAP = 0.25                        # between the body and the closing line
TAIL = 0.60                       # after the closing line, on the end card

CUTS = {
    "instagram": ("end-instagram.png", "close-ig.wav"),
    "tiktok": ("end-tiktok.png", "close-tt.wav"),
}


def dur(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                          "format=duration", "-of", "csv=p=0", path],
                         capture_output=True, text=True, check=True)
    return float(out.stdout.strip())


def render(cut):
    end_png, close_wav = CUTS[cut]
    body = dur(os.path.join(VO, "giveaway-eryn.wav"))
    close = dur(os.path.join(VO, close_wav))
    footage = round(BOOKS[1] / BOOKS[2] + FLIP[1] / FLIP[2], 3)
    assert footage >= body, f"footage {footage}s is shorter than the VO {body}s"
    card = round(body - footage + GAP + close + TAIL, 3)
    total = round(footage + card, 3)
    assert 15.0 <= total <= 20.0, f"{total}s is outside the 15-20s target"

    out = os.path.join(HERE, f"giveaway-{cut}.mp4")
    fc = (
        f"[0:v]trim=start={BOOKS[0]}:duration={BOOKS[1]},setpts=PTS-STARTPTS,"
        f"scale={W}:{H},fps={FPS},setsar=1[a];"
        f"[0:v]trim=start={FLIP[0]}:duration={FLIP[1]},setpts=PTS-STARTPTS,"
        f"setpts=PTS/{FLIP[2]},scale={W}:{H},fps={FPS},setsar=1[b];"
        f"[a][b]concat=n=2:v=1:a=0[v];"
        f"[1:v]scale={W}:{H},setsar=1[hook];"
        f"[v][hook]overlay=0:0:eof_action=repeat:repeatlast=1:"
        f"enable='between(t,0,{HOOK_UNTIL})'[vh];"
        f"[2:v]scale={W}:{H},fps={FPS},setsar=1,"
        f"trim=duration={card},setpts=PTS-STARTPTS[card];"
        f"[vh][card]concat=n=2:v=1:a=0[vout];"
        f"[3:a]adelay=0|0[v1];"
        f"[4:a]adelay={int((body + GAP) * 1000)}|{int((body + GAP) * 1000)}[v2];"
        f"[v1][v2]amix=inputs=2:normalize=0,"
        f"apad,atrim=duration={total}[aout]"
    )
    subprocess.run([
        "ffmpeg", "-v", "error", "-y",
        "-i", SRC,
        "-loop", "1", "-t", f"{HOOK_UNTIL + 0.1}", "-i", os.path.join(CARDS, "hook.png"),
        "-loop", "1", "-t", f"{card}", "-i", os.path.join(CARDS, end_png),
        "-i", os.path.join(VO, "giveaway-eryn.wav"),
        "-i", os.path.join(VO, close_wav),
        "-filter_complex", fc, "-map", "[vout]", "-map", "[aout]",
        "-c:v", "libx264", "-profile:v", "high", "-crf", "19",
        "-pix_fmt", "yuv420p", "-movflags", "+faststart",
        "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
        "-t", f"{total}", out], check=True)
    print(f"{cut}: footage {footage:.2f}s + card {card:.2f}s = {total:.2f}s "
          f"-> {os.path.basename(out)}")
    return out


if __name__ == "__main__":
    for c in CUTS:
        render(c)
