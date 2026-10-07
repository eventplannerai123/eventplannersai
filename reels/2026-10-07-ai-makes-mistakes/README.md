# 2026-10-07 — AI makes mistakes, just like us

The Wed 7 Oct Instagram piece, and the format test: the build-story format
rather than a demo. No screen recording and no ChatGPT prompt — Sahiba's own
conference b-roll with her off camera. Content bank item 10.

| | |
| --- | --- |
| Instagram | `ai-makes-mistakes-instagram.mp4` — 15.46s, −14.2 LUFS, TP −1.0 |
| TikTok | `ai-makes-mistakes-tiktok.mp4` — 15.14s, −14.3 LUFS, TP −1.0 |

Both 1080x1920 (0.5625 exactly), 30 fps, H.264 High, CRF 19, `+faststart`,
AAC 192k at 48 kHz. Both inside the 15–20s target.

## The source is not in this repo

`build/render.py` reads from `source/`, which is **gitignored**. This repo is
public — `raw.githubusercontent.com` URLs are exactly how Meta and Pinterest
fetch from it — so her raw footage, which has attendees' faces, a named venue
and third-party branding in it, does not belong here. Only the finished cuts do.

A first attempt committed the six source files so they could be handed to Drive
by URL, and it was blocked as an out-of-place publication. That was correct, and
`.gitignore` now carries the rule so it cannot happen again by habit.

The six files she sent, kept out of git:

| File | What it is | In the cut? |
| --- | --- | --- |
| `photo-1-eggs.jpg` | half-eaten plate | yes |
| `photo-2-beverage.jpg` | beverage table, still | no — the clip is the same table |
| `photo-3-ballroom.jpg` | ballroom of rounds | yes |
| `photo-4-foyer.jpg` | foyer colonnade | yes |
| `clip-1-beverage.mov` | 5.17s, beverage table pan | yes |
| `clip-2-coffee.mov` | 8.90s, coffee station pan | **no** |

## The clips turned out to be vertical

`ffprobe` reports both .mov clips as **1920x1080**, which reads as landscape and
would have meant a 608-wide centre slice upscaled 1.78x into the frame — soft,
and the worst-looking thing in the cut. They are not landscape. Both carry
`rotation=-90` in their stream side data, so they **decode as 1080x1920**:
already exactly the output frame, no crop and no upscale.

**Check `stream_side_data=rotation` before planning a crop on a phone clip.**
`-show_entries stream=width,height` alone is misleading, and the first plan here
was built on it.

The stills are 1932x2576 (0.75). Cropping to **1449x2576** is exactly 0.5625 and
still downscales into 1080 wide, so the stills are the sharpest thing in the cut
rather than the softest.

## No faces, no logos — what that cost

Her brief for this footage said no faces and no logos. Two beats had to give:

- **`clip-2-coffee.mov` is in neither cut.** It pans onto a sponsor's pull-up
  banner and table skirt with the logo large and legible, and past two people at
  a registration desk. Nothing salvageable: the branding is in frame from the
  first second.
- **The foyer still needed its crop pushed.** Even at the rightmost 0.5625 crop
  (`x=483`) the frame still caught an exhibitor's banner on the left. The fix is
  the `x-bias` argument in `build/render.py`: opening at zoom 1.15 with the zoom
  window pinned 88% right drops that edge out of frame. At 1.21 the window is
  still 2395px of a 2898px intermediate, so it is a downscale, not an
  enlargement.

The ballroom shot keeps attendees in it, at a distance — roughly 40px tall in
the output frame, with faces around 8px. Not identifiable, and the shot is the
one the voiceover is actually about.

## Beats

TikTok was built first, per the standing rule.

| | Instagram | TikTok |
| --- | --- | --- |
| 1 | foyer colonnade, push in | ballroom rounds, pull back |
| 2 | beverage table, clip | half-eaten plate, push in |
| 3 | half-eaten plate, push in | beverage table, clip |
| 4 | ballroom rounds, push in (6.1s hold) | foyer colonnade, pull back (5.6s hold) |

Genuinely different order and pacing, not one cut reversed by accident: the
Instagram cut lands its longest hold on the **ballroom rounds**, which is the
shot the voiceover is about, while TikTok opens on it and ends wide.

0.20s dissolves throughout. `-shortest` trims each cut to its voiceover, which
is why the finished durations sit just under the 15.40 / 15.70 the beats add up
to — deliberate, and it leaves no silent tail.

## Overlays

One hook each, 0:00–0:03, no end card.

- Instagram: "AI doesn't know which two execs can't sit together." — y 961–1319
- TikTok: "Stop letting AI do your VIP seating." — y 1092–1368

`build/make_cards.py` asserts both inside the Oct 5 safe band (below y=1440,
above y=230) rather than trusting the numbers. Both were then **checked on the
exported frames**, not from the filtergraph.

## Voiceovers

ElevenLabs, Vanessa - Beach Girl (`8DzKSPdgEQPaK5vKG0Rs`),
`eleven_multilingual_v2`, generated on 2026-10-07 before the footage arrived —
neither script depends on it.

The Instagram script is the guide's verbatim; TikTok changes only its opening
line, to the command-style hook the standing rules require:

- Instagram: "AI will never get VIP seating right on its own."
- TikTok: "Stop letting AI do your VIP seating."

Loudness: measured first pass, then explicit gain plus `alimiter` with
`level=0`. Two corrections came out of measuring the **export** rather than the
voiceover:

- The export read about 1 dB below the first-pass figure, because the cut
  carries the voiceover's own lead-in and tail. `TRIM = 1.10` in `render.py` is
  that measured difference.
- At `limit=-1.5dB` the ceiling bound before the gain landed, so the limiter
  sits at **−1.0 dB**. Measured peaks are −1.0, so there is still headroom.

## Caption

`build/caption.txt`, the guide's wording verbatim, for Instagram, Facebook and
TikTok alike. **No `AI Prompt:` line** — the guide says outright this piece is
not a demo, so the usual caption layout's prompt block does not apply.
