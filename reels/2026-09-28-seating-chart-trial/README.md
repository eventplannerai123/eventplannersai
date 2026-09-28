# Guest list with family notes into a seating chart — 2026-09-28

Status: **built, handed over. NOT posted, and must not be posted from here.**

| File | Platform | Duration | Voiceover | Payoff |
| --- | --- | --- | --- | --- |
| `seating-tiktok.mp4` | TikTok (manual) | 40.00s | -14.2 LUFS | ~3.0s |
| `seating-instagram.mp4` | Instagram **Trial Reel** (manual) | 40.43s | -13.9 LUFS | ~3.0s |

Both 1080x1920 (ratio exactly 0.5625), 30 fps, H.264 High, AAC 192k / 48 kHz.
Monday of Round 6 — 40–50s, **excluded from the length test** because trial
reach is non-follower and cannot be compared. Hook overlay 0:00–2:00; Round 6
ends on the output, so no end card.

## Why this session built it at all

The guide routes trial-day edits to the Claude.ai chat, not here, and says
outright: "If this block is pasted to you, stop and tell Sahiba it is a trial
day." That is what happened first — the footage arrived and this session
stopped and said so.

It got built here only because **the recording is 96.8 MB** (86.38s), three
times the ~30 MB chat ceiling, so it could not be uploaded to the Claude.ai
chat at all. It reached this session through Google Drive, which is the only
route that handles a file that size. The author was told, chose this, and said
"You can still build it and I'll post it."

**Nothing about that changes the posting rule.** The Trial toggle is in-app
only; anything published from here would go out as a regular feed Reel, waste
the trial, and risk Instagram's duplicate-content throttle on both copies for
up to 30 days if the piece later went up as a trial. The two files are handed
over and she uploads the Instagram one herself.

## The seeded constraints all surfaced

The guide's check: "Three constraints are impossible by design […] If the
output returns a tidy chart with nothing flagged, it has broken one silently —
re-run." It did not. The Constraint Audit flags **four**:

| # | Flagged on screen | Designed in? |
| --- | --- | --- |
| 1 | Immediate family — 14 must sit together, tables hold 10 | yes |
| 2 | Danvers cousins — 11 cannot fit one 10-person table | found by the model |
| 3 | Bridge club — all 8 together, but Pat and Gloria must be separated | yes |
| 4 | Nina Ellery — must sit with both Carol and Douglas, who must not sit together | yes |

All three seeded impossibilities are named, with the compromise stated for
each. No re-run needed.

## Structure

The source is badly shaped for a 40s cut: ~9s of usable input, a **42-second
visually static optimise phase**, and only ~9s of real reveal. The four-conflict
paragraph is what saves it — it lands early and is the actual payoff.

| # | Source | On screen | IG out |
| --- | --- | --- | --- |
| 1 | 6.0–14.0 @4.6x | The guest list spreadsheet, scrolling | 0.00–1.74 |
| 2 | 15.0–18.0 @2.4x | Prompt sent, response starts | 1.74–2.99 |
| 3 | 18.0–25.0 @2.8x | Generating beat, 2.50s on screen | 2.99–5.49 |
| 4 | 25.0–34.0 @1.0x | **The four incompatible notes** | 5.49–14.49 |
| 5 | 36.0–49.0 @2.9x | Representative slice of the optimise phase | 14.49–18.97 |
| 6 | 60.0–68.5 @1.0x | "The feasible core is now solved" | 18.97–27.47 |
| 7 | 69.0–77.0 @3.2x | The wait, then "Done" | 27.47–29.97 |
| 8 | 77.5–86.38 @0.85x | The Constraint Audit | 29.97–40.43 |

Segment 5 is a **representative slice**, not the whole phase compressed — the
body text does not change across those 42 seconds, only the status line, so
compressing all of it would have been 42 seconds of nothing.

Segment 8 runs at **0.85x, slower than real time**. The audit is dense and the
rule is to hold the reveal so it is readable; the source scroll is quicker than
a first-time reader can follow.

Measured payoff is **~3.0s** — the incompatibility paragraph is readable well
before the 5.49s the segment map predicts, because it is already on screen
during segment 3.

## Ad check

No in-app ad anywhere in this recording — the composer bar covers the bottom
of frame throughout. Verified on the source across all 86s, and again on the
bottom 300px of **both finished exports** across the last 3s at 10fps, through
to the final frame. Clean.

## Captions

| File | Use |
| --- | --- |
| `build/caption-instagram-trial.txt` | **No hashtags** — trials are kept off hashtag pages, so they do nothing. 502 bytes, md5 `3eb1e885b418cb995167adb33c3df044`. |
| `build/caption-tiktok.txt` | Normal upload, hashtags fine. 569 bytes, md5 `32d9e2ceced7af24218258d7fc8ec39b`. |

Both bodies and the AI prompt are verbatim from the guide.

## Renderer note

`build/render.py` renders each segment to its own file and concatenates,
rather than building one filtergraph. Eight trim branches over a 96.8 MB HEVC
source decode the whole file once per branch and the process was OOM-killed.
Kept segment-at-a-time for any source this size.

## What is still the author's

- Uploading `seating-instagram.mp4` to Instagram **with the Trial toggle on**.
- Uploading `seating-tiktok.mp4` to TikTok as a normal manual upload.
- The day's TikTok back-catalogue post: the Sep 2 hors d'oeuvres carousel.
- Relabelling the guide heading "Trial Reel — confirmed" with the view count
  once it has actually posted, and checking it after 72 hours.
