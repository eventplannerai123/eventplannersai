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

## Slide 4 is her real answer — swapped in the same day

It was built in house type first, under the neutral heading "HOW LONG EACH ONE
HOLDS", because she had not run the prompt and this session will not label its
own writing as a model's output. She then ran it and dropped the recording in
the day folder, so the slide is now a crop of her own ChatGPT answer and the
Oct 13 label — **"WHAT AI CAME BACK WITH"** — applies honestly.

**Her answer is better than the house version was.** The invented hold times
were round numbers; hers is a real three-column table (Hot item / Quality over
90 minutes / Refresh and replenishment plan) and gives the eggs *"Poor if left
in one pan. Dry, rubbery, watery, or discolored"* with a **15–20 minute**
replacement interval. That verdict is the piece.

It also reached the callout independently. Near the end of the recording it
says the priority is to get the manager to commit to **"a real replenishment
plan, not simply 'as needed.' That phrase doesn't tell you who is watching the
food, how frequently it's checked, or whether fresh batches will actually be
available."** The slide's own line under the screenshot — *The BEO said
"Replenishment: as needed."* — was written before that was read, and her
answer arrives at the same place.

| Detail | Value |
| --- | --- |
| Source | `ScreenRecording_10-16-2026 9-51-12 AM_1.mov`, Drive October 18 |
| Frame | **t = 10.8s** — the only one with the header and a whole row together |
| Crop | source `(20, 303, 1190, 1508)` of a 1206x2622 capture |
| Shows | header + scrambled eggs + applewood bacon |

**Ad check: the recording carries a FELFEL advert** ("Book a Free Tasting —
office meals stocked daily") that scrolls in at about **21s**, right at the
end. A sixth advertiser to add to the guide's list, and a fresh reminder not
to look for a known logo. The crop at 10.8s is ten seconds clear of it.

The top of the crop was moved down 17px after the first render: at y=286 it
caught a ghost of the app's floating buttons above the table. At 303 the
header is whole and the ghosts are gone.

**The card is capped, not just scaled.** The 4:5 slide is 570px shorter than
the 9:16 one and the screenshot does not shrink with it, so at full width the
restated line landed on top of the footer. The card now takes whatever is left
once the label, the line, the note and the footer have had their share, and
its width scales with it so the screenshot is never stretched.

The six hot items and `assert_beo()` stay in the script even though the table
no longer draws a slide: the piece still rests on nothing on that BEO holding
the full 90 minutes, and the build should fail if that stops being true.

## Slides

| # | Slide |
| --- | --- |
| 1 | Her photo + "Breakfast runs 7:30 to 9. The runny eggs don't." |
| 2 | Why it matters — scrambled eggs don't survive 90 minutes in a chafing dish |
| 3 | The prompt |
| 4 | Her real ChatGPT answer — the hold table, eggs at 15-20 minutes |
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
