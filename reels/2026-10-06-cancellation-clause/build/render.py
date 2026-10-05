"""Tue 6 Oct cancellation-clause quick piece — v2.

Four freeze frames, no scrolling, no voiceover.

v2 answers the author's note on v1: the highlighted lines are now genuinely
zoomed rather than shown at source size. That cannot be done with a plain crop
— the answer text runs nearly the full width of the capture, so any 9:16 crop
tight enough to magnify it clips words. So each highlighted passage is lifted
out as a strip, scaled up, and set on a dimmed copy of the frame it came from.
The frame stays as context; the strip is the thing to read.
"""
import os, subprocess
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

HERE = os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
SRC, OUT, W, H = "source.mp4", "frames", 1080, 1920
os.makedirs(OUT, exist_ok=True)

# Base crop, unchanged from v1: clears the status bar and red dot at the top and
# the "Ask ChatGPT" bar at the bottom, and is exactly 0.5625.
CX, CY, CW, CH = 40, 300, 1125, 2000
S = W / CW

# TikTok safe area, from the author's brief: nothing that matters in the top
# 12%, the bottom 25%, or the right 15%.
SAFE_TOP, SAFE_BOT, SAFE_RIGHT = int(H * 0.12), int(H * 0.75), int(W * 0.85)
STRIP_W = 880          # ~81% of frame width, and ends at x=910, clear of 918
STRIP_X = 30
STRIP_CY = int(H * 0.475)   # middle of the 25%-70% band

AMBER = (255, 206, 74, 125)
SANSB = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"

# the floating scroll-to-bottom button, in source coordinates
ARROW = (544, 2192, 662, 2310)

def grab(t, name):
    subprocess.run(f'ffmpeg -y -loglevel error -ss {t} -i {SRC} -frames:v 1 {OUT}/{name}',
                   shell=True, check=True)
    return Image.open(f"{OUT}/{name}").convert("RGB")

def background(full):
    """The frame, dimmed and softened so it reads as context and nothing more."""
    im = full.crop((CX, CY, CX + CW, CY + CH)).resize((W, H), Image.LANCZOS)
    # blurred hard on purpose: at a light blur the same sentence stays legible
    # in the background as well as in the strip, and the frame reads as two
    # copies of itself rather than one zoomed passage
    im = im.filter(ImageFilter.GaussianBlur(16))
    return ImageEnhance.Brightness(im).enhance(0.46).convert("RGBA")

def drop_arrow(full):
    """Blur out the floating down-arrow rather than paint over it — it sits on
    top of body text, so a filled patch would erase words as well."""
    x0, y0, x1, y1 = ARROW
    pad = 18
    box = (x0 - pad, y0 - pad, x1 + pad, y1 + pad)
    full.paste(full.crop(box).filter(ImageFilter.GaussianBlur(26)), box)
    return full

def strip(full, boxes, pad_x=20, pad_y=18):
    """Lift the highlighted passage out, scale it up, draw the bands on it."""
    x0 = min(b[0] for b in boxes) - pad_x; x1 = max(b[2] for b in boxes) + pad_x
    y0 = min(b[1] for b in boxes) - pad_y; y1 = max(b[3] for b in boxes) + pad_y
    f = STRIP_W / (x1 - x0)
    im = full.crop((x0, y0, x1, y1)).resize((STRIP_W, round((y1 - y0) * f)),
                                            Image.LANCZOS).convert("RGBA")
    lay = Image.new("RGBA", im.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    for bx0, by0, bx1, by1 in boxes:
        d.rounded_rectangle([(bx0 - x0) * f - 8, (by0 - y0) * f - 8,
                             (bx1 - x0) * f + 8, (by1 - y0) * f + 8],
                            radius=12, fill=AMBER)
    return Image.alpha_composite(im, lay)

def place(bg, st):
    """Set the strip in the safe middle band. The strip carries the chat's own
    near-white background, so it needs no card behind it — only a soft shadow to
    lift it off the dimmed frame."""
    x, y = STRIP_X, STRIP_CY - st.height // 2
    assert y > SAFE_TOP and y + st.height < SAFE_BOT, f"strip {y}-{y+st.height} outside safe band"
    assert x + st.width <= SAFE_RIGHT, f"strip right edge {x+st.width} intrudes on the right 15%"
    sh = Image.new("RGBA", bg.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle([x - 6, y - 6, x + st.width + 6, y + st.height + 6],
                                         radius=20, fill=(0, 0, 0, 120))
    out = Image.alpha_composite(bg, sh.filter(ImageFilter.GaussianBlur(14)))
    out.paste(st, (x, y), st)
    return out

def headline(img, lines, cy, maxw=800, fs=76):
    """The overlay card: the biggest type on screen, in the upper third."""
    d0 = ImageDraw.Draw(img)
    while fs > 30:
        f = ImageFont.truetype(SANSB, fs)
        if max(d0.textlength(l, font=f) for l in lines) <= maxw: break
        fs -= 2
    f = ImageFont.truetype(SANSB, fs); lh = int(fs * 1.28); pad = 40
    w = max(d0.textlength(l, font=f) for l in lines)
    bw, bh = w + pad * 2, lh * (len(lines) - 1) + fs + pad * 2
    x, y = STRIP_X, cy - bh // 2
    assert y > SAFE_TOP, f"headline top {y} is inside the top 12%"
    assert x + bw <= SAFE_RIGHT + 8, f"headline right edge {x+bw} intrudes"
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    d.rounded_rectangle([x, y, x + bw, y + bh], radius=28, fill=(26, 22, 20, 247))
    ty = y + pad
    for l in lines:
        d.text((x + pad, ty), l, font=f, fill=(255, 255, 255, 255)); ty += lh
    print(f"   headline {fs}px, card {x}-{x+bw} x {y}-{y+bh}")
    return Image.alpha_composite(img, lay)

# 1 — the prompt, full frame, held 3s. Sharp, so the arrow is blurred out here.
f1 = drop_arrow(grab(0, "f1.png"))
f1.crop((CX, CY, CX + CW, CY + CH)).resize((W, H), Image.LANCZOS).save(
    "frames/slide1.jpg", quality=95)

def beat(t, name, boxes, head=None, out_name="x.jpg"):
    full = drop_arrow(grab(t, name))
    img = place(background(full), strip(full, boxes))
    if head: img = headline(img, head, int(H * 0.235))
    img.convert("RGB").save(f"frames/{out_name}", quality=95)
    print(f"   {out_name} from t={t}")

# 2 — the deposit sits on top of the fee
beat(13, "f2.png", [(963, 369, 1055, 417), (47, 452, 1124, 502), (47, 537, 858, 587)],
     out_name="slide2.jpg")
# 3 — the arithmetic
beat(15, "f3.png", [(47, 544, 1098, 596), (47, 629, 736, 681)], out_name="slide3.jpg")
# 4 — the takeaway, at 25.5 not 26.0: the Visit Denver ad is on screen by 26.0
beat(25.5, "f4.png", [(1035, 1961, 1150, 2011), (47, 2046, 1061, 2096),
                      (47, 2131, 899, 2181)],
     head=["60 days out:", "the table says 75%.", "The contract charges 100%."],
     out_name="slide4.jpg")

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
subprocess.run('ffmpeg -y -loglevel error -i frames/novo.mp4 -f lavfi '
               '-i anullsrc=r=48000:cl=stereo -shortest -c:v copy -c:a aac -b:a 192k '
               '-ar 48000 -movflags +faststart ../cancellation-tiktok.mp4',
               shell=True, check=True)
print(subprocess.run('ffprobe -v error -show_entries stream=width,height,r_frame_rate '
                     '-show_entries format=duration -of default=noprint_wrappers=1 '
                     '../cancellation-tiktok.mp4', shell=True, capture_output=True,
                     text=True).stdout)
