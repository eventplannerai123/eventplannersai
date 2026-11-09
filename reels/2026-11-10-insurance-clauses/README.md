# Tue 10 Nov — insurance clauses in a venue contract

Redo-free original (content bank 6). Instagram + Facebook at 6:30pm Eastern;
TikTok at about 9am, by her hand, from the file sent the evening before.

| | |
| --- | --- |
| Cuts | `insurance-clauses-instagram.mp4`, `insurance-clauses-tiktok.mp4` |
| Length | 18.96s both, inside the brief's 15–20s |
| Export | 1080x1920, ratio 0.5625, 30fps, H.264 high, CRF 19, +faststart |
| Audio | Eryn (`kdnRe2koJdOK4Ovxn2DI`, `eleven_v4`), **-14.03 LUFS, -1.26 dBTP** |
| Source | her 1206x2622 iPhone capture, 68.9s, 60fps, no rotation side data |
| Crop | `crop=1206:2144:0:478` then `scale=1080:1920` |

## The answer ranked the mismatches differently from the brief

The brief leads on liquor liability. ChatGPT found that and three more, and
put the **policy's expiry date above it**: the certificate runs out on 31
March and the event is 17 April, so the cover lapses 17 days before the gala
and never reaches the load-in or load-out the contract requires.

What it caught, as "3 major insurance gaps + 1 additional coverage issue":

| Requirement | Contract | Certificate |
| --- | --- | --- |
| General liability | $1M / $2M | $1M / $2M — **matches** |
| Liquor liability | $2M minimum | $1M per common cause |
| Additional insured | venue, owners, officers, employees, agents | box unchecked |
| Waiver of subrogation | required | marked NO |
| Coverage period | event, load-in, load-out | expires 31 March 2027 |

It also wrote the broker email, pushed back on the indemnification clause
unprompted-but-asked, and flagged the vendor-insurance section — which is
what makes the last beat work.

So the voiceover is written around **its** ranking, not the brief's. The
hook keeps the brief's approved line, because the liquor gap is still real
and it is the sentence Sahiba approved.

## The twist is hers, and she confirmed it

It tells her to raise **her own** liquor limit to $2M. The caterer usually
holds the liquor licence, so the fix is the caterer's certificate naming the
venue, not a bigger policy of hers. Asked on the day, she agreed with that
reading, so it is the last line of the voiceover:

> It tells me to raise my limit. But usually that's the caterer's license.

The beat it plays over is the answer's own **Vendor insurance — Page 4,
Section 5** section, which ends "this means your own certificate does not
satisfy the vendors' obligations". The answer gets within one step of her
point without taking it.

## Beats

| Beat | t | What it shows |
| --- | --- | --- |
| b0-prompt | 18.50s | the sent prompt, both PDFs attached |
| b1-gaps | 22.50s | the review headline, both badges, the four issues |
| b2-table | 32.50s | liquor, waiver and the certificate date, side by side |
| b3-expiry | 36.50s | Issue 1, highest priority: 17 days before the gala |
| b4-raise | 41.50s | "Increase liquor liability to at least $2 million" |
| b5-vendor | 63.50s | vendor insurance: her certificate is not the fix |

**The beats are selected by frame number, not by a time window.** A first
version used `between(t,T,T+0.02)`, which at 60fps spans one or two frames
rather than exactly one: six windows matched eleven frames, `-frames:v 6`
kept the first six, and every beat after the second was silently the wrong
picture. `eq(n,N)` matches one frame per beat. Caught by looking at the
frames, which is the only check that would have caught it.

One decode for all six, too: accurate seeking re-decodes from the start of
the file each time, which on this source is about fifteen seconds a frame.

## Cards

Hook at 0:00–2:30, end card in the last 3s, nothing in between — the house
rule, and both current briefs override the two-overlay default down to one
plus the closing card.

**The end card is the BUDGET line and it substitutes.** The guide's Nov 3
soft mention says to end this Reel on "Comment BUDGET for the tracker I use"
*instead of* the usual closing line, so the brief's own takeaway overlay
("Check the certificate against the contract. Then confirm with your
broker.") is replaced rather than appended to. TikTok says "on my
Instagram": no bio link there, and the automation lives on Instagram.

**The end card sits high on this one**, at y=250, which is the opposite of
Mon 9. The last beat's whole job is the vendor-insurance section from about
y=750 down, so the card goes above it over the leftover indemnification
text. The hook sits at y=1200 and takes the prompt bubble's last line; the
first nine lines of the prompt stay readable, which is why the cut opens on
that frame at all.

**Both cards are opaque, not the usual 243 alpha.** Every card on this piece
lands on a dense paragraph rather than white space, and at 243 the text
underneath showed through the lavender in the exported frames.

## Checks

- **Ad check clean.** Nine advertisers have turned up in these recordings so
  far, so this was scanned twice: the whole 69s source at 1fps over the
  bottom 460px, and then the exported mp4's bottom 340px at 1fps through to
  its final frame. No ad anywhere in either.
- Hook verified present on the **exported** frames at 1.0s and 2.0s and gone
  by 2.6s; end card present at 17.5s and on the last frame, absent at 15.5s.
- Loudness measured on the finished exports, not on the voiceover.
- **The gain was swept, not computed.** Eryn came out at -25.24 LUFS with
  peaks at -3.09 dBTP, and the arithmetic +11.24 dB lands at -15.37 after
  `alimiter=limit=0.841:level=0`. It took **+14.0 dB** to measure -14.02.
- The first voiceover ran **21.1s**, past the brief's 20s ceiling, so the
  script was cut from 57 words to 52 and regenerated at 18.96s. 52 words in
  18.96s is 2.74 w/s — well under the 3.1 w/s planning figure, because this
  script carries an em dash and two full stops the planning figure does not.
