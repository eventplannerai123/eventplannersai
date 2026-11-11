"""Fri 13 Nov, 12:30pm — "Planning your own party is the hardest event you'll ever do."

The fifth planner-feelings post. The words are the guide's, verbatim —
headline, three paragraphs and caption were written into the Fri 13 block, so
nothing here is composed.

**1080x1920, NOT the 1350 the earlier ones used.** The Nov 8 format rule turns
this slot into a Reel on Instagram and Facebook — the same still held 7-10
seconds under soft music — and a photo post on TikTok. Both want the 9:16
frame, so one image serves them and `render.py` holds it for 8 seconds over an
instrumental bed generated here.

ITS FORMAT IS NOT THE CAROUSEL BRAND LOOK, AND THAT IS DELIBERATE. The guide
specifies the inverse: deep purple #3C3489 *background*, headline in Poppins
SemiBold *white*, body in Poppins Regular *lavender* #CECBF6, the handle small
at the bottom. No numbered badge, no EP wordmark, no AI demo and no sales
line — a plain text post about what the job feels like, which is the thing
being tested.

AND IT GOES TO TIKTOK TOO, from her Nov 7 rule: "everything should go to both
platforms". On Nov 9 the same JPEG took 322 views on TikTok against 23 on
Instagram, so the file and caption go to her as a matter of course now.

THE BED IS UPBEAT, which is new. Her instruction on Nov 10, after hearing the
first two: "moving forward lets to more upbeat instrumentals". The Wed 11 pair
were deliberately soft because the guide’s format line says "soft
royalty-free music"; she heard them and wanted more energy, and her words
govern. This one is plucked guitar and marimba with a light shaker pulse.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "slides")
FONTS = os.path.join(HERE, "build", "fonts")

W, H = 1080, 1920
PURPLE = (60, 52, 137)
LAVENDER = (206, 203, 246)
WHITE = (255, 255, 255)

P400 = os.path.join(FONTS, "Poppins-400.ttf")
P600 = os.path.join(FONTS, "Poppins-600.ttf")
F = lambda p, s: ImageFont.truetype(p, s)

M = 84
HANDLE = "@aiforeventplanners"

HEAD = "Planning your own party is the hardest event you\u2019ll ever do."

BODY = [
    "You can run a 3,000-person conference without blinking. Then it’s your "
    "own birthday and you can’t pick a restaurant.",

    "Because at work you’re the planner, and at home you just want to be the "
    "guest for once. Nobody believes you, so you end up planning it anyway.",

    "Let someone else do it this year. Even if they get the timeline wrong. "
    "Even if the playlist is terrible. Just show up and be the guest.",
]


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


def layout(d, head_px):
    """Blocks and total height for a headline size; the body scales off it."""
    maxw = W - 2 * M
    hf = F(P600, head_px)
    head = wrap(d, HEAD, hf, maxw)
    hstep = int(head_px * 1.17)

    bp = max(26, int(head_px * 0.50))
    bf = F(P400, bp)
    bstep = int(bp * 1.50)
    gap = int(bp * 1.05)

    paras = [wrap(d, t, bf, maxw) for t in BODY]
    total = (len(head) * hstep + int(head_px * 0.95)
             + sum(len(p) * bstep for p in paras) + gap * (len(paras) - 1))
    return (hf, head, hstep, bf, bstep, gap, paras), total


def build():
    img = Image.new("RGB", (W, H), PURPLE)
    d = ImageDraw.Draw(img)

    top, bottom = 118, H - 132
    budget = bottom - top

    for head_px in range(96, 35, -2):
        parts, total = layout(d, head_px)
        if total <= budget:
            break
    else:
        raise SystemExit("the text does not fit")

    hf, head, hstep, bf, bstep, gap, paras = parts
    y = top + (budget - total) // 2

    for ln in head:
        d.text((M, y), ln, font=hf, fill=WHITE)
        y += hstep
    y += int(head_px * 0.95)

    for k, para in enumerate(paras):
        if k:
            y += gap
        for ln in para:
            d.text((M, y), ln, font=bf, fill=LAVENDER)
            y += bstep

    hfont = F(P400, 24)
    d.text(((W - d.textlength(HANDLE, font=hfont)) / 2, H - 76), HANDLE,
           font=hfont, fill=LAVENDER)
    return img, head_px, y


def check():
    assert len(BODY) == 3, "the guide gives three paragraphs"
    joined = " ".join([HEAD] + BODY).lower()
    for banned in ("prompt", "chatgpt", "claude", "link in bio", "gumroad", "comment "):
        assert banned not in joined, f"no AI demo or sales line: found {banned!r}"
    print("checks pass: three paragraphs, no demo and no sales line")


def main():
    check()
    os.makedirs(OUT, exist_ok=True)
    img, px, end_y = build()
    assert img.size == (W, H)
    p = os.path.join(OUT, "plan-your-own-party.jpg")
    img.save(p, quality=95)
    print(f"headline {px}px, text ends y={end_y} -> {os.path.basename(p)}")


if __name__ == "__main__":
    main()
