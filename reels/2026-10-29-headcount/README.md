# 2026-10-29 — Headcount isn't an order

Thu 29 Oct's 6:30pm Instagram Reel, and **the first piece in Eryn's voice.**

## Built 2026-10-25 — both cuts

| File | |
| --- | --- |
| `headcount-tiktok.mp4` | 1080x1920, **9.30s**, 6.25 MB, -14.3 LUFS |
| `headcount-instagram.mp4` | 1080x1920, **8.20s**, 5.44 MB, -14.3 LUFS |

Pacing differs on purpose, which is the two-cuts rule rather than an accident:
the pan runs at **0.40x** on TikTok and **0.50x** on Instagram, each followed by
a freeze on the final frame. Hooks differ too — TikTok takes the command-style
"Stop giving AI just a headcount.", Instagram keeps the guide's own "150 guests.
Two completely different orders." Both cards are held for the whole clip, as the
brief specifies, at cy=520 over the plain curtain, inside the 230-1440 safe band.

## State

| | |
| --- | --- |
| Voiceover, Instagram | `build/vo/headcount-instagram-eryn.mp3` — **7.31s**, 19 words, the guide's script |
| Voiceover, TikTok | `build/vo/headcount-tiktok-eryn.mp3` — **8.52s**, 22 words, written here for the command hook |
| Voice | Eryn - Hyper Real, Conversation, Natural, Authentic (`kdnRe2koJdOK4Ovxn2DI`), model `eleven_v4`, default settings |
| Script | the guide's own, 19 words: "Same headcount, two completely different orders. Give AI the timing and who's in the room, not just a number." |
| Footage | `IMG_1005.MOV` only (Drive `15zEDUgmY7b5sTMUqcsVl4a0r3iqrTJe0`), source span **2.00-5.00s** |
| Overlay | held for the whole clip: "150 guests. Two completely different orders." |
| Length | 8-12s. IMG_1005 is a 5s spritz-bar clip, slowed to about 60% so it runs ~8s |

## Two things this piece is not

**It is not a trial.** The guide's Wed 21 block planned it as one and she
changed that on 2026-10-25: post it as a regular Reel. It never ran at all —
checked against the last 25 Instagram items on Oct 25, where the only
`is_shared_to_feed: false` post is the Oct 12 event brief — so there is no
duplicate risk and nothing to skip.

**It was never edited.** The Wed 21 block says "edited Oct 21"; there is no
build for it anywhere in this repo, so Thursday includes the edit, not just the
post.

## Footage warnings carried forward

- Use the **beverage-table** clip from Oct 7, never the coffee-station one — it
  pans onto a sponsor's banner with the logo legible.
- Check `IMG_1005` frame by frame for logos before using it.
- Check `stream_side_data=rotation` before planning any crop: her phone clips
  report 1920x1080 and decode as 1080x1920.

## Rate note

Eryn came back at **2.61 words a second** on this script, against the "about 3
a second" in her message. Short clips always read low on words-per-second
because the lead-in and tail silence are a bigger share of the file, so this is
not evidence that she is slower overall — Vanessa measured 2.92 on an 84-word
script. Measure the file, do not plan from a rate.


## Only 3 of the 5 source seconds are usable

`IMG_1005` is a 5-second pan along a drinks table, and **the first two seconds
carry a letterboard with the event's name on it.** A named sign is barred the
same way a client's name is — the Oct 19 branding rule, which is explicitly
about looking at the whole frame rather than the obvious piece. The letterboard
leaves frame at about 2.0s, so the cut starts there and runs to 5.0s.

That is the whole reason the slowdown is heavier than the brief's "about 60%":
the brief assumed all five seconds. Three seconds at 0.40x and 0.50x give 7.5s
and 6.0s of motion, and a freeze on the final frame carries each cut to length.

Also in frame and **left alone**: Aperol and prosecco bottles with legible
labels, and a printed cocktail menu. Those are products on a bar, not a client's
identity, and removing them would gut the shot.

## The optional conference clip is not used

The Wed 21 brief offers "3-4s of conference catering or coffee station b-roll
added on the end if a clean clip comes back" and calls it "a bonus, not
something Friday depends on". The beverage-table clip from Oct 7 is not in
Drive anywhere this session can find — the two cuts built from that footage on
Oct 7 were trashed, and the source appears to have come through the chat rather
than Drive. So it is left out rather than guessed at.

**Never the coffee-station clip** if it does turn up: it pans onto a sponsor's
banner with the logo legible.

## Loudness took three passes

A single open-loop gain computed from the measured `input_i` landed **-15.6 and
-15.9 LUFS**, not -14: with ten-plus dB of gain the `alimiter` at -1.0 dBTP eats
a real part of it. `render.py` now measures the export and corrects, twice,
landing both cuts at **-14.3**. It asymptotes rather than converging exactly,
which is why the loop accepts anything within 0.2 dB.

`loudnorm`'s two-pass is not used at all here, per the standing note that it
stalls short of -14 on this kind of material.

## Published

Thu 29 Oct at **6:31pm Eastern**, on her explicit go-ahead in the conversation
("yes post it"). The blanket travel-week go-ahead expired Wed 28, so this one
was asked for twice before it went: she said "great", which is feedback rather
than permission, and gave the word when asked directly.

| | |
| --- | --- |
| Instagram | media `17915583696507413`, [reel/DfGFiQTlS_o](https://www.instagram.com/reel/DfGFiQTlS_o/), 22:31:59 UTC |
| Facebook | [reel/1781480376397215](https://www.facebook.com/reel/1781480376397215/), feed id `1233196746554445_122118738753449533`, 22:32:35 UTC |
| Drive `October 29` | `12jadCalsMm4DP6J2OzDvLuHkOy3oQmzs` (instagram) and `1dzSxBsZXWzuSNiyKNTfM-6hQCDBpEdtI` (tiktok), both exact on size |

`is_shared_to_feed: true` — a regular feed Reel, which is what her Oct 25 change
asked for. Both live captions diff clean against `build/caption.txt`, line
breaks intact; the two-list structure depends on them.

**The publish call timed out at 60s on this side and the post had already gone
through.** A blind retry would have duplicated it, so the live media edge was
read first — it showed the Reel at 22:31:59, published. Treat a timeout on
`INSTAGRAM_POST_IG_USER_MEDIA_PUBLISH` as "unknown", never as "failed".

**Facebook surfaced on the first read-back**, unlike every day from Sep 25 to
Sep 28 and both Reels earlier this week, which took two or three. So the lag is
variable rather than reliable — still no reason to retry.

The TikTok cut went to her **early, at her request** ("send it now so i can do
it now"), about four hours before the Instagram slot rather than after it.
Last-10 duplicate check ran first and came back clear.
