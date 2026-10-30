"""“The scariest moments of my career.” — the Sat 31 Oct Halloween carousel.

Seven slides: a cover, five true moments, a closer. Her own answer to the
Halloween question of the day leads, then four moments out of the guide's
content bank, each with the AI shortcut that actually prevents it.

WHERE EACH MOMENT COMES FROM. Nothing here is invented; every slide is a bank
item, and the shortcut on it is that item's own shortcut rather than a new one
written to fit the slide:

  slide 2  item 39  the medical emergency — her answer, Oct 30
  slide 3  item 1   the AV crew sent to lunch during the keynote
  slide 4  item 13  boxes shipped to a venue and lost there
  slide 5  item 16  guests sent to the wrong entrance
  slide 6  item 20  a budget with no contingency line

THE ORDER IS THE POINT, and it answers her note on this build: "make sure the
heaviness of the first one has a smooth transition to the lighter ones". Her
ambulance moment is genuinely serious and the four bank moments are mishaps, so
the carousel cannot cut straight from one to the other. Three things carry it:

  1. Slide 2 gets NO Halloween decoration at all and no motif band, so the
     text sits in the full height. The hush is deliberate.
  2. Slide 3 opens with her own pivot line — "everything else is small change"
     — as a bridge above the headline, under a hairline. The reader is told the
     tone is changing by the person whose story it is.
  3. The motifs then grow slide by slide, in count and in contrast (MOTIFS
     below). By slide 6 the band is full and at nearly full purple. The ramp IS
     the transition, not an ornament sitting on top of one.

HALLOWEEN MOTIFS ARE DRAWN, NOT FETCHED. Her note: "make sure to add some
pumkins, grim reapers, ghosts etc so it 'holiday themed'". Two standing rules
bind that at once — no stock and no generated visuals, and "Never another colour
scheme" — so the pumpkin, ghost, bat, reaper and headstone are vector shapes
built here, in deep purple on lavender, tinted toward the background to set
their weight. They live in a reserved band above the bottom bar, so they can
never land on text.

THE BRAND SYSTEM IS THE GUIDE'S. Lavender #CECBF6, deep purple #3C3489,
Poppins, EP✦ wordmark, numbered badge, bottom bar. Poppins is not installed
here, so the three weights are committed under build/fonts/ and the slides
rebuild byte-identically. Poppins has no glyph at U+2726, so the star is a
polygon sized off the "EP" it follows.
"""
import math
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

M = 72
HANDLE = "@aiforeventplanners"

BAND = 178          # reserved motif strip above the bottom bar
MOTIF_S = 44

PROMPT = (
    "I'm running an event for [number] people at [venue]. Write me a one-page "
    "medical response card the whole team can read in ten seconds: the nearest "
    "hospital and how far it is, who calls 911 and from which phone, where the "
    "AED is, which door an ambulance comes to and who meets it there, who "
    "clears the route, and who tells the client. Keep it to one page."
)


# ---------------------------------------------------------------- motifs
def tint(t):
    """Blend the background toward deep purple. t=0 invisible, t=1 full."""
    return tuple(round(a + (b - a) * t) for a, b in zip(LAVENDER, PURPLE))


def pumpkin(d, cx, cy, s, c):
    d.ellipse([cx - s, cy - s * 0.78, cx + s, cy + s * 0.78], outline=c, width=4)
    d.arc([cx - s * 0.42, cy - s * 0.78, cx + s * 0.42, cy + s * 0.78], 0, 360,
          fill=c, width=3)
    d.line([(cx, cy - s * 0.74), (cx, cy - s * 1.12)], fill=c, width=6)
    d.line([(cx, cy - s * 1.10), (cx + s * 0.28, cy - s * 1.26)], fill=c, width=5)
    e = s * 0.17
    for sx in (-s * 0.40, s * 0.40):
        d.polygon([(cx + sx - e, cy - s * 0.08), (cx + sx + e, cy - s * 0.08),
                   (cx + sx, cy - s * 0.40)], fill=c)
    grin = [(cx - s * 0.46, cy + s * 0.18), (cx - s * 0.22, cy + s * 0.20),
            (cx - s * 0.12, cy + s * 0.40), (cx, cy + s * 0.20),
            (cx + s * 0.12, cy + s * 0.40), (cx + s * 0.22, cy + s * 0.20),
            (cx + s * 0.46, cy + s * 0.18), (cx + s * 0.30, cy + s * 0.50),
            (cx - s * 0.30, cy + s * 0.50)]
    d.polygon(grin, fill=c)


def ghost(d, cx, cy, s, c):
    r = s * 0.62
    top = cy - s * 0.18
    pts = [(cx + r * math.cos(math.radians(a)), top + r * math.sin(math.radians(a)))
           for a in range(180, 361, 6)]
    pts.append((cx + r, cy + s * 0.52))
    for i in range(3):                      # scalloped hem, right to left
        x0 = cx + r - (2 * r / 3) * i
        x1 = x0 - (2 * r / 3)
        mid = (x0 + x1) / 2
        pts += [(mid, cy + s * 0.86), (x1, cy + s * 0.52)]
    pts.append((cx - r, top))
    d.polygon(pts, fill=c)
    for sx in (-s * 0.24, s * 0.24):
        d.ellipse([cx + sx - s * 0.11, cy - s * 0.42,
                   cx + sx + s * 0.11, cy - s * 0.16], fill=LAVENDER)
    d.ellipse([cx - s * 0.10, cy - s * 0.02, cx + s * 0.10, cy + s * 0.16],
              fill=LAVENDER)


def bat(d, cx, cy, s, c):
    d.ellipse([cx - s * 0.15, cy - s * 0.26, cx + s * 0.15, cy + s * 0.40], fill=c)
    d.ellipse([cx - s * 0.17, cy - s * 0.52, cx + s * 0.17, cy - s * 0.20], fill=c)
    for sx in (-s * 0.12, s * 0.12):
        d.polygon([(cx + sx - s * 0.07, cy - s * 0.46),
                   (cx + sx + s * 0.07, cy - s * 0.46),
                   (cx + sx * 1.5, cy - s * 0.74)], fill=c)
    for m in (-1, 1):
        d.polygon([(cx + m * s * 0.12, cy - s * 0.22),
                   (cx + m * s * 1.00, cy - s * 0.52),
                   (cx + m * s * 0.82, cy - s * 0.02),
                   (cx + m * s * 0.62, cy + s * 0.22),
                   (cx + m * s * 0.44, cy + s * 0.00),
                   (cx + m * s * 0.26, cy + s * 0.26),
                   (cx + m * s * 0.12, cy + s * 0.08)], fill=c)


def reaper(d, cx, cy, s, c):
    hx = cx - s * 0.18
    d.polygon([(hx - s * 0.30, cy - s * 0.18), (hx + s * 0.30, cy - s * 0.18),
               (hx + s * 0.52, cy + s * 0.88), (hx - s * 0.52, cy + s * 0.88)],
              fill=c)
    d.ellipse([hx - s * 0.34, cy - s * 0.78, hx + s * 0.34, cy - s * 0.10], fill=c)
    d.ellipse([hx - s * 0.20, cy - s * 0.60, hx + s * 0.20, cy - s * 0.12],
              fill=LAVENDER)
    d.line([(cx + s * 0.62, cy + s * 0.90), (cx + s * 0.40, cy - s * 0.92)],
           fill=c, width=5)
    d.arc([cx - s * 0.20, cy - s * 1.14, cx + s * 0.60, cy - s * 0.46],
          300, 60, fill=c, width=6)


def headstone(d, cx, cy, s, c):
    """An arched stone. Deliberately NOT a cross inside — on a carousel whose
    first moment is a medical emergency, a + reads as a first-aid symbol."""
    hw = s * 0.70
    d.arc([cx - hw, cy - s * 1.02, cx + hw, cy + s * 0.38], 180, 360, fill=c, width=4)
    d.line([(cx - hw, cy - s * 0.32), (cx - hw, cy + s * 0.74)], fill=c, width=4)
    d.line([(cx + hw, cy - s * 0.32), (cx + hw, cy + s * 0.74)], fill=c, width=4)
    d.line([(cx - hw, cy + s * 0.74), (cx + hw, cy + s * 0.74)], fill=c, width=4)
    for i, w in enumerate((0.34, 0.44, 0.44)):
        d.line([(cx - s * w, cy - s * 0.22 + i * s * 0.26),
                (cx + s * w, cy - s * 0.22 + i * s * 0.26)], fill=c, width=4)
    d.line([(cx - s * 1.04, cy + s * 0.80), (cx + s * 1.04, cy + s * 0.80)],
           fill=c, width=3)


DRAW = {"pumpkin": pumpkin, "ghost": ghost, "bat": bat, "reaper": reaper,
        "headstone": headstone}

# The ramp. Slide 2 is empty on purpose — see the module docstring.
MOTIFS = {
    1: (["pumpkin", "ghost", "bat", "reaper", "headstone"], 1.00),
    2: ([], 0.0),
    3: (["pumpkin"], 0.38),
    4: (["ghost", "pumpkin"], 0.58),
    5: (["bat", "pumpkin", "ghost"], 0.76),
    6: (["headstone", "bat", "pumpkin", "ghost"], 0.90),
    7: (["reaper", "headstone", "bat", "pumpkin", "ghost"], 1.00),
}


# ---------------------------------------------------------------- slides
SLIDES = [
    dict(n=1, head="The scariest\nmoments of\nmy career.",
         sub="Five true ones — and what I do now so they can't happen twice."),

    dict(n=2, head="An ambulance\nhad been called.",
         body="The only moments that ever actually scared me had a medical "
              "emergency in them.",
         now="A one-page medical response card for every event: the nearest "
             "hospital, who calls 911 and from which phone, where the AED is, "
             "which door the ambulance comes to and who meets it, who clears "
             "the route, who tells the client."),

    dict(n=3, bridge="Everything else is small change.",
         head="The AV crew went\nto lunch during\nthe keynote.",
         body="Two schedules, two different lunch breaks. Nobody caught it "
              "until the room went quiet.",
         now="Paste the AV schedule and the production schedule in together "
             "and ask AI to flag every mismatch, day by day."),

    dict(n=4, head="The boxes never\nmade it to\nthe room.",
         body="Shipped to the venue a week early, signed for by someone who "
              "couldn't say where they'd put them.",
         now="Turn the packing list into a box-by-box manifest: tracking "
             "number, which room it goes to, and who signs for it."),

    dict(n=5, head="They used the\nwrong entrance.",
         body="They were told exactly which entrance. They still used the "
              "wrong one.",
         now="A “know before you go” message with the entrance in the first "
             "line, plus a landmark, transit and parking — checked against the "
             "venue's own directions."),

    dict(n=6, head="A budget with no\ncontingency line.",
         body="Nothing had gone wrong yet. There was just nowhere to put it "
              "when it did.",
         now="Have AI read the draft budget, work out 5%, and flag it when the "
             "contingency line is missing or too thin."),

    dict(n=7, head="None of these\nwere bad luck.",
         sub="Every one of them had a document that could have caught it. "
             "Save this for your next event."),
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

    if s.get("bridge"):
        bp = max(26, int(head_px * 0.34))
        bf = F(P600, bp)
        out.append((bf, wrap(d, s["bridge"], bf, maxw), int(bp * 1.30), 0, 0, True))

    hf = F(P700, head_px)
    head_lines = []
    for para in s["head"].split("\n"):
        head_lines += wrap(d, para, hf, maxw)
    out.append((hf, head_lines, int(head_px * 1.18), 34 if s.get("bridge") else 0,
                0, False))

    if s.get("sub"):
        sp = max(26, int(head_px * 0.40))
        sf = F(P400, sp)
        out.append((sf, wrap(d, s["sub"], sf, maxw), int(sp * 1.38), 40, 0, False))

    if s.get("body"):
        bp = max(26, int(head_px * 0.42))
        bf = F(P400, bp)
        out.append((bf, wrap(d, s["body"], bf, maxw), int(bp * 1.38), 36, 0, False))

    if s.get("now"):
        lp = max(23, int(head_px * 0.30))
        lf = F(P600, lp)
        out.append((lf, ["What I do now"], int(lp * 1.30), 48, 0, True))
        np_ = max(25, int(head_px * 0.38))
        nf = F(P400, np_)
        out.append((nf, wrap(d, s["now"], nf, maxw - 34), int(np_ * 1.40), 18, 34,
                    False))

    return out


def build(s, H):
    img = Image.new("RGB", (W, H), LAVENDER)
    d = ImageDraw.Draw(img)

    names, t = MOTIFS[s["n"]]
    top = 210
    bottom = H - 190 - (BAND if names else 0)
    budget = bottom - top

    start = 96 if s.get("now") else 104
    for head_px in range(start, 29, -2):
        parts = blocks(d, s, head_px)
        total = sum(g + len(ls) * st + (14 if rule else 0)
                    for _, ls, st, g, _, rule in parts)
        if total <= budget:
            break
    else:
        raise SystemExit(f"slide {s['n']} does not fit at {H}")

    y = top + (budget - total) // 2
    for font, lines, step, gap, indent, rule in parts:
        y += gap
        for ln in lines:
            d.text((M + indent, y), ln, font=font, fill=PURPLE)
            y += step
        if rule:
            y += 6
            d.line([(M, y), (M + 132, y)], fill=HAIRLINE, width=2)
            y += 8

    if names:
        c = tint(t)
        cy = H - 190 - BAND / 2 + 6
        step = MOTIF_S * 3.1          # a centred cluster that grows outward,
        x0 = W / 2 - step * (len(names) - 1) / 2   # not a row spanning the width
        for i, name in enumerate(names):
            DRAW[name](d, x0 + step * i, cy, MOTIF_S, c)

    chrome(img, d, H, s["n"])
    return img, head_px


def main():
    os.makedirs(OUT, exist_ok=True)
    for name, H in SIZES.items():
        for s in SLIDES:
            img, px = build(s, H)
            assert img.size == (W, H)
            p = os.path.join(OUT, f"2026-10-31-halloween-scariest-{name}-{s['n']}.jpg")
            img.save(p, quality=95)
            print(f"{name} slide {s['n']}: headline {px}px, "
                  f"{len(MOTIFS[s['n']][0])} motifs -> {os.path.basename(p)}")


if __name__ == "__main__":
    main()
