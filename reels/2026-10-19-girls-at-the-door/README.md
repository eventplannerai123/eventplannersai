# The girls at the door — 2026-10-19

Status: **published 2026-10-19** at 6:04pm ET on her go-ahead ("its fine post
it"). She posts the same file to TikTok.

| Account | Post |
| --- | --- |
| Instagram `@aiforeventplanners` | https://www.instagram.com/reel/DesSa3qkok0/ |
| Facebook "The Event Planners AI" | https://www.facebook.com/reel/1635228448047752/ |

Instagram media `18010485146775660`, `media_product_type: REELS`,
`is_shared_to_feed: true` — a regular feed Reel. Container finished in 19.1s
over 7 checks. **Facebook surfaced on the second read-back**, feed entry
`1233196746554445_122116649343449533` at 22:05:02 UTC — 36 seconds after the
Instagram publish, nothing retried in between.

**Both live captions compared character for character against
`build/caption.txt`: identical**, 852 bytes, four literal `#`, no `%23`, no
"Hashtags:" label.

Before posting: the raw URL returned 200 at exactly the committed byte count
(3,907,939), and both duplicate checks came back clean, newest entry on each
being the Oct 18 bar quantities cut.

**A stale container was left unused.** One was built for the silent version
before she asked why it was silent; it was abandoned rather than published, and
a fresh container built for the voiced file. Containers are single-use, so
reusing it would have posted the silent cut.

**This went out at 6:04pm, not in the morning.** Her Oct 16 rule puts a day's
only Instagram post in the morning; this one ran late because the photo edit,
the colour change and the voiceover all landed during the day. Worth knowing
when the numbers are read, and not a precedent.

| | |
| --- | --- |
| `girls-at-the-door.mp4` | 1080x1920 (0.5625 exactly), 30 fps, H.264 High, CRF 19, `+faststart` |
| Duration | 15.00s — the top of the brief's 12–15s |
| Audio | **Vanessa voiceover**, −15.42 LUFS, −0.85 dBTP |

Content bank: her own 2007 door story. **Never name the company, the client or
the blog** — the brief says so and nothing in the piece or the caption does.

## One still, a push-in, four cards

The brief specs the edited `IMG_0853` registration-table photo with a slow
push-in and nothing else moving.

| Beat | Holds | Card |
| --- | --- | --- |
| 0.0–4.0 | 4.0s | A gossip blog once said the girls at the door were "in way over their heads." |
| 4.0–7.0 | 3.0s | I was one of the girls at the door. |
| 7.0–11.0 | 4.0s | Here's how I'd fix that guest list today. |
| 11.0–15.0 | 4.0s | the prompt |

**The last two beats differ from the brief by one second.** It writes them as
7–12 and a 3-second prompt hold. A second was moved from the third card to the
prompt because three seconds cannot carry a readable prompt, and the prompt is
the payoff.

**The on-screen prompt is condensed, and the caption carries it whole.** The
real prompt runs about 45 words; nobody reads 45 words in four seconds while
also looking at the room. The card states what the prompt does in 16 words and
the caption states it in full, one scroll down — so nothing is withheld, it is
just not all on screen at once.

## The framing was rebuilt once

The still is 1536x2048 (3:4) and the frame is 9:16, so a window has to come out
of it. The widest one — 1152x2048, full height — was built first and thrown
away: it keeps the entire floor, so the tables sit in a band across the middle
under a wall of nothing, with the half-cropped cocktail table blobbing into the
bottom-left corner. It read as a photograph of a floor.

| | Opens on | Lands on |
| --- | --- | --- |
| Window | 1008x1792 at (470, 90) | 864x1536 at (610, 230) |
| What is in it | the room, the door, the whole table run | the check-in run, the navy runner, the door |

`zoompan` 1.00 → 1.167 across the full 15s, with the sampled centre drifting
68px right and 12px down. **The move is the story**: open on the room, end on
the door. The opening sample is 1008 wide against a 1080-wide output — a 1.07x
upscale — and only the final frame reaches 1.25x, so the softest moment is the
one nobody is still reading.

Motion runs from frame one, so this is not a static title card even though the
source is a still.

## The photo: de-branded here, not in ChatGPT

The guide's Mon 19 YOU line asks her to edit `IMG_0853` in ChatGPT and send it
over. She asked for it to run from here instead ("You can do it on your own"),
so it did — ElevenLabs `creative_edit_image`, `gpt-image-2.5-sunburst`, the
original as a reference node.

**The shortlist's edit line was not enough.** It covers only "the wall of
portraits and all lettering". The frame also carried a client-branded runner
down the front of the check-in table and a named room sign above the door, both
as identifying as the wall. All three came out.

**She then asked for the runner's colour to change as well**, and she was right
to: purple was the client's colour, so a plain purple runner still pointed at
them. It is navy now. Approved on 2026-10-19 ("APPROVED").

Two notes worth keeping:

- **The first run came back 16:9 at 1K** — the model's defaults, not the
  reference's shape — which is useless for a vertical Reel. `creative_edit_image`
  takes no aspect argument; set `aspect_ratio` and `resolution` through
  `creative_update_node` and then run the node with `creative_run_flow_nodes`.
  3:4 at 2K gives 1536x2048, which is enough for a 9:16 crop with push-in
  headroom. 4K was estimated and dropped as unnecessary.
- **Taking the portrait wall out leaves that side of the room bare.** Flagged to
  her rather than fixed, because the piece is a push-in with text over it and
  the wall is backdrop. If it ever reads as too empty, something neutral goes
  back on it.

`build/frames/door-still.png` is committed. It is not raw footage under the
repo rule: there are no faces, no branding and no venue name left in it, and it
is exactly what the public video shows.

## It shipped silent for about an hour, and then it did not

The brief says "No voiceover — the overlay and caption carry it", which is the
Oct 5 rule-1 exception for an overlay-led piece, so the first build was silent.
It was flagged to her, she said go ahead, and then — with the container already
built and not yet published — she asked **"why is it silent though"**.

That is the same objection she made to the Oct 6 cancellation piece, which
"made no sense without sound". **The standing preference beats the day's
brief**, and flagging silence is not the same as arguing against it. Nothing
had been published; the container was abandoned rather than used.

She approved a 39-word script and said to keep the overlays as they are.

| | |
| --- | --- |
| Voice | Vanessa - Beach Girl (`8DzKSPdgEQPaK5vKG0Rs`), `eleven_v4` |
| Takes | 2 — 14.72s and 13.04s. **The shorter one was used**, because it leaves the last 1.96s quiet under the prompt card: a beat under the payoff, not a dead tail |
| Level | take measures −27.05 LUFS → +13.05 dB, `alimiter` at −1.0 with `level=0` |

**The export measures −15.42 LUFS, not −14.** Speech-only measures the same, so
the tail is not the cause: true peak sits at −0.85 against the limiter's −1.0
ceiling, and more gain only buys more limiting. This is the documented case
where loudnorm's true-peak ceiling binds first — Sep 25 stalled at −15.8 and
was accepted. Measured on the finished export, not assumed.

### The card timings moved, the cards did not

Adding a voice forces this: the windows had to shift or the text would leave
while the voice was still saying it. Her instruction was to keep the overlays
as they are, which is about the words.

Boundaries were **measured off the take's own energy envelope**, not guessed —
20ms RMS windows, gaps found against the file's own noise floor:

| Voice says | Card |
| --- | --- |
| 0.16–4.16 | 0.0–4.4 |
| 4.70–5.64 | 4.4–6.8 |
| 6.04–10.26 | 6.8–10.9 |
| 11.06–13.04 | 10.9–15.0 |

Every card boundary falls inside a gap between sentences. Card 2 is held 2.4s
rather than the 0.94s its line takes to say, because the card carries the long
form ("I was one of the girls at the door") where the voice says the short one
("I was one of them").

Verified on the export's own audio envelope as well as its frames.

## Caption

`build/caption.txt`, the brief's TikTok caption verbatim, used for Instagram
too. Four literal `#`, no "Hashtags:" label, no retired "Prompt below." line.
The prompt sits inside the caption body rather than under an `AI Prompt:`
label, which is how the brief writes it.

## Checks

- 1080x1920, ratio 0.5625 exactly, 30 fps, 15.00s — ffprobe'd on the export.
- All four cards verified on **exported** frames at 0.2 / 3.8 / 4.3 / 6.6 /
  7.4 / 10.6 / 11.4 / 14.8s. Every one holds its whole window and hands over
  cleanly. That is the `repeatlast` class of bug, which only the export shows.
- Every card asserted inside the safe band (y 259–1401) by `make_cards.py`
  itself, so a reworded line that grew too tall would fail the build rather
  than drift into TikTok's furniture.
- Audio envelope of the export read back in 0.5s windows: speech in four runs
  with real gaps at 4.0–4.5, 5.5–6.5 and 10.5–11.0, silent from 13.5. The card
  boundaries land in those gaps.
- No ad check needed: there is no screen recording in this piece.

## Who posts what

| | |
| --- | --- |
| Instagram + Facebook | from here, after her go-ahead |
| TikTok | **hers**, same file, same caption |
