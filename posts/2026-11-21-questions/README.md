# Sat 21 Nov, 6:30pm — "Questions I get asked at every event."

Planner-life post, content bank 35, built for shares and comments. The Sat 21
CLAUDE CODE line specifies the look exactly, and this follows it: deep purple
#3C3489 ground, the title in Poppins SemiBold white, the numbered questions in
Poppins Regular lavender #CECBF6, and the last one set apart.

## The questions are hers or the bank's, never invented

Her Sat 21 line asks for 6 to 8 real questions by Thu 19. **They had not
arrived when this was built**, so it carries the content bank's default —
*Where's the bathroom? / What's the Wi-Fi password? / Are you with the
family?* and, set apart, *Did you eat?*

`QUESTIONS` in `make_post.py` is the only thing that changes when her list
comes in; `FROM_HER` flips with it, the layout re-centres itself for any count
from three to eight, and the caption's second paragraph gets rewritten around
her list. The guide's words: "Use Sahiba's questions exactly; never invent
one."

## Still to do before Friday

- The Reel version — the image held 7-10 seconds under its own bed, for
  Instagram and Facebook — with its own generation, not Friday's.
- Upload to Drive `November 21` (`1R2tXAIuuZUmAvWxb0Vj7be_W7J8_FroB`).

## Built Thu 19

- The Reel version is rendered: 1080x1920, **8.00s**, 30fps, CRF 19,
  AAC 192k/48kHz, **-14.04 LUFS**, over its own bed (nylon guitar and electric
  piano, a separate generation from Friday's marimba; instrumental by
  spectrogram and by Scribe returning an empty string; +3.7 dB into the
  limiter).
- Filed to Drive `November 21` (`1R2tXAIuuZUmAvWxb0Vj7be_W7J8_FroB`), image and
  Reel both, from commit-pinned raw URLs with the returned sizes checked.
- **If her questions arrive, both are rebuilt**: change `QUESTIONS`, flip
  `FROM_HER`, run `make_post.py` then `render.py`, re-upload, and rewrite the
  caption's second paragraph around her list.
