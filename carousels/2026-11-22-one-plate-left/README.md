# Sun 22 Nov, 6:30pm — "Only a few plates left and a line. How embarrassing."

**The headline changed when she saw the photo** (Nov 19: "the first slide has
more than one plate. say only a few plates left"). The guide had written "One
plate left" months before anyone had a picture, and the picture has a stack of
clean plates in it. The overlay, the caption's first line and all three
mentions in the guide now say "Only a few plates left"; `check()` asserts the
old wording cannot come back.

Six slides, content bank 38, third in the conference catering series after
runny eggs and dry sandwiches. One set at 1080x1920: a slide Reel for
Instagram and Facebook, the same slides as a photo carousel on TikTok.

## Slide 1 is her photo, and the guide's one wasn't real

The Sun 22 CC line asked for `event-one-plate-left-blurred.jpg`, "sent in chat
Oct 26". **It does not exist** — not in Drive under any title, not in
`Event photos`, not in this repo, and the Oct 26 conversation is gone with the
container. [`docs/SUN-22-PHOTO.md`](../../docs/SUN-22-PHOTO.md) has the full
check.

She sent a better one on Thu 19: two chafing trays scraped down to smears of
egg, a bacon tray with three rashers left, tongs lying in it, and a stack of
clean plates beside them.

- **No faces, no lanyards, no logos, no signage.** One person stood in the
  right eighth of the frame, cropped to a torso.
- **That strip is cropped off, not blurred.** A blur patch was tried first and
  read exactly as the Oct 10 note warns — a censor smudge with a hard
  rectangular edge. The crop loses a second chafing dish and some marble.
- It is landscape 1448x1086, so it sets as a full-width panel with the
  headline above and the line below, rather than a 9:16 crop that would keep a
  third of the width.
- **The source is not in this repo**, which is public. It lives in Drive
  `November 22` as `event-one-plate-left.jpg`
  (`1wYWoCsIiOQPNXzPRva1lVq0-rCAMGMky`), converted to JPEG per her Oct 25 rule;
  `make_slides.py` reads a scratch copy.

## Slide 5 is derived from the BEO

The prompt was run for real against the file's text — claude-opus-5-5 on the
ElevenLabs flow, Thu 19 — as a check that the piece's claim stands up. **That
node's text cannot be read back from this session**, so the sheet on the slide
is composed from the BEO's own values, and `make_slides.check()` re-asserts
every one of them against `demo-files/2026-11/make_week6.py`: the seven
stations, their service windows, their refresh times, the busiest hour and the
two flags. The slide does not claim an AI wrote it. Her YOU line is to check
slide 5, which is exactly the right check.

## The flag test is the gap between WAVES, not between walks

Caught while writing the caption, and it changes the answer:

- The captain walks **every 15 minutes** in the busiest hour — 6:30, 6:45,
  7:00, 7:15, 7:30.
- A station is flagged when its refresh runs longer than the **30 minutes
  between the first two guest waves**, because then it is still being rebuilt
  when the next hundred people walk in. That is the raw bar at 40 and the
  crudités display at 35 — **two**, which is what the guide's "what it should
  catch" says.
- Against the 15-minute walk gap, **four** would flag (pasta and dessert join
  at 20). An earlier draft of this generator said "longer than the gap between
  walks" and would have put a wrong number on the slide.

Both files now assert it from both directions: two flags against the wave gap,
four against the walk gap, so neither can be quietly swapped for the other.

## The rest

- Slide 4 carries **the guide's prompt word for word**, so the slide and the
  caption cannot drift apart.
- Slide 3 is what the captain does — walk, call at half full, know the refresh
  times, have the backup ready.
- No BUDGET line: a catering piece, not a money one, and `check()` asserts it.
- The planner is "them", never "her" — her Nov 17 instruction, asserted.
- Thorne Hall and Marchetti Hospitality are invented and appear on no slide.

## The Reel

Six slides at **3.00s** = **18.00s**, 1080x1920, 30fps, CRF 19, AAC 192k/48kHz,
**-14.05 LUFS**. The Sun 22 line says "about 2.5 seconds a slide"; 3.00 is what
she asked for on Nov 17 ("slow down the reel a little") and approved on the
Wed 18 set. Slide 5 is why it matters — seven sheet rows, the busiest hour, a
walk schedule and the flag is more to read in one beat than anything else here.

Hard cuts, no push, and slide 1 does not move either: a slow zoom on a still
photograph is the oldest tell there is.

The bed is its own generation — vibraphone over upright piano and plucked
double bass — instrumental by spectrogram and by Scribe returning an empty
string, trimmed 0-18s, **-0.55 dB** into the limiter. It came out of the model
hot, where Friday's needed +4.05, which is why the gain is swept every time.

## Posting

- **Instagram and Facebook at 6:30pm Sunday**, as a slide Reel, after she
  approves.
- **TikTok at about 9am**, hers, the same six slides as a photo carousel.
- Her Sun 22 block also has a Story to planners about bulk author copies.
