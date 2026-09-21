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
- **One crop rule: `crop=1206:2144:0:478`.** 478 off the top, nothing off
  the bottom — it drops the status bar and the red recording dot while
  keeping the ChatGPT input bar at the bottom, where the platform UI covers
  it. A y-offset of 0 leaves the recording dot in frame; the guide's
  duplicate `:0:0` rule was deleted on 2026-09-21, so this is the only one.
  It holds for the standard 1206x2622 iPhone capture. If a recording ever
  arrives at a different width, recompute (height = width / 0.5625) rather
  than reusing these numbers, and say so.
- 30 fps out, H.264 high, CRF 19, `+faststart`, AAC 192k at 48 kHz.
- **Voiceover to -14 LUFS.** Measure the source with a loudnorm first pass
  and feed the measured values back in, rather than a single dynamic pass.
- The screen recordings carry a silent audio track. The uploaded voiceover
  is the only audio.

## Timing rules

- **Length test, Sep 23-30.** Named days, not a formula:
  **short (15-20s): Sep 23, 25, 29.  long (40-50s): Sep 24, 26, 30.**
  Keep to them — it is a test, so drifting defeats it. Each day's block in
  the guide states its target; follow that. Sep 27 and 28 are trials and do
  not run through here at all (see Posting). Before Sep 23 the standing
  target was 16-20s. A day's brief still overrides both.
- **The 6-second payoff ceiling is unchanged by the length test.** A 40-50s
  piece has to front-load just as hard; the extra time goes into the reveal,
  never into a slower open.
- **Time to payoff must stay under 6 seconds** — everything before the
  reveal, combined. This is a hard ceiling from real watch-time data and is
  the rule most often missed. The Sep 12 reel shipped at 6.5s and broke it.
- The generating section needs a **visible beat of 2.5-3s minimum**, sped
  to 2-3x, about 4 seconds.
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
- **Never post both cuts to the same platform** — near-identical posts
  split engagement.
- Hooks must name a concrete scenario, number or timeframe immediately.
  Abstract superlatives and vague teases both measured badly.
- Prefer broader "event" framing in the opening hook line even when the
  demo content is sector-specific ("a $85,000 event just wrapped", not "a
  $85,000 corporate summit"). Say "event planner", not "wedding planner",
  in general self-identification. Neither overrides genuinely
  wedding-specific content, hashtags or research scope.
- **Transformation is the house format** (set 2026-09-20). A messy or ugly
  real input visibly becoming a structured or beautiful output on screen.
  The three best-performing posts are all this shape, and at least half of
  every week is now built this way. Advice and email-writing pieces
  underperform and should be the minority.
- **No more than two wedding-specific pieces in any seven.** The account is
  "event planner", and Round 5 drifted to four weddings in a row.
- Use only the author's uploaded footage. No stock, no generated visuals.
  Their own output files (a floor plan PNG, say) are fine when they send one.

## Posting

Never post without explicit approval in the conversation. Build both cuts,
show the Instagram one, ask, and wait.

This rule is the only thing standing between a draft and a live account.
A PreToolUse hook used to force a permission prompt on every publishing
call; the author had it removed on 2026-09-17, preferring to give the
go-ahead in conversation. So nothing mechanical stops a post now.

**There is no technical gate.** The PreToolUse hook was removed on
2026-09-17 at the author's instruction and has not been replaced, so
nothing mechanical stops a mistaken publish and a live post cannot be taken
back. Do not re-add the hook unless the author asks for it.

**Never publish without her explicit go-ahead in the conversation.**

**The standing rule is post when she says, not post whenever.** Wait for
words that clearly mean go: "go ahead", "publish", "post it". "Looks good"
or "great" is feedback on the cut, not permission — ask.

**Step-by-step mechanics, including exact tool slugs and arguments, are in
[`docs/POSTING.md`](docs/POSTING.md).** Posting runs through the Composio
MCP server; a session without `mcp__Composio__*` tools cannot post at all.

- **Instagram** — Composio account `instagram_newing-redate`, `ig_user_id`
  `28308094898830663`. Create the container with `media_type: REELS` and
  `share_to_feed: true`, then publish with a generous `max_wait_seconds`.
  Containers are single-use; on a processing error build a new one.
- **Facebook** — Composio account `facebook_radius-iguana`, page_id
  `1233196746554445` ("The Event Planners AI"). Never blind-retry, it
  duplicates posts.
- **TikTok is the main platform — and still a manual upload.** (138
  average views per video against Instagram's 53, on a fifth of the
  followers.) Composio cannot publish publicly to TikTok, so **hand over
  the TikTok cut every single day** and never attempt to post it. It is the
  platform that actually reaches people, so its cut is not an afterthought
  to the Instagram one.
- Facebook has 7 followers and is not yet a platform. Still post there, but
  do not read anything into its numbers.
- **Trial Reels are manual, and Sep 27 and 28 do not come through here at
  all.** Those two are planned Instagram trials: they are edited in the
  Claude.ai chat and the author uploads them herself. **Do not post them.**
  If their content turns up in this session, stop and say so rather than
  building or publishing anything.
  Generally: the Trial toggle is in-app only, so a trial cannot be
  published from here — only regular feed Reels can. Never post the same
  piece as both a regular Reel and a Trial Reel: that trips Instagram's
  duplicate-content detection and throttles both for up to 30 days. Only
  label a day "Trial Reel" after it has actually been posted as one.
- Meta fetches the video from a URL, so push the cut to this repo first and
  pass its `raw.githubusercontent.com` URL. Moving or renaming that file
  later breaks the live post.
- **Caption layout: caption body, blank line, `AI Prompt: "..."`, blank
  line, hashtags.** The AI prompt always goes in the caption so the post
  stands on its own without the video.
- Pass hashtags with literal `#`. The Composio field docs suggest URL
  encoding; that is wrong and would publish `%23tag`.
- **Never write the label "Hashtags:".** Hashtags go on their own line
  starting with `#`, unlabelled. The label used to paste through into live
  captions and had to be deleted by hand.
- After publishing, read both posts back and compare the live caption to the
  approved text character for character.

## CTA

**Never write "Comment [KEYWORD]."** Comment-to-unlock is retired — nine
keywords across the series returned zero comments between them.

- **Prompt pieces end: "The full prompt is in the caption below."** The AI
  prompt is already in the caption body, so the piece is self-contained.
- **"link in bio" is only for downloadable files**, and only once the bio
  links to a hub page that actually holds them. **It does not yet** — the
  bio currently points at the tablecloth cheat sheet alone. So do not write
  "link in bio" until the author says the hub is live.

The guide keeps the old keyword list as a record of what was tried, so the
mechanic is not reintroduced without knowing it already failed nine times.

## Practical gotchas

- **Aim for ~25 seconds of raw footage per recording.** That gives enough
  generating time to compress into a real 3-4 second ramp and enough reveal
  to fill the hold at natural speed. Shorter sources (~12-13s) force
  tradeoffs across duration, ramp and pacing at once.
- **But raw recordings usually exceed the upload limit.** iPhone screen
  capture runs about 1.1 MiB per second, so ~25 seconds sits right at the
  ceiling and anything past ~26 seconds fails. When it does, ask for
  roughly 20-second clips saved with "Save as New Clip", overlapping by a
  beat. Frame-match the overlap to find the seam, then concatenate.
- **Uploads must be sent at "Actual"/"Original" size.** The default
  compressed size produces visibly soft footage.
- **Google Drive is blocked** by the session's egress policy. Do not route
  around it; ask for split uploads instead.
- **A pasted image is not a file.** Images dropped into a message may render
  without landing in the uploads directory. Check for a real path before
  planning to use one.
- **Check the reveal for the Adobe Acrobat banner ad and trim around it.**
  It scrolls up into the bottom of frame during long scrolls. Verify this
  **visually** on bottom-strip frames — on 2026-09-21 a red-pixel detector
  reported a cut clean while "Adobe Acrobat ... Ad" was plainly legible in
  it, because the logo fades in and the colour test passed the faded frame.
  A false all-clear is worse than no check.
- Check the full raw footage for other in-app ads before finalising the
  reveal.
- The recording is supposed to start with the prompt sitting in the input
  box and the send tap on camera. Two recordings so far began after the tap.
  Flag it rather than faking an opening.
