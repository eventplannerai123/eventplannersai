"""The November week-one demo files, built ahead of the days that need them.

Her Oct 14 rule, restated in the November plan: every demo file a prompt needs
is built when the post is planned, not on the day. Three files are due this
week, and the guide gives each one its numbers:

  Mon 2  Venue Proposal — Winter Gala        (PDF, 6 pages)
  Wed 4  Event Budget — Spring Conference    (Google Sheet, built separately)
  Fri 6  AV Quotes — Spring Conference       (three PDFs)

EVERY VENUE AND COMPANY HERE IS INVENTED, and no real client, venue or
employer is named anywhere. That is the standing rule, and it is also what
makes these safe to keep in a public repo — which they have to be, because
Drive's server-side upload fetches them from a raw.githubusercontent URL.

THE ARITHMETIC IS CHECKED, NOT TRUSTED. The guide states the answer each
piece is supposed to land on, and a demo whose numbers do not add up ruins
the Reel it was built for. check() at the bottom recomputes every total from
the same figures the pages print and fails the build on a mismatch:

  Venue proposal   $47,062 real total, $261.46 a person, against a $185
                   headline — the fees are spread across six pages rather
                   than listed together, because the piece is about fees you
                   do not see in one place.
  AV quote A       $8,400 headline, $11,950 real
  AV quote B       $9,100 headline, $10,300 real
  AV quote C       $11,200, genuinely all-in — the dear one that is cheapest
"""
import os
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas

HERE = os.path.dirname(os.path.abspath(__file__))
W, H = LETTER
L, R = 1.0 * inch, W - 1.0 * inch
INK = (0.15, 0.15, 0.17)
GREY = (0.45, 0.45, 0.48)

GUESTS = 180
RATE = 185.00
LINEN = 1450.00
COAT_PER = 4.00
CAKE_PER = 3.50
SERVICE = 0.22
ADMIN = 0.07
GUARDS, GUARD_HOURS, GUARD_RATE = 2, 6, 65.00
BAR_FEE, BARS = 175.00, 3
OVERTIME_PER_HALF_HOUR = 1200.00


def money(x):
    return f"${x:,.2f}"


class Page:
    def __init__(self, c, title, n, of):
        self.c = c
        self.y = H - 1.0 * inch
        c.setFillColorRGB(*INK)
        c.setFont("Helvetica-Bold", 16)
        c.drawString(L, self.y, title)
        self.y -= 0.42 * inch
        c.setStrokeColorRGB(0.8, 0.8, 0.82)
        c.line(L, self.y, R, self.y)
        self.y -= 0.34 * inch
        c.setFillColorRGB(*GREY)
        c.setFont("Helvetica", 8)
        c.drawRightString(R, 0.62 * inch, f"Page {n} of {of}")
        c.setFillColorRGB(*INK)

    def h(self, text, size=12, gap=0.26):
        self.c.setFont("Helvetica-Bold", size)
        self.c.drawString(L, self.y, text)
        self.y -= gap * inch

    def p(self, text, size=10, gap=0.2, grey=False):
        self.c.setFillColorRGB(*(GREY if grey else INK))
        self.c.setFont("Helvetica", size)
        self.c.drawString(L, self.y, text)
        self.c.setFillColorRGB(*INK)
        self.y -= gap * inch

    def row(self, label, value, size=10, gap=0.21, bold=False):
        self.c.setFont("Helvetica-Bold" if bold else "Helvetica", size)
        self.c.drawString(L + 0.12 * inch, self.y, label)
        self.c.drawRightString(R, self.y, value)
        self.y -= gap * inch

    def gap(self, n=0.18):
        self.y -= n * inch


def venue_proposal(path):
    c = canvas.Canvas(path, pagesize=LETTER)
    of = 6

    p = Page(c, "Fairhaven Hall — Proposal: Winter Gala", 1, of)
    p.p("Prepared for: Winter Gala, Saturday 13 February 2027", grey=True)
    p.p("Guest count: 180    Room: The Ardsley Room    Hours: 6:00pm – 11:00pm", grey=True)
    p.gap(0.3)
    p.h("Your rate")
    p.gap(0.1)
    c.setFont("Helvetica-Bold", 34)
    c.drawString(L, p.y - 0.2 * inch, f"${RATE:,.0f} per person")
    p.y -= 0.72 * inch
    p.p(f"{GUESTS} guests at {money(RATE)} per person", gap=0.22)
    p.row("Food and beverage minimum", money(RATE * GUESTS), bold=True)
    p.gap(0.28)
    p.p("Includes the room from 4:00pm for setup, the house linen, standard")
    p.p("china and glassware, the dance floor, and one hour of passed canapes")
    p.p("before dinner service.")
    p.gap(0.3)
    p.p("Charges that are not part of the per-person rate are set out in the", grey=True)
    p.p("relevant sections and in the terms on page 6.", grey=True)
    c.showPage()

    p = Page(c, "The Ardsley Room", 2, of)
    p.p("Capacity 220 seated, 300 standing. Ceiling height 22 feet.")
    p.p("Pre-function foyer and cloakroom included in the hire.")
    p.gap(0.28)
    p.h("Room and front of house", 11)
    p.row("House linen (white or ivory, floor length)", "included")
    p.row("Textured linen upgrade, 18 rounds and 4 long tables", money(LINEN))
    p.row(f"Attended coat check, per guest", money(COAT_PER))
    p.gap(0.24)
    p.p("The coat check is operated by the venue and is charged on the", grey=True)
    p.p("guaranteed guest count rather than the number of coats taken.", grey=True)
    p.gap(0.3)
    p.h("Setup", 11)
    p.p("Vendor access from 4:00pm. The room must be cleared by 1:00am.")
    p.p("Nothing may be affixed to the panelling or the plaster.")
    c.showPage()

    p = Page(c, "Food and beverage", 3, of)
    p.p("Four-course plated dinner, selected from the winter menu.")
    p.p("Two entree choices plus one vegetarian, confirmed 14 days ahead.")
    p.gap(0.28)
    p.h("Included in the per-person rate", 11)
    p.row("Passed canapes, one hour, six varieties", "included")
    p.row("Four-course plated dinner", "included")
    p.row("Coffee, tea and petits fours", "included")
    p.gap(0.26)
    p.h("Charged separately", 11)
    p.row("Cake cutting and plating, per guest", money(CAKE_PER))
    p.gap(0.24)
    p.p("A cake brought in from an outside bakery is welcome. The cutting", grey=True)
    p.p("and plating charge applies whether or not the kitchen supplies the", grey=True)
    p.p("cake, and is calculated on the guaranteed guest count.", grey=True)
    p.gap(0.3)
    p.p(f"A service charge of {SERVICE:.0%} is applied to the food and beverage total.")
    c.showPage()

    p = Page(c, "Bar", 4, of)
    p.p("Five hours of open bar, premium pour, billed within the per-person")
    p.p("rate. Three bars: two in the Ardsley Room, one in the foyer.")
    p.gap(0.28)
    p.h("Bar staffing", 11)
    p.row(f"Bartender fee, per bar ({BARS} bars)", money(BAR_FEE))
    p.row(f"Total bartender fees", money(BAR_FEE * BARS))
    p.gap(0.24)
    p.p("One bartender per bar is included in the fee above. A second", grey=True)
    p.p("bartender on any bar is charged at the same rate.", grey=True)
    p.gap(0.3)
    p.h("Last call", 11)
    p.p("Bars close at 10:45pm. Service past 11:00pm is subject to the")
    p.p("overtime provision in the terms.")
    c.showPage()

    p = Page(c, "Staffing and security", 5, of)
    p.p("Service staff for dinner are included in the per-person rate at a")
    p.p("ratio of one server to every 16 guests.")
    p.gap(0.28)
    p.h("Security", 11)
    p.p("Licensed security is required for any event with an open bar and")
    p.p("more than 150 guests. Guards are booked through the venue.")
    p.gap(0.2)
    p.row(f"{GUARDS} guards x {GUARD_HOURS} hours x {money(GUARD_RATE)} per hour",
          money(GUARDS * GUARD_HOURS * GUARD_RATE))
    p.gap(0.26)
    p.h("Coat check staffing", 11)
    p.p("Included in the per-guest coat check charge on page 2.")
    p.gap(0.3)
    p.h("Load out", 11)
    p.p("Vendors must be off site by 1:00am. A member of your team must")
    p.p("remain until the last vendor has left.")
    c.showPage()

    p = Page(c, "Terms", 6, of)
    p.h("Administrative fee", 11)
    p.p(f"An administrative fee of {ADMIN:.0%} is applied to the food and beverage")
    p.p("total. This fee covers administration, overheads and the costs of")
    p.p("this event. It is not a gratuity and is not distributed to service")
    p.p("staff. Gratuities are at your discretion.")
    p.gap(0.28)
    p.h("Overtime", 11)
    p.p(f"Events running past 11:00pm are charged {money(OVERTIME_PER_HALF_HOUR)} per half hour")
    p.p("or part thereof, covering the room, service staff and security.")
    p.gap(0.28)
    p.h("Guarantee", 11)
    p.p("A guaranteed guest count is due 10 business days before the event")
    p.p("and may not be reduced after that date.")
    p.gap(0.28)
    p.h("Deposit and payment", 11)
    p.p("35% on signature, 35% at 90 days, the balance 10 days before.")
    p.p("All charges are subject to applicable state and local tax.")
    c.showPage()
    c.save()

    fb = RATE * GUESTS
    total = (fb + fb * SERVICE + fb * ADMIN + COAT_PER * GUESTS + LINEN
             + CAKE_PER * GUESTS + GUARDS * GUARD_HOURS * GUARD_RATE
             + BAR_FEE * BARS)
    return total


QUOTES = [
    dict(file="AV Quotes — Spring Conference — Quote A.pdf",
         company="Meridian Stage & Sound",
         headline=8400.00,
         lines=[("Main room projection: 2 x 10,000 lumen, 2 x 16ft screens", 3200.00),
                ("Main room audio: line array, 4 handhelds, 2 lavaliers", 2450.00),
                ("Main room lighting: 8 LED wash, 4 profile", 1550.00),
                ("Breakout rooms (2): projector, screen, speaker, microphone", 1200.00)],
         extras=[("Crew: 2 technicians x 12 hours", 1850.00),
                 ("Delivery and setup", 650.00),
                 ("Rigging (motors, points and certification)", 1050.00)],
         extras_note=("Labor, delivery and rigging are billed in addition to the "
                      "equipment total above."),
         allin=False),
    dict(file="AV Quotes — Spring Conference — Quote B.pdf",
         company="Northgate AV Partners",
         headline=9100.00,
         lines=[("Main room package: projection, audio and lighting, crewed", 7300.00),
                ("Breakout rooms (2): projector, screen, speaker, microphone", 1800.00)],
         extras=[("Delivery", 450.00),
                 ("Power distribution", 750.00)],
         extras_note=("Technician labor is included in the main room package. "
                      "Delivery and power distribution are billed separately."),
         allin=False),
    dict(file="AV Quotes — Spring Conference — Quote C.pdf",
         company="Halcyon Event Technologies",
         headline=11200.00,
         lines=[("Main room: projection, audio and lighting", 6800.00),
                ("Breakout rooms (2), fully equipped", 1700.00),
                ("Crew: 2 technicians, full event day", 1600.00),
                ("Delivery, setup and rigging", 1100.00)],
         extras=[],
         extras_note=("This quote is all-in. There are no labor, delivery, "
                      "rigging or power charges on top of the total above."),
         allin=True),
]


def av_quote(q, path):
    c = canvas.Canvas(path, pagesize=LETTER)
    p = Page(c, q["company"], 1, 1)
    p.p("Quotation — Spring Conference, 200 attendees", grey=True)
    p.p("One day, main room plus two breakout rooms. Valid 30 days.", grey=True)
    p.gap(0.3)
    p.h("Equipment and services", 11)
    for label, amount in q["lines"]:
        p.row(label, money(amount))
    p.gap(0.06)
    c.setStrokeColorRGB(0.8, 0.8, 0.82)
    c.line(L + 0.12 * inch, p.y + 0.1 * inch, R, p.y + 0.1 * inch)
    p.gap(0.08)
    p.row("Quote total", money(q["headline"]), bold=True)
    p.gap(0.34)
    p.h("Terms", 11)
    for line in q["extras_note"].split(". "):
        line = line.strip().rstrip(".")
        if line:
            p.p(line + ".")
    if q["extras"]:
        p.gap(0.18)
        for label, amount in q["extras"]:
            p.row(label, money(amount))
    p.gap(0.3)
    p.p("Payment: 50% to confirm, balance within 30 days of the event.", grey=True)
    p.p("Cancellation inside 14 days is charged at 50%.", grey=True)
    c.showPage()
    c.save()
    return q["headline"] + sum(a for _, a in q["extras"])


def check():
    out = os.path.join(HERE, "files")
    os.makedirs(out, exist_ok=True)

    total = venue_proposal(os.path.join(out, "Venue Proposal — Winter Gala.pdf"))
    per = total / GUESTS
    assert abs(total - 47062.00) < 0.01, total
    assert abs(per - 261.46) < 0.01, per
    print(f"Venue Proposal — Winter Gala: headline {money(RATE)} pp, "
          f"real {money(total)} = {money(per)} pp")

    expected = {"Quote A": 11950.00, "Quote B": 10300.00, "Quote C": 11200.00}
    for q in QUOTES:
        real = av_quote(q, os.path.join(out, q["file"]))
        name = q["file"].split("— ")[-1].replace(".pdf", "")
        assert abs(sum(a for _, a in q["lines"]) - q["headline"]) < 0.01, name
        assert abs(real - expected[name]) < 0.01, (name, real)
        print(f"{name} ({q['company']}): headline {money(q['headline'])}, "
              f"real {money(real)}")


if __name__ == "__main__":
    check()
