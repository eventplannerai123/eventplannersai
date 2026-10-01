# Vendor quotes reel — 2026-10-01

Status: **published 2026-10-01**, on the 9am ET schedule the author approved
on 2026-09-30 ("So much better. Thursday at 9am schedule go ahead").

| Account | Post |
| --- | --- |
| Instagram `@aiforeventplanners` | https://www.instagram.com/reel/Dd8-Gz8Feq6/ |
| Facebook "The Event Planners AI" | reel id `1046553998431682` — confirmation pending |

**Instagram caption verified**: read back live and diffed against
`build/caption.txt`, identical, 598 bytes each. Literal `#`, no `%23`, no
"Hashtags:" label, CTA is "Prompt below."

Facebook's create call succeeded but the post had not surfaced in the page
feed on the first read-back, which is the normal lag for this page. A
follow-up check is scheduled rather than a retry, since
`FACEBOOK_CREATE_VIDEO_POST` has no duplicate protection.

Pre-flight checks at fire time, all passing: mp4 md5
`7519d2e0f36ddaf922aff8c38f1d628f`, caption md5
`bac72e131e7184dca8449b10d1729b20`, raw URL 200 at 7,029,991 bytes, container
`18093807053367131` FINISHED after 15.9s, media id `18199658662376106`.

**First Instagram post under the October plan's three-a-week cadence**, and
the first since the length test was dropped.

First piece of the October plan, and the first Instagram day under the new
three-a-week cadence (Mon/Wed/Fri, plus this Thursday to start). Target
15-20s, like everything from Oct 1.

## What is here

`source/` holds three AV quotes for the same 200-person conference and an
answer key. They are built, not real — the author's own "still to build" list
named them, the way the Sep 23 catering invoice was built with deliberate
errors and an answer key.

| File | Quoted on the page | Real cost for this event |
| --- | --- | --- |
| `quote_meridian.pdf` | $6,799.50 | **$17,175.58** |
| `quote_clearline.pdf` | $8,700.00 | **$10,403.01** |
| `quote_stagecraft.pdf` | $12,400.00 | **$18,471.62** |

**Headline order:** Meridian < Clearline < Stagecraft.
**Real order:** Clearline < Meridian < Stagecraft.

So the cheapest-looking quote is $10,376 more expensive than the one that
actually wins, and the "all inclusive" one is the worst of the three. Both
of the tempting answers are wrong and the unglamorous middle quote is right,
which is a better lesson than a single gotcha.

## How each one hides cost

- **Meridian** — a genuine equipment-rental quote being read as a full quote.
  The headline covers the ballroom only: no breakout rooms, no labor, no
  power, no rigging, no tax. The 22% service charge then recalculates upward
  once the breakout equipment is added, which is the detail most likely to be
  missed.
- **Clearline** — nearly complete, and its only real gap is overtime: load-in
  06:00 to strike 19:00 is 13 hours against the 10 included. Its other two
  exclusions are deliberately *not* hidden costs — the recording package and
  the declinable damage waiver are not needed for this event. That is the
  test of whether the model separates "excluded" from "required", rather than
  adding up every number it sees.
- **Stagecraft** — "all inclusive" is the trap. A 20% coordination fee and a
  non-declinable 5% damage waiver both compound on top of the add-ons, and
  the included projector is 5,000 lumens, under-spec for a 200-person
  ballroom with house lights up, so that upgrade is not optional either.

## The answer key is generated, not written

`source/build_quotes.py` holds the line items once and renders both the PDFs
and `source/ANSWER-KEY.md` from them, so the key cannot drift from the
documents. Re-run it to change a number. Sales tax is 8.875% throughout.

Worth keeping: `reportlab` is not installed in a fresh container and
LibreOffice's HTML import fails here ("source file could not be loaded"),
so the PDFs come from `pip install reportlab` and reportlab's platypus,
not from an HTML conversion.

## Cuts

Both 1080x1920 (ratio exactly 0.5625), 30 fps, H.264 high, CRF 19,
`+faststart`, AAC 192k at 48 kHz.

| File | Platform | Duration | Voiceover | Payoff at |
| --- | --- | --- | --- | --- |
| `quotes-instagram.mp4` | Instagram, Facebook | 15.07s | -14.0 LUFS | 5.30s |
| `quotes-tiktok.mp4` | TikTok (manual upload) | 15.10s | -14.0 LUFS | 5.50s |

TikTok's opening beat is 0.3s shorter than Instagram's on purpose: it is the
primary platform, so it keeps more margin under the six-second ceiling.

Both inside the plan's 15-20s target and well under the 6-second payoff
ceiling. Two separate voiceovers, both generated here.

**The TikTok cut is not for Oct 1.** The plan holds it back to **Tue 13 Oct**;
Thursday's TikTok slot is the Sep 14 floor plan back-catalogue item.

## The recording

36.31s, 1206x2622 at 60fps HEVC, 51.5 MB, via Drive. The standard iPhone
capture size, so `crop=1206:2144:0:478` applies unchanged.

**It opens exactly right** — the prompt sitting in the input box with all
three PDFs attached, and the send tap at ~2.75s. Checked before choosing the
cold open rather than assumed, after the Sep 29 build threw away a correct
opening.

Six beats, and **no speed ramp anywhere** — unusual for this series, and the
result of the author's note on the first build.

ChatGPT opens each attached PDF in turn and renders it full-screen:
Stagecraft at 6.3-7.9, Meridian at 9.3-10.9, Clearline at 12.3-13.9. The
first build treated all of that as one "generating" beat and ran 3.15-11.55
at 3x. That was wrong twice over, and she caught both faults from the cut
alone:

- **The third quote was never in frame.** The slice ended at 11.55 and
  Clearline does not render until 12.3.
- **"Too many abrupt flashes."** At 3x the two quotes that were in frame got
  about half a second each.

The document views are the premise of the piece — it is called three quotes —
not filler to ramp through. So each now gets its own beat of 1.05s at 1.0x,
and the dead chat between them is cut out instead of sped up. Three seconds
of setup buys three legible documents, and the payoff still lands at 5.00s.

A reveal beat was dropped in the same pass, for the same reason: the
per-vendor breakdown ("1. Clearline... 2. Meridian... the classic low
headline-price trap") went, leaving the table and the bottom line. That is
one cut in the reveal instead of two, and the bottom line carries all three
numbers anyway. Dropping a beat rather than shaving every beat is the Sep 29
lesson.

## Flow

Every cut is a **0.20s dissolve**, not a hard cut, and the beat boundaries sit
on the voiceover's own phrase gaps rather than on round numbers. The gaps were
measured off the generated mp3 with
`silencedetect=noise=-32dB:d=0.18` rather than guessed:

| Instagram voiceover | Beat |
| --- | --- |
| "Three AV quotes for the same job," 0.00-1.91 | prompt in the box, send tap |
| "and not one of them lists the same things." 2.27-4.31 | the three quotes |
| "Here's all three side by side..." 4.93-8.07 | the table |
| "and where each one is hiding the cost." 8.57-10.62 | the table |
| "The cheapest one isn't the cheapest." 11.17-13.15 | the bottom line |

So the picture turns over where the narration does. The table arrives at 5.10
against "side by side" at 4.93, and the bottom line at 11.20 against "The
cheapest one" at 11.17.

**Each quote beat starts ~0.25s after its document appears.** ChatGPT shows a
"Loading" spinner before it renders a PDF, and starting on the render boundary
pulled that spinner into the dissolve. Caught on the exported frames, not from
the filtergraph. A faint "Loading" label does remain lower in the frame during
each quote hold — that is the viewer fetching page 2 of the same PDF, it is
what the screen actually showed, and it sits in whitespace well below the
page.

## Ads

**A sixth advertiser**: "NYC Event Spaces" from Will & Wall LLC, a black
circular NYC VENUE badge that scrolls up into frame at around t=34.5 in the
source. Both cuts end at 33.60, so it is out of frame, and both finished
exports were checked frame by frame over the whole frame through the final
frame — clean.

Worth recording: a dark-pixel count over the bottom strip was **useless**
here. The reveal is a dense page of black text, so the count swings between
3,000 and 9,000 from one frame to the next and the ad badge does not stand
out against it. That is the same shape of false all-clear as the Sep 21
colour threshold. The ad was found by looking.

## What ChatGPT got, and the one thing it missed

It ranked the three correctly — Clearline < Meridian < Stagecraft — and
named each hiding mechanism. Its pre-tax figures against the answer key:

| | ChatGPT | Answer key (pre-tax) |
| --- | --- | --- |
| Clearline | ~$9,555 | $9,555.00 |
| Meridian | ~$15,269.50 | $15,775.50 |
| Stagecraft | ~$16,965.90 | $16,831.25 |

Clearline is exact. **Meridian is $506 light, and that is precisely the
detail the quotes were built to test**: the 22% production service charge
recalculates on the breakout equipment too, and ChatGPT applied it only to
the ballroom. It also correctly refused to state tax-inclusive totals,
saying none of the quotes gives enough information to compute the tax — a
fair call rather than a miss.

None of this changes the ranking or the point of the piece, so it does not
affect the cut.

## Hooks and voiceovers

The plan gives one hook and one script. The standing rule is that the TikTok
cut takes a genuinely different command-style hook and slightly different
pacing, so TikTok got its own of both.

| | Instagram | TikTok |
| --- | --- | --- |
| Hook, 0:00-0:02 | Three quotes. / None of them comparable. | Stop comparing / quote totals. |
| Voiceover | 13.45s | 12.72s |

- **Instagram voiceover** — the plan's script, plus a closing line so the
  piece ends on its own payoff: "Three AV quotes for the same job, and not
  one of them lists the same things. Here's all three side by side on what's
  actually comparable, and where each one is hiding the cost. The cheapest
  one isn't the cheapest."
- **TikTok voiceover** — "Stop comparing the totals on vendor quotes. These
  three are for the same job, and not one of them lists the same things.
  Here's all three side by side — and the cheapest quote is ten thousand
  dollars more than it looks." The figure is exact: Meridian quotes
  $6,799.50 and lands at $17,175.58, a difference of $10,376.08.

**The hook card sits at y=1300, not the usual 620.** The opening exists to
show the prompt in the input box with all three PDFs attached, and 620 lands
straight on it. 1300 sits over the keyboard, which carries no information,
and still clears Instagram's own bottom furniture. Same call as Sep 29, and
verified on the exported frames rather than from the filtergraph.

## Caption

`build/caption.txt`, used for Instagram and Facebook. `build/caption-tiktok.txt`
is the same text — the plan gives no separate TikTok caption.

CTA is the shortened "Prompt below." No end card: every current brief ends on
the output itself.

## Posting

- Instagram and Facebook: this session, **after explicit approval**.
- TikTok: manual upload, always. And **not on Oct 1** — the plan holds this
  piece's TikTok cut back to Tue 13 Oct.
