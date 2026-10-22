# Wrong entrance carousel — 2026-10-21

Status: **published 2026-10-22** at 9:17am ET on her go-ahead ("approved", Wed
21 ~10pm ET). The TikTok photo carousel is hers.

| Account | Post |
| --- | --- |
| Instagram `@aiforeventplanners` | https://www.instagram.com/p/DezEe6EkbUL/ |
| Facebook "The Event Planners AI" | https://www.facebook.com/122100389133449533/posts/122117062881449533 |

Instagram media `18415004578092095`, `media_type: CAROUSEL_ALBUM`,
`media_product_type: FEED`. **`is_shared_to_feed` is absent**, which is correct
for a carousel rather than a signal about it — that field only comes back on a
`REELS` item, so it says nothing here either way.

**All three captions hash identically**: `build/caption.txt`, the live Instagram
caption and the live Facebook message are all 889 characters,
sha256 `dc5287e3ecc6d36e33dbaa0ae87be06c9001603bca5788082605e35014c9b1ef`. Four
literal `#`, no `%23`, no "Hashtags:" label. Hashing both live captions against
the file is the character-for-character check, done without retyping either.

**Facebook surfaced on the first read-back**, 22 seconds after the Instagram
publish — faster than the ~15 minutes the notes warn about, so nothing was
retried.

Before posting: all five raw URLs returned 200 at exactly the committed byte
counts, and both duplicate checks came back clean, the newest entry on each
being the Oct 19 cancellation clause Reel.

**Child container ids came back non-monotonic** (…839, …842, …836, …833, …920
for slides 1–5), so slide order was taken from the results array index. Reading
order off the ids would have shuffled the carousel.

**It went out a day late.** The brief put it on Wed 21; it was built that
evening after she asked what she had missed, approved that night, and posted the
next morning. Thu 22 therefore carries three Instagram posts instead of two.

| Set | Size | Goes where |
| --- | --- | --- |
| `slides/instagram/` | 1080x1350 | Instagram + Facebook |
| `slides/tiktok/` | 1080x1920 | TikTok photo carousel — she posts it |

Content bank **item 16**, her own line: "They were told exactly which entrance.
They still used the wrong one."

Caption: `build/caption.txt`, the Wed 21 brief's wording verbatim. Four literal
`#`, no "Hashtags:" label, no retired "Prompt below." line.

## It was a day late, and that is the thing worth recording

The brief put this on **Wed 21** as the day's regular Instagram post. It was
never built. She was travelling, asked at 8pm what she had missed, and the
answer was that Pinterest had run and Instagram had not — three days after she
set the rule that a scheduled item must not be allowed to lapse.

Her instruction on being told: **"you need to be doing things i cant when im
away."** So this was built that evening without waiting to be asked again.

## The venue is invented, and the slide says so

The demo invitation is `Invitation — Autumn Patrons Reception` in the October
21 Drive folder, built Oct 14. It is for **The Harrow Museum of Design, New
York**, which does not exist — the brief specifies "made-up museum, no real
venue".

That matters for slide 4. The prompt asks for subway, bus and parking detail
*checked against the museum's own directions page*, and ends "tell me which
ones you couldn't confirm". For an invented museum the honest answer is that
**none of it could be confirmed**, and that is what the slide shows: the
entrance line in full, the transit section named but not invented, and the
flag underneath in maroon.

Listing plausible-looking subway lines for a museum that does not exist would
have the piece demonstrating the opposite of what its own prompt asks for.

## Slide 4 is house type, not a screenshot

The Oct 13 contingency carousel embedded a crop of her real ChatGPT answer
under "WHAT AI CAME BACK WITH". There is no recording for this piece, so the
Oct 18 precedent applies: set the output in house type under a heading that
claims no particular tool. It reads **"THE TEXT IT WROTE"**, which is honest —
the text was generated here from the demo invitation, and an AI did write it.

If she runs the prompt herself and sends a recording, swap a crop in and
relabel it to match Oct 13.

## Slides

| | |
| --- | --- |
| 1 | The hook, typographic on the dark ground. No photograph exists for this piece — the Oct 18 cover was her own plate, and there is no equivalent here |
| 2 | Why it matters: the front steps *are* the entrance as far as a guest is concerned |
| 3 | The prompt |
| 4 | The text it wrote, as a message bubble, entrance leading — plus what it could not confirm |
| 5 | "Put the entrance in the first line." and her day-of fix |

Palette, fonts and furniture match the Oct 18 runny eggs and Oct 13
contingency carousels. Slide 1 asserts the hook text has not drifted from the
bank line, and that it clears the top 12% and bottom 25% safe zones at both
sizes.
