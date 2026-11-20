# The coloring book's first three reviews (slide Reel + TikTok carousel)

Built Fri 20 Nov from the three reviews Sahiba sent that afternoon, after the
Fri 20 block's YOU line asked her to check the listing. Her line: "3 reviewas",
then the paste.

**Thu 26 Nov, 6:30pm**, one-shot task `trig_019SGEKTiU2mZfqL65pRArpD` (23:30 UTC under EST), her decision on Fri 20 ("yes"). The guide's Fri 20 CC
line said to propose a date at the Sun 22 recap; she settled it two days
early, in the same sitting as approving the slides. The Thanksgiving calendar
piece that held the slot (content bank 36) is unscheduled and goes back in the
pool for December — noted on the Thu 26 calendar line in the guide, as an
addition rather than an edit to her own words.

## The reviews, and why three was the threshold

Three five-star verified purchases: **Pamela M.** (Oct 22), **Christina N.**
(Oct 4) and **Rose R.** (Oct 3). All three predate the ask by weeks, which is
the thing the brief was worried about: "two reviews a few days after asking
reads as solicited, which would make the piece worse than not posting it."

**amazon.com is blocked from this session**, so these are her paste and
nothing else. `make_slides.py` holds each quote twice — once in the slide and
once in `check()` — and asserts the two match, so a quote cannot drift into a
paraphrase of a stranger's words without the build failing.

**Names are first name and last initial**, the guide's own rule, and the check
refuses anything longer. The real surnames are on the public listing; they are
not ours to put on a slide.

## The slides

Five, 1080x1920, brand look — lavender #CECBF6, deep purple #3C3489, Poppins,
numbered badge, EP + star wordmark, bottom bar.

1. "Three strangers reviewed my coloring book." / all five stars, verified
2. Pamela M. — "So cute!"
3. Christina N. — "So cute! 100% would recommend."
4. Rose R. — "Perfect gift"
5. "Two copies are up for grabs until Friday."

Each review slide carries its title as the headline and its body as the quote,
both the reviewer's own words.

**Poppins has no glyph at U+2605**, the same trap as the wordmark's star at
U+2726: a literal "★★★★★" renders five tofu boxes. The star rows are drawn as
polygons, five-pointed, inner radius 0.382 of the outer.

## Why Thursday, and not another day

**The closing slide has a deadline in it.** "Two copies are up for grabs until
Friday" is true only while the Nov 20 giveaway is open, and it closes **Fri 27
Nov at 11:59pm Eastern**. So the piece only works Mon 23 to Thu 26 — and Mon
23 is the RSVP redo, Tue 24 Thanksgiving-for-20 and Wed 25 the consulting
carousel. Thu 26 was the only slot left, and the piece that held it has no
deadline on it, which is why that one moved rather than this one.

It also sits a day before Fri 27's coloring book Reel and the last day of the
giveaway, so the two run together rather than competing.

## The Reel

**18.00s**, 1080x1920, 30fps, CRF 19, AAC 192k at 48 kHz, `+faststart`. Hard
cuts, no push — typeset brand slides, not screenshots of a scrolling answer.

**The slides are not all the same length, and slide 3 is why.** Christina N.'s
review runs 37 words on top of a two-line headline, roughly twice what any
other slide asks anyone to read, so it gets 4.80s against 3.20s for the
one-line ones. Nothing is under the 3.00s she set on Nov 17 ("slow down the
reel a little"), and `render.py` asserts it.

**No voiceover, deliberately.** Three of the five slides are other people's
words, and having Eryn read a stranger's Amazon review in the first person is
the one thing this piece must not do. So it is overlay-led — which the Oct 5
rule 1 allows — and the bed is what keeps it from going out silent, her Nov 10
instruction in four words: "dont go out silent".

### The bed

Marimba and plucked nylon guitar over a light clap pulse and a soft bass,
upbeat per her Nov 10 instruction, its own generation.

**The first one was unusable and the measurement caught it.** It came back 20
seconds long but the groove stopped at 15.5s and rang away to nothing:
mean volume -18.5 dB at 15s, -30.7 at 16s, -42.4 at 17s, silence by 19. An
18-second cut would have ended on two and a half seconds of near-silence under
the closing slide. Regenerated at 30 seconds with the ending written out of
the prompt — "no final chord, no ritardando, no section where the arrangement
thins out or rings away" — and the second one holds -14.8 to -16.3 dB from the
first second to the last. **Measure the tail before trimming, not after.**

Instrumental, checked both ways: the spectrogram shows even texture end to end
with the regular vertical transients of a pulse and none of the sliding
formant bands a sung vowel makes, and Scribe returned an empty string. The
generation's own settings say "Instrumental: False" either way, so they are
not the check.

Trimmed 0.0-18.0s, 0.8s fade in, 1.2s fade out, **+0.1 dB** into
`alimiter=limit=0.891:level=0` — this one came out of the model almost exactly
right, where Friday's needed +4.05 and Sunday's -0.55. The export measures
-14.0 LUFS, true peak -0.7.

**No BUDGET line** — a coloring-book piece, not a money one, and `check()`
asserts the word appears on no slide.
