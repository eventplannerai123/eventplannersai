"""Tue 24 Nov — "Event planning advice I'd burn." THE WEEKLY HOOK TEST PAIR.

Her Nov 19 format: every week one extra piece is tested on non-followers
before it reaches the feed. CC builds two versions of one new Reel, identical
except the title, and she uploads both from her phone with Trial turned on —
this session cannot post trials. Friday she compares views and non-follower
reach after 72 hours, taps "Share to everyone" on the winner and leaves the
other as a trial. Facebook gets only the winner, after it is shared.

**A AND B DIFFER IN THE TITLE AND IN NOTHING ELSE.** That is the whole test,
so the five lines, the boxes, the sizes and the bed are the same file in both.
`check()` asserts the two titles differ and that nothing else does.

  A: "Event planning advice I'd burn."
  B: "17 years in, here's the event planning advice I'd burn."

**THE FIVE LINES CAME OUT OF A DRAFT SHE EDITED, WHICH IS NOT THE SAME AS
HERS.** The Sun 22 deadline for her own answers arrived with "Start with a
draft and I'll make edits", so this session wrote five and she worked them:
she rewrote the contingency rebuttal in her own words ("Contingency plan is a
line item"), rejected the original line 1 as weak, and picked its replacement
from five options. Every line here is one she kept or wrote. Nothing goes out
that she has not seen.

Format: the planner list Reel from the November plan — deep purple #3C3489
ground, lavender #CECBF6 boxes, Poppins, title in SemiBold white, held 8-10
seconds as a Reel with music. Each box holds the advice in quotes above the
rebuttal in SemiBold, because the turn is the joke and it should land on its
own line.

NO BUDGET LINE and no CTA at all: a trial exists to measure a hook, and an
ask would be a second variable.
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
QUOTE = (96, 88, 166)

P400 = os.path.join(FONTS, "Poppins-400.ttf")
P600 = os.path.join(FONTS, "Poppins-600.ttf")
F = lambda p, s: ImageFont.truetype(p, s)

M = 72
HANDLE = "@aiforeventplanners"

TITLES = {
    "a": "Event planning\nadvice I’d burn.",
    "b": "17 years in, here’s\nthe event planning\nadvice I’d burn.",
}

# advice, rebuttal
LINES = [
    ("“A good planner is invisible.”",
     "Invisible is how a room ends up with nobody in charge."),
    ("“That’s how we did it last year.”",
     "Last year is data, not a template."),
    ("“Under-promise and over-deliver.”",
     "The free extra becomes next year’s baseline."),
    ("“Just stay flexible on site.”",
     "Flexible is what’s left when nobody got a captain."),
    ("“Round the budget up and you’ll be fine.”",
     "Contingency plan is a line item."),
]

PAD_X, PAD_Y, GAP = 34, 26, 20
RADIUS = 24


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


def layout(d, title, title_px, box_px):
    maxw = W - 2 * M
    tf = F(P600, title_px)
    tl = []
    for line in title.split("\n"):
        tl += wrap(d, line, tf, maxw)
    tstep = int(title_px * 1.16)

    qf, rf = F(P400, int(box_px * 0.88)), F(P600, box_px)
    qstep, rstep = int(box_px * 0.88 * 1.30), int(box_px * 1.28)
    inner = maxw - 2 * PAD_X
    boxes = []
    for advice, rebut in LINES:
        q = wrap(d, advice, qf, inner)
        r = wrap(d, rebut, rf, inner)
        boxes.append((q, r, len(q) * qstep + 8 + len(r) * rstep + 2 * PAD_Y))

    total = (len(tl) * tstep + int(title_px * 0.70)
             + sum(b[2] for b in boxes) + GAP * (len(boxes) - 1))
    return (tf, tl, tstep, qf, qstep, rf, rstep, boxes), total, len(tl)


def build(key, force_box_px=None):
    title = TITLES[key]
    img = Image.new("RGB", (W, H), PURPLE)
    d = ImageDraw.Draw(img)
    # Safe zones are the layout, not a check afterwards: nothing important in
    # the top 12% or from 1440 down, where TikTok's furniture sits.
    top, bottom = 250, 1440
    budget = bottom - top

    written = len(title.split("\n"))
    for title_px in range(80, 33, -2):
        box_px = force_box_px or max(26, int(title_px * 0.46))
        parts, total, nlines = layout(d, title, title_px, box_px)
        if total <= budget and nlines == written:
            break
    else:
        raise SystemExit(f"version {key} does not fit")

    tf, tl, tstep, qf, qstep, rf, rstep, boxes = parts
    y = top + (budget - total) // 2

    for ln in tl:
        d.text((M, y), ln, font=tf, fill=WHITE)
        y += tstep
    y += int(title_px * 0.70)

    for q, r, h in boxes:
        d.rounded_rectangle([M, y, W - M, y + h], radius=RADIUS, fill=LAVENDER)
        ty = y + PAD_Y
        for ln in q:
            d.text((M + PAD_X, ty), ln, font=qf, fill=QUOTE)
            ty += qstep
        ty += 8
        for ln in r:
            d.text((M + PAD_X, ty), ln, font=rf, fill=PURPLE)
            ty += rstep
        y += h + GAP
    y -= GAP

    hf = F(P400, 24)
    d.text(((W - d.textlength(HANDLE, font=hf)) / 2, H - 92), HANDLE,
           font=hf, fill=LAVENDER)
    return img, title_px, box_px, y


def check():
    assert len(LINES) == 5, "the format is five lines"
    assert TITLES["a"] != TITLES["b"], "the two versions must differ"
    # The test measures the TITLE. Anything else that differs is a second
    # variable and would make the result unreadable.
    assert set(TITLES) == {"a", "b"}, TITLES
    # Her own edit, word for word.
    assert LINES[4][1] == "Contingency plan is a line item.", "her wording"
    joined = " ".join(a + " " + b for a, b in LINES).lower()
    for banned in ("budget for", "prompt", "chatgpt", "link in bio", "gumroad",
                   "comment "):
        assert banned not in joined, f"no CTA or AI demo: found {banned!r}"
    print("checks pass: 5 shared lines, 2 titles, no CTA")


def main():
    check()
    os.makedirs(OUT, exist_ok=True)
    # THE BODY MUST BE IDENTICAL IN BOTH, or the test has two variables.
    # Solved free, B's longer title squeezed its boxes to 34px against A's 36,
    # which is small but is still not "identical except the title". So B is
    # solved first and A is rebuilt at B's box size.
    _, _, shared_box_px, _ = build("b")
    sizes = {}
    for key in ("a", "b"):
        img, tpx, bpx, end_y = build(key, force_box_px=shared_box_px)
        assert img.size == (W, H)
        assert end_y <= 1440, f"{key}: last box ends at {end_y}, in the bottom 25%"
        sizes[key] = bpx
        p = os.path.join(OUT, f"advice-burn-{key}.jpg")
        img.save(p, quality=95)
        print(f"{key}: title {tpx}px, boxes {bpx}px, ends y={end_y}")
    assert sizes["a"] == sizes["b"], f"the bodies differ in size: {sizes}"


if __name__ == "__main__":
    main()
