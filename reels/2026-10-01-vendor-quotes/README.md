# Vendor quotes reel — 2026-10-01

Status: **source files built, nothing recorded yet.**

First piece of the October plan, and the first Instagram day under the new
three-a-week cadence (Mon/Wed/Fri, plus this Thursday to start). Target
15-20s, like everything from Oct 1.

## What is here

`source/` holds three AV quotes for the same 200-person conference and an
answer key. They are built, not real — the author's own "still to build" list
named them, the way the Sep 23 catering invoice was built with deliberate
errors and an answer key.

| File | Quoted on the page | Real cost for this event |
| --- | --- | --- |
| `quote_meridian.pdf` | $6,799.50 | **$17,175.58** |
| `quote_clearline.pdf` | $8,700.00 | **$10,403.01** |
| `quote_stagecraft.pdf` | $12,400.00 | **$18,471.62** |

**Headline order:** Meridian < Clearline < Stagecraft.
**Real order:** Clearline < Meridian < Stagecraft.

So the cheapest-looking quote is $10,376 more expensive than the one that
actually wins, and the "all inclusive" one is the worst of the three. Both
of the tempting answers are wrong and the unglamorous middle quote is right,
which is a better lesson than a single gotcha.

## How each one hides cost

- **Meridian** — a genuine equipment-rental quote being read as a full quote.
  The headline covers the ballroom only: no breakout rooms, no labor, no
  power, no rigging, no tax. The 22% service charge then recalculates upward
  once the breakout equipment is added, which is the detail most likely to be
  missed.
- **Clearline** — nearly complete, and its only real gap is overtime: load-in
  06:00 to strike 19:00 is 13 hours against the 10 included. Its other two
  exclusions are deliberately *not* hidden costs — the recording package and
  the declinable damage waiver are not needed for this event. That is the
  test of whether the model separates "excluded" from "required", rather than
  adding up every number it sees.
- **Stagecraft** — "all inclusive" is the trap. A 20% coordination fee and a
  non-declinable 5% damage waiver both compound on top of the add-ons, and
  the included projector is 5,000 lumens, under-spec for a 200-person
  ballroom with house lights up, so that upgrade is not optional either.

## The answer key is generated, not written

`source/build_quotes.py` holds the line items once and renders both the PDFs
and `source/ANSWER-KEY.md` from them, so the key cannot drift from the
documents. Re-run it to change a number. Sales tax is 8.875% throughout.

Worth keeping: `reportlab` is not installed in a fresh container and
LibreOffice's HTML import fails here ("source file could not be loaded"),
so the PDFs come from `pip install reportlab` and reportlab's platypus,
not from an HTML conversion.

## Still needed before this can be cut

1. The screen recording — paste the plan's prompt into ChatGPT with all three
   PDFs attached. **Start recording with the prompt already in the box and
   the send tap on camera**; the Sep 29 build threw away a correct opening by
   assuming it was missing.
2. Aim for ~25s of raw footage, and check the reveal for in-app ads before
   the cut is finalised. Five different advertisers turned up in five days.

## From the plan

- Hook overlay 0:00-0:02: "Three quotes. None of them comparable."
- Voiceover: "Three AV quotes for the same job, and not one of them lists the
  same things. Here's all three side by side on what's actually comparable,
  and where each one is hiding the cost."
- Caption: Three quotes for the same job, none of them comparable. Here's what
  each one actually includes once the extras are added. Prompt below.
- Hashtags: `#aiforeventplanners #corporateevents #eventprofs #eventplanningtips`
- TikTok cut is a manual upload, as always. Note the plan holds the TikTok
  version of this piece back to **Tue 13 Oct**, rather than running it the
  same day.
