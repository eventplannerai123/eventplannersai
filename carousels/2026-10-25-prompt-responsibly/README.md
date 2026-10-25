# Prompt Responsibly carousel — 2026-10-25

Status: **published 2026-10-25** at 8:46am ET on her go-ahead ("approved").
The TikTok photo carousel is hers.

| Account | Post |
| --- | --- |
| Instagram `@aiforeventplanners` | https://www.instagram.com/p/De6vTzFINrn/ |
| Facebook "The Event Planners AI" | https://www.facebook.com/122100389133449533/posts/122117563893449533 |

Instagram media `18413654191091529`, `media_type: CAROUSEL_ALBUM`,
`media_product_type: FEED`.

**All three captions hash identically**: `build/caption.txt`, the live Instagram
caption and the live Facebook message are all 335 characters,
sha256 `be0db41082c8ac55dafe8334b025143c7bec241cdaf1ae5f5b8dc78d3863f7c0`.

**Facebook surfaced on the first read-back**, 17 seconds after the Instagram
publish.

Before posting: all four raw URLs returned 200 at exactly the committed byte
counts, and both duplicate checks came back clean — the newest entry on each
was still Thu 22's staffing rebuild, because **nothing went out on Fri 23 or
Sat 24**.

**Child container ids were non-monotonic again** (…857, …866, …863, …860), so
slide order came from the results array index.

| Set | Size | Goes where |
| --- | --- | --- |
| `slides/instagram/` | 1080x1350 | Instagram + Facebook |
| `slides/tiktok/` | 1080x1920 | TikTok photo carousel — she posts it |

Four slides: her photo of the hat, then the three rules. No demo file and no
prompt, so the caption carries no `AI Prompt:` block.

## The photo was checked, not assumed

The brief says never to name the conference or whoever gave the hat out, so the
frame was examined rather than trusted: the hat carries only the words "Prompt
Responsibly", and the out-of-focus background is a kitchen counter with no
legible text or branding anywhere. Nothing needed removing.

It came off her phone as **HEIC at 4284x5712**, which nothing here opens
without `pillow-heif`. The decoded JPEG is committed as `build/hat.jpg` — it is
a photograph of a hat on a counter, with no faces, no venue and no third-party
branding, so it is not raw footage under the repo rule.

**Each size takes its own window out of the original** rather than one crop
being squashed to fit both: 1080x1350 trims top and bottom, 1080x1920 trims the
sides. The line sits over the maroon brim, where cream type reads cleanly and
covers none of the hat's own lettering.

The hat's colours — cream and maroon — are the house palette already, which is
why slides 2-4 sit against it without a jump.

## Slides

| | |
| --- | --- |
| 1 | The hat. "Got this at a conference. It's the rule I work by." |
| 2 | 1. Give it the whole picture |
| 3 | 2. Check everything it gives you |
| 4 | 3. Keep client names out of it + "Prompt responsibly." |

**Slide 1's line is broken by hand.** Wrapped to the panel width it orphans
"by." on a line of its own.

## Caption

`build/caption.txt`, the brief's wording verbatim. Four literal `#`, no
"Hashtags:" label.
