# 2026-10-15 — Rebuild 2: Sep 3 vendor deposit tracker

**Built, not posted.** Instagram and Facebook only, not TikTok, and nothing
goes out without her go-ahead.

| | |
| --- | --- |
| Instagram / Facebook | `deposit-tracker-rebuild-instagram.mp4` — 16.07s, 2.4 MB |

1080x1920 (0.5625 exactly), 30 fps, H.264 High, CRF 19, `+faststart`, AAC 192k
at 48 kHz. **Same length as the original to the frame**, and a different file:
md5 `ccfe2518…` against the master's `88886519…`, so duplicate detection has
nothing to catch.

Rebuild 2 of the four-Reel hook experiment. Original:
[instagram.com/reel/Dc04ivflJtl](https://www.instagram.com/reel/Dc04ivflJtl/),
IG media id `18437908249177797`, published 2026-09-03 — 14 views, 14 reach,
**83% skip rate**, 3.7s average watch.

## What changed, and only what changed

| | Original | Rebuild |
| --- | --- | --- |
| First frame | the prompt being typed | the finished tracker, Due Date and Status in frame, two rows **OVERDUE** |
| Hook overlay | "Five vendors, five deposit dates, five balance due dates. Here's how I stop losing track." | **"A missed vendor balance date is survivable. Going quiet isn't."** |
| Opening voiceover | the same list of numbers | the hook, read aloud |
| Everything after 4.10s | — | **untouched, picture and sound** |

Verified rather than asserted. Frames either side of the splice were matched
against the master: from 4.3s on, MAD runs **1.4–1.8** across seven
timestamps, which is re-encode noise and nothing else; before the splice it
runs **38–51**. The hook card is present at 0.2, 2.0 and 4.0s and gone by
4.4s.

## The splice is at 4.10s, not 3.0s

The rules say "change only the first 3 seconds". The original's opening line
does not end at 3 seconds — `silencedetect` puts its clause gaps at 0.96 and
2.31, the line finishing at **4.014**, and the next sentence starting at
4.478. A cut at 3.0 would slice it mid-sentence.

4.10 sits inside that gap, and the new beat is exactly 4.10 long, so the file
is the same 16.07s and the body keeps its original timing.

## The audio is deliberately not at −14 LUFS

The master runs **−21.3 LUFS** and the rebuild runs −21.2. The house spec is
−14, but normalising would re-level the whole body, which is the one thing
these rules forbid — the experiment only works if the hook is the only
variable. The new line was brought to the body instead: measured at −20.4,
given −0.94 dB, and both sides of the splice now read **−21.34 exactly**.

Instagram normalises on playback anyway; the live Sep 3 post serves at −14.5.

## Opening frame: t=9.80, not 12.50

The brief says "the finished tracker sorted by nearest due date". At **12.50**
the table is tidiest but the Due Date column is cut off at the right edge —
the column the hook is about. At **9.80** both Due Date and Status are fully
in frame with two rows reading **OVERDUE**, against a line that says a missed
date is survivable. The title is clipped to "Payment Schedule"; worth it.

## Overlay

One card, no end card. Text from `tools/cardkit.py`-style measurement, not
typed coordinates: the frame's own content stops at **y=796**, so the card
sits at **y 1043–1317** in the white below it and covers nothing. Inside the
Oct 5 safe band (nothing above 230 or below 1440), asserted in
`build/make_cards.py` and checked on `build/preview.png` before rendering.

## No ad

The bottom 340px of the finished file was scanned at 1s intervals through to
the final frame. Nothing.

## Starting from scratch was offered and declined

She offered the original screen recording on Oct 15. Not used, deliberately:
the rebuild rules exist so that a change in skip rate and watch time can be
attributed to the hook. A fresh edit from raw would change every variable at
once and measure nothing — the same mistake the length test made.

## The blocker, and what changed since Sep 27

The Sep 3 piece predates this repo, so the 1080x1920 master is in neither the
repo nor Drive. [`reels/2026-09-27-vendor-payment-repost/README.md`](../2026-09-27-vendor-payment-repost/README.md)
hit the same wall and recorded two dead ends.

One of them is no longer dead. **Instagram's CDN is still egress-blocked**
(`scontent-iad3-1.cdninstagram.com:443` → `connect_rejected`), but
`GOOGLEDRIVE_UPLOAD_FROM_URL` pulls server-side, so Drive can fetch what this
session cannot. The copy now sits in `October 15` as
`2026-09-03-vendor-deposit-tracker-ORIGINAL.mp4`, id
`1G_1nNMpEYGggPrR5uBmK6s1WSho7R1sf`, and downloads here normally. **That route
is worth keeping** — it reaches anything Drive can reach.

**The second dead end still stands.** What came back is Instagram's transcode:
**720x1280**, 16.07s, HE-AAC 44.1k, 1.1 MB — its own URL tag reads
`CLIPS.C3.720`. Upscaled to 1080x1920 it would be visibly softer than
everything else on the grid, and this rebuild exists to measure a hook. A
softer picture is exactly the kind of thing that moves watch time on its own,
so building from it would confound the one number the experiment is for.

So the master has to come from her. It is a 16s screen-recording piece, about
3-6 MB, well inside what the chat takes.

## What the original does

| Source | What is on screen |
| --- | --- |
| 0.0–2.3 | prompt in the input box, hook card over it |
| 2.3–6.0 | sent prompt bubble, "Analyzing" |
| 6.0–8.0 | the answer: $22,000 contracted, $8,000 paid, $14,000 owed |
| 8.0–13.0 | the finished Wedding Vendor Payment Schedule table |
| 13.0–16.1 | end card, "Save this before your next booking." |

The opening voiceover line runs **0.0 to 4.02s** — measured with
`silencedetect`, which puts clause gaps at 0.97, 2.33 and 4.02 and the next
sentence starting at 4.47. So the splice point is ~4.2s, not 3.0s: the line the
rebuild replaces is four seconds long.

Original loudness is **−14.5 LUFS**, so the new opening can be cut to match
without touching the rest.

## Oct 15: the first two files sent were the wrong ones

Recorded because the trap is easy to fall into again — an account that runs
two cuts of everything has two files with nearly the same name.

| Sent | What it is | Verdict |
| --- | --- | --- |
| `tracker_TIKTOK.mp4` | 1080x1920, 16.07s, AAC LC, 3.4 MB | **the TikTok cut, not the Instagram one** |
| `Video_1.mov` | **220x480**, 21.6s, 1.7 MB | the raw screen recording, sent at compressed size |

`tracker_TIKTOK.mp4` is the right quality and the right length, but it is a
different edit. Its hook card reads **"Stop losing track of vendor deposits.
Do this instead."** — the command-style TikTok opening — against the Instagram
cut's "Five vendors, five deposit dates, five balance due dates."

**And the difference is not only the hook.** A frame-match against the
Instagram copy was run at 6, 8, 10 and 12s across offsets from −3.0 to +3.0s,
looking for a uniform shift that would mean the same body with a different
opening. There is none: the best offset differs per timestamp (−1.0 at t=8,
−0.5 at t=12) and t=6 never matches at any offset. The two cuts are paced
differently in the middle, which is what the two-cuts rule asks for.

So it cannot stand in for the Instagram body without breaking the control the
experiment depends on. She then put **`tracker_INSTAGRAM.mp4`** in the
`October 15` Drive folder (id `1wlX8n0AcuF71zGZh4xcmr_NXlkGeBzHp`, 1080x1920,
16.07s, 3.6 MB) and that is what the rebuild is built from. It was checked
against the live copy before use: MAD 2.3–2.8 at seven timestamps, and
clearly unlike the TikTok cut at the same points.

`Video_1.mov` is the unedited capture — status bar and recording dot still in
frame — and at **220x480** it is far below the output frame, so it was sent at
the default compressed size rather than "Actual". Not needed for a rebuild
anyway: rebuilding from raw would change the whole edit, not the first three
seconds.

## The opening voiceover is made

She approved the line on Oct 15: **"A missed vendor balance date is survivable.
Going quiet isn't."** — the hook read aloud, so the first three seconds do one
job instead of two.

`voiceover/vo-new-opening.mp3`, ElevenLabs, Vanessa - Beach Girl,
`eleven_multilingual_v2`, **4.00s** against the 4.02s slot the original's first
line occupies. It drops straight in.

