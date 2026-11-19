"""Sun 22 Nov — "One plate left and a line. How embarrassing."

Six slides, content bank 38, third in the conference catering series after
runny eggs and dry sandwiches. Brand system: lavender #CECBF6, deep purple
#3C3489, Poppins, EP + star wordmark, numbered badge, bottom bar. Poppins has
no glyph at U+2726, so the star is a polygon.

ONE SET AT 1080x1920 — the Nov 8 format rule sends Instagram and Facebook a
slide Reel and TikTok the same slides as a photo carousel.

**SLIDE 1 IS HER PHOTO**, sent Thu 19: two chafing trays scraped down to
smears of egg, a bacon tray with three rashers left, tongs lying in it, and a
stack of clean plates beside them. The guide described a different file that
turned out never to have existed; this is better, and it is hers.

It is landscape, 1448x1086, so it sets as a full-width panel with the overlay
above it rather than a 9:16 crop that would throw away most of the width.
**One light blur** goes on the figure at the right edge — no face is in frame
and nothing identifies them, but a stranger in a public post gets softened
anyway. **The source stays out of this repo**, which is public; it lives in
Drive `November 22` and this reads a scratch copy.

**SLIDE 5 IS DERIVED FROM THE BEO, NOT PASTED OUT OF AN AI.** The prompt was
run for real against the file's text (claude-opus-5-5 on the ElevenLabs flow,
Nov 19) to check the piece's claim stands up, but that node's text cannot be
read back from this session, so the sheet here is composed from the BEO's own
values and every figure is recomputed in `make_week6.py` and asserted: the
seven stations with their service windows and refresh times, the busiest hour,
the five walks, and the two refreshes longer than the gap between them. The
slide does not claim an AI wrote it, and her YOU line is to check slide 5 —
which is exactly the right check.

NO VENUE, NO CLIENT, NO EMPLOYER. Thorne Hall and Marchetti Hospitality are
invented, and the photo names nobody.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "slides")
FONTS = os.path.join(HERE, "build", "fonts")
STEM = "2026-11-22-one-plate-left"

W, H = 1080, 1920

LAVENDER = (206, 203, 246)
PURPLE = (60, 52, 137)
HAIRLINE = (176, 172, 228)

P400 = os.path.join(FONTS, "Poppins-400.ttf")
P600 = os.path.join(FONTS, "Poppins-600.ttf")
P700 = os.path.join(FONTS, "Poppins-700.ttf")
F = lambda p, s: ImageFont.truetype(p, s)

M = 72
HANDLE = "@aiforeventplanners"

PHOTO = os.environ.get("ONE_PLATE_SRC", "/tmp/claude-0/-home-user-eventplannersai/"
                       "4079a8b4-9eb7-5c73-8b20-b79d77bad268/scratchpad/photo/"
                       "event-one-plate-left.jpg")
# The figure stands in the right eighth of the frame: no face, no lanyard,
# nothing identifying. A blur patch was tried first and read exactly as the
# Oct 10 note warns — a censor smudge with a hard rectangular edge — so the
# strip is CROPPED OFF instead. Nothing is lost but a second chafing dish and
# a stretch of marble. Fractions of the source, so a re-crop cannot miss it.
CROP = (0.0, 0.0, 0.845, 1.0)

# The guide's own prompt, word for word, so the slide and the caption cannot
# drift apart.
PROMPT = ("Here\u2019s the BEO and the run of show for a 300-person evening "
          "reception: [paste]. Build a food and beverage captain sheet: every "
          "station and bar, when it opens and closes, the refresh trigger "
          "(call the kitchen at half full, not empty), how long each refresh "
          "takes, the kitchen and banquet captain contacts, and a walk "
          "schedule every 15 minutes during the busiest hour. Flag any "
          "station where the refresh takes longer than the gap between guest "
          "waves.")

# Read out of the BEO, not typed from the brief. make_week6.check_beo()
# recomputes all of it from the same figures the PDF prints.
SHEET = [
    ("Raw bar",                     "6:00 - 8:00pm", 40),
    ("Carving station",             "6:30 - 8:30pm", 15),
    ("Pasta station",               "6:00 - 8:30pm", 20),
    ("Crudit\u00e9s and cheese",        "6:00 - 9:00pm", 35),
    ("Dessert station",             "7:30 - 9:00pm", 20),
    ("Main bar",                    "6:00 - 9:00pm", 10),
    ("Satellite bar",               "6:30 - 8:30pm", 10),
]
# 30 minutes is the gap between the first two guest waves, and that is what
# decides a flag: a refresh longer than it leaves the station half-built when
# the next hundred walk in. The walks themselves are every 15 minutes.
WAVE_GAP = 30
WALK_EVERY = 15
WALKS = "6:30  ·  6:45  ·  7:00  ·  7:15  ·  7:30pm"
BUSIEST = "Busiest hour 6:30 - 7:30pm: all 300 are in by 7:15, and six of the seven are open."
CONTACTS = "Kitchen ext. 214  ·  Banquet captain (212) 555-0148  ·  Radio channel 4"
FLAG = "Raw bar 40 min. Crudit\u00e9s 35 min."
FLAG_SUB = "Longer than the 30 minutes between waves, so call those two in before the next one lands."

SLIDES = [
    dict(n=1, photo=True,
         head="One plate left and a line.\nHow embarrassing.",
         sub="300 guests, seven stations and bars, nobody watching them."),

    dict(n=2, head="Every event needs\na food and beverage\ncaptain.",
         body="Not the caterer. Someone of yours, whose whole job for three "
              "hours is the food: walking the room, counting what is left, "
              "and calling it in before a guest sees an empty tray."),

    dict(n=3, head="What the captain\nactually does.",
         items=[
             ("Walks every station", "", "On a loop, not when someone complains."),
             ("Calls at half full", "", "Half full, never empty \u2014 a refresh takes "
              "time, and the queue forms while you wait."),
             ("Knows the refresh times", "", "They are in the BEO. Forty minutes "
              "and fifteen are not the same job."),
             ("Has the backup ready", "", "Which station covers which, and who "
              "to call when the kitchen cannot."),
         ],
         foot="One person, one loop, for three hours."),

    dict(n=4, label="The prompt",
         head="Ask it for the\nwalking order, and\nwhat it cannot cover.",
         quote=PROMPT),

    dict(n=5, card=True),

    dict(n=6, head="Call the kitchen\nat half full,\nnot empty.",
         sub="Save this for your next reception."),
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


def chrome(img, d, H, n):
    """Numbered badge, then the bottom bar: rule, EP + star wordmark, handle."""
    bf = F(P700, 30)
    r = 32
    cx, cy = M + r, 118
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=PURPLE, width=3)
    t = str(n)
    d.text((cx - d.textlength(t, font=bf) / 2, cy - 30 * 0.78), t, font=bf, fill=PURPLE)

    d.line([(M, H - 150), (W - M, H - 150)], fill=HAIRLINE, width=2)
    wf, hf = F(P700, 34), F(P400, 24)
    ep_w = d.textlength("EP", font=wf)
    star_r = 13
    ex, ey = (W - (ep_w + 10 + star_r * 2)) / 2, H - 112
    d.text((ex, ey), "EP", font=wf, fill=PURPLE)
    sx, sy = ex + ep_w + 10 + star_r, ey + 34 * 0.62
    waist = star_r * 0.30
    d.polygon([(sx, sy - star_r), (sx + waist, sy - waist), (sx + star_r, sy),
               (sx + waist, sy + waist), (sx, sy + star_r), (sx - waist, sy + waist),
               (sx - star_r, sy), (sx - waist, sy - waist)], fill=PURPLE)
    d.text(((W - d.textlength(HANDLE, font=hf)) / 2, H - 64), HANDLE, font=hf, fill=PURPLE)


def blocks(d, s, head_px):
    """Every text block in render order: (font, lines, step, gap, indent, rule)."""
    maxw = W - 2 * M
    out = []

    if s.get("label"):
        lp = max(24, int(head_px * 0.32))
        lf = F(P600, lp)
        out.append((lf, [s["label"]], int(lp * 1.30), 0, 0, True))

    hf = F(P700, head_px)
    head_lines = []
    for para in s["head"].split("\n"):
        head_lines += wrap(d, para, hf, maxw)
    out.append((hf, head_lines, int(head_px * 1.18), 30 if s.get("label") else 0,
                0, False))
    wrapped = len(head_lines)

    if s.get("body"):
        bp = max(26, int(head_px * 0.44))
        bf = F(P400, bp)
        out.append((bf, wrap(d, s["body"], bf, maxw), int(bp * 1.38), 36, 0, False))

    if s.get("quote"):
        qp = max(25, int(head_px * 0.40))
        qf = F(P400, qp)
        out.append((qf, wrap(d, "“" + s["quote"] + "”", qf, maxw - 34),
                    int(qp * 1.42), 38, 34, False))

    if s.get("items"):
        np_ = max(25, int(head_px * 0.38))
        nf, af = F(P600, np_), F(P400, max(22, int(np_ * 0.86)))
        for i, (name, amount, why) in enumerate(s["items"]):
            label = f"{name}  {amount}".rstrip()
            out.append((nf, [label], int(np_ * 1.26), 36 if i == 0 else 22, 0, False))
            out.append((af, wrap(d, why, af, maxw - 34),
                        int(max(22, int(np_ * 0.86)) * 1.34), 4, 34, False))

    if s.get("foot"):
        fp = max(23, int(head_px * 0.32))
        ff = F(P400, fp)
        out.append((ff, wrap(d, s["foot"], ff, maxw), int(fp * 1.34), 40, 0, "before"))

    if s.get("sub"):
        sp = max(26, int(head_px * 0.40))
        sf = F(P400, sp)
        out.append((sf, wrap(d, s["sub"], sf, maxw), int(sp * 1.38), 40, 0, False))

    return out, wrapped


def build(s, H):
    img = Image.new("RGB", (W, H), LAVENDER)
    d = ImageDraw.Draw(img)

    top, bottom = 210, H - 190
    budget = bottom - top

    start = 100
    # The headline's own line breaks are chosen, so a size that re-wraps one of
    # them is the wrong size: shrink until each written line fits whole.
    written = len(s["head"].split("\n"))
    for head_px in range(start, 29, -2):
        parts, wrapped = blocks(d, s, head_px)
        total = sum(g + len(ls) * st + (14 if rule else 0)
                    for _, ls, st, g, _, rule in parts)
        if total <= budget and wrapped == written:
            break
    else:
        raise SystemExit(f"slide {s['n']} does not fit at {H}")

    y = top + (budget - total) // 2
    for font, lines, step, gap, indent, rule in parts:
        y += gap
        if rule == "before":
            y += 6
            d.line([(M, y), (M + 132, y)], fill=HAIRLINE, width=2)
            y += 14
        for ln in lines:
            d.text((M + indent, y), ln, font=font, fill=PURPLE)
            y += step
        if rule is True:
            y += 6
            d.line([(M, y), (M + 132, y)], fill=HAIRLINE, width=2)
            y += 8

    chrome(img, d, H, s["n"])
    return img, head_px


def build_photo(s, H):
    """Slide 1: her photo as a full-width panel, overlay above, line below.

    The source is landscape 1448x1086. A 9:16 crop would keep a third of the
    width and lose both chafing trays, so it sets as a panel instead and the
    lavender carries the type above and below it.
    """
    img = Image.new("RGB", (W, H), LAVENDER)
    d = ImageDraw.Draw(img)

    photo = Image.open(PHOTO).convert("RGB")
    pw, ph = photo.size
    photo = photo.crop((int(CROP[0] * pw), int(CROP[1] * ph),
                        int(CROP[2] * pw), int(CROP[3] * ph)))
    cw, ch = photo.size
    panel_h = round(W * ch / cw)
    photo = photo.resize((W, panel_h), Image.LANCZOS)

    top, bottom = 210, H - 190
    budget = bottom - top
    maxw = W - 2 * M

    written = len(s["head"].split("\n"))
    for head_px in range(80, 29, -2):
        hf = F(P700, head_px)
        head_lines = []
        for para in s["head"].split("\n"):
            head_lines += wrap(d, para, hf, maxw)
        sp = max(26, int(head_px * 0.42))
        sf = F(P400, sp)
        sub_lines = wrap(d, s["sub"], sf, maxw)
        hstep, sstep = int(head_px * 1.18), int(sp * 1.36)
        total = (len(head_lines) * hstep + 40 + panel_h + 38
                 + len(sub_lines) * sstep)
        if total <= budget and len(head_lines) == written:
            break
    else:
        raise SystemExit("slide 1 does not fit")

    y = top + (budget - total) // 2
    for ln in head_lines:
        d.text((M, y), ln, font=hf, fill=PURPLE)
        y += hstep
    y += 40
    img.paste(photo, (0, y))
    y += panel_h + 38
    for ln in sub_lines:
        d.text((M, y), ln, font=sf, fill=PURPLE)
        y += sstep

    chrome(img, d, H, s["n"])
    return img, head_px


def build_card(s, H):
    """Slide 5: the captain sheet, the busiest hour, then the two flags.

    Laid out top-down from a measured height rather than centred, because the
    flag has to be the last thing read. Every value is the BEO's own.
    """
    img = Image.new("RGB", (W, H), LAVENDER)
    d = ImageDraw.Draw(img)

    lf = F(P600, 30)
    namef = F(P600, 32)
    metaf = F(P400, 26)
    bigf = F(P700, 30)
    bodyf = F(P400, 26)
    walkf = F(P600, 29)
    flagf = F(P700, 40)
    flagsub = F(P400, 26)

    y = 210
    d.text((M, y), "What came back", font=lf, fill=PURPLE)
    y += 39
    d.line([(M, y), (M + 132, y)], fill=HAIRLINE, width=2)
    y += 26

    x0, x1 = M, W - M
    row_h = 98
    for name, service, mins in SHEET:
        flagged = mins > WAVE_GAP
        d.rounded_rectangle([x0, y, x1, y + row_h], radius=16,
                            outline=PURPLE if flagged else HAIRLINE,
                            width=3 if flagged else 2)
        d.text((x0 + 26, y + 18), name, font=namef, fill=PURPLE)
        d.text((x0 + 26, y + 57), service, font=metaf, fill=PURPLE)
        tag = f"{mins} min"
        d.text((x1 - 26 - d.textlength(tag, font=bigf), y + 18), tag,
               font=bigf, fill=PURPLE)
        if flagged:
            note = "call it in early"
            d.text((x1 - 26 - d.textlength(note, font=metaf), y + 57), note,
                   font=metaf, fill=PURPLE)
        y += row_h + 10

    y += 14
    for ln in wrap(d, BUSIEST, bodyf, W - 2 * M):
        d.text((M, y), ln, font=bodyf, fill=PURPLE)
        y += 36
    y += 10
    d.text((M, y), "Walk every 15 min: " + WALKS, font=walkf, fill=PURPLE)
    y += 40
    for ln in wrap(d, CONTACTS, metaf, W - 2 * M):
        d.text((M, y), ln, font=metaf, fill=PURPLE)
        y += 34

    y += 22
    flag_lines = wrap(d, FLAG, flagf, W - 2 * M - 60)
    sub_lines = wrap(d, FLAG_SUB, flagsub, W - 2 * M - 60)
    fh = 30 + len(flag_lines) * 50 + 12 + len(sub_lines) * 36 + 30
    d.rounded_rectangle([x0, y, x1, y + fh], radius=22, fill=PURPLE)
    fy = y + 30
    for ln in flag_lines:
        d.text((x0 + 30, fy), ln, font=flagf, fill=LAVENDER)
        fy += 50
    fy += 12
    for ln in sub_lines:
        d.text((x0 + 30, fy), ln, font=flagsub, fill=LAVENDER)
        fy += 36
    bottom = y + fh

    assert bottom <= 1540, f"slide 5 runs past the safe line by {bottom - 1540}px"
    chrome(img, d, H, s["n"])
    return img, bottom


def check():
    assert len(SLIDES) == 6, len(SLIDES)
    assert [x["n"] for x in SLIDES] == [1, 2, 3, 4, 5, 6]
    assert SLIDES[3]["quote"] == PROMPT
    assert os.path.exists(PHOTO), f"her photo is not at {PHOTO}"
    # The crop has to take the right-hand strip off, or the figure is back.
    assert CROP[2] <= 0.85, "the crop must remove the right-hand strip"

    # The sheet is the BEO's, and make_week6.check_beo() recomputes it from the
    # same figures the PDF prints. Re-asserted here so a typo in either file
    # fails the build rather than the Reel.
    import sys
    sys.path.insert(0, os.path.join(HERE, "..", "..", "demo-files", "2026-11"))
    import make_week6 as beo
    beo.check_beo()
    assert len(SHEET) == len(beo.STATIONS) == 7, "seven stations and bars"
    for (name, service, mins), (bname, opens, closes, bmins, _) in zip(SHEET, beo.STATIONS):
        assert name.split()[0] == bname.split()[0], (name, bname)
        assert mins == bmins, (name, mins, bmins)
        assert service.replace(" - ", "-").replace("pm", "") in \
            f"{opens}-{closes}".replace("pm", ""), (service, opens, closes)
    assert WAVE_GAP == beo.WAVE_GAP and WALK_EVERY == beo.WALK_EVERY

    flagged = [n for n, _, m in SHEET if m > WAVE_GAP]
    assert len(flagged) == 2, flagged
    assert flagged[0].startswith("Raw bar") and flagged[1].startswith("Crudit")
    assert "40 min" in FLAG and "35 min" in FLAG, FLAG
    # Five walks fifteen minutes apart across the busiest hour, the last on
    # the hour's end. And the flag test is the WAVE gap, not the walk gap:
    # against 15 minutes four stations would flag, not two.
    assert WALKS.count("·") == 4, WALKS
    assert len([m for _, _, m in SHEET if m > WALK_EVERY]) == 4
    assert "gap between guest waves" in PROMPT
    assert "six of the seven" in BUSIEST

    text = " ".join(str(v) for x in SLIDES for v in x.values()
                    if isinstance(v, str)).lower()
    text += " " + " ".join(n + " " + w for n, _, w in SLIDES[2]["items"]).lower()
    text += " " + FLAG.lower() + " " + FLAG_SUB.lower() + " " + BUSIEST.lower()
    text += " " + " ".join(n for n, _, _ in SHEET).lower()

    # The planner is "them", not "her" — her instruction, Nov 17.
    words = text.replace(",", " ").replace(".", " ").split()
    for pronoun in ("her", "hers", "she", "she’s"):
        assert pronoun not in words, f"the planner is still {pronoun!r} on a slide"

    # No venue, no client, no employer. Thorne Hall and Marchetti are invented
    # and still do not appear on a slide: the sheet names stations, not places.
    for banned in ("thorne", "marchetti", "lowell", "llc", "inc.", "ltd",
                   "hotel", "pavilion"):
        assert banned not in text, f"slide text contains {banned!r}"

    # Her Nov 14 rule: check the closing line against the piece. This is a
    # catering piece, not a money one, so there is no BUDGET line.
    assert "budget" not in text, "a tracker CTA does not belong on a catering piece"
    assert "link in bio" not in text
    print("checks pass: 6 slides, sheet values read from the BEO, seven "
          "stations, two refreshes longer than the 30-minute gap between waves, "
          "walks every 15 minutes, no venue name, no BUDGET line")


def main():
    check()
    os.makedirs(OUT, exist_ok=True)
    for s in SLIDES:
        if s.get("photo"):
            img, px = build_photo(s, H)
            note = f"photo slide, headline {px}px"
        elif s.get("card"):
            img, bottom = build_card(s, H)
            note = f"card ends at {bottom}px"
        else:
            img, px = build(s, H)
            note = f"headline {px}px"
        assert img.size == (W, H)
        p = os.path.join(OUT, f"{STEM}-{s['n']}.jpg")
        img.save(p, quality=95)
        print(f"slide {s['n']}: {note} -> {os.path.basename(p)}")


if __name__ == "__main__":
    main()
