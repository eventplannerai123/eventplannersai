"""Fri 20 Nov — overlay cards for the coloring book giveaway Reel.

1080x1920. Unlike the four-steps Reel, the footage here is a full-frame
PORTRAIT phone clip of hers, so the overlays are floating bands rather than a
panel with a hole in it: a lavender #CECBF6 band with deep purple #3C3489
Poppins, and full-frame cards only at the end.

The band sits high, clear of the two books in the middle of the frame and of
the safe zones — nothing important in the top 12%, the bottom 25% or the
right 15%, where the app's own furniture sits.

The lines are the guide's, not ours: the Fri 20 block gives the first-two-
seconds overlay and the takeaway overlay, and the two cuts differ only in the
takeaway, because TikTok has no bio link to point at.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "build", "cards")
FONTS = os.path.join(HERE, "build", "fonts")

W, H = 1080, 1920
LAVENDER = (206, 203, 246)
PURPLE = (60, 52, 137)

P400 = os.path.join(FONTS, "Poppins-400.ttf")
P700 = os.path.join(FONTS, "Poppins-700.ttf")
F = lambda p, s: ImageFont.truetype(p, s)

M = 72
HANDLE = "@aiforeventplanners"

HOOK = "2 free copies.\nHere’s how to win one."
END_IG = "Comment the bride\nyou’d give it to."
END_TT = "Enter on\nmy Instagram."

BAND_TOP = 250          # under the top 12% (230px), clear of the books


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


def hook_card():
    """A lavender band high in the frame, over footage that keeps playing."""
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    f = F(P700, 74)
    lines = HOOK.split("\n")
    step = int(74 * 1.22)
    pad = 46
    bh = len(lines) * step + pad * 2 - int(74 * 0.22)
    d.rounded_rectangle([M - 28, BAND_TOP, W - M + 28, BAND_TOP + bh],
                        radius=34, fill=LAVENDER + (242,))
    y = BAND_TOP + pad - 8
    for ln in lines:
        d.text(((W - d.textlength(ln, font=f)) / 2, y), ln, font=f, fill=PURPLE)
        y += step
    return img


def end_card(text):
    """Full-frame card: nothing is playing underneath it."""
    img = Image.new("RGBA", (W, H), LAVENDER + (255,))
    d = ImageDraw.Draw(img)
    for px in range(96, 47, -2):
        f = F(P700, px)
        lines = []
        for para in text.split("\n"):
            lines += wrap(d, para, f, W - 2 * M)
        if len(lines) == len(text.split("\n")):
            break
    else:
        raise SystemExit("the end card does not fit")
    step = int(px * 1.20)
    y = (H - len(lines) * step) // 2
    for ln in lines:
        d.text(((W - d.textlength(ln, font=f)) / 2, y), ln, font=f, fill=PURPLE)
        y += step
    hf = F(P400, 26)
    d.text(((W - d.textlength(HANDLE, font=hf)) / 2, H - 92), HANDLE,
           font=hf, fill=PURPLE)
    return img, px


def check():
    # Her Nov 14 rule: the closing line has to follow from the piece. This one
    # is the giveaway itself, so the ask is the entry mechanic and nothing else.
    assert "BUDGET" not in (HOOK + END_IG + END_TT), \
        "no tracker CTA on a giveaway piece"
    assert "link in bio" not in END_TT.lower(), "never 'link in bio' on TikTok"
    assert "Instagram" in END_TT, "TikTok sends them to the Instagram post"
    assert "Comment" in END_IG, "Instagram's ask is the comment"
    assert HOOK.strip()[0].isdigit(), "the hook opens on the number of copies"
    assert BAND_TOP >= int(H * 0.12), "the band must clear the top 12%"
    print("checks pass: hook opens on a number, band clears the top 12%, "
          "Instagram asks for the comment and TikTok points at Instagram")


def main():
    check()
    os.makedirs(OUT, exist_ok=True)
    hook_card().save(os.path.join(OUT, "hook.png"))
    print("hook.png")
    for name, text in (("end-instagram", END_IG), ("end-tiktok", END_TT)):
        img, px = end_card(text)
        img.save(os.path.join(OUT, f"{name}.png"))
        print(f"{name}.png  {px}px")


if __name__ == "__main__":
    main()
