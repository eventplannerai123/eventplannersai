# 2026-10-15 — Rebuild 2: Sep 3 vendor deposit tracker

**Not built yet. Waiting on the original file.** Instagram and Facebook only,
not TikTok, and nothing posts without her go-ahead.

Rebuild 2 of the four-Reel hook experiment. Original:
[instagram.com/reel/Dc04ivflJtl](https://www.instagram.com/reel/Dc04ivflJtl/),
IG media id `18437908249177797`, published 2026-09-03 — 14 views, 14 reach,
**83% skip rate**, 3.7s average watch.

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

## Oct 15: two files arrived, neither is the one

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
experiment depends on.

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

## The plan once the file lands

Change only the opening, per the guide's rebuild rules:

1. **New first frame** — a freeze of the finished tracker sorted by nearest due
   date (available in the original around t=8.5), because the guide says open
   on the finished result rather than the typing.
2. **New hook overlay**, approved Oct 14:
   **"A missed vendor balance date is survivable. Going quiet isn't."**
3. **New opening voiceover line to match**, replacing *"Five vendors, five
   deposit dates, five balance due dates. Here's how I stop losing track."*
4. Everything from ~4.2s onward is the original, untouched — picture and audio
   both — so any change in the numbers belongs to the hook.
5. Fresh encode, new file. **Never re-upload the original**: a byte-identical
   re-upload gets suppressed as a duplicate.

Judge on **skip rate and average watch time at 7 days**, not views — the
account had fewer followers in early September.

## Caption

`build/caption.txt`. The original caption with its first sentence replaced by
the approved hook, and `#theeventplannerai` swapped for `#aiforeventplanners`
because the old handle points at an account name that no longer exists.

Her open question — *"How many deposits are you tracking right now, honestly?
Comment the number."* — is kept. That is a conversation prompt, not a
comment-to-unlock keyword gate, and only the keyword mechanic is retired.

## Why this hook

Content bank, her Oct 14 answer: a balance date slipping happens, and more
often than people admit. It has never cost her a vendor relationship — but only
because the slip is not the damage; **going quiet is**. She rings and
apologises straight away, every time.

She rejected a first version, "It never cost me a thing", as too flippant:
*"i dont want to be so flipant about it like its not important."* The
discipline is the point, not the escape.
