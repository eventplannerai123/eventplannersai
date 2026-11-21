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
  **Used 0.00–3.80 of it**, because a hand comes into the bottom of frame at
  about 4.75s.
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

## The one thing worth re-sending

**The turkey still arrived at 640x1136.** That is a compressed send, not the
original, and at 1080 wide it is upscaled 1.69x — soft enough to see against
the two video beats, which are native 1080. It is the closing frame, so it is
the worst place for it. Her Sep rule covers exactly this: uploads go at
Actual/Original size. Asked for again; the cut is built with what is here and
takes a drop-in replacement without any other change.

## The cuts

**8.60s each**, 1080x1920, 30fps, CRF 19, AAC 192k at 48 kHz, `+faststart`,
**-14.3 LUFS**. Two cuts, never one file posted twice.

| | Instagram | TikTok |
| --- | --- | --- |
| held overlay | "Thanksgiving for 20. The headcount is the easy part." | "Thanksgiving for 20. Stop starting with the headcount." |
| pan | 2.40s | 2.20s |
| table | 3.80s | 4.00s |
| turkey | 2.40s | 2.40s |

On this format the held overlay **is** the hook, so it is the thing that
differs: the brief's line on Instagram, a command-style one on TikTok, as the
structure rules require.

The card sits at y=1140 in the lower third, because the food is in the middle
of all three shots and the bottom 25% is TikTok's furniture. It is opaque and
it never leaves the screen, so it was composited onto all three beats before
anything was exported.

**No CTA on the frame.** The caption ends on a question instead.

## Voiceover

Eryn (`kdnRe2koJdOK4Ovxn2DI`), `eleven_v4`, the brief's own 21 words:

> Twenty people isn't a shopping list. Tell it the serving time, the oven
> you've got, and who's already bringing a pie.

**6.53s**, starting at 0.90s so it ends at 7.43s and the turkey holds for
just over a second after it. A freeze on the last frame is fine; a long
silent tail is not, and 1.2s is not one.

Measured in at -22.5 LUFS, true peak -2.1 — a crest factor of 20.4 dB, so the
gain was swept rather than computed: +8.5 landed at -15.4, +10.0 at -14.4,
+11.0 at -13.8. **+10.7 dB** into `alimiter=limit=0.891:level=0` measures
-13.9, and the export measures -14.3.

## Caption

No `AI Prompt:` block — there is no prompt in this piece, the same as Oct 29.
