# 2026-10-29 — What clients never tell you in the brief

Thu 29 Oct's morning carousel, content bank item 15. Second carousel in the
real lavender palette, after Oct 28's dry sandwich.

## Slides

| | |
| --- | --- |
| 1 | "4 things clients never tell you in the brief." / And the quote you'll get wrong without them. |
| 2 | "The budget. The headcount. The style." / A reception? A seated dinner? And what they actually want out of it. |
| 3 | The prompt |
| 4 | "Four for four" — the gaps, each with the demo email's own words |
| 5 | "Get all four before you quote anything." / Save this for your next enquiry. |

Built at 1080x1350 for Instagram and 1080x1920 for TikTok, both sets from
`make_slides.py`, in the guide's brand system: lavender `#CECBF6`, deep purple
`#3C3489`, Poppins, numbered badge, EP✦ bottom bar. Poppins is committed under
`build/fonts/`; its missing U+2726 is drawn as a polygon.

## Slide 4 is checked against the real demo email

`Client Email — Holiday Party` in Drive `October 29`
(`1byeHtblzLLQqwIhncbGd8op_FFifYDi7pTzwkW7pJfc`), built Oct 14. Every line on
slide 4 quotes it:

- **Budget** — "pricing so I can take it to my boss", and no number anywhere
- **Headcount** — "the whole team" plus "some people might bring a plus one"
- **Style** — "maybe a dinner, or maybe more of a drinks thing, we haven't decided"
- **The goal** — "fun but elegant", which is a mood rather than a purpose

Four for four is what makes it a clean demo: the prompt asks for four things and
the email answers none of them. The slide would be weaker if the email happened
to supply one, so it is worth saying that this was checked rather than assumed.

## The caption says "The prompt:", not "AI Prompt:"

That is the guide's own "Caption to paste" for this day, used verbatim. The
house layout in CLAUDE.md is `AI Prompt: "..."`, and Oct 28's sandwich carousel
followed it — so the grid carries both wordings. The guide wins over this repo's
notes when they disagree, and a caption she wrote is not silently normalised to
a convention. Flagged here rather than fixed.

## Who posts what

| | |
| --- | --- |
| Instagram + Facebook | from here, morning, **after her go-ahead** — the blanket travel-week go-ahead expired Wed 28 |
| TikTok | **hers** — the five `-tiktok-` slides as a photo carousel, same caption |

## Filed to Drive

All ten slides are in `October 29` (`1gyE_LzpNdL2PW1AQoM_vQmVC3Tw3DBkm`), both
sets, each upload's `parents` checked against the folder id rather than trusted
from the reply. Filed as part of the build, not when asked — the Oct 16 runny
eggs carousel was built, approved and committed with the Drive upload skipped
entirely, and she had to ask for it.

## Published

Thu 29 Oct, on her explicit go-ahead in the conversation ("sorry yes you can
post") — the blanket travel-week go-ahead had expired the day before, so this
was asked for and given.

| | |
| --- | --- |
| Instagram | media `18083538851706427`, [p/DfFEe8GoPrP](https://www.instagram.com/p/DfFEe8GoPrP/), `CAROUSEL_ALBUM`, 13:03:26 UTC — 9:03am Eastern |
| Facebook | multi-photo post `1233196746554445_122118678927449533` |
| Caption | both live captions hash `c5e4e020`, identical to `caption.txt` |

**Slide order was verified on the published post, not on the containers.**
Carousel child ids come back non-monotonic — this build's were 288/279/282/285/351
in request order — so ordering the parent's `children` array by id would have
scrambled the deck. The array is ordered by the **results index** instead.

To prove that worked, the five children were read back off the live post
(`children{id,media_url}`), downloaded from the CDN, grayscaled to 160x200 and
MAD-matched against the committed slides. Positions 1→5 map to slides 1→5 at
**MAD 0.00** each, with the nearest other slide 8.6 or more away. The CDN URLs
carry Instagram's own media ids, which do not map back to container ids, so
comparing the pictures is the only real check there is.
