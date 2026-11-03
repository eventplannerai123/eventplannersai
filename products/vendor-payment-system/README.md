# The Vendor Payment System — the Gumroad listing

**Status: draft built Tue 3 Nov. Nothing is published.** She approves the
listing on Wed 4, and the Wed 4 CLAUDE CODE line publishes it and sends her the
**product page** link (not the storefront) for her Thu 5 bio change.

Price **$24**, her decision of Mon 2 after testing both prompts on her own inbox
and a real contract. Black Friday is **$7 off with code BLACKFRIDAY ($17)**,
Fri 27 to Mon 30 — created on Thu 26, not now.

## The draft

`https://aiforeventplanners.gumroad.com/l/epbvxs` — permalink `epbvxs`, id
`KKvcHyyE7HsIBWM4TmRisA==`, **unpublished**. Cover, description, summary,
tags, the four detail rows and the $24 price are all set, and the tracker is
attached as a content button.

**The PDF is attached at publish, not now.** `add_file` fetches from a public
URL and copies the file into Gumroad's storage, and the only way to hand it one
from here is a Drive link shared for that single call. Doing that today would
mean doing it twice if her review changes a line of the guide, so the upload
waits until the Wed 4 publish — and it is the first step of it, before
`publish_product`, never after.

## What the buyer gets

| | |
| --- | --- |
| The tracker | a **make-a-copy link** to the Vendor Payment Tracker, as a content button |
| The guide | `Vendor Payment System — Setup Guide.pdf`, 5 pages, built here |

**The make-a-copy URL is the whole point of that link**:
`…/1q1RvBQZFvzctAt8Q0WB0Q7p3gW6U8JLQyw6DjX26FMo/copy`. The sheet is shared
"anyone with the link — viewer", checked before building, so `/copy` opens
Google's own copy dialog and no buyer ever lands on the original. Closing that
was the last item on the internal checklist before selling.

## The product itself is NOT in this repo, deliberately

The repo is public — that is what makes the `raw.githubusercontent.com` URLs
Meta, Pinterest and Gumroad fetch from work — so neither the built PDF **nor
`guide_text.py`** is committed. The six prompts are the product; putting them
here would publish a $24 download for nothing. A first attempt to commit this
directory was blocked for exactly that, and the block was right: the
`.gitignore` rule written at the time covered the PDF and not the text, which
is the same leak in a different file.

What is committed: `make_pdf.py`, `make_cover.py`, the fonts, this README and
the cover. The generator carries no product text, and the cover is an
advertisement.

**The live Google Doc is the source of truth**
(`19_SNj602VDJidoTFTg0C6g4EPasygdSPgXNv3-NrTRw`, in
`Event planners AI > Products > Vendor Payment System`). To rebuild, read that
doc and write `guide_text.py` beside `make_pdf.py` carrying `TITLE`,
`SUBTITLE`, `INTRO`, `SECTIONS`, `PROMPTS_INTRO`, `PROMPTS`, `RULES` and
`TRACKER_COPY_URL`, then:

    python3 make_pdf.py        # -> Vendor Payment System — Setup Guide.pdf
    python3 make_cover.py      # -> cover.png, 1280x720

**Why not just export the Doc as a PDF:** the Tue 3 line asks for it "in the
brand look", and a Docs export comes out in Docs' own default styling. The PDF
is laid out here in lavender `#CECBF6`, deep purple `#3C3489` and Poppins, with
each prompt on a tinted panel in a mono face, because a buyer is going to select
and copy those and a prompt that looks like body text invites a partial
selection.

A first build left "Prompt 6. Payment summary for a client" alone at the foot of
a page with its block overleaf; `make_pdf.py` now measures the panel before
drawing the heading, so a prompt and its name always travel together.

## How the file reaches Gumroad without going public

`add_file` fetches from a public https URL and copies the file into Gumroad's
own storage, so the source only has to be reachable for that one call. The PDF
therefore goes up through Drive: uploaded to
`Event planners AI > Products > Vendor Payment System`, shared "anyone with the
link", fetched by Gumroad, then **locked back down**. Never through this repo:
a raw.githubusercontent URL is permanent and indexed.
