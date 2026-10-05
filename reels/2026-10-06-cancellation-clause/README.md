# Cancellation clause — TikTok quick piece, 2026-10-06

Status: **built, handed over.** TikTok only, and TikTok is always her upload.
Nothing goes to Instagram or Facebook: Tue 6 has no Instagram piece.

The second of the October plan's five TikTok-only quick pieces — and **no longer
a quick piece in form**. v3 adds a voiceover at her request, which takes it out
of the silent, prompt-card-first format the guide sets for these and into
something closer to a short Reel built from stills.

| | |
| --- | --- |
| `cancellation-tiktok.mp4` | 1080x1920, ratio exactly 0.5625, 30 fps, H.264 high, CRF 19, `+faststart`, AAC 192k at 48 kHz |
| Duration | 16.39s |
| Voiceover | **-14.0 LUFS**, true peak -1.3 dBFS |

## Three versions, and what changed

| | |
| --- | --- |
| v1 | Four freeze frames, silent, prompt card first, highlights at source size |
| v2 | Highlighted passages lifted out as strips over a blurred frame |
| v3 | Her 39-word voiceover, opens on the takeaway, **no prompt card** |

v3 drops the opening prompt card entirely and opens on the cancellation table
with the 89-60 day row marked, under the biggest line in the piece. The prompt
moves to the caption, which is where the guide wants it anyway.

## Loudness

The two-pass `loudnorm` stalled at **-15.6 LUFS** with the true peak pinned at
-1.5 — the crest factor is high and the peak ceiling binds before the target
does. So the gain is applied explicitly, +9.7 dB, with `alimiter` at
`level=0` catching the peaks; without `level=0` it renormalises straight back to
full scale and the limiting looks broken. Measured on the finished export:
**-14.0 LUFS**, exactly on target.

The video runs 16.60s and the mux is `-shortest`, so the piece ends on the last
word at 16.39s rather than on a silent tail.

## She asked whether this was a rebuild. It is not

The Sep 20 vendor contract reel flagged a one-sided cancellation clause as one
of eight findings, and that piece went to TikTok on Oct 2 — four days before
this one. The overlap is real and was put to her rather than glossed over. The
difference is the scope: that piece reviewed a whole contract, this one takes a
single clause and answers one question, "what does 60 days actually cost".

## The clause is built, and so is the answer key

`source/clause.md` and `source/ANSWER-KEY.md`, written for the piece the way the
Sep 23 catering invoice was. Every mechanism in it occurs in real venue
contracts; what is artificial is having all of them in one article.
`source/paste-into-chatgpt.txt` is the single block she pasted — prompt and
clause together, at her request, because she was recording from a phone at a
conference.

## Four freeze frames, no scrolling

Her brief: no scrolling, freeze frames only. That suits the source, which only
ever moves by scrolling, and it is what keeps dense text readable at phone size.

| Beat | Source | On screen |
| --- | --- | --- |
| 0.00-3.00 | 13.0 | the cancellation table, 89-60 day row marked, under "This contract says 75%. It actually charges 100%." |
| 3.00-8.00 | 13.0 | the deposit sits **on top of** the fee |
| 8.00-12.00 | 15.0 | $21,250 + $63,750 = $85,000 |
| 12.00-end | **25.5** | 75% at 60 days becomes an effective 100% |

Hard cuts, not dissolves: the brief gives exact boundaries and a dissolve would
soften them.

The opening beat shows the whole table but marks only one row — the build takes
separate "what to show" and "what to highlight" boxes for exactly this.

## One crop for every beat

`crop=1125:2000:40:300`, then scaled to 1080x1920.

- 300 off the top clears the status bar — time and the red recording dot — and
  the nav row below it
- the window ends at 2300, which clears the "Ask ChatGPT" bar starting about
  2374
- 1125/2000 is exactly 0.5625, and **1125 is wide enough to hold the full text
  column** (x 47-1150), so no words are cut

## How the zoom works, and the limit on it (v2, after her note)

v1 showed the highlighted lines at source size inside the whole frame, and they
did not read as zoomed. v2 lifts each highlighted passage out as a **strip**,
sets it on a heavily blurred, dimmed copy of its own frame, and puts it in the
middle of the safe band.

The honest limit: **the lines cannot be made much larger than they already
were.** The answer text runs nearly the full width of the capture, so a crop
tight enough to magnify it clips words, and the strip can only be as wide as the
safe area allows — 880px, which is 81% of frame width against the 96% the same
lines occupied in v1. So the strip is fractionally *smaller* than before.

What makes it read as a zoom is the background, not the scale. At a light blur
the same sentence stayed legible behind the strip and the frame looked like two
copies of itself; at radius 16 and 46% brightness it becomes texture, and the
strip is the only thing in focus. If genuinely larger type is wanted, the
sentence has to be re-typeset as our own text rather than shown as a screenshot
— a different kind of piece, and her call.

Highlights are one colour throughout — amber, translucent, so the text reads
through — held four to five seconds each.

### Safe area

Her brief: nothing that matters in the top 12%, the bottom 25%, or the right
15%. The strips sit at x 30-910 against a 918 limit and are vertically centred
at 47.5% of the frame; the build **asserts** both rather than trusting the
arithmetic, and fails rather than shipping a frame that breaks them.

The prompt card is gone in v3, which also removes the one frame whose text sat
inside the top 12%.

## The last beat is taken at 25.5, not 26.0

The brief said freeze at 0:26. **The Visit Denver ad is already on screen at
26.0** — it sits around y 1965-2345 of the capture, and the target sentence runs
y 1961-2181, so no 9:16 crop can hold the sentence and exclude the ad.

At 25.5 the same sentence is on screen, in the same wording, with no ad anywhere
in frame. All four exported stills were checked whole-frame; the ad appears in
none of them. This is also why the piece is four stills rather than any moving
footage: there is no scroll to show that does not eventually reach it.

## Overlays

One highlight colour throughout — amber at 45% over the target lines, held four
to five seconds each, which is long enough to read twice.

The fourth beat adds the bold overlay the brief asked for, "60 days out: the
table says 75%. The contract charges 100%." It is a **solid dark card**, not the
highlight colour, so it reads as a separate element rather than a fourth
highlight. At 60px over three lines it is the biggest type on screen, and it
sits in the upper third, below the top 12% and clear of the strip. No hook line
before the prompt card and no end card, per the quick-piece format.

## The floating down-arrow

Blurred out rather than painted over, on every frame. It sits on top of body
text, so a filled patch would have erased words with it. On beats 2 to 4 the
background blur removes it anyway.

## Caption

`build/caption-tiktok.txt`, her wording, unchanged across v2 and v3. **One
change from what she sent**: her text ended `#eventplanningtips #` with a bare
hash and no fourth tag, so it is completed to `#eventplanner`, the fourth tag
the guide uses on every quick piece. Flagged to her rather than silently fixed.

The prompt stays in the caption, which matters more in v3 than it did before —
it is now the only place the prompt appears.
