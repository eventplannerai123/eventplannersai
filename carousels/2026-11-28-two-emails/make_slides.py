"""Sat 28 Nov — "The email I wanted to send vs the one I sent."

Content bank 37, the pair for the snippy-email Reel that was one of the top
performers. Six brand slides at 1080x1920: Instagram and Facebook take them
as a slide Reel with the Eryn voiceover, TikTok takes the same JPEGs as a
photo carousel.

**THE SITUATION IS HERS, AND SO ARE BOTH EMAILS.** Her Sat 28 YOU line asked
for one real situation by Tue 24. On Mon 23 she asked for a draft to edit
instead, approved it, and made one change: **"we also will need to add
rentals and servers."** Both emails carry it now, in their own registers —
the angry one counts them ("two more servers, and 40 more of every single
rental"), the sent one absorbs them into the cost. `check()` asserts her
edit survives in both, because it is the only part of this piece she wrote
herself and it is the part most likely to be smoothed away.

**NO NAMES, NO COMPANY, NO VENUE.** The guide says so and so does the
standing rule. The client is "a client"; the caterer is "the caterer".
`check()` refuses company-shaped strings.

**SLIDE 5 IS A REAL RUN OF THE PROMPT, NOT AN IMAGINED ONE.** The guide's
prompt was applied to slide 3's email and slide 5 carries what came back,
unedited. That matters because slide 6 and the caption are built around the
twist — the one thing she would still change — and inventing the output
would invent the twist too.

**THE TWIST, AS IT ACTUALLY LANDED.** The guide predicted the model would
soften the date into "at your earliest convenience". It did not: it kept the
deadline. What it did instead was **open by thanking the client for sending
the final numbers — which is the thing that caused the problem.** That is
the "genuinely good, except…", and it is more useful than the predicted one
because it is a habit rather than a slip: the prompt asks it to "thank them
for what went right", and when nothing did, it thanks them anyway.

NO BUDGET LINE. A client-communication piece, not a money one — the Nov 14
rule about reading the closing line against the piece.
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

# Her edit, Mon 23: "we also will need to add rentals and servers".
# Stems, not the exact words: the draft says "every single rental" and the
# sent email says "additional rentals", and both are her edit.
HER_EDIT = ("rental", "server")

WANTED = ('Forty people is not a rounding error. That’s another seating round, two more servers, and 40 more of every single rental — and the caterer’s nine-day cut-off was yesterday, which I told you about twice. The price was for 260. It is not for 300.')

SENT = ('Happy to add the 40! Flagging that we’re past the caterer’s nine-day confirmation, so I’ll check what they can do. 300 also means additional rentals and two more servers, so there’ll be a revised cost — I’ll have it to you by end of day tomorrow.')

# What the guide's prompt actually returned when run on WANTED. Not edited.
AI_VERSION = ('Adding 40 guests takes us from 260 to 300, which is past the caterer’s nine-day confirmation and means another seating round, two more servers and additional rentals. Can you confirm the revised cost by Thursday so I can hold the caterer’s availability?')

PROMPT_GIST = ("Keep every fact and the one thing I need, but make it calm "
               "and firm. Cut anything I’d regret if it got forwarded.")

SLIDES = [
    dict(n=1, head="The email I wanted\nto send vs the one\nI sent.",
         sub="A client added 40 guests nine days out."),

    dict(n=2, label="The situation",
         head="260 became 300,\nnine days out.",
         body="And they expected the per-head price to hold."),

    dict(n=3, label="The one I wanted to send", head="Draft.",
         quote=WANTED),

    dict(n=4, label="The one I sent", head="Sent.",
         quote=SENT),

    dict(n=5, label="Same facts, run through the prompt",
         head="What came back.",
         body=PROMPT_GIST,
         quote=AI_VERSION,
         foot="Good, except it opens by thanking them for the thing that "
              "caused the problem. Cut that line."),

    dict(n=6, head="Write the first one.\nSend the second.",
         sub="Send this to the planner who drafts in capitals."),
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
    # Her one edit has to survive in both emails. It is the only part of this
    # piece she wrote, and the part a tidy-up would smooth away first.
    for word in HER_EDIT:
        assert word in WANTED.lower(), f"{word!r} missing from the draft"
        assert word in SENT.lower(), f"{word!r} missing from the sent email"

    # Slide 5 is a real run of the prompt. If it ever stops matching what
    # came back, the twist on slide 6 is describing something that did not
    # happen.
    assert SLIDES[4]["quote"] == AI_VERSION
    assert "thank" in SLIDES[4]["foot"].lower(), (
        "slide 5's footnote is the twist and has to name what it got wrong")
    assert "Thursday" in AI_VERSION, (
        "the model kept the date; if a rerun softens it, the twist changes")

    # The numbers are the piece. All three have to be on the slides.
    joined = " ".join(str(v) for s in SLIDES for v in s.values()
                      if isinstance(v, str))
    for num in ("40", "260", "300"):
        assert num in joined, f"the slides lost {num}"

    # No names, no company, no venue — the guide says so twice.
    low = joined.lower()
    for banned in ("llc", "inc.", "ltd", "hotel", "hall", "pavilion",
                   "catering co"):
        assert banned not in low, f"slide text contains {banned!r}"

    # A client-communication piece, not a money one.
    assert "budget" not in low, "this post must not carry the BUDGET CTA"

    assert len(SLIDES) == 6, len(SLIDES)
    assert [s["n"] for s in SLIDES] == [1, 2, 3, 4, 5, 6]
    print("checks pass: 6 slides, her rentals-and-servers edit in both "
          "emails, slide 5 is the real output, 40/260/300 all present")


def main():
    check()
    os.makedirs(OUT, exist_ok=True)
    for s in SLIDES:
        img, px = build(s, H)
        assert img.size == (W, H)
        p = os.path.join(OUT, f"2026-11-28-two-emails-{s['n']}.jpg")
        img.save(p, quality=95)
        print(f"slide {s['n']}: headline {px}px -> {os.path.basename(p)}")


if __name__ == "__main__":
    main()
