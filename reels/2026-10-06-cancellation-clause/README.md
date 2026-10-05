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

## Four versions, and what changed

| | |
| --- | --- |
| v1 | Four freeze frames, silent, prompt card first, highlights at source size |
| v2 | Highlighted passages lifted out as strips over a blurred frame |
| v3 | Voiceover added, opens on the takeaway, no prompt card |
| **v4** | **Her story order, genuinely zoomed, no dimmed background** |

v4 is built to the five-beat brief she wrote: the prompt, what the contract
says, the catch, the maths, the takeaway. 17.40s.

| Beat | Source | On screen |
| --- | --- | --- |
| 0.00-4.00 | 0.0 | the question, zoomed 1.26x, under "I asked AI what cancelling 60 days out would cost." |
| 4.00-7.00 | 13.0 | the table, 89-60 day row marked |
| 7.00-11.00 | **12.0** | the deposit sits on top of the fee |
| 11.00-15.00 | **14.4** | $21,250 + $63,750 = $85,000 |
| 15.00-17.40 | **26.0** | 75% becomes an effective 100%, under "The table says 75%. The contract charges 100%." |

## How the zoom finally got solved

v2 and v3 put the highlighted lines on a panel over a blurred frame, and she
rejected that: "not a small box on a dimmed background". The fix is not a
different crop, it is **a different frame**.

The answer text is full-width in the capture, so it cannot be magnified — but
where it sits on screen changes as the page scrolls. So each beat now uses the
timestamp at which its own sentence happens to be mid-screen, and the frame is
shown whole:

- the catch is at the very top of frame at t=13 and at **43-54%** at t=12
- the maths is below the fold at t=14 and at **53-60%** at t=14.4
- the table row is at **48-51%** at t=13
- the takeaway is at **42-53%** at t=26

Every highlight lands between 42% and 60% of the frame height. The build asserts
it and fails rather than shipping a frame outside the band.

**Beat 1 is the only real magnification, and only because the prompt bubble is
narrower than the answer text** — 855px against the frame's 1206. Blown up to
1080 that is 1.26x, and the question genuinely fills the screen.

### The one rule that could not be kept

The Oct 5 safe zones ask for nothing important in the right 15%. **The answer
text runs to within 56px of the capture's right edge**, so filling the frame
with it — which is what she asked for — necessarily pushes the ends of those
lines into that band. The two requirements are geometrically incompatible on
this source.

Filling the frame won, because that was the explicit instruction and the dimmed
panel was the thing being rejected. Top 12% and bottom 25% are both honoured and
asserted. The only way to satisfy all three at once is to re-typeset the lines
as our own text instead of showing the screenshot.

## The ad, handled by cropping rather than by timing

v3 avoided the Visit Denver ad by taking the takeaway at 25.5 instead of 26.0.
v4 needs 26.0, because that is where the sentence is mid-screen — so the window
is cut at source y 1900 instead and the rest of the canvas is filled with the
page's own background colour. The ad starts at 1913 and simply is not in the
file. The fill sits in the bottom 25%, which is TikTok's own dead zone.

## Overlays and audio

One highlight colour throughout, amber, translucent. Two dark cards, neither in
the highlight colour: the opening line and the closing takeaway. No end card.

Voiceover is her 42-word script in the series voice, 15.65s against a 17.40s
cut, so the takeaway holds for about two seconds after the last word rather than
cutting on it. **-14.0 LUFS**, true peak -1.0 dBFS, reached the explicit way —
`loudnorm`'s two-pass stalls short on this voice because the true-peak ceiling
binds first, so the gain is applied directly with `alimiter` at `level=0`.

## Caption

`build/caption-tiktok.txt`, her wording, unchanged across v2 and v3. **One
change from what she sent**: her text ended `#eventplanningtips #` with a bare
hash and no fourth tag, so it is completed to `#eventplanner`, the fourth tag
the guide uses on every quick piece. Flagged to her rather than silently fixed.

The prompt stays in the caption, which matters more in v3 than it did before —
it is now the only place the prompt appears.
