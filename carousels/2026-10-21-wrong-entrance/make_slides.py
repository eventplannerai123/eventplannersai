"""Wrong entrance carousel — 5 slides, two sizes.

Wed 21 Oct. Content bank item 16, her own line: "They were told exactly which
entrance. They still used the wrong one."

Same palette, fonts and furniture as the Oct 18 runny eggs carousel and the
Oct 13 contingency one.

SLIDE 4 IS HOUSE TYPE, NOT A SCREENSHOT, and its heading says so. The Oct 13
carousel embedded a crop of her real ChatGPT answer under "WHAT AI CAME BACK
WITH"; there is no recording for this piece, so the Oct 18 precedent applies —
set the output in house type under a heading that claims no particular tool.
The text below was generated here from the demo invitation, which is a real
thing an AI wrote from that file, so "THE TEXT IT WROTE" is honest. If she
runs the prompt herself and sends a recording, swap a crop in and relabel.

THE VENUE IS INVENTED AND THAT IS THE POINT. The demo invitation in Drive
(Invitation — Autumn Patrons Reception, October 21 folder) is for "The Harrow
Museum of Design", which does not exist — the brief says "made-up museum, no
real venue". So every transit and parking line is unconfirmable, and the
prompt's last clause ("tell me which ones you couldn't confirm") is what the
slide turns on. Showing plausible subway lines without that flag would be the
piece teaching the opposite of what it says.
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

HOOK = ["They were told", "exactly which", "entrance.", "They still used", "the wrong one."]
HOOK_FLAT = "They were told exactly which entrance. They still used the wrong one."

WHY_HEAD = "Guests don't read the invitation."
WHY_BIG = "They head for the main doors."
WHY_NOTE = ("At a big museum the front steps ARE the entrance, as far as a "
            "guest is concerned. The line about the side gate was in "
            "paragraph four, three weeks ago, on a phone.")

PROMPT = ("Here's the invitation for an evening reception at a large museum: "
          "[paste]. Guests must use the side event entrance, not the main "
          "entrance. Write a “know before you go” text to send the day "
          "before and the morning of. Put the entrance in the first line with "
          "a landmark to look for, then the nearest subway, train and bus "
          "stops and which exit to use, then the closest parking garages. "
          "Nothing else. Check every transit and parking detail against the "
          "museum's own directions page and tell me which ones you couldn't "
          "confirm.")

# Written from the demo invitation. The entrance leads, as the prompt demands.
MSG_LEAD = "Tomorrow, 6:30pm — the Harrow."
MSG_BODY = ("Use the GARDEN GATE on the side of the building, by the copper "
            "beech. The front steps are closed all evening.")
MSG_REST = "Then: subway, bus and parking."
FLAG = ("Couldn't confirm: every transit and parking line. "
        "The museum has no public directions page.")

CLOSER = "Put the entrance in the first line."
CLOSER_SUB = "And on the day: one person at the wrong door."


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
    """Typographic cover. There is no photograph for this piece — the Oct 18
    cover was her own plate, and nothing equivalent exists here, so the line
    carries it on the dark ground used for the closing slide."""
    img, d = new(H, BROWN)
    assert " ".join(HOOK) == HOOK_FLAT, "hook text drifted"
    f = F(SERIF, 62)
    lh = int(62 * 1.32)
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
    """The text it wrote, as a message bubble, with the entrance leading.

    The flag line is not decoration: the venue is invented, so nothing in the
    transit section could be checked, and the prompt asked to be told that.
    It is set in maroon under the bubble so it reads as the output's own
    caveat rather than ours.
    """
    img, d = new(H)
    lead_f = F(SANSB, 38)
    body_f = F(SANS, 34)
    rest_f = F(SANS, 34)
    flag_f = F(SANS, 30)

    pad = 44
    bw = W - 2 * M
    inner = bw - 2 * pad
    bh = (pad + measure(d, MSG_LEAD, lead_f, inner, 1.3) + 18
          + measure(d, MSG_BODY, body_f, inner, 1.34) + 22
          + measure(d, MSG_REST, rest_f, inner, 1.34) + pad)

    hh = LABEL_H + bh + 40 + measure(d, FLAG, flag_f, bw, 1.34)
    y = head_label(d, "THE TEXT IT WROTE", (H - hh) // 2)

    d.rounded_rectangle([M, y, M + bw, y + bh], radius=28, fill=BUBBLE)
    ty = y + pad
    ty = block(d, MSG_LEAD, lead_f, M + pad, ty, inner, INK, lh=1.3)
    ty += 18
    ty = block(d, MSG_BODY, body_f, M + pad, ty, inner, INK, lh=1.34)
    ty += 22
    block(d, MSG_REST, rest_f, M + pad, ty, inner, GREY, lh=1.34)

    y += bh + 40
    block(d, FLAG, flag_f, M, y, bw, MAROON, lh=1.34)
    footer(d, H)
    return img


def slide5(H):
    img, d = new(H, BROWN)
    f = F(SERIF, 58)
    sub = F(SANS, 34)
    hh = (measure(d, CLOSER, f, W - 2 * M, 1.26) + 40
          + measure(d, CLOSER_SUB, sub, W - 2 * M, 1.3))
    y = (H - hh) // 2 - 20
    y = block(d, CLOSER, f, M, y, W - 2 * M, ONDARK, lh=1.26, align="center")
    y += 40
    block(d, CLOSER_SUB, sub, M, y, W - 2 * M, PINKTXT, lh=1.3, align="center")
    t = "Save this before your next invitation goes out."
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
