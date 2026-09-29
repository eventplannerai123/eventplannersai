# Outdoor reception rained out, rebuilt indoors — 2026-09-29

Status: **approved and scheduled.** Not yet posted.

Approved 2026-09-29: "It's better go ahead at post at 9 am and give me the
tik tok file."

| | |
| --- | --- |
| Fires | 2026-09-29 **13:00 UTC** = 9am ET (EDT, UTC-4) |
| Trigger | `trig_01LhZkGu8XRFQ48fNd5dLrpy`, one-shot, fires into this session |
| Platforms | Instagram + Facebook only |
| Video URL | `.../main/reels/2026-09-29-rain-plan/rainplan-instagram.mp4` — verified 200, content-length 3402934 |
| `rainplan-instagram.mp4` md5 | `f43aef67c9dddd7af77e4dd229b49bf7` |
| `build/caption.txt` md5 | `429a3ce08611f74b05258f9e6274929b` |

The scheduled run re-checks both md5s and the URL before posting and stops
rather than posting if anything has moved. `rainplan-tiktok.mp4` was handed
over the same day and the trigger will not touch it.

| File | Platform | Duration | Voiceover | Payoff |
| --- | --- | --- | --- | --- |
| `rainplan-tiktok.mp4` | TikTok (manual) | 18.83s | -13.7 LUFS | 5.36s |
| `rainplan-instagram.mp4` | Instagram, Facebook | 19.67s | -14.0 LUFS | 5.87s |

Both 1080x1920 (ratio exactly 0.5625), 30 fps, H.264 High, AAC 192k / 48 kHz.
Tuesday of Round 6 — a short day in the length test (15–20s). Hook overlay
0:00–2:00; Round 6 ends on the output, so no end card.

## Two things cut out of the recording

**The failed download, which the author asked for by name.** A modal reading
"The file download failed. Please try again later." sits at **42.5–43.9s**,
with a grey Loading screen either side. The whole interruption runs
**38.65–44.50s**. Nothing in either cut comes from that span.

**A second, quieter one at 48.25–48.90s.** Opening the rain-plan image throws
the same Loading screen again before the diagram renders. The first build
caught it — a blank "Loading" frame landed at 7s in the export, and it was
only visible because the finished file was checked frame by frame rather than
the segment list being trusted. The reveal now starts at **49.00s**, after
the diagram is drawn.

Both exports were re-scanned afterwards for near-blank frames. The only hits
are the rain-plan diagram itself, which is line art on white; each was pulled
and looked at to confirm.

## The ad

A **"Fever — Private corporate events"** in-app ad appears at the end. Its
lead-in line — "For private corporate event planning, here's one full-service
option" — enters at **104.25s**, so nothing past **104.00s** is used. That is
the sixth distinct advertiser in nine days, which is why the rule is to look
for anything new rather than a known logo.

The last segment ends at 76.40s, well clear of it. Bottom 300px of both
finished exports, last 3s at 10fps, through the final frame: clean.

## Voiceover

The guide's script is **30 words**, about 11.5s against a 15–20s target — the
very bottom of its own 30–45 band, and it would have left 7+ seconds of
silence in a 19s cut. Extended to **49 words** by naming what the output
actually rules out:

> …what still fits, what gets cut, and which vendor I call first. **The food
> truck, the fire pits, the lawn games and the string lights simply have no
> indoor version.**

All four are on screen in the reveal, each marked CUT in the table. TikTok's
opens command-style instead and runs 48 words.

Instagram 19.17s, TikTok 17.87s. Vanessa - Beach Girl, `8DzKSPdgEQPaK5vKG0Rs`.

## The opening was rebuilt

The first version started at source 7.00s and opened on the run-of-show PDF.
The author asked why the prompt was not the first thing on screen, and she was
right: **this recording opens exactly as the house rules ask** — the prompt
already sitting in the input box, all three files attached, and the send tap
on camera at about 0.7s. Three of the last four recordings began after the
tap, and that was assumed rather than checked. It is the first thing the
viewer sees now.

The hook card moved with it. At the usual y=620 it landed square on the prompt
text — the one thing the opening exists to show — so it sits at **y=1300**,
over the keyboard, which carries no information. The send button stays clear,
which is the fault the Sep 23 card had at y880.

## Structure

| # | Source | On screen | IG out |
| --- | --- | --- | --- |
| 1 | 0.00–1.70 @1.0x | **The prompt in the box, then the send tap** | 0.00–1.70 |
| 2 | 10.20–12.20 @1.0x | The 14,250 sq ft lawn plan, held at normal speed | 1.70–3.70 |
| 3 | 21.00–26.00 @2.3x | Generating, 2.17s on screen | 3.70–5.87 |
| 4 | 49.00–55.80 @1.0x | **The generated INDOOR RAIN PLAN diagram** | 5.87–12.67 |
| 5 | 68.00–74.90 @1.0x | "What stays vs. what gets cut" | 12.67–19.67 |

## Pacing: why the empty hall is not in the cut

An earlier build had four setup beats — prompt, lawn plan, empty hall,
generating — and with the 6-second payoff ceiling each came out at about a
second. The author's verdict: "It flips to the rain plan floorplan way too
fast." The generating beat in that version was **1.07s**, under the 2.5s the
timing rules ask for, which is what made the reveal feel unearned.

Four beats do not fit under six seconds at a speed anyone can read, so the
**empty hall was dropped rather than all four being squeezed**. Nothing is
lost from the idea: the rain plan's own header reads "Main hall · 76 × 50 ft ·
3,800 sq ft", so the indoor size still lands, and the diagram itself is the
hall. What it buys is a real 2.0s look at the lawn plan at normal speed and a
2.17s generating beat, with the reveal then held for 6.8s.

The transformation is legible without the voiceover: a green lawn plan, an
empty hall, then a drawn indoor layout and a KEEP/CUT table.

## The seeded constraints

The guide names two to watch for. One is **in the reel**: the table's first
row reads "Band — KEEP — 14×10 minimum indoor stage", which is the band's
stated refusal to play without it.

The other is **not**: Shelter Co's 48-hour notice, after which the full
pergola fee applies anyway, appears at 96s in the call-order section, past
where a 15–20s cut can reach. It is in the footage and correct — just not in
this cut. Worth knowing if the piece is ever recut longer.

## Caption

`build/caption.txt`, md5 `429a3ce08611f74b05258f9e6274929b`, 533 bytes.
Verbatim from the guide, including the shortened **"Prompt below."** CTA that
replaced "The full prompt is in the caption below" guide-wide on 2026-09-28.
