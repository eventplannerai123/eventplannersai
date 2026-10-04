# Hidden fees carousel — 2026-10-05

Seven slides, 1080x1350, JPEG (the Instagram carousel API requires JPEG, not
PNG, per the guide's carousel production standard).

Status: **built and approved 2026-10-04, scheduled to post Mon 5 Oct 13:06
UTC** (trigger `trig_01XDRY1cf2UXgEbHxxVQXbxw`). The author saw all seven
slides and said "Permission granted", so Monday's run is an approved publish
rather than a draft to re-check.

## Why a carousel, and why this one

The author is flying Mon 5, so the Instagram slot needed a piece that could be
built and posted with nothing from her — no screen recording, no upload. A
carousel is the only format in the series that qualifies. It also plays to the
one Pinterest-shaped lesson the account has not used on Instagram: **carousels
lead on saves**, and saves are the signal reach follows.

The content is **content bank item 24**, written from her own Oct 4 answer —
the fees that never appear in a venue's headline rate. It works for weddings and
corporate alike, which matters under the two-wedding-pieces-in-seven rule.

It is the venue-side twin of the Oct 1 vendor quotes reel: same lesson, same
"the headline number is not the number", different document.

## Slides

| # | Slide |
| --- | --- |
| 1 | Cover — "Coat check. Linens. Administrative fee. Cake cutting." / "5 charges that never make the venue's headline rate." |
| 2 | Coat check — per guest or attendant hours |
| 3 | Linens — included or add-on |
| 4 | Administrative fee — a percentage, and usually not a gratuity |
| 5 | Cake cutting — outside-baker fee |
| 6 | AV — projector, screen, microphones |
| 7 | The prompt, and "Ask on the site visit, not on the final invoice." |

**The cover says five and there are exactly five fee slides** — checked in code
at build time, because the Sep 22 carousel shipped its first version with
figures that contradicted the slide above them, and a cover that miscounts its
own contents is the same class of error. `make_slides.py` prints the count and
whether it matches.

Each fee slide carries one **ASK** panel: the question to say out loud on the
visit, rather than a restatement of the fee. That is the difference between a
list and something worth saving.

## Design

Palette and fonts sampled directly off the Sep 22 tablecloth slides, which the
guide names as the house carousel look:

| | |
| --- | --- |
| Cream | `#F5F1E8` |
| Pink panel | `#EDDFDE` |
| Ink | `#221D1A` |
| Warm grey | `#8A7E76` |
| Maroon (label on pink) | `#7A2A36` |
| Cover brown | `#3A3230` |

Display face is a bold serif, body and labels a sans, matching the original
pairing. The cover is the only dark slide, as on Sep 22.

## Posting

Instagram carousel + Facebook album, **both from this session**. The method is
the one proven on Sep 22 and recorded in that carousel's README: per-slide child
containers with `is_carousel_item: true` and their own `alt_text`, then a
carousel container in slide order; Facebook via `FACEBOOK_CREATE_MULTI_PHOTO_POST`.
**Child container IDs are not returned in a predictable order — the results
array order is what sets the slide sequence.**

Facebook alt text cannot be set from here (permissions), as on Sep 22.

### On approval

The guide's Mon 5 block says she approved the slide text on Oct 4 and to post
without waiting for her. CLAUDE.md's standing rule is the opposite and is
emphatic: never publish without a go-ahead in the conversation, and a brief's
wording does not override it.

Both were honoured rather than one chosen: the slides were **built and shown to
her on Oct 4**, before she travels, and she approved them in the conversation.
The guide line recorded an approval of the *text*, written before these slides
existed; showing the artwork turned it into a real go-ahead.

Scheduling it needed her permission too. The first attempt to create the Monday
trigger was refused, and rather than reaching the same end another way — editing
an existing trigger to carry the post — it was put to her, and she granted it.
Worth remembering: **a blocked scheduling call is a question for her, not an
obstacle to route around.**
