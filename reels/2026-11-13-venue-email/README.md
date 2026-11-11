# Fri 13 Nov — this email got $10,000 off the venue quote

Redo of the Sep 4 Reel, which reached 18; the original stays up. Instagram +
Facebook at 6:30pm Eastern Friday; TikTok at about 9am, by her hand, from the
file sent the evening before.

| | |
| --- | --- |
| Cuts | `venue-email-instagram.mp4`, `venue-email-tiktok.mp4` |
| Length | 17.52s both, inside the brief's 15–20s |
| Export | 1080x1920, ratio 0.5625, 30fps, H.264 high, CRF 19, +faststart |
| Audio | Eryn (`kdnRe2koJdOK4Ovxn2DI`, `eleven_v4`), **-14.0 LUFS, -1.3 dBTP** |
| Source | her 1206x2622 iPhone capture, 24.4s, 60fps, no rotation side data |
| Crop | `crop=1206:2144:0:478` then `scale=1080:1920` |

## The shortest recording yet, and it changes where the prompt comes from

24.4s, against 69s on Tue 10 and 108s on Thu 12. Two things follow.

**The whole prompt is in the input box, not the sent bubble** — the opposite
of the usual case. By the time the bubble is on screen the view has scrolled
and only its last three lines show, so the cut opens on **t=0.50s**, the input
box with the PDF chip attached, which is the one frame carrying the prompt
entire. The Sep 29 note says the sent bubble is "usually the better frame";
this is the exception it allows for.

**1.0–2.5s is a loading spinner.** The send happens off the top of the clip.
`LOADING_WINDOW` bars any beat landing in it.

## The answer did what the brief predicted, and one thing more

It found the small-print line, offered a Tuesday or Wednesday in October 2027
and a two-year commitment, and asked for the rate on each. Then it added a
**negotiation tip the brief never asked for**: don't name a target price, let
them come back with their best weekday and multi-year numbers first. That is
the last beat.

**$35,000 is not in the recording and is not in the cut.** The guide is
explicit that the figure in the hook is the outcome she got in real life on a
similar email, shown as the payoff rather than as AI output. The answer writes
the email; it does not negotiate it. So the hook card carries the $10,000, no
beat claims the venue replied, and the caption says the $35,000 was hers.

## The twist is the brief's predicted one

> It offers a two-year commitment without asking for a rate lock or a
> cancellation clause in return.

Checked against the email it actually wrote: it asks for "your best available
rates" for a weekday and for a two-year commitment, and nothing in it asks the
venue to hold the rate for the second year. So the prediction holds, and it is
the last line of the voiceover.

**Not yet confirmed by her.** She sent the recording without the "one thing
you'd still change", so this is the brief's prediction plus what the email
says, and it goes to her with the cut. The caption's "last time I sent one like
it" line is hers to correct too.

## Beats

| Beat | t | What it shows |
| --- | --- | --- |
| b0-prompt | 0.50s | the whole prompt in the input box, the quote attached |
| b1-quote | 7.50s | $45,000.00, the Saturday rate |
| b2-smallprint | 6.00s | rate notes: weekday rates available on request |
| b3-email | 19.00s | the email, both asks as bullets |
| b4-tip | 22.50s | "I would avoid naming a target price initially" |

**b2 sits a second and a half earlier in the recording than b1**, because the
beats follow the voiceover rather than the scroll and the $45,000 total is what
the voiceover opens on.

**The small-print line is legible in exactly one frame.** At t=6.00s page two
sits high enough to clear the PDF toolbar; a second later the scroll has taken
"Sunday-Thursday rates and multi-year agreements are available on request"
under the toolbar, where it cannot be read at all. Everything in this piece
hangs off that one sentence, so the timestamp is not adjustable.

Beats are selected by frame number (`eq(n,N)`), never a time window: at 60fps
`between(t,T,T+0.02)` spans one or two frames, and on Nov 10 six such windows
matched eleven frames and every beat after the second was silently wrong.

## One highlight, and it is baked into the frame

The first in this series. The small-print line is 8pt grey in the source —
legible at 1080x1920 and marginal on a phone — and it is the sentence the piece
turns on, so it earns the amber box where the headline numbers on Tue 10 and
Thu 12 did not.

It is **baked into the beat PNG rather than overlaid**, because every beat
carries a 4% push: an overlay added after the concat would stay still while the
line drifted out from under it.

Placed with `tools/cardkit.fit_highlight` from a seed y, not typed — her Oct 14
instruction. It snapped to y 923–956, x 118–613, 46% of the width, which is the
real extent of that line's ink.

## Cards

Hook at 0:00–2:30, end card in the last 3s, nothing between.

**No BUDGET line on this one.** The Nov 3 soft mention covers Thu 5, Mon 9,
Tue 10 and Tue 17 only, and Tue 10 came off it on Nov 9, so this Reel ends on
the guide's own takeaway overlay: "Read the small print, then ask for the
weekday rate." The same line on both cuts — nothing here turns on a bio link.

**The hook sits low and the end card high**, the Tue 10 shape, and both are
forced by their beats. The hook goes at y=1120, on the keyboard, because the
prompt runs y 380–790 and the prompt is the thing that opening exists to show.
The end card goes at y=250 over the tail of the email, because b4's whole job
is the negotiation tip from y=1030 down; the 4% push lifts it to about 953 by
the last frame, so the card's floor is 900 rather than 1000.

Both cards are opaque, as on Tue 10 and Thu 12, because the end card lands on a
dense paragraph.

## Checks

- **Ad check clean.** The source is 24.4s, so all 24 of its 1fps frames were
  read whole rather than as a bottom strip — a stronger check. Then the
  exported mp4's bottom 340px at 1fps through to its final frame. No ad in
  either, which is worth stating rather than assuming: nine advertisers have
  turned up in these recordings so far and the last three arrived late in the
  clip.
- Hook verified present on the **exported** frames at 1.0s and 2.0s and gone by
  2.6s, on both cuts; end card present at 15.5s and on the last frame, absent
  at 12.0s.
- All five beat frames were looked at whole, and the highlighted line was read
  at 1:1 before and after the box went on.
- Loudness measured on the finished exports, not on the voiceover.
- **The gain was swept, not computed.** Eryn came out at -23.9 LUFS with peaks
  at -2.6 dBTP, and the arithmetic +10.2 dB would have undershot; the sweep ran
  +12.0 to +13.5 and **+12.7 dB** through `alimiter=limit=0.841:level=0`
  measured -14.0.
- 53 words in 17.52s is 3.02 w/s, in line with the 3.1 planning figure for Eryn.
