# Contingency carousel — 2026-10-13

Six slides, two sizes. **Hers to post on both platforms** — TikTok photo mode on
Tue 13, then the Instagram carousel on Wed 14.

| Set | Size | Goes where |
| --- | --- | --- |
| `slides/tiktok/` | 1080x1920 | TikTok photo carousel, Tue 13 — she posts it from her phone |
| `slides/instagram/` | 1080x1350 | Instagram + Facebook, Wed 14 |

Caption: `build/caption-tiktok.txt`, the guide's Tue 13 wording verbatim. It
carries no "Prompt below." line, so nothing had to be stripped under the Oct 12
retirement.

Content bank item 20, from her Oct 4 answer on why budgets go over. Palette,
fonts and footer match the Mon 5 hidden-fees carousel.

## The source arrived as a recording, not a screenshot

The guide specs slide 5 as "ChatGPT's answer, from Sahiba's screenshot". What
she sent on Oct 12 was a **17.5s screen recording** (1206x2622, 60fps, no
rotation side data), with the message "here is tomorrow's screen recording".

Two things worth checking before building, both checked:

- **It is the contingency piece, not the AV one.** Tue 13 has no screen
  recording in it at all — its items are a photo carousel and a Story — and the
  AV schedule check is Wed 14. The footage decides it: frame one is the
  contingency prompt with the DEMO budget PDF attached. The directory was
  renamed from `2026-10-13-av-schedule` once the frames were read.
- **The recording opens correctly**, prompt sitting in the input box with the
  PDF attached, before the send tap. No faked cold open needed.

A recording is strictly better than a screenshot here: it allowed the answer
frame to be chosen rather than accepted.

## Slide 5 is her screenshot, minus one broken row

The crop is from **t=11.5s**, where the whole "Contingency calculation" card is
on screen and well clear of the ad. It is cut just below *Current contingency
percentage 2%*, and the row beneath it is dropped on purpose:

> ChatGPT wrapped **"$3,000" as "$3,00 / 0"** across two lines in its own
> shortfall row.

That is the single most important number in the piece, so it is restated
underneath in house type as **"$3,000 short."** rather than shipped broken.
Nothing above it is touched, so the card still carries the four figures the
claim rests on — total, required, existing, 2% — and $3,000 follows from them.

## The ad

A **Harvest** ad ("See project profitability") rides into the bottom of the
answer from about t=15 — the ninth distinct advertiser after Adobe Acrobat,
Adobe Firefly, Rillion, Cambridge, Turning Stone, Fever, Asana and Chivari. The
chosen frame is 3.5s earlier and the crop ends far above it. Not an issue for a
still carousel the way it is for a scrolling cut, but checked rather than
assumed.

## The maths is asserted, not eyeballed

The guide says "check the maths on slide 4 before sending", so `make_slides.py`
refuses to build if it moves. Read from her spreadsheet
(*Copy of DEMO Draft Event Budget (fake data, contingency post).xlsx*):

- the eleven line items sum to **exactly $100,000**
- 5% of that is **$5,000**; the contingency line holds **$2,000**
- that is **2.0%**, and **$3,000** short
- slide 6's three examples are each re-derived as 5% of their budget

All five of those are `assert`s. The figures also match what ChatGPT returned on
screen, which is the point of the piece.

## Slides

| # | Slide |
| --- | --- |
| 1 | Cover — "If the budget is $100,000, $5,000 of it should have no name on it." |
| 2 | Why it goes over — "Nobody budgeted for contingency in the first place." |
| 3 | The prompt |
| 4 | The draft budget, eleven lines, contingency row highlighted, total $100,000 |
| 5 | ChatGPT's answer card + "$3,000 short." |
| 6 | "My rule: at least 5% in a no-name line from day one." + $50k/$100k/$250k |

## Layout

Both sizes come from one pass: every slide centres its own block — tracked
label, rule, and body — so no y values are hand-tuned per aspect ratio. The
first build got this wrong by leaving the label out of the measured height,
which pushed every slide's content high.

**Safe zones checked on the exported JPEGs**, not from the code. Across all six
TikTok slides content runs y 478–1436, inside the Oct 5 band (nothing above
y=230 or below y=1440). Only the footer and the "keep swiping" line sit lower,
both decorative.

## Rebuilding

`slide-5` needs the answer crop, which is gitignored with the rest of the raw
source. Regenerate it first:

```bash
ffmpeg -ss 11.5 -i source/raw.mp4 -frames:v 1 build/frames/full.png
python3 -c "from PIL import Image; Image.open('build/frames/full.png').crop((40,1010,1166,2130)).save('build/frames/answer-card.png')"
python3.13 make_slides.py
```

PIL is on `python3.13` in this container, not `python3`.
