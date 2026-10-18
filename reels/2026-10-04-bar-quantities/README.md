# Bar quantities — TikTok quick piece, 2026-10-04

Status: **built, handed over** on Oct 4 — TikTok only, and TikTok is always
her upload. Nothing went to Instagram or Facebook on the day; the guide's Sun 4
row had no Instagram piece.

## Published 2026-10-18 to Instagram and Facebook — the day's second post

| Account | Post |
| --- | --- |
| Instagram `@aiforeventplanners` | https://www.instagram.com/reel/Depw19ACVdb/ |
| Facebook "The Event Planners AI" | https://www.facebook.com/reel/1630598911879889/ |

Went out at **6:32pm ET** (22:32:36 UTC), behind the runny eggs carousel at
9:05am. Instagram media `18128832925856211`, `media_product_type: REELS`,
`is_shared_to_feed: true` — a regular feed Reel. The live caption was read back
and diffed against `build/caption-instagram.txt`: **identical**.

This is the 6:30pm slot used as her Oct 16 rule intends it — the evening is
only ever a day's second post, and the day's main one went out in the morning.

Posted on her Oct 16 go-ahead ("yes to the second post") and her Oct 17 choice
of the voiced version over shipping it silent ("voiceover"). The file is
`barquantities-instagram.mp4` — md5 `add84f567f8b8c4e273b0a114083ad36`,
4,681,746 bytes, confirmed 200 at that exact byte count before posting. Both
duplicate checks were clean: the piece had never been on Instagram, and the
morning carousel was up on both platforms.

**The publish call timed out client-side at 60s and the post had in fact
succeeded.** Exactly the Sep 18 failure mode, and the reason the rule is read
state, never blind-retry: the media edge was read and the Reel was already
there at 22:32:36. Nothing was retried. `max_wait_seconds` was 55, inside the
under-60 rule, and the timeout was the MCP client's own, not Instagram's.

**Facebook surfaced on the second read-back**, feed entry
`1233196746554445_122116500765449533`, created 22:33:24 UTC — 48 seconds after
the Instagram publish. It was absent on the first read, which is normal for
that endpoint; nothing was retried in between, because it has no duplicate
protection and a live page post cannot be taken back. Its live caption was
compared character for character and is **identical** at 192 bytes.

**The guide's Sun 18 block says to use the existing cut with no re-edit**, and
that is honoured on the part a re-edit would damage: the picture is `-c:v copy`
from the Oct 4 export, bit-for-bit. Only a voice was added.

Two things flagged to her rather than fixed quietly:

- ~~**It is silent.**~~ **She chose the voiceover** on 2026-10-17, so the
  Instagram post is `barquantities-instagram.mp4`, not the silent TikTok file.
  See below. The silence was real — `astats` reported an RMS of `-inf` — and
  it predated the **Oct 5 video lessons** by a day; rule 1 exists because she
  said of the Oct 6 cancellation piece that it "made no sense without sound".
- **Instagram has not seen it**, which is the whole point of the repost, but
  the scheduled run checks the media edge live before posting rather than
  trusting this line.

The first of the October plan's five **TikTok-only quick pieces**. They exist to
test whether TikTok rewards volume, they cost about ten minutes of her time
each, and the plan says that if they perform anywhere near the full pieces that
is the most important finding of the fortnight.

| | |
| --- | --- |
| `barquantities-tiktok.mp4` | 1080x1920, ratio exactly 0.5625, 30 fps, H.264 high, CRF 19, `+faststart` |
| Duration | 12.20s |
| Audio | **silent** — a quick piece has no voiceover |

## The format is deliberately not the usual one

Per the guide: the prompt as the opening card held 3 seconds, then two key
moments of the answer held long enough to read, **no hook line and no end
card**. So the only overlay in the piece is the prompt itself. That is the one
case where the two-overlay default is overridden downwards to one, and the
overlay is not a hook.

Three beats, each a 0.20s dissolve rather than a hard cut:

| Beat | Source | On screen |
| --- | --- | --- |
| 0.00-3.00 | 0.30 | the prompt in the input box, send tap, prompt card |
| 3.00-7.20 | 4.60 | 5 drinks per guest, ~1,000 drinks total |
| 7.20-12.40 | 9.20 | the recommended order table |

Beats two and three zoom slightly (1100 wide against the full 1206) and shift
down the source, so the paragraph and then the table sit centred. Beat one keeps
the whole screen because it has to show both the prompt and the send.

**A silent AAC track is muxed on.** The piece has no voiceover, but an mp4 with
no audio stream at all is worth avoiding on upload.

## The card sits at y=1420

Not the usual 620. This opening exists to show the prompt sitting in the input
box, which lands around y 660-940 of the output frame — a card at 620 would
cover the one thing the shot is for. 1420 sits over the keyboard, which carries
no information, and still clears TikTok's own bottom furniture. Same call as
Sep 29 and Oct 1, and verified on the exported frames rather than from the
filtergraph.

Worth noting the card restates a prompt that is already legible on screen. That
is intentional: the input-box text is small at phone size, and the guide asks
for the prompt as an overlay.

## The recording

27.0s, 1206x2622 at 60fps HEVC, 27.9 MB, via Drive. The standard iPhone capture
size, so `crop=1206:2144:0:478` applies unchanged.

**It opens exactly right** — the prompt sitting in the input box with the send
tap on camera. Checked before choosing the cold open rather than assumed.

## Ads

**A seventh advertiser**: Fever, "Private corporate events", which scrolls up
into frame from about t=24 in the source. Both of the last two beats end well
before that — the final frame is source t≈14.6 — and the bottom strip of the
exported final frame was checked visually and is clean.

## There were two recordings that day, and the first was sent in error

She sent a centerpieces recording first, labelled as Sunday's TikTok — a
different prompt, DIY centerpieces against a professional florist for a 25-table
gala. It was raised with her rather than built on the assumption that the day's
piece had been swapped, and she confirmed on 2026-10-04: **"The centerpiece was
a mistake."** Later the same day she explained what the mistake was —
**"Centerpieces have also posted"**: the piece was already live on TikTok, so
sending the recording here was the error, not recording it. The bar quantities
recording arrived straight afterwards and is what this day uses.

So there is **no pending centerpieces piece**. Nothing is scheduled for it and
nothing is owed. Its source was never brought into the repo.

Worth keeping as a case for the rule: a recording that does not match the day's
brief is a question, not a swap. Building it would have produced a duplicate of
something already live, with a caption matching neither the footage nor the
guide.

**This repo cannot tell whether a TikTok has been posted.** Two pieces were
proposed for Mon 5 Oct on the strength of repo notes — the vendor quotes cut
and this one — and both were already up. Uploads are hers, nothing reports
back, and a schedule line records what was *planned*, never what happened. Until
there is a record she updates, the only reliable source is asking her.

## Caption

`build/caption-tiktok.txt`, exactly the guide's wording for this day. The
quick-piece caption format is one line of what it does, the prompt, four
hashtags, **no CTA** — and it writes `Prompt:` rather than the usual
`AI Prompt:`.

## The Instagram cut has a voiceover — added 2026-10-17

Offered as one of three options once it was established that **a Reel posted
from here cannot carry music** (Instagram's audio library is in-app only), so
the real choice was silent, a voiceover, or her uploading it by hand with a
trending track. She picked the voiceover.

> Two hundred guests, four hours, open bar. Five drinks a head — about a
> thousand drinks. Then the actual order, bottle by bottle, before anyone
> signs off on it.

**She approved the finished cut on 2026-10-17** ("approved"), after seeing and hearing it — so the go-ahead covers the rendered file, not just the decision to add a voice.

29 words, 11.42s against the 12.20s cut, Vanessa as always. Written against
what is actually on screen: the three beats are the prompt, "5 drinks per
guest, ~1,000 drinks total", and the order table — which really does break
down into bottles and servings, so "bottle by bottle" describes the video
rather than dressing it up.

**The picture is copied, not re-encoded** (`-c:v copy`). The video stream is
bit-for-bit the Oct 4 export — same codec, same 366 frames — so this is the
approved cut plus a voice, not a second-generation re-encode. The guide's
"use the existing cut, no re-edit" is honoured on the only part a re-edit
would damage, and adding an audio track changes no frame.

| | |
| --- | --- |
| `barquantities-instagram.mp4` | 12.20s, unchanged; **−14.44 LUFS, −0.93 dBTP** |
| VO gain | +5.56 dB from −19.56, with `alimiter level=0` catching the +2.96 dBTP it would otherwise hit |
| Speech ends | 11.0s, leaving a 1.2s tail — nothing clipped |
| md5 | `add84f567f8b8c4e273b0a114083ad36` |

**`barquantities-tiktok.mp4` is untouched.** It is already live on TikTok from
Oct 4 and moving or re-rendering it would break that post. Two files, two
platforms, and the no-both-cuts-to-one-platform rule is not in play because
the TikTok cut never went to Instagram.
