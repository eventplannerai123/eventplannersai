"""Thu 19 Nov — overlay cards for the Vendor Payment System Reel ("four steps").

1080x1920, lavender #CECBF6 ground, deep purple #3C3489 type, Poppins. Each
card is a full frame rather than a floating label, because the footage is a
LANDSCAPE laptop capture: it sits in a 1080x950 panel in the middle of the
frame and the card carries everything above and below it.

The step cards are the guide's own: a big numbered badge and one line each,
"Make a copy" / "Paste one prompt" / "Paste the table" / "Upload the contract".

**THE CLOSING LINE IS CHECKED AGAINST THE PIECE, and it passes.** Her Nov 14
rule pulled "Comment BUDGET" off the insurance Reel and the BEO redo because
neither was about money. This one IS the tracker: the Reel exists to sell the
Vendor Payment System, the CTA is the product's own, and the guide's Thu 19
block specifies it. So the assert here is the opposite of the Nov 17 BEO
generator's — this piece MUST carry it.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "build", "cards")
FONTS = os.path.join(HERE, "build", "fonts")

W, H = 1080, 1920
LAVENDER = (206, 203, 246)
PURPLE = (60, 52, 137)
WHITE = (255, 255, 255)

P400 = os.path.join(FONTS, "Poppins-400.ttf")
P600 = os.path.join(FONTS, "Poppins-600.ttf")
P700 = os.path.join(FONTS, "Poppins-700.ttf")
F = lambda p, s: ImageFont.truetype(p, s)

M = 72
HANDLE = "@aiforeventplanners"

# The panel the footage sits in. Everything else is placed around it.
PANEL_Y, PANEL_H = 500, 950

STEPS = [
    (1, "Make a copy"),
    (2, "Paste one prompt"),
    (3, "Paste the table"),
    (4, "Upload the contract"),
]

HOOK = "4 steps. Every vendor payment tracked."
END_IG = "Comment BUDGET\nand I’ll send it to you."
END_TT = "Comment BUDGET\non my Instagram."
URL_TT = "aiforeventplanners\n.gumroad.com"


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


def base():
    img = Image.new("RGBA", (W, H), LAVENDER + (255,))
    return img, ImageDraw.Draw(img)


def handle(d):
    hf = F(P400, 26)
    d.text(((W - d.textlength(HANDLE, font=hf)) / 2, H - 92), HANDLE,
           font=hf, fill=PURPLE)


def step_card(n, line):
    """A numbered badge and its one line, above the panel; handle below it."""
    img, d = base()
    # Punch the panel out so the footage shows through.
    d.rectangle([0, PANEL_Y, W, PANEL_Y + PANEL_H], fill=(0, 0, 0, 0))

    r = 64
    cx, cy = M + r, PANEL_Y - 230
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=PURPLE)
    nf = F(P700, 72)
    t = str(n)
    d.text((cx - d.textlength(t, font=nf) / 2, cy - 72 * 0.74), t, font=nf,
           fill=LAVENDER)

    lf = F(P700, 72)
    lines = wrap(d, line, lf, W - 2 * M - 2 * r - 36)
    y = cy - (len(lines) * 84) / 2 + 6
    for ln in lines:
        d.text((cx + r + 36, y), ln, font=lf, fill=PURPLE)
        y += 84

    handle(d)
    return img


def hook_card():
    """The payoff beat: no number, the guide's hook line above the panel."""
    img, d = base()
    d.rectangle([0, PANEL_Y, W, PANEL_Y + PANEL_H], fill=(0, 0, 0, 0))
    hf = F(P700, 82)
    lines = wrap(d, HOOK, hf, W - 2 * M)
    y = PANEL_Y - 60 - len(lines) * 96
    for ln in lines:
        d.text((M, y), ln, font=hf, fill=PURPLE)
        y += 96
    handle(d)
    return img


def end_card(text):
    """Full-frame CTA. No panel: nothing is playing underneath it."""
    img, d = base()
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
    handle(d)
    return img, px


def check():
    # Her Nov 14 rule, applied the other way round: this piece is the tracker,
    # so the CTA belongs and its absence is the error.
    assert "BUDGET" in END_IG and "BUDGET" in END_TT, "the CTA is the piece"
    assert "link in bio" not in END_TT.lower(), "never 'link in bio' on TikTok"
    assert "on my Instagram" in END_TT, "TikTok has no bio link"
    # The Thu 19 block asks the TikTok cut to end on the address in large
    # text, because TikTok has no bio link to point at. Split at the dot so it
    # sets large rather than shrinking to fit one line, as the Nov 5 cut did.
    assert URL_TT.startswith("aiforeventplanners") and ".gumroad.com" in URL_TT
    assert len(STEPS) == 4 and [n for n, _ in STEPS] == [1, 2, 3, 4]
    # The hook names a number in its first words, per the November growth rule.
    assert HOOK.strip()[0].isdigit(), "the hook has to open on a number"
    print("checks pass: 4 steps, hook opens on a number, BUDGET on both cuts, "
          "TikTok says 'on my Instagram'")


def main():
    check()
    os.makedirs(OUT, exist_ok=True)
    hook_card().save(os.path.join(OUT, "hook.png"))
    print("hook.png")
    for n, line in STEPS:
        step_card(n, line).save(os.path.join(OUT, f"step{n}.png"))
        print(f"step{n}.png  {line}")
    for name, text in (("end-instagram", END_IG), ("end-tiktok", END_TT),
                       ("url-tiktok", URL_TT)):
        img, px = end_card(text)
        img.save(os.path.join(OUT, f"{name}.png"))
        print(f"{name}.png  {px}px")


if __name__ == "__main__":
    main()
