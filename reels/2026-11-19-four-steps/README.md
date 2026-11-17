# Thu 19 Nov — the Vendor Payment System in four steps

The product's second Reel, after the Thu 5 launch. 6:30pm Instagram and
Facebook; TikTok about 9am, from her.

| File | | |
| --- | --- | --- |
| `four-steps-instagram.mp4` | 1080x1920, **32.80s**, 8.55 MB | -14.0 LUFS |
| `four-steps-tiktok.mp4` | 1080x1920, **35.33s**, 8.60 MB | -13.9 LUFS |

## Built Tue 17, from four recordings she made that morning

Her Thu 19 YOU line asked for the four steps screen-recorded by Tue 17, and the
folder they start from was two days late on my side — `November 19` did not
exist until Tue 17, which is in `products/vendor-payment-system/README.md`.

| | Source | What it shows |
| --- | --- | --- |
| Step 1 | `Recording 2026-11-17 092938` (17.7s) | the `/copy` link, the Copy document dialog, Make a copy |
| Step 2 | `092258` (70.2s) | Prompt 1 in ChatGPT with Gmail connected, and the table it returns |
| Step 3 | `093505` (44.6s) | the table pasted into the Payments tab, the colours filling in |
| Step 4 | `094509` (96.5s) | the catering agreement uploaded, Prompt 2, the clause table |

Her **first take of step 1 was re-recorded**: a Chrome bar reading *"Claude"
started debugging this browser* sat across the top for the whole 11.7 seconds.
The second take is clean and opens on the dialog, which the first did not.

**Step 3's first seconds show `#REF!`** in the Due date header, because the
paste carried the AI table's own header row into row 2 and broke the formula.
She fixed it; the cut starts at 31.0s, after it resolves. The finished tracker
reads $59,380 scheduled, $13,300 paid, Petal Press overdue and Fernwood's
$9,000 due this week — checked against the live sheet, not against the frames.

## The tracker shots show the whole sheet, and never the Reminder log

Her note, Nov 17: *"when you show the tracker have it show the entire length of
the spreadsheet and dont show the reminders"*. Both halves changed the build.

**The whole sheet.** The payoff and step 3 now take a **630-tall crop from
y=265**, which holds the header and all seventeen payment rows at once. The
first version used a *taller* 792-tall box from y=140 and showed **fewer** rows,
because it started above the data and ran out before the last vendor — more
pixels, less sheet.

**No Reminder log.** The crop stops at y=895 of a 944-tall capture, above the
tab bar the Reminder log tab sits in, so the tab name is out of frame for the
whole piece. She also opens that tab at 40.0s of the recording, so the step-3
beat now ends at **39.15s** rather than running to 43.15s as it first did.

Everything else was refitted to match: the panel is 1080x980 at y=450, and
every crop is 1080:980 in aspect so it fills it exactly, with its size chosen
per beat rather than shared.

## The source is landscape, which is new

Every other piece this month came off her phone at 1080x1920. These are laptop
captures at about 1910x1040, so a full-frame fit would letterbox the whole
browser window into 1080x589 and nothing on it would be readable. Each beat
instead takes a crop of the part of the screen that matters and scales it into a
1080x980 panel at y=450, with the card carrying the step number above it and
the handle below.

Two things that came out of looking at the exported frames rather than the
plan: at a 760-wide crop the answer column ran off the right of the panel
mid-sentence, so the ChatGPT crops were widened to 771; and `cy` is chosen per
source so the **"Ask ChatGPT" composer bar falls below the crop**, per the
Oct 5 cleaning rule.

## Step 3 says what step 3 shows

Her note, Nov 17: *"step 3 audio should match what is being shown on the sheet
— or the other way around"*. It did not. The line named three summary figures
($59,380 scheduled, $13,300 paid, one overdue) that live on the **Summary tab**,
and the recording never opens that tab — it is the Payments tab from start to
finish. Checked frame by frame across all 45 seconds before changing anything,
rather than assuming.

**Both ends moved.** The voiceover now says *"every deposit and balance gets
its own due date and a colour: paid, due this week, overdue"* — three words that
are literally in the Flag column — and step 3 became **two beats in the order
the line says them**: the pasted rows while she describes the paste, then a cut
to the Flag column, with its green, amber and red cells, exactly on the three
words that name them.

The recording happens to run colours-first (they are in frame 23-30s, and the
sheet scrolls left afterwards), so the two halves are taken from different parts
of it rather than played in capture order. The payoff takes a third window,
26.60-29.37s, so no second of footage appears twice.

Both voiceovers were regenerated. 96 words, 32.37s and 32.91s.

## The cuts are timed to the voiceover's own pauses

Found with `silencedetect` rather than guessed. "One:" lands at 2.84s, "Two:"
at 5.48, "Three:" at 11.77, "Four:" at 23.92 and "That's it" at 32.57 — so each
step's footage starts exactly where Eryn names it, and the payoff holds for the
first 2.84s before step 1 exists.

Speed: step 2's wait is compressed 8.0x and step 4's analysis 7.0x, then both
settle to 1.0x on what came back. Steps 1 and 3 run at normal speed, because
the thing to watch is the click and the colours filling in.

## The script was extended from 76 words to 100, deliberately

The block asks for "about 70 words" **and** 35-45 seconds, and both cannot hold
at Eryn's ~3 words a second: the guide's own 76 words measured **25.2s**, which
would have left ten seconds of silence inside her own duration target. The
duration is the instruction — the block says "Sahiba's target for this one, so
the 20-second cap doesn't apply" — and the word count was a planning estimate.

The extra words narrate what the recording actually shows: eight emails and
seventeen payments, the three flag colours, and May 3. That is exactly what the
guide's own rule says to do with a short script. Instagram measures 32.37s,
TikTok 32.91s.

## The closing line, checked against the piece

Her Nov 14 rule took "Comment BUDGET" **off** the Tue 10 insurance Reel and the
Tue 17 BEO redo, because neither was about money. This one is the opposite
case: the Reel exists to sell the Vendor Payment System, the CTA is the
product's own, and the Thu 19 block specifies it. So `make_cards.py` asserts
the word BUDGET **is** present — the inverse of the assert the BEO generator
carries — and that the TikTok card says "on my Instagram", never "link in bio".

TikTok also ends on a 2-second card with `aiforeventplanners.gumroad.com` in
large type, as the block asks, because TikTok has no bio link to point at. The
address is split at the dot so it sets at 94px instead of shrinking to fit one
line.

## ManyChat

The BUDGET automation is attached by the browser Claude at 6:32pm, not from
here, and the Mon 9 automation comes off first — the free plan holds four at
once. After posting, send the brief with this Reel's permalink, because the
free plan attaches to one specific post.

## Approved, filed and scheduled

She approved it on Tue 17, two days ahead of the slot, after two rounds of
changes — the tracker framing and the step-3 mismatch, both above.

- Drive `November 19` (`1QbiCyJL5p2bj8EZZfQJ2LthAZxrOSLvW`) — both cuts, from
  **commit-pinned** raw URLs with each returned `size` checked against the local
  file. The superseded uploads were trashed, so the folder holds one version of
  each.
- Instagram and Facebook at **6:30pm Thursday**, one-shot task
  `trig_011TtmmvrC6ncALYbkMtjYST` (23:30 UTC). Its prompt carries the standing
  Reel-not-photo check, the ManyChat brief with this Reel's permalink, and the
  reminder to read the comments afterwards for anyone who commented BUDGET
  before the automation went live.
- TikTok handed over the moment she approved, with the caption pasted into the
  message. The last-10 duplicate check ran first and came back clear.

