# Thu 5 Nov — Vendor Payment System launch Reel

`launch-instagram.mp4` and `launch-tiktok.mp4`, both 1080x1920, 30fps, 21.9s,
H.264 high CRF 19 +faststart, AAC 192k at 48 kHz, audio measured at
**-13.96 LUFS / -1.27 dBTP** on the finished export.

The piece the $24 Vendor Payment System launches on. It went live on Gumroad a
day early, Tue 3: <https://aiforeventplanners.gumroad.com/l/epbvxs>.

## It runs 21.9s, not 15-20

The October default is 15-20s and a day's brief overrides it. This brief asks
for five things — the filled tracker as the payoff, the prompt, the answer, a
cut to the contract reader, and the end card — and the voiceover the block
specifies is 69 words, which is 21.9s in Eryn at 3.1 w/s. The alternative was
cutting a beat the block names. Time to payoff is 0s, so the six-second ceiling
is not in play.

## Four recordings, and why the answer comes from the second

| Take | Length | Used for |
| --- | --- | --- |
| 9:20 inbox sweep | 60.7s | **its opening two seconds only** |
| 9:35 inbox sweep | 49.4s | the answer |
| 9:51 tracker | 44.1s | the payoff and the amounts |
| 9:57 contract reader | 72.7s | the "10 business days" row |

**The first take's answer is not used, and the reason is the whole point of the
piece.** It put a card on screen reading `$59,180` still unpaid and `$72,480`
scheduled. Rebuilding all 17 payments from the eight vendor emails and summing
them in code gives **$46,080 and $59,380** — it was $13,100 over on both, about
the paid deposits counted a second time. The paid figure ($13,300) and the
entry count (17) were right, which is exactly what makes a wrong total
convincing. The tracker's own formulas agree with the code.

Her Prompt 1 now ends **"Don't add up totals; the tracker does the math."**

The second take has no totals card at all, lists all five near-term dates, and
says outright that it left the event-relative deadlines for the tracker to
calculate. It starts after the send tap, though — so the opening comes from the
first take, which has the prompt sitting in the input box and the tap on
camera. Same prompt, and the status bar crops off, so the join is invisible.

## Her three notes of Nov 3

**"Open on Vendor | Amount | Due date | Flag together."** Those four do not fit
across her phone in portrait. Hiding every other column on the tracker copy and
narrowing the four was not enough — two takes both pan rather than showing them
at once. She turned the phone sideways, which fits them, so `make_four.py`
rotates that take back with `transpose=2` and lifts the table out of it. The
result is a wide band rather than a full frame, which is what a four-column
table looks like at 1080 across; it sits on a blurred copy of its own frame.

**"Contract shot: zoom on the quote and May 3, 2027, overlay above the text."**
A straight crop cannot zoom this. The clause is three full-width lines of a
letter page on a phone, so a crop tight enough to enlarge the type clips the
line ends, and one wide enough to keep them is barely a magnification.
`make_clause.py` uses the house technique instead — isolate rather than
magnify: the Payment Schedule paragraph goes on its own panel over a hard blur,
ending "...no later than ten (10) business days before the event date", and the
table row carrying **May 3, 2027** in bold follows as its own beat. The card
moved to y=494, clear above the panel at y=840.

**"End on the tracker, not the keyboard."** The last beat is the same
four-column band, scrolled to the tail, with the Comment BUDGET card under it.

**"The prompt section still has two frames with the keyboard up. Start that
section on the sent message instead."** It now does. The beat came from the
9:20 take, whose opening holds the send tap on camera — the thing the house
rules ask for — but the keyboard comes with it, and she would rather see the
message. So the beat is the sent bubble from the 9:35 take, which also holds
the whole prompt where the input box held only its first few lines. **The 9:20
recording is now unused entirely.**

## The voiceover changed by one lineIt said "the ones coming up in the
next thirty days turn red". The tracker's conditional formatting colours only
three states — `Paid` green, `Due this week` amber, `Overdue` red — and on Nov 5
the nearest payment is nine days out, so nothing is amber or red. It now reads
"get flagged", which is what the Flag column actually says.

## The tracker was filled from here

`Vendor Payment Tracker — May 15, 2027 wedding` in Drive `November 5`, a copy
of the product tracker carrying all 17 payments. The block asks for the table
to be pasted in during the recording; pasting a 15-column table into Sheets on
a phone lands as one squashed column as often as not, and the cut is vertical
so she films on the phone. See `build/tracker.md`.

## The caption carries no prompt, deliberately

Every other caption ends with the prompt so the post stands without the video.
Here the six prompts **are** the product, so Prompt 1 stays out — and the
guide's own Thu 5 caption leaves it out too. See `build/caption.md`.

`Comment BUDGET` returns for this launch after being retired across nine failed
keywords, because this time a ManyChat auto-reply sends the Gumroad link back.
The TikTok caption points that CTA at Instagram, where the auto-reply lives.

## Build

    python3 make_beats.py     # six frames out of her four recordings
    python3 make_cards.py     # hook, contract and end cards
    python3 render.py         # preview, then both cuts

`make_beats.py` reads the recordings from `$LAUNCH_SRC` — **her footage never
enters this repo**, so only the finished cuts are committed. Every seek is an
accurate one (`-ss` after `-i`): fast seek snaps to a keyframe, and on 60fps
screen recordings that chose the wrong moment for three of the first seven
frames, one of which cut the dollar figures in half.

`render.py`'s `preview()` composites each card onto its own beat before any
export, and the export itself was re-checked frame by frame — the hook is gone
by 2.5s, which is the `repeatlast` bug the rules warn about.

## Approved Mon 3 Nov, scheduled for Thu 5 at 6:30pm Eastern

She approved the Instagram cut on **Mon 3 Nov** — the fourth revision, the one
whose prompt section opens on the sent message rather than the keyboard.

- **Instagram + Facebook: `trig_01U7uNzPKCQSBMGMangvWsx3`**, one-shot at
  2026-11-05 23:30 UTC, which is 6:30pm Eastern now that Eastern is EST. It
  fires into this session, because a fresh session gets no connectors and could
  not post at all.
- **Her TikTok reminder is separate**: `trig_011wQRgx9XUT5rbygLznb5vi`, slot 4
  of the week-1 timing test, same 6:30pm. The file and caption went to her at
  approval time under her Oct 30 rule, so the reminder is a second delivery, not
  the first.
- **Duplicate check before the hand-over**: the last 10 TikToks (Oct 25 → Nov 3)
  carry nothing from the Vendor Payment System. Nearest neighbours are the Oct 31
  expense-report cut and today's hidden-cost piece; neither is this.

**Filed to Drive `November 5`** (`1iH1FrGOq5cfqHBSY23AUSw_UJ0fJUqV_`), sizes
checked against the local files byte for byte:

| Cut | Drive id | Bytes |
| --- | --- | --- |
| Instagram | `1CpwhklZ75G4WJgI6_Fa15i0TyuW17zX2` | 2,160,425 |
| TikTok | `15xkPDoT8FGfErXCYLqHDa5boPLTz-tdz` | 2,188,092 |

**Struck in the guide on approval, not on Thursday**: her two Thu 5 recording
lines (both clips are in `November 5`) and "Check the Reel CC sends before it
posts." The CLAUDE CODE line stays open, because it ends "post to Instagram and
Facebook at 6:30pm after she approves" — half of it has not happened yet, and a
line is only struck for what actually happened as written.

Her three Thu 5 lines still open are the Story, the bio change to the product
page, and the TikTok upload itself.

## The TikTok cut's ending, rebuilt on her note of Mon 3 Nov

> "Change the CTA to 'Comment BUDGET on my Instagram and I'll send it to you,'
> and add a 2-second end card with aiforeventplanners.gumroad.com in large
> text. Same caption rule: no 'link in bio' on TikTok."

Two changes, **both TikTok-only**:

- **`end-tiktok`** replaces `end` on that cut. Three lines at 54px instead of
  two at 60, so the longer sentence still clears the bottom 25% — it ends at
  y=1364 against the 1440 line.
- **`url-tiktok`**, a full lavender frame carrying the address alone, held
  **2.0s after the voiceover stops**. The cut runs **23.92s**: 21.92s of body,
  then the card.

**The address is set on two lines, split at the dot.** On one line it fits
only at 57px — smaller than the hook cards, on the one frame whose whole job
is to be read and typed. Split, it sets at **101px** and still reads as one
address. The size is computed to the 992px gutter rather than typed, so it
cannot silently overflow.

**Why TikTok gets a URL card and Instagram does not.** TikTok has no bio link
to point at: the account is 901 followers short of the 1,000 the website field
needs, and the business route now demands IRS tax documents (checked Nov 3 —
the old free "Switch to Business Account" option is gone from the app). So on
that platform the address has to be in the picture. Instagram keeps the
shorter CTA, no URL card and no tail, because its bio link does the job.

**The tail is deliberate silence**, which the timing rules otherwise warn
against. It is two seconds of a card that exists to be read, not a dead hold
on footage, and `apad` extends the voiceover to the file length so `-shortest`
cannot clip the card off the end.

**The Instagram cut was not re-rendered.** She approved it on Mon 3 and it is
scheduled; it was restored from git byte-for-byte (2,160,425 bytes) rather
than rebuilt, because re-encoding an approved artifact risks a change for no
gain.

**The caption did not change.** Her rule is unchanged and the TikTok caption
already reads "Comment BUDGET **on my Instagram**", never "link in bio".

Checked on the export: −13.9 LUFS, −1.3 dBTP over the full 23.92s; the CTA
card is up at 19.0s and 21.5s, the URL card at 22.3s and 23.85s; frames in
`build/check3/`.

## The ManyChat "Comment BUDGET" automation

Both cuts end on **Comment BUDGET**, so the auto-reply is load-bearing on two
platforms — and on the free plan it **cannot exist until the Reel is live**,
because a free automation attaches only to an already-published post.

**It runs in her Chrome, not from here.** This session has no browser control
and no ManyChat connector: `request_computer_folder` serves a folder, not a
browser, and the container's own Chromium is a fresh profile with none of her
sign-ins. So the set-up is hers, and the only thing that matters is that she
gets the exact steps **at the moment the Reel goes live**, not hours earlier.

That hand-off is folded into the 6:30pm posting task
(`trig_01U7uNzPKCQSBMGMangvWsx3`), which posts first, then sends her the six
steps with **the new Reel's permalink pasted in** so she cannot attach the
automation to an older post. The settings:

| | |
| --- | --- |
| Path | Home → "Auto-DM links from comments" → **a specific post or reel** |
| Keyword | `BUDGET` |
| Public reply | on — "Sent! Check your DMs 💜" / "Just sent it to you!" / "Check your messages ✨" |
| DM | "Here it is: the Vendor Payment System, a tracker that flags every deposit and balance before it's due, plus the six prompts I use to fill it from my inbox." |
| Button | **Get the system** → https://aiforeventplanners.gumroad.com/l/epbvxs |

**"Any post" and "next post" are paid features** — picking either is how this
silently fails to work on the free plan. Every template extra (follow-gate,
email capture, upsell) is skipped, and no trial is started.

**Two things only this session can do**, both after she says it is live:

- **Name the early commenters.** Anyone who comments BUDGET between the post
  going up and the automation going live gets nothing, so the Reel's comments
  get read from here and those people handed to her to answer by hand.
- **Strike the guide line** — on her confirmation, never on sending the steps.

**The free plan is 25 DMs a month.** If she reports a warning, she is told
plainly and nothing is upgraded.

Her own account will not trigger the keyword, so the test needs a friend.
