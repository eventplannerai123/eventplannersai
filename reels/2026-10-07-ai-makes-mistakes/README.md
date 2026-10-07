# 2026-10-07 — AI makes mistakes, just like us

The Wed 7 Oct Instagram piece, and the format test: the build-story format
rather than a demo. No screen recording, no ChatGPT prompt — Sahiba off camera
over b-roll of real work. Content bank item 10.

## Status: voiceovers built, footage missing

Both voiceovers were generated on 2026-10-07 and are in `voiceover/`. **No
footage has arrived**, so neither cut exists yet.

The guide intended this one built and scheduled by **Mon 5 Oct**, because Sahiba
is at a conference Tue 6 and Wed 7. That did not happen: Monday's piece was
switched out on her instruction ("lets switch mondays post to later next week —
find something easier for tomorrow"), the site report moved to Mon 12, and this
piece was never recorded. So the Wed 7 line "confirm the scheduled Instagram
Reel posted" has nothing to confirm — checked the live account on 2026-10-07 and
the most recent post is the Oct 5 hidden-fees carousel.

What it needs is the conference b-roll she was filming Tue 6 — catering, coffee
station, room filling, no faces, no logos. That is exactly the footage this
piece calls for, so nothing new has to be shot.

## Voiceovers

ElevenLabs, Vanessa - Beach Girl (`8DzKSPdgEQPaK5vKG0Rs`),
`eleven_multilingual_v2`, one generation each. Raw, not yet normalised —
loudness is applied at render time per the usual two-step (measure, then
explicit gain plus `alimiter` with `level=0`).

| Cut | File | Raw duration | Words | Words/sec |
| --- | --- | --- | --- | --- |
| Instagram | `voiceover/vo-instagram-raw.mp3` | 15.49s | 47 | 3.03 |
| TikTok | `voiceover/vo-tiktok-raw.mp3` | 15.18s | 46 | 3.03 |

Both land inside the 15-20s target with no padding needed.

The Instagram script is the guide's, verbatim. The TikTok one changes only its
opening line, to the command-style hook the standing rules require of the TikTok
cut:

- Instagram: "AI will never get VIP seating right on its own."
- TikTok: "Stop letting AI do your VIP seating."

The rest of both is identical, and the body is the guide's wording.

## Overlays

- Instagram hook, 0:00-0:03: "AI doesn't know which two execs can't sit together."
- TikTok hook, 0:00-0:03: "Stop letting AI do your VIP seating."

One overlay only, no end card, per the current briefs. The y position is picked
once the footage exists — it depends on what the opening frames show.

## Caption

`build/caption.txt`, the guide's wording verbatim, used for Instagram, Facebook
and TikTok alike. **No `AI Prompt:` line** — the guide says outright that this
piece is not a demo, so the usual caption layout's prompt block does not apply
here.
