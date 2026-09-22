# Coloring book reel — 2026-09-22

Status: **built, not posted.** Awaiting approval in the conversation.

The piece for *The Calm Before the Aisle*, a 50-page coloring book made with
AI.

**Built to `reel_script_1.txt`, not to the master guide.** The author asked
for that explicitly for this post. Where the two disagree, the script wins —
see "What the script overrode" below.

## Cuts

Both 1080x1920 (ratio exactly 0.5625), 30 fps, H.264 high, CRF 19,
`+faststart`, AAC 192k at 48 kHz.

| File | Platform | Duration | Voiceover | Ramp | Reveal held |
| --- | --- | --- | --- | --- | --- |
| `coloringbook-instagram.mp4` | Instagram, Facebook | 44.70s | -14.13 LUFS, TP -1.30 | 3.0x, 3.20s | 2.15s |
| `coloringbook-tiktok.mp4` | TikTok (manual upload) | 38.95s | -13.96 LUFS, TP -1.45 | 3.0x, 2.80s | 2.60s |

Two separate voiceovers, not one audio reused.

## The voiceover was re-recorded

The first take opened "This is a 50-page coloring book. I made it with AI."
The author flagged it twice: **"it" never names the thing**, and on mute or in
the first half-second a viewer has no idea what they are looking at. Both
voiceovers were regenerated so the object sits next to the verb:

- Instagram: "I made this 50-page wedding coloring book with AI in under
  three weeks."
- TikTok: "Stop thinking AI does the whole job. I made a 50-page wedding
  coloring book with AI in under three weeks."

The same pass fixed the one loose claim flagged earlier. It now says
**"Twelve pages had lines too thin to print"** rather than "12 pages too thin
to print" — pages are not thin, lines are, and the script's corrections
record is explicit about it. Both cuts now make identical claims.

Confirmed by transcribing the audio **off the finished mp4**, not off the
generator's echo of its own prompt.

### Pause tightening, not word cutting

The new Instagram take came back at 49.41s, over the script's 35-45s window.
Rather than cut any of the author's words, `build/tighten.py` compresses the
gaps *between* sentences to 0.59x and leaves every syllable untouched
(minimum gap 0.26s). That is 5.4s recovered from silence. The same factor is
applied to the TikTok take so the two cuts share a pace. The script reports
where every speech segment lands afterwards, and the shot and card timings
are set from that table rather than by eye.

## What the script overrode

- **Seven text cards, not two.** The script writes a TEXT line into every
  beat and they are all built. The guide allows only a hook and an end card
  and calls mid-video captions out as tested and worse for retention; the
  author set that aside for this post.
- **Length.** The script's 35-45s target, not the pre-Sep-23 16-20s.
- **Time to payoff.** If the payoff is the ChatGPT reveal it lands at 12.40s
  (Instagram) / 14.00s (TikTok), over the 6-second ceiling. The voiceover
  narrates the book first and the tooling second, so the reveal cannot move
  earlier without a different script. If the payoff is the finished book,
  it is on screen at 0:00.
- **Caption.** The script's caption verbatim, with no `AI Prompt:` block —
  the script's caption does not carry one.

The guide's rules on rendering, the ad check and posting approval were kept.

## Cards, verbatim from the script

| Card | Instagram | TikTok |
| --- | --- | --- |
| I made this 50-page coloring book with AI in under three weeks. | 0.00-2.60 | 0.00-2.60 |
| Three tools. One book. | 6.50-9.60 | 7.20-10.20 |
| The app's images: about $9 | 14.65-17.55 | 15.70-18.90 |
| The app itself: $183 | 17.75-23.00 | 19.10-24.60 |
| AI got me 90% there. | 24.55-28.60 | 25.25-27.30 |
| The last 10% is still you. | 33.20-36.60 | 27.55-30.00 |
| Now on Etsy / Amazon coming soon | 41.30-44.70 | 36.50-38.95 |

Two changes to the script's wording, both on the author's instruction:

- The script's beat-1 line is "I made this with AI in under three weeks."
  The author flagged that "this" never names the thing, so the card names it.
- The script says add "+ Amazon" only once it shows Live. The author says
  the print edition is coming shortly, so the card reads **"Amazon coming
  soon"** — true today, and it does not claim a listing that is not there.
  Swap it to "Now on Etsy + Amazon" the day it shows Live.

## TikTok has no bio link

Flagged by the author mid-build. The Instagram voiceover ends "Link in
bio"; TikTok profiles don't carry one, so the TikTok cut was given its own
voiceover ending on "The Calm Before the Aisle. On Etsy." and its own
caption. This is why the two cuts differ by more than a hook swap.

"Printable version in my bio" is on the Instagram caption only, and only
because the author confirmed on 2026-09-22 that the bio now points at the
book.

## The closing shot

The reel ends on the **digital cover** (`build/cover-digital.jpg`), composited
onto a 1080x1920 frame in the cover's own cream (#FBF7EE, sampled from the
file) with a slow push-in. The digital edition is the one that is live and
the one the bio points at, so it is the cover that matches the CTA.

The **print cover wrap** is in `build/CalmBeforeTheAisle_cover_wrap.pdf`
(back cover, spine, front cover, 8.5 x 11 with bleed). Its front panel is the
same bouquet with a different subtitle — "An Adult Coloring Book for Brides,
Bridesmaids & Wedding Planners", "50 INTRICATE PAGES · FOR COLORED PENCIL".
Swap it in once Amazon is Live and the CTA changes.

## The flip footage and the visible monitor

Three clips of the book being flipped were uploaded. Two of them
(`IMG_4033`, both takes) show a laptop monitor behind the book displaying
**this conversation, legibly** — including the author's own messages. A
200px top crop was tried and did not fix it: the text is still readable at
4.2s and later, well into mid-frame.

Neither `IMG_4033` take is used. The hook is `IMG_4030` instead, which is
clean — the book on a tiled floor, no screen anywhere in shot. It is
landscape 1458x1080 with rotation -180, so the 9:16 slice is
`crop=608:1080:850:0` upscaled 1.78x to 1080x1920. Checked at full size:
the line art stays sharp.

## The in-app ad

An **Adobe Firefly** ad scrolls into the bottom of frame during the reveal
clip. Bottom-strip frames at 0.2s steps: **clean at 6.4s, "Adobe Firefly
… Ad" legible at 6.6s.** The reveal cuts at **6.30s** on both cuts, with
margin, because the logo fades in — the Sep 21 lesson.

Verified **visually**, not by colour threshold, on the finished files: the
bottom 400px of every frame across the last 1.2s of each cut's reveal,
including the held frames. No ad in either.

## Structure

Eleven segments. Instagram timings; TikTok is the same shape, tighter.

| # | Beat | Source | Out |
| --- | --- | --- | --- |
| 1 | 1 | IMG_4030 0.00-6.15 | 0.00-6.15 |
| 2 | 2 | long SR 0.00-1.60 — prompt in the box, send tap on camera | 6.15-7.75 |
| 3 | 2 | long SR 1.60-11.20 @3x — generating | 7.75-10.95 |
| 4 | 2 | short SR 3.55-6.30 — into the reveal | 10.95-13.70 |
| 5 | 2 | freeze of short SR 6.28 | 13.70-14.55 |
| 6 | 3 | contact sheet, z 1.10-1.75 — all 50 pages | 14.55-20.60 |
| 7 | 3 | contact sheet, pan — close across pages | 20.60-24.20 |
| 8 | 4 | IMG_3940, push in — proof copy open | 24.20-30.20 |
| 9 | 4 | IMG_3939, push in — hand on a page | 30.20-36.60 |
| 10 | 5 | IMG_3927, push in — half-coloured page and pencils | 36.60-40.90 |
| 11 | 5 | digital cover, slow push in | 40.90-44.70 |

Shot assignment follows the script's beat list: contact sheet on the money
beat, proof copy open on the 90% beat, pencils page on the payoff. Cuts land
on the narration's beat boundaries, taken from a Scribe transcript of the
finished voiceover cross-checked against a silence map
(`silencedetect=noise=-32dB:d=0.28`). The 1.87s of lead-in silence is
trimmed so speech starts at 0.25s.

### Crop

`crop=1206:2144:0:478` for the two screen recordings — recomputed from this
source, not pasted: 1206 / 0.5625 = 2144, and 478 off the top clears the
status bar and the recording dot.

### Representative slice

The real generating phase runs past the end of the long recording — over 16
seconds, visually static the whole way. Segment 3 is a representative slice
of it at 3x, not the whole span compressed.

### The reveal hold

The generated page resolves at short-SR 5.0s and is then completely static
until the ad arrives at 6.6s, which leaves only 1.2s of live finished
image. Segment 5 freezes the last clean frame so the page is held long
enough to read — 2.15s on Instagram, 2.60s on TikTok. Nothing is faked; the
frame is the real one.

## Accuracy

Checked line by line against the script's own corrections record, against a
transcript taken from the finished files. Nothing outstanding: the earlier
"12 pages too thin to print" was re-recorded to "Twelve pages had lines too
thin to print", which matches the caption and the script.

Everything else matches: three sources not one style block, "under three
weeks" not two, "$9" scoped to the app's images only, "remade by hand in
ChatGPT" not drawn, and Etsy live with Amazon flagged as coming, not there.

## Sources used

| File | Used for |
| --- | --- |
| `b0cb03e7-IMG_4030.mov` | Beat 1 |
| `1448842b-…10-27-15AM_1.mov` (16.86s) | Beat 2, segments 2-3 |
| `b06cd7cf-…10-27-15AM_1_3.mov` (7.75s) | Beat 2, segments 4-5 |
| `images/13.webp` (2000x1294, 50 tiles) | Beat 3 |
| `99563f10-IMG_3940.HEIC` | Beat 4 |
| `b447192a-IMG_3939.HEIC` | Beat 4 |
| `b4bc3d31-IMG_3927.HEIC` | Beat 5 |
| `images/14.jpg` (2000x2000 digital cover) | Beat 5 close |

Unused: both `IMG_4033` takes (visible monitor), the second `IMG_4030`
upload, `4dba47df-…10-27-15AM_1.mov` (a smaller re-encode of the `b06cd7cf`
clip), and the print cover wrap (held for when Amazon is Live).
