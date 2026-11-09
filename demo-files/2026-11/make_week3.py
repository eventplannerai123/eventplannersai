"""Week three's demo files, built Mon 9 as the guide's CLAUDE CODE lines ask.

  Thu 12  Ticket Allocation — Annual Client Summit  (Google Sheet, 2 tabs)
  Fri 13  Venue Quote — Fall Leadership Summit      (PDF, 2 pages)

EVERY COMPANY, VENUE AND PERSON HERE IS INVENTED. No real client, venue or
employer appears, which is the standing rule and also what makes these safe
in a public repo — Drive fetches the PDF from a raw.githubusercontent URL.

THE ARITHMETIC IS RECOMPUTED, NOT TRUSTED. Both pieces are about a number:

  Thu 12  2,125 invite rows but 1,985 people, so 15 seats are left, not 125 short
  Fri 13  $45,000 for a Saturday, and a small-print line that gets it to $35,000

The Thu 12 sheet is the one that can go wrong quietly. The whole Reel turns on
ChatGPT finding exactly 140 people who sit on one team's CLIENT list and a
DIFFERENT team's PROSPECT list — so the builder asserts that count, that every
duplicate pair really does straddle two teams and two lists, and that nobody
else in the file shares an email. A 141st accidental duplicate would make the
answer in the guide wrong, and that would not be visible by looking.
"""
import csv
import datetime
import os
import random

from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas

from make_demo_files import Page, money, L, R, W, H, INK, GREY

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "files")

# ================================================================ Thu 12 ====
SEATS = 2_000
ALLOCATION = [
    ("Clients", 900),
    ("Prospects", 600),
    ("Partners", 250),
    ("Speakers", 100),
    ("Staff", 150),
]

CLIENT_ROWS = 940          # 40 over the 900 allocated
PROSPECT_ROWS = 685        # 85 over the 600 allocated
PARTNER_ROWS = 250
SPEAKER_ROWS = 100
STAFF_ROWS = 150
DOUBLE_BOOKED = 140        # same person, one team's client list + another's prospect list

TEAMS = [
    "Team Ashford", "Team Berwick", "Team Calder",
    "Team Dunmore", "Team Ellsworth", "Team Fairchild",
]

FIRST = """Amara Bea Caleb Dara Elin Faris Gia Hollis Imani Jonas Kira Lio
Mira Nadia Omar Pria Quinn Rhea Soren Tess Umi Vero Wren Xavi Yusuf Zane
Anders Brielle Cato Delia Emeka Fiona Gael Hana Ike Juno Kai Lena Mose Niamh
Otis Paloma Rafi Sana Theo Una Vidya Wes Yara Zuri Arden Blythe Cyrus Dove
Elias Freya Gus Hester Ivo Joss Keziah Lars Maeve Nico Orla Pax Rilla Silas
Tova Ulric Vesna Wyn Xenia Yonas Zola""".split()

LAST = """Abbott Ballard Cathcart Danforth Ellery Fenwick Garrick Halloway
Ingersoll Jessop Kettering Lanyon Mercer Northcote Oakley Pemberton Quayle
Ridgeway Sandoval Thwaite Underhill Vance Whitlock Yarrow Zeller Ashby
Brockman Caldecott Draycott Edgerly Fairbrother Gaskell Hensley Ivory Jarvis
Kemble Loxley Marchetti Nunnery Ormsby Pollard Quentin Rutherford Stapleton
Tarrant Ulverston Verity Wexford Yealand Zabriskie Alderton Birkett Chalmers
Dunlevy Esterhaus Fallowfield Grimsby Hartnell Isley Jerrold Kingsmill
Lattimer Mowbray Nethercott Ormerod Prideaux Quillon Rossiter Sowerby
Templeton Urquhart Vellacott Winterbourne Yelverton""".split()

COMPANIES = [
    "Alderney Freight", "Bellwether Analytics", "Cardinal Mills",
    "Driftwood Logistics", "Everline Health", "Foxglove Capital",
    "Granite Row Media", "Harbourstone Legal", "Ironwood Robotics",
    "Juniper Rail", "Kestrel Dynamics", "Larkspur Foods",
    "Meridian Castings", "Northgate Utilities", "Oriel Pharma",
    "Pinecrest Mutual", "Quarrymoor Cement", "Redbourne Textiles",
    "Saltmarsh Shipping", "Thistledown Brewing", "Umberslade Tooling",
    "Vantage Orchards", "Wellspring Water", "Yardley Optics",
    "Zephyr Avionics",
]

PARTNER_ORGS = [
    "Brightline Events Group", "Carrickfern Audio Visual",
    "Dovetail Exhibit Build", "Fernhill Travel Desk",
    "Greystone Print House", "Larkmount Staffing",
]
SPEAKER_ORGS = [
    "Independent", "Ashgrove Institute", "Fieldnote Research",
    "Marrowfield Press", "Thornbury Lecture Series",
]
HOST = "Fieldhouse Events LLC"   # the fictional host company


def _slug(company):
    """A plausible domain: the company's first word, so emails read like emails."""
    word = company.split()[0].lower()
    return "".join(ch for ch in word if ch.isalnum()) + ".example"


def _people(n, rng, used_emails, orgs=None):
    """n distinct invented people, each with an email nobody else in the file has."""
    out = []
    while len(out) < n:
        first = rng.choice(FIRST)
        last = rng.choice(LAST)
        company = rng.choice(orgs) if orgs else rng.choice(COMPANIES)
        email = f"{first[0].lower()}.{last.lower()}@{_slug(company)}"
        if email in used_emails:
            continue
        used_emails.add(email)
        out.append({"name": f"{first} {last}", "email": email, "company": company})
    return out


def ticket_allocation_rows(seed=20261112):
    """Tab 2's rows, plus the duplicate pairs, built so the counts are exact."""
    rng = random.Random(seed)
    used = set()

    # The 140 double-booked people exist once, and get two rows each.
    doubles = _people(DOUBLE_BOOKED, rng, used)
    # Everyone who appears on exactly one team list.
    client_only = _people(CLIENT_ROWS - DOUBLE_BOOKED, rng, used)
    prospect_only = _people(PROSPECT_ROWS - DOUBLE_BOOKED, rng, used)
    partners = _people(PARTNER_ROWS, rng, used, PARTNER_ORGS)
    speakers = _people(SPEAKER_ROWS, rng, used, SPEAKER_ORGS)
    staff = _people(STAFF_ROWS, rng, used, [HOST])

    rows, pairs = [], []

    def add(p, team, lst):
        rows.append([p["name"], p["email"], p["company"], team, lst])

    for p in doubles:
        a, b = rng.sample(TEAMS, 2)          # two DIFFERENT teams, always
        add(p, a, "Client")
        add(p, b, "Prospect")
        pairs.append((p["email"], a, b))
    for p in client_only:
        add(p, rng.choice(TEAMS), "Client")
    for p in prospect_only:
        add(p, rng.choice(TEAMS), "Prospect")
    for p in partners:
        add(p, "Partner program", "Partner")
    for p in speakers:
        add(p, "Content committee", "Speaker")
    for p in staff:
        add(p, "Event team", "Staff")

    rng.shuffle(rows)
    return rows, pairs


def write_invite_csv(rows, path):
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["Name", "Email", "Company", "Account team", "List"])
        w.writerows(rows)
    return path


# ================================================================ Fri 13 ====
QUOTE_VENUE = "Marchmont Pavilion"
QUOTE_EVENT = "Fall Leadership Summit"
QUOTE_DATE = datetime.date(2027, 10, 16)
QUOTE_GUESTS = 180
ROOM_RENTAL = 15_000.00
FB_MINIMUM = 30_000.00
QUOTE_TOTAL = ROOM_RENTAL + FB_MINIMUM          # 45,000
SERVICE_PCT = 0.21
TAX_PCT = 0.08875
SMALL_PRINT = ("Sunday-Thursday rates and multi-year agreements are "
               "available on request.")


def venue_quote(path):
    c = canvas.Canvas(path, pagesize=LETTER)

    p = Page(c, f"{QUOTE_VENUE} — Quote: {QUOTE_EVENT}", 1, 2)
    p.p(f"Prepared for: {HOST}", grey=True)
    p.p(f"Event date: {QUOTE_DATE.strftime('%A %-d %B %Y')}", grey=True)
    p.p(f"Guest count: {QUOTE_GUESTS}    Space: The Marchmont Ballroom", grey=True)
    p.p("Hours: 5:30pm - 11:30pm    Quote valid 30 days", grey=True)
    p.gap(0.34)

    p.h("Your quote")
    p.gap(0.1)
    c.setFont("Helvetica-Bold", 34)
    c.drawString(L, p.y - 0.2 * inch, money(QUOTE_TOTAL))
    p.y -= 0.74 * inch
    p.row("Ballroom rental, Saturday rate", money(ROOM_RENTAL))
    p.row("Food and beverage minimum", money(FB_MINIMUM))
    p.row("Total before tax and service", money(QUOTE_TOTAL), bold=True)
    p.gap(0.3)
    p.p("Service charge of 21% and sales tax of 8.875% are applied to food")
    p.p("and beverage at final billing and are not included above.")
    p.gap(0.26)

    p.h("What the rental includes", size=11)
    for line in [
        "The ballroom from 1:00pm for setup and until 1:00am for load-out",
        "House tables, banquet chairs, house linen, china and glassware",
        "Dance floor, staging to 24 feet, and the house sound system",
        "One event manager on site, two porters, and cloakroom staffing",
    ]:
        p.p("- " + line, gap=0.21)
    p.gap(0.24)

    p.h("Payment", size=11)
    p.row("Deposit, due on signing", money(QUOTE_TOTAL * 0.5))
    p.row("Balance, due 30 days before the event", money(QUOTE_TOTAL * 0.5))
    c.showPage()

    p = Page(c, f"{QUOTE_VENUE} — Quote: {QUOTE_EVENT}", 2, 2)
    p.h("Terms", size=12)
    for n, line in [
        ("1.", "Guest count is confirmed 14 days before the event and may not"),
        ("", "    fall more than 10% below the count quoted above."),
        ("2.", "The food and beverage minimum is a minimum spend, not a cap."),
        ("", "    Shortfall against the minimum is billed as a room charge."),
        ("3.", "Outside catering is not permitted. Alcohol is served only by"),
        ("", "    the Pavilion's licensed bartenders."),
        ("4.", "Cancellation more than 180 days before the event: deposit"),
        ("", "    forfeited. Within 180 days: 50% of the total. Within 60: full."),
        ("5.", "Amplified sound ends at 11:00pm. Open flame requires consent."),
    ]:
        p.p(f"{n} {line}".strip(), gap=0.21)
    p.gap(0.3)

    p.h("Rate notes", size=12)
    p.p("Rates quoted are the Saturday rates in effect for the 2027 season.")
    p.p("Seasonal surcharges apply from 20 November to 2 January.")
    p.gap(0.26)
    c.setFillColorRGB(*GREY)
    c.setFont("Helvetica", 8)
    c.drawString(L, p.y, SMALL_PRINT)
    p.y -= 0.2 * inch
    c.drawString(L, p.y, "Contact your sales manager to discuss either option.")
    p.y -= 0.34 * inch
    c.setFillColorRGB(*INK)

    p.h("Acceptance", size=12)
    p.p("Signature ______________________    Date ______________")
    p.gap(0.2)
    p.p(f"{QUOTE_VENUE}  ·  M. Harkness, Sales  ·  quote ref MP-2027-0416", grey=True)
    c.save()
    return QUOTE_TOTAL


# ================================================================ checks ====
def check():
    assert sum(n for _, n in ALLOCATION) == SEATS, ALLOCATION

    rows, pairs = ticket_allocation_rows()
    assert len(rows) == 2_125, len(rows)
    assert len(rows) == CLIENT_ROWS + PROSPECT_ROWS + PARTNER_ROWS \
        + SPEAKER_ROWS + STAFF_ROWS

    by_list = {}
    for r in rows:
        by_list[r[4]] = by_list.get(r[4], 0) + 1
    assert by_list == {"Client": CLIENT_ROWS, "Prospect": PROSPECT_ROWS,
                       "Partner": PARTNER_ROWS, "Speaker": SPEAKER_ROWS,
                       "Staff": STAFF_ROWS}, by_list

    emails = [r[1] for r in rows]
    people = len(set(emails))
    assert len(emails) - people == DOUBLE_BOOKED, (len(emails), people)
    assert people == 1_985, people
    assert SEATS - people == 15, SEATS - people

    # every duplicate must straddle two teams AND the two lists, and no email
    # may appear three times or twice on the same list
    seen = {}
    for name, email, company, team, lst in rows:
        seen.setdefault(email, []).append((team, lst))
    dups = {e: v for e, v in seen.items() if len(v) > 1}
    assert len(dups) == DOUBLE_BOOKED, len(dups)
    for email, appearances in dups.items():
        assert len(appearances) == 2, (email, appearances)
        (t1, l1), (t2, l2) = appearances
        assert t1 != t2, (email, t1, t2)
        assert {l1, l2} == {"Client", "Prospect"}, (email, l1, l2)
    assert len(pairs) == DOUBLE_BOOKED

    # on paper, versus once deduplicated
    assert CLIENT_ROWS - 900 == 40
    assert PROSPECT_ROWS - 600 == 85
    assert len(rows) - SEATS == 125

    assert QUOTE_DATE.strftime("%A") == "Saturday", QUOTE_DATE
    assert QUOTE_TOTAL == 45_000.00, QUOTE_TOTAL
    assert ROOM_RENTAL + FB_MINIMUM == QUOTE_TOTAL

    print(f"Thu 12: {len(rows):,} rows, {people:,} people, "
          f"{DOUBLE_BOOKED} double-booked, {SEATS - people} seats left "
          f"(on paper {len(rows) - SEATS} over)")
    print(f"Fri 13: {money(QUOTE_TOTAL)} = {money(ROOM_RENTAL)} room + "
          f"{money(FB_MINIMUM)} F&B, {QUOTE_DATE.strftime('%A %d %B %Y')}")
    return rows, pairs


def main():
    rows, _ = check()
    os.makedirs(OUT, exist_ok=True)
    csv_path = write_invite_csv(
        rows, os.path.join(OUT, "Ticket Allocation — Annual Client Summit — tab2.csv"))
    print(f"{os.path.basename(csv_path)}  {os.path.getsize(csv_path):,} bytes")
    pdf = os.path.join(OUT, "Venue Quote — Fall Leadership Summit.pdf")
    venue_quote(pdf)
    print(f"{os.path.basename(pdf)}  {os.path.getsize(pdf):,} bytes")


if __name__ == "__main__":
    main()
