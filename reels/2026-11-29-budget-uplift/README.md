# Sun 29 Nov, 6:30pm — "Last year's summit: $107,800."

Content bank 22, "Last year's budget is not this year's budget", taken one
step further: where next year is already quoted, use the quote instead of the
uplift. Two cuts, 19.68s, from her Tue 24 screen recording.

## The guide's figure was a dollar out, and the screen wins

The brief predicted the answer would land on **$113,180** and wrote the
voiceover as "a hundred and thirteen, one-eighty". It didn't. Two lines land
on a half-dollar at 3% — printing $1,905.50 and insurance $1,287.50 — and the
answer kept both rather than rounding up, so what is on screen, twice, is
**$113,179**.

A voiceover that says a number the frame contradicts is broken, so the
script, both captions and `demo-files/2026-11/annual_summit_actuals.py` all
moved to the screen's figure. The generator now works in `Decimal` and
asserts the three numbers the piece depends on:

| | |
| --- | --- |
| Eleven lines | $107,800 (catering $142 × 250) |
| Flat 3% on everything | $111,034 — the wrong answer |
| Two quotes + 3% on the nine | **$113,179** |
| Gap on the flat uplift | **$2,145**, not $2,146 |
| What the answer leads on | $5,379 over the 2026 actuals, 4.99% |

**Worth correcting in the guide.** It is a dollar, but the caption states it
and the overlay sits next to it.

## The twist is hers, arrived at backwards

Her Sun 29 YOU line asks for the one thing she would still change. She said
she would change nothing and asked what this session thought.

The answer's section 2 — "Lines most likely to increase faster than 3%" —
opens with **venue rental and catering, both High**, and the reason it gives
is that they are already confirmed at 8.33% and 6.34%. Those are the only two
lines in the budget that are contracted. A risk list is for what can still
move, and the nine unquoted lines are ranked beneath the two that can't. She
agreed: *"yes thats the twist"*.

It is beat 3, the last line of the voiceover, and the caption's third
paragraph.

## The recording

`ScreenRecording_11-24-2026 10-08-59 AM_1.mp4`, Drive id
`1QNjIGDj23u8fSZbGFTRs6MnQ0mfRCsd_` in November 29. **59 MB, not in this
repo** — the repo is public and only finished cuts belong in it;
`make_beats.py` reads it from `$SUN_SRC`.

1206x2622 at 60fps, 32.35s, no rotation side data, so the crop is recomputed
as `crop=1206:2144:0:478` — 478 off the top, nothing off the bottom.

**Clean end to end.** A half-second scan of all 65 frames found no advertiser
and no ChatGPT "Get Plus" pop-up, so unlike Mon 23 there is no window to
assert beats out of. It opens exactly as asked: the prompt in the box, the
PDF chip above it, the send tap at about 1.0s.

## The cuts

| | Instagram | TikTok |
| --- | --- | --- |
| hook 0:00–0:02.3 | "Last year: $107,800. Two vendors already quoted next year higher." | "Stop adding 3% to last year's budget." |
| b0 the 2027 column | 3.60s | 3.40s |
| b1 the prompt | 3.40s | 3.30s |
| b2 down to TOTAL | 3.60s | 3.70s |
| b3 the risk table | 4.20s | 4.40s |
| b4 the summary | 4.88s | 4.88s |

**19.68s**, 1080x1920, 30fps, CRF 19, AAC 192k at 48 kHz, `+faststart`,
**-14.0 LUFS**. Eryn, `eleven_v4`, measured -24.5 LUFS / -1.2 dBTP and swept
+11.0 → -15.0, +12.0 → -14.3, **+12.4 → -14.0** into
`alimiter=limit=0.891:level=0`. The voiceover is the only audio.

**It opens on the payoff, not the prompt** — the brief's own instruction, so
$113,179 is on screen at t=0 and the 6-second ceiling is met at frame one.

## This one does carry the BUDGET CTA

Unlike Mon 23 and Tue 17, where it came off. The Nov 14 rule is to read the
closing line against the piece, not to ban it: this is a budget, and the
guide calls it the one money piece inside the Black Friday window. So
`make_cards.py`'s assert is **inverted** — it requires the CTA and requires
its deadline, because a code with no date is a promise with no end.

**ManyChat is paused, so the DM is hers by hand.** Her Sun 29 YOU line says
so outright. The card is only honest while she is watching the comments.

The takeaway and the CTA run back to back over the last beat, 1.6s then
1.4s, rather than stacking: two lavender panels at once on a dense page of
text reads as a mistake.

## Posting

- **Instagram and Facebook at 6:30pm Sunday**, after she approves Sat 28.
- **TikTok**, hers, at about 9am — different hook, slightly different pacing,
  and a caption that says "Comment BUDGET on my Instagram" because there is
  no bio link there and the automation lives on Instagram.
