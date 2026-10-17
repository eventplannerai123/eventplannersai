# Feedback debrief rebuild — 2026-10-17

Status: **published 2026-10-17** at 11:18am ET on her go-ahead ("approve").
Not TikTok: the rebuild rules say Instagram and Facebook only.

| Account | Post |
| --- | --- |
| Instagram `@aiforeventplanners` | https://www.instagram.com/reel/DemaWL6iETX/ |
| Facebook "The Event Planners AI" | https://www.facebook.com/reel/922363110962541/ |

Instagram media `18002430083814206`, `is_shared_to_feed: true` — a regular
feed Reel, which is what a rebuild must be. Container finished in 22.5s over 8
checks. The live Instagram caption was read back and diffed against
`build/caption.txt`: **identical**.

Before posting: the raw URL returned 200 at exactly the committed byte count
(16,583,075), and both duplicate checks came back clean, newest entry on each
being the Oct 16 AI-makes-mistakes piece.

**Facebook surfaced on the second read-back**, feed entry
`1233196746554445_122116305879449533`, created 15:18:59 UTC — 56 seconds after
the Instagram publish, so the lag was under a minute rather than the three
reads and ~fifteen minutes seen daily from Sep 25 to Sep 28. Nothing was
retried in between: that endpoint has no duplicate protection, so a retry on
an apparently missing post double-posts a live page.

| | |
| --- | --- |
| `feedback-debrief-rebuild-instagram.mp4` | 1080x1920 (0.5625 exactly), 30 fps, H.264 High, CRF 19, `+faststart`, AAC 192k / 48 kHz |
| Duration | **31.17s — identical to the master**, which is the check that nothing after the splice moved |
| Loudness | −14.18 LUFS, −0.54 dBTP (master: −14.11) |

Rebuilds the Sep 30 post-event feedback debrief
([`reel/Dd6ZV5vlZTH`](https://www.instagram.com/reel/Dd6ZV5vlZTH/)), the
third-lowest-viewed Reel on the account at 20 views / 16 reach.

## The approved hook

> **Stop saying "that's how we did it last year."**

Her own line, **content bank item 8**, which the bank already records as
pairing with this Reel. **APPROVED by her on 2026-10-15** — "keep that hook
its perfect" — so it needed nothing from her and was not re-shown.

The original opened on *"Most post-event feedback gets skimmed and filed"*,
which describes the problem rather than taking a side.

## What changed, and what did not

The rules: change the hook overlay, the first frame and the opening voiceover
line; keep the rest of the edit as it was, so any movement in skip rate and
watch time belongs to the hook.

| | |
| --- | --- |
| Splice | **2.95s** |
| Why there | `silencedetect` puts the master's first gap at **2.778–3.136**, so 2.95 sits inside it and the original's opening sentence is replaced whole rather than sliced mid-word |
| New line | "Stop saying that's how we did it last year." — 2.27s, leaving ~0.68s of air before the cut |
| Opening frame | **t=31.0 of the master**: "Bottom line" and the three numbered changes |
| Everything from 2.95s | untouched, picture and sound |

Unlike Rebuild 2, "the first 3 seconds" lands naturally here — that master's
opening line ran to 4.014s and forced a 4.10 splice.

## Opening frame: the three changes, not the survey

The brief says open on the three concrete changes rather than the survey
responses, and t=31.0 is where they sit clean and high in frame:

> 1. Faster arrival + better food execution →
> 2. Right-size rooms and protect breaks →
> 3. Dedicated onsite operations/technical response.

**The hook card is placed against measured ink, not by eye.** cardkit's line
finder reports the frame's 19 text lines; the three changes occupy
**1017–1289**. The card sits at **343–617**, over the "The survey doesn't
suggest that you need to reinvent the conference" paragraph — context for the
changes, not the changes. `make_cards.py` asserts both that the card ends
before 1017 and that the changes block still starts there, so the build fails
rather than quietly covering the payoff if the frame ever moves.

Checked on `build/preview.png` before rendering, then again on the exported
frames at 0.3 / 1.2 / 2.4 / 2.9s — the card holds the whole opening beat and
is gone by 3.3s. That is the `repeatlast` class of bug the preview cannot
catch.

## The levels are the opposite problem to Rebuild 2

That master ran −21.3 LUFS and the new line was brought **down** to meet it.
This master is already at the house −14.11, and the raw line came in at
−20.04, so it goes **up by 5.93 dB**.

At +5.93 the line's true peak would be **+2.56 dBTP**, so `alimiter` catches
it — with `level=0`, or the limiter renormalises back to full scale and the
audio clips at 0.0 dBFS however low the limit is set.

The body is not re-levelled. It is already at the house figure and touching it
would change the rest of the edit, which is the one thing these rules forbid.

## Caption

`build/caption.txt`, 486 bytes. A one-line diff against the Sep 30 caption:
the first line is replaced by the new hook and nothing else moves.

The original's **"Prompt below."** is dropped — retired 2026-10-12 ("we dont
need to say prompt below its redundent"). The hashtags already carried
`#aiforeventplanners`, so the rules' swap away from `#theeventplannerai` did
not apply here.

## Ad check

The master's own notes record no in-app ad anywhere in the recording. Verified
again on **this** export rather than taken on trust: bottom 300px, from 28s at
10fps through to the final frame — **clean**, nothing but the ChatGPT input
bar and the answer text.

Worth doing: the Oct 16 FELFEL ad appeared at the very *end* of a recording,
and this piece ends on a long scroll.

## Judging it

Skip rate and average watch time at 7 days, **not views** — the account had
fewer followers in early September, so views are not comparable. Original:
20 views, 16 reach.

A new file, never a re-upload of the original: a re-upload of the same bytes
gets suppressed as a duplicate.

## A TikTok cut as well — added later the same day

The rebuild rules say Instagram and Facebook only, so this one is extra. She
asked for it after the Instagram post went out: the original went to TikTok on
**Sep 30**, so a straight repost would show that audience the same opening
twice. The rebuilt cut has a new hook, a new opening frame and a new file, so
TikTok reads it as a new video rather than a duplicate.

It changes nothing about the experiment — the rebuild is judged on the
Instagram numbers, and TikTok is a separate audience on a separate platform.

`feedback-debrief-rebuild-tiktok.mp4`, **28.90s — identical to the TikTok
master**, −14.16 LUFS.

Same shape as the Instagram build, different numbers throughout, because the
TikTok master is cut to its own pacing:

| | Instagram | TikTok |
| --- | --- | --- |
| Master length | 31.17s | 28.90s |
| First silence | 2.778–3.136 | **2.880–3.521** |
| Splice | 2.95 | **3.10** |
| Opening frame | t=31.0 | **t=28.8** |
| Three changes at | 1017–1289 | **961–1233** |
| Card centred | 480 | **425** |
| Body loudness | −14.11 | −14.10 |
| VO gain | +5.93 dB | +5.94 dB |

**Nothing was reused on assumption.** The same content sits about 56px higher
in the TikTok frame, so a card placed from the Instagram measurement would
have drifted toward the payoff. `make_cards.py` now measures both frames and
asserts each card clears its own frame's changes block, so the build fails
rather than quietly covering them.

Hook verified on the exported frames at 0.3 / 1.5 / 3.0s and gone by 3.5s.
Ad check on the export's bottom strip from 26s through to the final frame:
clean.

**Hers to upload.** Anything going to TikTok is her upload, always.
