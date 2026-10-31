# 2026-11-02 — The fees nobody quotes

**Status: both cuts built and rendered. Waiting on her go-ahead.**

## The cuts

| | |
| --- | --- |
| Instagram | `venue-fees-instagram.mp4` — 20.0s, 1080x1920, **−13.9 LUFS**, −1.3 dBTP |
| TikTok | `venue-fees-tiktok.mp4` — 22.0s, 1080x1920, **−13.8 LUFS**, −1.1 dBTP |
| Voiceover | Eryn (`kdnRe2koJdOK4Ovxn2DI`, `eleven_v4`), 16.27s (45 words) and 18.13s (50 words) |
| Caption | `build/caption.txt` — the guide's, with "The prompt:" under its own `AI Prompt:` label |

Both open on the prompt, as the guide's DETAILS block asks ("Prompt (shown
first on screen)"). Time to payoff is **5.4s on both** — the fee table — inside
the 6-second ceiling but not by much, which is what sets the first two beats'
lengths.

## Her recording

Filmed Sat 31 Oct, six days early, in the same sitting as the Tue 3 deposit
tracker one, and dropped into Drive `November 2` as a bare link. 1206x2622,
**40.4s**, 60fps HEVC, 74.0 MB. Opening is right: prompt in the box, proposal
attached, send tap on camera.

## The twist did not happen, and that is her call

The guide's twist note expected the model to treat the 7% administrative fee
like a tip. It does the opposite, in a bullet of its own: *"This is separate
from the 22% service charge. The venue explicitly says it is not a gratuity."*
Asked what she would still change, she said **"its clean"**, so this ships as a
straight demo with the brief's voiceover, takeaway and caption unchanged.

That is **two pieces running** where the predicted twist failed to land — the
Sun 1 boxes Reel was the other. Worth watching before another brief writes the
twist in advance: the model is catching the thing the twist assumed it would
miss.

## It found all eight fees

Linen $1,450 · coat check $720 · cake cutting $630 · service charge $7,326 ·
bartenders $525 · security $780 · administrative fee $2,331 · overtime $1,200+.
Every figure matches the demo file.

## Two real numbers, and the cuts handle them differently

Its headline is **$253.40 a head ($45,612)**, because it treats the linen
upgrade as optional. It then gives **$261.46 ($47,062)** with the upgrade in —
which is the guide's sanity-check figure and the number the hook, the
voiceover and the caption all use.

So **Instagram never shows $253.40 at all**: it runs fee table → admin-fee
detail → the $261.46 line, and there is exactly one number in the piece.
**TikTok shows both**, in the order the answer gives them, and closes on "I
would budget $46,000–$47,000" where Instagram closes on the $261.46 line.

## How it is cut

Freeze frames with a slow 4% push, per rule 3, since the answer is one long
scroll. Highlights fitted with `tools/cardkit.py` `fit_highlight`; see
`build/preview.png`.

| Beat | Source | Instagram | TikTok |
| --- | --- | --- | --- |
| the sent prompt, proposal attached | 3.0s | 2.8s | 3.0s |
| proposal page 1, "$185 per person" | 5.2s | 2.6s | 2.6s |
| all eight fees outside the rate | 22.5s | 5.2s | 5.4s |
| the admin fee is not a gratuity | 28.0s | 4.0s | — |
| the bill as billed, $253.40 a head | 32.0s | — | 3.6s |
| with the linen upgrade, $261.46 | 36.0s | **closes, 5.4s** | 3.8s |
| "I would budget $46,000–$47,000" | 39.5s | — | **closes, 3.6s** |

**The proposal beat is at 5.2s, not 6.0s.** By 6.0 the page has drifted up far
enough that "$185 per person" sits in the top 12% that Instagram's own UI
covers. At 5.2 the whole of page 1 is in frame with the headline rate at 13%.

Crop computed from the source: 1206/0.5625 = 2144, standard 478 y-offset.

## No ad in this recording

Nine advertisers so far, so the check is for anything new rather than a known
logo. All seven beat stills were looked at whole in `build/preview.png`, and
the exports are built from nothing but those stills.

## The demo

`Venue Proposal — Winter Gala.pdf`, Drive id
`10H1B2BXJlzWkfF_s6-de7aAoS_hK4IQi`, in `November 2`. Six pages, fictional
venue, built Fri 31 Oct from `demo-files/2026-11/make_demo_files.py`, which
asserts the real total ($47,062, $261.46 a head) against the guide's figure.
