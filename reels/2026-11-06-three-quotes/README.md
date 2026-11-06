# Fri 6 Nov 2026 — Three quotes, same AV job

**Instagram Reel, 6:30pm Eastern (23:30 UTC — Eastern is EST from Sun 1 Nov).**
Also to Facebook. **Both cuts approved Thu 5 Nov** ("both approved"), so the
Instagram post is a one-shot task firing into this session,
`trig_01VJLXCdnywm69BTVnavaCv3`, at 23:30 UTC Fri 6. It checks the live media
edge before it posts.

TikTok cut is hers to post and went over with its caption the moment she
approved, per her Oct 30 rule — not held to the slot.
`trig_01TC4A4CUA3MNoMfWYwjhzAw` is the Fri 6 evening TikTok reminder in the
week-1 timing test.

| | |
| --- | --- |
| Instagram cut | `three-quotes-instagram.mp4` — 21.033s, 1080x1920, 2,129,739 bytes |
| TikTok cut | `three-quotes-tiktok.mp4` — 21.033s, 1080x1920, 2,098,135 bytes |
| Audio | Eryn voiceover only, measured **-14.0 LUFS / -1.3 dBTP** on the Instagram export |
| Voice | Eryn `kdnRe2koJdOK4Ovxn2DI`, `eleven_v4`, default settings |

## Live

| | |
| --- | --- |
| Instagram | [reel/DfayyEPgmsK](https://www.instagram.com/reel/DfayyEPgmsK/) — media id `17952364014056073`, posted 2026-11-06 23:32 UTC (6:32pm Eastern) |
| Facebook | video `2287411988776422` |

Live caption diffed against `build/caption.txt` character for character:
identical. Media edge and Page feed both read before posting; neither held
the piece.

## Her recording

Drive `November 6` (`1CQ3AvEmakzfPRg8NzBBRD9PBt3aagHm1`), file id
`1zde-_QgaS5WUG81YmrsnwI5W8vcKVFlb` — 75,022,693 bytes, 1206x2622, 60fps,
40.94s. Downloaded to the session scratchpad and read from there via
`$QUOTES_SRC`: **it is not in this repo and must not be** (the repo is public).

Crop is the usual 1206-wide iPhone one, recomputed rather than pasted:
`crop=1206:2144:0:478` then `scale=1080:1920:flags=lanczos`.

**Ad check: clean.** Scanned the bottom strip of the source across the whole
40.94s and then the bottom ~300px of both exports through to the final frame.
Nothing from any of the nine known advertisers, and nothing new. The answer
ends on ChatGPT's own closing paragraph, with no sponsored line introducing
itself in the answer's voice the way Amazon Business did on Oct 30.

## The answer matches the brief

Headline prices $8,400 / $9,100 / $11,200; real totals once labor, delivery and
rigging are added:

| Vendor | Headline | Real total |
| --- | --- | --- |
| Meridian A | $8,400 | $11,950 |
| Northgate B | $9,100 | **$10,300 — actually cheapest** |
| Halcyon C | $11,200 | $11,200 |

So the cheapest-looking quote is the most expensive, which is the piece. The
$1,650 in the caption is Meridian's real total minus Northgate's.

## Build

Six freeze frames, no scrolling footage (`make_beats.py`):

| Beat | Source t | What it shows |
| --- | --- | --- |
| b0-prompt | 1.00s | the sent prompt bubble, whole |
| b1-cards | 5.20s | the three totals with Northgate's green "Cheapest" badge |
| b2-table | 12.00s | the side-by-side table |
| b3-hiding | 24.00s | where each vendor hides cost |
| b4-rec | 32.00s | the recommendation |
| b5-final | 40.50s | the closing paragraph — the twist |

**Time to payoff is 2.40s** on the Instagram cut and 2.20s on TikTok: beat 1
carries the real totals, so the reveal is inside the 6-second ceiling with room
to spare. A 4% slow push over each beat keeps the frame moving from frame one —
no static title card.

Card placement was **measured, not typed** (`make_cards.py`):

- The prompt bubble on b0 ends at y=1245 and TikTok's bottom furniture starts
  at y=1440, leaving 195px. That is two lines, not three — so the Instagram
  hook is 44px over two lines at y=1248, and the TikTok hook had to come down
  from 56px to 46px to clear 1440.
- The end card sits at y=1020, not lower: the twist line on b5 starts at
  y=1395 and the 4% push lifts it about 77px over the beat's 5.2s, so anything
  below ~1300 would cover the sentence the piece ends on.

Two overlays only — hook 0.00-2.30s, end card over the last 3s. No mid-video
captions, no comment CTA (this is not one of the four BUDGET Reels).

## Voiceover

63 words, 21.04s — **3.0 w/s**, which sits right on the ~3.1 planning figure
for Eryn over a 20s script. The timeline was built from the measured file
rather than from the word count, as always.

Raw Eryn came out at ~-24.4 LUFS / -2.7 dBTP. **+13.5 dB** then
`alimiter=limit=0.841:level=0` measured -14.0. Swept it rather than computing
it: the arithmetic gain lands several dB short because the limiter eats the
crest.

`elevenlabsusercontent.com` is blocked from this session, so the mp3 came back
through Drive (`GOOGLEDRIVE_UPLOAD_FROM_URL` into `November 6`, then
`drive.usercontent.google.com`).

## Checks run on the exports

- Prompt fully readable at 0.5s and 2.0s with the hook card below it; hook gone
  by 2.6s.
- Payoff (Northgate $10,300, "Cheapest") on screen at 2.6s.
- End card at 18.5s and 20.9s sitting above the twist line, which stays
  readable.
- 1080x1920 (ratio 0.5625), 30fps, H.264, AAC 192k/48kHz, `+faststart`.

## Caption

`build/caption.txt`, 820 characters, same text for TikTok (TikTok takes no
"link in bio" and this piece has nothing to download, so the body simply ends
on "Save this for your next vendor quote.").
