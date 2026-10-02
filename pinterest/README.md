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

- **Claim the Etsy shop in Pinterest settings.** Affects attribution on
  everything, including pins already up.
- **Rewrite the six existing pin descriptions** (the Sep 13-22 pins).
- The profile's website is a single listing URL rather than the shop root.
- No pin has `alt_text` — the copy CSV has no column for it. Worth adding
  for accessibility and search; would need generating from the descriptions.

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
