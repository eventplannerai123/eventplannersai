import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1350
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "slides"); os.makedirs(OUT, exist_ok=True)

# Palette sampled straight off the Sep 22 tablecloth slides, which the guide
# names as the house carousel look ("same fonts and colours as the earlier
# cheat-sheet carousels").
CREAM   = (245, 241, 232)
PINK    = (237, 223, 222)
INK     = (34, 29, 26)
GREY    = (138, 126, 118)
MAROON  = (122, 42, 54)
BROWN   = (58, 50, 48)     # cover only
ONDARK  = (247, 243, 234)
PINKTXT = (214, 180, 190)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS  = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
SANSB = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
F = lambda p, s: ImageFont.truetype(p, s)

M = 86  # side margin

def wrap(d, text, font, maxw):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= maxw: cur = t
        else: lines.append(cur); cur = w
    if cur: lines.append(cur)
    return lines

def block(d, text, font, x, y, maxw, fill, lh=1.26, align="left"):
    """Draw wrapped text, return the y below it."""
    for ln in wrap(d, text, font, maxw):
        w = d.textlength(ln, font=font)
        xx = x if align == "left" else x + (maxw - w) / 2
        d.text((xx, y), ln, font=font, fill=fill)
        y += int(font.size * lh)
    return y

def tracked(d, text, font, cx, y, fill, track=7):
    """Letter-spaced uppercase label, centred on cx."""
    total = sum(d.textlength(c, font=font) + track for c in text) - track
    x = cx - total / 2
    for c in text:
        d.text((x, y), c, font=font, fill=fill); x += d.textlength(c, font=font) + track
    return y + int(font.size * 1.4)

def footer(d, dark=False):
    f = F(SANS, 26)
    t = "@aiforeventplanners"
    d.text(((W - d.textlength(t, font=f)) / 2, H - 70), t, font=f,
           fill=(GREY if not dark else (120, 108, 104)))

def cover():
    img = Image.new("RGB", (W, H), BROWN); d = ImageDraw.Draw(img)
    f = F(SERIF, 78)
    lines = ["Coat check.", "Linens.", "Administrative fee.", "Cake cutting."]
    y = 300
    for ln in lines:
        d.text(((W - d.textlength(ln, font=f)) / 2, y), ln, font=f, fill=ONDARK)
        y += int(78 * 1.30)
    y += 54
    fs = F(SANS, 38)
    y = block(d, "5 charges that never make the venue's headline rate.",
              fs, M, y, W - 2 * M, PINKTXT, align="center")
    fk = F(SANSB, 32)
    t = "keep swiping  >"
    d.text(((W - d.textlength(t, font=fk)) / 2, H - 300), t, font=fk, fill=PINKTXT)
    footer(d, dark=True)
    img.save(os.path.join(OUT, "slide-1.jpg"), quality=94)

def fee(n, total, title, body, ask, idx):
    img = Image.new("RGB", (W, H), CREAM); d = ImageDraw.Draw(img)
    y = tracked(d, f"CHARGE {n} OF {total}", F(SANSB, 26), W / 2, 250, GREY)
    d.line([(M, y + 26), (W - M, y + 26)], fill=(220, 212, 200), width=2)
    y += 110
    ft = F(SERIF, 72)
    y = block(d, title, ft, M, y, W - 2 * M, INK, lh=1.18)
    y += 44
    fb = F(SANS, 40)
    y = block(d, body, fb, M, y, W - 2 * M, INK, lh=1.42)
    # the pink panel carries the thing to actually say out loud on the visit
    pad, fa = 44, F(SANSB, 36)
    al = wrap(d, ask, fa, W - 2 * M - 2 * pad)
    ph = pad * 2 + int(fa.size * 1.34) * (len(al) - 1) + fa.size + 46
    # sits just under the body rather than pinned to the bottom, so the slide
    # does not open a dead band across its middle
    py = y + 76
    d.rounded_rectangle([M, py, W - M, py + ph], radius=28, fill=PINK)
    ty = tracked(d, "ASK", F(SANSB, 24), W / 2, py + pad, MAROON)
    for ln in al:
        d.text(((W - d.textlength(ln, font=fa)) / 2, ty), ln, font=fa, fill=INK)
        ty += int(fa.size * 1.34)
    footer(d)
    img.save(os.path.join(OUT, f"slide-{idx}.jpg"), quality=94)

def prompt_slide():
    img = Image.new("RGB", (W, H), CREAM); d = ImageDraw.Draw(img)
    y = tracked(d, "THE PROMPT", F(SANSB, 26), W / 2, 250, GREY)
    d.line([(M, y + 26), (W - M, y + 26)], fill=(220, 212, 200), width=2)
    y += 250
    txt = ("Read this venue quote and list every charge that is not in the "
           "headline number. Mark each one as per-person, declinable or "
           "negotiable.")
    pad, fp = 52, F(SANS, 42)
    pl = wrap(d, txt, fp, W - 2 * M - 2 * pad)
    ph = pad * 2 + int(fp.size * 1.40) * (len(pl) - 1) + fp.size
    d.rounded_rectangle([M, y, W - M, y + ph], radius=28, fill=PINK)
    ty = y + pad
    for ln in pl:
        d.text((M + pad, ty), ln, font=fp, fill=INK); ty += int(fp.size * 1.40)
    y = y + ph + 110
    block(d, "Ask on the site visit, not on the final invoice.",
          F(SERIF, 56), M, y, W - 2 * M, INK, lh=1.24, align="center")
    footer(d)
    img.save(os.path.join(OUT, "slide-7.jpg"), quality=94)

FEES = [
    ("Coat check.", "Often charged per guest, or as attendant hours.",
     "Is it per guest or per hour, and is it required in colder months?"),
    ("Linens.", "Sometimes included in the room, sometimes an add-on.",
     "Which sizes and colours does the price cover?"),
    ("Administrative fee.", "Usually a percentage on top of food and beverage, "
     "and usually not a gratuity.", "What does this fee actually cover?"),
    ("Cake cutting.", "Charged when the cake comes from an outside baker.",
     "Per slice or per guest?"),
    ("AV.", "Projector, screen and microphones are not always in the room rate.",
     "Per item, and is there a fee for bringing my own AV team?"),
]

cover()
for i, (t, b, a) in enumerate(FEES, start=1):
    fee(i, len(FEES), t, b, a, i + 1)
prompt_slide()
print(f"{len(FEES)} fee slides + cover + prompt = {len(FEES) + 2} slides")
print("cover says 5, fee slides =", len(FEES), "->", "OK" if len(FEES) == 5 else "MISMATCH")
