# Fri 20 Nov, 6:30pm — the coloring book giveaway opens

Two cuts from her own footage, filmed Thu 19 after she asked for the shot list
the morning before.

## The footage

`IMG_0424.MOV`, 33.7s, shot landscape-flagged at 1920x1080 with
`rotation=-90`, so it decodes as 1080x1920 and needs no crop — the Oct 7 rule
about checking `stream_side_data=rotation` before planning any crop.

It opens exactly on the payoff: both paperbacks in frame from the first frame,
with a slow push across the covers, then the flip-through. **Her raw clip is
not in this repo** — the repo is public. It lives in Drive `November 20`
(`13KeZV3qJI5EPl1QdT5ZMXQuNOgyAATmW`) and `render.py` reads a scratch copy.

## The cut

| | |
| --- | --- |
| books | source 0.00–4.60 at 1.0x |
| flip-through | source 5.00–18.10 at 1.5x |
| end card | 2.56s (Instagram) / 2.24s (TikTok) |
| total | **15.89s** / **15.57s** |

The flip is not compressed harder than 1.5x: above that the drawings stop
reading as drawings, and the pages are the piece.

## Overlays

A lavender band high in the frame for the first 2 seconds — "2 free copies.
Here's how to win one." — clear of the books and of the top 12%. Then the
takeaway card: **"Comment the bride you'd give it to."** on Instagram,
**"Enter on my Instagram."** on TikTok, because TikTok has no bio link.

No BUDGET line. Her Nov 14 rule is to check the closing line against the
piece, and this one is the giveaway, not the tracker; `make_cards.py` asserts
the word never appears.

## Audio

Eryn, the guide's 40-word script, 13.04s, +11.5 dB into
`alimiter=limit=0.841:level=0` for **-14.0 LUFS**. No music under it, as with
every voiceover piece.

**The closing line is spoken as well as shown**, so the end card is not three
silent seconds: each cut hears its own card read out, which is also the Nov 19
lesson from step 3 of the four-steps Reel — the audio has to match what is on
screen. Exports measure **-13.82 LUFS**.

## Posting

- **Instagram and Facebook at 6:30pm Friday**, after she approves.
- **TikTok at about 9am**, hers, with its own caption and end card.
- Her Story the same evening: the timelapse or a photo of the book, the text
  "Giveaway open until Fri 27," and the post shared in.

## Posted

- **Instagram**, Fri 20 Nov 6:31pm Eastern, from `trig_01JbxYMsYw3eANaYW958muK9`:
  [instagram.com/reel/Df-11HBlH_X](https://www.instagram.com/reel/Df-11HBlH_X/),
  media `17970851820208246`, read back as `media_product_type: REELS`. The
  container reached FINISHED after 19.2s over seven status checks and
  published first time.
- **Facebook** `4030670113894758`, same caption.
- **The full rules went out word for word.** The live caption was diffed
  against `build/caption-instagram.txt` character for character and is
  identical — the dates, the 11:59pm Eastern close, the random draw, the
  Nov 28 announcement, "contacted by DM from @aiforeventplanners only", the
  no-password-or-payment line, "No purchase necessary", "US residents 18+",
  "Entries count on Instagram only", and the not-sponsored-by-Instagram line.

## If it closes with fewer than two entries — settled over three messages

She answered this **twice**, on Nov 23 in the guide and again on Nov 25 in
conversation, and the two did not agree. Both are recorded because the
difference is what the Mon 30 piece gets built from.

**Nov 23, in her own words on the guide's Fri 27 line:** any outside entrant
still wins a copy; any book with no winner rolls into the **Mon 30 hat
giveaway**; if both roll over, that giveaway's prize becomes the hat plus a
coloring book for the winner and a coloring book for a second winner, with
Monday's overlay, voiceover and caption rules rewritten for two winners.

**That line was never struck**, so the daily audit read it as open and put the
question to her a second time. The audit was reading `strikethrough` and not
the line's text, which carried her answer in plain sight. Written up as a
standing rule in `CLAUDE.md`.

**Nov 25, first answer:** "then we save the books for a later giveaway in a
month or two" — which would have emptied Monday's giveaway back to hat-only.

**Nov 25, after the conflict was put to her: "hat plus a book."** So Monday's
prize is **the hat plus one coloring book**, and the reading carried into the
build is **one winner**, with the second book held for a giveaway in a month
or two. That is what reconciles both of today's messages: one book now, one
saved. **She confirmed it in the next breath — "and then only 1 book" — so
one winner is hers, not an inference.** A giveaway's published rules have to
state a winner count and cannot be left vague, which is why it was put to her
as a reading rather than built on a guess.

No substitute draw on this giveaway, no copy to whoever happened to enter, and
no extension of the Fri 27 deadline.

The state when she decided: **zero comments on the Reel**, five days in and
two days from closing, checked with `INSTAGRAM_GET_IG_MEDIA_COMMENTS` on
media `17970851820208246`. The Sun 22 recap had already found none; this is
the same number four days later, so the Fri 27 fallback line stopped being a
contingency and became the likely path.

What it changes about Sat 28:

- The 9am draw has nothing to draw from unless entries arrive in the last two
  days, so the job becomes writing her the Story wording instead, for a
  giveaway that closed empty rather than two winners to announce.
- Her line about DMing winners for addresses and shipping media mail is moot
  in that case; the unpin-and-re-pin line is not, and still runs.

It is recorded on the guide's own Fri 27 fallback line rather than in a new
paragraph, because that is where the question was asked and where anyone
reading it later will look.

**Nothing about Thu 26 or Fri 27 changes.** Both pieces say the giveaway is
open and closing Friday, which is true either way; a giveaway that ends with
too few entries is still a giveaway that ran.

## And if it closes empty: nothing is posted (her decision, Fri 27 Nov)

**"we wont post anything if no one entered."** Fri 27 morning the Reel still
had zero comments (`INSTAGRAM_GET_IG_MEDIA_COMMENTS`, media
`17970851820208246`), so that is the likely path.

So if nobody has entered when it closes at 11:59pm Fri 27: **no winners Story,
no "closed empty" Story, no Story wording** — nothing goes out about it at all.
That replaces what was said to her on Thu 26 ("I'll send you the Story wording
for a giveaway that closed empty"), which assumed an announcement she does not
want. The Sat 28 9am draw has nothing to draw from, so it becomes a one-line
check for late entries and nothing more.

What still stands from before: both books are held for a later giveaway in a
month or two, and the Mon 30 hat giveaway is hat plus one book, one winner.

The unpin of the giveaway Reel and re-pin of "You're allowed to be tired" is a
separate tidy-up she did not mention, so it is left on her Sat 28 line as it
was.
