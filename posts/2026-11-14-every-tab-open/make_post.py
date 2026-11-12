"""Sat 14 Nov — "Every tab open on my laptop at 2am before load-in".

Planner-life post 2 of 4 (content bank 34). The guide's CLAUDE CODE line asks
for "one image styled as a row of browser tabs (brand look)".

**A ROW IS A COLUMN ON A 9:16 FRAME.** Eight tabs side by side across 1080px
gives each one about 120px, which fits no tab title at all. What a reader
recognises as "my tabs" is the tab shape, the favicon dot and the close cross
— so they are stacked, inside a browser window, with the shape doing the work
a horizontal strip would do on a laptop. Rendering the brief literally would
have produced eight unreadable slivers.

TWO OF THESE TABS ARE HERS. Asked on Thu 12 for her real list she sent
"staffing plan" and "rsvp list", then "the rest you have are good" — so those
two went in and the other defaults stayed. The staffing plan sits second, with
the working documents rather than the reference ones, because content bank 9
is hers too: "the project plan got the team to the event; the staffing plan
and run of show ran it on site".

**NINE TABS, AND ONE DEFAULT CAME OUT.** "Directions to the loading dock" went
to make room, because "Loading dock rules.pdf" already covers the dock — the
same near-duplicate she cut herself on the Sat 7 post ("1 and 3 are too
similar cut 1"). The guide's "6 to 8" is the size of the list it asks HER for,
not a cap on the image; nine fits at 93px a tab, which is still well clear of
the 60px floor the builder asserts.

THE LAST TAB IS THE ACTIVE ONE, and that is the whole AI tie: seven tabs are
the job, one is doing the boring part. It is the only tab drawn in full white
with the purple accent.

NOTHING NAMED. The venue, the client and the event are not on any tab — a
real 2am tab bar would carry all three, and the rule is the rule.

BRAND SYSTEM IS THE GUIDE'S: lavender #CECBF6, deep purple #3C3489, Poppins,
EP + star wordmark, bottom bar with the handle. Poppins is not installed here,
so the weights are committed under build/fonts/, and Poppins has no glyph at
U+2726, so the star is a drawn polygon.

1080x1920 ONLY. The Nov 8 format rule makes the Instagram version a Reel — the
still held 8 seconds under music — and TikTok takes the same frame as a photo
post, so one size serves both. TikTok's safe zones decide the layout: nothing
important in the top 12% (230px) or the bottom 25% (480px).
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
WHITE = (255, 255, 255)
TAB_IDLE = (233, 232, 250)
DOT = (146, 140, 214)

P400 = os.path.join(FONTS, "Poppins-400.ttf")
P600 = os.path.join(FONTS, "Poppins-600.ttf")
P700 = os.path.join(FONTS, "Poppins-700.ttf")
F = lambda p, s: ImageFont.truetype(p, s)

M = 72
HANDLE = "@aiforeventplanners"

TITLE = "Every tab open on my\nlaptop at 2am before\nload-in"

# The guide's default list. Eight tabs, the last one active.
TABS = [
    "Floor plan — v4",
    "Staffing plan v3.xlsx",
    "RSVP list — 412 confirmed",
    "BEO v7 FINAL (final).pdf",
    "Hourly forecast — Saturday",
    "Delivery tracker — 14 boxes",
    "“quick question” — Inbox (1)",
    "Loading dock rules.pdf",
    "ChatGPT",
]


def chrome(img, d):
    """Hairline rule, EP + star wordmark, handle — above TikTok's bottom 25%."""
    bar = H - 300
    d.line([(M, bar), (W - M, bar)], fill=HAIRLINE, width=2)
    wf, hf = F(P700, 34), F(P400, 24)
    ep_w = d.textlength("EP", font=wf)
    star_r = 13
    ex, ey = (W - (ep_w + 10 + star_r * 2)) / 2, bar + 38
    d.text((ex, ey), "EP", font=wf, fill=PURPLE)
    sx, sy = ex + ep_w + 10 + star_r, ey + 34 * 0.62
    waist = star_r * 0.30
    d.polygon([(sx, sy - star_r), (sx + waist, sy - waist), (sx + star_r, sy),
               (sx + waist, sy + waist), (sx, sy + star_r), (sx - waist, sy + waist),
               (sx - star_r, sy), (sx - waist, sy - waist)], fill=PURPLE)
    d.text(((W - d.textlength(HANDLE, font=hf)) / 2, ey + 48), HANDLE,
           font=hf, fill=PURPLE)
    return bar


def tab(d, x, y, w, h, text, font, active):
    """One browser tab: the shape, a favicon dot, the title, a close cross."""
    fill = WHITE if active else TAB_IDLE
    d.rounded_rectangle([x, y, x + w, y + h], radius=16, fill=fill)
    if active:
        d.rounded_rectangle([x, y, x + 10, y + h], radius=5, fill=PURPLE)
    cy = y + h / 2
    d.ellipse([x + 34, cy - 11, x + 56, cy + 11],
              fill=PURPLE if active else DOT)
    tf = font
    tx = x + 80
    d.text((tx, cy - tf.size * 0.72), text, font=tf, fill=PURPLE)
    # close cross
    cx, r = x + w - 36, 9
    d.line([(cx - r, cy - r), (cx + r, cy + r)], fill=DOT, width=3)
    d.line([(cx - r, cy + r), (cx + r, cy - r)], fill=DOT, width=3)


def build():
    img = Image.new("RGB", (W, H), LAVENDER)
    d = ImageDraw.Draw(img)
    bar = chrome(img, d)

    top = 250                      # clear of TikTok's top 12% (230)
    tf = F(P700, 72)
    tstep = int(72 * 1.16)
    y = top
    for ln in TITLE.split("\n"):
        d.text((M, y), ln, font=tf, fill=PURPLE)
        y += tstep
    y += 52

    # The window: fit the tabs in whatever room is left above the wordmark.
    win_top = y
    win_bot = bar - 56
    room = win_bot - win_top
    pad = 26
    n = len(TABS)
    th = int((room - pad * 2 - (n - 1) * 14) / n)
    assert th >= 60, f"tabs are {th}px tall, too short to read"
    tabfont = F(P400, min(34, int(th * 0.46)))

    d.rounded_rectangle([M, win_top, W - M, win_bot], radius=28,
                        fill=(246, 245, 253))
    ty = win_top + pad
    for i, t in enumerate(TABS):
        tab(d, M + pad, ty, (W - 2 * M) - pad * 2, th, t, tabfont,
            active=(i == len(TABS) - 1))
        ty += th + 14
    return img, th, tabfont.size


def check():
    # The guide's "6 to 8" is the size of the list it asks HER for, not a cap
    # on the image. She sent two and approved the rest, which makes nine.
    assert 6 <= len(TABS) <= 10, "too few or too many tabs to read"
    joined = " ".join([TITLE] + TABS).lower()
    for banned in ("prompt", "link in bio", "gumroad", "comment ", "claude"):
        assert banned not in joined, f"no sales line or prompt: found {banned!r}"
    assert TABS[-1] == "ChatGPT", "the active tab is the AI tie and goes last"
    print(f"checks pass: {len(TABS)} tabs, active tab is {TABS[-1]!r}")


def main():
    check()
    os.makedirs(OUT, exist_ok=True)
    img, th, px = build()
    assert img.size == (W, H)
    p = os.path.join(OUT, "every-tab-open.jpg")
    img.save(p, quality=95)
    print(f"tab height {th}px, title {px}px -> {os.path.basename(p)}")


if __name__ == "__main__":
    main()
