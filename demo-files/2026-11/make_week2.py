"""Week two's demo files, built on Fri 6 as the guide's CLAUDE CODE lines ask.

  Mon 9   BEO — Autumn Board Dinner          (PDF, 3 pages, signed)
          Invoice — Autumn Board Dinner      (PDF, 1 page)
  Tue 10  Venue Agreement — Spring Gala      (PDF, 8 pages)
          Certificate of Insurance — Spring Gala (PDF, 1 page)

EVERY COMPANY, VENUE AND PERSON HERE IS INVENTED. No real client, venue or
employer appears, which is the standing rule and also what makes these safe
in a public repo — Drive fetches them from a raw.githubusercontent URL.

THE ARITHMETIC AND THE DATES ARE CHECKED, NOT TRUSTED. check() recomputes
every total and re-derives every deadline from the event date, and fails the
build on a mismatch. A demo whose numbers do not hold ruins the Reel it is
for, and both of these pieces are *about* a number:

  Mon 9   the invoice is $1,140 over the signed BEO, in three differences
  Tue 10  four insurance mismatches, and an indemnity worth pushing back on

THE INSURANCE TERMS ARE SPREAD ACROSS PAGES 3, 5 AND 7, never listed
together — the guide says so, and it is the piece: a requirement you meet on
page 3 and break on page 7.

Page 1 of the agreement is deliberately ordinary. If the whole contract read
like a trap the Reel would not be worth making.
"""
import os
import datetime
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas

from make_demo_files import Page, money, L, R, W, H, INK, GREY

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "files")

# ---------------------------------------------------------------- Mon 9 ----
CATERER = "Hearthstone Catering Co."
BEO_EVENT = "Autumn Board Dinner"
BEO_VENUE = "The Lyndale Room"
BEO_DATE = datetime.date(2026, 10, 22)
INVOICE_DATE = datetime.date(2026, 10, 29)

GUARANTEE = 120
BILLED = 124
DINNER_PP = 85.00
BAR_PP = 40.00
PER_HEAD = DINNER_PP + BAR_PP          # 125.00
SERVICE = 0.22
CAKE_PER = 3.50
CAKE_COUNT = 120
BAR_EXTENSION = 110.00

BEO_FB = GUARANTEE * PER_HEAD          # 15,000
BEO_SERVICE = BEO_FB * SERVICE         # 3,300
BEO_TOTAL = BEO_FB + BEO_SERVICE       # 18,300

INV_FB = BILLED * PER_HEAD             # 15,500
INV_SERVICE = INV_FB * SERVICE         # 3,410
CAKE = CAKE_COUNT * CAKE_PER           # 420
INV_TOTAL = INV_FB + INV_SERVICE + CAKE + BAR_EXTENSION   # 19,440

# --------------------------------------------------------------- Tue 10 ----
GALA_VENUE = "Thornbury Hall"
GALA_EVENT = "Spring Gala"
GALA_DATE = datetime.date(2027, 4, 17)
GALA_GUESTS = 250
CLIENT_COI_DAYS = 30
VENDOR_COI_DAYS = 14
CLIENT_COI_DUE = GALA_DATE - datetime.timedelta(days=CLIENT_COI_DAYS)
VENDOR_COI_DUE = GALA_DATE - datetime.timedelta(days=VENDOR_COI_DAYS)

REQ_GL_OCC, REQ_GL_AGG = 1_000_000, 2_000_000
REQ_LIQUOR = 2_000_000
COI_GL_OCC, COI_GL_AGG = 1_000_000, 2_000_000
COI_LIQUOR = 1_000_000
POLICY_FROM = datetime.date(2026, 5, 1)
POLICY_TO = datetime.date(2027, 3, 31)

BROKER = "Kestrel Lane Insurance Services"
CARRIER = "Anchorlight Specialty Insurance Company"
INSURED = "Fieldhouse Events LLC"


def longdate(d):
    return d.strftime("%A, %B %-d, %Y")


def shortdate(d):
    return d.strftime("%m/%d/%Y")


# ----------------------------------------------------------------- BEO -----
def beo(path):
    c = canvas.Canvas(path, pagesize=LETTER)

    p = Page(c, f"{CATERER} — Banquet Event Order", 1, 3)
    p.p("SIGNED — this BEO is the agreement. Changes require a signed addendum.", grey=True)
    p.gap()
    p.h("Event")
    p.row("Event", BEO_EVENT)
    p.row("Date", longdate(BEO_DATE))
    p.row("Room", BEO_VENUE)
    p.row("Service", "Reception 6:00pm · Dinner 7:00pm · Bar closes 10:30pm")
    p.row("Final guarantee", f"{GUARANTEE} guests")
    p.gap()
    p.p("The final guarantee was received in writing on October 15, 2026 and is", grey=True)
    p.p("the number billed. The guarantee is a minimum, not a cap: guests served", grey=True)
    p.p("above it are billed at the per-person rate on page 2.", grey=True)
    p.gap(0.3)
    p.h("Signatures")
    p.row("Client", "M. Ardelle, on behalf of the client")
    p.row("Caterer", f"J. Rourke, {CATERER}")
    p.row("Signed", "October 15, 2026")
    c.showPage()

    p = Page(c, "Food and Beverage", 2, 3)
    p.h("Per person")
    p.row("Plated dinner, three courses", money(DINNER_PP))
    p.row("Four-hour bar package", money(BAR_PP))
    p.row("Per guest", money(PER_HEAD), bold=True)
    p.gap()
    p.h("Charges")
    p.row(f"Food and beverage, {GUARANTEE} guests at {money(PER_HEAD)}", money(BEO_FB))
    p.row(f"Service charge, {int(SERVICE * 100)}% on food and beverage", money(BEO_SERVICE))
    p.row("Total before tax", money(BEO_TOTAL), bold=True)
    p.gap()
    p.p("The service charge applies to food and beverage only. Tax is billed at", grey=True)
    p.p("the prevailing rate on the final invoice.", grey=True)
    c.showPage()

    p = Page(c, "Terms", 3, 3)
    p.h("Included at no charge")
    p.p("Cake cutting and plating — waived for this event.")
    p.p("House linen, china, glassware and flatware.")
    p.p("Cloakroom attendant for the reception hour.")
    p.gap()
    p.h("Bar")
    p.p("The bar closes at 10:30pm. No extension is authorised under this BEO.")
    p.p("Any extension must be agreed in writing before the event and billed as")
    p.p("a signed addendum.")
    p.gap()
    p.h("Billing")
    p.p("Guests served above the final guarantee are billed at the per-person")
    p.p("rate, with the service charge applied.")
    p.p("Charges not listed in this BEO are not authorised.")
    p.gap(0.3)
    p.p(f"{CATERER} · Banquet Event Order · {BEO_EVENT} · {shortdate(BEO_DATE)}", grey=True)
    c.save()


def invoice(path):
    c = canvas.Canvas(path, pagesize=LETTER)
    p = Page(c, f"{CATERER} — Final Invoice", 1, 1)
    p.row("Invoice", "HC-20261029-0447")
    p.row("Event", f"{BEO_EVENT} · {longdate(BEO_DATE)}")
    p.row("Room", BEO_VENUE)
    p.row("Issued", longdate(INVOICE_DATE))
    p.row("Terms", "Net 30")
    p.gap(0.3)
    p.h("Charges")
    p.row(f"Food and beverage, {BILLED} guests at {money(PER_HEAD)}", money(INV_FB))
    p.row(f"Service charge, {int(SERVICE * 100)}%", money(INV_SERVICE))
    p.row(f"Cake cutting, {CAKE_COUNT} at {money(CAKE_PER)}", money(CAKE))
    p.row("Bar extension, 30 minutes", money(BAR_EXTENSION))
    p.gap(0.1)
    p.row("Total before tax", money(INV_TOTAL), bold=True)
    p.gap(0.3)
    p.p("Guest count taken from the banquet captain's count at service.", grey=True)
    p.p("Questions on this invoice: accounts@hearthstonecatering.example", grey=True)
    c.save()


# ------------------------------------------------------- Venue agreement ---
def agreement(path):
    c = canvas.Canvas(path, pagesize=LETTER)
    title = f"{GALA_VENUE} — Venue Agreement"

    p = Page(c, title, 1, 8)
    p.h("Parties and event")
    p.row("Venue", f"{GALA_VENUE}, a private event venue")
    p.row("Client", INSURED)
    p.row("Event", GALA_EVENT)
    p.row("Date", longdate(GALA_DATE))
    p.row("Attendance", f"{GALA_GUESTS} guests")
    p.row("Bar", "Open bar, hosted, beer wine and spirits")
    p.row("Access", "Load-in 8:00am · Event 6:30pm to midnight · Load-out by 2:00am")
    p.gap()
    p.p("This agreement is made on the date last signed below and covers the use")
    p.p("of the premises described in Schedule A for the event above.")
    c.showPage()

    p = Page(c, title, 2, 8)
    p.h("2. Fees and payment")
    p.row("Facility fee", "$18,500.00")
    p.row("Deposit, due on signing", "$9,250.00")
    p.row("Balance, due 14 days before the event", "$9,250.00")
    p.row("Refundable damage deposit", "$2,500.00")
    p.gap()
    p.h("3. Cancellation")
    p.p("Cancellation more than 180 days before the event: deposit forfeited.")
    p.p("Within 180 days: 50% of the facility fee. Within 60 days: in full.")
    c.showPage()

    p = Page(c, title, 3, 8)
    p.h("4. Insurance — general liability")
    p.p("The Client shall maintain commercial general liability insurance with")
    p.p(f"limits of not less than {money(REQ_GL_OCC)} per occurrence and")
    p.p(f"{money(REQ_GL_AGG)} in the aggregate, written on an occurrence form.")
    p.gap()
    p.p(f"The policy shall name {GALA_VENUE}, its owners, officers, employees and")
    p.p("agents as additional insured for the duration of the event, including")
    p.p("load-in and load-out.")
    p.gap()
    p.p("4.3  The Client's certificate of insurance is due no later than")
    p.p(f"      {CLIENT_COI_DAYS} days before the event, being {longdate(CLIENT_COI_DUE)}.")
    p.gap()
    p.p("Coverage shall be in force for the whole period of the Client's use of")
    p.p("the premises. A policy expiring before the event date does not satisfy")
    p.p("this section.")
    c.showPage()

    p = Page(c, title, 4, 8)
    p.h("5. Vendors")
    p.p("Every vendor engaged by the Client shall carry its own general liability")
    p.p("insurance and name the Venue as additional insured.")
    p.gap()
    p.p("5.2  Vendor certificates are due no later than "
        f"{VENDOR_COI_DAYS} days before the")
    p.p(f"      event, being {longdate(VENDOR_COI_DUE)}. The Venue may refuse access")
    p.p("      to any vendor whose certificate has not been received.")
    p.gap()
    p.h("6. Staffing")
    p.p("The Venue provides one house manager and two porters. Additional")
    p.p("security is billed at $65.00 an hour for each guard.")
    c.showPage()

    p = Page(c, title, 5, 8)
    p.h("7. Alcohol service")
    p.p("Alcohol shall be served only by the Venue's licensed bartenders. Service")
    p.p("ends 30 minutes before the event ends.")
    p.gap()
    p.p("7.3  Where alcohol is served, the Client shall maintain liquor liability")
    p.p(f"      insurance with a limit of not less than {money(REQ_LIQUOR)}, naming")
    p.p("      the Venue as additional insured. This limit applies whether the bar")
    p.p("      is hosted or cash.")
    p.gap()
    p.p("No alcohol may be brought onto the premises by the Client, guests or")
    p.p("vendors.")
    c.showPage()

    p = Page(c, title, 6, 8)
    p.h("8. Damage, noise and conduct")
    p.p("The Client is responsible for damage caused by guests and vendors.")
    p.p("Amplified sound ends at 11:30pm. Open flame requires written consent.")
    p.gap()
    p.h("9. Force majeure")
    p.p("Neither party is liable for failure to perform caused by an event beyond")
    p.p("its reasonable control. Fees paid are credited to a rescheduled date")
    p.p("within twelve months, subject to availability.")
    c.showPage()

    p = Page(c, title, 7, 8)
    p.h("10. Waiver of subrogation")
    p.p("Each policy required under this agreement shall include a waiver of")
    p.p(f"subrogation in favour of {GALA_VENUE}, and the Client waives every right")
    p.p("of recovery against the Venue to the extent of insurance collectible.")
    p.gap()
    p.h("11. Indemnification")
    p.p("The Client shall indemnify, defend and hold harmless the Venue, its")
    p.p("owners, officers, employees and agents from and against all claims,")
    p.p("damages, losses and expenses arising out of or connected with the event,")
    p.p("including claims arising from the negligence of the Venue itself.")
    p.gap()
    p.p("This obligation survives the end of this agreement.")
    c.showPage()

    p = Page(c, title, 8, 8)
    p.h("12. General")
    p.p("This agreement is the entire agreement between the parties and may be")
    p.p("amended only in writing signed by both.")
    p.gap(0.4)
    p.h("Signatures")
    p.row("Venue", f"R. Alcott, {GALA_VENUE}")
    p.row("Client", f"on behalf of {INSURED}")
    p.row("Date", "____________________")
    c.save()


def certificate(path):
    c = canvas.Canvas(path, pagesize=LETTER)
    p = Page(c, "Certificate of Liability Insurance", 1, 1)
    p.p("This certificate is issued as a matter of information only and confers", grey=True)
    p.p("no rights upon the certificate holder.", grey=True)
    p.gap()
    p.row("Producer", BROKER)
    p.row("Insured", INSURED)
    p.row("Carrier", CARRIER)
    p.row("Policy number", "ASI-GL-4471902")
    p.row("Policy period", f"{shortdate(POLICY_FROM)} to {shortdate(POLICY_TO)}")
    p.gap(0.3)
    p.h("Coverages")
    p.row("Commercial general liability — each occurrence", money(COI_GL_OCC))
    p.row("Commercial general liability — general aggregate", money(COI_GL_AGG))
    p.row("Liquor liability — each common cause", money(COI_LIQUOR))
    p.gap(0.3)
    p.h("Endorsements")
    p.row("Additional insured", "[    ]")
    p.row("Waiver of subrogation", "[    ]  NO")
    p.gap()
    p.p("Description of operations: Spring Gala, April 17, 2027.", grey=True)
    p.gap(0.3)
    p.row("Certificate holder", GALA_VENUE)
    p.row("Issued", "10/02/2026")
    c.save()


def check():
    # Mon 9 — the invoice is $1,140 over, in exactly three differences.
    assert PER_HEAD == 125.00
    assert BEO_FB == 15_000.00 and BEO_SERVICE == 3_300.00 and BEO_TOTAL == 18_300.00
    assert INV_FB == 15_500.00 and INV_SERVICE == 3_410.00
    assert CAKE == 420.00
    assert INV_TOTAL == 19_440.00
    diff = INV_TOTAL - BEO_TOTAL
    assert diff == 1_140.00, diff
    over_guests = (BILLED - GUARANTEE) * PER_HEAD
    over_service = over_guests * SERVICE
    assert over_guests == 500.00 and over_service == 110.00
    assert over_guests + over_service + CAKE + BAR_EXTENSION == diff
    # the BEO waives the cake fee the invoice charges, which is the point
    assert CAKE_COUNT == GUARANTEE

    # Tue 10 — four mismatches, and general liability is NOT one of them.
    assert (COI_GL_OCC, COI_GL_AGG) == (REQ_GL_OCC, REQ_GL_AGG), "GL must match"
    assert COI_LIQUOR < REQ_LIQUOR, "liquor liability must fall short"
    assert POLICY_TO < GALA_DATE, "the policy must expire before the event"
    assert CLIENT_COI_DUE == datetime.date(2027, 3, 18), CLIENT_COI_DUE
    assert VENDOR_COI_DUE == datetime.date(2027, 4, 3), VENDOR_COI_DUE
    assert GALA_DATE.strftime("%A") == "Saturday"
    assert CLIENT_COI_DUE.strftime("%A") == "Thursday"
    assert VENDOR_COI_DUE.strftime("%A") == "Saturday"

    print(f"checks pass: invoice {money(INV_TOTAL)} vs BEO {money(BEO_TOTAL)}, "
          f"difference {money(diff)}; COI due {CLIENT_COI_DUE}, "
          f"vendors {VENDOR_COI_DUE}, policy ends {POLICY_TO}")


def main():
    check()
    os.makedirs(OUT, exist_ok=True)
    jobs = [
        (beo, "BEO — Autumn Board Dinner.pdf"),
        (invoice, "Invoice — Autumn Board Dinner.pdf"),
        (agreement, "Venue Agreement — Spring Gala.pdf"),
        (certificate, "Certificate of Insurance — Spring Gala.pdf"),
    ]
    for fn, name in jobs:
        path = os.path.join(OUT, name)
        fn(path)
        print(f"{name}  {os.path.getsize(path):,} bytes")


if __name__ == "__main__":
    main()
