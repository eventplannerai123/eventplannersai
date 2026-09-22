# Tablecloth sizing carousel — 2026-09-22

Six slides, 1080x1350, JPEG (the Instagram carousel API requires JPEG, not
PNG, per the guide's carousel production standard).

Status: **published 2026-09-22.**

| Account | Post |
| --- | --- |
| Instagram `@aiforeventplanners` | https://www.instagram.com/p/Ddl4KrWoPVd/ |
| Facebook "The Event Planners AI" | https://www.facebook.com/122100389133449533/posts/122110942545449533 |

Both captions read back live and compared to the approved text byte for
byte - identical, four literal `#`, no "Hashtags:" label, no comment
keyword. All six Instagram alt texts read back correct and in order.

CTA: none of the retired kinds. This is a reference carousel, not a prompt
piece, so it ends on a question rather than "the full prompt is in the
caption below". No "link in bio" - the bio hub does not exist yet.

## The two wrong numbers, caught before posting

The first version of the slides had round-table **half-drop** figures that
did not match the cheat sheet:

| Row | First version | Cheat sheet (source of truth) |
| --- | --- | --- |
| 48" round | 90" | **78"** |
| 72" round | 108" | **102"** |

It also carried a `30/36" cocktail | 42" | - | 120" rd` row that appears
nowhere in the PDF. By the formula that value is right for a 36" cocktail
(36 + 2x42) but 6" over for a 30" one, and the row covered both.

What made the half-drop errors especially catchable: the same slide stated
**"lap length = width + 30""** directly above the table. 48 + 30 = 78, and
the table said 90. The piece contradicted itself on the slide designed to
be screenshotted and saved.

The rewrite fixed all of it: correct figures, cocktail row removed, and
"lap length" replaced with the source's own "half drop / full drop"
vocabulary, which removes the formula-versus-table contradiction entirely.

## Verification against `Tablecloth_Sizing_Cheat_Sheet.pdf`

Every figure on the final slides, re-checked one at a time. The PDF has no
text layer, so it was rendered and read at 200 dpi.

| Row | Half drop | Full drop | Matches PDF |
| --- | --- | --- | --- |
| 48" round | 78" | 108" | yes |
| 72" round | 102" | 132" | yes |
| 36" square | 66" | 96" | yes |
| 6 ft rectangle | 102x60" | 132x90" | yes |
| 8 ft rectangle | 126x60" | 156x90" | yes |
| 60" round (callout) | - | 120" | yes |

Each was also re-derived independently from `table size + (drop x 2)` with
half drop 15" and full drop 30". All correct.

## The swipe mechanic

The zoom illusion is the whole premise, and **it can only be confirmed on a
device** - which the author did before giving the go-ahead. Attempting to
measure the zoom programmatically was abandoned: JPEG noise and the dark
glyphs sitting inside the pink panel made every automated measurement
unstable, and reporting a number that unreliable would have been worse than
reporting none. What a contact sheet does show is a monotonic, evenly paced
progression where each slide adds exactly one new element - square-cloth
line, then drop definitions, then the formula, then the title.

## Facebook alt text

**Not set, and not settable from here.** Per the guide, `alt_text_custom`
returns a permissions error for the Composio app's access level and every
photo comes back `alt=NONE`. Instagram alt text works fine through the same
pipeline. Facebook alt text has to be added by hand, per photo, via
Edit -> Alt text.

## Method

Instagram: six child containers via `INSTAGRAM_POST_IG_USER_MEDIA` with
`is_carousel_item: true` and a per-slide `alt_text`, then
`INSTAGRAM_CREATE_CAROUSEL_CONTAINER` with the children in slide order and
the caption, then publish. Child container IDs are **not** returned in a
predictable numeric order, so the order of the results array is what
determines slide sequence - not sorting the IDs.

Facebook: `FACEBOOK_CREATE_MULTI_PHOTO_POST`, which performs the guide's
confirmed method - upload each photo with `published=false`, then one
`/feed` post referencing them as `attached_media`. The packaged
CREATE_POST / CREATE_PHOTO_POST / UPLOAD_PHOTOS_BATCH tools cannot produce
a captioned multi-photo album.

Both platforms were posted by separate direct API calls. Instagram's "also
share to Facebook" toggle is deliberately not used - it is in-app only and
Meta decides unpredictably what form the Facebook copy takes.
