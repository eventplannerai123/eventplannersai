# Working in this repo

This repo holds the website plus the daily Reels for **@aiforeventplanners**.
Each finished piece lives in `reels/YYYY-MM-DD-slug/` with its two cuts, the
card generator, and a README recording what shipped.

The authoritative source is the author's September guide (a .docx they
upload per session). The rules below are the parts that govern rendering
and posting, copied here so they survive between sessions — the guide
itself records that relying on a per-session upload has caused rules to be
missed. **If the uploaded guide and this file disagree, the guide wins, and
update this file to match.**

## Render rules

- **1080x1920, ratio exactly 0.5625.** Verify with ffprobe before calling an
  export finished; never leave raw screen-recording dimensions.
- **Crop for a 1206-wide iPhone recording: `crop=1206:2144:0:478`.** The
  y-offset matters. 478 drops the status bar and the red recording dot off
  the top and keeps the ChatGPT input bar at the bottom, where the platform
  UI covers it anyway. A y-offset of 0 leaves the recording dot in frame.
  Recalculate the offset for any other capture width.
- 30 fps out, H.264 high, CRF 19, `+faststart`, AAC 192k at 48 kHz.
- **Voiceover to -14 LUFS.** Measure the source with a loudnorm first pass
  and feed the measured values back in, rather than a single dynamic pass.
- The screen recordings carry a silent audio track. The uploaded voiceover
  is the only audio.

## Timing rules

- **16-20 seconds** unless that day's brief says otherwise.
- **Time to payoff must stay under 6 seconds** — everything before the
  reveal, combined. This is a hard ceiling from real watch-time data and is
  the rule most often missed. The Sep 12 reel shipped at 6.5s and broke it.
- The generating section needs a **visible beat of at least 2.5s**, sped to
  2-3x, about 4 seconds.
- If the real generating phase runs much longer than that and is visually
  static, take a **representative slice** rather than compressing the whole
  thing, and say so in the reply.
- Hold the reveal at normal speed so it is readable. A freeze on the final
  frame is fine; a long silent tail is not, so prefer the lower end of the
  duration range when the voiceover is short.

## Structure and overlays

- **Two separate cuts every time**, never one file posted twice. Instagram
  takes the narrative hook; TikTok takes a genuinely different command-style
  hook ("Stop doing X") and slightly different pacing.
- Footage in motion from frame one. **Never open on a static title card.**
- Only two text overlays: the hook at 0:00-0:02 and the end card. **No
  rolling mid-video captions** — transcription-synced captions were tested
  and made retention worse.
- Hooks must name a concrete scenario, number or timeframe immediately.
  Abstract superlatives and vague teases both measured badly.
- Use only the author's uploaded footage. No stock, no generated visuals.
  Their own output files (a floor plan PNG, say) are fine when they send one.

## Posting

Never post without explicit approval in the conversation. Build both cuts,
show the Instagram one, ask, and wait.

That rule is also enforced, not just written down. `.claude/settings.json`
carries a PreToolUse hook that inspects every Composio execution call and
returns `permissionDecision: "ask"` when the payload names an Instagram,
Facebook, LinkedIn or TikTok create/post/update/delete/publish slug. Read
calls are untouched, so caption verification still runs without a prompt.
Do not weaken or remove it to make posting smoother.

- **Instagram** — Composio account `instagram_newing-redate`, `ig_user_id`
  `28308094898830663`. Create the container with `media_type: REELS` and
  `share_to_feed: true`, then publish with a generous `max_wait_seconds`.
  Containers are single-use; on a processing error build a new one.
- **Facebook** — Composio account `facebook_radius-iguana`, page_id
  `1233196746554445` ("The Event Planners AI"). Never blind-retry, it
  duplicates posts.
- **TikTok is manual.** Composio cannot publish publicly to TikTok. Produce
  the cut, hand it over, do not attempt to post it.
- Meta fetches the video from a URL, so push the cut to this repo first and
  pass its `raw.githubusercontent.com` URL. Moving or renaming that file
  later breaks the live post.
- Pass hashtags with literal `#`. The Composio field docs suggest URL
  encoding; that is wrong and would publish `%23tag`.
- After publishing, read both posts back and compare the live caption to the
  approved text character for character.

## Comment-to-unlock keywords

One per deliverable, never reused — two posts sharing a keyword misroute the
automated DM to one of them.

**The assignment list lives in the guide, under the standing production
rules. Read it there before writing a new CTA.** It is deliberately not
copied here: it changes with every new deliverable, so a copy would go stale
and a stale copy is worse than no copy for this particular rule.

## Practical gotchas

- **Raw recordings usually exceed the upload limit.** iPhone screen capture
  runs about 1.1 MiB per second, so anything past ~26 seconds fails. Ask for
  roughly 20-second clips saved with "Save as New Clip", overlapping by a
  beat. Frame-match the overlap to find the seam, then concatenate.
- **Google Drive is blocked** by the session's egress policy. Do not route
  around it; ask for split uploads instead.
- **A pasted image is not a file.** Images dropped into a message may render
  without landing in the uploads directory. Check for a real path before
  planning to use one.
- Check the full raw footage for in-app ads before finalising the reveal.
- The recording is supposed to start with the prompt sitting in the input
  box and the send tap on camera. Two recordings so far began after the tap.
  Flag it rather than faking an opening.
