# Wed 25 Nov, 12:30pm — "Things I normalized in events that I really shouldn't have."

The second planner list Reel, a week after the first. One image, 9.00s, held
with music on Instagram and Facebook; TikTok takes the same image as a photo
post.

## It is built with four lines and the format wants five

Her Wed 25 YOU line asks her for a fifth by Mon 23 — one true thing from her
own years — and says in as many words that it runs with four if none comes.
So this is the guide's four, laid out as four, and `check()` accepts four or
five rather than pretending the slot is filled. **Adding hers is one edit:**
append it to `LINES` and rerun; the layout solves its own sizes, so nothing
else needs touching.

The four:

1. Eating standing up, behind a curtain, in under three minutes.
2. Keeping every vendor payment in my head.
3. Every tab open on my laptop at 2am before load-in.
4. Signing the Saturday quote without asking for the weekday rate.

`check()` asserts the first four word for word against the guide, so a
later tidy-up fails the build instead of publishing a paraphrase of her own
habit. Two of them are things this account has already made a piece about —
vendor payments (Mon 9, Thu 19) and the 2am tabs (Sat 14) — which is what
makes the list hers rather than a listicle.

## The look

Deep purple #3C3489 ground, lavender #CECBF6 boxes, title in Poppins
SemiBold white, lines in Poppins Regular deep purple — the inverse of the
carousel, as the November plan specifies for this format. No numbered badge,
no AI demo, no sales line, **no BUDGET line**, which `check()` asserts along
with "prompt", "chatgpt", "link in bio" and "comment".

**The safe zones are the layout, not a check afterwards.** The whole block is
centred inside 250–1440 rather than in the frame, so the last box ends at
**y=1355** and clears the bottom 25% where TikTok's caption and buttons sit.
`main()` asserts it. The longest line is 63 characters, so the box text size
is solved for it rather than typed.

## The cut

**9.00s**, 1080x1920, 30fps, CRF 19, AAC 192k at 48 kHz, `+faststart`,
**-14.0 LUFS**. Nothing moves: a push on typeset text softens the glyphs for
no gain.

**Its bed is not the slide Reel's.** Both pieces go out on Wed 25, and her
Nov 10 rule is that a bed is never reused across two posts on the same day.
Two separate generations with different prompts: the 6:30pm one is electric
piano and shaker mixed to sit under a voiceover, this one is a bouncy guitar
riff with handclaps and a walking bass — upbeat per her Nov 10 instruction,
and chosen to match a list of bad habits admitted with a shrug.

Energy ran -13.5 to -14.7 dB across all 30 seconds, flat end to end with no
intro build and no ring-out, so the cut starts at 0.0 with a 0.8s fade in and
1.2s out. **-0.6 dB** into the limiter: +0.0 measured -13.4, which is hot.

Instrumental, checked the same two ways: the spectrogram shows regular
transients and nothing sweeping, and Scribe returned an empty string.

## Posting

- **Instagram and Facebook at 12:30pm Wednesday.**
- **TikTok**, hers, the same image as a photo post.
- She leaves the first comment within ten minutes — her own answer to the
  caption's question. The Wed 18 and Fri 20 first comments went up on Nov 21,
  days late, which does nothing.

## Published

Wed 25 Nov 2026, 12:30pm Eastern (17:30 UTC), from the one-shot task
`trig_016mxU8v4eF4Le6KDhdxMyx2`. The guide's Wed 25 CLAUDE CODE line assigns
this slot to CC, and she chose the fifth line herself on Mon 23.

- Instagram: https://www.instagram.com/reel/DgLEks5xQN9/ (media id
  `18116074847190849`, container `18106023029367131`, FINISHED after 18.7s).
  **`media_product_type` reads `REELS`**, which is the check that matters on a
  single still held nine seconds — that is exactly the shape Instagram can
  file as an image instead. Live caption diffed against `build/caption.txt`:
  identical.
- Facebook: post id `1185125960741606`, same commit-pinned URL
  (`a43a9fb`, 424,112 bytes verified against the local file before the call).

Checked both accounts first. Nothing of this piece was live; the newest items
were the two hook-test trials from this morning.

### Her Facebook toggle cross-posted both hook-test trials

Worth recording because it was not planned: the two "advice I'd burn" trials
she uploaded at 9:30am and 9:32am appeared on the Page as Reels at 14:30:12
and 14:32:17 UTC, carrying her Instagram captions verbatim. The advice-burn
README says Facebook gets only the winner, after it is shared; her in-app
toggle got there first.

**Nothing to do about it.** Facebook cannot be measured at all — reach and
impressions were deprecated in its API in Nov 2025 — so having both versions
there costs nothing and tells nobody anything. It does not touch the
Instagram trial figures, which are what the test is read from, and it is not
an Instagram duplicate: two different files, and a Facebook cross-post is a
separate object from an Instagram trial.
