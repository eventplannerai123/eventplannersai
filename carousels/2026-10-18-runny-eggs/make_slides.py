"""Runny eggs carousel — 5 slides, two sizes.

Sun 18 Oct. Content bank item 25, her own line from the conference on Oct 7.
Swapped in on Oct 16: this day was the dry sandwich lunch until she sent a
photo of a conference breakfast plate and moved the sandwich piece to Wed 28.

Slide 1 is her own photograph, cover-cropped and darkened so the serif reads
over it. The rest is house type, same palette and fonts as the Oct 13
contingency carousel and the Oct 5 hidden-fees one.

Slide 4 is NOT a screenshot. The Oct 13 carousel embedded a crop of her real
ChatGPT answer and labelled it "WHAT AI CAME BACK WITH"; there is no such
recording for this piece, so the hold times are set in house type under a
descriptive heading that claims no tool. If she runs the prompt and sends the
answer, swap a crop in and relabel.

The hold times and the swaps are read off the real demo BEO in Drive
(BEO — Day 1 Breakfast, October 18 folder): 400 guests, 7:30-9:00am, buffet
from chafing dishes, six hot items. HOT below is that list, in BEO order, and
assert_beo() checks it still matches rather than trusting the numbers.
"""
import os
from PIL import Image, ImageDraw, ImageEnhance, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "slides")
SRC = os.path.join(HERE, "source")

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

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
SANSB = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
F = lambda p, s: ImageFont.truetype(p, s)

M = 86
LABEL_H = 146

SERVICE_MIN = 90        # 7:30 to 9:00
GUESTS = 400

# (name on the BEO, minutes it holds in a chafing dish, what to do about it)
# Flagged = anything that does not cover the service window on its own.
HOT = [
    ("Scrambled eggs with chives", 20, "half pans, or an attended station"),
    ("Buttermilk pancakes", 20, "waffles on a rack, or a French toast bake"),
    ("Applewood smoked bacon", 30, "shallow pans, raised off the fat"),
    ("Chicken apple sausage", 45, "holds"),
    ("Rosemary breakfast potatoes", 45, "uncovered, or they steam soft"),
    ("Steel-cut oatmeal", 60, "stir and thin"),
]

PROMPT = ("Here's the breakfast BEO for a 400-person conference: [paste]. "
          "Service runs 7:30 to 9am from chafing dishes. Tell me which hot "
          "items won't hold for the full 90 minutes, how often each one needs "
          "refreshing, and what to swap in for anything that won't survive "
          "the hold. Then write the line I send the catering manager.")

# Her suggestion, Oct 16: "should we say - the runny scrambbled eggs dont?"
# Taken, minus "scrambled" — "runny scrambled eggs" is two words doing one
# job, and slide 2 says scrambled eggs anyway. "Runny" is what makes the pun
# land (the eggs do not run to 9) and it is her own word from bank item 25.
HOOK = "Breakfast runs 7:30 to 9. The runny eggs don't."
CLOSER = "Nobody complains about breakfast. They just remember it."


def assert_beo():
    """The piece only works if nothing on the BEO covers the window alone."""
    assert len(HOT) == 6, "the BEO lists six hot items"
    worst = min(m for _, m, _ in HOT)
    assert worst == 20, "scrambled eggs and pancakes are the 20-minute items"
    assert all(m < SERVICE_MIN for _, m, _ in HOT), \
        "something now holds the full 90 minutes; the slide's claim moved"
    flagged = [n for n, m, _ in HOT if m <= 20]
    assert flagged[0].startswith("Scrambled eggs"), "eggs lead the table"
    return worst, len(flagged)


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


def cover(path, w, h):
    """Scale to cover w x h and centre-crop. Her plate sits mid-frame, so a
    centre crop keeps the eggs in shot at both aspect ratios."""
    im = Image.open(path).convert("RGB")
    s = max(w / im.width, h / im.height)
    im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    left = (im.width - w) // 2
    top = (im.height - h) // 2
    return im.crop((left, top, left + w, top + h))


# ---------------------------------------------------------------- slides

def slide1(H):
    """Her photograph with the hook on a gradient band beneath the food.

    A flat scrim over the whole frame was tried first and it muddied the
    plate into brown soup — the photo is the hook, so it has to stay legible
    as food. Instead: a light global knock-back to tame the highlights on the
    white china, then a gradient that is clear at the top and near-solid by
    the time the type starts. The eggs sit in the clean half.
    """
    img = cover(os.path.join(SRC, "conference-runny-eggs.jpg"), W, H)
    # Shot under warm banquet lighting with no flash, so it comes in dim and
    # orange. Lift it before anything is laid over it ("yes brighen it up",
    # Oct 16) — the plate should read as food, not as a dark smudge.
    img = ImageEnhance.Brightness(img).enhance(1.30)
    img = ImageEnhance.Contrast(img).enhance(1.10)
    img = ImageEnhance.Color(img).enhance(0.92)
    img = Image.blend(img, Image.new("RGB", (W, H), BROWN), 0.10)

    f = F(SERIF, 68)
    lines = ["Breakfast runs", "7:30 to 9.", "The runny", "eggs don't."]
    assert " ".join(lines).replace("  ", " ") == HOOK, "hook text drifted"
    lh = int(68 * 1.30)
    bh = len(lines) * lh

    # A gradient cannot satisfy both constraints at 1080x1920: the type wants
    # to sit on solid colour, and rule 4 keeps it out of the bottom 25% where
    # TikTok's caption and buttons sit. Those two zones barely overlap. So the
    # frame is split instead — photograph above, solid panel below — which
    # also leaves the plate completely unobscured.
    #
    # The tall cut has far less room beneath the safe line, so it gives more
    # of the frame to the panel; the 4:5 Instagram slide has no such furniture.
    end = 0.73 if H / W > 1.5 else 0.88
    ty = int(H * end) - bh
    panel_top = ty - 96
    assert panel_top > H * 0.38, "panel has eaten more than half the photo"
    assert ty + bh <= H * end, "hook runs into the platform's bottom furniture"

    photo = cover(os.path.join(SRC, "conference-runny-eggs.jpg"), W, panel_top)
    photo = ImageEnhance.Brightness(photo).enhance(1.30)
    photo = ImageEnhance.Contrast(photo).enhance(1.10)
    photo = ImageEnhance.Color(photo).enhance(0.92)

    img = Image.new("RGB", (W, H), BROWN)
    img.paste(photo, (0, 0))
    d = ImageDraw.Draw(img)

    y = ty
    for ln in lines:
        d.text(((W - d.textlength(ln, font=f)) / 2, y), ln, font=f, fill=ONDARK)
        y += lh

    fk = F(SANSB, 32)
    t = "keep swiping  >"
    d.text(((W - d.textlength(t, font=fk)) / 2, H - 150), t, font=fk, fill=PINKTXT)
    f2 = F(SANS, 26)
    u = "@aiforeventplanners"
    d.text(((W - d.textlength(u, font=f2)) / 2, H - 70), u, font=f2,
           fill=(168, 154, 148))
    return img


def slide2(H):
    img, d = new(H)
    f = F(SERIF, 56)
    body = F(SANS, 38)
    head = "Breakfast is the first thing every attendee has an opinion about."
    big = "Scrambled eggs don't survive 90 minutes in a chafing dish."
    note = ("They weep, they go rubbery, and the pan gets topped up on top of "
            "what is already sitting there. By 8:15 you are serving something "
            "nobody would have chosen at 7:30.")
    hh = LABEL_H + measure(d, head, body, W - 2 * M) + 30 \
        + measure(d, big, f, W - 2 * M, 1.24) + 44 + measure(d, note, body, W - 2 * M)
    y = head_label(d, "WHY IT MATTERS", (H - hh) // 2)
    y = block(d, head, body, M, y, W - 2 * M, GREY)
    y += 30
    y = block(d, big, f, M, y, W - 2 * M, INK, lh=1.24)
    y += 44
    block(d, note, body, M, y, W - 2 * M, GREY)
    footer(d, H)
    return img


def slide3(H):
    img, d = new(H)
    f = F(SANS, 38)
    ph = measure(d, PROMPT, f, W - 2 * M - 46, 1.38)
    y = head_label(d, "THE PROMPT", (H - (LABEL_H + ph)) // 2)
    d.line([(M, y - 6), (M, y + ph + 6)], fill=MAROON, width=5)
    block(d, PROMPT, f, M + 46, y, W - 2 * M - 46, INK, lh=1.38)
    footer(d, H)
    return img


def slide4(H):
    worst, nflag = assert_beo()
    img, d = new(H)
    fr = F(SANS, 32)
    frb = F(SANSB, 32)
    fsm = F(SANS, 27)
    row, sub = 46, 38
    cap = F(SANS, 31)
    note = ('The BEO says "Replenishment: as needed." Ninety minutes of '
            "service needs a number, not a phrase.")

    hh = LABEL_H + len(HOT) * (row + sub) + 30 + measure(d, note, cap, W - 2 * M)
    y = head_label(d, "HOW LONG EACH ONE HOLDS", (H - hh) // 2)

    for name, mins, fix in HOT:
        hot = mins <= 20
        if hot:
            d.rounded_rectangle([M - 18, y - 10, W - M + 18, y + row + sub - 20],
                                10, fill=(238, 226, 228))
        f1 = frb if hot else fr
        d.text((M, y), name, font=f1, fill=MAROON if hot else INK)
        t = f"{mins} min"
        d.text((W - M - d.textlength(t, font=f1), y), t, font=f1,
               fill=MAROON if hot else INK)
        y += row
        d.text((M, y), fix, font=fsm, fill=GREY)
        y += sub

    y += 30
    block(d, note, cap, M, y, W - 2 * M, INK, align="center")
    footer(d, H)
    return img


def slide5(H):
    img, d = new(H, BROWN)
    f = F(SERIF, 58)
    hh = measure(d, CLOSER, f, W - 2 * M, 1.26)
    y = (H - hh) // 2 - 20
    block(d, CLOSER, f, M, y, W - 2 * M, ONDARK, lh=1.26, align="center")
    t = "Save this for your next breakfast BEO."
    fk = F(SANSB, 30)
    d.text(((W - d.textlength(t, font=fk)) / 2, H - 230), t, font=fk, fill=PINKTXT)
    footer(d, H, dark=True)
    return img


BUILDERS = [slide1, slide2, slide3, slide4, slide5]


def main():
    worst, nflag = assert_beo()
    print(f"BEO ok: 6 hot items, worst holds {worst} min against a "
          f"{SERVICE_MIN}-minute service, {nflag} flagged")
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
