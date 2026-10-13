# 2026-10-11 — Headcount to floor space

The Sun 11 Oct TikTok quick piece. **TikTok only** — she uploads it. There is
no Instagram post on Sun 11.

## Posted to Instagram and Facebook on Tue 13 Oct

| | |
| --- | --- |
| Instagram | [reel/Deb7C2CDBdO](https://www.instagram.com/reel/Deb7C2CDBdO/) — media id `17991951482852906`, 13:32:20 UTC |
| Facebook | [reel/1076904781993706](https://www.facebook.com/reel/1076904781993706/) — post id `1233196746554445_122115634539449533`, 13:32:56 UTC |

**Both captions verified identical** to `build/caption-tiktok.txt` (md5
`e8fd5f4512e0309d73c4f708dc806dd6`) by `cmp`, not by eye — the guide's Sun 11
wording. Four literal `#` on one line, no `%23`, no "Hashtags:" label.

She approved this on 2026-10-12 ("approved") for the Tue 13 slot, and it ran
from a scheduled wake-up while she was at a conference. **Held back from Oct 12
deliberately:** that day's Instagram slot was already taken by the event-brief
Reel she posted herself, and a second feed post competes for the same reach.

**The pre-check earned its place.** Both platforms were read before anything was
published, because her own Instagram upload had cross-posted to the Facebook
Page in 12 seconds the day before via the in-app toggle. Neither carried this
piece, so both posts went ahead. Facebook has no duplicate protection and a live
post cannot be taken back, so this check now runs before every Facebook post.

Worth noting for next time: the Facebook **feed** had not surfaced the new reel
on the first read-back, exactly as `docs/POSTING.md` says to expect. The video
listing showed it immediately (15.1s, right caption), and the feed entry
appeared on the next read. That is processing lag, not a failure — do not
re-post.

## Beats

Freeze frames, 0.20s dissolves. Same clean band as Oct 10 — **1161x2064 at
x=22, y=300**, which is exactly 9/16; the roomier 1166x2074 is 0.5622 and fails
the assertion in `render.py`.

| | Source | What it shows |
| --- | --- | --- |
| 1 | t=3.00 | the prompt, ask highlighted, setup card over the answer below |
| 2 | t=15.60 | dinner seating, dance floor and two bars — the three figures the voiceover names |
| 3 | t=18.80 | RECOMMENDED TARGET 4,500–5,000 sq. ft. |
| 4 | t=21.20 | the takeaway, over the room-dimensions table |

As on Oct 10 the source **times** are the composition: each key line sits in the
middle of the frame only because the answer has scrolled to the right place, so
the times were found by sampling and measuring.

**Beat 1 is better than Oct 10's.** There the prompt bubble filled the frame
top to bottom, so the setup card had to cover two lines of it. Here the answer
has already begun below the bubble, so the card sits over the answer's opening
lines — which this beat is not about — and the prompt is left completely
uncovered.

## Overlays

| | Position | Width |
| --- | --- | --- |
| the ask | y 695–1060 | 72% |
| setup card | y 1185–1415 | — |
| dinner / dance floor / bars | y 800–1105 | 98% |
| recommended target | y 640–900 | 95% |
| takeaway card | y 1026–1274 | — |

All asserted inside the Oct 5 safe band by `build/make_cards.py`, then checked
on the exported frames.

## The ad

A **Chivari** ad rides into the bottom of the answer from about t=23 of the
source — the ninth distinct advertiser in three weeks, after Adobe Acrobat,
Adobe Firefly, Rillion, Cambridge, Turning Stone, Fever and Asana. No beat is
taken from the last two seconds, and the export was scanned over its whole
frame anyway.

The run rate is now roughly one new advertiser per recording. Treat an ad as
certain rather than possible, and check the tail of every source before
choosing the final beat.

## Voiceover

ElevenLabs, Vanessa - Beach Girl (`8DzKSPdgEQPaK5vKG0Rs`),
`eleven_multilingual_v2`. 39 words, inside the format's 30–40:

> A hundred and eighty guests needs about four and a half thousand square feet.
> Eighteen hundred of that is dinner seating, seven hundred the dance floor,
> four hundred the two bars. Ask venues for a sixty by eighty room.

13.84s against 15.10s of beats, so the takeaway overlay holds for the last 1.3s.
`-shortest` is deliberately not used — trimming to the audio would drop the cut
under the format's 15s floor.

Loudness: measured first pass, explicit gain, `alimiter` with `level=0` at a
−1.0 dB ceiling. Confirmed on the finished file at −13.8 LUFS.

## Scroll button

Left in frame, per her 2026-10-10 instruction ("you dont need to blur it"). It
sits in the bottom 25% that TikTok's caption covers.
