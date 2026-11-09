# November demo files

Her Oct 14 rule, restated in the November plan: **every demo file a prompt
needs is built when the post is planned, not on the day.** These are week
one's.

| Built for | File | Drive |
| --- | --- | --- |
| Mon 2 | `Venue Proposal — Winter Gala.pdf` (6 pages) | `November 2` |
| Wed 4 | `Event Budget — Spring Conference` (Google Sheet) | `November 4` |
| Fri 6 | `AV Quotes — Spring Conference` — Quote A, B, C (3 PDFs) | `November 6` |

Week two, built Fri 6 by `make_week2.py`:

| Built for | File | Drive |
| --- | --- | --- |
| Mon 9 | `BEO — Autumn Board Dinner.pdf` (3 pages, signed) | `November 9` |
| Mon 9 | `Invoice — Autumn Board Dinner.pdf` (1 page) | `November 9` |
| Tue 10 | `Venue Agreement — Spring Gala.pdf` (8 pages) | `November 10` |
| Tue 10 | `Certificate of Insurance — Spring Gala.pdf` (1 page) | `November 10` |
| Sun 8 | `Garden Reception — Budget and Rain Plan` (Google Sheet, two tabs) | `November 8` |

The Sun 8 sheet is built in Drive rather than here, the same way the Wed 4
budget was: `1oKTGZntZsocspeZrBS9auIKm0jtYZ0k_7-BJdWSqnPk`, tabs **Outdoor
plan** and **Tent quote (rain plan)**. Both totals are live formulas and both
were read back after writing:

| | |
| --- | --- |
| Outdoor plan | **$35,800** |
| Tent quote | **$14,080** |
| Rain plan total | $35,800 − $1,200 string lighting + $14,080 = **$48,680** |
| Difference | **$12,880** |
| Tent held and not used | 50% of the tent line = **$3,600** |
| Rain call | 72 hours before Sat 12 June 2027 = **Wed 9 June 2027** |

All six match the guide's stated answers. The tent lighting line says on the
face of the quote that it replaces the string lighting, which is what makes
the $12,880 right rather than $14,080 — that substitution is the thing the
prompt is meant to catch.

Mon 9's pair has to come out **$1,140 apart in exactly three differences**,
and it does: four guests over the 120 guarantee at $125 plus 22% service
($610), a cake-cutting fee of $420 the BEO waives, and an unsigned 30-minute
bar extension at $110. The BEO says in two places that the guarantee is a
minimum rather than a cap, which is what makes the twist true — if 124 people
came through the door, that line is correct and only the other two are
errors.

Tue 10's pair has to come out with **four mismatches and one match**. General
liability agrees at $1M/$2M on purpose; liquor liability is $1M against the
contract's $2M, the additional-insured and waiver-of-subrogation boxes are
blank, and the policy ends 31 March 2027, seventeen days before the event.
The insurance terms sit on **pages 3, 5 and 7** rather than in one list, and
the indemnity on page 7 covers the venue's own negligence — the thing to push
back on.

`check()` re-derives both deadlines from the event date rather than copying
them from the guide, and asserts the weekdays too: Sat 17 April 2027, client
certificate Thu 18 March, vendor certificates Sat 3 April. All three match.

`make_demo_files.py` builds the four PDFs and **fails the build if any total
is wrong**. The guide states the number each piece has to land on, and a demo
whose arithmetic does not hold ruins the Reel it exists for:

| | Headline | Real |
| --- | --- | --- |
| Venue proposal | $185.00 pp | **$47,062.00 = $261.46 pp** |
| AV quote A (Meridian Stage & Sound) | $8,400 | **$11,950** |
| AV quote B (Northgate AV Partners) | $9,100 | **$10,300** |
| AV quote C (Halcyon Event Technologies) | $11,200 | **$11,200**, genuinely all-in |

All three match the guide's stated answers exactly.

**The venue fees are spread across six pages, not listed together** — service
charge on the food and beverage page, coat check and linen on the room page,
cake cutting with the catering, bartender fees on the bar page, security with
staffing, and the administrative fee and overtime in the terms. That is the
piece: the fees you do not see in one place. The administrative fee carries
the line saying it is not a gratuity, as the brief asks.

The Google Sheet is 14 lines summing to exactly $100,000 with **no contingency
line** — the absence is the point of the Wed 4 carousel.

**Every venue and company here is invented** and no real client, venue or
employer appears. That is the standing rule, and it is also what makes these
safe to keep in a public repo — which they have to be, because Drive's
server-side upload fetches them from a `raw.githubusercontent.com` URL.

## Build

    python3 -m pip install --break-system-packages reportlab
    python3 make_demo_files.py

PDFs land in `files/`. `pdftoppm -r 70 -png` renders them for a visual check;
do that rather than trusting the generator, the same as for a Reel export.

## Garden Reception — Budget and Rain Plan (Sun 8, built Nov 1)

Not built by `make_demo_files.py`: it is a two-tab Google Sheet, made directly
in Drive `November 8` (folder `1L2H-JKLOIXFMNntUW1Ft2dLl2MtAIrcO`, created the
same day), id `1Y00Ga41aFYzGT7vCFBKAjWUIuo63ehCqGqS_SJVzWy8`.

Built six days early, off the note from the Claude.ai chat listing it as due
Fri 6. Its totals are **formulas, not typed figures**, and were read back after
writing:

| | Guide says | Sheet returns |
| --- | --- | --- |
| Outdoor plan total | $35,800 | **35800** |
| Tent quote total | $14,080 | **14080** |
| Tent held and not used | $3,600 | **3600** |

The rain-plan total the Reel turns on is **$48,680** — the outdoor $35,800,
less the $1,200 string lighting the tent lighting replaces, plus the $14,080
quote — and the difference is **$12,880**. Those two are the answer's job, not
the file's, so the sheet does not state them: the whole point of the piece is
that AI works them out from the two tabs. The trap is the tent lighting, which
adds $200 rather than $1,400.

The rain call is 72 hours before Sat 12 June 2027, so **Wed 9 June 2027**. The
sheet gives the rule, not the date, for the same reason.

## Week three — Thu 12 and Fri 13 (built Mon 9, `make_week3.py`)

Both were due by Mon 9 in the guide's CLAUDE CODE lines.

### Ticket Allocation — Annual Client Summit (Thu 12)

Drive `November 12` (`1o4pppjuH-8V_8yuje0_r_F1Rc5yjdjVf`, created the same day),
sheet id `1FTQoSTIJ7WqtmQ0NM_sQby7WRprE0tvQ-Itst1sYGUE`. Two tabs: **Allocation**
(clients 900, prospects 600, partners 250, speakers 100, staff 150 = 2,000) and
**Invite lists** (2,125 rows, one per person, from six account teams).

The whole Reel is one number — **140 people on one team's client list and a
different team's prospect list** — so `check()` proves it from the data rather
than from the brief: exactly 140 emails appear twice and none three times,
every pair straddles two teams *and* the two lists, no other email repeats, and
2,125 rows resolve to 1,985 people. Clients come out 40 over and prospects 85
over; 2,125 rows read as 125 over capacity and the event is in fact **15 seats
short of full**.

Then the same five figures were re-derived **inside the live sheet** with
temporary COUNTA/COUNTIF/SUMPRODUCT formulas and read back — 2125, 1985, 940,
685, 140 — before the formulas were cleared. The local build passing says
nothing about what actually landed in Drive.

**Getting 2,125 rows into a Google Sheet from here took three attempts, and the
two that failed are worth recording.** A CSV uploaded with
`GOOGLEDRIVE_UPLOAD_FROM_URL` arrives as **text/plain**, and Drive refuses to
convert that: `files.copy` with a target mimeType returns *"The requested
conversion is not supported."* `IMPORTDATA` into an API-created spreadsheet
returns **#REF!** whatever the URL — with em dashes percent-encoded and with a
plain ASCII filename alike. What works: build an **.xlsx** (openpyxl, not
installed here — `python3 -m pip install --break-system-packages openpyxl`),
upload it from a raw.githubusercontent URL, and copy *that* with
`GOOGLEDRIVE_COPY_FILE_ADVANCED` and `mimeType:
application/vnd.google-apps.spreadsheet`. The xlsx arrives with its real
mimeType and converts, carrying both tabs, the frozen header and the brand
colours. The staging xlsx and CSV were trashed afterwards.

Writing the rows through `mcp__Google_Sheets__update_values` was never an
option: the data lives in a file, so it would have to pass through the session
in chunks, and 2,125 generated rows cannot be retyped faithfully.

### Venue Quote — Fall Leadership Summit (Fri 13)

Drive `November 13` (`1dobgV369hK8hiSoB9chAM37OjXULkhLx`), file id
`1xvKEAWcixxMToNDme33ujj6qURGP15xS`. Two pages: $15,000 room + $30,000 F&B
minimum = **$45,000** for Saturday 16 October 2027, with the weekday asserted
rather than assumed.

Page 2 carries the line the piece turns on, set in 8pt grey where small print
belongs: *"Sunday-Thursday rates and multi-year agreements are available on
request."* Both pages were rendered at 70dpi and read before the upload.
