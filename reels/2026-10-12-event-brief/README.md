# 2026-10-12 — Consultation notes to event brief

The Mon 12 Oct piece, and **both cuts are hers to upload**: the Instagram one is
a planned Trial (in-app toggle only) and TikTok is always manual. Nothing posts
from here.

| | |
| --- | --- |
| TikTok | `event-brief-tiktok.mp4` — 16.30s, −14.4 LUFS, TP −1.0 |
| Instagram (Trial) | `event-brief-instagram.mp4` — 15.70s, −14.1 LUFS, TP −1.0 |

1080x1920 (0.5625 exactly), 30 fps, H.264 High, CRF 19, `+faststart`, AAC 192k
at 48 kHz. Both inside 15–20s.

## What this piece became, and why

It started as the **site report** scheduled for Mon 5, moved to Mon 12. It is
not that any more, and the path there is worth keeping because two of the three
turns were her catching something.

1. **The source changed.** There were no site-visit photos. What exists is one
   page of handwritten **client-consultation notes** for a 200-person cocktail
   reception — `handwritten_consultation_notes (1).jpeg`, the only handwritten
   notes anywhere in her Drive. So the prompt was reworded from a site report to
   an **event brief**.
2. **She killed the firewall hook, correctly.** The piece was to be hooked on
   content bank item 23 — "is there a firewall, or can we put our own laptops on
   your network?" — but, as she put it, *"theres nothing about it in the prompt
   currently that would cause chatgbt to check"*. True of the original
   site-report prompt too: it asks for power and AV and nothing about
   connectivity. **A hook has to name something the answer actually contains.**
3. **She chose to leave the prompt open and expect the miss.** Rather than
   adding "check network access" to the prompt — which would have made the AI
   look clever for following instructions — the prompt stays generic.

## The prediction was wrong, and the piece is better for it

I expected ChatGPT to omit connectivity entirely. It did not. Its checklist
contains:

> **"Confirm power access, internet/Wi-Fi, and any restrictions on outside
> equipment."**

So it is not a miss. It is **the generic half-question** — exactly the one bank
item 23 says is insufficient: *not whether there is wifi, but whether the
machines the client actually brings can get on it.*

That is a stronger piece than a clean omission, for two reasons. It is harder
to argue with, because the line is on screen and highlighted rather than
asserted. And it is truer: the failure is not that AI forgot, it is that AI
asked the same shallow question the whole industry asks.

**Checked properly before building on it.** Frames were read at roughly 1.2s
intervals across all 29.5s, and the line was cropped at full resolution to
confirm the wording. The claim "it never mentions the network" would have been
false.

## Beats

Freeze frames, 0.20s dissolves. Clean band 1161x2064 at x=22, y=300 — exactly
9/16; the roomier 1166x2074 is 0.5622 and fails the assertion in `render.py`.

| | Source | What it shows |
| --- | --- | --- |
| 1 | t=4.20 | the prompt, with the notes photo attached, hook over the thumbnail |
| 2 | t=20.10 | **Follow-up tracker — 0 of 31 complete**, highlighted |
| 3 | t=22.40 | **"Confirm power access, internet/Wi-Fi…"**, highlighted |
| 4 | t=27.50 | the takeaway, over the end of the brief, dimmed |

Source times place each line mid-frame; the scroll does the composition. Beat 1
needed no compromise — the prompt bubble sits clear of the thumbnail, so the
hook covers the photo and not a word of the prompt.

**Opening on the prompt follows the guide's Oct 5 rule 2.** The older Mon 5
block for this piece says "open on the finished report, not the prompt being
sent", which predates rule 2 and is superseded by it.

## Overlays

| | Position | Width |
| --- | --- | --- |
| hook (both cuts) | y 368–593 | — |
| follow-up tracker | y 660–765 | 90% |
| internet/Wi-Fi line | y 885–1105 | 89% |
| takeaway card | y 732–1068 | — |

Hooks:

- **Instagram** — "31 things to confirm. The wifi one won't save you."
- **TikTok** — "Stop asking venues if they have wifi."

All asserted inside the Oct 5 safe band by `build/make_cards.py`, then checked
on the exported frames of both cuts.

## No ad

First recording in a while with **no in-app advertiser** at all. The bottom
strip was scanned from t=24 through to the final frame before that was relied
on. The run had been Adobe Acrobat, Adobe Firefly, Rillion, Cambridge, Turning
Stone, Fever, Asana and Chivari — eight in a row — so this is the exception, not
a reason to stop checking.

## Voiceovers

ElevenLabs, Vanessa - Beach Girl (`8DzKSPdgEQPaK5vKG0Rs`),
`eleven_multilingual_v2`. 42 words each, inside the guide's 30–45 for this
piece. Written **after** seeing the output, which the usual rule does not allow
early — the script depends entirely on what the answer said.

- **TikTok** — "Stop asking venues if they have wifi. I gave AI a page of notes
  and it built a 31-point checklist, and its network line says the same thing:
  confirm internet and wifi. Ask whether your client's laptops can actually get
  on it."
- **Instagram** — "I gave it one page of consultation notes. It came back with a
  31-point checklist. Useful. But the network line just says confirm internet
  and wifi. That's the question everyone asks, and it isn't the one that saves
  you on the day."

Loudness: measured first pass, explicit gain, `alimiter` with `level=0` at a
−1.0 dB ceiling, `TRIM = 1.10` for the lead-in and tail. Confirmed on both
finished files.

## Captions: the trial one has no hashtags

Two files, and the difference is deliberate.

- `build/caption-tiktok.txt` — the ordinary layout, four hashtags.
- `build/caption-instagram-trial.txt` — **identical body, no hashtags.** A trial
  is kept off hashtag pages, so tags do nothing there. That reasoning is
  Instagram-only; if this piece ever goes to Facebook it takes the hashtags.

Both end "Prompt below.", the standing CTA for prompt pieces, and both carry the
reworded prompt in the body so the post stands on its own.

## The prebuilt voiceovers in `reels/2026-10-05-site-report/` are dead

They say "site report" and "five photos and a page of notes", and both lead on
the firewall. That directory's README carries the full explanation.
