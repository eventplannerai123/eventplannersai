# Runny eggs carousel — 2026-10-18

Five slides, two sizes. **Built, not posted** — Instagram and Facebook run from
here after her go-ahead; the TikTok photo carousel is hers.

| Set | Size | Goes where |
| --- | --- | --- |
| `slides/instagram/` | 1080x1350 | Instagram + Facebook, Sun 18 morning |
| `slides/tiktok/` | 1080x1920 | TikTok photo carousel — she posts it |

Caption: `build/caption.txt`, the guide's Sun 18 wording verbatim. Four literal
`#`, no `%23`, no "Hashtags:" label, no retired "Prompt below." line.

Content bank **item 25**, her own line from the conference on Oct 7: "Runny
eggs are the worst thing you can put in front of a conference room."

## This day was the dry sandwich lunch until Oct 16

Sun 18 was built around item 26, the dry sandwich lunch, and was blocked on a
photo she was asked to film. On Oct 16 she sent a photo of a **conference
breakfast plate** instead — scrambled eggs sitting in liquid, roast potatoes,
used cutlery — and swapped the two days herself: **runny eggs to Sun 18, the
dry sandwich post to Wed 28.** She moved the demo files in Drive to match
(`BEO — Day 1 Breakfast` to October 18, `Caterer Menu — Boxed Lunch` to
October 28).

Worth recording, because the first instinct here was wrong: the photo was
offered and this session's first answer was that it did not fit the sandwich
piece. True, but the useful move was the one she made — **change the piece to
fit the photograph that exists**, rather than hold the piece for a photograph
that does not. Item 25 was already in the bank waiting for exactly this image.

She also caught a caption bug in the guide's own eggs block: it ended with the
internal note "Pairs with the dry sandwich post. Never name the venue or
caterer," which would have been published. Her fix, now in the guide, ends it
"Save this for your next breakfast BEO." `build/caption.txt` carries the fixed
version, and the check for it is in the build log.

## The hook is hers, minus one word

The guide specified "Breakfast runs 7:30 to 9. The scrambled eggs don't."
She then asked: *"should we say - the runny scrambbled eggs dont?"*

Taken, dropping "scrambled": **"Breakfast runs 7:30 to 9. The runny eggs
don't."** "Runny scrambled eggs" is two words doing one job, slide 2 says
scrambled eggs anyway, and "runny" is what makes the pun land — the eggs do
not *run* to 9. It is also her own word, straight from item 25.

## Slide 1 is her photograph, and the layout went through two wrong versions

| Try | What happened |
| --- | --- |
| Flat scrim over the whole frame at 62% | Muddied the plate into brown soup. The photo *is* the hook; it has to read as food. |
| Gradient, clear at top, solid by the type | Cannot satisfy both constraints at 1080x1920 — the type wants solid colour, and rule 4 keeps it clear of the bottom 25% where TikTok's caption and buttons sit. Those two zones barely overlap. |
| **Split frame: photograph above, solid panel below** | Shipped. The plate is completely unobscured and the type sits on flat colour. |

The tall cut gives more of the frame to the panel because it has far less room
above the safe line; the 4:5 Instagram slide has no such furniture, so its
photo runs larger. Both are computed from the text block rather than hand-set,
and two asserts fail the build if the hook drifts into the photo or down into
the platform's furniture.

The photo was shot under warm banquet lighting with no flash, so it arrives
dim and orange. It is lifted before anything is laid over it — brightness
1.30, contrast 1.10, saturation 0.92 — on her instruction, "yes brighen it
up". Her first version read as a dark smudge.

## Slide 4 is NOT a screenshot, and is not labelled as one

The Oct 13 contingency carousel embedded a crop of her real ChatGPT answer
under the heading "WHAT AI CAME BACK WITH". There is no such recording for
this piece — she has not run the prompt — so the hold times are set in house
type under **"HOW LONG EACH ONE HOLDS"**, a heading that claims no tool and
does not present the slide as any model's output.

The precedent for a carousel with no answer slide is the Oct 5 hidden-fees
one, which is house type throughout.

**If she runs the prompt and sends the answer, crop it in and relabel.** That
would be the stronger slide; this is the honest version of the weaker one.

The six hot items, their order and their hold times come from the real demo
file in Drive (`BEO — Day 1 Breakfast`, October 18 folder): 400 guests,
7:30–9:00am, buffet from chafing dishes. `assert_beo()` fails the build if
anything on the list grows to cover the 90-minute window, because the whole
piece rests on nothing on that BEO surviving the hold unattended.

The callout under the table is the real find in the demo file: it says
**"Replenishment: as needed"**, which names no interval and so makes the
refresh nobody's job.

## Slides

| # | Slide |
| --- | --- |
| 1 | Her photo + "Breakfast runs 7:30 to 9. The runny eggs don't." |
| 2 | Why it matters — scrambled eggs don't survive 90 minutes in a chafing dish |
| 3 | The prompt |
| 4 | How long each one holds — the six hot items, two flagged |
| 5 | "Nobody complains about breakfast. They just remember it." |

Palette, fonts and footer match the Oct 13 contingency and Oct 5 hidden-fees
carousels.

## Her photo is not in this repo

`source/conference-runny-eggs.jpg` is gitignored under the existing
`carousels/*/source/*` rule. The repo is public — `raw.githubusercontent.com`
URLs are how Meta fetches these slides — so her raw camera roll does not
belong here. Only the finished slides are committed, and slide 1 is a crop of
the photo she is choosing to publish.

She is uploading the original to Drive herself (October 18,
`conference-runny-eggs.jpg`); it cannot be filed there from here, because the
upload-from-URL route needs a public URL and the inline route is base64 over
the size cap.
