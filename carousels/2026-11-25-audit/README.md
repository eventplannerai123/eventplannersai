# Wed 25 Nov, 6:30pm — "One week of your admin. Three fixes."

Consulting post 2, the follow-up to Wed 11. Six brand slides, 15.00s, posted
to Instagram and Facebook as a slide Reel; TikTok takes the same six JPEGs as
a photo carousel.

## What changed from Wed 11, and why

Wed 11 opened on "What I'd fix first in an event studio's admin." It reached
83, brought **no DMs**, and sat at 1 view on TikTok until the Sat 21 repost
(which then did 127). The Sun 22 recap's reading was the hook: no number in
the first line. So slide 1 here is **"One week of your admin. Three fixes."**
and the explanation drops underneath it. `make_slides.py` asserts the hook
carries a number, so a later edit cannot quietly undo the one change the
recap made.

The ask changed too. Wed 11 ended on "DM me and tell me what eats your week";
this one ends on **"DM me AUDIT"** — a keyword, so the DMs are countable and
she can tell an audit enquiry from anything else in the inbox. No ManyChat
automation behind it: that is BUDGET's, and the guide says the ask here is
the DM itself.

## The words are hers, the line breaks are not

The Sun 22 recap wrote slide text for all six. What this build decided is
only where each sentence splits into headline and body, and where the
headline wraps. `check()` rebuilds every slide from head + body and compares
it word for word against `GUIDE`, so a tidy-up fails the build rather than
shipping a paraphrase of how she sells her own work.

**Slides 2–5 are hers to correct.** Her Wed 25 YOU line says they describe how
an audit actually runs and to change anything that is not how she would do
it.

## No BUDGET line

A services post, not a tracker post. `check()` asserts the word appears
nowhere — the same guard the Nov 17 BEO redo got after she caught a tracker
CTA on a run-sheet piece, and the Nov 14 rule to read the closing line
against the piece before rendering.

No employer, no client, no venue anywhere: this is the post most likely to
reach for a name, so `check()` refuses a set of company-shaped strings too.

## The cut

**15.00s**, 1080x1920, 30fps, CRF 19, AAC 192k at 48 kHz, `+faststart`,
**-14.1 LUFS**. Six slides at 2.50s, hard cuts, no push — typeset cards, so a
drift only softens the glyph edges and a crossfade between two lavender
slides reads as a smear.

| | |
| --- | --- |
| Voiceover | Eryn `kdnRe2koJdOK4Ovxn2DI`, `eleven_v4`, the guide's own 35-word script |
| VO length | 11.60s, starting at **2.40s** |
| VO gain | measured -23.6 LUFS / -3.0 dBTP, swept +9.5 → -15.6, +11.5 → -14.5, **+12.2 → -14.1** into `alimiter=limit=0.891:level=0` |
| Bed | `eleven_music_v2_5`, 30s generated, trimmed 0.0–15.0, 0.8s in / 1.2s out |
| Bed level | swept against the export: -10 left the opening at -27 dB, **-6.0** puts it at -23 under slide 1 and -16 under the voice |

**2.40s is load-bearing.** The VO runs 11.60s, so from 2.40 it ends at 14.00
and its last phrase — "DM me AUDIT" — lands inside slide 6, which is the
slide that makes the same ask. From 0.00 the ask would land under slide 5 and
leave 3.4s of bare bed on the end. `render.py` asserts it.

**The bed is its own generation.** The 12:30pm list Reel the same day has a
different one — her Nov 10 rule, after she heard two Wednesday posts sharing
their opening bars and asked "are they both the same?"

Instrumental, checked the two ways that do not need ears: the spectrogram
shows regular transients and none of the formant movement a sung vowel makes,
and **Scribe transcribed it to an empty string**. The generation's own
settings read `Instrumental: False` regardless, so they are not the check.

## Posting

- **Instagram and Facebook at 6:30pm Wednesday**, after she approves.
- **TikTok**, hers, the same six JPEGs as a photo carousel at about 9am.
- After posting, confirm `media_product_type` reads REELS. Six stills under a
  bed is exactly the shape Instagram can file as an image instead.
