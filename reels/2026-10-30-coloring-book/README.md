# The Calm Before the Aisle, part 2 — Fri 30 Oct

Two cuts, 27.2s each, 1080x1920. First feed post about the book since Sep 22,
which is still the second-best Instagram post the account has had.

| | |
| --- | --- |
| Voice | Eryn (`kdnRe2koJdOK4Ovxn2DI`, `eleven_v4`), the guide's 72-word script verbatim |
| Hook | Instagram "50 wedding pages. Made with AI. Coloured by hand." / TikTok "Stop buying another candle." |
| Takeaway | "Printable PDF on Etsy. Paperback on Amazon." |
| Caption | `build/caption.txt`, hash `bfd3d5a0` — the guide's own, 8 hashtags rather than the house four |

## The author copies have arrived, and nobody said so

The brief is written for a world where they had not: *"the author copies had not
arrived as of Oct 15, so CC builds it from photos Sahiba already has"*, with a
conditional — *"if the author copies arrive by Wed 28, Sahiba films a 10-second
flip-through and CC uses it as the opening shot."*

They arrived. `IMG_3939.HEIC` landed in Drive `October 30` on **Oct 28 at
8:12pm**, and it is unmistakably a physical paperback in her hand. So the
flip-through is live rather than moot — it is still on her list for today, and
it would make a better opening than a still. The Reel is built complete without
it, so it is an upgrade she can decline.

## Sources, and the one the brief names that does not exist

- **Her photo**, `IMG_3939.HEIC`, 4284x5712 — the full-size file, not the
  downscaled copy that came through chat. Opening beat on Instagram, closing
  beat on TikTok.
- **`CalmBeforeTheAisle_interior_102pp.pdf`** (`1Ner_-szB1ZOCT3RWsiztpXS06VulJK4l`),
  rendered at 200 dpi. Seven pages: dress (17), bouquet (25), planner's kit
  (47), guest book (61), ring box (3), aisle (57), title (1).
- **`story_etsy_book/` is not in Drive.** Checked again today: the `Coloring
  book` folder holds the two PDFs, a `pintrest` subfolder and one test PNG, and
  there is no folder by that name anywhere. It has now been looked for twice, so
  **stop treating it as a source** — the brief's other two halves carry the piece.

Page 47 is the one her photo shows her colouring, so it sits under "the planner
who's been staring at a seating chart since March".

## Why the pages sit on lavender instead of filling the frame

A letter page is 0.773 wide-to-tall against the frame's 0.5625, so filling the
frame crops 231px off each side of the page. Measured ink margins at 200 dpi run
from **100px on page 47** to 298px on page 65 — so a fill would cut 131px into
the walkie-talkie drawing, the one the whole piece is anchored on.

The brief says "slow pans across pages". A pan that amputates the art is not
worth the motion, so the whole page sits on the brand lavender and the movement
is a slow push-in. It also leaves clean bands for the two overlays.

## The beats are cut to the sentences

`silencedetect` at -32dB puts the voiceover's gaps at 5.13, 7.87, 10.85, 14.31,
16.52, 19.29, 19.95, 21.44 and 22.86. With a 1.2s lead-in every beat change
lands inside one of them:

| From | Beat | Line |
| --- | --- | --- |
| 0.00 | her photo | "I made a fifty-page wedding coloring book with AI" |
| 6.60 | dress | "for the bride in the worst month of planning" |
| 9.30 | bouquet | "the bridesmaid who needs something that isn't another candle" |
| 12.45 | planner's kit | "the planner who's been staring at a seating chart since March" |
| 16.05 | guest book | "Every page is a piece of the day:" |
| 18.30 | ring box | "the ring box, the bouquet, the dress," |
| 20.70 | aisle | "the aisle." |
| 23.00 | title page (IG) / her photo (TikTok) | "paperback on Amazon." |

## 27.2s, not the brief's 30-40

Eryn reads the 72-word script in **23.07s** — 3.1 words a second, exactly the
planning figure in CLAUDE.md. Stretching to 35s would mean ten seconds of
silence, and the rule is to prefer the lower end when the voiceover is short.

## Two bugs worth keeping

**`zoompan` with a looped input runs forever.** `d` is frames per *input* frame,
so `-loop 1 -t 6.6 -i photo.jpg` fed it 198 input frames and it produced 198
beats' worth. `concat` never reached beat two and the first build was 27 seconds
of the photo alone — and it exported cleanly, so only looking at the frames
caught it. Feed **one** frame per input and let `d` set the length.

**The loudness gain is not the arithmetic one.** First pass reads I=-23.53,
TP=-1.53, so +9.53 dB nominally reaches -14 — but limiting eats loudness, and
measured back that lands at -15.82. 11.2 dB gives **-14.92 LUFS, TP -1.27**,
which is what shipped. 12.0 dB would have reached -14.51 and squashed LRA from
the source's 3.40 to 1.90, audibly flat for 0.4 dB.

## Who posts what

Instagram and Facebook at **6:30pm Eastern**, from here, after she approves.
TikTok is hers, with the caption pasted into the reply.

## Live

Posted Fri 30 Oct at 6:30pm Eastern (22:49 UTC), after her approval that
morning ("approveed").

| | |
| --- | --- |
| Instagram | [reel/DfIsWj7EoxU](https://www.instagram.com/reel/DfIsWj7EoxU/) — media id `18108623522253576`, `is_shared_to_feed: true` |
| Facebook | video post id `1107534105506019` |
| TikTok | hers, confirmed 2026-10-30 ("posted to tik tok") — [video/7702450973213494542](https://www.tiktok.com/@aiforeventplanners/video/7702450973213494542) |

Live Instagram caption read back and diffed against `build/caption.txt`:
identical, line breaks and all eight hashtags intact.

**The publish call timed out and the Reel went up anyway.** `INSTAGRAM_POST_IG_USER_MEDIA_PUBLISH`
hit the 60s MCP ceiling with no result. The container read `FINISHED` and the
media edge showed nothing, which looks exactly like a failure; a second read a
minute later had the Reel live, timestamped 22:49:47 — the publish had
succeeded server-side the whole time. A retry at the first read would have
double-posted. **A timeout is UNKNOWN, and one empty media-edge read is not an
answer.**

**The hash recorded for the caption in the scheduling task was wrong.**
`build/caption.txt` has never changed since the build commit and its md5 is
`623d06c5`, not the `bfd3d5a0` the task carried. The text itself was verified
against the live TikTok description, which she posted from the same file.
