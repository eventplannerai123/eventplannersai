# Prompt Responsibly carousel — 2026-10-25

Status: **built, not posted.** Instagram and Facebook run from here after her
go-ahead; the TikTok photo carousel is hers.

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
