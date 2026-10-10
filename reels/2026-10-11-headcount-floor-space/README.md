# 2026-10-11 — Headcount to floor space

The Sun 11 Oct TikTok quick piece. **TikTok only** — she uploads it. There is
no Instagram post on Sun 11.

Built a day early: she sent the recording on Oct 10 with "if you wanna get a
head start".

| | |
| --- | --- |
| Cut | `headcount-floor-space-tiktok.mp4` — 15.10s, −13.8 LUFS, TP −1.0 |
| Caption | `build/caption-tiktok.txt`, the guide's wording verbatim |

1080x1920 (0.5625 exactly), 30 fps, H.264 High, CRF 19, `+faststart`, AAC 192k
at 48 kHz.

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
