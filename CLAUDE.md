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

## How to reply to her (standing instruction, 2026-09-30)

She asked for this twice, so it is a rule, not a preference.

- **Be as concise as possible.** No walls of text, no restating what she
  already knows, no narrating the work. Lead with the answer.
- **Keep the technical detail out of the reply.** ffmpeg numbers, loudness
  figures, filter names and timestamps belong in the reel README and the
  commit message, not in chat. Mention a number only when she has to act on
  it or decide something with it.
- **End with a clear action list** — hers separated from this session's, with
  dates. She should be able to read the last block and know exactly what is
  on her.
- **Spell out anything she has not done before**, step by step, including
  where to click. Do not assume a setting is findable just because it is
  named.

## The working guide is a Google Doc (from 2026-09-30)

**"AI for Event Planners — Working Guide"**, doc id
`1x8jXHHNOOl9ipDO5u7ZEfbtiG9ABor_zrEYal56Xtrg`. It replaces the per-session
.docx, and **no local copy is kept** — read the section you need from the live
doc at the start of each task and make every update in the doc itself.

Read and write were both verified on 2026-09-30 through Composio's
`googledocs` connection (account `googledocs_malter-azoch`).

- Read with `GOOGLEDOCS_GET_DOCUMENT_PLAINTEXT`. The doc is ~87k characters,
  so the response goes to the workbench; pull out the one section you need
  there rather than into chat.
- **Never append to the very end.** The doc finishes with a bulleted list, so
  an append becomes a bullet, and deleting its text leaves an empty bullet
  behind. Insert into the right section instead.

**Question of the day.** Ask it at the start of every session, plus any
earlier ones still unanswered, and write her answer straight into the doc's
career content bank as a new numbered item — hook, the true story, the AI
shortcut — then mark that day's question answered with the date. Claude.ai
reads the answers from this doc, so an answer that stays in chat is lost.

**Take the next item number from the highest one in the bank, never from the
question list.** They do not line up: the bank also holds extras she adds by
hand, such as item 16 on 2026-09-30 ("They were told exactly which entrance.
They still used the wrong one."), which answers no daily question. On
2026-09-30 the bank ran 1-16, so the next item was 17 while only three daily
questions had been answered. As of 2026-10-04 it runs **1-24** (17-19 came from
her 2007 internship paper; 20-22 from her Oct 4 budget answer; 23-24 from her
Oct 4 site-visit answer), so the next new item is 25.

**One answer can be several items.** Her Oct 4 answer to "the most common
reason an event budget goes over" named three distinct causes — no contingency
line, an unpriced rain plan, and year-on-year inflation — and she said so
herself: "could actually lead into 3 pieces of content". Each became its own
numbered item rather than one crowded entry, because the bank is a source of
individual pieces. Mark the question answered with the range (items 20-22).

The same happened again that day: her site-visit answer gave a firewall
question and, filed under "other", hidden venue fees — items 23 and 24. **Her
"other" items are bank material too**, even when they do not answer the
question asked.

**Check which questions are already marked answered before asking.** The Oct 1,
2 and 3 questions were all answered on Sep 30 in one sitting, so on Oct 2 the
next unanswered one was **Sun 4 Oct** — the one she asked to be given on
Sunday. A day whose question is already answered has nothing to ask.

## Finished cuts go to Google Drive (from 2026-10-01)

Her idea, so she stops saving cuts to a hard drive. **Both cuts of every piece
are uploaded to Drive once they are pushed**, as part of finishing the build —
not something to be asked for.

Structure, set by the author on 2026-10-01: a month folder holding **one
subfolder per day**.

| | |
| --- | --- |
| Parent | `AI for Event Planners — Reels`, id `1GFs9qwlVHq6Pdo0LEX0TG5lFN4ipmtax` |
| Month | `October`, id `1gCWHchI1_mvS7eQiQmGDlp6H8P8i59Qg` |
| Days | `October 1` … `October 14` exist; create the rest as the schedule reaches them |
| Naming | `YYYY-MM-DD-slug-instagram.mp4` and `-tiktok.mp4` |

`October 1` is `1I9q3H4T29ZoMeDt72CYik_ck-oqxhDzG`. Day folder ids are not
listed here beyond that — look them up with `GOOGLEDRIVE_FIND_FOLDER` under
the month folder, since Drive allows duplicate names and the id is what
matters.

At the start of each month, create the month folder under the parent and its
day subfolders, and record the month id here.

**Use `GOOGLEDRIVE_UPLOAD_FROM_URL`** (Composio, account
`googledrive_hasty-charer`) with the cut's `raw.githubusercontent.com` URL —
the same one Meta fetches from. Drive pulls it server-side, so no bytes pass
through the session. Push to the repo first, or the URL will not resolve.

**Its field names are `source_url`, `name` and `parent_folder_id`** — not
`file_url`, and not `parent_id`. On 2026-10-04 `parent_id` was passed and
**silently ignored**: the call reported success and the file landed in the root
of My Drive instead of the day folder. A wrong `source_url`/`name` fails loudly;
a wrong parent does not. **Check `parents` in the response against the folder id
you asked for**, not just `size`. The stray copy was trashed and the file
re-uploaded.

**Do not use the inline-upload route for video.** Both the native Drive
connector's `create_file` and Composio's `GOOGLEDRIVE_UPLOAD_FILE` take the
bytes inside the call: base64 adds a third, so a 6.8 MB cut becomes 9.1 M
characters, and `GOOGLEDRIVE_UPLOAD_FILE` caps at 5 MB anyway. Every finished
cut so far is larger than that.

Verify by comparing the returned `size` to the local file. Started 2026-10-01
with the vendor quotes pair, both exact.

## Render rules

- **1080x1920, ratio exactly 0.5625.** Verify with ffprobe before calling an
  export finished; never leave raw screen-recording dimensions.
- **Compute the crop from the source, don't reuse numbers.** Height =
  width / 0.5625, and set the y-offset so the status bar and the red
  recording dot fall off the top while the ChatGPT input bar stays at the
  bottom, where the platform UI covers it anyway. A y-offset of 0 leaves
  the recording dot in frame. For the usual 1206x2622 iPhone capture that
  is **`crop=1206:2144:0:478`** — 478 off the top, nothing off the bottom.
  Those numbers hold only for a 1206-wide source; a different device
  silently breaks them, so recompute when the capture size changes. The
  guide's duplicate `:0:0` rule was deleted on 2026-09-21, so this is now
  the only crop rule — but it is still compute-from-source, not a fixed
  string to paste blindly.
- 30 fps out, H.264 high, CRF 19, `+faststart`, AAC 192k at 48 kHz.
- **Voiceover to -14 LUFS.** Measure the source with a loudnorm first pass
  and feed the measured values back in, rather than a single dynamic pass.
- The screen recordings carry a silent audio track. The voiceover is the
  only audio.
- **Generate both voiceovers here — standing instruction from 2026-09-24.**
  The author used to record the Instagram one herself and leave the TikTok
  one to this session; she asked for both to be generated from now on. Use
  ElevenLabs, voice "Vanessa - Beach Girl" (`8DzKSPdgEQPaK5vKG0Rs`). Neither
  script depends on the footage, so both can be made as soon as the day's
  script is settled, before the recording exists.
- **Check the day's script length before generating.** The guide's per-day
  scripts have twice run short for a 40-50s day — 66 words on Sep 24 and 64
  on Sep 26, about 25s, which would leave ~20s of silence. Target roughly
  2.55 words per second of finished cut and extend the script by narrating
  what the output actually shows, as the Sep 24 rewrite did.

## Timing rules

- **Everything is 15-20s from Oct 1.** The October plan sets one target for
  every piece. A day's brief still overrides it, but no piece is long by
  default any more.
- **The length test is over — it measured nothing.** It ran Sep 23-30 on
  named days (short: 23, 25, 29; long: 24, 26, 30) and the October plan
  dropped it: short days averaged 25 views and long days 23, but both sat
  inside a decline that halved reach mid-test, so the comparison is
  worthless. At three Instagram posts a week it would be three against
  three, which is not enough either. Recorded so it is not re-run in the
  belief it was never tried.
- **The 6-second payoff ceiling was never part of the length test** and is
  unaffected by dropping it. It applies to every piece at every duration.
- **Time to payoff must stay under 6 seconds** — everything before the
  reveal, combined. This is a hard ceiling from real watch-time data and is
  the rule most often missed. The Sep 12 reel shipped at 6.5s and broke it.
- The generating section needs a **visible beat of 2.5-3s minimum**, sped
  to 2-3x, about 4 seconds. **This is what gets sacrificed first when the
  setup is crowded, and it shows.** On Sep 29 a four-beat setup - prompt,
  lawn plan, empty hall, generating - left each beat about a second under
  the 6-second ceiling, and the author said the piece "flips to the rain
  plan floorplan way too fast". The fix is to drop a setup beat, not to
  shave the generating one: three beats at a readable speed beat four
  flashing past. Check what the reveal itself already says before keeping a
  setup shot - that day's diagram was captioned with the indoor dimensions,
  so the empty-hall shot was redundant.
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
- **Build the TikTok cut first.** Round 6 briefs say so outright: TikTok is
  the primary discovery platform now, so its cut is not a derivative of the
  Instagram one.
- Footage in motion from frame one. **Never open on a static title card.**
- Only two text overlays: the hook at 0:00-0:02 and the end card. **No
  rolling mid-video captions** — transcription-synced captions were tested
  and made retention worse.
- **Round 6 (Sep 23-30) dropped the end card**: every brief in it said "end on
  the output itself, not an end card asking for a comment". The October
  plan's six Instagram briefs continue this — each specifies a hook overlay
  at 0:00-0:02 and nothing else — and its five TikTok-only quick pieces say
  "no hook line, no end card" outright. The two-overlay rule is the written
  default; in practice every current brief overrides it down to one.
- **Never post both cuts to the same platform** — near-identical posts
  split engagement.
- Hooks must name a concrete scenario, number or timeframe immediately.
  Abstract superlatives and vague teases both measured badly.
- Prefer broader "event" framing in the opening hook line even when the
  demo content is sector-specific ("a $85,000 event just wrapped", not "a
  $85,000 corporate summit"). Say "event planner", not "wedding planner",
  in general self-identification. Neither overrides genuinely
  wedding-specific content, hashtags or research scope.
- **Transformation is a hypothesis, not the house format** (downgraded by the
  October plan, 2026-09-28). A messy real input visibly becoming a structured
  output on screen. It was written in on 2026-09-20 off three posts — 83, 110
  and 155 reach — and every transformation piece since has gone 28, 19, 16,
  13, 8. The pattern did not hold. Keep making them, because they are good
  pieces, but **stop treating the format as the explanation for anything**,
  and do not enforce a quota of them.
- **The build-story format is the one being tested now.** The best Instagram
  post of the week by a distance was the coloring book build story — 90 views,
  79 reach, against a weekly average of 29. Not a demo: a personal, honest
  account of making something, including what went wrong. Oct 7 ("The one
  thing I stopped using AI for") is the piece that tests whether it repeats.
- **No more than two wedding-specific pieces in any seven.** The account is
  "event planner", and Round 5 drifted to four weddings in a row.
- Use only the author's uploaded footage. No stock, no generated visuals.
  Their own output files (a floor plan PNG, say) are fine when they send one.

## Posting

**Cadence from Oct 1 (October plan, written 2026-09-28).** Daily Instagram
posting is over.

| | Frequency | Days |
| --- | --- | --- |
| Instagram | **3 a week** | Mon, Wed, Fri — plus Thu Oct 1 to start |

**The guide's day-by-day table governs, not the Mon/Wed/Fri shorthand.** Week
one is Thu 1, Sat 3, Mon 5, Wed 7 — so **Fri 2 Oct has no Instagram Reel at
all**, and Sat 3 is an extra single photo (the Future of AI pinned post), which
the guide says is placed on a Saturday precisely so it does not take a
Mon/Wed/Fri slot. Read the day's row before assuming a weekday is a posting
day.
| TikTok | daily | every day |
| Facebook | whatever this session posts | automatic |
| Pinterest | 2 pins a day | from Fri Oct 2 |

Why: Instagram reach fell every day of the week to Sep 28 — 79, 38, 28, 19,
16, 13, 8, averaging 29 against 53 the week before. Five weeks of daily
posting with almost no engagement is the likeliest cause. TikTok over the
same week averaged 77 views and grew 62 to 73 followers against Instagram's
281 to 284: twice the reach and three times the growth on a quarter of the
base.

**This is a test with a decision point, and the author is hesitant about it.**
The number that matters is **total weekly Instagram reach, not reach per
post** — three posts reaching 250 beats seven reaching 200. Decision on **Wed
14 Oct**.

**The decision rule is pre-registered in
[`docs/OCT-CADENCE-TEST.md`](docs/OCT-CADENCE-TEST.md)** — written 2026-09-30,
before any data existed, because the plan says "if reach has not improved"
without saying improved against what, and the two candidate baselines (201 and
371) are not equivalent tests. Read that file on Oct 14 rather than
re-deciding what counts as a pass. Two things it fixes that are easy to get
wrong: the baseline is **201**, and the metric is Instagram's **deduplicated
weekly accounts reached**, never the sum of per-post reach.

Honest caveat worth repeating rather than burying: reach was already sliding
before the change, so a recovery cannot be cleanly attributed to posting less.

**Facebook cannot be measured at all.** It deprecated reach and impressions
in its API in November 2025, it has 7 followers, and every reaction on every
post is the author's own. Keep posting there because it costs nothing —
but **do not report on it** and do not spend manual time on it.

**Who posts what — the author restated this on 2026-09-24 and it has had to
be said more than once, so read it before assuming a piece is yours:**

| Goes out as | Who posts it |
| --- | --- |
| **Anything to TikTok** — the day's cut, the back catalogue, anything a brief calls a "repost to TikTok" | **The author.** Build the file, hand it over with its caption, never upload it. |
| **Anything that is a Trial Reel** | **The author.** Edited in the Claude.ai chat, uploaded with the in-app toggle. |
| Instagram feed Reels and Facebook | This session, after explicit approval. |
| An Instagram **repost** on a trial day | This session in principle — but ask first. Sep 27's was cancelled outright. |

The wording in a brief does not change this: what matters is the platform
and whether it is a trial, not how the line is phrased. **The author is
re-editing the guide as of 2026-09-24 because its Round 6 blocks are
confusing on exactly this point** — two reposts filed under one day, trial
and non-trial posts described in adjacent paragraphs. Until the new guide
lands, treat anything ambiguous about a second post as hers and ask.

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
  `28308094898830663`. **The guide agrees as of the 2026-09-29 revision**,
  which also explains the discrepancy that ran from Sep 25 to Sep 28: the
  `17841441013925532` it used to carry is the legacy business-account ID
  that appears inside Insights URLs, and is not what you call the API with.
  Both numbers are real; only this one works. Create the container with `media_type: REELS` and
  `share_to_feed: true`, then publish with a generous `max_wait_seconds`.
  Containers are single-use; on a processing error build a new one.
- **Facebook** — Composio account `facebook_radius-iguana`, page_id
  `1233196746554445` ("The Event Planners AI"), now recorded in the guide
  too. Never blind-retry, it duplicates posts. It has taken three read-backs
  and about fifteen minutes to surface in the page feed on every day from
  Sep 25 to Sep 28; that is normal, not a failure.
- **TikTok is the main platform — and still a manual upload.** (138
  average views per video against Instagram's 53, on a fifth of the
  followers.) Composio cannot publish publicly to TikTok, so **hand over
  the TikTok cut every single day** and never attempt to post it. It is the
  platform that actually reaches people, so its cut is not an afterthought
  to the Instagram one.
- **The split, stated plainly (author, 2026-09-24): anything going to
  TikTok is hers.** Not just the day's TikTok cut — the back-catalogue
  uploads and every item a brief labels "repost to TikTok" too, whatever
  the wording. This session builds those files and hands them over with
  their captions; it never uploads one. **Reposts to Instagram are the
  opposite and do run from here** — the Sep 27 and Sep 28 repost days are
  the only case. So when a day's brief lists a second post, read which
  platform it names before assuming it is this session's work.
- Facebook has 7 followers and is not yet a platform. Still post there, but
  do not read anything into its numbers.
- **Facebook keeps the hashtags even on a trial day** (author, 2026-09-28:
  "Keep hashtags on Facebook"). A trial day's Instagram caption carries no
  hashtags, because a trial is kept off hashtag pages and tags do nothing
  there. That reasoning is Instagram-only. Facebook is never a trial, so it
  takes the ordinary caption - body, blank line, `AI Prompt: "..."`, blank
  line, hashtags - exactly as on any other day.
- **Trial Reels are manual: the Sep 27 and 28 trials do not come through
  here.** Both are planned Instagram trials, edited in the Claude.ai chat and
  uploaded by the author. **Do not post them.** If their content turns up in
  this session, stop and say so rather than building or publishing anything.
- **But each trial day also has a second post, and that one does come through
  here.** Sep 27 and 28 each carry an Instagram **repost** — Sep 3's vendor
  payment schedule and Sep 2's seating chart — posted as a normal feed Reel
  through Claude Code as usual.
  **Sep 27's was cancelled by the author on 2026-09-24** ("skip sunday all
  together"), after the distinction between the trial and the repost was
  put to her. Sep 27 therefore has nothing in it for this session. Sep 28's
  repost has not been cancelled, but do not assume it is on either — ask
  before building it. A trial reaches only non-followers, so on a
  trial day the 280 followers see nothing in feed and nothing lands on the
  grid; the repost reaches a separate audience and the two do not compete.
  **Re-export the file rather than re-using the original byte for byte**, or
  duplicate detection can throttle both copies, and space it several hours
  from the trial upload.
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

- **Prompt pieces end: "Prompt below."** Shortened guide-wide on 2026-09-28:
  the previous wording, "The full prompt is in the caption below", appeared
  18 times in the Sep 27 guide and zero times in the Sep 28 one, replaced by
  "Prompt below" in all 16 places. The standing-rules line was changed to
  match, so this is a deliberate edit rather than drift. The point is
  unchanged - the AI prompt sits in the caption body, so the piece is
  self-contained without the video. **Captions already published keep their
  original wording**; do not go back and edit live posts.
- **"link in bio" is available again from 2026-09-28** and is still only for
  **downloadable files**. It was blocked while the bio pointed at the single
  tablecloth product; the bio now points at the Gumroad profile page,
  `aiforeventplanners.gumroad.com`, which holds them. Prompt pieces — most
  of the schedule — still end "Prompt below." instead, because the prompt is
  already in the caption body and there is nothing to download.

The guide keeps the old keyword list as a record of what was tried, so the
mechanic is not reintroduced without knowing it already failed nine times.

**What has actually gone up on TikTok is tracked in
[`docs/TIKTOK-POSTED.md`](docs/TIKTOK-POSTED.md), not in a schedule line.**
Uploads are hers and nothing reports back, so a day's plan records only what was
*meant* to run. On 2026-10-04 two pieces were offered to her as unposted on the
strength of repo notes and both were already live. She now sends one line when
she uploads; record it there, and **never call a piece unposted without checking
that file.**

## TikTok back catalogue (added to the guide 2026-09-23, corrected same day)

**12 of 39** Instagram pieces have never been posted to TikTok, verified
against the full 31-video TikTok catalogue. These are **not reposts** — the
TikTok audience has genuinely not seen them. One goes up per day as a second
post alongside that day's scheduled piece. All manual uploads, so they never
publish from here.

Most of the twelve are carousels: TikTok did not support carousels when they
ran, so they had nowhere to go. That changed, and the first TikTok carousel
went up on Sep 22, which is what makes the backlog postable at all.

- **`#theeventplannerai` is dead** — it points at an account name that no
  longer exists. Swap it for `#aiforeventplanners` wherever the old handle
  appears in the original caption.
- Strip any comment-to-unlock CTA. The Sep 13 centerpieces caption still has
  one. Open questions ("what's the pettiest seating conflict you've had?")
  stay — those are conversation prompts, not a keyword gate.
- Excluded on purpose: the Aug 23 poll carousel (it points at a Story poll
  that no longer exists) and the Aug 30 tablecloth carousel (the
  swipe-to-zoom version of the same content went to TikTok on Sep 22).
- Three links in the guide are still placeholders — the Sep 8 photography
  carousel, the Sep 14 floor plan and the Sep 20 vendor contract. Find them
  on the profile grid by date.
- **The back catalogue ends Sat 3 Oct.** The October plan schedules the last
  three: Sep 14 floor plan (Thu 1, strip the retired LAYOUT keyword), Sep 20
  vendor contract (Fri 2, strip REVIEW), Sep 22 coloring book build story
  (Sat 3). After that every TikTok day is either an Instagram piece's cut or
  one of the five TikTok-only quick pieces.
  **All three are now up** (author, 2026-10-05: "All are posted"), so the back
  catalogue is finished and nothing is left in it.
- **Not to Instagram, not yet.** A second Instagram feed post competes with
  that day's main post for the same small pool of reach. Followers went 271
  to 280 over the fortnight these ran, so the same people would simply see it
  twice. Revisit when the count has roughly doubled.

**How the first version of this list got it wrong**, recorded because the
failure mode is easy to repeat: it listed 15 pieces and 11 of them were
wrong. The TikTok list endpoint returns 20 videos per page and the second
page was never fetched, so the catalogue was incomplete; the "missing" list
was then built by fuzzy word-overlap against captions of very different
lengths. Page the endpoint to the end, and match on something stronger than
word overlap.

## The paid guide and the four templates (added 2026-09-24)

`@_eventguide` — the account whose awards-night post was the model for the
comment-to-unlock experiment — has launched a paid product for the same
audience: a per-event Claude project setup, four document templates, prompt
workflows and instructions.

**The four document templates are the blocker.** Event brief, project plan,
budget, run of show — the four Sahiba actually works from, named Sep 8 and
still unbuilt. Two things wait on them: the Round 6 awards-night piece
promises the pack as its deliverable, and any paid guide would be built
around them.

## Pinterest (added to the guide 2026-09-28, started 2026-09-29)

A separate account and a separate workstream: `@calmbeforetheaisle`, business
account, for the coloring book only. Nothing to do with `@aiforeventplanners`.
**Full working detail is in [`pinterest/README.md`](pinterest/README.md)** —
board ids, the Drive folder, the schedule CSV. The parts that govern:

- **Two pins a day, never a batch.** Twelve at once on a new account reads as
  automated. Two a day for a fortnight takes it from 6 pins to about 30,
  which is the minimum volume Pinterest responds to.
- **It does not need this repo.** `PINTEREST_CREATE_PIN` takes the image bytes
  via `media_source image_base64`, so there is no push-then-fetch step the way
  Instagram and Facebook have. Composio account `pinterest_reking-alpha`.
- **Pin creation works; pin editing does not.** `PINTEREST_UPDATE_PIN` returns
  "does not have access to this restricted feature: `pin_edit`". That is the
  app's access tier, not anything session-specific, so a wrong board or a
  typo is permanent. **Check every argument before the call, not after.** The
  guide's worry that trial-level access would block creation outright was
  tested on 2026-09-29 and did not happen.
- **Outbound clicks is the only number that matters.** Baseline over two
  weeks: 137 impressions, 16 pin clicks, **0 saves, 0 outbound clicks** — and
  133 of the 137 impressions landed on one day, Sep 22, Pinterest's initial
  distribution test. The creative is fine (11.7% tap rate). Nobody clicks
  through, which points at the descriptions; and nobody saves, which matters
  more than it sounds, because **on Pinterest saves are distribution**, so a
  pin with no saves never gets redistributed.
- **No ad spend.** Paying for impressions at a zero outbound-click rate buys
  a larger version of zero. The threshold for revisiting is one organic
  outbound click.
- Review **Tue 14 Oct**. If outbound clicks are still zero after ~30 pins
  across four boards, the problem is the offer or the price rather than the
  marketing, and Pinterest goes on the back burner rather than getting money.
- Links carry `?utm_source=pinterest&utm_medium=social&utm_campaign=<sampler
  |book>&utm_content=<file stem>`. `campaign` is the product, because the
  question worth answering is whether the 99c sampler beats the $5.99 book.
  **The guide says the tag makes traffic "identifiable in Etsy's own stats"
  and that is wrong** — Etsy reports "Pinterest" as a source and nothing
  finer. The author knew and kept the tags anyway: they cost nothing and
  become readable if pins ever point at Gumroad or an owned page.

## Practical gotchas

- **Aim for ~25 seconds of raw footage per recording.** That gives enough
  generating time to compress into a real 3-4 second ramp and enough reveal
  to fill the hold at natural speed. Shorter sources (~12-13s) force
  tradeoffs across duration, ramp and pacing at once.
- **The upload ceiling is ~30 MB, NOT a number of seconds.** Measured
  across every clip uploaded this month: the largest that succeeded was
  29.7 MB, and source bitrates range from **0.96 to 2.68 MB/s - nearly
  3x**. So a duration rule is actively misleading. At ~25 MB:
  screen recordings (1.0-2.1 MB/s) give 12-25s; camera video in HEVC
  (~2.6 MB/s) gives only **9-10s**. Always quote a size, and work out the
  seconds from that clip's own bitrate.
- **Never route uploads through email.** Mail attachment caps are
  typically 25 MB - *tighter* than the chat's ~30 MB - so a clip that
  would have uploaded fine gets bounced, sliced smaller, and bounced
  again. Sending from the phone straight into the chat removes both the
  round trip and the tighter limit.
- Shooting at **1080p/30** rather than 4K/60 roughly halves the camera
  bitrate, and a 1080x1920 30fps Reel discards the extra anyway.
- When clips do need splitting, ask for overlapping takes saved with
  "Save as New Clip". Frame-match the overlap to find the seam, then
  concatenate.
- **Uploads must be sent at "Actual"/"Original" size.** The default
  compressed size produces visibly soft footage.
- **Google Drive works here, and not in the Claude.ai chat.** That is the
  distinction the 2026-09-29 guide revision drew, and it explains the old
  "blocked" note: the Claude.ai chat has no Drive tools and an allowlisted
  network, so files for *that* chat must still be uploaded directly, while
  Claude Code can fetch from Drive freely. The author changed this session's
  network policy on 2026-09-24 and it has been used daily since.
  Download with
  `https://drive.usercontent.google.com/download?id=<FILE_ID>&export=download&confirm=t`.
  The file must be shared **"Anyone with the link - Viewer"**; a
  Restricted file returns a Google sign-in HTML page, not the video, and
  `curl` will happily save that page as an .mp4. Check the response is
  `content-type: video/mp4` before trusting it.
  **This retires the ~30 MB ceiling for anything routed through Drive** -
  the first file this way was 40.6 MB, well past what the chat takes. So
  no more splitting a clip into overlapping takes, and no more seam
  matching, unless the author prefers the chat. Send full-length
  recordings via Drive.
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
- **Ad-check the finished export, over the whole frame — not a crop of the
  source.** On 2026-09-24 a bottom-620px crop of the raw clip read clean at
  the chosen cut point, and the exported reel still carried the ad's lead
  line on its last frame: once the 2144-tall crop is scaled to 1920 that
  source crop stops about 20px short of the frame bottom. Scan the bottom
  ~300px of the actual mp4 through to its final frame. A crop that misses the
  last few rows gives the same false all-clear a colour threshold does.
- **Ads seen so far are not one banner**: Adobe Acrobat (Sep 21), Adobe
  Firefly (Sep 22), Rillion "AI for Accounts Payable" (Sep 23), Cambridge
  "Event Florals in NYC" (Sep 24), Turning Stone "Make It Easier" (Sep 25).
  Five advertisers in five days. Do not search for a known logo — look for
  anything new at the bottom of the reveal.
- **"Save as New Clip" splits are not always frame-matchable.** On 2026-09-24
  three clips of the same answer turned out to be separate scroll passes: best
  whole-frame match across the overlaps was MAD 13.4 and 18.6, and last-frame
  to first-frame 21.0 and 17.7 against a control of 28.2 — no true match
  anywhere. That is not a blocker. A dense page of text throws a large MAD for
  even a one-line scroll offset, so check contiguity by **reading the text**
  at each boundary instead; a seam of a line or two reads as ordinary
  scrolling.
- The recording is supposed to start with the prompt sitting in the input
  box and the send tap on camera. Three recordings have begun after the tap
  (the third on Sep 25, where the author said to run with it). Flag it
  rather than faking an opening. **But check before assuming it is missing
  again** - the Sep 29 recording opened exactly right, prompt in the box with
  all three files attached and the tap at ~0.7s, and the first build started
  at 7.00s and threw it away. The author spotted it: "Why is the ChatGPT
  prompt not the first thing we see". Look at the first two seconds of every
  source before choosing a cold open.
- **The hook card's usual y=620 is not automatic.** It is placed to avoid
  whatever the frame is showing at 0:00-0:02, and that changes per day: on
  Sep 23 it covered the send button at y880 and moved to 620; on Sep 29 it
  landed on the prompt text - the one thing that opening exists to show - and
  moved to **y=1300**, which sits over the keyboard, carries no information,
  and still clears Instagram's own bottom furniture. Look at the opening
  frames, then pick the y.
- **A single-frame PNG overlay needs `repeatlast=1`.** Feeding a hook card
  straight into `overlay` with `eof_action=pass:repeatlast=0` shows it on
  frame one and then drops it — the Sep 25 first build shipped with no hook
  at all and the filtergraph looked correct. Use
  `eof_action=repeat:repeatlast=1` with an `enable=between(t,0,2)` window,
  and **verify the hook on the exported frames**, never from the command.
  (The Sep 26 script builds the card as a timed stream instead, which is
  also fine — that export was checked and does render.)
- **`alimiter` undoes its own limiting unless you pass `level=0`.** Its
  `level` option (auto level) defaults to true and renormalises the output
  back to full scale, so the audio clips at 0.0 dBFS however low `limit` is
  set. This looks exactly like the limiter not working.
- **`loudnorm` cannot always reach -14 LUFS.** When a voiceover's crest
  factor is high the filter's true-peak ceiling binds first: on Sep 25 the
  measured two-pass result stalled at -15.8 LUFS with TP pinned to -1.5, and
  raising the offset moved it 0.6 dB. When that happens, apply the gain
  explicitly and let `alimiter` (with `level=0`) catch the peaks. Still take
  the first-pass measurement — it is what the gain is computed from. Always
  confirm by measuring the finished export.
