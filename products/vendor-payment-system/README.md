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

**And the coupon is dated, which decides more than the tiers do.** It is the
**H2'26 New Advertiser Coupon**, marked *Conditional*, code `GKOLCCEJGOKMMNAP`,
**valid 2026-12-04 07:00 to 2027-01-03 12:18**. So the money moves in December,
not this month — the credit cannot be burned on Black Friday (Nov 27–30), which
ends a week before the window opens.

Read the window as *when the earned credit can be spent*, not as when the
qualifying spend must happen; "Conditional" means the coupon sits in the
account until the spend condition is met. **That reading is not certain from
the text alone**, and the account screen can settle it, so check before
committing $200 on the strength of it.

What the dates do settle either way: **this is a December decision about the
coloring book, not a November one about the Vendor Payment System.** Dec 4 to
Jan 3 lands squarely in what her own November plan calls peak proposal season
(December to February), which is when the engagement-season Stories start and
when the book has its best case for paid reach. The launch Reel is long cold by
then.

**And there is a second notice on that screen that may kill the test outright.**
Her words, Nov 4: *"Starting October 7, 2026, unverified TikTok accounts can't
be linked to ad accounts for ad creation. Existing linked accounts will not be
affected."*

Two facts, both read from the API the same day:

- **`identity/get/` on the new ad account returns an empty list.** Nothing is
  linked to it. The ad account was created Nov 4, so the "existing linked
  accounts" grandfather clause cannot apply to her.
- **`@aiforeventplanners` reports `is_verified: false`.**

So the planned test — promoting the launch Reel as a Spark Ad from her own
account — needs exactly the link the notice restricts. **What "unverified"
means there is not defined in the notice**, and it is not the blue tick in
every TikTok context, so do not conclude the test is dead; the identity picker
in Ads Manager when building an ad is where it is settled in one look.

What it does mean is that the Sun 8 decision has a prior question. If the
account cannot be linked, the only ad available is one with a custom identity —
a video under a generic display name, with no account behind it and no
engagement carried over. That is a weaker thing than the test was designed to
measure, and a reason to drop it that has nothing to do with the $200.

**Nothing can be built in the account yet, not even paused.** On Nov 4 she
asked for the ad to be ready to look at, so `campaign/create/` was called with
`operation_status: DISABLE` — a paused campaign that cannot spend. TikTok
refused it outright:

> Your account has an outstanding payment or no valid payment method. Check
> your billing settings to continue.

Nothing was created. So a **payment method has to be on the account before any
object exists in it**, which puts the card before the campaign rather than
after it — the opposite of the order the plan assumes, and a thing to decide
rather than drift into.

**She put $100 on the account on Nov 4 and the campaign now exists, paused:**
`campaign_id 1880931999927201`, "Vendor Payment System — Gumroad traffic test",
objective TRAFFIC, `operation_status: DISABLE`, no budget at campaign level.

**The ad group stops on a number, and it is not a small problem.** In a USD
account TikTok's floor is **$20 a day** for a daily budget, or **$140** for a
7-day lifetime budget. The plan is $10 a day for 5 to 7 days. **That campaign
cannot be created at all** — $70 is under the floor by either route, and the
API refuses rather than rounds.

So the shapes actually available are:

| Shape | Spend | Credit earned |
| --- | --- | --- |
| The plan, $10/day × 7 | $70 | impossible — under the floor |
| Floor, $20/day × 7 | $140 | $0, short of the first tier |
| $20/day × 10 | $200 | $200 |

The middle row is the trap: it is the smallest run TikTok will accept, it costs
twice what the plan says, and it still earns nothing. **The honest choice is
$200 or nothing**, and that is the Sun 8 decision stated properly.

The ad group was deliberately **not** created at the floor. Raising her stated
budget without asking would have buried the whole finding inside an object that
merely looked ready.

**The lesson worth keeping: the sign-up screen settled in one line what nine
blogs could not.** Every figure in them was wrong by an order of magnitude for
this account. Where a number is visible in the product itself, read it there.

Written into the guide's Wed 4 block as the answer that line asked for, with
the task struck and the answer left unstruck so it stays readable.

## The BUDGET automation is live (Fri 6 Nov, 7:20am)

Set up in ManyChat by the browser Claude on her Chrome, not from here — her
Nov 3 decision. It missed Thursday evening because Chrome was off, so it went
live about thirteen hours after the Reel.

Attached to [reel/DfYN-IEDf_G](https://www.instagram.com/reel/DfYN-IEDf_G/)
specifically: the free plan allows one automation per post and four live at
once, which is exactly the four BUDGET Reels planned (Thu 5, Mon 9, Tue 10,
Tue 17). A fifth means retiring one first.

**Nobody was missed by the gap.** `INSTAGRAM_GET_IG_MEDIA_COMMENTS` on that
media returned an empty list, so no one commented BUDGET before the
automation existed and there is no one to answer by hand. The note she added
to the guide says the same.

Her own comments will never trigger it, so the test needs someone else.

## The weekly Story image

`make_story.py` → `story/vendor-payment-tracker-story.jpg`, 1080x1920. The
guide's Fri 13 line asks for "a screenshot of the filled Vendor Payment System
tracker"; this is a brand-look render of it rather than a literal screengrab,
because a Google Sheet is 16:9 of mostly empty columns and a Story is 9:16.

**Every number is read from the live tracker**, `Vendor Payment Tracker —
May 15, 2027 wedding` (`1P6zCWC18kY-SC2oocX7xzZcEMF0CXxEg3f6qDqdiOqo`), the
one filled from the Nov 2 inbox test — including the two that recompute daily,
Due this week ($9,680) and Due in the next 30 days. Every vendor in it is a
demo vendor from the product's own test emails, which is what makes it safe to
publish.

**It carries no headline and no CTA.** Her Sat 14 YOU line puts the text
"Every vendor payment in one place," and the Gumroad link sticker on top in
the app; a printed line underneath a sticker reads as a mistake. The empty
band under the grid is where the sticker goes.

**Re-rendered each week from the live sheet, 2026-11-20 for her Sat 21
Story.** Three figures moved since the Nov 13 build: Petal Press' $680 went
six days past its Nov 14 due date, so the sheet's Flag column now reads
**Overdue** on that row and the generator has a chip for it — filled red with
white text, the loudest thing on the card, because a caught late payment is
the whole argument for the tracker. Fernwood's second payment came due today,
so Due this week fell from $9,680 to $9,000. "Next payment due" still reads
Nov 14 because that row is unpaid; that is the sheet's own arithmetic and the
Overdue chip on the same row explains it, so it is left as the tracker states
it. The grid now carries eleven rows rather than ten — the card holds eleven
and the generator asserts the last one is in frame, along with the Overdue row
itself.

**Column widths are measured, not typed.** The first build ran "Second
payment" straight through the Amount column and pushed the "Due this week"
chip off the card; the generator now measures every column against the real
strings and asserts the flag column ends inside the card.

## Thu 19's recording folder (prepared 2026-11-17)

The guide's Thu 19 CC line asked for this by Mon 16 and it had not been done —
found on the Tue 17 audit, and it blocked her, because step 1 of her recording
is "open the tracker link CC saves in Reels > November > November 19".

Drive `November 19` is `1QbiCyJL5p2bj8EZZfQJ2LthAZxrOSLvW`, created under the
`November ` month folder (trailing space, `1nENfiitkVU06xQsAuPKINBKTj3RliX--`).
It holds:

- **`Vendor Payment Tracker`**, `1f6Yg3f6Yhhn6crxLyB8I0sV3apQOpdEZTNmjG5ET-z8`
  — a copy of the product master (`1q1RvBQZFvzctAt8Q0WB0Q7p3gW6U8JLQyw6DjX26FMo`),
  not the master itself, so a clumsy click during the recording cannot touch
  what buyers get. Her "make a copy" link is the file's edit URL with `/edit`
  replaced by `/copy`.
- **`Catering Agreement — Harbor Light Catering — May 15 2027.pdf`**,
  `114txqystv5ArbI4xqZTJNbPDpg3jKhAx`, for step 4.

**The eight practice emails are still under the Gmail label** "Reel — vendor
payments", all eight, and their figures still match the brief: five deposits
totalling $13,300 paid, Petal Press $680 (which was due Nov 14, so it reads as
overdue on a Nov 17 recording, exactly as the brief wants), Fernwood Estate
$9,000 due Nov 20.

**The guide said 18 payments and there are 17.** Its own enumeration lists 17
— Fernwood 3, Harbor Light 3, Bloom & Bough 2, Lumen 2, Sound Theory 2, Petal
Press 1, Crumb & Co. 2, Tall Order 2 — and the filled tracker
(`1P6zCWC18kY-SC2oocX7xzZcEMF0CXxEg3f6qDqdiOqo`) holds 17 rows. Corrected to 17
in both places in the doc, the Mon 2 practice-run line and the Thu 19 block.
Nothing on screen cites the count, so no build depended on it.

## Testing whether ChatGPT can write into the tracker (her call, 2026-11-17)

She asked mid-recording why step 3 is a copy-and-paste at all, and told me to
test the alternative this week.

**The capability is real and officially documented**, which the Nov 17 search
settled: OpenAI's own help article
[ChatGPT for Excel and Google Sheets](https://help.openai.com/en/articles/20001063-chatgpt-for-excel-and-google-sheets)
describes a sidebar add-on that builds and updates spreadsheets directly,
installed from the Workspace Marketplace and opened from the Extensions menu.
The [Marketplace listing](https://workspace.google.com/marketplace/app/chatgpt/870214997678)
lists "Edit and update existing spreadsheets" and says it works on Free, Go,
Plus and Pro. That replaces the vendor-blog answer given earlier the same day,
which could not be relied on.

**What still has to be tested, and why it needs her**: the add-on installs into
a Google account and runs against an open sheet, so it cannot be exercised from
this session. The test is five minutes on her laptop, against a throwaway copy
rather than the product master.

Two things to decide from the result, not from the fact that it works:

- **Does it land in the right columns?** The tracker's grey columns (Due date,
  Days until due, Flag) must stay empty — they calculate themselves — and the
  example row in A2 has to be replaced rather than pushed down, or the summary
  carries the example's $17,150.
- **The privacy line changes.** The Marketplace listing says workbook content
  may be shared with Google and OpenAI so the add-on can read and update the
  sheet. Buyers paste vendor contracts and payment amounts into this tracker,
  so if this route goes into the guide it is named in the guide, not buried.

**Chased Fri 20, and she has not run it.** Looked before asking: no copy of
the tracker in her Drive has been touched since Nov 17 14:34, which is the
Thu 19 recording itself — the newest `Copy of Vendor Payment Tracker`
(`17QiIcUwwH4JS60BauHZetIpWoZIEQVg9NTxjEQwhzGE`) holds the pasted result from
that take, with the grey columns computed by the sheet's own formulas. That is
the paste route working, not the add-on.

So the test went over with a throwaway already made for it: **`ADD-ON TEST —
throwaway copy (not the product)`**, `1_GflodLs6EOdz2LyHsNkASitqp-1fFgc4U2NDZnZvMQ`,
copied from the product master (`1q1RvBQZFvzctAt8Q0WB0Q7p3gW6U8JLQyw6DjX26FMo`)
into `Products > Vendor Payment System`. The master is the right source
because it still carries the Spring Gala example row at A2 and its $17,150 —
which is what makes the second question answerable at all. **The pass/fail
number is the Summary's Total scheduled: $21,500 if the example row was
replaced, $38,650 if it was pushed down.**

**RUN SAT 21 NOV, AND IT PASSED BOTH CHECKS.** Read off the throwaway copy
here rather than taken on her word:

- **Total scheduled reads $21,500**, which is 6,000 + 9,000 + 6,500. The
  Spring Gala example row was **replaced**, not pushed down — $38,650 would
  have meant the opposite.
- **The grey columns calculated themselves and the add-on did not type over
  them.** Row 3 carries Due date Nov 20, Days until due -1, Flag "Overdue";
  row 4 carries Dec 1, 10, "Due in 30 days". It filled only the lavender
  columns, which is what the sheet's "How to use" line asks of a human.

**Three rows is the right answer, not a fault.** She flagged that the
Payments tab "only has 3 line items" — the prompt asked for exactly three
payments, so three is correct. Worth recording because it is the obvious
thing to misread as a failure.

One cosmetic liberty: it wrote "Wedding" in the Event column where the
example row said "Spring Gala". Nothing depends on that column.

**So the capability is confirmed and the question is now editorial**, not
technical: whether it goes into the setup guide as an optional step, with
the privacy line the Marketplace listing requires — workbook content may be
shared with Google and OpenAI so the add-on can read and update the sheet.
Buyers paste vendor contracts and payment amounts into this tracker, so if
this route goes in the guide it is named in the guide, not buried.

## The missing-value test, Sat 21 Nov — and it changed the recommendation

She pushed back on leaving the add-on out: "i didnt like it when the paste
didnt work the first time", and she was right that it hadn't. On Nov 3 the
pasted result came back with the computed columns blank, because ChatGPT had
written a literal "not stated" into a date or amount cell and text in a
numeric column stops the tracker calculating. The fix then was a **prompt**
fix — Prompt 1 rewritten the same day to return those cells blank with the
words in Notes.

So the open question was whether the add-on shares that flaw, since it is the
same model deciding what to put in a cell. Her words: "i dont want other
people to have the same problem." The test, run on the throwaway in a fresh
sidebar chat, with **nothing in the prompt about leaving cells blank** —
because a buyer would not know to say it:

> Add two more payments to the Payments tab. Fernwood Estate, Venue — final
> balance, due Apr 15 2027, unpaid; the contract doesn't state the amount.
> Bloom & Bough, Florals — deposit $1,200, unpaid; the contract doesn't state
> when it's due.

**It got both right, unprompted:**

| | Amount | Fixed due date | Computed columns | Notes |
| --- | --- | --- | --- | --- |
| Fernwood, final balance | **empty** | Apr 15, 2027 | 145 days, "Upcoming" | "Contract doesn't state the amount." |
| Bloom & Bough, deposit | $1,200 | **empty** | "No due date" | "Contract doesn't state when it's due." |

That is exactly the behaviour Prompt 1 had to be rewritten to produce, done
without being asked, and the tracker's own formulas kept working on both rows.

**So the recommendation here was wrong and is reversed.** It argued the
add-on was not worth the privacy line, partly on the grounds that it would
carry the same failure and hide it where a blank column at least showed. It
does not carry it. The add-on belongs in the setup guide as an **optional**
step, with the Marketplace privacy line stated plainly: workbook content may
be shared with Google and OpenAI so the add-on can read and update the sheet.

One honest limit: this is one run of one case. It is the case that actually
burned her, which is why it is worth acting on, but it is not proof the
add-on never puts text in a numeric cell.

**The test also found a real gap in the product, which is worth more than
the add-on question.** With the two new rows the Summary reads **Total
scheduled $22,700** — 6,000 + 9,000 + 6,500 + 1,200. That is correct
arithmetic and a misleading number: there are five payments and one of them
has no amount, so the real total is $22,700 *plus Fernwood's final balance*.
Nothing on the Summary tab says so. A buyer would read $22,700 as the whole
commitment.

The tracker already counts things it wants you to notice — "Overdue payments"
is a count row. A second one, **"Payments with no amount yet"**, would close
this in the same idiom and cost one formula. Raised with her Sat 21; hers to
decide, and it is a change to a product people have bought.

**The paste stays the default**, and the reason is unchanged and has nothing
to do with reliability — see below.

**The paste is not only a limitation.** It is where a buyer checks the amounts
against the invoice before they become the record — which the setup guide tells
them to do, and which has nowhere to happen if the model writes straight in. If
the add-on works, it belongs in the guide as an optional step with that warning
attached, not as the default.
