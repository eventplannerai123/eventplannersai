# Wed 11 Nov, 12:30pm — "You're allowed to be tired after someone else's best day."

The fourth planner-feelings post, and the first one that goes out as a Reel.

| | |
| --- | --- |
| Image | `slides/allowed-to-be-tired.jpg`, 1080x1920 |
| Reel | `allowed-to-be-tired-instagram.mp4`, 8.0s, **-14.03 LUFS** |
| Caption | `build/caption.txt`, identical for TikTok |
| Instagram + Facebook | the Reel at 12:30pm, from here — the guide assigns this slot to CC |
| TikTok | the JPEG as a photo post, hers, around 12:30pm |

**The words are the guide's, verbatim.** Headline, three paragraphs and
caption were written into the Wed 11 block, so nothing here is composed.

**1080x1920, not the 1350 the earlier ones used.** The Nov 8 format rule turns
this slot into a Reel on Instagram and Facebook — the same still held 7–10
seconds under soft music — and a photo post on TikTok. Both want the 9:16
frame, so one image serves them and `render.py` holds it for 8 seconds, the
middle of that range and about as long as three paragraphs take to read.

**The format is the inverse of the carousel brand look, deliberately**: deep
purple `#3C3489` background, headline in white Poppins SemiBold, body in
lavender `#CECBF6` Poppins Regular, the handle small at the foot. No numbered
badge, no EP wordmark, no demo and no sales line — `check()` asserts the text
carries none of those. The absence of a demo is what this post type tests.

**And it goes to TikTok too**, from her Nov 7 rule. On Nov 9 the same JPEG took
322 views on TikTok against 23 on Instagram, so the file and caption go to her
as a matter of course now.

## The music

A Reel posted from this session cannot use Instagram's licensed audio library
— that is in-app only, and `INSTAGRAM_POST_IG_USER_MEDIA` has no field that
attaches a track — so whatever is in the mp4 is what goes out. She settled the
question in four words on Nov 10: **"dont go out silent"**.

**This piece has its own bed, and that took a correction.** Both Wednesday
Reels first went out of here on one track, the 8-second cut being literally
the opening of the 15-second one, and she spotted it: *"are they both the
same?"* Two posts on the same day sharing their opening bars is worse than a
second generation costs. So this one is a separate `eleven_music_v2_5` track —
sparser electric piano over a low drone, slower than the slide Reel's.

**Taken from 10.0s into the generation, not 0.0s.** Its first two and a half
seconds are the drone alone, so an 8-second cut from the top would have opened
on near-silence under a 0.8s fade. Faded 0.8s in and 1.2s out, measured to
-14 LUFS.

**Nobody in this session can hear it, so "instrumental" was checked twice
rather than assumed.** The spectrogram shows chordal blocks and a sustained
low drone with none of the formant movement a sung vowel makes, and ElevenLabs
Scribe transcribed the file to an **empty string**, which is what an
instrumental returns. The generation's own settings report
`Instrumental: False` even though the prompt asked for no vocals, so the
settings are not the check.

What neither check can tell us is whether it *sounds* good. That went to her
with the file rather than being decided here.
