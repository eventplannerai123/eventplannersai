# Sat 7 Nov 2026 — Things I've said into a walkie-talkie this year

**Instagram image post, 6:30pm Eastern (23:30 UTC).** Also to Facebook.
TikTok is the same image as a photo post, hers to upload, in the timing test's
**9am slot** — so it goes up *before* the Instagram post, which is why the cut
had to exist and be approved on Fri 6.

Planner-life post 1 of 4 (content bank 33, weekly from November).

| | |
| --- | --- |
| Instagram | `slides/walkie-talkie-instagram.jpg` — 1080x1350 |
| TikTok | `slides/walkie-talkie-tiktok.jpg` — 1080x1920 |

## The lines are hers

Four came from her verbatim on Nov 5. Five more she picked from a list
drafted here and approved in one message ("1 - 4 and 6"), which makes those
hers as well — the guide's "use her lines exactly; never invent one" is about
not putting words in her mouth, and an approved line is not an invented one.
Nothing on this image went on unasked.

**Eight, not nine.** She cut one of her own on sight: "1 and 3 are too similar
cut 1", so *I need extra staff at registration* came out and the
directional-duties one stayed, which makes the same point somewhere less
obvious.

Her wording is exact, with two changes she made herself: the spelling of
*beginning*, and *the meal* to *the lunch*.

Order is hers first, in the order she sent them, then the five she picked.

No names, venues, clients or employer anywhere — role and room only. The
generator asserts it rather than trusting a read-through.

## Build

`make_post.py`, 1080 wide, brand system from the guide: lavender `#CECBF6`,
deep purple `#3C3489`, Poppins (700 for the title and the numbers, 400 for the
lines), EP + star wordmark over the handle. Poppins has no glyph at U+2726, so
the star is a drawn polygon. The three weights are committed under
`build/fonts/`.

**The two sizes are laid out, not scaled.** The title size is searched
downward until the whole block fits the window, and the window differs:

| | Window | Result |
| --- | --- | --- |
| 1350 | y 150 to 1160 | title 84px, list ends y=1130 |
| 1920 | y 254 to 1416 — TikTok's top 12% and bottom 25% | title 84px, list ends y=1310 |

So nothing important sits under TikTok's caption or its right-hand buttons,
and the wordmark on the 1920 sits above the bottom 25% rather than inside it.

A wrapped line hangs on the number's column instead of returning to the
margin, which is why line 3 reads as one item rather than two.

## Caption

`build/caption.txt` — the guide's own text for this day, same for TikTok. No
AI prompt line: this piece has no prompt in it.
