# Mon 16 Nov, 12:30pm — "The guests leave at 11. You leave at 1."

Planner-feelings post 6. Instagram and Facebook from here as a still-image
Reel; TikTok takes the same JPEG as a photo post, from her.

## Why it exists at all

**The 12:30pm slot came up empty this morning.** The Mon/Wed/Fri rule has run
since Nov 4, but the Mon 16 block was written on Thu 12 — before the Sun 15
recap restarted the second posts on Wed 18 — so Monday fell through the gap
between the two. Flagged to her as a gap rather than reported as "nothing to
do", and she added it to the guide the same morning: *"Second post, 12:30pm —
planner-feelings Reel (added Nov 16, Sahiba: yes to one today)"*.

Every word is hers, verbatim from that block: headline, three paragraphs,
caption.

## Build

- 1080x1920, deep purple ground, white headline, lavender body — the inverse
  of the carousel look, which is what the guide specifies for this slot. No
  badge, no wordmark, no demo, no sales line.
- **The headline keeps its own line break.** "The guests leave at 11." and
  "You leave at 1." are the two halves of the joke; a reflowed break would
  run them together, so `make_post.py` wraps each half separately rather than
  wrapping the whole string.
- **A Reel, not a photo.** The Sun 15 recap put a number on it: on Mon 9 the
  photo version of this slot reached 15, against 146 and 130 for the two
  posted as Reels. Check the profile after posting.
- Its own upbeat bed — bright electric piano, warm synth bass, light
  tambourine. Never Friday's guitar-and-marimba or Saturday's
  piano-and-claps, and never shared with the day's other post.
- Instrumental proved twice, spectrogram and Scribe, as every bed is.

## The bed

Own generation, `eleven_music_v2_5` — bright electric piano, warm synth bass,
light tambourine. md5 `937759cb…`, distinct from Friday's `2ff24237…` and
Saturday's `12ea94dd…`.

Instrumental proved both ways: the spectrogram is regular transients and flat
harmonic bands with none of the formant movement a sung vowel makes, and
Scribe returned an empty string.

30.02s raw, trimmed 0.0–8.0s (full texture from the first frame, no near-silent
head to skip), 0.8s fade in, 1.2s fade out. **This one came out of the model
hot — -13.3 LUFS, louder than the -14 target** — so the sweep went *down*,
**-0.7 dB** into `alimiter=limit=0.841:level=0` for -14.0 LUFS. Saturday's
needed +0.2 and Friday's +3.4; never carry a gain figure over, and do not
assume the sign.

Export: 1080x1920, 30fps, CRF 19, +faststart, AAC 192k/48kHz, 8.00s,
-14.0 LUFS measured on the finished mp4.

## Approved, filed and scheduled

She approved it the same morning she added the block.

- Drive `November 16` (`1mij0zABAvcy7QT7Ronw3cglG8nmG93wo`) — the Reel and the
  JPEG, uploaded from commit-pinned raw URLs with each returned `size`
  checked against the local file.
- Instagram and Facebook at **12:30pm today**, one-shot task
  `trig_01AxMstF5Ac1krCEEjfWT565` (17:30 UTC). Its prompt carries the Sun 15
  standing check: read the item back afterwards and confirm it posted as a
  Reel and not a photo.
- TikTok handed to her with the caption at approval time, after a clear
  last-10 check.
