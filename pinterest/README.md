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

`pin_01_bouquet` was published untagged on 2026-09-29, before the convention
was settled. The author asked on 2026-09-30 for it to be tagged too, but
`pin_edit` is not permitted at this API access tier, so **it can only be done
by hand in the Pinterest app.** The string it needs:

```
https://www.etsy.com/listing/4581180302/printable-wedding-coloring-pages-5-page?utm_source=pinterest&utm_medium=social&utm_campaign=sampler&utm_content=pin_01_bouquet
```

`utm_content` is the **full file stem** (`pin_01_bouquet`), not a bare
`pin_01`, matching the convention as the author first wrote it on 2026-09-29.

## Still outstanding, and the author's to do

- **Claim the Etsy shop in Pinterest settings.** Affects attribution on
  everything, including pins already up.
- **Rewrite the six existing pin descriptions** (the Sep 13-22 pins).
- The profile's website is a single listing URL rather than the shop root.
- No pin has `alt_text` — the copy CSV has no column for it. Worth adding
  for accessibility and search; would need generating from the descriptions.
