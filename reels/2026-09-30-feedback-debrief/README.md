# Fifty feedback responses into a one-page debrief — 2026-09-30

Status: **approved and scheduled.** Not yet posted. Built a day ahead on
2026-09-29 at the author's request.

Approved 2026-09-29: "Yes to both. For Instagram/facebook schedule Wednesday
at 9 AM."

| | |
| --- | --- |
| Fires | 2026-09-30 **13:00 UTC** = 9am ET (EDT, UTC-4) |
| Trigger | `trig_011Uacnre4d6ouzL7tvPo5vR`, one-shot, fires into this session |
| Platforms | Instagram + Facebook only |
| Video URL | `.../main/reels/2026-09-30-feedback-debrief/debrief-instagram.mp4` — verified 200, content-length 17993244 |
| `debrief-instagram.mp4` md5 | `e3c5717bedf0c6a2840f70010a0ed328` |
| `build/caption.txt` md5 | `73279958f9b32186b5696d494a195139` |

The scheduled run re-checks both md5s and the URL before posting and stops
rather than posting if anything has moved. It also carries a note that the
31.17s length is a deliberate miss, so a later session does not read it as a
fault and try to "fix" it. `debrief-tiktok.mp4` was handed over on 2026-09-29
and the trigger will not touch it.

| File | Platform | Duration | Voiceover | Payoff |
| --- | --- | --- | --- | --- |
| `debrief-tiktok.mp4` | TikTok (manual) | 28.90s | -13.9 LUFS | ~4.6s |
| `debrief-instagram.mp4` | Instagram, Facebook | 31.17s | -13.9 LUFS | **~5.0s** |

Both 1080x1920 (ratio exactly 0.5625), 30 fps, H.264 High, AAC 192k / 48 kHz.

## This day deliberately misses the length test

The guide asks for **40–50s** and the footage cannot give it. The author was
shown the arithmetic and chose to ship short.

| | |
| --- | --- |
| Source | 36.47s |
| Usable reveal | 13.10–34.20s = **21.1s** (the last ~2s is blank scroll past the end of the answer) |
| Must be compressed | ~10s of prompt, CSV and generating, to hold the 6-second payoff ceiling |
| Natural length | ~29–32s |
| To reach 40s | the reveal would need ~**0.60x** — visible slow motion on a page of scrolling text |

**Sep 30 is the last day of the length test**, so this costs a data point.
That is the author's call, recorded here rather than presented as a drift.

## Voiceover: the guide's script says the same thing twice

The guide's 106-word script lists the ask — "group them into themes, count how
many said each thing, pull the quote that best captures each one, and give me
three concrete changes" — and then lists it again as the result: "Back came
the themes, how many people raised each one, the quote that says it best, and
three changes I could actually make."

At 106 words it is also ~41s, which a ~31s cut cannot carry. The second list
was replaced with what the output actually returned:

> **Six themes across all fifty, program flow and room capacity the biggest at
> thirteen.**

Checked against the footage: six themes, counts 9 + 8 + 7 + 8 + 13 + 5 = 50,
and 13 is the largest. Instagram 84 words / 30.12s, TikTok 73 words / 27.82s.

## Structure

Three setup beats, none under two seconds — the fault the author called out on
Sep 29, where four beats left each at about a second.

| # | Source | On screen | IG speed |
| --- | --- | --- | --- |
| 1 | 0.00–3.15 | Prompt in the box, send tap, the model starting to respond | 1.00x |
| 2 | 4.20–11.00 | The 50 free-text responses, scrolling | 3.40x |
| 3 | 13.40–34.20 | Themes and counts, the quotes, the three changes | **0.800x** |

Segment 1 carries the working beat inside it rather than as a separate
one-second flash. Segment 3 runs slower than real time because the debrief is
dense and the rule is to hold the reveal so it can be read.

**The reveal entry moved from 13.10 to 13.40 after checking the first build.**
At 13.10 the frame is still mostly the prompt bubble with the answer only
starting underneath, and the theme table did not become readable until about
**6.0s** in the export — at the payoff ceiling rather than under it. Entering
at 13.40 lands on "Worked for 10s" with the answer and the Theme breakdown
heading already on screen, which brings the payoff to **~5.0s**. The 0.3s
skipped was the least informative part of the answer.

## Ad check

No in-app ad anywhere in this recording — it ends on the Sources row with
clean white space. Verified on the source across 30–36.5s, and again on the
bottom 300px of **both finished exports**, last 3s at 10fps, through to the
final frame: **clean**. Both end on "Those three changes address the largest
concentration of negative feedback while preserving the things attendees
already said were working."

## Caption

`build/caption.txt`, md5 `73279958f9b32186b5696d494a195139`, 503 bytes.
Verbatim from the guide, with the shortened "Prompt below." CTA.
