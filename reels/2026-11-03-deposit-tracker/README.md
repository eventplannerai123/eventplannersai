# 2026-11-03 — Vendor deposit tracker, redone with a file

**Status: both cuts built and rendered. Waiting on her go-ahead.**

**The date moved twice and the folder name now matches it.** Sat 24 → Sat 31 →
**Tue 3 Nov**, where her revised calendar of 2026-10-25 puts it. This directory
was `2026-10-24-deposit-tracker-file` until the recording arrived; nothing had
been published from it, so it was renamed rather than duplicated.

Replaces the Sep 3 prompt, which typed every dollar amount and date into the
chat — her note of Oct 19: no planner does that. The Oct 15 rebuild stays up;
this is a new video, not an edit of it.

## The cuts

| | |
| --- | --- |
| Instagram | `deposit-tracker-instagram.mp4` — 30.0s, 1080x1920, **−14.3 LUFS**, −1.3 dBTP |
| TikTok | `deposit-tracker-tiktok.mp4` — 32.0s, 1080x1920, **−14.2 LUFS**, −1.0 dBTP |
| Voiceover | Eryn (`kdnRe2koJdOK4Ovxn2DI`, `eleven_v4`), 26.28s and 28.53s |
| Caption | `build/caption.txt` — the guide's, with "The prompt:" under its own `AI Prompt:` label |

Both sit inside the brief's 30–45s. Time to payoff is **0s on both**: the
guide's format line for this piece asks to open on the finished list, so the
answer is on screen from frame one and the prompt is the second beat. It is
never cut — rule 2 — only moved behind the result.

## Her recording

Filmed Sat 31 Oct, three days early, and dropped straight into Drive
`October 24` as a bare link. 1206x2622, **38.6s**, 60fps HEVC, 70.1 MB.

**The opening is exactly right and needed no rescue.** At 0.0s the prompt sits
in the input box with the PDF attached and the send button in shot; the tap
lands inside the first second. That is the third recording in a row to open
correctly, and it is still worth checking rather than assuming.

**The answer matches the guide's sanity check exactly**: $74,940 contracted,
$28,225 paid, $46,715 still owed, 37.7% paid, transportation ($1,350, Nov 1)
next. That is what the demo file was built to produce, and it held — ChatGPT
resolved every wedding-relative date too (catering to Feb 27, the band and hair
and makeup to Mar 13).

**No ad in this recording.** Nine advertisers so far, so the check is for
anything new at the bottom of the answer rather than for a known logo. Every
one of the eight beat stills was looked at whole in `build/preview.png`, and
the exports are built from nothing but those stills, so the scan covers every
frame that ships.

## How it is cut

**Freeze frames, not scrolling footage.** The answer is one long scroll, so each
beat is a still lifted from it and held, per rule 3, with a slow 4% push across
its own length so the frame is never actually static.

| Beat | Source | Instagram | TikTok |
| --- | --- | --- | --- |
| totals dashboard, $46,715 highlighted | 15.0s | 3.5s | **opens, 4.8s** |
| chronological table, Nov 1 row highlighted | 17.6s | **opens, 4.6s** | 4.4s |
| the sent prompt, PDF attached | 2.0s | 3.2s | 3.4s |
| the payment sheet she uploaded | 7.0s | 3.0s | 3.0s |
| further down the same table | 19.6s | 4.2s | — |
| the band, due on the wedding day | 21.4s | 3.8s | 4.6s |
| $7,350 due in the next 30 days | 23.0s | — | 4.2s |
| "My biggest concern is catering." | 29.5s | 7.7s | 7.6s |

Crop computed from the source: 1206 wide means 1206/0.5625 = 2144 tall, with
the standard 478 y-offset — status bar and red recording dot off the top, the
input bar left at the bottom where the platform's furniture covers it. The
floating scroll-to-bottom button stays, her instruction of Oct 10.

Highlights are fitted with `tools/cardkit.py` `fit_highlight` from a seed y,
never typed: the seed picks the line and the frame decides where its ink is.
`build/preview.png` is the check.

## A bug in cardkit this build found, now fixed

The first preview came back with four flat yellow bars where the figures should
have been — the highlight was **opaque and hiding the line it exists to
emphasise**. Pillow only blends an RGBA fill when the destination has no alpha
channel of its own; draw the same fill onto an image opened with
`.convert("RGBA")` and it replaces the pixels instead. `draw_highlight` now
asserts the image is RGB and says why.

The preview step is what caught it, before an export was burned. That is the
whole reason it exists.

## Loudness

Measured Eryn takes: **−24.0 LUFS / −1.6 dBTP** (Instagram) and **−23.7 /
−1.1** (TikTok). `loudnorm`'s two-pass stalls at −16.5 on her crest factor, so
the gain goes on explicitly (**12.8 dB** and **12.5 dB**) and `alimiter` with
`level=0` catches the peaks — auto level renormalises back to full scale and
looks exactly like no limiting at all. Tuned against the export: 12.3/12.0 gave
−14.5 on both.

## The demo

`Vendor Payments — March Wedding`, Google Sheet id
`1JiQVyhx72BvWMDZPTn99_KQGmOZ980oR8d8VbEwePKQ`, built Oct 19, in Drive
`October 24`. Wedding **Sat 13 March 2027**, 160 guests, ten vendors, due dates
deliberately mixing fixed dates with ones tied to the wedding.

## Prompt she pasted (sheet uploaded first, as a PDF)

> Here's the vendor payment sheet for a March 13 wedding. Today is October 24.
> List every payment still owed in date order, working out the real date for
> anything tied to the wedding date. Flag anything due in the next 30 days,
> total what's been paid and what's still owed, and tell me which balances
> could still change.
