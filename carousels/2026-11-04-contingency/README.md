# 2026-11-04 — "If the budget is $100,000, $5,000 should have no name on it."

**Status: built two days early. Not shown to her yet** — her one open item today
is the Vendor Payment System review that gates Thursday's launch, so this goes
to her on Tue 3, which is still the night before its 9am TikTok slot.

Six slides, both sets, in the guide's own structure for the day: the claim, why
budgets actually go over, what a contingency line is, the prompt, what AI gives
back from the demo budget, the closer. Content bank item 20.

## Slide 5 is computed, not written

The guide's CLAUDE CODE line says to run the prompt on `Event Budget — Spring
Conference` and put the result on slide 5. The figures therefore come out of
the file, and `make_slides.py` asserts them rather than trusting the copy:

- the 14 lines sum to **$100,000**
- 5% of that is **$5,000**
- the six trimmed lines sum to **exactly $5,000**, so the rebalanced total is
  still $100,000
- no trimmed line is also one of the three flagged as at risk
- there are **six** trimmed lines, because the slide says "six lines" in words

The three flagged lines are the three the file itself makes vulnerable, each
with the reason it moves: plated lunch $14,800 (priced per head, guaranteed
before the real number is in), AV and production $11,200 (on-site additions and
overtime past strike), evening reception bar $4,200 (billed on consumption).

A carousel whose arithmetic does not hold ruins the point it is making, which
is why the checks run before a single slide is drawn.

## Brand look

The guide's, not the Halloween build's: lavender `#CECBF6`, deep purple
`#3C3489`, Poppins, EP✦ wordmark, numbered badge, bottom bar. **No motif band**
— that was a Halloween device and does not carry over. Poppins is committed
under `build/fonts/`; the star is a polygon, because Poppins has no glyph at
U+2726.

`build/preview.png` is the six Instagram slides side by side. Look at it before
sending anything.

## Caption

`build/caption.txt`, the guide's text with the prompt under its own `AI Prompt:`
label.

## Published Wed 4 Nov, 6:30pm Eastern

Posted from the one-shot task `trig_013gietq9YW34DsDxdNPCghy` on her Mon 2
approval.

| | |
| --- | --- |
| Instagram | [p/DfVpQwQDQYi](https://www.instagram.com/p/DfVpQwQDQYi/) — media `18484287427117419`, `CAROUSEL_ALBUM`, 6 children |
| Facebook | multi-photo post `1233196746554445_122119656693449533` |

Live caption read back and diffed against `build/caption.txt`: identical, 547
characters, line breaks and all five hashtags intact.

**Slide order verified on the published post, 1→6 at MAD 0.00 each**, with the
next-nearest source slide 7.50 or further away. Worth doing rather than
trusting the ordering rule: the child container ids came back non-monotonic
again — request order ended 896, 890, 887, 893, 965, 968 — so ordering the
parent's `children` by id instead of by the child calls' **results index**
would have shuffled slides 1 to 4.

The check needs a second network: `scontent-*.cdninstagram.com` is refused by
this session's proxy, so the published images and the committed slides were
both pulled inside Composio's remote sandbox and compared there.

Facebook took `FACEBOOK_CREATE_MULTI_PHOTO_POST` with the six raw URLs and the
same caption, which uploads each photo unpublished and then makes one feed post
from them — the same shape as the Halloween carousel.
