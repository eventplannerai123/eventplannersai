# Sun 8 Nov 2026 — "Everyone has a rain plan. Almost nobody has priced one."

**Instagram carousel, 6:30pm Eastern (23:30 UTC).** Also to Facebook. TikTok
takes the same six slides as a photo post, hers, at 6:30pm alongside
Instagram. Content bank 21.

Built Sat 7, the day before, so the slides exist before she is asked to look
at them.

A redo of the Sep 29 rain plan Reel, which reached 21 in a morning slot. The
original stays up.

| | |
| --- | --- |
| Instagram | `slides/2026-11-08-rain-plan-instagram-1.jpg` … `-6.jpg`, 1080x1350 |
| TikTok | `slides/2026-11-08-rain-plan-tiktok-1.jpg` … `-6.jpg`, 1080x1920 |

All twelve slides are filed in Drive `November 8` alongside the sheet.

## Live

| | |
| --- | --- |
| Instagram | [p/Dff8cx8CYSU](https://www.instagram.com/p/Dff8cx8CYSU/) — media id `18093986798293229`, posted 2026-11-08 23:32 UTC (6:32pm Eastern) |
| Facebook | post `1233196746554445_122120384961449533`, six photos |

Live caption diffed against `build/caption.txt` character for character:
identical.

**Slide order verified 1-6 at MAD 0.00**, each published child against its
committed slide. The check had to run in Composio's remote sandbox, because
`scontent-*.cdninstagram.com` is blocked from this session. It was worth
running: the child container ids came back non-monotonic again (…855, …861,
…858, …864, …927, …930), so ordering the parent's `children` by id rather
than by results index would have shuffled slides 2 and 3.

## Slide 5 is computed from the file

The guide asks for the sheet to be built and the prompt run on it, so every
figure on slide 5 comes out of `Garden Reception — Budget and Rain Plan`
(Drive `November 8`, `1oKTGZntZsocspeZrBS9auIKm0jtYZ0k_7-BJdWSqnPk`), and
`make_slides.py` recomputes all of them before a slide is drawn:

| | |
| --- | --- |
| Outdoor plan | $35,800 |
| Tent quote | $14,080 |
| Rain plan | $48,680 |
| Difference | **$12,880** |
| Tent held and not used | $3,600 |
| Rain call | Wed 9 June 2027, 72 hours before Sat 12 June |

**The whole number turns on one substitution.** The tent lighting replaces
the string lighting rather than adding to it, so it costs $200 net, not
$1,400 — take it as an addition and the difference reads $14,080. That is
exactly what the prompt exists to catch, so slide 5 says it in words and the
generator asserts it.

## Two layout bugs fixed here, both inherited

Both came from `carousels/2026-11-04-contingency/make_slides.py`, where
neither showed:

- **The foot's rule was placed by comparing the wrapped lines to the raw
  string.** That matched only while every foot fitted on one line; slide 5's
  does not, so the hairline was drawn *through* its second line instead of
  above the block. It is keyed on the flag now.
- **The headline re-wrapped its own line breaks.** Slide 1 first rendered as
  "Everyone has a / rain / plan. Almost / nobody / has priced one." The size
  search now rejects any size at which a written line does not fit whole,
  which is why slide 1 sits at 86px while slides 2 and 3 sit at 100.

## Caption

`build/caption.txt`, the guide's own text, same for TikTok. It keeps the
guide's "The prompt:" label rather than the `AI Prompt:` form — that is how
this day's caption is written in the doc.
