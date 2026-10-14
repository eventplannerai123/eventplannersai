# 2026-10-14 — AV schedule check

The Wed 14 Oct piece, and **both cuts are hers to upload**: the Instagram one
is a planned Trial (in-app toggle only) and TikTok is always manual. Nothing
posts from here.

| | |
| --- | --- |
| TikTok | `av-schedule-tiktok.mp4` — 16.60s, −14.4 LUFS |
| Instagram (Trial) | `av-schedule-instagram.mp4` — 15.20s, −14.5 LUFS |

1080x1920 (0.5625 exactly), 30 fps, H.264 High, CRF 19, `+faststart`, AAC 192k
at 48 kHz. Both inside 15–20s.

## The piece

Her true story, content bank item 1: at her first job she sent the AV team to
lunch during the keynote, because the day two and day three crew schedules had
been swapped. This is AI finding exactly that fault in a demo pair of
schedules, so the claim is on screen rather than asserted.

**It caught the swap**, which is what the brief says to re-run for if missed —
along with the Day 1 camera call 15 minutes after the keynote starts, the four
microphones against two, and the unassigned breakout rooms.

## The wrong file came first

The link sent on Oct 14 was `1fiJQcgceGoIs8_mGPGq-g8FrP0EJ0_Ol`, which is the
**Oct 12 contingency budget recording** already used for the carousel — same
file id, and `md5` identical byte for byte. Flagged rather than built on; she
sent the right one straight after. Worth checking the id against what is
already in the repo when a link looks familiar.

## Beats

Freeze frames, 0.20s dissolves. Clean band 1161x2064 at x=22, y=300.

| | Source | What it shows |
| --- | --- | --- |
| 1 | t=1.20 | the prompt, whole, hook card above it |
| 2 | t=13.00 | **"the Day 2 and Day 3 crew schedules appear to be swapped"**, highlighted |
| 3 | t=26.50 | the day-swap diagnosis, **both directions** highlighted |
| 4 | t=31.90 | the bottom line, dimmed, takeaway over it |

**Beat 3 was rebuilt.** The first attempt put its two highlights at y 408–500
and 738–832, read off a ruler overlay in a hurry; the headings are actually
700px apart, so both boxes landed on body text instead. Caught by checking the
exported frames rather than the card generator's own numbers — which is exactly
why that check exists. Moving the beat from t=26.0 to **t=26.5** brings both
headings inside the Oct 5 safe band (300–440 and 995–1135) and the symmetry —
Day 2 → Day 3 above, Day 3 → Day 2 below — now reads in a single frame.

## Opening on the prompt

This day's block says "open on the finished list of mismatches, not the prompt
being sent". That wording predates the guide's **Oct 5 rule 2** — "never cut
the prompt; a video without the original prompt makes no sense" — so the cut
opens on the prompt, the same call made on the Oct 12 piece.

It costs nothing here. **The recording starts after the send tap**, which is
usually a problem, but frame one carries the *whole* prompt in the sent bubble,
which is the better frame to open on anyway. No opening had to be faked.

The hook card sits at y 261–439, in the gap above the bubble (which runs
470–1455), so it covers the PDF attachment chip and **not a word of the
prompt**.

## Overlays

| | Position | Width |
| --- | --- | --- |
| hook (both cuts) | y 261–439 | — |
| "biggest issue … swapped" | y 815–1045 | 95% |
| Day 2 → Day 3 | y 300–440 | 67% |
| Day 3 → Day 2 | y 995–1135 | 67% |
| takeaway card | y 689–1011 | — |

Hooks:

- **Instagram** — "I sent the AV crew to lunch during the keynote." (the
  guide's wording verbatim)
- **TikTok** — "Stop assuming the AV schedule matches the run of show."

All asserted inside the Oct 5 safe band by `build/make_cards.py`, then checked
on the exported frames of both cuts.

## No ad

**No in-app advertiser anywhere in the 32s** — the bottom strip was scanned at
2s intervals across the whole source, and then the bottom 340px of both
finished exports was scanned through to the final frame. Second clean recording
in a row, after a run of nine advertisers.

## Voiceovers

ElevenLabs, Vanessa - Beach Girl (`8DzKSPdgEQPaK5vKG0Rs`),
`eleven_multilingual_v2`.

- **Instagram** — the guide's script verbatim, 41 words, 14.63s.
- **TikTok** — same script with the opening line swapped for the command-style
  hook, 44 words, 16.12s.

Loudness: measured first pass, explicit gain, `alimiter` with `level=0` at a
−1.0 dB ceiling, `TRIM = 1.10`. Confirmed on both finished files.

## Captions

- `build/caption-tiktok.txt` — the ordinary layout, four hashtags.
- `build/caption-instagram-trial.txt` — identical body, **no hashtags**, because
  a trial is kept off hashtag pages.

Both have "Prompt below." stripped, per the Oct 12 retirement; the guide's own
block still carries it.
