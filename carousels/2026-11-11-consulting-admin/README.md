# Wed 11 Nov — consulting post 1: what I'd fix first in an event studio's admin

Her first post about her own services. Six slides in the brand system, built
Tue 10 as the guide's CLAUDE CODE line asks.

| | |
| --- | --- |
| Slides | `slides/2026-11-11-consulting-admin-1.jpg` … `-6.jpg`, 1080x1920 |
| Caption | `build/caption.txt`, identical for TikTok |
| Instagram + Facebook | slide Reel at 6:30pm, **after she approves** |
| TikTok | the same six JPEGs as a photo carousel, hers, about 9am |

**One set at 1080x1920, not the usual 1080x1350 pair.** The Nov 8 format rule
sends Instagram and Facebook a slide Reel — each slide about 2.5 seconds,
soft music — and TikTok the same slides as a photo carousel, so both outputs
want the 9:16 frame and one set serves them.

**No BUDGET line.** The guide says so outright: the ask on this one is "DM
me", and `check()` asserts the word BUDGET appears nowhere in the slides.

**No company name anywhere.** `check()` asserts it. This is the first post
that talks about what she sells, which makes it the one most likely to reach
for an employer or a client as proof.

## Slide 5 is a placeholder, and that is deliberate

Her Wed 11 YOU line asks for two or three lines on the offer — what it is
(workshop, audit or both), roughly how long, and who it's for — by Tue 10,
and says that until they arrive the slides use the plan in Section 12 of the
guide: *a 2-hour AI workshop for in-house event teams with a 30-day
check-in, and an AI admin audit for small event studios.*

That is exactly what slide 5 says, and `check()` asserts it still matches
`SECTION_12`. So the build fails loudly on the day the offer changes, which
is the day the caption's last paragraph has to change with it.

## The music question, unresolved

The format rule asks for **soft royalty-free music** under the slide Reel. A
Reel posted from here cannot use Instagram's licensed audio library — that
is in-app only, and `INSTAGRAM_POST_IG_USER_MEDIA` has no field that
attaches a track — so whatever audio is in the mp4 is what goes out. A
royalty-free bed baked into the file is therefore the only version of this
that works from here.

Nothing is settled yet and nothing is assumed: the slides exist, the Reel
assembly is tomorrow, and the choice between a baked-in bed, a silent hold
and her uploading it in-app belongs to her.
