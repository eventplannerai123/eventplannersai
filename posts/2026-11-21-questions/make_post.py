"""Sat 21 Nov, 6:30pm — "Questions I get asked at every event."

Planner-life post, content bank 35, built for shares and comments. The Sat 21
CLAUDE CODE line specifies the look exactly: deep purple #3C3489 ground, the
title in Poppins SemiBold white, the numbered questions in Poppins Regular in
lavender #CECBF6, and the last one set apart.

THE QUESTIONS ARE HERS OR THE BANK'S, NEVER INVENTED. Her line asks for 6 to
8 real ones by Thu 19. Until those arrive this builds the bank's default —
three questions plus the one nobody asks — and QUESTIONS below is the only
thing that changes when she sends her list. The guide's words: "Use Sahiba's
questions exactly; never invent one."

The last question is set apart because it is the whole point of the piece: it
sits lower, in white rather than lavender, after a rule and the small line
that introduces it.
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

TITLE = "Questions I get\nasked at every\nevent."

# From the content bank, until she sends her own list.
QUESTIONS = [
    "Where’s the bathroom?",
    "What’s the Wi-Fi password?",
    "Are you with the family?",
]
LAST_INTRO = "And the one nobody ever asks the planner:"
LAST = "Did you eat?"

FROM_HER = False   # flip when QUESTIONS is her list


def build():
    img = Image.new("RGB", (W, H), PURPLE)
    d = ImageDraw.Draw(img)

    tf = F(P600, 88)
    qf = F(P400, 50)
    nf = F(P600, 50)
    intro_f = F(P400, 38)
    last_f = F(P600, 76)

    title_lines = TITLE.split("\n")
    tstep = int(88 * 1.17)
    # Measured before anything is drawn, so three bank questions and eight of
    # hers both land centred rather than stacked at the top.
    total = (len(title_lines) * tstep + 90
             + len(QUESTIONS) * 108
             + 60 + 54 + 66 + int(76 * 1.2))
    top, bottom = 150, H - 170
    y = top + ((bottom - top) - total) // 2

    for line in title_lines:
        d.text((M, y), line, font=tf, fill=WHITE)
        y += tstep

    y += 90
    for i, q in enumerate(QUESTIONS, 1):
        d.text((M, y), f"{i}.", font=nf, fill=WHITE)
        d.text((M + 70, y), q, font=qf, fill=LAVENDER)
        y += 108

    y += 60
    d.line([(M, y), (W - M, y)], fill=LAVENDER, width=2)
    y += 54

    d.text((M, y), LAST_INTRO, font=intro_f, fill=LAVENDER)
    y += 66
    d.text((M, y), LAST, font=last_f, fill=WHITE)
    y += int(76 * 1.2)

    hf = F(P400, 24)
    d.text(((W - d.textlength(HANDLE, font=hf)) / 2, H - 76), HANDLE,
           font=hf, fill=LAVENDER)
    return img, y


def check():
    assert 3 <= len(QUESTIONS) <= 7, "three from the bank, up to seven of hers"
    assert LAST == "Did you eat?", "the piece ends on the one nobody asks"
    joined = " ".join(QUESTIONS + [TITLE, LAST_INTRO, LAST]).lower()
    for banned in ("prompt", "chatgpt", "claude", "comment ", "link in bio"):
        assert banned not in joined, f"no demo and no CTA: found {banned!r}"
    print(f"checks pass: {len(QUESTIONS)} questions"
          f" ({'hers' if FROM_HER else 'the content bank default'})"
          ", ending on the one nobody asks")


def main():
    check()
    os.makedirs(OUT, exist_ok=True)
    img, end_y = build()
    assert img.size == (W, H)
    assert end_y < H - 180, "the block runs into the handle"
    p = os.path.join(OUT, "questions.jpg")
    img.save(p, quality=95)
    print(f"text ends y={end_y} -> {os.path.basename(p)}")


if __name__ == "__main__":
    main()
