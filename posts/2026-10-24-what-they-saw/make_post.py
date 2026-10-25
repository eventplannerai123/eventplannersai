"""“What they saw / What I checked” — the Sat 24 industry-truth post.

A text-only post in the industry-truth brand look, which is NOT the cream and
maroon of the carousels: lavender #CECBF6, deep purple #3C3489, Poppins, the
EP✦ wordmark. The guide sets that look for this format specifically.

OUR OWN DEVICE, NOT HERS. The format is borrowed from @thejuliettripp, and the
guide is explicit about where the line is: two columns are ours, crossed-out
lines and run-on paragraph lists are hers and are never used. Every row is a
true moment of Sahiba's from the content bank.

THE FIFTH ROW IS NOT THE ONE THE BRIEF WROTE. The brief had "Lunch was fine. |
The sandwiches were dry. I'll spec them properly next time." She caught it on
2026-10-25: "everything is ok but the lunch one ... the rest follow a positive
outcome stance". She was right — the other four are "it went well, and here is
the unseen work that made it", while that one was lukewarm on the left and an
admitted miss on the right. It is now the breakfast hold, from her own runny
eggs story, which keeps food in the set and keeps the pattern.

POPPINS IS NOT INSTALLED HERE. The three weights are fetched from Google Fonts
and committed under build/fonts/ so the post can be rebuilt byte-identically
later. Poppins is SIL Open Font License.

AND POPPINS HAS NO GLYPH AT U+2726. Setting the wordmark as the literal
"EP✦" renders a tofu box, which the first build did. The star is drawn as a
polygon instead, sized and baselined off the "EP" it follows.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "slides")
FONTS = os.path.join(HERE, "build", "fonts")

W = 1080
SIZES = {"instagram": 1350, "tiktok": 1920}

LAVENDER = (206, 203, 246)
PURPLE = (60, 52, 137)
HAIRLINE = (176, 172, 228)

P400 = os.path.join(FONTS, "Poppins-400.ttf")
P600 = os.path.join(FONTS, "Poppins-600.ttf")
P700 = os.path.join(FONTS, "Poppins-700.ttf")
F = lambda p, s: ImageFont.truetype(p, s)

M = 64
GUTTER = 34

ROWS = [
    ("Everyone found it easily.",
     "I put the entrance in the first line of the reminder text, and someone at the wrong door anyway."),
    ("The keynote went perfectly.",
     "I checked the AV schedule against the run of show, day by day."),
    ("It came in on budget.",
     "5% of it had no name on it from day one."),
    ("The tech just worked.",
     "I asked whether our laptops could get past the venue's firewall on the site visit."),
    ("Breakfast ran smoothly.",
     "I checked which hot dishes wouldn't survive a 90-minute hold and swapped the ones that wouldn't."),
]

CLOSER = "Nobody sees the second column. That's the job."
HANDLE = "@aiforeventplanners"


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


def layout(d, H, body_px, label_px, closer_px, lh=1.34):
    """Return the total height this type size needs, or None if it overflows."""
    colw = (W - 2 * M - GUTTER) // 2
    lf = F(P700, label_px)
    bfl = F(P600, body_px)
    bfr = F(P400, body_px)
    step = int(body_px * lh)

    head = int(label_px * 1.5) + 26
    rows = []
    for left, right in ROWS:
        nl = len(wrap(d, left, bfl, colw))
        nr = len(wrap(d, right, bfr, colw))
        rows.append(max(nl, nr) * step + 46)        # 46 = padding under the row
    cf = F(P700, closer_px)
    closer = len(wrap(d, CLOSER, cf, W - 2 * M)) * int(closer_px * 1.3)
    total = head + sum(rows) + 54 + closer
    return total, head, rows, closer, colw


def build(H):
    img = Image.new("RGB", (W, H), LAVENDER)
    d = ImageDraw.Draw(img)

    # The type is sized to the frame rather than guessed: the 1080x1350 crop is
    # tight for five two-column rows, and the 1080x1920 one is not.
    budget = H - 150 - 120                           # top start .. wordmark
    for body_px in range(30, 17, -1):
        label_px = max(20, int(body_px * 0.74))
        closer_px = int(body_px * 1.22)
        total, head, rows, closer, colw = layout(d, H, body_px, label_px, closer_px)
        if total <= budget:
            break
    else:
        raise SystemExit("nothing fits")

    y = (H - 120 - total) // 2 + 20
    lx, rx = M, M + colw + GUTTER

    lf = F(P700, label_px)
    d.text((lx, y), "WHAT THEY SAW", font=lf, fill=PURPLE)
    d.text((rx, y), "WHAT I CHECKED", font=lf, fill=PURPLE)
    y += int(label_px * 1.5)
    d.line([(M, y), (W - M, y)], fill=PURPLE, width=3)
    y += 26

    bfl, bfr = F(P600, body_px), F(P400, body_px)
    step = int(body_px * 1.34)
    for i, (left, right) in enumerate(ROWS):
        ry = y
        for ln in wrap(d, left, bfl, colw):
            d.text((lx, ry), ln, font=bfl, fill=PURPLE)
            ry += step
        ry2 = y
        for ln in wrap(d, right, bfr, colw):
            d.text((rx, ry2), ln, font=bfr, fill=PURPLE)
            ry2 += step
        y += rows[i]
        if i < len(ROWS) - 1:
            d.line([(M, y - 24), (W - M, y - 24)], fill=HAIRLINE, width=2)

    y += 54 - 46
    cf = F(P700, closer_px)
    for ln in wrap(d, CLOSER, cf, W - 2 * M):
        d.text(((W - d.textlength(ln, font=cf)) / 2, y), ln, font=cf, fill=PURPLE)
        y += int(closer_px * 1.3)

    # EP✦ wordmark and the handle, bottom centre. The star is DRAWN, not
    # set: Poppins has no glyph at U+2726 and renders a tofu box for it.
    wf = F(P700, 34)
    hf = F(P400, 24)
    ep_w = d.textlength("EP", font=wf)
    star_r = 13
    ex = (W - (ep_w + 10 + star_r * 2)) / 2
    ey = H - 112
    d.text((ex, ey), "EP", font=wf, fill=PURPLE)
    cx, cy = ex + ep_w + 10 + star_r, ey + 34 * 0.62
    waist = star_r * 0.30
    d.polygon([(cx, cy - star_r), (cx + waist, cy - waist), (cx + star_r, cy),
               (cx + waist, cy + waist), (cx, cy + star_r), (cx - waist, cy + waist),
               (cx - star_r, cy), (cx - waist, cy - waist)], fill=PURPLE)
    d.text(((W - d.textlength(HANDLE, font=hf)) / 2, H - 64), HANDLE, font=hf, fill=PURPLE)
    print(f"  {W}x{H}: body {body_px}px, label {label_px}px, closer {closer_px}px")
    return img


def main():
    os.makedirs(OUT, exist_ok=True)
    for name, H in SIZES.items():
        img = build(H)
        assert img.size == (W, H)
        img.save(os.path.join(OUT, f"what-they-saw-{name}.jpg"), quality=95)
        print(f"{name} -> {OUT}/what-they-saw-{name}.jpg")


if __name__ == "__main__":
    main()
