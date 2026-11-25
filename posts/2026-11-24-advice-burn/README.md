# Tue 24 Nov — "Event planning advice I'd burn." The first weekly hook test.

Her Nov 19 format: every week one extra piece is tested on non-followers
before it reaches the feed. Two versions of one new Reel, **identical except
the title**. She uploads both from her phone with Trial turned on — this
session cannot post trials — on the Tuesday morning. Friday she compares
views and non-follower reach at 72 hours, taps "Share to everyone" on the
winner and leaves the other as a trial. Facebook gets only the winner, after
it is shared.

Trials are extras: they never replace the day's 12:30pm or 6:30pm post, and a
tested piece is never also posted as a regular Reel, which would trip
duplicate-content detection.

| | Title |
| --- | --- |
| **A** | "Event planning advice I'd burn." |
| **B** | "17 years in, here's the event planning advice I'd burn." |

## Where the five lines came from, stated plainly

**They are a draft she edited, which is not the same as hers.** The plan had
her own answers due by Sun 22; what arrived on Sat 21 was "Start with a draft
and I'll make edits". So this session wrote five, and she worked them:

- She rewrote the contingency rebuttal in her own words — **"Contingency plan
  is a line item."** `check()` asserts that string, because it is hers.
- She rejected the original line 1 ("Always have a plan B." / Not if nobody's
  priced it) — it was also the weakest, because it said the same thing as the
  contingency line.
- She picked its replacement from five options: **"A good planner is
  invisible." / Invisible is how a room ends up with nobody in charge.**

Every line here is one she kept, chose or wrote. Nothing goes out she has not
seen.

Four of the five rebuttals are positions this account has already taken — the
captain (Wed 18), "last year is data, not a template" (Sun 15), and the
contingency line (content bank 20) — which is what keeps a list of opinions
from reading as a listicle.

## Holding everything but the title constant

The test measures the hook. Solved freely, B's three-line title squeezed its
boxes to 34px against A's 36 — small, but not "identical except the title".
So **B is solved first and A is rebuilt at B's box size**, and `main()`
asserts the two match. Both end up at title 80px and boxes 34px.

What still differs, unavoidably, is where the block sits: B's title is three
lines, so its boxes start lower. The text, the sizes and the bed are the same.

## The look

The planner list Reel format: deep purple #3C3489 ground, lavender #CECBF6
boxes, Poppins, title in SemiBold white. Inside each box the advice sits in
quotes in Regular at 88% size and a lighter purple, with the rebuttal under it
in SemiBold — **the turn is the joke, so it gets its own line.**

Safe zones are the layout, not a check afterwards: the block is centred inside
250–1440 rather than in the frame, so the last box clears the bottom 25% where
TikTok's caption and buttons sit. A ends at 1379, B at 1425.

**No BUDGET line and no CTA at all.** A trial exists to measure one thing, and
an ask would be a second variable.

## The cuts

**9.00s each**, 1080x1920, 30fps, CRF 19, AAC 192k at 48 kHz, `+faststart`,
**-14.0 LUFS** both.

**Both share one bed, deliberately.** Her Nov 10 rule — no two posts on the
same day share a track — was written after two of Wednesday's Reels went out
on one and she heard it immediately. This is the case that rule is not about:
A and B are the same piece twice. A second bed would be a second variable.
Tuesday's 6:30pm Thanksgiving Reel carries an Eryn voiceover and no bed, so
nothing else that day sounds like this.

Muted electric guitar stabs and a tight tambourine over a punchy electric
bass, its own generation, nothing shared with Monday's list Reel.
Instrumental by spectrogram — even dense texture end to end, regular
transients, nothing sweeping — and by Scribe returning an empty string.
Energy -14.2 to -15.1 dB across all 25 seconds with no ring-out, so the cut
starts at 0.0; **+0.3 dB** into the limiter.

## What happens after

- **Tue 24 morning:** she uploads both as Trial Reels. Not as regular Reels.
- **Fri 27:** compare views and non-follower reach at 72 hours; she shares the
  winner to everyone, Facebook gets it then.
- The winning hook style goes into the next week's day blocks, and the weekly
  recap logs both versions.

## What actually went up

**TikTok, Tue 24 Nov at 9:05am Eastern** — one version, as an ordinary video
(`7710652569181375775`, 285 views by Wed 25). The guide only ever asked for
the pair on Instagram, so this is the day's TikTok rather than half the test.

**Instagram, Wed 25 Nov — both, as trials, two minutes apart:**

| | Live | Media | Posted |
| --- | --- | --- | --- |
| **A** | `reel/DgKv2XuRg-X/` | `18093133250372083` | 9:30am Eastern |
| **B** | `reel/DgKwEyuRBGY/` | `18088237253707790` | 9:32am Eastern |

Both read `is_shared_to_feed: false`, which is what a live trial looks like.
A went up alone first; B was not there three minutes later, and she said so
herself — "oh i need to post both as trials" — so both files went over again
and B followed.

**Which is which cannot be read off the captions, because the captions are
identical by design** — the test varies the title on screen and nothing else.
So they were told apart by measuring the title block, in the one way that
needs no guessing: count the bands of white text rows in the top third of the
frame.

| | Title bands | Spans |
| --- | --- | --- |
| local A render | 2 | (372,464) (475,544) |
| live 9:30am | 2 | (373,464) (476,544) |
| local B render | 3 | (321,413) (423,516) (526,595) |
| live 9:32am | 3 | (322,412) (424,516) (527,595) |

Within a pixel on every span, so the mapping is settled rather than inferred
from the order she happened to upload them in. **A's title wraps to two lines,
not one** — worth writing down, since the two-against-three count is now the
fingerprint that identifies them.

`scontent-*.cdninstagram.com` is blocked from this session, so the two
thumbnails were fetched and measured in Composio's remote sandbox, the same
route the Oct 31 carousel used to check slide order. A blocked host is not the
end of a check.

**The Tue 24 YOU line was struck and then un-struck**, which is worth
recording rather than hiding. It was struck on her "posted as as trial", and
the media edge showed one of the two. Her own rule decides it: only strike
what happened as written, and half of a two-piece test is not the task. The
repair was one batch — `deleteContentRange` over the 69-unit marker, then
`updateTextStyle` with `strikethrough: false` back over the paragraph — and
re-reading confirms the line is its original text again with nothing spilled
either side.

The lesson is narrower than "verify before striking", which was already the
rule. It is that **"posted" in the singular is not confirmation of a pair.**
A line asking for two things needs the count checked, not the verb.

## The 72-hour point moved to Sat 28

A went up Wed 25, not Tue 24, so the comparison the guide puts on Fri 27 is a
day early. `trig_01S1hqeSm7EmMGU8xxQe6muN` fires Sat 28 at 9:10am Eastern to
do it, and it is written to refuse the comparison outright if only one of the
two is up — a trial reaches only non-followers, so A cannot be compared
against anything else in the feed, and one piece is not a test.

**Non-follower reach decides it, not views.** Views would reward whichever one
Instagram happened to push. And at this account's volume two pieces is a weak
signal either way: if they land within a few percent the honest answer is that
they tied.
