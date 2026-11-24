"""Fri 27 Nov, 12:30pm — "Everyone’s off this week. Your December isn’t."

A planner-feelings Reel: one text image held 7-10 seconds with music and no
voiceover on Instagram and Facebook, and the same image as a photo post on
TikTok. Deep purple #3C3489 ground, white headline, lavender body, Poppins —
the November plan’s format for this type.

**THE WORDS ARE THE GUIDE’S**, headline and all three paragraphs, split on
the "/" its Fri 27 block uses. `check()` reconstructs them and compares word
for word, so a tidy-up fails the build.

**IT GOES OUT ON BLACK FRIDAY AND CARRIES NO SALE.** The day’s other post
does — the 6:30pm giveaway Reel sits inside the BLACKFRIDAY window — and the
guide is explicit that the discount belongs in the Story, not in a Reel. This
piece is about closing the laptop, so a price on it would undo the sentiment
it is selling. `check()` refuses BUDGET, BLACKFRIDAY and a dollar sign.

NO CTA on the frame; the ask is the question at the end of the caption, and
she leaves the first comment within ten minutes.
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

HEAD = "Everyone\u2019s off this week. Your December isn\u2019t."

# The guide's three paragraphs, split on its own "/".
BODY = [
    "The holiday parties are booked, the headcounts aren\u2019t final, and half "
    "the vendors are out until Monday.",

    "So you answer the one email that can\u2019t wait, and you close the laptop.",

    "December will still be there on Monday morning. Eat the leftovers.",
]

GUIDE_HEAD = "Everyone\u2019s off this week. Your December isn\u2019t."
GUIDE_BODY = ("The holiday parties are booked, the headcounts aren\u2019t final, "
              "and half the vendors are out until Monday. / So you answer the "
              "one email that can\u2019t wait, and you close the laptop. / "
              "December will still be there on Monday morning. Eat the "
              "leftovers.")


def check():
    import re
    w = lambda s: re.findall(r"[a-z0-9\u2019]+", s.lower())
    assert HEAD == GUIDE_HEAD, "the headline drifted from the guide"
    assert w(" ".join(BODY)) == w(GUIDE_BODY.replace("/", " ")), (
        "a body paragraph drifted from the guide")
    assert len(BODY) == 3, len(BODY)

    # Black Friday is the day, and the sale lives in the Story, not here.
    joined = (HEAD + " " + " ".join(BODY)).lower()
    for banned in ("budget", "blackfriday", "$", "%", "link in bio", "comment ",
                   "prompt", "chatgpt", "claude", "gumroad"):
        assert banned not in joined, f"this piece must not carry {banned!r}"
    print("checks pass: the guide's headline and three paragraphs, "
          "no sale and no demo")


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

    # THE SAFE ZONE IS THE LAYOUT, not a check afterwards. The Nov 11
    # planner-feelings image centred its text in a 118-1788 band, which is
    # the whole frame, and its last line landed at y=1627 — inside the
    # bottom 25% where TikTok's caption and buttons sit. It got away with it
    # because the paragraph that fell there was the one the reader had
    # already finished. This piece is three short paragraphs, so the block is
    # centred inside 250-1440 like the list Reels instead, and main() asserts
    # it. The headline solves down a size or two as a result.
    top, bottom = 250, 1440
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


def main():
    check()
    os.makedirs(OUT, exist_ok=True)
    img, px, end_y = build()
    assert img.size == (W, H)
    # Nothing important in the bottom 25%, where TikTok's caption and buttons
    # sit. On this format the paragraphs ARE the content.
    assert end_y <= 1440, f"the text ends at {end_y}, inside the bottom 25%"
    p = os.path.join(OUT, "december-isnt.jpg")
    img.save(p, quality=95)
    print(f"headline {px}px, text ends y={end_y} -> {os.path.basename(p)}")


if __name__ == "__main__":
    main()
