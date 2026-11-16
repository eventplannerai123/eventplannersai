"""Mon 16 Nov, 12:30pm — "The guests leave at 11. You leave at 1."

Planner-feelings post 6. **She added this one to the guide this morning**
after the 12:30pm slot came up empty: the Mon 16 block was written on Thu 12,
before the Sun 15 recap restarted the second posts on Wed 18, so Monday fell
through the gap in the Mon/Wed/Fri rule. Her line in the block reads "added
Nov 16, Sahiba: yes to one today".

The words are hers, verbatim from the block — headline, three paragraphs and
caption. Nothing here is composed.

FORMAT IS THE INVERSE OF THE CAROUSEL LOOK, as the guide specifies for this
slot: deep purple #3C3489 ground, headline in Poppins SemiBold white, body in
Poppins Regular lavender #CECBF6, the handle small at the bottom. No numbered
badge, no EP wordmark, no AI demo and no sales line.

1080x1920 AND A REEL, NOT A PHOTO. The Nov 8 rule makes this slot a Reel on
Instagram and Facebook — the still held 8 seconds under a bed — and the Sun 15
recap sharpened it with a number: on Mon 9 the photo version reached 15,
against 146 and 130 for the two posted as Reels. The Wed 18 block now says to
check the profile after posting and confirm it shows as a Reel.

TikTok takes the same image as a photo post, from her, per the Nov 7
both-platforms rule.
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

HEAD = "The guests leave at 11.\nYou leave at 1."

BODY = [
    "Strike starts when the last guest walks out.",

    "The rentals get counted, the vendors get signed out, the lost-and-found "
    "gets a bag. Someone has to be the last one to leave, and it\u2019s always "
    "you.",

    "The party ended at 11. Your night ended in the parking lot.",
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
    # HEAD carries its own break ("The guests leave at 11." / "You leave at
    # 1."), because the two halves are the joke and a reflowed break ruins it.
    head = []
    for line in HEAD.split("\n"):
        head += wrap(d, line, hf, maxw)
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
    p = os.path.join(OUT, "guests-leave-at-11.jpg")
    img.save(p, quality=95)
    print(f"headline {px}px, text ends y={end_y} -> {os.path.basename(p)}")


if __name__ == "__main__":
    main()
