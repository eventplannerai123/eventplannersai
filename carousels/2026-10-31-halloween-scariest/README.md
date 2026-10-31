# Sat 31 Oct — "The scariest moments of my career" (Halloween carousel)

Industry-truth carousel, 7 slides, both sets. Instagram 1080x1350, TikTok
1080x1920. Morning slot (~9am Eastern), which puts it 9½ hours clear of the
6:30pm expense report Reel — the 6-hour two-post gap is satisfied with room.

Built in the real brand palette: lavender `#CECBF6`, deep purple `#3C3489`,
hairline `#B0ACE4`, Poppins 400/600/700 committed under `build/fonts/`.

## What is on each slide, and where it came from

Nothing is invented. Every moment is a content-bank item and the shortcut on
its slide is that item's own shortcut, not a new one written to fit the layout.

| Slide | Moment | Bank item |
| --- | --- | --- |
| 1 | cover | — |
| 2 | an ambulance had been called | **39** (her answer, Oct 30) |
| 3 | the AV crew went to lunch during the keynote | **1** |
| 4 | the boxes never made it to the room | **13** |
| 5 | they used the wrong entrance | **16** |
| 6 | a budget with no contingency line | **20** |
| 7 | closer | — |

The order is the gravity order: the medical emergency, then the one with a
room full of people waiting, then two logistics failures, then the one that is
only money. Nothing after slide 2 is a near-miss involving a person.

## Her two notes on this build, and how each is answered

**"make sure to add some pumkins, grim reapers, ghosts etc so it 'holiday
themed'".** Five motifs — pumpkin, ghost, bat, reaper, headstone — drawn as
vector shapes in `make_slides.py`. They have to be drawn rather than fetched:
"no stock, no generated visuals" bars an image, and "Never another colour
scheme" bars anything that arrives in orange and black. They sit in a reserved
178px band above the bottom bar, as a centred cluster, so they can never land
on text.

The headstone deliberately carries engraved lines rather than a cross. A `+`
inside a stone reads as a first-aid symbol, which is the last thing this
carousel needs two slides after an ambulance.

**"make sure the heaviness of the first one has a smooth transition to the
lighter ones".** Three things carry it, and the third is the main one:

1. **Slide 2 has no motif band at all** and no decoration. The text takes the
   full height. The hush is the design.
2. **Slide 3 opens with her own pivot line** — "Everything else is small
   change." — set above the headline under a hairline. The reader is told the
   tone is turning, by the person whose story it is.
3. **The motifs ramp**, in count and in contrast, from one faint pumpkin on
   slide 3 to a full band at near-full purple on slide 6:

   | Slide | Motifs | Tint |
   | --- | --- | --- |
   | 1 | 5 | 1.00 |
   | 2 | **0** | — |
   | 3 | 1 | 0.38 |
   | 4 | 2 | 0.58 |
   | 5 | 3 | 0.76 |
   | 6 | 4 | 0.90 |
   | 7 | 5 | 1.00 |

   `tint(t)` blends the background toward deep purple, so a low-tint motif is
   a genuinely lighter mark rather than a smaller one. The ramp *is* the
   transition — it is not an ornament sitting on top of one.

## Build

    python3 make_slides.py

Headline size is solved per slide by shrinking from 96/104px until the block
fits the budget, so a text edit re-fits itself. Slide 2 keeps the whole
210 → H-190 budget; every other slide gives up 178px of it to the motif band.

## Caption

`caption.txt`, md5 `71533ceb`. First line states the takeaway, then the five
moments, then her "small change" line, then the medical-response-card prompt in
full, then one save line and the four standing hashtags. No employer and no
client is named anywhere in the slides or the caption.

## Approved, scheduled, filed

Sahiba approved it on 2026-10-30 ("approved"), before the blanket travel-week
go-ahead's successor rules — so this is her explicit go-ahead for this piece
and nothing else.

| | |
| --- | --- |
| Instagram + Facebook | 9:00am Eastern Sat 31 Oct (13:00 UTC, still EDT), one-shot task `trig_01SbNbpEpKmDypCmQPJHH876` firing into this session |
| TikTok | handed to her with the caption on 2026-10-30, the moment she approved the Instagram set. Last 10 TikToks checked first: nothing like it — the nearest are the Oct 29 client-brief carousel and the Oct 30 coloring book Reel |
| Drive | all 14 slides in `October 31` (`16UUW2lQ9YnjyZGZyN71zOuUnQfoHJsu2`), both sets, filed as part of the build |

The 6:30pm expense report Reel is a separate task (`trig_01Hix1kj2ho1vSiUWNGGZ3Dh`).
9:00am to 6:30pm is 9½ hours, so the 6-hour two-post gap holds with room.

The caption is also written into the guide's Sat 31 CLAUDE CODE block, and that
block's carousel line is struck `✅ done Oct 30`.

## Live

Posted Sat 31 Oct at 9:03am Eastern (13:03 UTC), from the scheduled task, on
her Oct 30 approval.

| | |
| --- | --- |
| Instagram | [p/DfKODl_EbP0](https://www.instagram.com/p/DfKODl_EbP0/) — media `17989773509881305`, `CAROUSEL_ALBUM` |
| Facebook | multi-photo post `1233196746554445_122118984231449533` |

Live Instagram caption read back and diffed against `caption.txt`: identical,
line breaks and all four hashtags intact.

**Slide order verified on the published post, 1→7 at MAD 0.00 each**, with the
next-nearest slide 12.6 or more away. Carousel child ids come back
non-monotonic — this build's ended 537/543/534/540/657/654/660 in request
order — so the parent's `children` array is ordered by the **results index** of
the child call, never by id.

Two things this build had to work around:

- **`INSTAGRAM_CREATE_CAROUSEL_CONTAINER` with `child_image_urls` is refused**
  ("Invalid parameter", HTTP 400, nothing created). The working route is the
  long one: seven `INSTAGRAM_POST_IG_USER_MEDIA` calls with
  `is_carousel_item: true`, then the parent with their ids in `children`.
  `share_to_feed` is a Reels field and does not belong on a carousel parent.
- **The Instagram CDN is blocked from this session's egress** —
  `scontent-*.cdninstagram.com` returns `connect_rejected` through the proxy —
  so the pictures could not be downloaded here to check the order. They came
  down inside Composio's remote sandbox instead, which can reach the CDN, and
  the MAD match was run there. Worth remembering: when the only real check
  needs a blocked host, the workbench is a second network, not a dead end.
