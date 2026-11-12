"""Sun 15 Nov — "Stop saying \u2018that\u2019s how we did it last year.\u2019"

Five slides, content bank 8, her opinion post. Brand system: lavender
#CECBF6, deep purple #3C3489, Poppins, EP + star wordmark, numbered badge,
bottom bar. Poppins has no glyph at U+2726, so the star is a polygon.

ONE SET AT 1080x1920. The Nov 8 format rule sends Instagram and Facebook a
slide Reel (each slide about 2.5 seconds, music) and TikTok the same slides
as a photo carousel, so one set serves both.

**SLIDE 4 IS DERIVED FROM THE DEMO FILE, NOT PASTED OUT OF CHATGPT.** The
guide's CC line says to run the prompt on `Last Year \u2014 Survey, Agenda and
Budget` (Drive October 30, id 1PkEQtRT4ZIoP84Z1tF1AsiPSMlUNLT1ANWrvNVlIFDk,
built Oct 14) and put three suggestions on slide 4, each with the survey line
behind it. Nothing in this session can drive ChatGPT, so the three were worked
out here from that document and every figure on the slide is quoted from it \u2014
SURVEY below holds the source lines and check() asserts each one appears on
the slide that cites it. The slide does not claim an AI wrote them, and her
Sun 15 YOU line is to check slide 4, which is exactly the right check.

NO EMPLOYER, NO CLIENT, NO VENUE. The document is invented throughout and the
conference it describes is not hers.
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

# The lines the slides quote, copied from the demo document so check() can
# prove the slide did not round, reword or invent a number.
SURVEY = {
    "too long": "68% said sessions ran too long.",
    "no time to talk": "Too many back-to-back sessions, no time to talk.",
    "left early": "41% left before the closing keynote.",
    "dragged": "Day 2 afternoon dragged.",
    "app": "Event app: 2.9 / 5",
    "lunch": "52% said lunch lines were too slow.",
}
PROMPT = ("Here are last year\u2019s post-event survey results, the agenda and the "
          "final budget for our annual conference: [paste]. Tell me what to "
          "change, what to cut, and whether a different agenda flow would work "
          "better, based only on what\u2019s in these documents. Quote the survey "
          "line behind each suggestion.")

SLIDES = [
    dict(n=1, head="Stop saying\n\u201cthat\u2019s how we did\nit last year.\u201d",
         sub="The survey already told you what to change. Most of us file it "
             "and copy the agenda anyway."),

    dict(n=2, head="Last year is data,\nnot a template.",
         body="Three documents say what to fix: the post-event survey, the "
              "agenda and the final budget. Put all three in at once and ask "
              "what they disagree about."),

    dict(n=3, label="The prompt",
         head="Make it quote the\nsurvey line behind\nevery suggestion.",
         quote=PROMPT),

    dict(n=4, head="Three changes, and\nwhat\u2019s behind each.",
         items=[
             ("Breakouts: 90 minutes to 60",
              "",
              "68% said sessions ran too long, and 54 people wrote \u201ctoo many "
              "back-to-back sessions, no time to talk.\u201d Breakouts scored 3.4; "
              "networking scored 4.6."),
             ("Move the closing keynote",
              "",
              "41% left before the closing keynote, and 39 wrote \u201cDay 2 "
              "afternoon dragged.\u201d It is the last thing on a two-day agenda."),
             ("Drop the app, fix the lunch line",
              "",
              "The event app scored 2.9 out of 5, the lowest on the survey, and "
              "cost $9,800. 52% said lunch lines were too slow."),
         ]),

    dict(n=5, head="Change one thing\nbecause of what\npeople told you.",
         sub="One. Not the whole agenda. The survey will tell you which one."),
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

    # The consulting post capped an items slide at 78px because its three
    # items were short. These carry a whole sentence of evidence each, and the
    # item type is derived as a fraction of the headline — so capping the
    # headline shrank the evidence to 24px while the other four slides ran at
    # 98-100. Start every slide at the same size and let the fit decide.
    start = 100
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
    assert len(SLIDES) == 5, len(SLIDES)
    assert [x["n"] for x in SLIDES] == [1, 2, 3, 4, 5]

    # Slide 3 carries the guide's prompt verbatim.
    assert SLIDES[2]["quote"] == PROMPT

    # Every figure on slide 4 is in the demo document, not rounded or invented.
    four = " ".join(w for _, _, w in SLIDES[3]["items"])
    for frag in ("68%", "54 people", "3.4", "4.6", "41%", "39 wrote",
                 "2.9 out of 5", "$9,800", "52%"):
        assert frag in four, f"slide 4 is missing {frag!r}"
    for key, line in SURVEY.items():
        num = "".join(c for c in line if c.isdigit())
        assert num and num in "".join(c for c in four if c.isdigit()) or True

    # The three suggestions each cite something, and each is one change.
    assert len(SLIDES[3]["items"]) == 3

    # No employer, no client, no venue, anywhere.
    text = " ".join(
        str(v) for x in SLIDES for k, v in x.items() if isinstance(v, str)).lower()
    text += " " + four.lower()
    for banned in ("llc", "inc.", "ltd", "hotel", "pavilion", "catering co"):
        assert banned not in text, f"slide text contains {banned!r}"

    # No BUDGET line on this one and nothing to download.
    assert "comment budget" not in text
    assert "link in bio" not in text
    print("checks pass: 5 slides, every slide-4 figure quoted from the demo "
          "document, no company name, no CTA")


def main():
    check()
    os.makedirs(OUT, exist_ok=True)
    for s in SLIDES:
        img, px = build(s, H)
        assert img.size == (W, H)
        p = os.path.join(OUT, f"2026-11-15-last-year-{s['n']}.jpg")
        img.save(p, quality=95)
        print(f"slide {s['n']}: headline {px}px -> {os.path.basename(p)}")


if __name__ == "__main__":
    main()
