"""Week four's demo files, built Wed 11 so both exist before she records.

  Mon 16  Registration Export — Annual Partner Weekend  (Google Sheet)
  Tue 17  BEO — Winter Partner Summit                   (PDF, 14 pages)

EVERY COMPANY, VENUE AND PERSON HERE IS INVENTED. No real client, venue or
employer appears, which is the standing rule and also what makes these safe in
a public repo — Drive fetches them from a raw.githubusercontent URL.

THE ARITHMETIC IS RECOMPUTED, NOT TRUSTED, because each piece is about a
number the guide has already promised:

  Mon 16  3,500 rows but 3,388 people, so 112 duplicate registrations come
          out; 96 spellings of 61 organisations; and five guest-type codes
          totalling 3,388 — 2,540 DEL, 510 SPO, 96 SPK, 162 STF, 80 VIP.
  Tue 17  eleven times spread over eleven of the fourteen pages, three
          headcounts, four vendor numbers in the footers, and $64,800 of food
          and beverage that becomes $87,483.24 once service and tax are on.

The registration export is the one that can go wrong quietly. The Reel turns
on ChatGPT reporting 112 removed rows and 3,388 tags, so the builder asserts
the row count, the duplicate count, that every duplicate pair really is the
same email twice and nothing else is, the five code totals, and that the
organisation spellings collapse to exactly 61 names. A 113th accidental
duplicate would make the guide's answer wrong and would not be visible by
looking at the sheet.

The BEO is the opposite problem: nothing in it is hard to compute, but the
piece only works if the eleven times really are scattered rather than listed,
so the builder asserts that no page carries more than two of them and that
the first page carries none.
"""
import os
import random

from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas

from make_demo_files import Page, money, L, R, W, H, INK, GREY

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "files")

LAVENDER = "CECBF6"
PURPLE = "3C3489"

# ================================================================ Mon 16 ====
ROWS = 3_500
DUPES = 112
PEOPLE = ROWS - DUPES                      # 3,388
CODES = [("DEL", 2_540), ("SPO", 510), ("SPK", 96), ("STF", 162), ("VIP", 80)]
ORGS_CANONICAL = 61
ORG_SPELLINGS = 96

# Free text as the attendees typed it: 14 spellings of five types.
TYPE_WORDS = {
    "DEL": ["Delegate", "delegate", "DELEGATE", "Attendee"],
    "SPO": ["Sponsor", "sponsor", "SPONSOR"],
    "SPK": ["Speaker", "speaker"],
    "STF": ["Staff", "staff", "Internal"],
    "VIP": ["VIP", "Vip"],
}

FIRST = """Amara Priya Devon Marisol Tobias Nadia Everett Imani Soren Thalia Caleb
Rosalind Mateo Yuki Desmond Fenella Ayaan Bronwen Lucian Odette Rafferty Saoirse
Emeka Juniper Kieran Anouk Hugo Linnea Dashiell Oona Tarik Marguerite Ivo Delphine
Casper Mirabel Anders Zahra Leopold Sunniva Bastian Elowen Rasmus Wren Octavian
Ingrid Florian Niamh Kwame Sylvie Radek Clemence Ottoline Bo Henrike Idris Cleo
Jarrah Maeve Ptolemy Vida Wilhelm Xiomara Yannick Zora Alaric Beatrix""".split()

LAST = """Whitlock Arrindell Bellweather Castellane Drummond Ellingham Fairweather
Grimaldi Harkness Ingersoll Jessamy Kilbride Lindqvist Marchetti Nightingale
Oyelaran Pemberton Quayle Rosewood Stavros Thorsby Underhill Vasquez Wexford
Yarrow Zielinski Ashcombe Birkenshaw Calloway Dunmore Esterhazy Fontaine
Galbraith Holloway Ironside Jankowski Kettleborough Larchmont Mowbray Norrington
Osterley Prideaux Quintrell Ravensworth Sandringham Trelawney Urquhart Vandeleur
Winterbourne Yelverton Zabrowski Appleyard Bramhall Cheswick Delacroix""".split()

ORG_STEMS = """Northgate Harbourline Ellerby Vantage Pelham Cardinal Westmere
Thornbury Rivermark Oakhaven Stonebridge Fairlight Greyfriars Ashworth Belmonte
Carraway Dunsmore Everley Foxglove Glenmara Hartwell Inverness Juniperbrook
Kestrel Lanthorn Merrowfield Netherby Orchardson Pinecrest Quillon Redferne
Saltmarsh Tollgate Umberleigh Verity Wrenfield Yoxall Alderney Brackenhill
Crossmoor Dalewood Edgemont Fernleigh Goldcrest Highmoor Ingleby Kingsmead
Larkspur Marchmont Nethercote Oversley Pennyroyal Quarrington Ravensmere
Selkirk Tamarind Underwood Vexley Wychwood Yarmouth Zephyrine""".split()

ORG_SUFFIX = ["Group", "Partners", "Holdings", "Industries", "Logistics",
              "Advisory", "Systems", "Capital", "Laboratories", "Collective"]

TITLES = """Head of Partnerships|Regional Director|Procurement Lead|Chief of Staff
Operations Manager|Programme Director|Senior Analyst|Commercial Director
Head of Marketing|Account Director|Supply Chain Manager|Managing Partner
Director of Engineering|Head of Delivery|Client Services Lead|Finance Manager
Head of People|Strategy Director|Category Manager|Technical Lead""".replace(
    "\n", "|").split("|")


def _mess_case(text, mode):
    if mode == 0:
        return text.upper()
    if mode == 1:
        return text.lower()
    return text


def _org_variants(canonical):
    """A second, messier spelling of the same organisation."""
    stem, suffix = canonical.rsplit(" ", 1)
    # No all-caps variant: it would differ from the canonical name only by
    # case, and a reader counting spellings case-insensitively would then get
    # 91 rather than 96. Every variant here differs by punctuation or by a
    # word, so the count is the same whichever way it is counted.
    return [
        f"{stem} {suffix}.",
        f"{stem}, {suffix}",
        f"The {stem} {suffix}",
        f"{stem} {suffix[:3]}.",
    ]


def build_registration_rows(seed=20261116):
    rnd = random.Random(seed)

    # 61 canonical organisations, and 35 of them also appear under one
    # alternative spelling: 96 raw spellings in all.
    canon = []
    used = set()
    i = 0
    while len(canon) < ORGS_CANONICAL:
        stem = ORG_STEMS[i % len(ORG_STEMS)]
        suffix = ORG_SUFFIX[(i // len(ORG_STEMS)) % len(ORG_SUFFIX)]
        name = f"{stem} {suffix}"
        if name not in used:
            used.add(name)
            canon.append(name)
        i += 1
    variant_of = {}
    for name in canon[: ORG_SPELLINGS - ORGS_CANONICAL]:
        variant_of[name] = rnd.choice(_org_variants(name))

    # One row per person first, with the guest-type codes in the stated counts.
    codes = []
    for code, n in CODES:
        codes += [code] * n
    assert len(codes) == PEOPLE, (len(codes), PEOPLE)
    rnd.shuffle(codes)

    people = []
    emails = set()
    for n, code in enumerate(codes):
        first = FIRST[rnd.randrange(len(FIRST))]
        last = LAST[rnd.randrange(len(LAST))]
        org = canon[rnd.randrange(len(canon))]
        slug = org.split()[0].lower()
        stem = f"{first.lower()}.{last.lower()}@{slug}.com"
        email = stem
        bump = 2
        while email in emails:
            email = f"{first.lower()}.{last.lower()}{bump}@{slug}.com"
            bump += 1
        emails.add(email)
        people.append({
            "first": first, "last": last, "org": org, "email": email,
            "title": TITLES[rnd.randrange(len(TITLES))], "code": code,
        })

    def row_for(p, mode, org_spelling, day):
        return [
            _mess_case(p["first"], mode),
            _mess_case(p["last"], mode),
            _mess_case(p["title"], mode),
            org_spelling,
            p["email"],
            rnd.choice(TYPE_WORDS[p["code"]]),
            f"2027-01-{day:02d}",
        ]

    rows = []
    for n, p in enumerate(people):
        spelling = p["org"]
        if p["org"] in variant_of and n % 3 == 0:
            spelling = variant_of[p["org"]]
        rows.append(row_for(p, n % 3, spelling, 4 + (n % 24)))

    # 112 people register a second time: same email, messier the second time.
    for p in rnd.sample(people, DUPES):
        spelling = variant_of.get(p["org"], p["org"])
        rows.append(row_for(p, 0, spelling, 26 + rnd.randrange(4)))

    rnd.shuffle(rows)
    spellings = {r[3] for r in rows}
    return rows, canon, spellings


def check_registration(rows, canon, spellings):
    assert len(rows) == ROWS, len(rows)

    seen = {}
    for r in rows:
        seen.setdefault(r[4], []).append(r)
    assert len(seen) == PEOPLE, f"{len(seen)} unique emails, not {PEOPLE}"
    twice = [e for e, rs in seen.items() if len(rs) == 2]
    more = [e for e, rs in seen.items() if len(rs) > 2]
    assert not more, f"{len(more)} emails appear more than twice"
    assert len(twice) == DUPES, f"{len(twice)} duplicate registrations, not {DUPES}"

    # Every duplicate pair is the same person: same name once case is ignored.
    for e in twice:
        a, b = seen[e]
        assert (a[0].lower(), a[1].lower()) == (b[0].lower(), b[1].lower()), e

    # The five codes, counted from the free text the rows actually carry.
    word_to_code = {w: c for c, ws in TYPE_WORDS.items() for w in ws}
    assert len(word_to_code) == 14, len(word_to_code)
    counts = {c: 0 for c, _ in CODES}
    for e, rs in seen.items():
        counts[word_to_code[rs[0][5]]] += 1
    for code, n in CODES:
        assert counts[code] == n, f"{code}: {counts[code]} people, not {n}"
    assert sum(counts.values()) == PEOPLE

    # A duplicate's two rows must agree on the guest type, or the split moves.
    for e in twice:
        a, b = seen[e]
        assert word_to_code[a[5]] == word_to_code[b[5]], e

    assert len(canon) == ORGS_CANONICAL, len(canon)
    assert len(spellings) == ORG_SPELLINGS, \
        f"{len(spellings)} organisation spellings, not {ORG_SPELLINGS}"
    # Counted case-insensitively as well, because a reader counting them in a
    # spreadsheet gets the case-insensitive answer and the guide states one
    # number for both.
    assert len({s.lower() for s in spellings}) == ORG_SPELLINGS, \
        "two spellings differ only by case"

    # Messy capitalisation really is in the file, all three ways.
    firsts = [r[0] for r in rows]
    assert any(f.isupper() for f in firsts)
    assert any(f.islower() for f in firsts)
    assert any(f[0].isupper() and not f.isupper() for f in firsts)


def registration_workbook(path, rows):
    from openpyxl import Workbook
    from openpyxl.styles import Alignment, Font, PatternFill
    from openpyxl.utils import get_column_letter

    head_fill = PatternFill("solid", fgColor=LAVENDER)
    head_font = Font(name="Calibri", bold=True, color=PURPLE, size=11)
    title_font = Font(name="Calibri", bold=True, color=PURPLE, size=14)

    wb = Workbook()
    s = wb.active
    s.title = "Registrations"
    s["A1"] = "Annual Partner Weekend — registration export"
    s["A1"].font = title_font
    s["A2"] = "Exported from the registration system. One row per registration."
    s["A2"].font = Font(name="Calibri", italic=True, size=10)
    header = ["First name", "Last name", "Job title", "Organisation",
              "Email", "Guest type", "Registered"]
    s.append([])
    s.append(header)
    for c in range(1, len(header) + 1):
        cell = s.cell(4, c)
        cell.font = head_font
        cell.fill = head_fill
        cell.alignment = Alignment(vertical="center")
    for row in rows:
        s.append(row)
    s.freeze_panes = "A5"
    for c, w in enumerate([16, 20, 30, 30, 38, 14, 13], start=1):
        s.column_dimensions[get_column_letter(c)].width = w

    wb.save(path)
    return path


# ================================================================ Tue 17 ====
GUESTS = 240
BREAKOUT = 120
RECEPTION = 180
SERVICE = 0.24
TAX = 0.08875

FB = [
    ("Breakfast buffet, per person", GUESTS, 38.00),
    ("Coffee break, mid-morning and mid-afternoon, per person per break",
     GUESTS * 2, 23.50),
    ("Plated lunch, per person", GUESTS, 68.00),
    ("Evening reception, canapes and stations, per person", RECEPTION, 104.00),
    ("Four-hour bar package, per person", RECEPTION, 52.00),
]
FB_SUBTOTAL = 64_800.00

# (time, what, room, headcount, page it is printed on)
SCHEDULE = [
    ("6:00am", "Load-in opens", "Dock 3", None, 2),
    ("6:30am", "AV drop and rig", "Grand Ballroom", None, 9),
    ("7:30am", "Breakfast buffet", "Grand Ballroom", GUESTS, 4),
    ("8:00am", "Registration opens", "Foyer", None, 3),
    ("9:00am", "General session", "Grand Ballroom", GUESTS, 4),
    ("11:00am", "Breakout A / Breakout B", "Studio A / Studio B", BREAKOUT, 5),
    ("12:30pm", "Plated lunch", "Grand Ballroom", GUESTS, 6),
    ("2:00pm", "Afternoon session", "Grand Ballroom", GUESTS, 10),
    ("6:00pm", "Evening reception", "Terrace", RECEPTION, 7),
    ("10:30pm", "Bar closes", "Terrace", None, 8),
    ("11:00pm", "AV strike", "Grand Ballroom", None, 9),
]

VENDORS = [
    ("Catering — Harrowgate Hospitality", "Imani Oyelaran", "(212) 555-0148"),
    ("Audio visual — Beaconfield AV", "Tobias Whitlock", "(212) 555-0172"),
    ("Floral and decor — Lanthorn Studio", "Nadia Esterhazy", "(212) 555-0193"),
    ("Rentals — Saltmarsh Event Hire", "Devon Kilbride", "(212) 555-0121"),
]

PAGES = 14


def _footer(c, n):
    """Vendor contacts live in the footers, not in a list on one page."""
    label, who, phone = VENDORS[(n - 1) % len(VENDORS)]
    c.setFillColorRGB(*GREY)
    c.setFont("Helvetica", 7.5)
    c.drawString(L, 0.62 * inch, f"{label} · {who} · {phone}")
    c.setFillColorRGB(*INK)


def beo(path):
    c = canvas.Canvas(path, pagesize=LETTER)
    T = "BEO — Winter Partner Summit"

    def page(n, title):
        p = Page(c, title, n, PAGES)
        _footer(c, n)
        return p

    def line(p, t):
        for item in SCHEDULE:
            if item[0] == t:
                time, what, room, head, _ = item
                head = f"{head} guests" if head else "—"
                p.row(f"{time}   {what}", f"{room}   ·   {head}")

    p = page(1, T)
    p.p("Banquet Event Order · Thursby House · 1 Thursby Place", grey=True)
    p.p("Event date: Tuesday 9 February 2027", grey=True)
    p.gap(0.3)
    p.h("Winter Partner Summit")
    p.p("Client: Northgate Partners (the “Client”)")
    p.p("On-site contact: Marisol Bellweather")
    p.p(f"Expected attendance: {GUESTS} guests")
    p.p("Rooms: Grand Ballroom, Studio A, Studio B, Terrace")
    p.gap(0.3)
    p.p("This order sets out the arrangements agreed for the above event. It", grey=True)
    p.p("supersedes all previous versions. Times, counts and charges appear in", grey=True)
    p.p("the sections to which they relate.", grey=True)
    p.gap(0.3)
    p.h("Contents", 11)
    for t in ["2  Load-in and access", "3  Registration and foyer",
              "4  Morning food and general session", "5  Breakouts",
              "6  Lunch", "7  Evening reception", "8  Bar",
              "9  Audio visual", "10  Afternoon session",
              "11  Guarantee and changes", "12  Charges",
              "13  House rules", "14  Signatures"]:
        p.p(t, size=9.5, gap=0.17)
    c.showPage()

    p = page(2, T + " · Load-in and access")
    p.h("Load-in", 11)
    line(p, "6:00am")
    p.gap(0.22)
    p.p("Dock 3 is the only dock cleared for this event. Vehicles over 26 feet")
    p.p("must be announced to the loading supervisor the day before.")
    p.gap(0.26)
    p.h("Access", 11)
    p.p("Crew entrance on the Thursby Place side, staffed from 5:45am.")
    p.p("Freight lift capacity 3,500 lb; two passes per hour are reserved for")
    p.p("the Client between 6:00am and 8:00am.")
    c.showPage()

    p = page(3, T + " · Registration and foyer")
    p.h("Registration", 11)
    line(p, "8:00am")
    p.gap(0.22)
    p.p("Six tables, skirted, with two chairs each. Power to each table.")
    p.p("Name tags are the Client’s responsibility and are not printed by the")
    p.p("venue. Signage frames are supplied; artwork is the Client’s.")
    p.gap(0.26)
    p.h("Cloakroom", 11)
    p.p("Attended from 7:00am. Charged on the guaranteed count, not on coats.")
    c.showPage()

    p = page(4, T + " · Morning")
    p.h("Breakfast", 11)
    line(p, "7:30am")
    p.gap(0.2)
    p.p("Buffet, three stations. Hot items held in chafing dishes; no eggs")
    p.p("cooked to order. Service concludes at 8:45am.")
    p.gap(0.26)
    p.h("General session", 11)
    line(p, "9:00am")
    p.gap(0.2)
    p.p("Theatre set, centre aisle. Stage 24 ft x 16 ft, 24 in high.")
    p.p("Water service at the stage and on every fourth row.")
    c.showPage()

    p = page(5, T + " · Breakouts")
    p.h("Breakouts", 11)
    line(p, "11:00am")
    p.gap(0.2)
    p.p("Studio A: crescent rounds. Studio B: hollow square.")
    p.p("Both rooms flip from the morning set between 10:15am and 10:50am;")
    p.p("the rooms are not available to the Client during the flip.")
    p.gap(0.26)
    p.p("Each studio seats 120 in the set above and no more.", grey=True)
    c.showPage()

    p = page(6, T + " · Lunch")
    p.h("Lunch", 11)
    line(p, "12:30pm")
    p.gap(0.2)
    p.p("Plated, two courses with a shared dessert station. Rounds of ten.")
    p.p("Dietary covers: 18 vegetarian, 6 vegan, 4 gluten free, 2 nut free,")
    p.p("confirmed with the guarantee.")
    c.showPage()

    p = page(7, T + " · Evening reception")
    p.h("Reception", 11)
    line(p, "6:00pm")
    p.gap(0.2)
    p.p("Canapes passed for the first hour, then three stations. High tops and")
    p.p("lounge seating for 60. Terrace heaters included; the Terrace is")
    p.p("weather dependent and the Ardsley Room is held as the indoor")
    p.p("alternative until 2:00pm on the event day.")
    c.showPage()

    p = page(8, T + " · Bar")
    p.h("Bar", 11)
    line(p, "10:30pm")
    p.gap(0.2)
    p.p("Three bars, four-hour package from 6:00pm. Last call 10:15pm.")
    p.p("No extension is agreed in this order; any extension is charged at")
    p.p("$1,200 per half hour and must be requested before 9:00pm.")
    c.showPage()

    p = page(9, T + " · Audio visual")
    p.h("Rig and strike", 11)
    line(p, "6:30am")
    line(p, "11:00pm")
    p.gap(0.22)
    p.p("House system in the Grand Ballroom: line array, two 20 ft screens,")
    p.p("confidence monitor, four handhelds and two lavaliers.")
    p.p("Studio A and Studio B: one screen and two handhelds each.")
    p.gap(0.24)
    p.p("Strike must be complete by 11:45pm. Crew remaining after midnight is", grey=True)
    p.p("charged to the Client at the overtime rate on page 13.", grey=True)
    c.showPage()

    p = page(10, T + " · Afternoon session")
    p.h("Afternoon session", 11)
    line(p, "2:00pm")
    p.gap(0.2)
    p.p("Room reset from the breakout configuration during lunch.")
    p.p("Closing remarks from 4:40pm; room cleared for the reception flip by")
    p.p("5:15pm.")
    c.showPage()

    p = page(11, T + " · Guarantee and changes")
    p.h("Guaranteed count", 11)
    p.p("The guarantee is due 72 hours before the event: by 10:00am on")
    p.p("Saturday 6 February 2027.")
    p.gap(0.22)
    p.p("Charges are based on the guarantee or the actual number served,")
    p.p("whichever is higher. The guarantee is a minimum and not a cap.")
    p.gap(0.26)
    p.h("Changes", 11)
    p.p("Set changes requested within 72 hours are charged as labour at the")
    p.p("rate on page 13 and are subject to availability.")
    c.showPage()

    p = page(12, T + " · Charges")
    p.h("Food and beverage", 11)
    for label, qty, rate in FB:
        p.row(f"{label}  × {qty}", money(qty * rate), size=9.5)
    p.gap(0.1)
    p.row("Food and beverage subtotal", money(FB_SUBTOTAL), bold=True)
    svc = FB_SUBTOTAL * SERVICE
    p.row(f"Service charge, {SERVICE:.0%}", money(svc))
    p.row("Subtotal", money(FB_SUBTOTAL + svc))
    tax = (FB_SUBTOTAL + svc) * TAX
    p.row(f"Sales tax, {TAX * 100:.3f}%", money(tax))
    p.gap(0.08)
    p.row("Total food and beverage", money(FB_SUBTOTAL + svc + tax), bold=True)
    p.gap(0.26)
    p.p("Room rental, audio visual and rentals are invoiced separately.", grey=True)
    p.p("The service charge is taxable in this jurisdiction.", grey=True)
    c.showPage()

    p = page(13, T + " · House rules")
    p.h("Labour and overtime", 11)
    p.row("Banquet labour, per server per hour", money(42.00))
    p.row("Crew overtime after midnight, per person per hour", money(96.00))
    p.row("Bar extension, per half hour", money(1200.00))
    p.gap(0.26)
    p.h("On site", 11)
    p.p("No open flame. No adhesive on painted surfaces. Deliveries are")
    p.p("accepted from 48 hours before the event and are charged storage")
    p.p("after that. Nothing may be rigged from the ceiling in the Studios.")
    c.showPage()

    p = page(14, T + " · Signatures")
    p.p("Signing this order confirms the arrangements, the guarantee deadline", grey=True)
    p.p("and the charges set out above.", grey=True)
    p.gap(0.4)
    p.h("For the Client", 11)
    p.p("Name _______________________________   Date ______________")
    p.gap(0.34)
    p.h("For Thursby House", 11)
    p.p("Name _______________________________   Date ______________")
    p.gap(0.4)
    p.p("Catering manager: Imani Oyelaran · Harrowgate Hospitality", grey=True)
    c.showPage()

    c.save()
    return path


def check_beo():
    sub = sum(qty * rate for _, qty, rate in FB)
    assert abs(sub - FB_SUBTOTAL) < 0.005, sub
    svc = FB_SUBTOTAL * SERVICE
    assert abs(svc - 15_552.00) < 0.005, svc
    tax = (FB_SUBTOTAL + svc) * TAX
    total = FB_SUBTOTAL + svc + tax
    assert abs(total - 87_483.24) < 0.005, total

    assert len(SCHEDULE) == 11, len(SCHEDULE)
    assert len({t for t, *_ in SCHEDULE}) == 11
    heads = sorted({h for _, _, _, h, _ in SCHEDULE if h})
    assert heads == [BREAKOUT, RECEPTION, GUESTS], heads
    assert len(VENDORS) == 4

    # The point of the piece: the times are scattered, not listed.
    per_page = {}
    for _, _, _, _, n in SCHEDULE:
        per_page[n] = per_page.get(n, 0) + 1
    assert 1 not in per_page, "page 1 must carry no times"
    assert max(per_page.values()) <= 2, per_page
    assert len(per_page) == 9, per_page
    return total


def main():
    os.makedirs(OUT, exist_ok=True)

    rows, canon, spellings = build_registration_rows()
    check_registration(rows, canon, spellings)
    xlsx = registration_workbook(
        os.path.join(OUT, "Registration Export — Annual Partner Weekend.xlsx"),
        rows)
    print(f"{os.path.basename(xlsx)}  {os.path.getsize(xlsx):,} bytes")
    print(f"  {ROWS:,} rows, {PEOPLE:,} people, {DUPES} duplicate registrations")
    print(f"  {len(spellings)} organisation spellings of {len(canon)} names")
    print("  " + ", ".join(f"{n:,} {c}" for c, n in CODES))

    total = check_beo()
    pdf = beo(os.path.join(OUT, "BEO — Winter Partner Summit.pdf"))
    print(f"{os.path.basename(pdf)}  {os.path.getsize(pdf):,} bytes")
    print(f"  {len(SCHEDULE)} times over {len({n for *_, n in SCHEDULE})} pages, "
          f"F&B {money(FB_SUBTOTAL)} → {money(total)}")


if __name__ == "__main__":
    main()
