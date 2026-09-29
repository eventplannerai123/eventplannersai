#!/usr/bin/env python3
"""Three AV quotes for the same 200-person conference, priced so the headline
order and the real order disagree. Every total is computed from the line items
below, and the answer key is generated from the same numbers, so the key cannot
drift from the documents."""
import html, os, subprocess, json

TAX = 0.08875          # NYC combined rate
HERE = os.path.dirname(os.path.abspath(__file__))

SPEC = """One-day conference, 200 attendees. Main ballroom general session
08:00-17:00, two breakout rooms 10:00-15:00. Load-in from 06:00, strike
complete by 19:00. Venue: hotel ballroom, house rigging points available."""

# (label, amount, note)   note=None means it is a plain included line
VENDORS = [
 dict(
  name="Meridian AV Group", ref="Q-4471", style="equipment rental",
  tagline="Equipment Rental Quote — Main Ballroom",
  headline_note="Equipment rental only. Labor, power and rigging quoted separately.",
  quoted=[  # what the headline total is built from
    ("12ft x 7ft fast-fold screen with dress kit", 450.00),
    ("10,000 lumen laser projector", 1200.00),
    ("Line array, 4 tops + 2 subs", 950.00),
    ("24-channel digital mixing console", 375.00),
    ("Wireless handheld microphones (4 @ $80)", 320.00),
    ("Wireless lavalier microphones (2 @ $90)", 180.00),
    ('55" confidence monitor', 275.00),
    ("Presentation switcher", 425.00),
    ("Uplighting, 12 fixtures", 600.00),
    ("Stage wash, 6 fixtures", 450.00),
  ],
  quoted_extra=[("Delivery and pickup", 425.00)],
  service_charge=("Production service charge, 22% of equipment rental", 0.22),
  # required for THIS event but not in the headline number
  excluded=[
    ("Breakout rooms (2) — projector, screen, audio, per room $1,150", 2300.00, "equipment"),
    ("Labor: 42 technician-hours @ $85 (load-in crew 4x4h, show ops 2x9h, strike 4x2h)", 3570.00, "flat"),
    ("Power distribution", 450.00, "flat"),
    ("Rigging, 2 motor points", 650.00, "flat"),
    ("Venue rigger fees, billed by hotel (quoted range $1,200-$1,800)", 1500.00, "flat"),
  ],
  excluded_note="Sales tax not included in any figure on this quote.",
  taxed=True,
 ),
 dict(
  name="Clearline Event Technologies", ref="CL-2026-1188", style="production package",
  tagline="Production Quote — Ballroom and Breakouts",
  headline_note="Labor, delivery, power distribution and rigging are included.",
  quoted=[
    ("Ballroom package: screen, 10,000 lumen projector, line array, console,\n        4 handheld, 2 lavalier, confidence monitor, switcher", 5850.00),
    ("Breakout room package (2 @ $975): projector, screen, audio, 1 handheld", 1950.00),
    ("Lighting: uplighting 12 fixtures, stage wash 6 fixtures", 900.00),
    ("Labor — crew of 3, load-in through strike", 0.00),
    ("Delivery, setup and strike", 0.00),
    ("Power distribution", 0.00),
    ("Rigging, house points", 0.00),
  ],
  quoted_extra=[],
  service_charge=None,
  excluded=[
    ("On-site overtime beyond 10 hours: 3 crew x 3 hours @ $95", 855.00, "flat"),
  ],
  optional=[
    ("Recording or live stream package", 1450.00, "not required for this event"),
    ("Damage waiver, 4% — declinable", None, "declined"),
  ],
  excluded_note="Sales tax shown separately below.",
  taxed=True,
 ),
 dict(
  name="Stagecraft Productions", ref="SP-9930", style="all inclusive",
  tagline="ALL-INCLUSIVE CONFERENCE AV PACKAGE",
  headline_note="One price. Ballroom, both breakouts, all labor, delivery, rigging and power.",
  quoted=[
    ("Complete conference AV package — ballroom + 2 breakouts, all labor,\n        delivery, rigging and power distribution included", 12400.00),
  ],
  quoted_extra=[],
  service_charge=None,
  excluded=[
    ("Projector upgrade: package includes 5,000 lumens, under-spec for a\n        200-person ballroom with house lights up — 10,000 lumen upgrade", 875.00, "equipment"),
    ("Additional wireless handhelds: 2 included, 4 required (2 @ $95)", 190.00, "equipment"),
  ],
  post_charges=[
    ("Production coordination fee, 20% of package including add-ons", 0.20),
    ("Damage waiver, 5% — mandatory, not declinable", 0.05),
  ],
  excluded_note="Coordination fee, damage waiver and sales tax are applied to the final figure.",
  taxed=True,
 ),
]

def money(x): return f"${x:,.2f}"

def compute(v):
    """Returns (headline, real_total, workings) — every figure derived here."""
    w = []
    equip = sum(a for _, a in v['quoted'])
    extra = sum(a for _, a in v.get('quoted_extra', []))
    if v['service_charge']:
        _, rate = v['service_charge']
        sc_headline = equip * rate
    else:
        sc_headline = 0.0
    headline_sub = equip + extra + sc_headline
    headline = headline_sub if not v.get('post_charges') else headline_sub
    w.append(("Quoted equipment / package", equip))
    if extra: w.append(("Quoted extras on the page", extra))
    if sc_headline: w.append((v['service_charge'][0], sc_headline))

    # ---- real total ----
    add_equip = sum(a for _, a, k in v['excluded'] if k == 'equipment')
    add_flat  = sum(a for _, a, k in v['excluded'] if k == 'flat')
    for label, amt, _ in v['excluded']:
        w.append(("REQUIRED, not in the headline: " + label.replace("\n        ", " "), amt))

    if v['service_charge']:
        _, rate = v['service_charge']
        sc_real = (equip + add_equip) * rate
        w.append((f"{v['service_charge'][0]} — recalculated on the breakout equipment too", sc_real))
        sub = equip + add_equip + extra + sc_real + add_flat
    else:
        sub = equip + add_equip + extra + add_flat

    for label, rate in v.get('post_charges', []):
        amt = sub * rate
        w.append((label, amt))
        sub += amt

    tax = sub * TAX if v['taxed'] else 0.0
    w.append((f"Sales tax {TAX*100:.3f}%", tax))
    return headline + (headline_sub * 0 ), sub + tax, w, headline_sub

# ---------------------------------------------------------------- rendering
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle, KeepTogether)

ss = getSampleStyleSheet()
H   = ParagraphStyle('H', parent=ss['Normal'], fontName='Helvetica-Bold', fontSize=16, leading=19)
SUB = ParagraphStyle('SUB', parent=ss['Normal'], fontSize=8.5, leading=11, textColor=colors.HexColor('#555555'))
SPECS = ParagraphStyle('SPECS', parent=ss['Normal'], fontSize=8.5, leading=11.5, textColor=colors.HexColor('#333333'))
BAND = ParagraphStyle('BAND', parent=ss['Normal'], fontName='Helvetica-Bold', fontSize=10, leading=13)
CELL = ParagraphStyle('CELL', parent=ss['Normal'], fontSize=9, leading=11.5)
NOTE = ParagraphStyle('NOTE', parent=ss['Normal'], fontSize=8.5, leading=11.5, textColor=colors.HexColor('#333333'))
NOTEB= ParagraphStyle('NOTEB', parent=NOTE, fontName='Helvetica-Bold')

def band(text):
    t = Table([[Paragraph(text, BAND)]], colWidths=[6.9*inch])
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),colors.HexColor('#EFEFEF')),
                           ('LEFTPADDING',(0,0),(-1,-1),7),('TOPPADDING',(0,0),(-1,-1),5),
                           ('BOTTOMPADDING',(0,0),(-1,-1),5)]))
    return t

def lines_table(rows, total=None):
    data = [[Paragraph(l.replace("\n        ", "<br/>&nbsp;&nbsp;&nbsp;&nbsp;"), CELL),
             Paragraph(v, ParagraphStyle('R', parent=CELL, alignment=2))] for l, v in rows]
    style = [('VALIGN',(0,0),(-1,-1),'TOP'),
             ('LINEBELOW',(0,0),(-1,-1 if total is None else -2),0.4,colors.HexColor('#DDDDDD')),
             ('TOPPADDING',(0,0),(-1,-1),3.5),('BOTTOMPADDING',(0,0),(-1,-1),3.5),
             ('LEFTPADDING',(0,0),(-1,-1),2)]
    if total:
        data.append([Paragraph(f"<b>{total[0]}</b>", ParagraphStyle('T', parent=CELL, fontSize=11.5)),
                     Paragraph(f"<b>{total[1]}</b>", ParagraphStyle('TR', parent=CELL, fontSize=11.5, alignment=2))])
        style += [('LINEABOVE',(0,-1),(-1,-1),1.1,colors.black),
                  ('TOPPADDING',(0,-1),(-1,-1),7)]
    t = Table(data, colWidths=[5.35*inch, 1.55*inch])
    t.setStyle(TableStyle(style))
    return t

def build_pdf(v, path):
    headline_sub = compute(v)[3]
    doc = SimpleDocTemplate(path, pagesize=LETTER, title=f"{v['name']} — AV Quote",
                            author=v['name'], leftMargin=0.8*inch, rightMargin=0.8*inch,
                            topMargin=0.7*inch, bottomMargin=0.7*inch)
    f = [Paragraph(v['name'], H), Spacer(1, 2),
         Paragraph(f"{v['tagline']} &nbsp;·&nbsp; Quote ref {v['ref']} &nbsp;·&nbsp; Valid 30 days", SUB),
         Spacer(1, 9),
         Paragraph("<b>Event:</b> " + SPEC.replace("\n", " "), SPECS), Spacer(1, 11),
         band("QUOTED"), Spacer(1, 5)]

    rows = [(l, 'included' if a == 0 else money(a)) for l, a in v['quoted']]
    rows += [(l, money(a)) for l, a in v.get('quoted_extra', [])]
    if v['service_charge']:
        equip = sum(a for _, a in v['quoted'])
        rows.append((v['service_charge'][0], money(equip * v['service_charge'][1])))
    f += [lines_table(rows, total=("QUOTE TOTAL", money(headline_sub))), Spacer(1, 8),
          Paragraph(v['headline_note'], NOTEB), Spacer(1, 12),
          band("NOT INCLUDED IN THE ABOVE"), Spacer(1, 5)]

    ex = [(l, money(a)) for l, a, _ in v['excluded']]
    ex += [(f"{l} <i>({why})</i>", money(a) if a else "—") for l, a, why in v.get('optional', [])]
    ex += [(l, "applied below") for l, _ in v.get('post_charges', [])]
    f += [lines_table(ex), Spacer(1, 8), Paragraph(v['excluded_note'], NOTE)]
    doc.build(f)

for v in VENDORS:
    out = os.path.join(HERE, f"quote_{v['name'].split()[0].lower()}.pdf")
    build_pdf(v, out)
    print("wrote", os.path.basename(out))

# ---------------------------------------------------------------- answer key
results = []
for v in VENDORS:
    _, real, workings, headline = compute(v)
    results.append((v['name'], headline, real, workings))

by_head = sorted(results, key=lambda x: x[1])
by_real = sorted(results, key=lambda x: x[2])

out = ["# Answer key — three AV quotes, Oct 1",
       "",
       "Generated by `build_quotes.py` from the same line items the PDFs are",
       "rendered from, so it cannot drift from the documents. Sales tax is",
       f"{TAX*100:.3f}% throughout.", "",
       "## The result the piece turns on", "",
       "| | Quoted on the page | Real cost for this event |",
       "| --- | --- | --- |"]
for n, h, r, _ in results:
    out.append(f"| {n} | {money(h)} | **{money(r)}** |")
out += ["",
        f"- Headline order: {'  <  '.join(n for n, *_ in by_head)}",
        f"- **Real order: {'  <  '.join(n for n, *_ in by_real)}**",
        "",
        f"The cheapest-looking quote ({by_head[0][0]}, {money(by_head[0][1])}) is "
        f"**{money(by_head[0][2] - by_real[0][2])} more expensive** than the one that "
        f"actually wins. The gap between the headline and the real cost is "
        f"{money(by_head[0][2] - by_head[0][1])} on that quote alone.", ""]

for n, h, r, w in results:
    out += [f"## {n}", "", f"Quoted: **{money(h)}** → real: **{money(r)}**", "",
            "| Line | Amount |", "| --- | --- |"]
    for label, amt in w:
        out.append(f"| {label} | {money(amt)} |")
    out += ["", f"| **Real total** | **{money(r)}** |", "| --- | --- |", ""]

out += ["## What each one hides", "",
        "- **Meridian** — a genuine equipment-rental quote read as a full quote. "
        "The headline covers the ballroom only: no breakout rooms, no labor, no "
        "power, no rigging. The 22% service charge also recalculates upward once "
        "the breakout equipment is added, which is the detail most likely to be missed.",
        "- **Clearline** — nearly complete, and the only real gap is overtime: "
        "load-in 06:00 to strike 19:00 is 13 hours against the 10 included. The "
        "recording package and damage waiver are exclusions that are *not* hidden "
        "costs, because this event does not need them — a good test of whether the "
        "model separates 'excluded' from 'required'.",
        "- **Stagecraft** — 'all inclusive' is the trap. A 20% coordination fee and "
        "a non-declinable 5% damage waiver both compound on top of the add-ons, and "
        "the included projector is 5,000 lumens, under-spec for a 200-person "
        "ballroom, so the upgrade is not optional.", ""]

open(os.path.join(HERE, "ANSWER-KEY.md"), "w").write("\n".join(out))
print()
for n, h, r, _ in results:
    print(f"{n:<32} quoted {money(h):>12}   real {money(r):>12}")
print()
print("headline:", " < ".join(n for n, *_ in by_head))
print("real:    ", " < ".join(n for n, *_ in by_real))
