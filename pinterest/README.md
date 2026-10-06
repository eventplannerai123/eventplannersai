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
  - `1148629079995092117` (Sep 14) has **no title, no link and a single space
    for a description**. It is a dead pin sitting on the profile.
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

## The schedule runs dry after Wed 7 Oct (checked 2026-10-06)

`pin_12_whatyouget` on Wed 7 is the last scheduled pin. The guide wants two a
day through the **Tue 14 Oct** review, so **Oct 8-14 needs fourteen more** and
none exist.

The blocker is copy, not images. The guide's Pinterest section says a **batch of
15 pins was due Mon 5 Oct** and that `pin_13` (planner's kit) and `pin_14`
(aisle) "are already cropped to 2:3 and count toward it" — but the doc carries
**no titles, descriptions or links for either**, and the batch itself never
landed. Checked the live doc on 2026-10-06: that one sentence is its only
mention of them.

So both stay unscheduled. Do not draft their copy here: these are
customer-facing pins on a product account, the copy is the author's, and
**nothing posted can be edited afterwards** at this access tier.

The pin sources the guide lists in build order are still unused and would cover
the fourteen: the eight Etsy listing images, individual sample pages (each page
its own pin), the printed-book photos, and the partially-coloured walkie-talkie
page.

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
