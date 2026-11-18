# Wed 18 Nov — "Every role has a captain, so nobody has to guess who to ask."

Content bank 28. Six slides, 1080x1920, **3.00s each after her Nov 17 note to
slow it down** — 18.00s in all, inside the 15–20s target. Brand look: lavender `#CECBF6`, deep
purple `#3C3489`, Poppins, EP✦ wordmark, numbered badge, bottom bar.

Built Tue 17 to her Wed 18 CC line, which asks for the slides and the
planner-feelings image a day early so she can check them Tuesday evening and
post the TikTok at 9am Wednesday — under the Sun 8 morning rule a cut has to
exist and be approved the night before.

## What it runs on

`Staffing Plan — Fall Product Launch`, Drive `November 18`
(sheet `11I47YKlbK4vt_FZWMgJyMYwwR636mhUarQhR3NNmaDo`), built Nov 16 by
`demo-files/2026-11/make_week5.py`. 600 guests, 40 staff in six roles, one row
per person; a second tab gives three escalation situations per role.

**The defect is deliberate and asserted in the generator**: Hospitality and
VIPs has two people marked "lead" and no captain, and the Escalations tab
leaves its captain cell blank rather than writing "NOT NAMED". So the gap has
to be derived from the Staff tab — which is the difference between AI spotting
a problem and AI reading a word.

## Slide 5 is derived here, and that is on the record

Nothing in this session can drive ChatGPT. The guide's CC line says to run the
prompt on the sheet and show what comes back, so the Registration card was
composed here and **every value on it is read out of the file** — Dana Ruiz,
channel 2, `(212) 555-0200`, and the three Registration situations verbatim
from the Escalations tab. `check()` asserts the captain, the channel, the
mobile, the staff counts summing to 40 and that exactly one role has no named
captain. The slide does not claim an AI wrote it, and her YOU line is to check
slide 5, which is the right check.

**Slide 3 was rebuilt to stop it spoiling slide 5.** The first version listed
each role with its captain's name and ended "VIPs — channel 7, and this is the
one with no captain", which hands over the catch three slides early.
`check()` now fails if any captain's name or the phrase "no captain" appears on
slide 3.

## The planner is "them"

Her instruction, Nov 17: *"change her to them"*. Slide 1 read "Nobody should
have to find her" and slide 2 "every question lands on her". `check()` now
fails if "her", "hers", "she" or "she’s" appears anywhere in the slide text,
so a later edit cannot put it back — the account says "event planner", and
gendering the one person in the story narrows who reads it as being about
themselves.

## The closing line, checked against the piece

Her Nov 14 rule. This is a piece about a staff briefing, not about money, so
there is no "Comment BUDGET" line on it — `check()` asserts the word BUDGET
appears nowhere in the slides, the same assert the Tue 17 BEO redo carries
after she pulled its CTA. Slide 6 closes on the takeaway and a save.

## Export

`render.py` — six slides at **3.00s**, hard cuts, 18.00s, 1080x1920, 30fps, CRF 19,
`+faststart`, AAC 192k/48kHz. No push and no crossfade: these are typeset
cards, not a scrolling answer.

**Its bed is its own.** Nylon-string guitar and a woodblock pulse over an
upright bass, upbeat per her Nov 10 instruction. Wednesday carries two posts
and they do not share a track — the 12:30pm planner-feelings Reel runs on
Rhodes and glockenspiel from a separate generation, because on Nov 11 both of
that day's Reels went out on one bed and she heard it at once.

Instrumental proved twice: the spectrogram shows percussive transients with no
sung-vowel formant movement, and Scribe returned an empty string. The
generation's own settings report `Instrumental: False` either way, so they are
not the check.

30.02s raw, trimmed 0.0–18.0s (full texture from the first frame), 0.8s fade
in, 1.2s fade out. It came out of the model hot: **-0.3 dB** of gain for -14.0
LUFS. Monday's needed -0.7 and Saturday's +0.2 — sweep it every time, and do
not assume the sign. **And re-sweep when the length changes**: the same 0 dB
measured -13.9 at the first 15s trim and -13.7 at 18s, because the loudness is
integrated over whatever you keep.

## Where it goes

- **Instagram and Facebook, 6:30pm Wednesday**, as a slide Reel. After posting,
  read the item back and confirm `media_product_type: REELS` — the Sun 15
  standing check.
- **TikTok, about 9am Wednesday**, the same six JPEGs as a photo carousel,
  from her, with the caption pasted into the message.

## Approved, filed and scheduled

She asked for the slides early on Tue 17 ("send me the slides now"), made two
changes and approved the same morning.

- Drive `November 18` (`1Vd-aqk-iMbGXTMkaXP3oGaa8kGvAjZos`) — the Reel and the
  six slides as `-tiktok-1.jpg` … `-6.jpg`, uploaded from **commit-pinned** raw
  URLs with each returned `size` checked against the local file. The three
  files her changes touched (the mp4 and slides 1 and 2) were re-uploaded from
  the new commit and the superseded copies trashed, so the folder holds one
  version of each.
- Instagram and Facebook at **6:30pm Wednesday**, one-shot task
  `trig_01MogsjyiWVyX2JiBmCpQ7Hf` (23:30 UTC — Eastern is EST now). Its prompt
  carries the standing Reel-not-photo check.
- TikTok carousel handed over the moment she approved, per her Oct 30 rule,
  with the caption pasted into the message. The last-10 duplicate check ran
  first and came back clear: Nov 10 to Nov 17 holds no staffing, escalation or
  briefing piece.

## Published

- **Instagram Reel, Wed 18 Nov 6:30pm Eastern** —
  [instagram.com/reel/Df5sQGQjUmF](https://www.instagram.com/reel/Df5sQGQjUmF/),
  media id `18117134804231948`, read back as `media_product_type: REELS` and
  `is_shared_to_feed: true`. The check matters most on a slide Reel, which is
  the shape that can land as an image.
- **Facebook**, post id `1479708740758559`. The Page feed was read first and
  held only the day's 12:30pm planner-feelings piece, so there was nothing to
  duplicate.
- The container sat `IN_PROGRESS` for about three and a half minutes before it
  read `FINISHED` — longer than any other cut this month, and the 18-second
  slide Reel is the largest file of the week. It published first time off the
  same container; nothing was rebuilt.
- Live caption identical to `build/caption.txt`, hashtags included. No BUDGET
  line and no ManyChat brief: this is a staffing piece, and `make_slides.py`
  asserts the word appears on no slide.
