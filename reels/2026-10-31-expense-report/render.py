"""Render both cuts of the Sat 31 expense report Reel.

TWO SOURCES, BOTH HERS, NEITHER IN THIS REPO (raw media never is):
  * the ChatGPT screen recording, 1206x2622, 53.5s
  * a 13.4s clip of the finished sheet open on her phone, filmed on request
    because the recording ends on a download link and never shows the report

WHAT SHE RECORDED IS NOT WHAT THE BRIEF DESCRIBES, and the brief's version is
the weaker one. It specs pasting twelve Chicago receipts into the chat. She
pointed ChatGPT at her Gmail instead, uploaded photos of three paper receipts
and a card-statement screenshot, attached her own expense template and asked for
it back as a filled Excel file. So the voiceover, the takeaway overlay and the
caption are written around the Denver run, which the guide's twist note
explicitly asks for: "CC rewrites the last voiceover line, the takeaway overlay
and the caption's second paragraph around what she actually caught".

The brief's "What it should catch" numbers are the Chicago ones and do not apply
here: no receipt is undated, and the catch is a duplicate $186.40 dinner plus
one $22.64 charge with a card statement and no itemised receipt.

CROP, computed from the source rather than pasted. 1206 wide means height
1206/0.5625 = 2144. The y-offset is 440, not CLAUDE.md's usual 478: 478 clips
the top ~6px off the attachment thumbnails, and those thumbnails are the whole
point of the opening frame — they are what tells you she uploaded a template and
photographed receipts. 440 still takes the status bar and the red recording dot
off the top, and leaves the ChatGPT input bar at the bottom where the platform's
own furniture covers it.

HER SHEET CLIP IS SHOWN FULL WIDTH, which is her correction and she was right.
The first build cropped to the right-hand columns to make the type bigger, and
that cut the leftmost column down the middle and ran the beat on to 10.8s, where
her scroll has gone past the table and the frame is half empty. Her words: "It's
missing the very first column, and then when it trails off to the last column,
it looks messy. Keep it just visible between the lines."

So the crop is the full 1206 and the window is 1.6s to 9.6s at her own speed —
it starts on a clean Date column and stops before the scroll runs out of table.
The strip is smaller as a result. That is the trade and she made it: a complete
table, whole columns, nothing sliced.

Measured, the table is a 419px band in a 2622px-tall frame — 2.9:1 — so filling
a 0.5625 frame from it was never possible. It sits on the brand lavender,
between two hairlines, which also matches the coloring book Reel from the day
before.

HER CLIP ENDS ON HER OWN NAME. At about 12s she exits the preview into the Files
app and "Sahiba Anand Paint...ume" is plainly legible in the recents list. The
beat stops at 10.8s. Check the tail of every clip she films, not just the part
she filmed on purpose.

AND THE SUMMARY BLOCK IS DELIBERATELY OUT OF FRAME. The phone's file preview
does not evaluate formulas, so every category subtotal and the TOTAL read $0.00
on screen. The band stops above it, and nothing in the script claims a total —
a Reel about getting an expense report right cannot show a $0.00 total.
"""
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
B = os.path.join(HERE, "build")
SRC = "/tmp"
REC = os.path.join(SRC, "rec.mp4")
SHEET = os.path.join(SRC, "sheet.mp4")
VO = os.path.join(B, "vo", "expense-eryn-take1.mp3")

FPS = 30
LEAD = 1.0
TOTAL = 25.5
LAVENDER = "0xCECBF6"

# (source, in, out, target seconds). The chat beats are cut to the voiceover's
# own sentence gaps; see the README for the mapping.
BEATS = [
    (REC, 0.30, 4.30, 4.00),      # the prompt, with its three attachments
    (REC, 17.00, 23.50, 6.50),    # it names the three paper receipts and the card statement
    (REC, 45.50, 53.40, 7.00),    # scrolls the table, lands on 11 rows and the duplicate
    (SHEET, 1.60, 9.60, 8.00),    # her filled sheet, at her own speed: Date through Notes
]


def seg(i, src, a, b, secs):
    """Trim, crop, and fit the beat to its slot. Chat beats crop; the sheet beat
    is a band on lavender, because a spreadsheet row is not 9:16."""
    speed = (b - a) / secs
    if src == REC:
        v = (f"[{i}:v]trim=start={a}:end={b},setpts=(PTS-STARTPTS)/{speed:.6f},"
             f"crop=1206:2144:0:440,scale=1080:1920:flags=lanczos,fps={FPS},setsar=1[v{i}]")
    else:
        v = (f"[{i}:v]trim=start={a}:end={b},setpts=(PTS-STARTPTS)/{speed:.6f},"
             f"crop=1206:430:0:588,scale=1080:385:flags=lanczos,fps={FPS},setsar=1[s{i}];"
             f"color=c={LAVENDER}:s=1080x1920:d={secs}:r={FPS}[bg{i}];"
             f"[bg{i}][s{i}]overlay=0:760:shortest=1,"
             f"drawbox=x=0:y=759:w=1080:h=2:color=0xB0ACE4:t=fill,"
             f"drawbox=x=0:y=1145:w=1080:h=2:color=0xB0ACE4:t=fill,setsar=1[v{i}]")
    return v


def build(platform, out):
    hook = os.path.join(B, f"card-hook-{platform}.png")
    take = os.path.join(B, "card-takeaway.png")
    cmd = ["ffmpeg", "-y"]
    for src, a, b, secs in BEATS:
        cmd += ["-i", src]
    cmd += ["-i", VO, "-i", hook, "-i", take]

    n = len(BEATS)
    parts = [seg(i, src, a, b, secs) for i, (src, a, b, secs) in enumerate(BEATS)]
    parts.append("".join(f"[v{i}]" for i in range(n)) + f"concat=n={n}:v=1:a=0[base]")
    parts.append(f"[{n+1}:v]format=rgba[hk]")
    parts.append(f"[{n+2}:v]format=rgba[tk]")
    # repeatlast=1 or a single-frame PNG shows on frame one and then vanishes.
    parts.append("[base][hk]overlay=0:0:eof_action=repeat:repeatlast=1"
                 ":enable='between(t,0,2)'[b1]")
    parts.append(f"[b1][tk]overlay=0:0:eof_action=repeat:repeatlast=1"
                 f":enable='between(t,{TOTAL-3:.2f},{TOTAL})'[vout]")
    # Measured I=-25.14, TP=-5.13. The arithmetic +11.14 dB would put true peak
    # at +6, so the gain goes on explicitly and alimiter catches the peaks, with
    # level=0 or auto-level renormalises it all back to full scale. The figure
    # is tuned against a measurement, not computed: 12.0 dB lands at -15.06 and
    # 14.0 dB at -14.14. Unlike the coloring book Reel there is no cost to the
    # higher gain here — LRA only moves 1.70 to 1.60, because Eryn's read of
    # this script was already flat at 2.00.
    parts.append(f"[{n}:a]volume=14.0dB,alimiter=limit=0.841:level=0,aresample=48000,"
                 f"adelay={int(LEAD*1000)}|{int(LEAD*1000)},apad,atrim=0:{TOTAL}[aout]")

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
        build(platform, os.path.join(HERE, f"expense-report-{platform}.mp4"))


if __name__ == "__main__":
    main()
