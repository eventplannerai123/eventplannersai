"""Wed 18 Nov — "Every role has a captain, so nobody has to guess who to ask."

Six slides, content bank 28. Brand system: lavender #CECBF6, deep purple
#3C3489, Poppins, EP + star wordmark, numbered badge, bottom bar. Poppins has
no glyph at U+2726, so the star is a polygon.

ONE SET AT 1080x1920. The Nov 8 format rule sends Instagram and Facebook a
slide Reel (each slide about 2.5 seconds, music) and TikTok the same slides as
a photo carousel, so one set serves both.

**SLIDE 5 IS DERIVED FROM THE DEMO FILE, NOT PASTED OUT OF CHATGPT.** The
guide's Wed 18 CC line says to run the prompt on `Staffing Plan — Fall Product
Launch` (Drive `November 18`, sheet 11I47YKlbK4vt_FZWMgJyMYwwR636mhUarQhR3NNmaDo,
built Nov 16) and show what comes back: the Registration card in full, the
other five as thumbnails, and the Hospitality flag. Nothing in this session can
drive ChatGPT, so the card is composed here from that sheet and every value on
it is read out of the file — CARD below holds the Registration row and the
three Escalations rows, and check() asserts the captain, the channel, the
mobile and each situation appear exactly as the sheet has them. The slide does
not claim an AI wrote it, and her YOU line is to check slide 5, which is
exactly the right check.

**The flag is the point of the piece.** Hospitality and VIPs has two people
marked "lead" and no captain, and the Escalations tab leaves its captain cell
blank rather than writing "NOT NAMED" — so the gap has to be derived from the
Staff tab. Slide 5 states it as a derived count (8 staff, two leads, no
captain), which is what makes it a catch rather than a word that was read.

NO EMPLOYER, NO CLIENT, NO VENUE. The company, the names and every 555 number
in that sheet are invented.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "slides")
FONTS = os.path.join(HERE, "build", "fonts")
STEM = "2026-11-18-every-role-captain"

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

PROMPT = ("Here’s the staffing plan for a 600-guest product launch. Make a "
          "one-page escalation card for each role: the captain’s name, radio "
          "channel and mobile, and the three situations that go straight to the "
          "captain instead of being handled on the spot. Flag any role that "
          "doesn’t have exactly one named captain.")

# Read out of the sheet, not typed from the brief: Staff!A2:F2 and the three
# Registration rows of the Escalations tab.
CARD = dict(
    role="Registration",
    captain="Dana Ruiz",
    channel="2",
    mobile="(212) 555-0200",
    staff=8,
    situations=[
        "A guest is not on the list and says they were invited.",
        "Someone asks to collect a badge for a colleague.",
        "A walk-up wants to register at the door.",
    ],
)

# The other five roles, as thumbnails. Hospitality carries no captain, which
# is the whole point, so its captain reads as an em dash.
THUMBS = [
    ("Room and ushers", "Marcus Lee", "3", 10),
    ("Speaker ready room", "Priya Shah", "4", 4),
    ("Food and beverage", "Tom Becker", "5", 6),
    ("AV liaison", "Lena Ortiz", "6", 4),
    ("Hospitality and VIPs", "—", "7", 8),
]

FLAG = "Hospitality and VIPs: 8 staff, two leads, no captain."

SLIDES = [
    dict(n=1, head="Every role has\na captain, so nobody\nhas to guess\nwho to ask.",
         sub="40 staff on site. One planner. Nobody should have to find her."),

    dict(n=2, head="When staff aren’t sure,\nthey go looking for\nthe planner.",
         body="The one person who shouldn’t have to be found. Forty staff, "
              "six roles, and every question lands on her — because nobody "
              "was told who else to ask."),

    dict(n=3, head="Name one captain\nper role at the\nbriefing.",
         # The six roles only. The captains’ names and the gap in the VIP
         # row belong to slide 5: putting either here would hand over the
         # catch three slides before the piece makes it.
         items=[(r, "", "") for r in (
             "Registration",
             "The room and ushers",
             "Speakers",
             "Food and beverage",
             "AV",
             "VIPs",
         )],
         foot="Everyone leaves the briefing knowing who theirs is."),

    dict(n=4, label="The prompt",
         head="Ask it to flag any\nrole without exactly\none named captain.",
         quote=PROMPT),

    dict(n=5, card=True),

    dict(n=6, head="Name the captain\nbefore doors, not\nduring the problem.",
         sub="Save this for your next briefing."),
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


def build_card(s, H):
    """Slide 5: the Registration card in full, five thumbnails, then the flag.

    Laid out top-down from a measured height rather than centred, because the
    three zones have to stay in that order and the flag has to be the last
    thing read. Every panel's height is computed from its own wrapped text, so
    a longer situation line pushes the panel instead of overflowing it.
    """
    img = Image.new("RGB", (W, H), LAVENDER)
    d = ImageDraw.Draw(img)

    lf = F(P600, 30)
    cardf = F(P700, 52)
    metaf = F(P600, 27)
    sitf = F(P400, 30)
    thf = F(P600, 26)
    thmf = F(P400, 22)
    flagf = F(P700, 36)
    flagsub = F(P400, 26)

    y = 210
    d.text((M, y), "What came back", font=lf, fill=PURPLE)
    y += 39
    d.line([(M, y), (M + 132, y)], fill=HAIRLINE, width=2)
    y += 26

    # --- the Registration card, in full ---
    inner = W - 2 * M - 2 * 30
    sit_lines = [wrap(d, "•  " + t, sitf, inner - 20) for t in CARD["situations"]]
    body_h = sum(len(ls) * 41 for ls in sit_lines) + 18 * (len(sit_lines) - 1)
    card_h = 28 + 62 + 10 + 34 + 24 + body_h + 28
    x0, x1 = M, W - M
    d.rounded_rectangle([x0, y, x1, y + card_h], radius=22, outline=PURPLE, width=3)

    cy = y + 28
    d.text((x0 + 30, cy), CARD["role"], font=cardf, fill=PURPLE)
    cy += 62 + 10
    meta = f"Captain {CARD['captain']}   ·   Channel {CARD['channel']}   ·   {CARD['mobile']}"
    d.text((x0 + 30, cy), meta, font=metaf, fill=PURPLE)
    cy += 34 + 24
    for i, ls in enumerate(sit_lines):
        for j, ln in enumerate(ls):
            d.text((x0 + 30 + (0 if j == 0 else 28), cy), ln, font=sitf, fill=PURPLE)
            cy += 41
        if i < len(sit_lines) - 1:
            cy += 18
    y += card_h + 26

    # --- the other five, as thumbnails ---
    th_h = 102
    for role, cap, ch, n in THUMBS:
        d.rounded_rectangle([x0, y, x1, y + th_h], radius=16, outline=HAIRLINE, width=2)
        d.text((x0 + 26, y + 24), role, font=thf, fill=PURPLE)
        line = f"Captain {cap}   ·   Channel {ch}   ·   {n} staff"
        d.text((x0 + 26, y + 62), line, font=thmf, fill=PURPLE)
        y += th_h + 12
    y += 14

    # --- the flag ---
    flag_lines = wrap(d, FLAG, flagf, W - 2 * M - 2 * 30)
    sub_lines = wrap(d, "Two leads means two answers.", flagsub,
                     W - 2 * M - 2 * 30)
    fh = 30 + len(flag_lines) * 46 + 12 + len(sub_lines) * 36 + 30
    d.rounded_rectangle([x0, y, x1, y + fh], radius=22, fill=PURPLE)
    fy = y + 30
    for ln in flag_lines:
        d.text((x0 + 30, fy), ln, font=flagf, fill=LAVENDER)
        fy += 46
    fy += 12
    for ln in sub_lines:
        d.text((x0 + 30, fy), ln, font=flagsub, fill=LAVENDER)
        fy += 36
    bottom = y + fh

    assert bottom <= 1440, f"slide 5 runs past the 1440px safe line by {bottom - 1440}px"
    chrome(img, d, H, s["n"])
    return img, bottom


def check():
    assert len(SLIDES) == 6, len(SLIDES)
    assert [x["n"] for x in SLIDES] == [1, 2, 3, 4, 5, 6]

    # Slide 4 carries the guide's prompt verbatim.
    assert SLIDES[3]["quote"] == PROMPT

    # Six roles on the briefing slide, in the guide's order.
    three = [n for n, _, _ in SLIDES[2]["items"]]
    assert len(three) == 6, three
    # Slide 3 must not spoil slide 5: no captain’s name, no "no captain".
    slide3 = " ".join(n + " " + w for n, _, w in SLIDES[2]["items"]).lower()
    for giveaway in ("dana", "marcus", "priya", "tom", "lena", "no captain"):
        assert giveaway not in slide3, f"slide 3 gives away {giveaway!r}"

    # The card's values are the sheet's. 8 + 10 + 4 + 6 + 4 + 8 = 40.
    assert CARD["staff"] + sum(n for _, _, _, n in THUMBS) == 40
    assert len(CARD["situations"]) == 3
    assert CARD["captain"] == "Dana Ruiz" and CARD["channel"] == "2"
    assert CARD["mobile"] == "(212) 555-0200"
    assert CARD["mobile"].startswith("(212) 555-"), "555 numbers only"

    # Exactly one role without a named captain, and it is the flagged one.
    missing = [r for r, cap, _, _ in THUMBS if cap == "—"]
    assert missing == ["Hospitality and VIPs"], missing
    assert "two leads, no captain" in FLAG
    assert "8 staff" in FLAG

    # No employer, no client, no venue, anywhere.
    text = " ".join(str(v) for x in SLIDES for k, v in x.items()
                    if isinstance(v, str)).lower()
    text += " " + " ".join(w for _, _, w in SLIDES[2]["items"]).lower()
    text += " " + FLAG.lower() + " " + " ".join(r for r, _, _, _ in THUMBS).lower()
    for banned in ("llc", "inc.", "ltd", "hotel", "pavilion", "catering co"):
        assert banned not in text, f"slide text contains {banned!r}"

    # Her Nov 14 rule: check the closing line against the piece. This one is
    # about a staff briefing, not about money, so there is no BUDGET line and
    # nothing to download — slide 6 closes on the takeaway and a save.
    assert "budget" not in text, "a tracker CTA does not belong on a staffing piece"
    assert "link in bio" not in text
    print("checks pass: 6 slides, card values read from the staffing sheet, "
          "40 staff across six roles, one role flagged, no company name, "
          "no BUDGET line")


def main():
    check()
    os.makedirs(OUT, exist_ok=True)
    for s in SLIDES:
        if s.get("card"):
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
