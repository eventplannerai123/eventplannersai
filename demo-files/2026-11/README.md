# November demo files

Her Oct 14 rule, restated in the November plan: **every demo file a prompt
needs is built when the post is planned, not on the day.** These are week
one's.

| Built for | File | Drive |
| --- | --- | --- |
| Mon 2 | `Venue Proposal — Winter Gala.pdf` (6 pages) | `November 2` |
| Wed 4 | `Event Budget — Spring Conference` (Google Sheet) | `November 4` |
| Fri 6 | `AV Quotes — Spring Conference` — Quote A, B, C (3 PDFs) | `November 6` |

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
