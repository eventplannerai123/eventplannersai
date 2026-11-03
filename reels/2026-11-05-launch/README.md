# Thu 5 Nov — Vendor Payment System launch Reel

`launch-instagram.mp4` and `launch-tiktok.mp4`, both 1080x1920, 30fps, 21.9s,
H.264 high CRF 19 +faststart, AAC 192k at 48 kHz, audio measured at
**-13.96 LUFS / -1.27 dBTP** on the finished export.

The piece the $24 Vendor Payment System launches on. It went live on Gumroad a
day early, Tue 3: <https://aiforeventplanners.gumroad.com/l/epbvxs>.

## It runs 21.9s, not 15-20

The October default is 15-20s and a day's brief overrides it. This brief asks
for five things — the filled tracker as the payoff, the prompt, the answer, a
cut to the contract reader, and the end card — and the voiceover the block
specifies is 69 words, which is 21.9s in Eryn at 3.1 w/s. The alternative was
cutting a beat the block names. Time to payoff is 0s, so the six-second ceiling
is not in play.

## Four recordings, and why the answer comes from the second

| Take | Length | Used for |
| --- | --- | --- |
| 9:20 inbox sweep | 60.7s | **its opening two seconds only** |
| 9:35 inbox sweep | 49.4s | the answer |
| 9:51 tracker | 44.1s | the payoff and the amounts |
| 9:57 contract reader | 72.7s | the "10 business days" row |

**The first take's answer is not used, and the reason is the whole point of the
piece.** It put a card on screen reading `$59,180` still unpaid and `$72,480`
scheduled. Rebuilding all 17 payments from the eight vendor emails and summing
them in code gives **$46,080 and $59,380** — it was $13,100 over on both, about
the paid deposits counted a second time. The paid figure ($13,300) and the
entry count (17) were right, which is exactly what makes a wrong total
convincing. The tracker's own formulas agree with the code.

Her Prompt 1 now ends **"Don't add up totals; the tracker does the math."**

The second take has no totals card at all, lists all five near-term dates, and
says outright that it left the event-relative deadlines for the tracker to
calculate. It starts after the send tap, though — so the opening comes from the
first take, which has the prompt sitting in the input box and the tap on
camera. Same prompt, and the status bar crops off, so the join is invisible.

## Her three notes of Nov 3

**"Open on Vendor | Amount | Due date | Flag together."** Those four do not fit
across her phone in portrait. Hiding every other column on the tracker copy and
narrowing the four was not enough — two takes both pan rather than showing them
at once. She turned the phone sideways, which fits them, so `make_four.py`
rotates that take back with `transpose=2` and lifts the table out of it. The
result is a wide band rather than a full frame, which is what a four-column
table looks like at 1080 across; it sits on a blurred copy of its own frame.

**"Contract shot: zoom on the quote and May 3, 2027, overlay above the text."**
A straight crop cannot zoom this. The clause is three full-width lines of a
letter page on a phone, so a crop tight enough to enlarge the type clips the
line ends, and one wide enough to keep them is barely a magnification.
`make_clause.py` uses the house technique instead — isolate rather than
magnify: the Payment Schedule paragraph goes on its own panel over a hard blur,
ending "...no later than ten (10) business days before the event date", and the
table row carrying **May 3, 2027** in bold follows as its own beat. The card
moved to y=494, clear above the panel at y=840.

**"End on the tracker, not the keyboard."** The last beat is the same
four-column band, scrolled to the tail, with the Comment BUDGET card under it.

## The voiceover changed by one lineIt said "the ones coming up in the
next thirty days turn red". The tracker's conditional formatting colours only
three states — `Paid` green, `Due this week` amber, `Overdue` red — and on Nov 5
the nearest payment is nine days out, so nothing is amber or red. It now reads
"get flagged", which is what the Flag column actually says.

## The tracker was filled from here

`Vendor Payment Tracker — May 15, 2027 wedding` in Drive `November 5`, a copy
of the product tracker carrying all 17 payments. The block asks for the table
to be pasted in during the recording; pasting a 15-column table into Sheets on
a phone lands as one squashed column as often as not, and the cut is vertical
so she films on the phone. See `build/tracker.md`.

## The caption carries no prompt, deliberately

Every other caption ends with the prompt so the post stands without the video.
Here the six prompts **are** the product, so Prompt 1 stays out — and the
guide's own Thu 5 caption leaves it out too. See `build/caption.md`.

`Comment BUDGET` returns for this launch after being retired across nine failed
keywords, because this time a ManyChat auto-reply sends the Gumroad link back.
The TikTok caption points that CTA at Instagram, where the auto-reply lives.

## Build

    python3 make_beats.py     # six frames out of her four recordings
    python3 make_cards.py     # hook, contract and end cards
    python3 render.py         # preview, then both cuts

`make_beats.py` reads the recordings from `$LAUNCH_SRC` — **her footage never
enters this repo**, so only the finished cuts are committed. Every seek is an
accurate one (`-ss` after `-i`): fast seek snaps to a keyframe, and on 60fps
screen recordings that chose the wrong moment for three of the first seven
frames, one of which cut the dollar figures in half.

`render.py`'s `preview()` composites each card onto its own beat before any
export, and the export itself was re-checked frame by frame — the hook is gone
by 2.5s, which is the `repeatlast` bug the rules warn about.
