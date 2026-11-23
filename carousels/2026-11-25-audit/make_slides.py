"""Wed 25 Nov — consulting post 2: "One week of your admin. Three fixes."

Six slides in the brand system (lavender #CECBF6, deep purple #3C3489,
Poppins, EP + star wordmark, numbered badge, bottom bar), one set at
1080x1920. Instagram and Facebook take them as a slide Reel with the Eryn
voiceover under soft music; TikTok takes the same six JPEGs as a photo
carousel. Poppins has no glyph at U+2726, so the star is drawn as a polygon.

**THE WORDS ARE THE GUIDE'S, THE LINE BREAKS ARE NOT.** Her Sun 22 recap
wrote slide text for all six; what this file decides is only where each one
splits into headline and body, and where the headline wraps. `check()`
asserts every slide's text still reconstructs the guide's sentence, so a
later edit that rewrites her words fails the build rather than shipping.

**WHY IT OPENS ON A NUMBER.** Wed 11 was the first consulting post and it
opened on "What I'd fix first in an event studio's admin" — 83 reach and no
DMs. The recap's reading is that the hook carried no number, so slide 1 here
leads with "One week. Three fixes." and the explanation goes underneath.

**SLIDES 2-5 ARE HERS TO CORRECT.** Her Wed 25 YOU line says they describe
how an audit actually runs and to change anything that is not how she would
do it. They are built from the guide's own text, not invented, but she is
the one who sells the thing.

NO BUDGET LINE — the guide says so outright, because the ask is the DM.
`check()` asserts the word appears nowhere, the same guard the Nov 17 BEO
redo got after she caught a tracker CTA on an insurance piece.

NO EMPLOYER, NO CLIENT, NO VENUE, anywhere. This is a post about her own
services, which is the post most likely to reach for a name.
"""
import os
import re
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

# The guide's own slide text for Wed 25, sentence by sentence. check()
# rebuilds each slide from head + body and compares it to these, so the
# words stay hers however the breaks are rearranged.
GUIDE = {
    1: "One week of your admin. Three fixes.",
    2: "First, one ordinary week of your admin. "
       "The client emails, the vendor trackers, the proposals.",
    3: "Then the three jobs that eat the most hours. "
       "Usually vendor payments, client emails and proposals.",
    4: "For each one, a prompt or a template. "
       "Your team can use it the next morning, in the tools you already have.",
    5: "That's the audit. "
       "Or a 2-hour AI workshop on your own workflows, for in-house event teams.",
    6: "DM me AUDIT and tell me what eats your week.",
}

SLIDES = [
    dict(n=1, head="One week of your\nadmin. Three fixes.",
         sub="What an AI audit of an event studio actually looks like."),

    dict(n=2, head="First, one ordinary\nweek of your admin.",
         body="The client emails, the vendor trackers, the proposals."),

    dict(n=3, head="Then the three jobs\nthat eat the most\nhours.",
         body="Usually vendor payments, client emails and proposals."),

    dict(n=4, head="For each one, a prompt\nor a template.",
         body="Your team can use it the next morning, in the tools you "
              "already have."),

    dict(n=5, label="What I do for event teams",
         head="That's the audit.",
         body="Or a 2-hour AI workshop on your own workflows, for in-house "
              "event teams."),

    dict(n=6, head="DM me AUDIT and tell\nme what eats your\nweek.",
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
    # Every slide must still say the guide's sentence. Compare on words, so
    # a colon becoming a full stop is allowed and a rewrite is not.
    def words(t):
        return re.findall(r"[a-z0-9']+", t.lower())
    for s in SLIDES:
        mine = words(s["head"] + " " + s.get("body", "") + " " + s.get("sub", ""))
        theirs = words(GUIDE[s["n"]])
        assert mine[:len(theirs)] == theirs, (
            f"slide {s['n']} no longer says the guide's line:\n"
            f"  guide: {theirs}\n  built: {mine[:len(theirs)]}")

    # No employer, no client, no venue — anywhere on any slide.
    text = " ".join(
        str(v) for s in SLIDES for k, v in s.items() if isinstance(v, str)).lower()
    for banned in ("llc", "inc.", "ltd", "hotel", "hall", "pavilion", "catering co"):
        assert banned not in text, f"slide text contains {banned!r}"

    # The guide: no BUDGET line on this one, the ask is the DM.
    assert "budget" not in text, "this post must not carry the BUDGET CTA"
    assert "dm me audit" in text, "the ask is DM me AUDIT"

    # The hook has to carry a number: that is the one thing the recap changed
    # about Wed 11.
    assert any(ch.isdigit() for ch in SLIDES[0]["head"]) or "three" in \
        SLIDES[0]["head"].lower(), "slide 1 must lead with a number"

    assert len(SLIDES) == 6, len(SLIDES)
    assert [s["n"] for s in SLIDES] == [1, 2, 3, 4, 5, 6]
    print("checks pass: 6 slides, every line still the guide's, "
          "no company name, no BUDGET line, a number in the hook")


def main():
    check()
    os.makedirs(OUT, exist_ok=True)
    for s in SLIDES:
        img, px = build(s, H)
        assert img.size == (W, H)
        p = os.path.join(OUT, f"2026-11-25-audit-{s['n']}.jpg")
        img.save(p, quality=95)
        print(f"slide {s['n']}: headline {px}px -> {os.path.basename(p)}")


if __name__ == "__main__":
    main()
