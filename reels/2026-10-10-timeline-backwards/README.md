# 2026-10-10 — Timeline backwards from doors

The Sat 10 Oct TikTok quick piece. **TikTok only** — she uploads it. There is
no Instagram post on Sat 10.

| | |
| --- | --- |
| Cut | `timeline-backwards-tiktok.mp4` — 15.40s, −14.1 LUFS, TP −1.0 |
| Caption | `build/caption-tiktok.txt`, the guide's wording verbatim |

1080x1920 (0.5625 exactly), 30 fps, H.264 High, CRF 19, `+faststart`, AAC 192k
at 48 kHz. Inside the format's 15–20s.

## The format: open on the prompt, not the takeaway

Worth stating plainly because the repo had it backwards. The guide's Oct 5 rule
2 reads:

> Tell it in order: the prompt first as the setup (what Sahiba asked, zoomed on
> the question), then the key lines of the answer, then the biggest takeaway as
> a big overlay at the end. **Never cut the prompt: a video without the original
> prompt makes no sense (Sahiba, Oct 5).**

`CLAUDE.md` had recorded that rule as "open on the biggest takeaway, not on the
prompt — the prompt goes in the caption", which is its opposite, and had been
wrong since Oct 5. Corrected there as well as here. No piece was mis-built on
it: the Oct 6 cancellation rebuild opened on the prompt because her own brief
said so, and the Oct 7 piece had no prompt to show.

## Beats

Freeze frames, 0.20s dissolves, 4.0s each.

| | Source | What it shows |
| --- | --- | --- |
| 1 | t=6.00 | the prompt, with the ask highlighted and a card stating the setup |
| 2 | t=11.55 | 1:00 PM — Rentals, linens and chairs, "First in" |
| 3 | t=27.60 | the key rule on the guest entrance |
| 4 | t=15.00 | the takeaway, over the 2:30 bar-team row, dimmed |

**The source times are the composition.** Each beat's key line had to sit in the
middle of the frame, and the crop can't do that — the crop is fixed at full
width. What moves the line up and down is where the answer has scrolled to, so
each time was found by sampling the recording and measuring, not guessed. That
is why they are oddly specific.

`-shortest` is deliberately **not** used: the voiceover is 14.77s and the beats
run 15.40s. Trimming to the audio would land the cut at 14.77s, just under the
format's 15s floor. The 0.6s tail holds the takeaway overlay, which is what the
format ends on anyway.

## Overlays

`build/make_cards.py` asserts every card and highlight inside the Oct 5 safe
band (below y=1440, above y=230) rather than trusting the numbers, and prints
what fraction of the width each highlight fills. All four were then checked on
the exported frames.

| | Position | Width |
| --- | --- | --- |
| setup card | y 238–473 | — |
| the ask | y 1135–1300 | 72% |
| 1:00 PM rentals | y 930–1105 | 86% |
| key rule | y 775–1000 | 94% |
| takeaway card | y 686–975 | — |

Beat 1 is the compromise. The prompt bubble fills the frame top to bottom, so
there is no empty space for a card. The card goes over the opening two lines and
carries exactly what they said — "Doors open at 7pm for a 200-person evening
event" becomes "Doors at 7pm. 200 guests. Six vendors." — and the operative
sentence, the actual ask, is highlighted instead. Nothing is lost.

## The scroll-to-bottom button is still in frame

At about y 1772–1892 of the output, deep inside the bottom 25% that TikTok's own
caption covers. She asked for it gone on Oct 6 and it is not gone here, because
both ways of removing it were tried and both were worse:

- **Blur it.** A boxblur patch over this answer's black-on-white text leaves a
  grey smudge that reads as a censor box — more conspicuous than the button.
- **Crop it out.** The button sits at source y 2205–2335, so the crop has to end
  above it, which forces the width down from 1161 to 1062. That clips the **K
  off "Key rule"** — the most important line in the piece — and shaves the
  margins on every other beat.

Leaving it costs nothing visible. Both alternatives cost legibility. Flagged to
her rather than quietly dropped.

## The ad

An **Asana** ad rides into the bottom of the answer from about t=26 of the
source — the eighth distinct advertiser. Every beat is cropped well above it,
and the finished export was scanned over its whole frame through to the last
frame, not a crop of the source.

## Voiceover

ElevenLabs, Vanessa - Beach Girl (`8DzKSPdgEQPaK5vKG0Rs`),
`eleven_multilingual_v2`. 39 words, inside the format's 30–40, written here from
the takeaway:

> Doors at seven means your first vendor is in at one. Rentals, then AV, then
> catering, then florals, in that order, because nobody can work around a room
> that isn't set yet. And no deliveries through the guest entrance.

Loudness: measured first pass, then explicit gain plus `alimiter` with
`level=0`, limiter at −1.0 dB because −1.5 binds before the gain lands on this
voice. `TRIM = 1.10` accounts for the export measuring about 1 dB below the
voiceover's own figure, since the cut carries its lead-in and tail. Confirmed on
the finished file at −14.1 LUFS.

## Crop arithmetic worth not repeating

The clean band is **1161x2064 at x=22, y=300**. The obvious choice —
1166x2074, the largest band that clears the status bar and the input bar — is
**0.5622, not 0.5625**, and fails the assertion in `render.py`. 2064 is a
multiple of 16, so 1161 = 9×2064/16 exactly.
