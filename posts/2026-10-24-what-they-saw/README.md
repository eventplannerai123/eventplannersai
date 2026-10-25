# "What they saw / What I checked" — 2026-10-24

Status: **built, not posted.** It was Saturday's post and was never built on the
day; she approved the wording on Sun 25. Instagram and Facebook run from here
after her go-ahead; the TikTok photo post is hers.

A text-only industry-truth post — no demo file, no prompt — so the caption
carries no `AI Prompt:` block.

## The brand look here is the right one

Lavender `#CECBF6`, deep purple `#3C3489`, Poppins, the EP✦ wordmark and the
handle. That is the guide's standard for both industry-truth posts and
carousels, and it says "Never another colour scheme".

**The carousels had drifted off it** — Oct 18, 21, 22 and 25 all went out cream
and maroon, which she caught on Oct 25 ("i thought we went back to purple").
Those are published and cannot have their images swapped. This post is the first
thing built back on the real palette.

**Poppins is not installed here.** The three weights come from Google Fonts and
are committed under `build/fonts/` so this rebuilds identically later. SIL Open
Font License.

**Poppins has no glyph at U+2726**, so a literal "EP✦" renders a tofu box — the
first build did exactly that. The star is drawn as a polygon beside the "EP".

## The fifth row is not the one the brief wrote

The brief's last row was "Lunch was fine. | The sandwiches were dry. I'll spec
them properly next time."

She rejected it on Oct 25: *"everything is ok but the lunch one ... the rest
follow a positive outcome stance"*. She was right — the other four are "it went
well, and here is the unseen work that made it", while that one was lukewarm on
the left and an admitted miss on the right.

Three replacements were offered; she picked **breakfast**:

> Breakfast ran smoothly. | I checked which hot dishes wouldn't survive a
> 90-minute hold and swapped the ones that wouldn't.

It keeps food in the set, it is her own runny-eggs story, and it restores the
pattern.

## Our own device, not hers

The format came from @thejuliettripp, and the guide draws the line: two columns
are ours; crossed-out lines, run-on paragraph lists and "Behind every event
planner…" are hers and are never used. Every row is a true moment of hers from
the content bank.

## Type is sized to the frame, not guessed

Five two-column rows is tight at 1080x1350 and loose at 1080x1920, so the
generator steps the body size down from 30px until the block fits the frame's
budget rather than carrying one hard-coded size. Both sizes landed at 30px.

| | |
| --- | --- |
| `slides/what-they-saw-instagram.jpg` | 1080x1350 — Instagram + Facebook |
| `slides/what-they-saw-tiktok.jpg` | 1080x1920 — TikTok photo post, hers |

## Caption

`build/caption.txt`, the brief's wording verbatim. The last line ties it back to
AI in one line, which is the industry-truth caption rule.
