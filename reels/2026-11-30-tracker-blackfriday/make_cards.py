"""Mon 30 Nov — overlay cards for the Vendor Payment System Black Friday Reel.

Same frame as the Thu 19 "four steps" Reel: 1080x1920, lavender #CECBF6, deep
purple #3C3489, Poppins, the laptop capture in a 1080x980 panel at y=450.

PAYOFF FIRST: the finished, coloured tracker is on screen from frame one with
"$17 until midnight." over it. The price card then states the offer in full
(the code and the deadline), because the code is the one thing the viewer
has to be able to read and act on.

**THE CLOSING LINE IS CHECKED AGAINST THE PIECE, and it passes** (her Nov 14
rule): the Reel sells a money product, the CTA is the product's own and the
Mon 30 block specifies it. The assert is the inverse of the BEO generator's.

**THE DEADLINE IS A DISCOUNT CODE'S REAL ONE.** BLACKFRIDAY runs to
2026-12-01T04:59Z, which is 11:59pm Eastern Mon 30 Nov. "Until midnight" is
the guide's own wording and is within a minute of that; the price card says
11:59pm so the card is exact even where the voiceover rounds.
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
P600 = os.path.join(FONTS, "Poppins-600.ttf")
P700 = os.path.join(FONTS, "Poppins-700.ttf")
F = lambda p, s: ImageFont.truetype(p, s)
M = 72
HANDLE = "@aiforeventplanners"
PANEL_Y, PANEL_H = 450, 980

HOOK = "$17 until midnight."
STEP_B1 = "One paste fills it."
STEP_B2 = "Paid. Due this week. Overdue."
PRICE_WAS, PRICE_NOW = "$24", "$17"
PRICE_CODE = "Code BLACKFRIDAY"
PRICE_NOTE = "Ends tonight, 11:59pm Eastern"
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
    d.text(((W - d.textlength(HANDLE, font=hf)) / 2, H - 92), HANDLE, font=hf, fill=PURPLE)


def over_panel(text, size):
    img, d = base()
    d.rectangle([0, PANEL_Y, W, PANEL_Y + PANEL_H], fill=(0, 0, 0, 0))
    f = F(P700, size)
    lines = wrap(d, text, f, W - 2 * M)
    step = int(size * 1.17)
    y = PANEL_Y - 44 - len(lines) * step
    for ln in lines:
        d.text((M, y), ln, font=f, fill=PURPLE)
        y += step
    handle(d)
    return img


def centred(d, text, font, y, fill=PURPLE):
    d.text(((W - d.textlength(text, font=font)) / 2, y), text, font=font, fill=fill)


def price_card():
    img, d = base()
    centred(d, PRICE_WAS, F(P700, 150), 520)
    wf = F(P700, 150)
    tw = d.textlength(PRICE_WAS, font=wf)
    y = 520 + 150 * 0.72
    d.line([(W - tw) / 2 - 8, y, (W + tw) / 2 + 8, y], fill=PURPLE, width=10)
    centred(d, PRICE_NOW, F(P700, 340), 700)
    centred(d, PRICE_CODE, F(P700, 82), 1130)
    centred(d, PRICE_NOTE, F(P600, 46), 1260)
    handle(d)
    return img


def end_card(text):
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
        centred(d, ln, f, y)
        y += step
    handle(d)
    return img, px


def check():
    assert "BUDGET" in END_IG and "BUDGET" in END_TT, "the CTA is the piece"
    assert "link in bio" not in END_TT.lower(), "never 'link in bio' on TikTok"
    assert "on my Instagram" in END_TT
    assert URL_TT.startswith("aiforeventplanners") and ".gumroad.com" in URL_TT
    # $24 less $7 is $17; the code is $7 off, never a percentage.
    assert int(PRICE_WAS[1:]) - 7 == int(PRICE_NOW[1:]) == 17
    assert "%" not in (HOOK + PRICE_CODE + PRICE_NOTE), "the code is $7 off, not a percentage"
    assert "BLACKFRIDAY" in PRICE_CODE
    assert HOOK.startswith("$"), "hook opens on the number"
    print("checks pass: $24 - $7 = $17, no percentage, BUDGET on both cuts, TikTok says 'on my Instagram'")


def main():
    check()
    os.makedirs(OUT, exist_ok=True)
    over_panel(HOOK, 96).save(os.path.join(OUT, "hook.png"))
    over_panel(STEP_B1, 82).save(os.path.join(OUT, "b1.png"))
    over_panel(STEP_B2, 70).save(os.path.join(OUT, "b2.png"))
    price_card().save(os.path.join(OUT, "price.png"))
    for name, text in (("end-instagram", END_IG), ("end-tiktok", END_TT), ("url-tiktok", URL_TT)):
        img, px = end_card(text)
        img.save(os.path.join(OUT, f"{name}.png"))
        print(name, px)


if __name__ == "__main__":
    main()
