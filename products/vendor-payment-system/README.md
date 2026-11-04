# The Vendor Payment System — the Gumroad listing

**LIVE since Tue 3 Nov**, a day ahead of the Wed 4 line: she reviewed the
listing that afternoon and said publish.
<https://aiforeventplanners.gumroad.com/l/epbvxs> is the **product page** — the
link for her Thu 5 bio change, not the storefront.

Price **$24**, her decision of Mon 2 after testing both prompts on her own inbox
and a real contract. Black Friday is **$7 off with code BLACKFRIDAY ($17)**,
Fri 27 to Mon 30 — created on Thu 26, not now.

## The listing

`https://aiforeventplanners.gumroad.com/l/epbvxs` — permalink `epbvxs`, id
`KKvcHyyE7HsIBWM4TmRisA==`, **published**. Cover, description, summary, tags,
the four detail rows and the $24 price are all set, the tracker is attached as
a content button and the setup guide as the file.

**Her Nov 3 pass on the copy**, after reading the draft: the tagline stands
alone, `What's inside`, `What the prompts actually do` and `What you need` are
`<h3>` headings rather than running into the body, the six prompts are an
`<ol>`, and Prompt 1's line is hers — "pulls the payments for one event from 90
days of email into a table shaped to match the tracker". Category went from
`other` to `business-and-money`. Gumroad takes `<h3>`, `<ul>`, `<ol>` and
`<strong>` in `description` and renders them, so the formatting is real markup
rather than blank lines.

She also rewrote `custom_receipt_text` herself; leave it alone.

**Re-exported Nov 3 from her own edits.** She rewrote the guide and the
tracker the same day: Step 3 says where to paste and that the grey columns
fill themselves, Step 5 runs Prompt 4 before Prompt 3, Prompt 1 returns all
fifteen tracker columns (the three computed ones blank), Prompt 3 says how to
get the tab out, Prompt 4 catches vendor mail that never names the event, and
there is a fifth rule about checking totals. She then went back to Prompt 1
once more the same day: a literal "not stated" in a date or amount cell is
text in a numeric column, which stops the tracker computing Due date, Days
until due and Flag, so those come back blank with the words in Notes. Last
of all, Prompt 6's bracket was brought into line with Prompt 3's: both now tell
the buyer how to get the Payments tab out. The transcription was re-taken
from the live doc and checked **both ways** — every string in it appears in
the doc, and every paragraph of the doc appears in it — and Prompt 1's column
list was checked against `Payments!A1:O1` in the sheet itself rather than
against the doc's description of it. A prompt that writes into a tracker is
verified against the tracker.

**The PDF is attached: one file, 35,510 bytes, checked against the local
build's sha256.** She asked for it on before Wed 4, so it went up on the Tue 3
listing pass rather than at publish.

**SHE PUT IT IN DRIVE, BECAUSE THIS SESSION CANNOT.** `add_file` fetches from a
public URL, and there is no way to put 35 KB of local bytes on one from here:
`mcp__Google_Drive__create_file` takes the content inline, and transcribing
47,348 characters of base64 through a tool call produced a 12,795-byte file —
a corrupt PDF, caught by comparing the returned `fileSize` to the local one and
trashed. (**Always compare that size.** The call reported success.) Publishing
it through this repo is barred for the same reason as ever, and an artifact
asset upload was refused. So the handover is hers: she drops the PDF into
`Products > Vendor Payment System`, this session finds it and attaches it. One
message, and it uses the workflow she already has for recordings.

**No share step was needed**, and none is possible: the file inherits
`role: reader, type: anyone` from the Products folder, and changing a
permission from here is refused. So there is nothing to lock back down either —
the folder's sharing is what it is, and the guide PDF now sits behind an
unguessable link like the tracker does.

**Gumroad lists the file as `BIN`, not PDF.** Drive serves
`application/octet-stream` whatever the URL form (`drive.usercontent`,
`drive.google.com/uc`, both checked), so that is the type Gumroad recorded at
fetch time. The bytes are right and the name carries `.pdf`, so a buyer
downloads a working file; only the type badge is wrong, and only the Gumroad
editor can change it. **There is no `remove_file` tool**, so a second
`add_file` would leave two files on the product — do not retry the attach to
fix cosmetics.

**AND THAT MEANS THE FILE CANNOT BE REPLACED FROM HERE.** On Nov 3 she added a
line to Prompt 1 ("Don't add up totals; the tracker does the math") and asked
for the PDF on the product to be swapped. The Gumroad toolset has `add_file`
and `list_files` and nothing that removes one, so attaching the new export
would leave two files with the same name and no way to delete either. A swap
is a Gumroad-editor job: delete the old file there, upload the new one. Do not
attempt it with `add_file` — the duplicate is permanent from here.

**She did the swap on Nov 3, and `list_files` then reported two files that are
not two files.** It returned the current export (35,544 bytes, type `PDF`,
`position: null`) *and* a 35,510-byte `BIN` at `position: 1` — the leftover of
the earlier attach from Drive. On the strength of that, she was told buyers
would get both. **She checked the editor and saw one file, and she was right.**

So: **`list_files` lists records, not the product's contents**, and a record
with no `position` is not attached to anything. Read the editor, or ask her
to, before telling her a buyer gets two downloads. The content question is
answerable without the file list at all — have her open the attached file and
look at the end of Prompt 1, which carries the Nov 3 line if it is current.
Confirmed current that evening: "its the correct file i checked".

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

**Three layout faults, all fixed, all found by measuring the render.** `prompt()` advanced
the cursor only by the text it had drawn, leaving the panel's own bottom
padding above it — so the next prompt's name printed inside the previous
tint (pages 3 and 4) and the padding read 18pt at the bottom against 7pt at
the top. It now ends the cursor below the panel, and both pads measure 14.9pt.
Separately, the tracker URL overshot the right margin by 44pt: a URL has no
spaces, so the wrapper could not break it. `link()` now shrinks it until it
fits and asserts that it does. Third, the re-export stranded "Prompt 4. Change
check" at the foot of a page with its panel overleaf — the very thing the
keep-together rule exists to stop. The panel starts 6pt **above** the cursor,
and `prompt()` tested the cursor while `build()` tested the panel, so a prompt
that fitted by 3pt broke anyway. Both now measure the panel's own top, and
`build()` asserts that a prompt's name and its panel land on the same page.

**Check the rendered pages before calling a build finished** — `pdftoppm -r 150
-png`, then the rightmost inked column against `W - M` and the tint bands for
their padding. None of the three showed up in the text, and the third appeared
only after her edits moved the page breaks.

## How the file reaches Gumroad without going public

`add_file` fetches from a public https URL and copies the file into Gumroad's
own storage, so the source only has to be reachable for that one call. The PDF
therefore goes up through Drive: uploaded to
`Event planners AI > Products > Vendor Payment System`, shared "anyone with the
link", fetched by Gumroad, then **locked back down**. Never through this repo:
a raw.githubusercontent URL is permanent and indexed.

## TikTok Pixel on Gumroad, and the new-advertiser credit (looked up Nov 4)

The Wed 4 block asked whether Gumroad supports the TikTok Pixel, because the
matching credit reportedly needs one. **It does — but not through Gumroad's own
TikTok Pixel field.** That field is reported broken: `analytics.tiktok.com` is
missing from Gumroad's `script-src` Content Security Policy, so the pixel never
loads and a seller using that field gets no tracking at all. The working route
is Gumroad's **third-party analytics code snippet**, with a standard
"Place an Order" event carrying the order value.

**On the credit, the blogs were wrong.** They all quoted matched credit up to
$6,000 in tiers from $200 of spend. She registered the account on Nov 4 and the
offer actually in it is **two tiers and no more**:

| Spend | Credit |
| --- | --- |
| $200 | $200 |
| $500 | $500 |

**So the ad test as planned earns nothing.** The Thu 5 block sets it at about
$10 a day for 5 to 7 days — $50 to $70 — and the first tier starts at $200.
Matching any credit means committing $200, which is a different decision from
the one the plan describes, and it is the Sun 8 decision's real shape.

**The account, read from the API on Nov 4** (connector `TikTok for Business`,
live the same day): advertiser id `7704289498087194632`, "AI for Event
Planners1104", USD, `America/New_York`, US, balance $0, status
`STATUS_SELF_SERVICE_UNAUDITED`, and **no `owner_bc_id`** — it is not under a
Business Center, so the exclusion worry above does not apply to it.

**The lesson worth keeping: the sign-up screen settled in one line what nine
blogs could not.** Every figure in them was wrong by an order of magnitude for
this account. Where a number is visible in the product itself, read it there.

Written into the guide's Wed 4 block as the answer that line asked for, with
the task struck and the answer left unstruck so it stays readable.
