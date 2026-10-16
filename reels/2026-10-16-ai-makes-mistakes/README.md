# 2026-10-16 — AI makes mistakes, just like us

Status: **published 2026-10-16** at 9:15am ET by the scheduled task, on her
Oct 16 approval ("approved"). TikTok went up by her hand the same day
("tik tok posted").

| Account | Post |
| --- | --- |
| Instagram `@aiforeventplanners` | https://www.instagram.com/reel/Dejnfc_ilLR/ |
| Facebook "The Event Planners AI" | https://www.facebook.com/reel/1546513110527670/ |

Instagram media id `18020923679941031`, `is_shared_to_feed: true` — a regular
feed Reel, not a trial. Container processing took 25.4s over 9 status checks.

The live Instagram caption was read back and diffed against
`build/caption.txt`: **identical**. Before posting, the raw URL was fetched and
its md5 compared to the committed file — `f886e393adf7da2e420b4a0b4c8b102d` on
both, 6,786,104 bytes — and both duplicate checks were run and came back clean
(`INSTAGRAM_GET_IG_USER_MEDIA` and `FACEBOOK_GET_PAGE_POSTS`, newest entry on
each being the Oct 15 annoyed-email piece).

## Posted in the morning, not the evening

It was scheduled for 6:30pm as day 1 of the morning-vs-evening test, and moved
to 9:10am on the morning itself. Her instruction: "i think we should only test
the 6:30 time when 2 posts are scheduled that day", and "in general we know
that 9am is optimal or early morning". Today carries one Instagram post, so it
is a morning post.

That rule also **ends the posting-time test unrun** — the pre-registration
excluded second posts, so an evening slot that only ever carries a second post
can never fill its arm. Closed in
[`docs/POSTING-TIME-TEST.md`](../../docs/POSTING-TIME-TEST.md) with the
reasoning; this piece is therefore not test data.

Facebook surfaced in the page feed on the **first** read-back, which is faster
than the three reads and ~15 minutes seen every day from Sep 25 to Sep 28. Feed
entry `1233196746554445_122116127379449533`; the live message was compared to
`build/caption.txt` and matches. Nothing was retried.

Fired 13:10 UTC, Instagram published 13:15:28 UTC, Facebook 13:16:03 UTC.

| | |
| --- | --- |
| TikTok | `ai-makes-mistakes-tiktok.mp4` — 15.30s, −14.2 LUFS |
| Instagram / Facebook | `ai-makes-mistakes-instagram.mp4` — 16.60s, −14.2 LUFS |

1080x1920 (0.5625 exactly), 30 fps, H.264 High, CRF 19, `+faststart`, AAC 192k
at 48 kHz. Both inside the brief's 15–20s.

## The piece

The build-story format, which is what this day exists to test — the coloring
book build story reached 79 against a weekly average of 29, and this piece asks
whether that repeats. **Not a demo: no ChatGPT prompt anywhere**, which the
brief states outright, so the caption carries no `AI Prompt:` block either.

Content bank item 10, her own rule: she has not stopped using AI for anything
and checks everything it does, because it makes mistakes just like people do —
and the one thing it cannot be trusted with is VIP seating, because it has no
way of knowing which two executives can't sit together or who reports to whom.

## Three clips, one per sentence

Cut to the voiceover's own pauses, measured with `silencedetect` rather than
guessed.

| | Clip | Sentence |
| --- | --- | --- |
| 1 | the seating chart | "AI will never get VIP seating right on its own" |
| 2 | a name being moved | "it doesn't know which two executives can't sit together, or who reports to whom" |
| 3 | the wide of her desk | "I use it for most of the paperwork, and I check everything it gives me" |

**The desk wide is the close, not the opening.** Opening on a desk whose
screens show nothing is the Oct 7 mistake, where generic footage was rejected
with "No this isn't good content." The artefact goes first, the correction
second, and the pull-back to her real workspace lands on the honest line.

## Clip 2 is offset, and it matters

Taken from **1.5s in** (1.8s on the TikTok cut), not from its start. The move
happens late: Tom Becker's row is selected around t=3, he leaves the head table
at t=4–5, and **Jack Turner is sitting in the Board Chair seat from t=5 on**.
Starting at zero would have spent the whole beat on the before state and cut
away exactly as the chart changed.

Verified on the exported frames: at 4.2s Tom Becker is in the seat, at 6.0s his
cell is picked up, at 8.0s the seat is empty, at 8.9s Jack Turner is in it —
while the voiceover is saying AI doesn't know who reports to whom.

## No crop, and the rotation handled itself

All three sources are already **1080x1920**, so there was nothing to compute.
The desk clip is 60fps HEVC carrying `rotation=-90`; ffmpeg applies that on
decode and `fps=30` drops the rate. **Its real room audio is never mapped** —
the voiceover is the only sound.

Motion was checked rather than assumed: the chart clip looks static but drifts
steadily (frame difference 3.0 → 10.7 over four seconds), so it is scrolling
gently and satisfies "footage in motion from frame one". No camera move was
added to fake it.

## Overlays

One hook card per cut, no end card.

| Cut | Hook | Position |
| --- | --- | --- |
| Instagram | "AI doesn't know which two execs can't sit together." (guide verbatim) | y 1148–1352 |
| TikTok | "Stop letting AI do your VIP seating." (command-style, per the two-cuts rule) | y 1148–1352 |

Placed **below the head table**, which runs y 380–990 and holds the very people
the line is about — CEO, CFO, Board Chair. They stay readable behind the card.
Inside the Oct 5 safe band, asserted in `build/make_cards.py`, checked on
`build/preview.png` before rendering, and confirmed on the exported frames:
present at 0.5s and 2.5s, gone by 3.5s.

## Nothing identifying in frame

No faces, no documents, no handwriting, no client or company names. The chart
is the demo *Seating Chart — Leadership Dinner* — invented names, and its own
header says so. The desk shot carries incidental consumer hardware branding
only.

**Worth her knowing:** both screens in the desk wide show the Windows desktop,
not a seating chart. The brief asked for "a wide of your desk (screen plus
what's around it)", so it is the shot that was requested — but if she wants the
chart up on screen in it, that is a two-minute reshoot.

## Voiceovers

ElevenLabs, Vanessa - Beach Girl (`8DzKSPdgEQPaK5vKG0Rs`),
`eleven_multilingual_v2`.

- **Instagram** — the guide's script verbatim, 47 words, 16.21s.
- **TikTok** — same script with the opening line swapped for the command hook,
  14.21s.

Measured first pass (−21.9 / −21.6 LUFS), explicit gain, `alimiter` with
`level=0` at −1.0 dB. `TRIM` is **1.75**, carried over from the Oct 15 build
where 1.10 landed 0.8 dB low. Finished files measure **−14.18 and −14.15**.

## Caption

`build/caption.txt`, the guide's wording verbatim. It carries **no prompt
block**, because the piece is not a demo, and no "Prompt below." line.
