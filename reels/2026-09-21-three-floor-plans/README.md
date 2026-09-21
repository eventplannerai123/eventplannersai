# Three floor plan options reel — 2026-09-21

CTA: **"The full prompt is in the caption below."** This morning's brief
said "link in bio", but the guide's own copy of this day's caption (and its
Round 6 note) says the caption-below wording: "link in bio" is reserved for
downloadable files, and only once the bio links to a hub page holding them,
which it does not yet. The author confirmed the change before posting.
THREE was the assigned comment keyword and went unused - the mechanic is
retired.

Status: **published 2026-09-21.** Approved in conversation, then posted to
Instagram and Facebook.

| Account | Post |
| --- | --- |
| Instagram `@aiforeventplanners` | https://www.instagram.com/reel/DdjwZmKCPZB/ |
| Facebook "The Event Planners AI" | https://www.facebook.com/reel/1370019611567622/ |

Both captions were read back live and compared to the approved text byte
for byte - identical on both, four literal `#`, no "Hashtags:" label, no
comment keyword and no "link in bio".

**The Instagram container took longer than 45s to process** and the publish
call returned a 408 wait-timeout with the container still IN_PROGRESS.
Nothing had been published at that point. Rather than retrying blind or
building a second container, the container's status was read directly with
`INSTAGRAM_GET_POST_STATUS` (note: the field is `creation_id`, not
`ig_container_id`), which reported FINISHED on the second poll; the *same*
container then published cleanly. Worth recording because the single-use
rule applies to containers that **error**, not to ones still working - a
new container here would have risked a duplicate.

Facebook again had not surfaced on the first read-back and was re-read
rather than re-posted.

TikTok is not posted from here; that cut is uploaded by hand per the guide.

## The in-app ad

This is the first day the standing ad check actually caught something, and
it nearly got through.

An **Adobe Acrobat ad** scrolls into the bottom of frame during the reveal.
A first pass looked for the Acrobat logo's red and reported the ad starting
at 12.4s, so the reveal was cut at 12.20s — and the finished frame at 16.20s
still had **"Adobe Acrobat ... Ad"** legible under the input bar. The
detector was wrong: the logo fades in gradually, so while the ad text was
already readable the red pixels were still below threshold. An automated
sweep of the finished cut returned "0 red pixels" on a file that visibly
contained the ad.

Re-checked by eye on bottom-strip montages at 0.1s steps: **clean at
C 11.8, ad visible at C 11.9.** The reveal now ends at **C 11.70**, and both
finished cuts were re-verified the same way — strips across the final 1.75s
of each, no ad in either.

**Lesson: verify an ad check visually.** A colour threshold silently passes
a faded overlay, and the failure mode is a false all-clear, which is worse
than no check.

## Cuts

Both 1080x1920 (ratio exactly 0.5625), 30 fps, H.264 high, CRF 19,
voiceover normalised to -14 LUFS (measured -14.03, TP -1.48).

| File | Platform | Duration | Ramp | Time to payoff | Opening line |
| --- | --- | --- | --- | --- | --- |
| `floorplans-instagram.mp4` | Instagram, Facebook | 16.33s | 3.0x | 5.55s | "Two hundred guests, two bars, a candy bar, a photo booth — and I couldn't decide on one layout." |
| `floorplans-tiktok.mp4` | TikTok (manual post) | 16.53s | 2.8x | 5.65s | "Stop settling for one floor plan. Two hundred guests, two bars, a photo booth — ask for three." |

End card on both: "Save this before your next big event."

## Source handling

Three uploads arrived; **two were byte-identical**. Clip `0c44efac` is a
re-send of `ff2d5a70` (same 16.015s duration, same hash over the first
6 MB). The Sep 16 duplicate check caught it before any work was wasted.

The two distinct clips:

| Clip | Length | Contents |
| --- | --- | --- |
| A (`ff2d5a70`) | 16.02s | prompt in box with plan attached, send tap at 0.5s, fullscreen of the blank plan 2.9-6.5s, then generating — **ends still generating** |
| C (`8b589f28`) | 14.54s | generating to 1.2s, options appear 1.2-3.4s, fullscreen of all three layouts 3.4-7.3s, scrolling text to 11.85s, then the ad |

**The first upload had no payoff at all.** Clip A ends on "Setting the
scene" with the image still rendering, so the piece could not be built from
it — flagged rather than filled with anything synthetic. Clip C, sent
after, carries the reveal.

A and C do not overlap: A ends mid-generation and C starts later in the
same wait. Since the join sits inside the sped generating section, the gap
is invisible.

Structure, four segments:

1. Send tap — A 0.20-1.30. Prompt already in the box with the plan
   attached, tap on camera at 0.5s.
2. The blank hall — A 2.95-4.80, fullscreen. The "before" half of the
   transformation.
3. Generating — A 6.60-14.40 at 3.0x (2.60s).
4. Reveal — C 0.90-11.70 at normal speed (10.80s): the three options
   appearing, the fullscreen view of all three side by side, then the
   commentary scrolling.

### Representative slice

Flagging per the timing rules. This is image generation, so the wait is far
longer than the text pieces — it runs past the end of clip A and on into
clip C, well over 20 seconds. Segment 3 is a representative slice of it,
not the whole span compressed.

## Accuracy

The typed prompt on screen says "a 100 x 60 ft main hall, 6,000 sq ft",
which matches the attached `venue-floorplan-6000sqft.png` exactly, and
ChatGPT's reply opens "for your 6,000-square-foot hall". Nothing on screen
contradicts the file. Note this is a different room from the 3,800 sq ft
hall used on Sep 14.

## Silent tail

The voiceover is 10.16s against a 16.33s cut, leaving 6.2s. As on Sep 20
the tail is filled with the reveal **scrolling at normal speed** rather
than a freeze, which is what the brief asked for and what a "save this"
end card needs.
