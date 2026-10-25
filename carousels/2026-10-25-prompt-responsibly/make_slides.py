"""Prompt Responsibly carousel — 4 slides, two sizes.

Sun 25 Oct. Slide 1 is her own photo of the hat; slides 2-4 are the three
rules in house type.

NEVER NAME THE CONFERENCE OR WHOEVER GAVE THE HAT OUT — the brief says so, and
the photo was checked for it rather than assumed: the hat itself carries only
the words "Prompt Responsibly", and the out-of-focus background is a kitchen
counter with no legible text or branding anywhere in frame.

THE PHOTO IS HERS, SO IT IS CROPPED, NOT REGENERATED. It comes off the phone at
4284x5712 (3:4) as HEIC, which needs pillow-heif to open at all; the decoded
JPEG is committed as build/hat.jpg. Each output size takes its own window out
of it rather than squashing one crop to fit both.

The line on slide 1 sits over the maroon brim, where cream type reads cleanly
and nothing in the photograph is covered. The hat's own colours are cream and
maroon, which is the house palette already.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "slides")
HAT = os.path.join(HERE, "build", "hat.jpg")

W = 1080
SIZES = {"tiktok": 1920, "instagram": 1350}

CREAM = (245, 241, 232)
INK = (34, 29, 26)
GREY = (138, 126, 118)
MAROON = (122, 42, 54)
BROWN = (58, 50, 48)
ONDARK = (247, 243, 234)
PINKTXT = (214, 180, 190)
RULE = (220, 212, 200)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
SANSB = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
F = lambda p, s: ImageFont.truetype(p, s)

M = 86
LABEL_H = 146

# Broken by hand: wrapped to the panel width it orphans "by." on its own line.
HAT_LINES = ["Got this at a conference.", "It's the rule I work by."]

RULES = [
    ("1.", "Give it the whole picture.",
     "Guest count, venue, service style, budget. “Plan a dinner” gets you a "
     "generic list anyone could have written."),
    ("2.", "Check everything it gives you.",
     "AI makes mistakes, just like we do."),
    ("3.", "Keep client names out of it.",
     None),
]

CLOSER = "Prompt responsibly."


def wrap(d, text, font, maxw):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= maxw:
            cur = t
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def measure(d, text, font, maxw, lh=1.26):
    return len(wrap(d, text, font, maxw)) * int(font.size * lh)


def block(d, text, font, x, y, maxw, fill, lh=1.26, align="left"):
    for ln in wrap(d, text, font, maxw):
        w = d.textlength(ln, font=font)
        xx = x if align == "left" else x + (maxw - w) / 2
        d.text((xx, y), ln, font=font, fill=fill)
        y += int(font.size * lh)
    return y


def footer(d, H, dark=False):
    f = F(SANS, 26)
    t = "@aiforeventplanners"
    d.text(((W - d.textlength(t, font=f)) / 2, H - 70), t, font=f,
           fill=(GREY if not dark else (120, 108, 104)))


def new(H, bg=CREAM):
    img = Image.new("RGB", (W, H), bg)
    return img, ImageDraw.Draw(img)


def slide1(H):
    """Her photo, cropped to this output's shape, with the one small line."""
    src = Image.open(HAT)
    sw, sh = src.size
    target = W / H
    if sw / sh > target:                      # too wide: trim the sides
        cw = int(sh * target)
        box = ((sw - cw) // 2, 0, (sw - cw) // 2 + cw, sh)
    else:                                     # too tall: trim top and bottom
        ch = int(sw / target)
        top = int((sh - ch) * 0.52)           # the hat sits a touch below centre
        box = (0, top, sw, top + ch)
    img = src.crop(box).resize((W, H), Image.LANCZOS)
    d = ImageDraw.Draw(img, "RGBA")

    f = F(SANSB, 38)
    lines = HAT_LINES
    lh = int(38 * 1.34)
    bh = lh * (len(lines) - 1) + 38 + 72
    bw = max(d.textlength(l, font=f) for l in lines) + 96
    y0 = int(H * 0.60)
    assert y0 > H * 0.12 and y0 + bh < H * 0.80, "line is outside the safe band"
    x0 = (W - bw) / 2
    d.rounded_rectangle([x0, y0, x0 + bw, y0 + bh], radius=26, fill=(34, 29, 26, 196))
    ty = y0 + 36
    for l in lines:
        d.text(((W - d.textlength(l, font=f)) / 2, ty), l, font=f, fill=ONDARK)
        ty += lh
    footer(d, H, dark=True)
    return img


def rule_slide(H, n, head, body, closer=False):
    img, d = new(H, BROWN if closer else CREAM)
    numf = F(SERIF, 72)
    headf = F(SERIF, 54)
    bodyf = F(SANS, 36)
    fg = ONDARK if closer else INK
    sub = PINKTXT if closer else GREY

    hh = int(72 * 1.3) + 30 + measure(d, head, headf, W - 2 * M, 1.26)
    if body:
        hh += 36 + measure(d, body, bodyf, W - 2 * M, 1.34)
    if closer:
        hh += 60 + int(58 * 1.3)
    y = (H - hh) // 2

    d.text((M, y), n, font=numf, fill=MAROON if not closer else PINKTXT)
    y += int(72 * 1.3) + 30
    y = block(d, head, headf, M, y, W - 2 * M, fg, lh=1.26)
    if body:
        y += 36
        y = block(d, body, bodyf, M, y, W - 2 * M, sub, lh=1.34)
    if closer:
        y += 60
        cf = F(SERIF, 58)
        d.text(((W - d.textlength(CLOSER, font=cf)) / 2, y), CLOSER, font=cf, fill=ONDARK)
    footer(d, H, dark=closer)
    return img


def main():
    for name, H in SIZES.items():
        out = os.path.join(OUT, name)
        os.makedirs(out, exist_ok=True)
        slides = [slide1(H)]
        for i, (n, head, body) in enumerate(RULES):
            slides.append(rule_slide(H, n, head, body, closer=(i == len(RULES) - 1)))
        for i, img in enumerate(slides, 1):
            assert img.size == (W, H)
            img.save(os.path.join(out, f"slide-{i}.jpg"), quality=94)
        print(f"{name}: {len(slides)} slides at {W}x{H} -> {out}")


if __name__ == "__main__":
    main()
