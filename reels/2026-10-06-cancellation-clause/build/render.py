"""Tue 6 Oct cancellation piece — v4, built to her Oct 5 story brief.

Five freeze frames in narrative order: the prompt, what the contract says, the
catch, the maths, the takeaway. Voiceover throughout.

The change from v3: no strip on a dimmed frame. Each beat fills the frame with
real screenshot, and the target lines are centred by **choosing a source frame
where they already sit mid-screen** rather than by moving them afterwards.
"""
import os, subprocess
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
SRC, OUT, W, H = "source.mp4", "frames", 1080, 1920
os.makedirs(OUT, exist_ok=True)

# The widest 9:16 window that clears the status bar (ends ~300) at the top and
# the "Ask ChatGPT" bar (starts ~2374) at the bottom. 1125/2000 = 0.5625 exactly,
# and 1125 still holds the full text column (x 47-1150), so no words are cut.
CX, CY, CW, CH = 40, 300, 1125, 2000
S = W / CW

SAFE_TOP, SAFE_BOT = int(H * 0.12), int(H * 0.75)
AMBER = (255, 206, 74, 125)
PAPER = (247, 247, 248)          # the chat's own background
SANSB = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
ARROW = (544, 2192, 662, 2310)   # the floating scroll-to-bottom button

def grab(t, name):
    subprocess.run(f'ffmpeg -y -loglevel error -ss {t} -i {SRC} -frames:v 1 {OUT}/{name}',
                   shell=True, check=True)
    return Image.open(f"{OUT}/{name}").convert("RGB")

def no_arrow(im):
    from PIL import ImageFilter
    x0, y0, x1, y1 = ARROW; pad = 18
    box = (x0 - pad, y0 - pad, x1 + pad, y1 + pad)
    im.paste(im.crop(box).filter(ImageFilter.GaussianBlur(26)), box)
    return im

def frame(full, crop, shift=0, height=None):
    """Scale a source window to fill the frame width. `height` crops the window
    short (used to cut an ad off the bottom); `shift` drops it down the canvas.
    Anything not covered is filled with the chat's own background, so the join
    reads as more page rather than as a card."""
    x0, y0, w, h = crop
    im = full.crop((x0, y0, x0 + w, y0 + (height or h)))
    sc = W / w
    im = im.resize((W, round(im.height * sc)), Image.LANCZOS)
    canvas = Image.new("RGBA", (W, H), PAPER + (255,))
    canvas.paste(im.convert("RGBA"), (0, shift))
    return canvas, sc, x0, y0, shift

def highlight(img, geom, boxes, pad=10, r=14):
    _, sc, x0, y0, shift = geom
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    top, bot = H, 0
    for bx0, by0, bx1, by1 in boxes:
        X0, Y0 = (bx0 - x0) * sc, (by0 - y0) * sc + shift
        X1, Y1 = (bx1 - x0) * sc, (by1 - y0) * sc + shift
        d.rounded_rectangle([X0 - pad, Y0 - pad, X1 + pad, Y1 + pad], radius=r, fill=AMBER)
        top, bot = min(top, Y0), max(bot, Y1)
    assert top > SAFE_TOP and bot < SAFE_BOT, f"highlight {top:.0f}-{bot:.0f} outside the safe band"
    print(f"      highlight {top:.0f}-{bot:.0f}  ({top/H:.0%}-{bot/H:.0%})")
    return Image.alpha_composite(img, lay)

def card(img, lines, cy, maxw=820, fs=78, pad=38, r=26, x=36):
    d0 = ImageDraw.Draw(img)
    while fs > 28:
        f = ImageFont.truetype(SANSB, fs)
        if max(d0.textlength(l, font=f) for l in lines) <= maxw: break
        fs -= 2
    f = ImageFont.truetype(SANSB, fs); lh = int(fs * 1.26)
    w = max(d0.textlength(l, font=f) for l in lines)
    bw, bh = w + pad * 2, lh * (len(lines) - 1) + fs + pad * 2
    y = cy - bh // 2
    assert y > SAFE_TOP and y + bh < SAFE_BOT, f"card {y}-{y+bh} outside the safe band"
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    d.rounded_rectangle([x, y, x + bw, y + bh], radius=r, fill=(26, 22, 20, 247))
    ty = y + pad
    for l in lines:
        d.text((x + pad, ty), l, font=f, fill=(255, 255, 255, 255)); ty += lh
    print(f"      card {fs}px  {y}-{y+bh}")
    return Image.alpha_composite(lay, img) if False else Image.alpha_composite(img, lay)

def save(img, name):
    img.convert("RGB").save(f"frames/{name}", quality=95); print(f"   {name}")

# 1 — THE PROMPT. The bubble is narrower than the answer text, so this is the one
# beat that takes a real zoom: a 855px-wide window blown up to 1080 is 1.26x.
# Dropped 180px down the canvas so the overlay has room above it without
# covering the question — there is only 240px of blank screen above the bubble
# in the source, and no crop can manufacture more.
f = no_arrow(grab(0, "f1.png"))
g = frame(f, (290, 150, 855, 1520), shift=180, height=1300)
img = card(g[0], ["I asked AI what cancelling", "60 days out would cost."], 350)
save(img, "slide1.jpg")

# 2 — WHAT THE CONTRACT SAYS. At t=13 the 89-60 day row sits at 48% of frame.
f = no_arrow(grab(13, "f2.png"))
g = frame(f, (CX, CY, CW, CH))
save(highlight(g[0], g, [(47, 1264, 1150, 1323)]), "slide2.jpg")

# 3 — THE CATCH. At t=12 this sentence sits at 43-54%; at t=13 it is at the very
# top of the frame. Picking the frame is what centres it.
f = no_arrow(grab(12, "f3.png"))
g = frame(f, (CX, CY, CW, CH))
save(highlight(g[0], g, [(969, 1166, 1055, 1216), (47, 1251, 1124, 1301),
                         (47, 1336, 858, 1386)]), "slide3.jpg")

# 4 — THE MATHS. At t=14.4 the total sits at 53-60%.
f = no_arrow(grab(14.4, "f4.png"))
g = frame(f, (CX, CY, CW, CH))
save(highlight(g[0], g, [(47, 1369, 1098, 1421), (47, 1454, 736, 1506)]), "slide4.jpg")

# 5 — THE TAKEAWAY. At t=26 the sentence sits at 42-53%, but the Visit Denver ad
# is on screen from y 1913. The window is cut at 1900 and the rest of the canvas
# is the page's own background, so the ad cannot appear at all.
f = no_arrow(grab(26, "f5.png"))
g = frame(f, (CX, CY, CW, CH), height=1600)
img = highlight(g[0], g, [(1035, 1133, 1150, 1185), (47, 1218, 1061, 1270),
                          (47, 1303, 899, 1356)])
img = card(img, ["The table says 75%.", "The contract charges 100%."], 1250)
save(img, "slide5.jpg")

BEATS = [("slide1.jpg", 4.0), ("slide2.jpg", 3.0), ("slide3.jpg", 4.0),
         ("slide4.jpg", 4.0), ("slide5.jpg", 2.4)]
parts = []
for i, (fn, dur) in enumerate(BEATS):
    p = f"frames/seg{i}.mp4"; parts.append(p)
    subprocess.run(f'ffmpeg -y -loglevel error -loop 1 -t {dur} -i frames/{fn} '
                   f'-vf "scale={W}:{H},setsar=1,fps=30" -c:v libx264 -profile:v high '
                   f'-crf 19 -pix_fmt yuv420p {p}', shell=True, check=True)
with open("frames/list.txt", "w") as fh:
    for p in parts: fh.write(f"file '{os.path.basename(p)}'\n")
subprocess.run('ffmpeg -y -loglevel error -f concat -safe 0 -i frames/list.txt '
               '-c:v copy frames/novo.mp4', shell=True, check=True)
# loudnorm's two-pass stalls short on this voice (the true-peak ceiling binds
# first), so the gain is applied directly and alimiter — level=0, or it
# renormalises straight back — catches the peaks. Confirmed on the export.
subprocess.run('ffmpeg -y -loglevel error -i vo-raw.mp3 '
               '-af "volume=9.9dB,alimiter=limit=-1.5dB:level=0" -ar 48000 vo.wav',
               shell=True, check=True)
subprocess.run('ffmpeg -y -loglevel error -i frames/novo.mp4 -i vo.wav -c:v copy '
               '-c:a aac -b:a 192k -ar 48000 -movflags +faststart '
               '../cancellation-tiktok.mp4', shell=True, check=True)
print(subprocess.run('ffprobe -v error -show_entries stream=codec_name,width,height '
                     '-show_entries format=duration -of default=noprint_wrappers=1 '
                     '../cancellation-tiktok.mp4', shell=True, capture_output=True,
                     text=True).stdout)
