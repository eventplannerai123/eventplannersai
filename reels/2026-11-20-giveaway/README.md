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
