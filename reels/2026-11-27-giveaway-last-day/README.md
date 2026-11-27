# Fri 27 Nov, 6:30pm — "Last day: 2 free copies."

The giveaway's closing Reel. Two cuts, 16.60s, from footage she already had.

## No new footage, by her decision

The Fri 27 YOU line asked for 4–6 photos of the author copies and a fresh
10–20 second flip-through, or a word that she would rather not film again.
She said so on Mon 23, and the guide line records it: cut from the Nov 19
flip-through, **IMG_0424 and IMG_0430** in Drive November 20.

**Her footage is not in this repo** — 58 MB and 170 MB of .MOV, read from
`$GIVE_SRC`. The repo is public and only finished cuts belong in it.

**IMG_0424 carries `rotation=-90` and IMG_0430 does not.** The first reports
1920x1080 and decodes as 1080x1920; the second is already 1080x1920. ffmpeg
applies the rotation itself, so both land on the output frame with no crop —
but the Oct 7 lesson is why that was checked rather than assumed.

## The cut

| | Instagram | TikTok |
| --- | --- | --- |
| both copies on the table | 0.00–3.20 | 0.00–3.00 |
| the flip-through | 6.00–10.00 | 6.00–10.20 |
| colouring the mandala | 18.00–23.00 | 18.00–23.00 |
| the page well under way | 89.00–93.40 | 89.00–93.40 |
| hook 0:00–0:02.3 | "Last day: 2 free copies. Closes 11:59pm tonight." | same |
| end card, last 3s | "Comment who you'd give it to. Closes tonight." | "Enter on my Instagram. Closes tonight." |

**16.60s**, 1080x1920, 30fps, CRF 19, AAC 192k at 48 kHz, `+faststart`,
**-14.0 LUFS**.

**It opens on both books**, which is the brief's own instruction — "payoff
first: both books in shot with the overlay in the first second". IMG_0424
opens on exactly that.

**The last seconds of IMG_0430 are out.** The clip ends on her turning to
camera, and this is a piece about the book rather than a piece to camera.
`render.py` asserts no window runs past 94.0s of it.

**The source audio is dropped.** Both clips have a room track; the voiceover
is the only audio, which also means nothing said over the filming goes out.

## The voiceover is longer than the brief's, deliberately

The guide's script is 35 words and ran 10.40s against a 16.60s cut — a five
second silent tail, which the Oct 1 rule calls out by name. The deadline and
the eligibility line were moved into the voiceover instead, 42 words and
**13.12s**, so the tail is 2.28s under the end card. `render.py` asserts the
tail stays under 2.5s rather than leaving it to judgement.

Eryn, `eleven_v4`, measured -22.6 LUFS / -1.5 dBTP, swept +9.5 → -14.9,
+10.5 → -14.3, **+11.0 → -14.1** into `alimiter=limit=0.891:level=0`.

## No sale on this Reel, on Black Friday

The guide is explicit: the only Black Friday discount is BLACKFRIDAY on the
Vendor Payment System, and "it goes in the Story, not in this Reel". There is
no coloring book discount at all (Sahiba, Oct 31) — the book is the prize,
not the offer.

`make_cards.py` refuses BLACKFRIDAY, BUDGET, a dollar sign, "off" and "sale"
on any card, because the one day this piece could drift is the day
everything else is on sale. It also asserts both cards still say "tonight",
so the piece cannot be reused on another date without failing the build.

**No music bed.** The voiceover carries it, and the day's 12:30pm
planner-feelings Reel has a bed of its own — her Nov 10 rule is that two
posts on one day never share one, and the simplest way to keep that true is
for this one to have none.

## Posting

- **Instagram and Facebook at 6:30pm Friday**, after she approves.
- **TikTok**, hers, at about 9am — different end card, and a caption that
  points entrants to Instagram because entries count there only.
- Her own Fri 27 lines: two Stories after the Reel, and the giveaway closes
  at 11:59pm. The draw runs Sat 28 at 9am.

## What went up

Fri 27 Nov 6:30pm ET. Instagram Reel https://www.instagram.com/reel/DgQ3Xi6hwO9/ (media 17914050123576095, `REELS`, shared to feed). Facebook video 1835516080999506. Commit-pinned source 1c2134b. Live caption diffed against `build/caption.txt`: identical. Pre-flight: neither platform carried this piece; Page feed read first.
