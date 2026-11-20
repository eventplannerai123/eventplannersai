# The coloring book's first three reviews (slide Reel + TikTok carousel)

Built Fri 20 Nov from the three reviews Sahiba sent that afternoon, after the
Fri 20 block's YOU line asked her to check the listing. Her line: "3 reviewas",
then the paste.

**Not dated yet.** The guide's Fri 20 CLAUDE CODE line says to build it and
propose a date at the Sun 22 recap. The slides are the build; the Reel render
and its music bed wait, for a reason — see below.

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

## Why the Reel is not rendered yet

Two things that depend on the date, which is Sunday's decision:

- **The closing slide has a deadline in it.** "Two copies are up for grabs
  until Friday" is true only while the Nov 20 giveaway is open, and it closes
  **Fri 27 Nov at 11:59pm Eastern**. So the piece has to post Mon 23 to Thu 26,
  and the slide is wrong the moment it does not.
- **The music bed cannot be generated before the day is known.** Her Nov 10
  rule is that no two posts on the same day share a bed, and upbeat by
  default. Picking the day first is cheaper than finding out afterwards.

**No BUDGET line** — a coloring-book piece, not a money one, and `check()`
asserts the word appears on no slide.
