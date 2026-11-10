"""Wed 11 Nov — consulting post 1: "What I'd fix first in an event studio's admin."

Six slides, the guide's own text for the day, in the brand system: lavender
#CECBF6, deep purple #3C3489, Poppins, EP + star wordmark, numbered badge,
bottom bar. Poppins has no glyph at U+2726, so the star is a polygon.

ONE SET AT 1080x1920, not the usual 1080x1350 pair. The Nov 8 format rule
sends Instagram and Facebook a **slide Reel** (each slide about 2.5 seconds,
soft music) and TikTok the same slides as a photo carousel, so both outputs
want the 9:16 frame and one set serves them.

SLIDE 5 IS A PLACEHOLDER UNTIL SHE CONFIRMS IT. Her Wed 11 YOU line asks for
two or three lines on the offer by Tue 10, and says that until they arrive
the slides use the plan in Section 12 of the guide: a 2-hour AI workshop for
in-house event teams with a 30-day check-in, and an AI admin audit for small
event studios. That is exactly what slide 5 says, and `check()` asserts it
still matches SECTION_12 so the day it changes is the day she changed it.

NO BUDGET LINE ON THIS ONE — the guide says so outright, because the ask is
"DM me".

NO EMPLOYER AND NO CLIENT, anywhere. check() asserts the slides carry no
company name at all: this is the first post that talks about her own
services, which is the post most likely to reach for one.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "slides")
FONTS = os.path.join(HERE, "build", "fonts")

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

# The fallback the guide names, so check() can tell it apart from her words.
SECTION_12 = ("a 2-hour AI workshop for in-house event teams with a 30-day "
              "check-in, and an AI admin audit for small event studios")

SLIDES = [
    dict(n=1, head="What I'd fix first\nin an event studio's\nadmin.",
         sub="17 years in, it's never the creative. It's the admin."),

    dict(n=2, head="Every vendor payment\nlives in someone's\nhead.",
         body="One tracker the whole team can see, instead of one person "
              "remembering what's due and when."),

    dict(n=3, head="The same client email\ngets written from\nscratch twenty\ntimes a month.",
         body="Saved templates AI drafts from, so the work is the edit rather "
              "than the blank page."),

    dict(n=4, head="The proposal takes\na full day.",
         body="AI turns the brief into a first draft. You spend your time on "
              "the judgement, not the typing."),

    dict(n=5, label="What I do for event teams",
         head="A 2-hour AI workshop,\nor an admin audit.",
         body="The workshop runs on your own workflows, with a 30-day "
              "check-in. The audit goes through a small studio's admin and "
              "says what to fix first."),

    dict(n=6, head="DM me and tell me\nwhat eats your week.",
         sub="That's the whole ask. No pitch."),
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
    """Numbered badge, then the bottom bar: rule, EP✦ wordmark, handle."""
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
            out.append((nf, [f"{name}  {amount}"], int(np_ * 1.26),
                        36 if i == 0 else 22, 0, False))
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

    start = 78 if s.get("items") else 100
    # The headline's own line breaks are chosen, so a size that re-wraps one
    # of them is the wrong size: shrink until each written line fits whole.
    # Slide 1 shipped as "Everyone has a / rain / plan. Almost / nobody" the
    # first time this was left to the wrapper.
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
        # "before" is the foot's rule, which sits above it; True is the
        # label's, which sits under. Keyed on the flag, never on the text —
        # comparing the wrapped lines to the raw string only worked while
        # every foot happened to fit on one line, and put the rule through
        # the second line the first time one did not.
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


def check():
    # Slide 5 must still be the guide's Section 12 fallback, or she has sent
    # her own lines and this assert is the reminder to rewrite the caption too.
    five = SLIDES[4]
    assert "2-hour AI workshop" in five["head"], five["head"]
    assert "30-day" in five["body"] and "admin audit" in five["head"].lower() \
        or "audit" in five["head"].lower(), five
    assert "workshop" in SECTION_12 and "audit" in SECTION_12

    # No employer, no client, no venue — anywhere on any slide.
    text = " ".join(
        str(v) for s in SLIDES for k, v in s.items() if isinstance(v, str)).lower()
    for banned in ("llc", "inc.", "ltd", "hotel", "hall", "pavilion", "catering co"):
        assert banned not in text, f"slide text contains {banned!r}"

    # The guide: no BUDGET line on this one, the ask is "DM me".
    assert "budget" not in text, "this post must not carry the BUDGET CTA"
    assert "dm me" in text, "the ask is DM me"

    assert len(SLIDES) == 6, len(SLIDES)
    assert [s["n"] for s in SLIDES] == [1, 2, 3, 4, 5, 6]
    print("checks pass: 6 slides, slide 5 is still the Section 12 fallback, "
          "no company name, no BUDGET line")


def main():
    check()
    os.makedirs(OUT, exist_ok=True)
    for s in SLIDES:
        img, px = build(s, H)
        assert img.size == (W, H)
        p = os.path.join(OUT, f"2026-11-11-consulting-admin-{s['n']}.jpg")
        img.save(p, quality=95)
        print(f"slide {s['n']}: headline {px}px -> {os.path.basename(p)}")


if __name__ == "__main__":
    main()
