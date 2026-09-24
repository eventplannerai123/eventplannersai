# Client enquiry to event brief reel — 2026-09-24

Status: **published 2026-09-24.** Approved in conversation ("go ahead and
post"), then posted to Instagram and Facebook.

| Account | Post |
| --- | --- |
| Instagram `@aiforeventplanners` | https://www.instagram.com/reel/Ddq8qEDihmJ/ |
| Facebook "The Event Planners AI" | https://www.facebook.com/reel/2060227754604735/ |

Both captions were read back live and diffed against `build/caption.txt` with
`cmp` — **identical byte for byte on both**, md5
`f0cb38790c659cbcb0c3d96630537abe`, 587 bytes. Four literal `#`, no
"Hashtags:" label, no comment keyword, no link-in-bio, no dead
`#theeventplannerai`.

The Instagram container (`18092292773367131`) reached FINISHED after 25.1s
over 9 status checks and published first try as media `18161078440433918`.

Facebook took two reads plus a 60s wait to surface in the page feed — the
same lag as Sep 19, 21, 22 and 23. Read through `FACEBOOK_GET_PAGE_POSTS`
per the Sep 23 note, since `FACEBOOK_CREATE_VIDEO_POST` returns the reel id
(`2060227754604735`) rather than the post id
(`1233196746554445_122111505363449533`). Nothing was re-posted; the feed shows
one copy.

TikTok is not posted from here. `enquiry-tiktok.mp4` was handed to the author
for manual upload.

Thursday of Round 6 — a long day in the Sep 23–30 length test (40–50s).
Milestone category, not wedding.

## Cuts

Both 1080x1920 (ratio exactly 0.5625), 30 fps, H.264 high, CRF 19,
`+faststart`, AAC 192k at 48 kHz. **TikTok built first**, per the brief.

| File | Platform | Duration | Voiceover | Time to payoff |
| --- | --- | --- | --- | --- |
| `enquiry-tiktok.mp4` | TikTok (manual upload) | 44.65s | -14.16 LUFS, TP -0.97 | 2.60s |
| `enquiry-instagram.mp4` | Instagram, Facebook | 45.91s | -14.10 LUFS, TP -1.19 | 2.90s |

Opening lines:

- Instagram (author's upload): "Every planner gets this message."
- TikTok (generated to match): "Stop reading client enquiries four times
  over."

Hook overlay `Every client sends you this paragraph.` at 0:00–2:00, verbatim
from the brief. **No end card** — Round 6 ends on the output. Both finish on
"The biggest items I'd resolve first", the six-question summary.

## The voiceover carries it

The guide's script was extended on Sep 24 to 112 words, about 45s spoken.
That is what makes a long day work: the Instagram cut is 45.91s against 44.68s
of speech, so the silent tail is **1.23s**. Yesterday's 15s piece had 6.8s of
tail; a 45s piece built on the old 66-word script would have had twenty.

Sync landed well without forcing it — "Venue type, dietary needs, timings"
plays exactly as the dietary questions scroll past at 38s.

## The generating beat is 1.4s, and that is honest

The standing rule wants a visible generating beat of 2.5–3s sped to 2–3x.
**Not achievable from this footage, and not faked.** The real wait was about
1.5 seconds — the prompt is text, not a document to read, so the answer began
almost immediately. It plays at 1x. Stretching a 1.4s loading dot to 2.5s
would have misrepresented the wait as longer than it was, which is the
opposite of what the rule is for.

## Three clips, no frame-matchable seam

Not one recording split with "Save as New Clip" — three separate scroll
passes. Tested and recorded so the next long day does not repeat the search:

- Best whole-frame match across the overlap regions: MAD **13.4** and
  **18.6**. A true frame match sits near zero.
- Last frame of one clip against the first frame of the next: MAD **21.0**
  and **17.7**, against a control (C-last vs A-first) of 28.2. No adjacency
  either.

The content *is* contiguous — checked by reading the text at each boundary —
with about one to two lines of scroll offset at each seam. On a continuously
scrolling page that reads as ordinary scrolling. A dense page of text throws
a large MAD for even a one-line offset, which is why the number looked alarming
and the eye did not.

| Clip | Used | Content |
| --- | --- | --- |
| `8eeb2955` (17.05s) | 0.40–17.05 | Prompt in the box, **send tap on camera at 1.5s**, client message |
| `5831a557` (16.86s) | 0.00–16.86 | Rest of the message, then the structured brief |
| `4b51390e` (15.59s) | 0.00–12.40 | Questions to ask before quoting, biggest items |

### Crop

`crop=1206:2144:0:478` — recomputed from this source: 1206 / 0.5625 = 2144,
478 off the top clears the status bar and the recording dot.

## The in-app ad — and a crop that was too shallow

A **Cambridge "Event Florals in NYC"** ad follows the answer in clip A.

First pass cut clip A at 13.00, which a bottom-620px crop of the raw footage
showed as clean. **The finished export still had the ad's lead line on its
last frame** — "For the 60th birthday event brief, here's an event…" — because
that crop stopped about 20px short of the frame bottom once scaled.

Re-scanned the **full bottom 300px of the export** at 0.3s steps: clean
through 46.2s, text visible at 46.5s. Clip A now stops at **12.40s**, and both
finished files were re-checked to the bottom edge of their final frame. Clean.

Worth recording: the Sep 21 lesson was "verify visually, not by colour
threshold". This adds a second half — **verify on the finished file, over the
full frame**. A crop of the source that misses the last few rows gives the same
false all-clear a colour test does.

## Accuracy — the five seeded traps

The guide says the enquiry was written with five deliberate traps and that
"those are the traps the brief should surface". All five do:

| Trap | Where it surfaces |
| --- | --- |
| Two conflicting dates (14th, then the 21st) | "I'd treat November 14 and November 21 as tentative dates, with the 21st currently sounding like the stronger possibility" — and it is question 1 of the final six |
| Headcount as a range | "Working planning number: 50 guests until the client confirms otherwise"; "Exact guest-count range" in the final six |
| Budget buried mid-sentence | "Target budget: Approximately $4,000–$5,000 total… **Important:** Need to clarify exactly what 'everything' includes before determining whether the budget is realistic" |
| Hates attention / would love a surprise | "Guest of honor: Turning 60; reportedly does not like being the center of attention, but would enjoy a surprise" |
| Half-remembered allergy | "One aunt has a dietary restriction, but client is unsure whether it is **gluten or dairy**"; question 26 asks which |

Nothing to redact — the enquiry was written for the demo, and the caption
says so outright.
