"""Tue 6 Oct cancellation-clause quick piece.

Four freeze frames, no scrolling, no voiceover. Everything is a still: the
source only ever moves by scrolling, and the brief rules scrolling out.
"""
import os, subprocess
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
SRC, OUT, W, H = "source.mp4", "frames", 1080, 1920
os.makedirs(OUT, exist_ok=True)

# One crop for every beat, so the piece does not appear to jump around.
# 1125x2000 at (40,300) from the 1206x2622 capture:
#   - 300 off the top clears the status bar (time, red dot) and the nav row
#   - ending at 2300 clears the "Ask ChatGPT" bar, which starts about 2374
#   - 1125/2000 is exactly 0.5625, and 1125 wide still holds the full text
#     column (x 47-1150), so no words are cut
CX, CY, CW, CH = 40, 300, 1125, 2000
S = W / CW  # 0.96, source px -> output px

INK    = (34, 29, 26)
AMBER  = (255, 206, 74, 115)   # the single highlight colour, translucent
SANS   = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
SANSB  = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"

def grab(t, name):
    subprocess.run(f'ffmpeg -y -loglevel error -ss {t} -i {SRC} -frames:v 1 {OUT}/{name}',
                   shell=True, check=True)
    return Image.open(f"{OUT}/{name}").convert("RGB")

def base(t, name):
    im = grab(t, name).crop((CX, CY, CX + CW, CY + CH)).resize((W, H), Image.LANCZOS)
    return im.convert("RGBA")

def hl(img, boxes, pad=10, r=12):
    """Amber bands behind the lines named in source coordinates."""
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    for x0, y0, x1, y1 in boxes:
        X0, Y0 = (x0 - CX) * S, (y0 - CY) * S
        X1, Y1 = (x1 - CX) * S, (y1 - CY) * S
        d.rounded_rectangle([X0 - pad, Y0 - pad, X1 + pad, Y1 + pad], radius=r, fill=AMBER)
    return Image.alpha_composite(img, lay)

def card(img, lines, cy, fs=58, pad=42, r=28):
    """Solid dark card — a text overlay, deliberately not the highlight colour."""
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    f = ImageFont.truetype(SANSB, fs); lh = int(fs * 1.34)
    w = max(d.textlength(l, font=f) for l in lines)
    bw, bh = w + pad * 2, lh * (len(lines) - 1) + fs + pad * 2
    x0, y0 = (W - bw) // 2, cy - bh // 2
    d.rounded_rectangle([x0, y0, x0 + bw, y0 + bh], radius=r, fill=(26, 22, 20, 242))
    ty = y0 + pad
    for l in lines:
        d.text(((W - d.textlength(l, font=f)) / 2, ty), l, font=f, fill=(255, 255, 255, 255))
        ty += lh
    return Image.alpha_composite(img, lay)

# 1 — the prompt, held 3s. No hook line before it, per the quick-piece format.
base(0, "f1.png").convert("RGB").save("frames/slide1.jpg", quality=95)

# 2 — the deposit sits on top of the fee
im = base(13, "f2.png")
im = hl(im, [(963, 369, 1055, 417),    # "the" (end of line 1)
             (47, 452, 1124, 502),     # "25% deposit is on top of the cancellation"
             (47, 537, 858, 587)])     # "fee—it does not count toward it."
im.convert("RGB").save("frames/slide2.jpg", quality=95)

# 3 — the arithmetic
im = base(15, "f3.png")
im = hl(im, [(47, 544, 1098, 596),     # "$21,250 deposit + $63,750 cancellation"
             (47, 629, 736, 681)])     # "damages = $85,000 total."
im.convert("RGB").save("frames/slide3.jpg", quality=95)

# 4 — the takeaway. Taken at 25.5, NOT 26.0: the Visit Denver ad is already on
# screen at 26.0, and no 9:16 crop can hold this full-width sentence while
# excluding it. Same sentence, same wording, one frame earlier, no ad anywhere.
im = base(25.5, "f4.png")
im = hl(im, [(1035, 1961, 1150, 2011), # "turns"
             (47, 2046, 1061, 2096),   # "an otherwise 75% cancellation fee at 60"
             (47, 2131, 899, 2181)])   # "days into an effective 100% cost."
im = card(im, ["60 days out: the table says 75%.",
               "The contract charges 100%."], 1330)
im.convert("RGB").save("frames/slide4.jpg", quality=95)

# Hold each still for its beat, then join. Hard cuts: the brief gives exact
# boundaries and a dissolve would soften them.
BEATS = [("slide1.jpg", 3.0), ("slide2.jpg", 4.0), ("slide3.jpg", 4.0), ("slide4.jpg", 5.0)]
parts = []
for i, (f, dur) in enumerate(BEATS):
    p = f"frames/seg{i}.mp4"; parts.append(p)
    subprocess.run(f'ffmpeg -y -loglevel error -loop 1 -t {dur} -i frames/{f} '
                   f'-vf "scale={W}:{H},setsar=1,fps=30" -c:v libx264 -profile:v high '
                   f'-crf 19 -pix_fmt yuv420p {p}', shell=True, check=True)
with open("frames/list.txt", "w") as fh:
    for p in parts: fh.write(f"file '{os.path.basename(p)}'\n")
subprocess.run('ffmpeg -y -loglevel error -f concat -safe 0 -i frames/list.txt '
               '-c:v copy frames/novo.mp4', shell=True, check=True)
# silent track, so the file is not audio-less on upload
subprocess.run('ffmpeg -y -loglevel error -i frames/novo.mp4 -f lavfi '
               '-i anullsrc=r=48000:cl=stereo -shortest -c:v copy -c:a aac -b:a 192k '
               '-ar 48000 -movflags +faststart ../cancellation-tiktok.mp4',
               shell=True, check=True)
print(subprocess.run('ffprobe -v error -show_entries stream=width,height,r_frame_rate '
                     '-show_entries format=duration,size -of default=noprint_wrappers=1 '
                     '../cancellation-tiktok.mp4', shell=True, capture_output=True,
                     text=True).stdout)
