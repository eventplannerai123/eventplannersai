"""Fri 20 Nov, 12:30pm — "You’re the calmest person in the room because you
already panicked at 5am."

Planner-feelings post 8, the third under the Sun 15 recap's restart of the
second posts on Mon, Wed and Fri. The words are hers, verbatim from the Fri 20
block — headline, three paragraphs and caption. Nothing here is composed.

Format is the inverse of the carousel look, as the guide specifies for this
slot: deep purple #3C3489 ground, headline in Poppins SemiBold white, body in
Poppins Regular lavender #CECBF6, the handle small at the bottom. No numbered
badge, no EP wordmark, no AI demo and no sales line.

1080x1920 AND A REEL, NOT A PHOTO — the still held 8 seconds under its own
bed. On Mon 9 the photo version of this slot reached 15, against 146 and 130
for the two posted as Reels, so the block says to check the profile after
posting and confirm it shows as a Reel.

ITS BED IS ITS OWN. Friday carries two posts — the 6:30pm giveaway Reel and
this one — and on Nov 11 both of that day's Reels went out on one track, the
short cut being the opening bars of the long one, which she heard at once.
Two generations, two different instruments.

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

HEAD = "You’re the calmest\nperson in the room\nbecause you already\npanicked at 5am."

BODY = [
    "By the time doors open you’ve run every version of what could go wrong.",

    "The weather, the shuttle, the speaker who hasn’t landed. You did the "
    "worrying early so nobody else has to do it at 7pm.",

    "Calm isn’t the absence of panic. It’s panic that got there first.",
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
    # HEAD carries its own breaks, because "because you already" has to land
    # on one line: let the wrapper choose and it splits mid-phrase.
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
    return (hf, head, hstep, bf, bstep, gap, paras), total, len(head)


def build():
    img = Image.new("RGB", (W, H), PURPLE)
    d = ImageDraw.Draw(img)

    top, bottom = 118, H - 132
    budget = bottom - top

    # A size that re-wraps one of HEAD’s own lines is the wrong size, however
    # well the block fits — the Nov 18 build found that at 96px, where its
    # headline broke into six ragged lines. Kept as a guard, not a tweak.
    written = len(HEAD.split("\n"))
    for head_px in range(96, 35, -2):
        parts, total, lines = layout(d, head_px)
        if total <= budget and lines == written:
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
    p = os.path.join(OUT, "calmest-person.jpg")
    img.save(p, quality=95)
    print(f"headline {px}px, text ends y={end_y} -> {os.path.basename(p)}")


if __name__ == "__main__":
    main()
