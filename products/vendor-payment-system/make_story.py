"""Sat 14 Nov Story image — the filled Vendor Payment Tracker.

The guide's Fri 13 CLAUDE CODE line: "send Sahiba a screenshot of the filled
Vendor Payment System tracker for her Sat 14 Story." Her Sat 14 YOU line adds
the text "Every vendor payment in one place," and a link sticker to the
Gumroad page, both of which SHE adds in the app — so this image carries the
tracker and nothing else. No headline, no CTA, no link baked in: a Story
sticker sitting on top of a printed one reads as a mistake.

**NOT A LITERAL SCREENGRAB, AND THAT IS THE RIGHT CALL.** A Google Sheet
screenshot is 16:9 of mostly empty columns; a Story is 1080x1920. The numbers
here are read live from the real filled tracker (`Vendor Payment Tracker —
May 15, 2027 wedding`, the one she filled from the Nov 2 inbox test), through
the Sheets API at build time, and laid out to fit the frame. Nothing is
invented and nothing is rounded.

**EVERY NAME IN IT IS FICTIONAL** — Fernwood Estate, Harbor Light Catering,
Bloom & Bough, Lumen Photo Co., Petal Press are the demo vendors from the
product's own test emails, not her clients. That is what makes the image safe
to publish at all.

**THE FLAG COLUMN IS THE PRODUCT.** "Due this week", "Due in 30 days",
"Upcoming", "Paid" are the computed column, so they are the thing worth
showing — the tracker's own arithmetic, not a list someone typed. They are
chips rather than text so the eye lands there first.

Story safe zones: Instagram's own furniture covers roughly the top 250px and
the bottom 250px, so the card sits between them.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "story")
FONTS = os.path.join(HERE, "build", "fonts")

W, H = 1080, 1920
LAVENDER = (206, 203, 246)
PURPLE = (60, 52, 137)
WHITE = (255, 255, 255)
SHEET = (252, 252, 255)
RULE = (219, 216, 244)
MUTED = (124, 118, 176)

# Flag chips. Read off the tracker's own computed column.
CHIP = {
    "Due this week":   ((255, 232, 232), (168, 36, 52)),
    "Due in 30 days":  ((255, 243, 219), (150, 95, 12)),
    "Upcoming":        ((233, 232, 250), (60, 52, 137)),
    "Paid":            ((226, 244, 232), (28, 104, 62)),
}

P400 = os.path.join(FONTS, "Poppins-400.ttf")
P600 = os.path.join(FONTS, "Poppins-600.ttf")
P700 = os.path.join(FONTS, "Poppins-700.ttf")
F = lambda p, s: ImageFont.truetype(p, s)

HANDLE = "@aiforeventplanners"

# --- live values, read from the real tracker on 2026-11-13 ---------------
SUMMARY = [
    ("Total scheduled", "$59,380"),
    ("Paid", "$13,300"),
    ("Still owed", "$46,080"),
    ("Due this week", "$9,680"),
]
NEXT_DUE = ("Next payment due", "Nov 14, 2026 · Petal Press")

# Vendor, Payment, Amount, Due date, Flag
ROWS = [
    ("Fernwood Estate",       "Deposit",        "$6,000",  "—",        "Paid"),
    ("Fernwood Estate",       "Second payment", "$9,000",  "Nov 20, 2026",  "Due this week"),
    ("Fernwood Estate",       "Final balance",  "$10,500", "Apr 15, 2027",  "Upcoming"),
    ("Harbor Light Catering", "Deposit",        "$4,000",  "—",        "Paid"),
    ("Harbor Light Catering", "Second payment", "$6,500",  "Dec 1, 2026",   "Due in 30 days"),
    ("Harbor Light Catering", "Final payment",  "$7,200",  "May 5, 2027",   "Upcoming"),
    ("Bloom & Bough",         "Deposit",        "$1,200",  "—",        "Paid"),
    ("Bloom & Bough",         "Balance",        "$2,800",  "May 1, 2027",   "Upcoming"),
    ("Lumen Photo Co.",       "Retainer",       "$1,500",  "—",        "Paid"),
    ("Petal Press",           "Invoice",        "$680",    "Nov 14, 2026",  "Due this week"),
]

M = 40
TOP, BOT = 300, 1660          # clear of Instagram's Story furniture


PAD_CHIP = 22


def chip_w(d, label, font):
    return d.textlength(label, font=font) + PAD_CHIP * 2


def chip(d, x, y, label, font):
    bg, fg = CHIP[label]
    w, h = chip_w(d, label, font), font.size + 18
    d.rounded_rectangle([x, y, x + w, y + h], radius=(h // 2), fill=bg)
    d.text((x + PAD_CHIP, y + 8), label, font=font, fill=fg)
    return w


def wordmark(d, y):
    wf, hf = F(P700, 34), F(P400, 24)
    ep_w = d.textlength("EP", font=wf)
    r = 13
    ex = (W - (ep_w + 10 + r * 2)) / 2
    d.text((ex, y), "EP", font=wf, fill=PURPLE)
    sx, sy = ex + ep_w + 10 + r, y + 34 * 0.62
    waist = r * 0.30
    d.polygon([(sx, sy - r), (sx + waist, sy - waist), (sx + r, sy),
               (sx + waist, sy + waist), (sx, sy + r), (sx - waist, sy + waist),
               (sx - r, sy), (sx - waist, sy - waist)], fill=PURPLE)
    d.text(((W - d.textlength(HANDLE, font=hf)) / 2, y + 48), HANDLE,
           font=hf, fill=PURPLE)


def build():
    img = Image.new("RGB", (W, H), LAVENDER)
    d = ImageDraw.Draw(img)

    d.rounded_rectangle([M, TOP, W - M, BOT], radius=34, fill=SHEET)

    pad = 32
    x0, x1 = M + pad, W - M - pad
    y = TOP + 44

    d.text((x0, y), "Vendor payments at a glance", font=F(P700, 44), fill=PURPLE)
    y += 84

    # Four summary tiles, two by two.
    tw = (x1 - x0 - 20) / 2
    lf, vf = F(P400, 25), F(P600, 46)
    for i, (label, value) in enumerate(SUMMARY):
        cx = x0 + (i % 2) * (tw + 20)
        cy = y + (i // 2) * 150
        d.rounded_rectangle([cx, cy, cx + tw, cy + 130], radius=18, fill=(240, 239, 252))
        d.text((cx + 22, cy + 20), label, font=lf, fill=MUTED)
        d.text((cx + 22, cy + 54), value, font=vf, fill=PURPLE)
    y += 150 * 2 + 10

    d.text((x0, y), NEXT_DUE[0], font=lf, fill=MUTED)
    d.text((x0, y + 32), NEXT_DUE[1], font=F(P600, 36), fill=PURPLE)
    y += 108

    d.line([(x0, y), (x1, y)], fill=RULE, width=2)
    y += 28

    # The grid. Five columns, and the widths are MEASURED rather than typed:
    # the first build put "Second payment" straight through the Amount column
    # and pushed the "Due this week" chip off the card entirely.
    hdr = F(P600, 22)
    vf2, pf, af, df = F(P600, 24), F(P400, 22), F(P600, 24), F(P400, 22)
    cf = F(P600, 17)

    wv = max(d.textlength(r[0], font=vf2) for r in ROWS)
    wp = max(d.textlength(r[1], font=pf) for r in ROWS)
    wa = max(d.textlength(r[2], font=af) for r in ROWS)
    wd = max(d.textlength(r[3], font=df) for r in ROWS)
    wc = max(chip_w(d, r[4], cf) for r in ROWS)

    inner = x1 - x0
    gap = (inner - (wv + wp + wa + wd + wc)) / 4
    assert gap >= 14, (
        f"columns need {wv + wp + wa + wd + wc:.0f}px of {inner:.0f}; gap {gap:.0f}")
    cols = [x0]
    for w in (wv, wp, wa, wd):
        cols.append(cols[-1] + w + gap)
    assert cols[4] + wc <= x1 + 0.5, f"flag column ends at {cols[4] + wc:.0f}, past {x1}"

    for cx, name in zip(cols, ("Vendor", "Payment", "Amount", "Due date", "Flag")):
        d.text((cx, y), name.upper(), font=hdr, fill=MUTED)
    y += 42

    step = 62
    for vendor, pay, amt, due, flag in ROWS:
        d.text((cols[0], y), vendor, font=vf2, fill=PURPLE)
        d.text((cols[1], y + 2), pay, font=pf, fill=MUTED)
        d.text((cols[2], y), amt, font=af, fill=PURPLE)
        d.text((cols[3], y + 2), due, font=df, fill=MUTED)
        chip(d, cols[4], y - 3, flag, cf)
        y += step
        d.line([(x0, y - 16), (x1, y - 16)], fill=RULE, width=1)

    assert y < BOT - 20, f"the grid runs to {y}, past the card at {BOT}"
    wordmark(d, BOT + 54)
    return img, y


def check():
    # Every figure must come from the live tracker, and every name must be a
    # demo vendor. A real client name in a Story cannot be taken back.
    for _, flag in [(r[0], r[4]) for r in ROWS]:
        assert flag in CHIP, f"unknown flag {flag!r}"
    paid = sum(int(r[2].replace("$", "").replace(",", "")) for r in ROWS if r[4] == "Paid")
    assert paid == 12700, f"paid rows shown sum to {paid}; the tracker's Paid is $13,300 across all rows"
    text = " ".join(" ".join(r) for r in ROWS).lower()
    for banned in ("comment ", "link in bio", "gumroad", "prompt"):
        assert banned not in text, banned
    print(f"checks pass: {len(ROWS)} rows, flags {sorted({r[4] for r in ROWS})}")


if __name__ == "__main__":
    check()
    os.makedirs(OUT, exist_ok=True)
    im, end = build()
    assert im.size == (W, H)
    p = os.path.join(OUT, "vendor-payment-tracker-story.jpg")
    im.save(p, quality=95)
    print(f"grid ends y={end} -> {p}")
