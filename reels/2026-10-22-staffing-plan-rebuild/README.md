# Staffing plan rebuild (Rebuild 4) — 2026-10-22

Status: **published 2026-10-22** at 6:31pm ET on her go-ahead ("Approved"),
the day's second post. The TikTok cut is hers.

| Account | Post |
| --- | --- |
| Instagram `@aiforeventplanners` | https://www.instagram.com/reel/De0D7FxiMX-/ |
| Facebook "The Event Planners AI" | https://www.facebook.com/reel/1583887796316110/ |

Instagram media `18133295842786706`, `media_product_type: REELS`,
**`is_shared_to_feed: true`** — a regular feed Reel, which is what a rebuild
must be. Container finished in 25.0s over 7 checks.

**All three captions hash identically**: `build/caption.txt`, the live Instagram
caption and the live Facebook message are all 538 characters,
sha256 `d25a731fe286128690347d3b78e13707f9a8ba8b119bb29ff3fc541a37342ba5`.

**Facebook surfaced on the second read-back**, feed entry
`1233196746554445_122117132559449533` at 22:32:19 UTC — 34 seconds after the
Instagram publish. Nothing was retried in between.

Before posting: the raw URL returned 200 at exactly the committed byte count
(12,071,315), and both duplicate checks came back clean, the newest entry on
each being the setup-times carousel from that morning.

Rebuilds the Sep 26 conference agenda → staffing plan Reel
([`reel/DdwGGoXk0u1`](https://www.instagram.com/reel/DdwGGoXk0u1/)): 23 views,
20 reach, **80% skip rate** — the worst remaining hook on the account, which is
what makes it the right rebuild, because a hook rebuild can only fix the
opening.

**This is a regular Reel, not a trial** (changed Oct 16). The original went out
as a regular Reel, and the same piece posted both ways trips Instagram's
duplicate detection and throttles both for up to 30 days.

## The approved hook

> **Four staff, six sessions, one block you're short.**

**APPROVED by her on 2026-10-16** ("a is good"). The old hook was "Six sessions.
Three rooms. Four staff." — three numbers and no stake. The new one leads with
what the output actually delivers: the prompt ends "flag any block where we're
short", and the answer's verdict is "staffable with four people, but—".

## What changed, and what did not

The rules: change the hook overlay, the first frame and the opening voiceover
line; keep the rest of the edit as it was, so any movement in skip rate and
watch time belongs to the hook.

| | |
| --- | --- |
| Splice | **3.70s** (Instagram), **3.78s** (TikTok) |
| Why there | the new line runs 3.46s, so the master's first gap (1.998–2.328) cannot hold it. 3.70 sits inside the second gap, 3.501–3.913 |
| What that costs | the master's first **two** sentences are replaced, not one — the same compromise Rebuild 2 made at 4.10 |
| Opening frame | the master's own **t=0.000** |
| Everything from the splice | untouched, picture and sound |
| Duration | **807 frames, same as the master.** The container reads 26.92s against 26.90 — 0.02s of audio padding, under one frame of video |
| Payoff | still **5.80s**, because the splice replaces rather than inserts |

## Frame zero is the only clean frame

The opening has to show the prompt in the box (video rule 2: never cut the
prompt), and the master's first 1.8s is exactly that. But **the old hook card is
burned into it** — it fades in over 0.20s from t=0, so every frame in that range
carries it except one. At exactly t=0.000 the card's alpha is still zero, so
frame zero is clean: the prompt, the agenda PDF attached, the send button live.
That is the still the new beat freezes on.

**The new card sits at y=1300, over the keyboard, not at the old y=620.** At 620
it would cover the prompt text, which is the one thing this opening exists to
show — the Sep 29 mistake recorded in CLAUDE.md. It clears the top 12% and
bottom 25% safe zones, and `make_cards.py` asserts both rather than trusting the
number typed here.

## The line is sped 8%

Vanessa reads it in 3.74s flat, which would need a 3.85 splice and a longer
freeze. At `atempo=1.08` it is 3.46s and lands snappier, which suits a hook.
Pitch is preserved. Two takes were generated; the first was used.

## A stereo master made concat quietly clip the body

Worth recording, because the filtergraph names no gain anywhere and the overall
loudness barely moved.

The Oct 17 rebuild's master was **mono**. This one is **stereo**, so `concat`
matched the layouts by downmixing the body to mono — which sums L+R and brought
the untouched body from **−1.36 dB peak to +1.40**, i.e. clipping, in a section
the rules say must not be touched at all. The whole-file LUFS moved from −14.06
to −14.70 and hid it.

The fix is an explicit `aformat=...:channel_layouts=stereo` on **both** branches.
The check that catches it is measuring **the body of the export against the body
of the master**, not the export as a whole.

| | master | rebuild |
| --- | --- | --- |
| Body RMS, 4–26s | −18.37 dB | −18.38 dB |
| Body peak, from 4s | −1.36 dB | −1.14 dB |
| Whole file | −14.06 LUFS, −1.34 dBTP | −14.25 LUFS, −1.14 dBTP |

The new beat sits at −18.73 dB RMS against the body's −18.38 — within 0.35 dB,
so the hook is neither buried nor shouted.

## Checks

- 1080x1920, ratio 0.5625 exactly, 30 fps, H.264 High, CRF 19, `+faststart`,
  AAC 192k / 48 kHz, **stereo**.
- 807 video frames, identical to the master.
- Hook verified on **exported** frames at 0.00 / 1.50 / 3.50s, gone by 3.69,
  and the splice hands over cleanly to the agenda at 3.80s. That is the
  `repeatlast` class of bug, which only the export shows.
- The old hook card appears nowhere in either export.
- The payoff is on screen at 5.80s, as in the master.
- No ad check needed: nothing new was pulled from the source recordings.

## Caption

`build/caption.txt`. The new hook is the first line, the original AI prompt is
kept whole, and the retired "The full prompt is in the caption below." has been
dropped. Four literal `#`, no "Hashtags:" label.

## Who posts what

| | |
| --- | --- |
| Instagram + Facebook | from here, 6:30pm, after her go-ahead |
| TikTok | **hers**, `staffing-plan-rebuild-tiktok.mp4` |
