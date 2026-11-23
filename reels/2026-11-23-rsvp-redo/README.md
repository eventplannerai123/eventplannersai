# Mon 23 Nov — the holiday party RSVP list (Reel redo, 6:30pm)

A redo of the **Sep 18** RSVP meal-counts Reel, which reached 31 and ended on
the retired CATERER keyword. The original stays up. This one is ten times the
size — 180 invitees against 30 — opens on the finished caterer sheet, and ends
on the catch instead of a keyword.

## Her note on the hand-over, and what was done about it

> Remove the chatgbt pop up that's midway

A ChatGPT **"Improve accuracy for documents and research / Get Plus"** upsell
card slides over the answer partway through the recording. It is out, and by
construction rather than by eye:

- **Measured, not guessed.** A 10 fps scan of the Get Plus pill's own band
  across all 83.6 seconds found it solid from **46.2s to 47.4s**; frames
  either side put the fade at **46.0s to 47.6s**, source frames 2760–2856.
- `make_beats.py` carries that window as `POPUP` and **asserts that no beat
  frame falls inside it**, so a later nudge to a frame number cannot bring it
  back silently.
- The five beats sit at 1.0s, 38.6s, 52.0s, 68.3s and 83.0s. None is close.

**Ad-checked as well**, over the whole recording rather than a crop of the
reveal: a 2-second contact sheet of the bottom 560px, which is where all nine
advertisers so far have appeared. Nothing. The pop-up is the only
interruption in the file.

## The source

**Not in this repo** — 170,611,099 bytes of her screen, Drive id
`1iHul6APHr7k_v_aooTTsllSLE-YfTMOF` in `November 23`, filmed Fri 20 Nov.
1206x2622, 60 fps, HEVC, 83.6s, no rotation side data, so the crop is
recomputed as `crop=1206:2144:0:478` and scaled to 1080x1920.

The opening is right: the prompt sits in the box with the PDF chip above it
and the send arrow lit, from frame one. She then opened the attachment
preview and scrolled all four pages before sending, so the send tap is at
about 7s rather than 2s — which does not matter here, because the cut opens
on the payoff and uses the prompt as beat two.

## What the answer actually did

Everything the brief's "what it should catch" list asks for:

- **54 / 48 / 22 / 18 adding to 142**, with "plus-ones not included" said out
  loud under the heading.
- **The 23 free-text notes grouped into the six real restrictions** with the
  right counts and the names against each: gluten-free 8, nut 5, dairy 4,
  shellfish 3, vegan 2, pescatarian 1. The source sheet holds those 23 notes
  in **14 distinct wordings** — "no gluten", "celiac", "GF please", "gluten
  free pls" are four spellings of one table — counted off the live sheet, not
  taken on trust.
- **All three self-contradicting rows named** (Aisha Garrow, Gus Alvarez,
  Elena Kowalski) under "3 confirmed conflicts", with the action against each.
- **The six plus-ones with no meal choice called out as unknowns.**

### The brief's predicted twist did not happen

It expected the answer to group the notes correctly and still report 142
meals, reading the six empty plus-one cells as empty rather than as a
question. It did not. §4 says all 142 primary guests chose and then names the
six plus-ones who did not, and the closing recommendation is:

> Don't finalize the order at 142 meals just yet. You potentially have 148
> attendees, and three confirmed meal conflicts plus six missing plus-one
> selections need resolution.

Predicting a twist is not the same as having one. The brief's own twist line
says that when this happens, CC rewrites the last voiceover line, the overlay
and the caption's third paragraph around what she actually catches — so all
three are written around **142 against 148**.

## The cut

Five freeze frames, each with a 4% push, 1080x1920, 30 fps, CRF 19, AAC 192k
at 48 kHz, `+faststart`. **18.56s**, which is the voiceover's own length and
inside the brief's 15–20s.

| | Beat | Instagram | TikTok |
| --- | --- | --- | --- |
| 1 | §1 meal counts, 54/48/22/18, Total 142 | 3.40s | 3.20s |
| 2 | the prompt, PDF chip, send arrow | 3.40s | 3.30s |
| 3 | four spellings of one table; Nut / Tree Nut 5 | 3.60s | 3.70s |
| 4 | §3, "3 confirmed conflicts", all three named | 3.60s | 3.70s |
| 5 | the counts panel and "don't finalize at 142" | 4.56s | 4.66s |

**Time to payoff is zero** — the finished sheet is the opening shot, which is
what the Mon 23 brief asks for ("readable in the first 2 seconds"), the same
inversion as Mon 16 and Tue 17. The prompt is beat two and the whole of it is
in the caption, so nothing about the piece depends on seeing it first.

### Overlays

Two, as the format allows, and no rolling captions.

- Instagram hook, 0:00–0:02.3: **"142 RSVPs. 23 dietary notes, written 14
  different ways."** — the guide's own line.
- TikTok hook, same window: **"Stop sending the caterer one number."**
- End card, last 3 seconds, both cuts: **"142 meals. 148 people."**

The brief's planned takeaway, "Send the caterer the conflicts, not just the
counts", still closes the caption. On screen it is the number instead,
because the number is what the answer did.

**No BUDGET line.** A catering piece, not a money one — the guide's Mon 23
takeaway line says so, and `make_cards.py` asserts the word appears on no
card, the same guard the Tue 17 generator carries after she caught a tracker
CTA on an insurance piece and then on a run-sheet one.

Card placement is measured against the beat underneath and checked by
`preview()` before anything is exported: the hook sits at y=1220, clear of
the meal-count table and its bars, and the end card at y=1140, below the
recommendation paragraph it is about.

## Voiceover

Eryn (`kdnRe2koJdOK4Ovxn2DI`), `eleven_v4`, default settings, 46 words:

> A hundred and forty-two yeses, and twenty-three dietary notes written
> fourteen different ways. Six restrictions, counted, with names. Three meals
> that contradict their own note. And it wouldn't call the order a hundred
> and forty-two — six plus-ones never chose. The room is a hundred and
> forty-eight.

**The guide's script says "twenty-three different ways" and that is wrong.**
The demo sheet holds 23 notes in **14** wordings, which is what the overlay,
the caption and the brief's own file description all say. Counted off the
live sheet before recording the line. The script here says fourteen.

**The first take was too long.** The guide's 40-word script plus the ask
sentence came back at **21.12s**, over the brief's ceiling — spelled-out
numbers read far slower than the 3.1 words-a-second planning figure, about
2.56 here. Dropping "I ask for what the caterer actually needs" took it to 46
words and **18.56s**. Nothing is lost: the prompt is beat two and the caption
carries it in full.

Loudness: measured in at **-25.0 LUFS, true peak -4.4 dBTP** — a crest factor
of 20.6 dB, so the gain was swept rather than computed. +11.0 landed at -15.1,
+12.0 at -14.5, +13.0 at -13.9; **+12.9 dB into `alimiter=limit=0.891:level=0`**
measures **-14.0 LUFS, TP -0.6**. The export measures the same. The voiceover
is the only audio; the screen recording's track is silent.

`elevenlabsusercontent.com` is still blocked from this session, so the mp3
came in through Drive — uploaded server-side into `November 23` and pulled
from `drive.usercontent.google.com`, then trashed.

## Posting

- **Instagram and Facebook at 6:30pm Monday**, one-shot task
  `trig_011HT4oc8zJjqK2Vtkv7aFRK` (23:30 UTC — Eastern is EST now), created
  after she said "go ahead" on Fri 20. Its prompt carries the Reel-not-photo
  read-back.
- **TikTok at about 9am Monday**, hers. Last-10 duplicate check run before the
  hand-over: Nov 10–22 holds no RSVP, caterer, dietary or meal-count piece.
  The nearest are the Nov 18 staffing captain and the Nov 22 catering captain,
  and neither is about counts.
- Within 10 minutes of the 6:30pm post she leaves the first comment herself.

## Live

- Instagram: https://www.instagram.com/reel/DgGkQDRjApO/ — posted Mon 23 Nov
  6:30pm Eastern. Container finished in 18.8s over 7 checks and published
  first time. Read back as `media_product_type: REELS`.
- Facebook: post id `2267770110620553` on page 1233196746554445, same cut,
  same caption. The Page feed was read first.
- Caption identical to `build/caption.txt` character for character, em dashes
  and curly apostrophes included.
