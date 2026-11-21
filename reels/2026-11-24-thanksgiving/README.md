# Tue 24 Nov — "Thanksgiving for 20. The headcount is the easy part."

The Oct 29 food-quantities format the brief points at, which reached 248: one
overlay held for the whole clip, a short Eryn voiceover, 8–12 seconds, no
screen recording and no demo file. The 15–20 second target does not apply.

## The brief's footage did not exist, and could not

It asked her to film her own Thanksgiving prep by Sun 22 — the table being
laid, the shopping list on the counter, the oven, bags coming in. On Sat 21
she said she is **doing nothing until Thursday morning and her mother-in-law
is doing the shopping**, so there was nothing to film and no way to make
there be.

Two of the four shots looked pre-Thanksgiving — the shopping list and the
bags — which is why she was asked before the format was changed. Neither was
hers to film. The fallback was a text card in the brand look, and she offered
**old Thanksgiving footage** instead, which is better than either.

**The piece keeps its date.** It only works two days before Thanksgiving, so
moving it was never an option; only the format was in question.

## What she sent, and what is in the cut

Two clips and two stills. **None of it is in this repo** — the repo is
public, only finished cuts belong here, and `render.py` reads a scratch path
from `$TG_SRC`.

- **`pan.mov`, 2.75s** — a pan of stuffing steaming on the hob: butternut,
  celery, mushroom, onion, bread. Used 0.00–2.40.
- **`table.mov`, 5.80s** — a pan across the laid table: mac and cheese,
  creamed spinach, roast potatoes, garlic knots, an empty plate waiting.
  **Used 0.00–2.80 of it**, because a hand comes into the bottom of frame at
  about 4.75s. It was 3.80s until the vegetable tray went in.
- **the vegetable tray still**, `veg.jpg`, 1512x2016 — a sheet tray of
  roasted sweet potato, squash, cauliflower, sprouts, mushrooms and new
  potatoes on the counter. **She sent it on Sat 21 after seeing the
  three-beat cut**, full size and with no message, which is a beat to add
  rather than a question to ask. Second beat, with a 4% push that pans
  **upward** where the turkey's pans down, so the two stills are not the
  same move twice. `render.py` asserts the two directions differ.
- **the turkey still** — the platter on an autumn-leaf cloth, as the closing
  beat with a 4% push.
- the plated dinner still is not used: steak and mac and cheese reads as a
  good dinner rather than as Thanksgiving, and the piece already has a table.

**Both clips report 1920x1080 and carry `rotation=-90`**, so they decode as
1080x1920 — already the output frame, no crop. That is the Oct 7 lesson:
`stream=width,height` alone is misleading for anything shot on a phone.

**Checked frame by frame for faces: there are none**, in either clip or
either still. The only person anywhere is a hand at the end of `table.mov`,
and the cut lands before it.

**The source audio is dropped.** Both clips carry a real AAC track from her
kitchen. The rule is that the voiceover is the only audio — and it also means
nothing anyone said at that table goes out.

## The turkey came twice, and the second one is in

**The first send was 640x1136** — the compressed size, not the original — and
at 1080 wide that is a 1.69x upscale on the closing frame, soft enough to see
against two native-1080 video beats. Her own rule covers it: uploads go at
Actual/Original size. Asked for again, and the full one came back at
**1512x2016**.

That changed the filter, not just the file. The first was 9:16 already, so it
scaled straight to frame; **1512x2016 is 3:4**, and scaling that to 1080x1920
would stretch it by a third. The still is now covered and cropped like the
clips — `force_original_aspect_ratio=increase`, then the 4% push pans the
crop down over the beat. A 1:1 look at the result before and after is the
check that mattered: herb flecks and skin texture are crisp in the second.

## The prep photo that is not in it

She also sent a shot of the counter mid-prep — a dozen bowls of diced
vegetables, exactly the "professional prep" image the brief wanted. It is
**a screenshot of someone else's Instagram Story**: another account's
username and profile photo at the top, and tagged handles — including her own
personal one — burned into the bottom of the picture itself.

Both can be cropped off, and she asked for that. What survives is the
problem: the clean photo area is about **800 x 900**, so a full-bleed 9:16
crop out of it is roughly **500px wide**, upscaled past 2x. Beside two
native-1080 clips it would read as a screenshot, which is what it is.

The Nov 22 precedent — setting a landscape photo as a full-width panel on a
brand ground rather than cropping it to 9:16 — would rescue the resolution
but not the consistency: one panelled beat among three full-bleed ones.

So it is out unless the original turns up, and **on Sat 21 she said she does
not have it**. The prep shot is closed. The vegetable tray she sent minutes
later is what the fourth beat became instead, and it needed no crop at all.

## The cuts

**9.60s each**, 1080x1920, 30fps, CRF 19, AAC 192k at 48 kHz, `+faststart`,
**-14.5 LUFS**. Two cuts, never one file posted twice.

| | Instagram | TikTok |
| --- | --- | --- |
| held overlay | "Thanksgiving for 20. The headcount is the easy part." | "Thanksgiving for 20. Stop starting with the headcount." |
| pan | 2.20s | 2.00s |
| vegetable tray | 2.20s | 2.40s |
| table | 2.80s | 2.80s |
| turkey | 2.40s | 2.40s |

**The tray added one second to the piece, not two.** A fourth beat at its
natural length would have run the cut to 11s against a 6.53s voiceover, and
the extra would all have landed as silence on the final still. The first and
third beats gave the time back instead.

On this format the held overlay **is** the hook, so it is the thing that
differs: the brief's line on Instagram, a command-style one on TikTok, as the
structure rules require.

The card sits at y=1140 in the lower third, because the food is in the middle
of all four shots and the bottom 25% is TikTok's furniture. It is opaque and
it never leaves the screen, so it is composited over the whole concatenated
body rather than per beat.

**No CTA on the frame.** The caption ends on a question instead.

## Voiceover

Eryn (`kdnRe2koJdOK4Ovxn2DI`), `eleven_v4`, the brief's own 21 words:

> Twenty people isn't a shopping list. Tell it the serving time, the oven
> you've got, and who's already bringing a pie.

**6.53s**, starting at **1.20s** so it ends at 7.73s and the turkey holds
1.87s after it — 0.90s and 1.17s before the tray went in. A freeze on the
last frame is fine; a long silent tail is not, and `render.py` now asserts
the tail stays under two seconds rather than leaving it to judgement.

Measured in at -22.5 LUFS, true peak -2.1 — a crest factor of 20.4 dB, so the
gain was swept rather than computed: +8.5 landed at -15.4, +10.0 at -14.4,
+11.0 at -13.8. **+10.7 dB** into `alimiter=limit=0.891:level=0` measures
-13.9, and the export measures -14.5 over the longer cut.

## Caption

No `AI Prompt:` block — there is no prompt in this piece, the same as Oct 29.
