"""Setup times carousel — 5 slides, two sizes.

Thu 22 Oct, the day's regular Instagram post. Content bank item 14, her line:
"The pros know their setup time down to the minute."

Same palette, fonts and furniture as the Oct 21 wrong-entrance carousel and the
Oct 18 runny eggs one.

SLIDE 4 IS HOUSE TYPE, NOT A SCREENSHOT, and its heading says so. There is no
recording for this piece — the guide's CLAUDE CODE line builds the carousel
outright — so the Oct 18/Oct 21 precedent applies: set the output in house type
under a heading that claims no particular tool.

THE FLAGS WERE COMPUTED FROM THE SHEET, NOT COPIED FROM THE GUIDE. The guide
says ChatGPT "should flag" the florist, the photo booth and the bar/registration
buffer, and the arithmetic agrees — but it was run against the real demo file
(Vendor Arrival Times — Saturday Gala, October 22 folder) rather than taken on
trust:

  Florist      arrives 5:00, 90 min of setup, 60 min to doors   -> 30 min short
  Photo booth  arrives 5:00, 60 min of setup, 60 min to doors   -> zero buffer
  Bar          arrives 4:00, 120 min, 120 min to doors          -> zero buffer
  Registration arrives 5:15, 45 min, 45 min to doors            -> zero buffer

One finding the guide does not name is folded into the florist row, because it
is the same conflict and it makes the 30 minutes worse: the caterer is laying
place settings on those same 18 tables until 5:30, so the florist's 90 minutes
cannot even start when they arrive.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "slides")

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
BUBBLE = (236, 231, 220)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
SANSB = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
F = lambda p, s: ImageFont.truetype(p, s)

M = 86
LABEL_H = 146

HOOK = ["Doors at 6pm.", "The florist needs", "90 minutes.", "They arrive at 5."]
HOOK_FLAT = "Doors at 6pm. The florist needs 90 minutes. They arrive at 5."

WHY_HEAD = "Everyone gives you an arrival time."
WHY_BIG = "Nobody checks it against the clock."
WHY_NOTE = ("The pros know their setup time down to the minute. The ones who "
            "skipped the walk-through find out on the day, in the twenty "
            "minutes before doors.")

PROMPT = ("Here is every vendor's arrival time for Saturday's 180-guest gala, "
          "with the setup time each one told me and the space they need: "
          "[paste]. Doors are at 6pm and the stage is closed for AV focus from "
          "3:30 to 4:30. Flag every vendor whose window between arrival and "
          "doors is shorter than the setup time they gave me, or who needs a "
          "space someone else is still using. Then draft a short note asking "
          "each flagged vendor to join a walk-through this week.")

# Computed from the demo sheet. See the module docstring.
FLAGS = [
    ("Florist — 30 minutes short",
     "Arrives 5:00 with 90 minutes of work and 60 minutes until doors. "
     "And the caterer is still laying place settings on those same 18 tables "
     "until 5:30."),
    ("Photo booth — in the bar's corner",
     "5:00 in the ballroom corner by the bar, which is not clear until 6:00, "
     "while the florist works the room around it."),
    ("Bar and registration — no buffer",
     "Both finish at exactly 6:00. One late van and the doors open on a "
     "half-set room."),
]

CLOSER = "Ask for their setup time, then check the clock against it."
CLOSER_SUB = "Every arrival time on that sheet was agreed. Three of them still don't work."


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


def tracked(d, text, font, cx, y, fill, track=7):
    total = sum(d.textlength(c, font=font) + track for c in text) - track
    x = cx - total / 2
    for c in text:
        d.text((x, y), c, font=font, fill=fill)
        x += d.textlength(c, font=font) + track
    return y + int(font.size * 1.4)


def head_label(d, text, y):
    yy = tracked(d, text, F(SANSB, 26), W / 2, y, GREY)
    d.line([(M, yy + 20), (W - M, yy + 20)], fill=RULE, width=2)
    return y + LABEL_H


def footer(d, H, dark=False):
    f = F(SANS, 26)
    t = "@aiforeventplanners"
    d.text(((W - d.textlength(t, font=f)) / 2, H - 70), t, font=f,
           fill=(GREY if not dark else (120, 108, 104)))


def new(H, bg=CREAM):
    img = Image.new("RGB", (W, H), bg)
    return img, ImageDraw.Draw(img)


# ---------------------------------------------------------------- slides

def slide1(H):
    """Typographic cover, same treatment as Oct 21: no photograph exists for
    this piece, so the hook carries it on the dark ground."""
    img, d = new(H, BROWN)
    assert " ".join(HOOK) == HOOK_FLAT, "hook text drifted"
    f = F(SERIF, 64)
    lh = int(64 * 1.32)
    bh = len(HOOK) * lh
    y = (H - bh) // 2 - 30
    assert y > H * 0.12, "hook runs into the top 12% safe zone"
    assert y + bh < H * 0.75, "hook runs into the bottom 25% safe zone"
    for ln in HOOK:
        d.text(((W - d.textlength(ln, font=f)) / 2, y), ln, font=f, fill=ONDARK)
        y += lh
    fk = F(SANSB, 32)
    t = "keep swiping  >"
    d.text(((W - d.textlength(t, font=fk)) / 2, H - 150), t, font=fk, fill=PINKTXT)
    footer(d, H, dark=True)
    return img


def slide2(H):
    img, d = new(H)
    f = F(SERIF, 56)
    body = F(SANS, 38)
    hh = (LABEL_H + measure(d, WHY_HEAD, body, W - 2 * M) + 30
          + measure(d, WHY_BIG, f, W - 2 * M, 1.24) + 44
          + measure(d, WHY_NOTE, body, W - 2 * M))
    y = head_label(d, "WHY IT MATTERS", (H - hh) // 2)
    y = block(d, WHY_HEAD, body, M, y, W - 2 * M, GREY)
    y += 30
    y = block(d, WHY_BIG, f, M, y, W - 2 * M, INK, lh=1.24)
    y += 44
    block(d, WHY_NOTE, body, M, y, W - 2 * M, GREY)
    footer(d, H)
    return img


def slide3(H):
    img, d = new(H)
    f = F(SANS, 34)
    ph = measure(d, PROMPT, f, W - 2 * M - 46, 1.38)
    y = head_label(d, "THE PROMPT", (H - (LABEL_H + ph)) // 2)
    d.line([(M, y - 6), (M, y + ph + 6)], fill=MAROON, width=5)
    block(d, PROMPT, f, M + 46, y, W - 2 * M - 46, INK, lh=1.38)
    footer(d, H)
    return img


def slide4(H):
    """The three flags, each on its own panel with a maroon stub.

    House type under a heading that claims no tool, per Oct 18 and Oct 21.
    The numbers in it came out of the demo sheet, not out of the guide's
    expectation of them — see the module docstring.
    """
    img, d = new(H)
    hf = F(SANSB, 36)
    bf = F(SANS, 31)
    pad = 32
    bw = W - 2 * M
    inner = bw - 2 * pad
    GAP = 26

    heights = []
    for head, body in FLAGS:
        heights.append(pad + measure(d, head, hf, inner, 1.26) + 12
                       + measure(d, body, bf, inner, 1.34) + pad)
    hh = LABEL_H + sum(heights) + GAP * (len(FLAGS) - 1)
    y = head_label(d, "WHAT IT FLAGGED", (H - hh) // 2)

    for (head, body), bh in zip(FLAGS, heights):
        d.rounded_rectangle([M, y, M + bw, y + bh], radius=22, fill=BUBBLE)
        d.rounded_rectangle([M, y + 18, M + 6, y + bh - 18], radius=3, fill=MAROON)
        ty = y + pad
        ty = block(d, head, hf, M + pad, ty, inner, INK, lh=1.26)
        ty += 12
        block(d, body, bf, M + pad, ty, inner, GREY, lh=1.34)
        y += bh + GAP
    footer(d, H)
    return img


def slide5(H):
    img, d = new(H, BROWN)
    f = F(SERIF, 54)
    sub = F(SANS, 32)
    hh = (measure(d, CLOSER, f, W - 2 * M, 1.26) + 40
          + measure(d, CLOSER_SUB, sub, W - 2 * M, 1.3))
    y = (H - hh) // 2 - 20
    y = block(d, CLOSER, f, M, y, W - 2 * M, ONDARK, lh=1.26, align="center")
    y += 40
    block(d, CLOSER_SUB, sub, M, y, W - 2 * M, PINKTXT, lh=1.3, align="center")
    t = "Save this for your next load-in."
    fk = F(SANSB, 28)
    d.text(((W - d.textlength(t, font=fk)) / 2, H - 230), t, font=fk, fill=PINKTXT)
    footer(d, H, dark=True)
    return img


BUILDERS = [slide1, slide2, slide3, slide4, slide5]


def main():
    for name, H in SIZES.items():
        out = os.path.join(OUT, name)
        os.makedirs(out, exist_ok=True)
        for i, fn in enumerate(BUILDERS, 1):
            img = fn(H)
            assert img.size == (W, H)
            img.save(os.path.join(out, f"slide-{i}.jpg"), quality=94)
        print(f"{name}: {len(BUILDERS)} slides at {W}x{H} -> {out}")


if __name__ == "__main__":
    main()
