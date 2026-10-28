# 2026-10-28 — "Every conference has the dry sandwich lunch."

Wed 28 Oct's morning Instagram carousel. Content bank item 26, which she added
herself on Oct 7.

**This is the first carousel in the real brand palette.** Lavender `#CECBF6`,
deep purple `#3C3489`, Poppins, EP✦ wordmark, numbered badge, bottom bar — the
guide's Carousel image production standard, which the four carousels before it
did not follow. Those stay live by her decision of 2026-10-25 ("keep it up,
lavendar moving forward"), so the grid carries a deliberate seam here.

## Slides

| | |
| --- | --- |
| 1 | "Made at 9am. Served at 12:30." + "Every conference has the dry sandwich lunch." |
| 2 | "Filling that stops an inch from the edge." |
| 3 | the prompt |
| 4 | the spec AI writes from the demo menu |
| 5 | "Don't order 'sandwiches.' Order a spec." + save |

Both sets built: `-instagram-1..5` at 1080×1350 and `-tiktok-1..5` at 1080×1920.

## Slide 1 is text only, and that is the brief's own fallback

The brief offers her photo — `conference-dry-sandwiches.jpg` in Drive
`October 28` — if it is there. Checked 2026-10-26: the folder holds only the
demo menu. If she adds the photo before Wednesday, slide 1 can be rebuilt
around it.

## Slide 4 answers the real file

`Caterer Menu — Boxed Lunch` (Drive id
`18NIYt2DdXgcD0BFQ_ZZ2x6cLFpfaZZYIx8fu1i77i04`), built Oct 14, reads:

> Assorted gourmet sandwiches on artisan bread: turkey and swiss, ham and
> cheddar, caprese, chicken salad. … Vegetarian and gluten-free options
> available upon request. … Boxes delivered and set at 11:30am.

Every line on slide 4 answers something actually in that menu. The veg and
gluten-free line is about replacing **"upon request"** with counts rather than
inventing numbers the menu never gave — the menu is the thing being corrected,
so putting made-up figures on the slide would have been answering a different
document.

## Type is sized to the frame, not guessed

Each slide searches down from a starting headline size until the whole block
fits the budget between the badge and the bottom bar, then centres it. That is
why slide 4 sets at 84px on the 1350 crop and 92px on the 1920 one: five
bullets need the room, and the taller frame has it.

## Published 2026-10-28

| Account | Post |
| --- | --- |
| Instagram `@aiforeventplanners` | [p/DfCiJxHIEGS](https://www.instagram.com/p/DfCiJxHIEGS/) |
| Facebook "The Event Planners AI" | [posts/122118466989449533](https://www.facebook.com/122100389133449533/posts/122118466989449533) |

Instagram media `18074162465762287`, `CAROUSEL_ALBUM`, out at 9:24am Eastern —
the morning slot her Oct 25 rule assigns to carousels, 9.1 hours before the
evening Reel and so clear of the 6-hour rule. Posted on her Sun 25 approval,
on the last day of the blanket go-ahead.

**Both captions hash to `ebee194d`, 845 characters** — the approved
`caption.txt`, the live Instagram caption and the live Facebook message, hashed
in the sandbox off the API responses rather than retyped.

### The slide order was verified on the published post, not assumed

The child container ids came back **non-monotonic** — submitted as slides 1→5,
they returned `…791`, `…788`, `…794`, `…770`, `…920`. Ordering the parent's
`children` array by id instead of by submission order would have published the
carousel as 4, 2, 1, 3, 5. The array was built from the results-array index.

That is the guard working, which is not the same as the result being right, so
the live post was checked: its five children were downloaded from Instagram's
CDN and matched against the committed slides. Every position matched its own
slide at **MAD 0.00**, with the nearest other slide 11.4 or further away. The
published media ids embedded in the CDN URLs are Instagram's own and do not
map back to the container ids, so comparing the pictures is the only check
that actually reads the order.

`FACEBOOK_CREATE_MULTI_PHOTO_POST` keeps the order of `photo_urls`; its five
subattachments came back in upload order.

### Her photo never arrived, so slide 1 is the specified fallback

The brief offers `conference-dry-sandwiches.jpg` for slide 1 and names the text
slide as the fallback. Drive `October 28` was checked on Oct 26, again at 6:52am
and again at 9:24am: the folder holds the demo caterer menu and the ten
generated slides, and nothing else. The text slide is the brief's own answer to
that, not a shortcut.

### TikTok

The five `-tiktok-` slides and the caption went to her at 6:53am Eastern, ahead
of the Instagram post rather than after it, so she had the morning to use them.
Last 10 TikToks checked first — newest was the Oct 27 ROI rebuild, no carousel
among them. The upload is hers; nothing is recorded in `docs/TIKTOK-POSTED.md`
until she says it went up, because scheduled and handed-over are not posted.
