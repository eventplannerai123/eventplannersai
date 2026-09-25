# Dense BEO into a one-page day-of crib sheet — 2026-09-25

Status: **published 2026-09-25.** Approved in conversation ("Its perfect go
ahead and post").

| Account | Post |
| --- | --- |
| Instagram `@aiforeventplanners` | https://www.instagram.com/reel/Ddta32ulMwS/ |
| Facebook "The Event Planners AI" | https://www.facebook.com/reel/1115616567472637/ |

Both live captions were read back and compared to `build/caption.txt`
character for character: **identical on both**. Instagram container
processing took 28.4s.

Facebook did not surface in the page feed on the first two read-backs, which
is the documented normal behaviour — it appeared on the third, post id
`1233196746554445_122111744817449533`. Nothing was retried.

| File | Platform | Duration | Voiceover | Payoff |
| --- | --- | --- | --- | --- |
| `beo-tiktok.mp4` | TikTok (manual) | 15.67s | -13.9 LUFS | 5.60s |
| `beo-instagram.mp4` | Instagram, Facebook | 15.57s | -13.9 LUFS | 5.90s |

Both 1080x1920 (ratio exactly 0.5625), 30 fps, H.264 High, AAC 192k / 48 kHz.
Friday of Round 6 — a short day in the length test (15–20s). Hook overlay
0:00–2:00; Round 6 ends on the output, so no end card.

Built from the **new guide** (`theeventplannerai_september_guide.docx`,
uploaded 2026-09-25). Friday's block is unchanged in substance from the
previous version.

## The AutoFill banner, cut out

The author asked for it before anything else. ChatGPT's "AutoFill can assist
with filling out this form" banner covers the top of clip A from **7.60s to
9.30s** while the BEO is open. Removing 7.50–9.40 takes the clip from 16.00s
to 14.10s.

The whole clip was scanned for the banner's button rather than just the spot
she pointed at — it appears once. The other blue-pixel hits at 0.0–5.9 and
14.8–15.9 are the chat bubble and the send button, not the banner.

At the seam the BEO page sits at an identical scroll position either side, so
there is no jump. The "1 of 20" page pill fades at the cut, which reads as its
normal auto-hide.

`build/A_noautofill.mp4` is that cleaned clip, kept because every later step
depends on it.

## What capped the length

Two independent limits, and together they fix the duration almost exactly:

- **A "Turning Stone" in-app ad** ("Make It Easier — work with an onsite
  events team") starts fading in at **B 11.30s**. The reveal therefore ends at
  **11.10s**. This is a fifth distinct advertiser in five days — Acrobat,
  Firefly, Rillion, Cambridge, now Turning Stone. Looking for a known logo
  remains the wrong check.
- **The 6-second payoff ceiling.**

The crib sheet's title lands at B 1.45s. So:

```
total = payoff + (11.10 - 1.45) = payoff + 9.65
```

With payoff held under 6s, **the piece cannot exceed ~15.65s**. Both cuts sit
just under that, inside the 15–20s target. Nothing was traded away — the
ceiling simply is where it is.

## Voiceover

The guide's script is **29 words**, about 11s against a 15–20s target — below
the guide's own 30–45 word band for a short piece, and it would have left ~4s
of silence. Extended to **37 words** by naming what the sheet actually shows:

> A full banquet event order, and on the day you need about a tenth of it.
> Here's that tenth, on one page, in the order the day actually happens —
> **arrivals, room sets, meal times, dietary notes, deadlines.**

Every item added is genuinely on screen in the reveal: "8:00 AM — Arrive /
Office", the room sets, meal service times, the per-guest dietary list, and
the DEADLINES / MUST-DO ITEMS block. No counts are named, per the guide.

TikTok's opens command-style instead: "Stop carrying the whole banquet event
order around on site." 38 words.

Both generated here — Vanessa - Beach Girl, `8DzKSPdgEQPaK5vKG0Rs`.
Instagram 15.28s, TikTok 15.54s.

## Structure

| # | Source | On screen | IG out | TikTok out |
| --- | --- | --- | --- | --- |
| 1 | A 7.30–12.60 | The dense BEO, scrolling | 0.00–2.00 (2.65x) | 0.00–1.80 (2.95x) |
| 2 | A 0.60–6.70 | Prompt sent, "Searched files", "Thinking" | 2.00–5.00 (2.03x) | 1.80–4.45 (2.30x) |
| 3 | B 0.55/0.30–11.10 | The one-page crib sheet | 5.00–15.57 | 4.45–15.27 |

TikTok then holds its final frame for 0.40s, because its voiceover is 0.26s
longer than Instagram's and the reveal cannot be extended past the ad.

Segments 1 and 2 run out of chronological order: she opened the BEO while the
answer was generating. Document → thinking → answer reads correctly and is
all her own footage.

## Ad check

Bottom 300px of **both finished exports**, last 2.5s at 10fps, through to the
final frame — clean. Checked on the mp4s, not a crop of the source, per the
rule added after Sep 24.

## Two rendering bugs found and fixed

- **The hook overlay did not render.** A single-frame PNG fed to `overlay`
  with `repeatlast=0` shows on frame one and then vanishes. The first build
  had no hook at all. Fixed with `eof_action=repeat:repeatlast=1`. Verified
  visually on the export, not assumed from the filtergraph.
  The Sep 26 reel was checked for the same fault and is **fine** — its script
  builds the hook as a timed stream, so it renders 0:00–2:00 correctly.
- **`alimiter` silently undid its own limiting.** Its `level` option
  (auto-level) defaults to **true**, which renormalises the output back to
  full scale. With it on, the audio clipped at 0.0 dBFS no matter how low the
  `limit` was set. `level=0` is required.

## Loudness: why not loudnorm

This voiceover could not reach -14 LUFS through `loudnorm`. Its crest factor
is high enough that the filter's own true-peak ceiling binds first: the
measured two-pass result stalled at **-15.8 LUFS with TP pinned to -1.5**, and
raising the offset moved it only 0.6 dB.

So the gain is applied explicitly and `alimiter` catches the peaks. Both cuts
land at **-13.9 LUFS**, peaks -1.2 / -1.1 dBFS, LRA 3.0 / 3.2 against the
source's 2.8 — the body of the speech is untouched.

The first-pass measurement is still taken; it is what the gain is computed
from. Gains: Instagram +10.9 dB, TikTok +10.1 dB, limiter at 0.85.

## The recording does not show the send tap

Clip A opens with the prompt already sent and "Thinking" on screen. The guide
asks for the tap to be on camera. Flagged to the author, who said to run with
it today ("My mistake but let's run with it today"). Third occurrence.

Not faked: the piece opens on the BEO in motion instead, which suits a
transformation piece — the messy input is the cold open.

## Caption

`build/caption.txt`, md5 `fad0e48421e7ade9366259c8563709e3`, 568 bytes.
Body, AI prompt and the four hashtags are verbatim from the new guide.
