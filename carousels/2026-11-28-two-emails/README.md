# Sat 28 Nov, 6:30pm — "The email I wanted to send vs the one I sent."

Content bank 37, the pair for the snippy-email Reel that was one of the top
performers. Six brand slides, 15.00s, to Instagram and Facebook as a slide
Reel; TikTok takes the same six JPEGs as a photo carousel. Planner-life
Saturdays have been the best 6:30pm slot — Sat 21 reached 121.

## Where the situation came from

Her Sat 28 YOU line asked for one real situation by Tue 24. On Mon 23 she
asked for a draft to edit instead, read it, and made one change: **"we also
will need to add rentals and servers."** So the frame is this session's and
the correction is hers.

The situation: a client adds 40 guests nine days out, 260 becomes 300, and
expects the per-head price to hold. **No client, no company, no venue** — the
client is "a client" and the caterer is "the caterer". `check()` refuses
company-shaped strings and asserts all three numbers survive to the slides.

Her edit is asserted in both emails, on the stem rather than the exact word:
the angry draft counts them ("two more servers, and 40 more of every single
rental"), the sent one absorbs them into the cost ("additional rentals and
two more servers"). It is the only part of the piece she wrote, and the part
a tidy-up would smooth away first.

## Slide 5 is a real run of the prompt

The guide's prompt was applied to slide 3's email and slide 5 carries what
came back, unedited. That matters because slide 6 and the caption are built
around the twist, and inventing the output would invent the twist too.

**The twist is not the one the guide predicted.** The guide expected the
model to soften the date into "at your earliest convenience". It did not — it
kept "by Thursday", and `check()` asserts that, so a rerun that loses the
date forces the twist to be rewritten rather than quietly contradicted.

What it did instead: **it opened by thanking the client for sending the final
numbers, which is the thing that caused the problem.** That is better
material than the predicted slip, because it is a habit rather than an
accident — the prompt asks it to "thank them for what went right", and when
nothing did, it thanks them anyway. Slide 5's footnote and the caption's
fifth paragraph both say to cut that line.

## The prompt is in the caption, not on slide 5

The guide's slide plan says slide 5 carries "the prompt, and the AI's version
of slide 3". The full prompt is 60 words and slide 5 already holds a label, a
headline, the returned email and the twist; a fifth block drops every size on
the slide. So slide 5 carries the **gist** — "Keep every fact and the one
thing I need, but make it calm and firm. Cut anything I'd regret if it got
forwarded." — and the caption carries it in full under its `AI Prompt:`
label, which is the house rule anyway: the prompt goes in the caption so the
post stands on its own without the video. Worth her ear on it; it is a
judgement call against a line in the guide.

## The cut

**15.00s**, 1080x1920, 30fps, CRF 19, AAC 192k at 48 kHz, `+faststart`,
**-14.5 LUFS**. Six slides at 2.50s, hard cuts, no push.

| | |
| --- | --- |
| Voiceover | Eryn `kdnRe2koJdOK4Ovxn2DI`, `eleven_v4`, the guide's own 30-word script |
| VO length | 11.52s, starting at **2.40s** |
| VO gain | measured -23.1 LUFS / -2.8 dBTP, swept +11.0 → -15.0, +12.0 → -14.6, **+13.0 → -14.1** into `alimiter=limit=0.891:level=0` |
| Bed | `eleven_music_v2_5`, 30s generated, trimmed 0.0–15.0, 0.8s in / 1.2s out |
| Bed level | **-7.0 dB**, swept: -6 left only 4.5 dB between bed and voice, -8 pulled the whole file to -14.7 |

**2.40s is load-bearing.** From there the VO ends at 13.92 and its last line —
"send the one that comes back, after one read" — lands inside slide 6, which
is the slide that says "Write the first one. Send the second." `render.py`
asserts it.

**The bed rings out, so the trim window matters.** Energy sits between -12.4
and -14.9 dB to 24s, then -21.6 at 26s and -34.4 at 28s. The 15s cut from 0.0
is well clear, but a longer piece on this bed would have to move its window
rather than extend it.

**It is its own generation**, distinct from both of Wednesday's — checked on
the md5, not by ear. Instrumental, checked the same two ways as every bed:
the spectrogram shows regular transients and no formant movement, and Scribe
returned an empty string.

## No BUDGET line

A client-communication piece, not a money one. `check()` asserts it — the
Nov 14 rule about reading the closing line against the piece.

## Posting

- **Instagram and Facebook at 6:30pm Saturday**, after she approves Fri 27.
- **TikTok**, hers, the same six JPEGs as a photo carousel at about 9am.
- Saturday also carries the giveaway winners, which is a separate job: pull
  every comment on the Fri 20 Reel to Fri 27 11:59pm Eastern, drop her own
  and repeats, add her reported Story shares, pick two at random.
