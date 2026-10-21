# Pinterest — October pin run

Twelve pins for `@calmbeforetheaisle` (the coloring book shop), one pin
already published and eleven scheduled two a day from Oct 1.
`2026-10-pin-schedule.csv` is the working copy: the date, the image, its
Drive file id, the board, and the exact tagged link to post.

This is a separate workstream from the Reels and **needs nothing from this
repo at post time** — `PINTEREST_CREATE_PIN` takes the image bytes via
`media_source image_base64`, so there is no push-then-fetch step the way
Instagram and Facebook have. The schedule lives here only so it survives a
session ending.

## Where the source files are

Google Drive, `Coloring book/pintrest/`, folder id
`1MUMAJax9jXCUZwdmiGKUnvJF2Vv3kT6s`. Shared "Anyone with the link — Viewer",
so a session can fetch each image by its file id:

```
https://drive.usercontent.google.com/download?id=<FILE_ID>&export=download&confirm=t
```

All twelve verified 1000x1500 JPEG. Encode at full size, never downscale.

**`pin_copy_v4.csv` is the authoritative copy from 2026-09-30**, on the
author's instruction ("Post from pin_copy_v4.csv starting Friday"). It adds a
`Post date` column and holds the eleven unposted pins. Two older copies are
in the same folder and are both stale: `pin_copy (2).csv` (5 columns, no post
dates) and a 4-column one with no `Link` column that prices everything at
$5.99. `2026-10-pin-schedule.csv` here is generated from v4.

v4 changed more than the dates. Several pins moved from the 99c sampler to
the $5.99 book, so the split is now 3 sampler / 7 book / 1 Amazon rather than
9 / 3, and `pin_11_gift` points at the **Amazon paperback** (B0HL3B4CLM)
rather than Etsy.

v4 also arrived with `utm_campaign=calmbeforetheaisle` on every link and no
`utm_content`. **That was raised and reversed** (author, 2026-09-30: "switch
the tags back so we can still compare the sampler against the book"), because
one campaign name for everything cannot answer the question the convention
exists for. The schedule CSV here carries the restored tags; v4 in Drive still
has the flat ones, so regenerating from it means re-running the retag.

Also in that Drive folder and **not part of this run**: `pin_1.jpg`,
`pin_2.jpg`, `pin_3.jpg` and `pinterest_post.txt`, which belong to the six
pins published Sep 13-22.

## Accounts and boards

Composio account `pinterest_reking-alpha`, business account
`calmbeforetheaisle`. All three board ids verified live on 2026-09-29:

| Board | id |
| --- | --- |
| Wedding planning printables | `1148629148653722470` |
| Bridal shower gifts | `1148629148653722469` |
| Adult coloring pages | `1148629148653722468` |

The connection's cached `user_info` reports `board_count: 1`, which is stale
— `PINTEREST_LIST_BOARDS` shows five. Do not plan against the cached number.

Two older boards exist and are not used by this run: `Wedding Coloring
Pages` (`1148629148653658866`, the six earlier pins) and `Products you
tagged` (`1148629148653662359`, PROTECTED).

## Two things that constrain how this runs

**Two a day, never a batch.** Standing instruction from the author, stated as
mattering more than the rest of the brief: twelve pins at once on a new
account reads as automated, and two a day is the cadence in the October plan.

**Pins cannot be edited after posting.** `PINTEREST_UPDATE_PIN` returns
`your application does not have access to this restricted feature: pin_edit`.
Creating works, editing does not, and this is the app's access tier rather
than anything session-specific — so a wrong board, a typo or a missing link
cannot be fixed afterwards. Get it right at creation time. Verify board ids
before posting rather than after.

## Links and UTM

Nine pins point at the 99c 5-page sampler (listing `4581180302`), three at
the $5.99 full book (listing `4572665693`). The two prices are not a
discrepancy — they are two products.

Every link carries:

```
?utm_source=pinterest&utm_medium=social&utm_campaign=<sampler|book>&utm_content=<file stem>
```

`campaign` is the product, because the question worth answering is whether
the 99c sampler outperforms the $5.99 book; board tells you nothing about
that. Pin-level detail goes in `utm_content`.

Etsy's shop stats do not report UTM parameters — they show "Pinterest" as a
traffic source and nothing finer. The tags are kept anyway: they cost
nothing, Etsy ignores unknown parameters, and they become readable if pins
ever point at Gumroad or an owned page. The number that actually answers the
question is Pinterest's own outbound clicks per pin, which it reports
regardless.

**`pin_11_gift` is the one exception and keeps no UTM at all** — it points at
Amazon, not Etsy, and the author confirmed that is deliberate (2026-09-30).
Post its link exactly as it stands; do not "correct" it to an Etsy URL.

It went up on 2026-10-05 with `https://www.amazon.com/dp/B0HL3B4CLM` and no
tag, read back and confirmed. The one pin in the twelve that sends traffic
somewhere Pinterest's own outbound-click number is the only measure of.

`pin_01_bouquet` went out untagged on 2026-09-29 and **has since been tagged
by hand**, found on 2026-09-30 by reading the live pin rather than trusting
the earlier note:

```
...?utm_source=pinterest&utm_medium=social&utm_campaign=calmbeforetheaisle&utm_content=pin_01
```

So it carries the flat campaign name that was reversed the same day. It still
needs one word changed by hand — `calmbeforetheaisle` to `sampler` — because
`pin_edit` is not permitted at this API access tier.

That live pin also settles the form of `utm_content`: it is the **short
`pin_NN`**, not the full file stem, matching how the author wrote the
instruction ("keep utm_content=pin_XX on every link"). The schedule CSV uses
the short form throughout so the whole set is consistent with what is already
live.

**Read the live pin before assuming its state.** This session twice recorded
pin_01 as untagged from an old read; the author asked "are you sure that
hasn't been done already", and it had.

## Still outstanding, and the author's to do

- **Rewrite the six existing pin descriptions** (the Sep 13-22 pins). Listed
  the account on 2026-10-06: still untouched, and three of them are worse than
  "needs a rewrite".
  - ~~`1148629079995092117` (Sep 14) has **no title, no link and a single space
    for a description**. It is a dead pin sitting on the profile.~~
    **FIXED — confirmed live 2026-10-16.** It now carries the title "Wedding
    Flowers Coloring Page | Printable Adult Coloring Book", a full description
    ("Three vases of wedding flowers, before and after colouring...") and a
    tagged link, `utm_content=old_vase`. Nothing here wrote that and `pin_edit`
    is still refused for this app, so Sahiba fixed it in the Pinterest app.
    **It is the account's best pin: 62 lifetime impressions, 4 clicks** — more
    than half the per-pin impressions on the whole profile — so deleting it was
    always the wrong instinct, and it is moot now.

    Recorded because this session told her on 2026-10-16 that the Sunday
    Pinterest review was blocked on this pin and that deleting might be the
    only route. Both wrong, and the guide's own rule 6 says why: **check the
    live account before calling something undone.** The claim came from this
    file rather than from Pinterest.
  - `1148629079995007641` (Sep 13) links to `sahibaanandpaintal.etsy.com` with
    **no UTM tag**, and `1148629079995739314` (Sep 22) links with `?etsrc=sdt`,
    also untagged. Neither will ever show up as Pinterest traffic.
  - `1148629079995092123` (Sep 14) does carry a tag, `utm_content=old_blank`.
    Nothing here wrote that, so it came from the Mac queue or an in-app edit.

  All four are **Idea pins** (`creative_type: IDEA`), and `pin_edit` is refused
  for this app, so every one of these is an in-app fix only. Deleting the dead
  pin is possible from here — the connection can delete — but it is permanent,
  so it waits for the author to say so.
- The profile's website is a single listing URL rather than the shop root.
  The guide's Sep 30 Composio note treats that as sufficient, so this is a
  preference rather than a task.
- ~~Claim the Etsy shop in Pinterest settings.~~ **Dropped 2026-10-06**: the
  guide records that the Etsy claim option no longer exists in Pinterest
  settings, and that the profile website linking to the $5.99 listing covers
  it. It was carried here as an open item for a week after the guide had
  already closed it, so nothing was ever actionable.
- No pin has `alt_text` — the copy CSV has no column for it. Worth adding
  for accessibility and search; would need generating from the descriptions.
  One exception found on 2026-10-16: the Sep 22 pin does carry alt text, which
  she must have written in the app.

## What the Sun 18 review will find — read 2026-10-16

Pulled from `PINTEREST_LIST_PINS` with `include_metrics`, all 26 live pins.
Putting it here now so Sunday is not a surprise, **without pre-empting the
review itself** — the decision is hers with the content planning chat, and the
pre-registered condition is ~30 pins across four boards.

**Lifetime, across every one of the 26: 0 saves and 0 outbound clicks.** Not
one, on any pin, since Sep 13. That is the number the review turns on, and it
has not moved in five weeks.

Per-pin lifetime impressions, the only ones above zero:

| Pin | Created | Impressions | Clicks |
| --- | --- | --- | --- |
| `...95092117` vase | Sep 14 | 62 | 4 |
| `...95092123` | Sep 14 | 20 | 1 |
| `...96340621` pin_01 | Sep 29 | 12 | 4 |
| `...95739314` | Sep 22 | 7 | 1 |
| `...96575282`, `...96575283` | Oct 2 | 1 each | 0 |

**Every pin created Oct 3 or later reports 0 lifetime impressions** — 19 of
them. Treat that figure with suspicion rather than reporting it as fact: the
per-pin numbers sum to about 103 while the profile reports 213 monthly views,
so the per-pin impression counts are lagging or partial. The zero on outbound
clicks is the robust part, because it agrees with every earlier reading.

Oct 17 and 18 take the account to **32 pins**, which clears the guide's ~30
threshold. On the guide's own pre-registered rule, that means the problem is
the offer or the price rather than the marketing, and Pinterest goes on the
back burner rather than getting ad spend. Her call, on Sunday.

## Batch v6 — approved 2026-10-19, runs Tue 20 to Sat 24 Oct

15 pins, three a day, from `pin_copy_v6.csv` in her Drive folder. Generated
into `2026-10-pin-schedule-v6.csv` with board ids resolved and ISO dates.

**v6 uses a FOURTH board, and it is intentional.** `Wedding Coloring Pages`,
id `1148629148653658866`. This file's cached table did not carry it, so it was
put to her, and she confirmed on 2026-10-19: *"Wedding Coloring Pages (board ID
1148629148653658866) is intentional. It's the original public board. Post to it
as written."*

So it is not a new board and not a typo — it is the **original public board**,
created before the three this file has been tracking, and it already holds 5
pins. The ids were read live from `PINTEREST_LIST_BOARDS` rather than matched
against the table, which is the rule and is what surfaced it.

**The guide's review condition said "~30 pins across four boards" and this is
the fourth.** The Oct 19 review noted the four-boards half was unmet; it was
met all along, by a board this file did not know about. That does not change
the review's outcome — she overruled it anyway — but the caveat was wrong and
should not be repeated.

| Board | id |
| --- | --- |
| Wedding planning printables | `1148629148653722470` |
| Bridal shower gifts | `1148629148653722469` |
| Adult coloring pages | `1148629148653722468` |
| **Wedding Coloring Pages** | **`1148629148653658866`** |

Checked before anything was scheduled, because nothing is editable afterwards:

- all 15 images **1000x1500 JPEG**, byte-identical to Drive
- titles 44–61 characters, descriptions 287–347 — inside Pinterest's caps
- all four board names resolve to live ids
- all 15 raw GitHub URLs return `200 image/jpeg` at the exact byte count
- **UTM tags survived.** Thirteen Etsy links carry
  `campaign=sampler|book` with `utm_content` set to the pin stem. The two
  Amazon links are untagged, which matches `pin_11` and `pin_27` and is
  deliberate.
- **Only `pin_42_samplerstart` links to the 99c sampler.** Every other Etsy
  link goes to the $5.99 book, which is the guide's rule: the sampler holds
  five pages and a pin for any other page links to the full book.
- `alt_text` still **null**. v6 has no column for it. Fourth batch running —
  worth asking her for a column.

### Scheduled

| Fires | Pins | Trigger |
| --- | --- | --- |
| 2026-10-20 13:30 UTC | `pin_28`, `pin_29`, `pin_36` | `trig_019L2mVu4eJJC7MxkXhYZ26a` |
| 2026-10-21 13:30 UTC | `pin_30`, `pin_31`, `pin_37` | `trig_01Ufh57wyFHhaEkjbXujTkDu` |
| 2026-10-22 13:30 UTC | `pin_32`, `pin_33`, `pin_39` | `trig_01HbLMEtgRVQP1ekbhPsYFrf` |
| 2026-10-23 13:30 UTC | `pin_34`, `pin_38`, `pin_40` | `trig_01GV5g81WZUKAJ98LAmBuUGx` |
| 2026-10-24 13:30 UTC | `pin_35`, `pin_41`, `pin_42` | `trig_018DkYECJm42BFWTUb12k9Ec` |

13:30 UTC is **9:30am ET**, the same slot v5 ran. Every firing is before the
Nov 1 clock change, so all five land at 9:30am her time.

Each trigger names its own three pins rather than deriving them from the CSV,
so a firing cannot post the wrong three if the file moves.

## DECIDED 2026-10-19: Pinterest keeps running. She overruled the review.

The review below recommended the back burner, which is what the guide's own
pre-registered rule calls for at zero outbound clicks. **She said no, keep
posting.** Her call, and it is the decision of record — a future session
reading the recommendation below should not act on it.

No ad spend either way: that rule was never in question and still stands.

The queue is empty as of Oct 19, so nothing can run until she sends the next
batch of pin copy. Three a day, as the v5 batch ran.

## The Sun 18 review — the numbers, read 2026-10-18

The queue is finished. `pin_14_aisle`, `pin_17_kitcoloured` and `pin_24_mug`
went up at 9:33am ET, which takes the account to **33 pins across three
boards** and clears the guide's ~30 threshold. So the review can finally run
against the condition it was written for.

Pulled from `PINTEREST_GET_ACCOUNT_ANALYTICS`, which is a better source than
the per-pin `include_metrics` figures used on Oct 16 — those summed to about
103 against a profile reporting 213 monthly views, so they were lagging or
partial. The account edge agrees with itself.

| | Baseline, Sep 15–28 | Posting, Sep 29 – Oct 18 |
| --- | --- | --- |
| Pins live at the end | 6 | **33** |
| Impressions | 133 | **144** |
| Pin clicks | 16 | **12** |
| Saves | 0 | **0** |
| **Outbound clicks** | **0** | **0** |

**Nought outbound clicks, and nought saves, across 27 pins in twenty days.**
That is the number the review turns on, and it has not moved once since Sep 13.

The impressions line looks flat and is worse than flat. **All 133 baseline
impressions landed on a single day, Sep 22** — Pinterest's initial
distribution test — and every other day of that fortnight was zero. The
posting window's 144 is spread over twenty days of actual pinning, with its
own two spikes on Oct 1 (19) and Oct 15 (51). So four-and-a-half times the pin
count bought no more distribution than one unprompted test did.

Honest caveats, both of which cut the same way:

- **Oct 17 and 18 are still `PROCESSING`** and Oct 16 reads a flat zero, so
  the last three days are not final. Today's three pins are twenty minutes old
  and cannot have data at all.
- The zero on outbound clicks is the robust part, because it agrees with every
  earlier reading from every endpoint. No lag explains a metric that has never
  once been non-zero.

**On the guide's own pre-registered rule, this is the back-burner outcome, not
the ad-spend one.** The creative is not the problem: the tap rate across both
windows is 8–12%, which is healthy. People look and do not click through, and
nobody saves — and on Pinterest saves *are* distribution, so a pin with no
saves is never redistributed. That points at the offer or the price, which is
not something more pins or paid impressions can fix. The standing rule holds:
no ad spend, and the threshold for revisiting is **one organic outbound
click**.

Her call, with the content planning chat.

## The batch landed on 2026-10-14, and the gap it leaves

`pin_12_whatyouget` went up on Wed 7 Oct and was the last of the Sep 29 batch,
so **nothing posted between Oct 8 and Oct 13** — seven days dark. The blocker
was always copy rather than images: the guide named `pin_13` and `pin_14` as
"already cropped to 2:3" but carried no titles, descriptions or links for them,
and the batch of 15 due Mon 5 Oct never arrived. The live doc was re-read on
Oct 6 and Oct 7 and was unchanged both times.

She approved it on **2026-10-14**, and it arrived as `pin_copy_v5.csv` in the
Drive folder with fifteen images, `pin_13` to `pin_27`. All fifteen are now in
`images/` and `2026-10-pin-schedule-v5.csv` is generated from v5 with board ids
resolved.

**v5 is three a day, not two**, running Tue 13 to Sat 17. Worth noting against
the standing "two a day, never a batch" rule — three is close enough to keep
the intent, and the dates are hers.

**The queue shifted one day.** v5 starts Tue 13, which had already passed when
the batch landed, so running it as written would have meant six pins in one
day — exactly the burst the rule guards against. It now runs Wed 14 to Sun 18.

### What was checked before the first three went out

Nothing can be edited at this access tier, so all of it was checked at
creation time rather than after:

- all fifteen images are **1000x1500 JPEG**, byte-identical to Drive
- titles 49-59 characters, descriptions 251-331 — well inside Pinterest's caps
- the three board names resolve to the three live board ids, read from
  `PINTEREST_LIST_BOARDS` rather than trusted from this file's cached table
- the raw GitHub URLs return `200 image/jpeg` at the exact byte count
- **the UTM tags survived.** v4 arrived with a flat
  `utm_campaign=calmbeforetheaisle` on every link and had to be re-tagged by
  hand; v5 carries `campaign=sampler|book` with `utm_content` set to the pin
  stem, so the question the convention exists for is still answerable. The two
  Amazon links carry no tags, matching `pin_11`.
- `alt_text` is still **null**. v5 has no column for it, and it is permanent
  here, so it stays unwritten rather than invented. Third batch running — worth
  asking her for a column.

### The rest of the queue is scheduled

The four remaining days are set as one-shot wake-ups rather than left to be
remembered, now that scheduling is permitted from here (she added
`send_later` to `permissions.allow` on Oct 12):

| Fires | Pins | Trigger |
| --- | --- | --- |
| 2026-10-15 13:30 UTC | `pin_13`, `pin_16`, `pin_22` | `trig_019bKjDHgwAVGcdRc3MiK21o` |
| 2026-10-16 13:30 UTC | `pin_18`, `pin_19`, `pin_25` | `trig_019LVmp6gAZsqmRj9mavZJXL` |
| 2026-10-17 13:30 UTC | `pin_20`, `pin_23`, `pin_27` | `trig_01NtVsq395gFGQPn2ZTZ65nK` |
| 2026-10-18 13:30 UTC | `pin_14`, `pin_17`, `pin_24` | `trig_01Pb9KyLRjU3KTHzQceqx79o` |

Each names its own pins rather than deriving them, so a firing cannot post the
wrong three if the CSV moves. The Sun 18 one also carries the review and the
"schedule is dry again from Mon 19" flag.

### The Tue 14 review cannot run as specified

The guide sets a review for **Tue 14 Oct** against "~30 pins across four
boards". With the seven dark days, the account stands at **21** — six from
September plus twelve, plus today's three — across three boards. The review's
own threshold is not met, so a zero-outbound-click reading today would be a
verdict on a gap in posting rather than on the offer or the price. It should
move to after the queue finishes on **Sun 18 Oct**, which lands it at 33 pins.

## The Mac's scheduled tasks were running a second, pre-v4 queue (2026-10-01)

A local Claude session on the author's Mac had its own Pinterest schedule in
`~/.claude/scheduled-tasks/pin-*/`, one task per pin — "pin 2 of the 1-5 Oct
batch of 10", ten pins across Oct 1-5, against this file's twelve across Oct
2-7. The author stopped the chat, but the scheduled tasks fire on their own
timer whatever the chat is told, so they had to be deleted rather than
called off.

Nothing of it reached the account. Verified 2026-10-01 by listing all three
target boards directly as well as the account feed: `Adult coloring pages`
and `Bridal shower gifts` are empty, `Wedding planning printables` holds only
`pin_01` from Sep 29. No pin exists with a Sep 30 or Oct 1 creation date.

**Its manifest was pre-v4, and its safety check could not have caught that.**
The `pin-oct01-pm-cake` task has `pin_03_cake.jpg` linking to the 99c sampler
(`4581180302`) with a description stating "99c". In v4 `pin_03` is one of the
pins that moved to the **$5.99 book** (`4572665693`). Its step 1 opens the
sampler listing and refuses to post unless the live price reads $0.99 — which
it does, so the check passes and the superseded copy goes out. The price was
never the thing that was wrong; the product was. A check that validates copy
against the listing the copy itself names cannot detect copy pointing at the
wrong listing.

It also held `pin_11_gift.jpg` back permanently for a copy error — "claims a
50-page book for under $1" — that v4 had already fixed by pointing pin_11 at
the Amazon paperback. So its queue would have under-posted by one as well as
mis-posting pin_03.

The general lesson, since this will recur as long as two sessions can both
reach the account: **a second scheduler is a duplicate-post risk even when it
is correct, and pins cannot be edited or cleanly deleted at this API access
tier.** Pinterest posting runs from the cloud session only.

## Posted log

| Date | Pin | Board | Pin id |
| --- | --- | --- | --- |
| 2026-09-29 | `pin_01_bouquet` | Wedding planning printables | `1148629079996340621` |
| 2026-10-02 | `pin_02_dress` | Adult coloring pages | `1148629079996575282` |
| 2026-10-02 | `pin_07_cover` | Adult coloring pages | `1148629079996575283` |
| 2026-10-03 | `pin_04_arch` | Wedding planning printables | `1148629079996676934` |
| 2026-10-03 | `pin_05_ring` | Bridal shower gifts | `1148629079996676933` |
| 2026-10-04 | `pin_08_fifty` | Adult coloring pages | `1148629079996771403` |
| 2026-10-04 | `pin_10_coloured` | Adult coloring pages | `1148629079996771404` |
| 2026-10-05 | `pin_03_cake` | Adult coloring pages | `1148629079996849379` |
| 2026-10-05 | `pin_11_gift` | Bridal shower gifts | `1148629079996849380` |
| 2026-10-06 | `pin_06_table` | Wedding planning printables | `1148629079996935180` |
| 2026-10-06 | `pin_09_printed` | Wedding planning printables | `1148629079996935181` |
| 2026-10-07 | `pin_12_whatyouget` | Bridal shower gifts | `1148629079997014987` |
| 2026-10-14 | `pin_15_sampler5` | Adult coloring pages | `1148629079997617009` |
| 2026-10-14 | `pin_21_cakedetail` | Adult coloring pages | `1148629079997617008` |
| 2026-10-14 | `pin_26_paperbackgift` | Bridal shower gifts | `1148629079997617007` |
| 2026-10-15 | `pin_13_plannerskit` | Wedding planning printables | `1148629079997699620` |
| 2026-10-15 | `pin_16_ringdetail` | Bridal shower gifts | `1148629079997699623` |
| 2026-10-15 | `pin_22_archdetail` | Wedding planning printables | `1148629079997699625` |
| 2026-10-16 | `pin_18_bouquetcoloured` | Wedding planning printables | `1148629079997788394` |
| 2026-10-16 | `pin_19_howtoprint` | Adult coloring pages | `1148629079997788393` |
| 2026-10-16 | `pin_25_coverquiet` | Adult coloring pages | `1148629079997788395` |
| 2026-10-17 | `pin_20_showerstation` | Bridal shower gifts | `1148629079997878754` |
| 2026-10-17 | `pin_23_candles` | Wedding planning printables | `1148629079997878755` |
| 2026-10-17 | `pin_27_engagementgift` | Bridal shower gifts | `1148629079997878756` |
| 2026-10-18 | `pin_14_aisle` | Wedding planning printables | `1148629079997970612` |
| 2026-10-18 | `pin_17_kitcoloured` | Adult coloring pages | `1148629079997970616` |
| 2026-10-18 | `pin_24_mug` | Adult coloring pages | `1148629079997970614` |
| 2026-10-20 | `pin_28_seatingchart` | Wedding planning printables | `1148629079998142919` |
| 2026-10-20 | `pin_29_rsvp` | Wedding planning printables | `1148629079998142918` |
| 2026-10-20 | `pin_36_maidofhonor` | Bridal shower gifts | `1148629079998142920` |
| 2026-10-21 | `pin_30_emergencykit` | Wedding planning printables | `1148629079998228369` |
| 2026-10-21 | `pin_31_rainplan` | Adult coloring pages | `1148629079998228367` |
| 2026-10-21 | `pin_37_guestbook` | Wedding Coloring Pages | `1148629079998228368` |

Both Oct 2 pins read back live on `calmbeforetheaisle`, right board, title,
description and tagged link exactly as this directory's schedule CSV holds
them. One read-back each, no retry.

## Posting route: `image_url`, not base64 (from 2026-10-02)

`pin_01` went up with `media_source image_base64`. That works, but a
1000x1500 JPEG here is 120-340 KB, which is 160k-450k characters of base64
inside the tool call for an image that never changes — paid again on every
pin.

The eleven unposted images are now committed under `images/`, and pins are
created with:

```
media_source: { source_type: "image_url",
                url: "https://raw.githubusercontent.com/eventplannerai123/eventplannersai/main/pinterest/images/<file>" }
```

Pinterest fetches it server-side, the same way Meta fetches a Reel. Confirm
the raw URL returns `200 image/jpeg` at the expected byte count before the
call. Drive stays the author's working copy; `images/` is what actually gets
posted, and the two were verified byte-identical on download.

This retires the note above that this workstream "needs nothing from this repo
at post time" — it now does, in exchange for not re-encoding every image.

## Still open: `alt_text`

Both Oct 2 pins went out with `alt_text: null`, matching `pin_01` and the copy
CSV, which has no column for it. Not invented here: alt text is permanent at
this access tier and would be unreviewed copy on a customer-facing pin. Worth
asking the author to add a column for the next batch rather than writing it
unilaterally.

## Deleting a scheduled task's files does not stop it firing (2026-10-02)

The author deleted the `pin-*` folders under `~/.claude/scheduled-tasks/` on
the Mac and the runs kept arriving — `pin-oct02-am-arch` fired at 9:00 her
time on Oct 2, for `pin_04_arch.jpg`, and surfaced on her phone through Remote
Control.

That is the expected behaviour, and worth writing down because it is
counter-intuitive: **the folder holds the task's instructions, the schedule
itself lives in the account.** Removing the folder leaves the timer intact and
the run then fails on a missing file — which is exactly the "can't find the
file" message she had been getting. The schedule has to be deleted as a
schedule.

Nothing of it reached the account: all three target boards listed directly at
13:33Z on Oct 2 hold only `pin_01` and the two posted from here that morning.

Those Mac tasks are local to that computer and **do not appear in this
session's `list_triggers`**, so they cannot be stopped from here. Only the
author can remove them, from the machine that owns them.

## A duplicate this session nearly caused, and the rule that follows

This session's own Routine `trig_0169hJ1CezAfwKaiTeNuHhp1` was set to post
`pin_02` and `pin_07` at 13:48Z on Oct 2. Both had already gone up at 11:28Z,
posted by hand earlier in the same conversation. The Routine would have posted
both a second time, and a duplicate pin cannot be edited or cleanly removed.
It was disabled at 13:32Z, sixteen minutes before firing.

**Posting a day's pins early does not cancel that day's Routine.** Whenever a
scheduled item is done ahead of its trigger, disable the trigger in the same
breath — `update_trigger` with `enabled: false`, which is reversible, rather
than `delete_trigger`. The remaining pin Routines (Oct 3, 4, 5, 6 and 7) are
untouched and still correct.

The scheduled prompts still describe the `image_base64` route and a Drive
download. That route works and was not changed; the images committed under
`images/` make the cheaper `image_url` route available to any run that
prefers it.

## pin_27 went out with an untagged link, on purpose

`pin_27_engagementgift` points at `https://www.amazon.com/dp/B0HL3B4CLM` with
no query string at all, where every other pin in v5 carries the
`utm_source=pinterest&utm_medium=social&utm_campaign=…&utm_content=pin_XX` set.

That is the CSV she approved on Oct 14 and it was posted verbatim, which is
the standing rule — pins cannot be edited at this access tier, so a guessed
tag would have been permanent too.

It is also the right call on the merits: **Amazon ignores `utm_*` entirely.**
Attribution there runs through Amazon Attribution tags (`tag=…`), which is a
different mechanism and is on the guide's list to set up from Sun 18 Oct. A
utm string on an Amazon link buys nothing; a `tag=` value invented here would
be worse than none.

So the pin is permanently unattributable and that costs approximately nothing:
the account has recorded **0 outbound clicks across 26 pins in five weeks**.
Worth noting rather than fixing, and worth remembering when the Amazon
Attribution setup lands — **future Amazon pins want a `tag=`, not a `utm_`.**
